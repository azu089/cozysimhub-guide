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
const style = fs.readFileSync(path.join(root, "templates", "style.css"), "utf8");
const moonStyle = fs.readFileSync(path.join(root, "templates", "style-moon.css"), "utf8");

function inspect(html) {
  const failures = [];
  if (!html.includes('<link rel="icon" href="/favicon.svg" type="image/svg+xml" />') ||
      !html.includes('<link rel="icon" href="/favicon-32x32.png" sizes="32x32" type="image/png" />') ||
      !html.includes('<link rel="apple-touch-icon" href="/apple-touch-icon.png" />')) failures.push("favicon-head-links");
  if (html.includes('class="tome-nav"')) {
    if (!html.includes('id="sovereign-navigation" class="tome-nav"')) failures.push("sovereign-nav-id");
    if (!html.includes('aria-controls="sovereign-navigation" aria-expanded="false"')) failures.push("sovereign-toggle-aria");
    if (!html.includes("function setNavigation(open, returnFocus)") || !html.includes("setNavigation(false, true)")) failures.push("sovereign-close-sync");
    if (!html.includes("e.key === 'Escape' && nav.classList.contains('open')")) failures.push("sovereign-escape");
  }
  if (html.includes('class="moon-nav"')) {
    if (!html.includes('id="moonlight-navigation" class="moon-nav"')) failures.push("moon-nav-id");
    if (!html.includes('aria-controls="moonlight-navigation" aria-expanded="false"')) failures.push("moon-toggle-aria");
    if (!html.includes("function setMoonNavigation(open, returnFocus)") || !html.includes("setMoonNavigation(false,true)")) failures.push("moon-close-sync");
    if (!html.includes("e.key==='Escape'&&nav.classList.contains('open')")) failures.push("moon-escape");
  }
  return failures;
}

assert.equal(htmlFiles.length, 529, "generated HTML inventory changed");
for (const file of htmlFiles)
  assert.deepEqual(inspect(fs.readFileSync(file, "utf8")), [], `navigation contract failed in ${path.relative(publicDir, file)}`);

const assets = [
  ["favicon.svg", null], ["favicon-16x16.png", [16, 16]], ["favicon-32x32.png", [32, 32]], ["apple-touch-icon.png", [180, 180]],
];
for (const [name, dimensions] of assets) {
  const file = path.join(root, "assets", name);
  assert(fs.existsSync(file) && fs.statSync(file).size > 0, `missing favicon asset ${name}`);
  if (dimensions) {
    const data = fs.readFileSync(file);
    assert.equal(data.toString("hex", 1, 4), "504e47", `${name} is not PNG`);
    assert.deepEqual([data.readUInt32BE(16), data.readUInt32BE(20)], dimensions, `${name} dimensions drifted`);
  }
  assert(fs.existsSync(path.join(publicDir, name)), `favicon output missing ${name}`);
}
assert(/\.tome-nav-toggle\s*\{[^}]*padding:\s*14px 16px/s.test(style), "Sovereign toggle 44px target contract missing");
assert(/\.tome-chapter a\s*\{[^}]*min-height:\s*44px/s.test(style), "Sovereign navigation target contract missing");
assert(/\.moon-nav-toggle\{[^}]*padding:8px 10px/s.test(moonStyle), "Moonlight toggle target contract missing");
assert(/\.moon-nav-item\{[^}]*min-height:44px/s.test(moonStyle), "Moonlight navigation target contract missing");
assert(/\.privacy-settings[\s\S]*?min-height:\s*44px/.test(style), "privacy settings target contract missing");

const sovereign = fs.readFileSync(path.join(publicDir, "index.html"), "utf8");
const moon = fs.readFileSync(path.join(publicDir, "moonlight-peaks.html"), "utf8");
const faults = [
  [sovereign.replace('id="sovereign-navigation"', 'id="broken-navigation"'), "sovereign-nav-id"],
  [sovereign.replace('aria-controls="sovereign-navigation"', 'aria-controls="broken-navigation"'), "sovereign-toggle-aria"],
  [sovereign.replaceAll("setNavigation(false, true)", "setNavigation(false, false)"), "sovereign-close-sync"],
  [sovereign.replace("e.key === 'Escape'", "e.key === 'Enter'"), "sovereign-escape"],
  [moon.replace('id="moonlight-navigation"', 'id="broken-navigation"'), "moon-nav-id"],
  [moon.replace('aria-controls="moonlight-navigation"', 'aria-controls="broken-navigation"'), "moon-toggle-aria"],
  [moon.replaceAll("setMoonNavigation(false,true)", "setMoonNavigation(false,false)"), "moon-close-sync"],
  [sovereign.replace('/favicon.svg', '/missing-favicon.svg'), "favicon-head-links"],
];
for (const [html, expected] of faults)
  assert(inspect(html).includes(expected), `negative fault was not caught: ${expected}`);

console.log(JSON.stringify({
  status: "pass",
  pages: htmlFiles.length,
  navigationSystems: ["sovereign-tower", "moonlight-peaks"],
  staticWidths: [375, 1440],
  targetMinPx: 44,
  escapeFocusReturn: true,
  faviconAssets: assets.length,
  negativeFaults: faults.length,
}, null, 2));
