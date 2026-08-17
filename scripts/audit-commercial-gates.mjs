#!/usr/bin/env node
import assert from "node:assert/strict";
import crypto from "node:crypto";
import fs from "node:fs";
import path from "node:path";
import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const publicDir = path.join(root, "public");
const sitePath = path.join(root, "data", "site.json");
const basePath = path.join(root, "data", "site.base.json");
const generatorPath = path.join(root, "scripts", "generate.js");
const expectedPublisher = "pub-4174270222899193";
const expectedClient = `ca-${expectedPublisher}`;
const expectedAmazon = {
  modulePages: 337,
  modules: 337,
  tagOccurrences: 1685,
  urls: 1685,
  disclosures: 337,
  disclosureSha256: "61a91f292da1e39c8ba6da57b42dcecec4233d3b70f82675d32a265c8cd10ca4",
  shapeSha256: "aefb6de346ba44e2caf0558f53843a0ceffe2cd33bdb0550088ea81ca5ed888e",
};

const readJson = file => JSON.parse(fs.readFileSync(file, "utf8"));
const count = (text, needle) => text.split(needle).length - 1;
const filesUnder = dir => fs.readdirSync(dir, { withFileTypes: true })
  .flatMap(entry => entry.isDirectory()
    ? filesUnder(path.join(dir, entry.name))
    : [path.join(dir, entry.name)])
  .sort();
