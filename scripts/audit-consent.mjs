#!/usr/bin/env node
import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const publicDir = path.join(root, "public");
const walk = dir => fs.readdirSync(dir, { withFileTypes: true }).flatMap(entry =>
  entry.isDirectory() ? walk(path.join(dir, entry.name)) : [path.join(dir, entry.name)]).sort();
const htmlFiles = walk(publicDir).filter(file => file.endsWith(".html"));
const providerTag = /<script[^>]+src=["'][^"']*(?:googletagmanager\.com|googlesyndication\.com|effectivecpmnetwork\.com)[^"']*["'][^>]*>/i;

function inspect(html) {
  const failures = [];
  if (providerTag.test(html)) failures.push("pre-consent-provider");
  if (!html.includes("data-consent-reject")) failures.push("missing-reject");
  if (!html.includes("data-consent-settings")) failures.push("missing-settings");
  if (!html.includes("data-consent-withdraw")) failures.push("missing-withdraw");
  if (!html.includes("dialog.showModal()")) failures.push("nonmodal-dialog");
  if (!html.includes("loaded={analytics:false,adsense:false,adsterra:false}")) failures.push("non-fail-closed-state");
  if (!html.includes('save({analytics:false,advertising:false})')) failures.push("withdrawal-or-reject-drift");
  if (!html.includes('key="cozysimhub-consent-v1"')) failures.push("missing-local-preference-key");
  if (!html.includes('dialog.addEventListener("cancel"')) failures.push("missing-escape-focus-return");
  if (!html.includes('aria-controls="privacy-consent-dialog"') || !html.includes('aria-expanded="false"')) failures.push("settings-aria-drift");
  return failures;
}

assert.equal(htmlFiles.length, 529, "generated HTML inventory changed");
for (const file of htmlFiles) {
  const html = fs.readFileSync(file, "utf8");
  assert.deepEqual(inspect(html), [], `consent contract failed in ${path.relative(publicDir, file)}`);
}

const localeRoots = ["", "zh-CN", "ja", "ko", "fr", "de"];
const privacyMarkers = [
  "Before you choose", "在您作出选择前", "選択前に", "선택 전에는", "Avant votre choix", "Vor Ihrer Auswahl",
];
localeRoots.forEach((locale, index) => {
  const base = locale ? path.join(publicDir, locale) : publicDir;
  const home = fs.readFileSync(path.join(base, "index.html"), "utf8");
  const privacy = fs.readFileSync(path.join(base, "privacy.html"), "utf8");
  for (const token of ["data-consent-accept", "data-consent-reject", "data-consent-manage-open", "data-consent-save", "data-consent-withdraw"])
    assert(home.includes(token), `${locale || "en"} missing ${token}`);
  assert(privacy.includes(privacyMarkers[index]), `${locale || "en"} privacy copy is incomplete`);
  assert(privacy.includes("cozysimhub-consent-v1"), `${locale || "en"} privacy storage boundary missing`);
});

const baseline = fs.readFileSync(path.join(publicDir, "index.html"), "utf8");
const faults = [
  [baseline.replaceAll("data-consent-reject", "data-broken-reject"), "missing-reject"],
  [baseline.replaceAll("data-consent-settings", "data-broken-settings"), "missing-settings"],
  [baseline.replaceAll("data-consent-withdraw", "data-broken-withdraw"), "missing-withdraw"],
  [baseline.replace("</head>", '<script src="https://www.googletagmanager.com/gtag/js?id=fault"></script></head>'), "pre-consent-provider"],
  [baseline.replaceAll("dialog.showModal()", "dialog.show()"), "nonmodal-dialog"],
  [baseline.replace("loaded={analytics:false", "loaded={analytics:true"), "non-fail-closed-state"],
  [baseline.replaceAll('save({analytics:false,advertising:false})', 'save({analytics:true,advertising:true})'), "withdrawal-or-reject-drift"],
  [baseline.replaceAll('aria-controls="privacy-consent-dialog"', 'aria-controls="broken-dialog"'), "settings-aria-drift"],
];
for (const [html, expected] of faults)
  assert(inspect(html).includes(expected), `negative fault was not caught: ${expected}`);

console.log(JSON.stringify({
  status: "pass",
  pages: htmlFiles.length,
  locales: localeRoots.length,
  defaultProviderScriptTags: 0,
  controls: ["accept", "reject", "manage", "save", "withdraw"],
  negativeFaults: faults.length,
}, null, 2));