const htmlFiles = () => filesUnder(publicDir).filter(file => file.endsWith(".html"));
const hashJson = value => crypto.createHash("sha256").update(JSON.stringify(value)).digest("hex");
const treeHash = () => {
  const hash = crypto.createHash("sha256");
  for (const file of filesUnder(publicDir)) {
    hash.update(path.relative(publicDir, file));
    hash.update("\0");
    hash.update(fs.readFileSync(file));
    hash.update("\0");
  }
  return hash.digest("hex");
};
const runBuild = fixture => {
  const env = { ...process.env };
  delete env.COZY_ADSENSE_FIXTURE;
  if (fixture) {
    env.NODE_ENV = "test";
    env.COZY_ADSENSE_FIXTURE = "enabled";
  }
  const result = spawnSync(process.execPath, [generatorPath], { cwd: root, env, encoding: "utf8" });
  assert.equal(result.status, 0, result.stderr || result.stdout || "generator failed");
  return result.stdout.trim();
};
const rows = () => htmlFiles().map(file => {
  const relative = path.relative(publicDir, file);
  const html = fs.readFileSync(file, "utf8");
  return {
    relative,
    html,
    amazonModules: count(html, 'class="amazon-gear"'),
    amazonTag: count(html, "cozysimhub20-20"),
    amazonUrls: count(html, "https://www.amazon.com/s?k="),
    disclosures: [...html.matchAll(/<p class="aff-note">([\s\S]*?)<\/p>/g)].map(match => match[1]),
  };
});
const amazonFingerprint = currentRows => ({
  modulePages: currentRows.filter(row => row.amazonModules > 0).length,
  modules: currentRows.reduce((sum, row) => sum + row.amazonModules, 0),
  tagOccurrences: currentRows.reduce((sum, row) => sum + row.amazonTag, 0),
  urls: currentRows.reduce((sum, row) => sum + row.amazonUrls, 0),
  disclosures: currentRows.reduce((sum, row) => sum + row.disclosures.length, 0),
  disclosureSha256: hashJson(currentRows.map(row => [row.relative, row.disclosures])),
  shapeSha256: hashJson(currentRows.map(row => [row.relative, row.amazonModules, row.amazonTag, row.amazonUrls])),
});
const sitemapFiles = () => {
  const xml = fs.readFileSync(path.join(publicDir, "sitemap.xml"), "utf8");
  return [...xml.matchAll(/<loc>https:\/\/[^/]+(\/[^<]*)<\/loc>/g)].map(match => {
    const route = match[1];
    const relative = route.endsWith("/")
      ? `${route.replace(/^\//, "")}index.html`
      : `${route.replace(/^\//, "")}.html`;
    return path.join(publicDir, relative);
  });
};
const assertOutput = ({ fixture }) => {
  const currentRows = rows();
  assert.deepEqual(amazonFingerprint(currentRows), expectedAmazon, "registered Cozy Amazon output changed");
  assert(currentRows.some(row => row.html.includes('class="colophon"')), "Sovereign Tower render path missing");
  assert(currentRows.some(row => row.html.includes('class="moon-colophon"')), "Moonlight Peaks render path missing");
  for (const row of currentRows) {
    const scripts = count(row.html, "pagead2.googlesyndication.com/pagead/js/adsbygoogle.js");
    assert.equal(scripts, fixture ? 1 : 0, `AdSense serving count mismatch in ${row.relative}`);
    assert.equal(row.html.includes("client=pub-"), false, `raw pub client leaked in ${row.relative}`);
    assert.equal(row.html.includes("client=ca-ca-pub-"), false, `double ca- prefix in ${row.relative}`);
    if (fixture) assert.equal(count(row.html, `client=${expectedClient}`), 1, `fixture client mismatch in ${row.relative}`);
    for (const token of ["data-consent-settings", "data-consent-accept", "data-consent-reject", "data-consent-withdraw"])
      assert(row.html.includes(token), `consent control ${token} missing in ${row.relative}`);
    assert.equal(/<script[^>]+src=["'][^"']*(?:googletagmanager\.com|googlesyndication\.com|effectivecpmnetwork\.com|\/invoke\.js)/i.test(row.html), false,
      `optional provider injected before consent in ${row.relative}`);
  }
  return { currentRows, amazon: amazonFingerprint(currentRows) };
};

const site = readJson(sitePath);
const base = readJson(basePath);
for (const config of [site.site, base.site]) {
  assert.equal(config.adsenseId, expectedPublisher, "AdSense publisher data must stay raw pub-");
  assert.deepEqual(config.adsenseServing, {
    enabled: false,
    providerReady: false,
    certifiedCmpReady: false,
  }, "all three production serving gates must default false");
}
assert.equal(site.site.languages.length, 6, "six-language configuration changed");

const firstDefaultBuild = runBuild(false);
const firstDefault = assertOutput({ fixture: false });
const firstDefaultHash = treeHash();
const indexableFiles = sitemapFiles();
assert.equal(indexableFiles.length, 498, "six-language route set changed");
for (const file of indexableFiles) {
  assert.equal(fs.existsSync(file), true, `missing indexable output ${path.relative(publicDir, file)}`);
  const html = fs.readFileSync(file, "utf8");
  assert.equal(count(html, `<meta name="google-adsense-account" content="${expectedClient}" />`), 1,
    `AdSense ownership meta count mismatch in ${path.relative(publicDir, file)}`);
}
assert.equal(fs.readFileSync(path.join(publicDir, "ads.txt"), "utf8"),
  `google.com, ${expectedPublisher}, DIRECT, f08c47fec0942fa0\n`, "ads.txt raw publisher record changed");

const secondDefaultBuild = runBuild(false);
assertOutput({ fixture: false });
assert.equal(treeHash(), firstDefaultHash, "two default builds are not byte-identical");

const firstFixtureBuild = runBuild(true);
assertOutput({ fixture: true });
const firstFixtureHash = treeHash();
const secondFixtureBuild = runBuild(true);
assertOutput({ fixture: true });
assert.equal(treeHash(), firstFixtureHash, "two enabled-fixture builds are not byte-identical");

runBuild(false);
assertOutput({ fixture: false });
assert.equal(treeHash(), firstDefaultHash, "fixture round-trip did not restore byte-identical default output");

console.log(JSON.stringify({
  status: "pass",
  locales: site.site.languages.length,
  pages: firstDefault.currentRows.length,
  indexablePages: indexableFiles.length,
  renderPaths: ["sovereign-tower", "moonlight-peaks"],
  defaultServingScripts: 0,
  fixtureScriptsPerPage: 1,
  publisherId: expectedPublisher,
  clientId: expectedClient,
  amazon: firstDefault.amazon,
  defaultTreeSha256: firstDefaultHash,
  fixtureTreeSha256: firstFixtureHash,
  builds: [firstDefaultBuild, secondDefaultBuild, firstFixtureBuild, secondFixtureBuild],
}, null, 2));
