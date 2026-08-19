#!/usr/bin/env node
/* CozySimHub 导航完整性审计 —— 布局重构后契约（cozy-layout-redesign-20260818-01）
   覆盖：顶部导航条（品牌 + 游戏下拉 + 全局语言 6 语 + 站内搜索 + 隐私）、
   左「当前游戏指南」侧栏（P1-03 每游戏数据源化回归）、右栏（TOC/相关/广告位）、
   移动端抽屉（关闭态 inert + 打开态焦点圈闭 + Escape 归还，P1-06）。 */
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
const ALL_LANG_NAMES = ["English", "简体中文", "日本語", "한국어", "Français", "Deutsch"];

/* 从相对路径识别页面所属游戏（去语言前缀后按 slug 前缀判定） */
const gameOfFile = relative => {
  const slug = relative.replace(/\.html$/, "").replace(/^(en|zh-CN|ja|ko|fr|de)\//, "");
  if (slug.startsWith("sovereign-tower")) return "sovereign-tower";
  if (slug.startsWith("moonlight-peaks")) return "moonlight-peaks";
  if (slug.startsWith("sandustry")) return "sandustry";
  return null;
};
const linksOf = (html, openTag) => {
  const block = (html.match(new RegExp(openTag + "[\\s\\S]*?<\\/nav>")) || [""])[0];
  return [...block.matchAll(/href="(\/[^"#?]*)"/g)].map(m => m[1]);
};
const footerLinksOf = (html, cls) => {
  const block = (html.match(new RegExp('class="' + cls + '"([\\s\\S]*?)<\\/div>')) || [""])[0];
  return [...block.matchAll(/href="(\/[^"#?]*)"/g)].map(m => m[1]);
};
/* 去语言前缀（/de/sovereign-tower/knights → /sovereign-tower/knights）后按游戏判定 */
const barePath = l => l.replace(/^\/(en|zh-CN|ja|ko|fr|de)\//, "/");
const gameOfLink = l => {
  if (l.startsWith("/sovereign-tower")) return "sovereign-tower";
  if (l.startsWith("/moonlight-peaks")) return "moonlight-peaks";
  if (l.startsWith("/sandustry")) return "sandustry";
  return null;
};
const escRe = s => s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
const cssRule = (css, sel) => {
  const m = css.match(new RegExp(escRe(sel) + "\\s*\\{([^}]*)\\}", "s"));
  return m ? m[1] : "";
};
const minHeightOf = rule => {
  const m = rule.match(/min-height:\s*([^;]+)/);
  if (!m) return 0;
  const v = m[1].trim();
  if (v === "var(--control-min)") return 44;
  const n = parseFloat(v);
  return Number.isFinite(n) ? n : 0;
};

function inspect(html, relative) {
  const failures = [];
  const game = gameOfFile(relative);
  if (!html.includes('<link rel="icon" href="/favicon.svg" type="image/svg+xml" />') ||
      !html.includes('<link rel="icon" href="/favicon-32x32.png" sizes="32x32" type="image/png" />') ||
      !html.includes('<link rel="apple-touch-icon" href="/apple-touch-icon.png" />')) failures.push("favicon-head-links");
  // 顶部导航条：品牌 + 游戏下拉 + 全局语言 + 站内搜索 + 隐私
  if (!html.includes('class="site-header"')) failures.push("site-header-missing");
  if (!html.includes('class="header-brand"')) failures.push("header-brand-missing");
  if (!html.includes('class="game-dd"')) failures.push("game-dd-missing");
  if (!html.includes('class="lang-dd"')) failures.push("lang-dd-missing");
  if (!html.includes('class="site-search"')) failures.push("site-search-missing");
  if (!html.includes('name="as_sitesearch"')) failures.push("search-sitesearch-missing");
  if (!/<form class="site-search"[^>]*action="https:\/\/www\.google\.com\/search"/.test(html)) failures.push("search-form-drift");
  if (!html.includes('data-consent-settings')) failures.push("privacy-settings-missing");
  // 全局语言：永远显示全部 6 语
  for (const name of ALL_LANG_NAMES) if (!html.includes(`<span class="lang-name">${name}</span>`)) failures.push("lang-list-incomplete");
  // 沙金工业 3 语白名单：可用语言为链接，其余置灰（unavailable ×2 份：顶栏 + 抽屉）
  const unavailableCount = (html.match(/class="lang-item unavailable"/g) || []).length;
  if (game === "sandustry" && unavailableCount > 0) failures.push("lang-unavailable-unexpected");
  if (game !== "sandustry" && unavailableCount > 0) failures.push("lang-unavailable-unexpected");
  // 抽屉（P1-06）：id + toggle aria + 关闭态 inert + 打开态焦点圈闭 + Escape 归还
  if (!html.includes('id="sovereign-navigation" class="tome-nav"')) failures.push("sovereign-nav-id");
  if (!html.includes('aria-controls="sovereign-navigation" aria-expanded="false"')) failures.push("sovereign-toggle-aria");
  if (!html.includes("function setNavigation(open, returnFocus)")) failures.push("sovereign-close-sync");
  if (!html.includes("setNavigation(false, true)")) failures.push("sovereign-close-sync");
  if (!html.includes("nav.setAttribute('inert'")) failures.push("drawer-inert-missing");
  if (!html.includes("/* drawer-focus-trap */")) failures.push("drawer-focus-trap-missing");
  if (!html.includes("e.key === 'Escape'")) failures.push("sovereign-escape");
  // 统一主题契约：月光页并入共享导航，不得残留独立 moon 骨架
  if (html.includes('class="moon-article"') || html.includes('class="moon-ruled"')) {
    if (html.includes('class="moon-nav"') || html.includes('class="moon-lang"') || html.includes('class="moon-head"')) failures.push("moon-chrome-remnant");
  }
  // 每游戏侧栏（P1-03）：tome-chapters 全部链接必须属于当前游戏
  if (game) {
    const chaptersLinks = linksOf(html, '<nav class="tome-chapters"').map(barePath);
    for (const l of chaptersLinks) {
      if (!l.startsWith("/" + game)) { failures.push("sidebar-cross-game"); break; }
    }
    if (chaptersLinks.length === 0) failures.push("sidebar-empty");
    // 页脚 key 链接同样按游戏路由（沙金页不再出现 ST/MP 导航；月光页不再出现 ST/SD）
    const footerLinks = footerLinksOf(html, "colophon-links").concat(footerLinksOf(html, "moon-colophon-links")).map(barePath);
    for (const l of footerLinks) {
      const lg = gameOfLink(l);
      if (lg && lg !== game) { failures.push("footer-cross-game"); break; }
    }
  }
  // 右栏：内容页（page-shell）必须带 TOC / 相关攻略 / 预留广告位
  if (html.includes('class="page-shell')) {
    if (!html.includes('class="page-folio')) failures.push("rail-missing");
    if (!html.includes('class="folio-toc"')) failures.push("rail-toc-missing");
    if (!html.includes('class="folio-related"')) failures.push("rail-related-missing");
    if (!html.includes("data-rail-ad")) failures.push("rail-ad-slot-missing");
  }
  return failures;
}

assert.equal(htmlFiles.length, 529, "generated HTML inventory changed");
for (const file of htmlFiles) {
  const relative = path.relative(publicDir, file);
  assert.deepEqual(inspect(fs.readFileSync(file, "utf8"), relative), [], `navigation contract failed in ${relative}`);
}

/* CSS 契约：≥44px 触控目标 + 核心布局类 */
const targetSelectors = [".tome-nav-toggle", ".tome-chapter a", ".game-dd-item", ".dd-lang .lang-item", ".site-search input[type=\"search\"]", ".privacy-settings", ".folio-toc a", ".tome-game a", ".folio-rel a"];
for (const sel of targetSelectors) {
  assert(minHeightOf(cssRule(style, sel)) >= 44, `${sel} touch target must be >= 44px`);
}
for (const sel of [".site-header", ".header-inner", ".header-brand", ".shell-body", ".page-shell", ".page-folio", ".ad-slot", ".drawer-chrome"])
  assert(style.includes(sel), `missing layout class ${sel} in style.css`);
assert(!/\.moon-nav-toggle/.test(moonStyle), "moon-nav-toggle must be removed from style-moon.css");
assert(!/\.moon-nav-item/.test(moonStyle), "moon-nav-item must be removed from style-moon.css");

/* 负向故障注入：每个故障都必须被 inspect 抓住（顶栏/抽屉组件出现两次，需 replaceAll） */
const sovereign = fs.readFileSync(path.join(publicDir, "index.html"), "utf8");
const knights = fs.readFileSync(path.join(publicDir, "sovereign-tower/knights.html"), "utf8");
const sandustry = fs.readFileSync(path.join(publicDir, "sandustry/materials.html"), "utf8");
const moon = fs.readFileSync(path.join(publicDir, "moonlight-peaks/achievements.html"), "utf8");
const faults = [
  [sovereign.replace('id="sovereign-navigation"', 'id="broken-navigation"'), "index.html", "sovereign-nav-id"],
  [sovereign.replace('aria-controls="sovereign-navigation"', 'aria-controls="broken-navigation"'), "index.html", "sovereign-toggle-aria"],
  [sovereign.replaceAll("setNavigation(false, true)", "setNavigation(false, false)"), "index.html", "sovereign-close-sync"],
  [sovereign.replaceAll("nav.setAttribute('inert'", "nav.setAttribute('hidden'"), "index.html", "drawer-inert-missing"],
  [sovereign.replace("/* drawer-focus-trap */", ""), "index.html", "drawer-focus-trap-missing"],
  [sovereign.replaceAll("e.key === 'Escape'", "e.key === 'Enter'"), "index.html", "sovereign-escape"],
  [sovereign.replace('class="site-header"', 'class="broken-header"'), "index.html", "site-header-missing"],
  [sovereign.replaceAll('class="game-dd"', 'class="broken-dd"'), "index.html", "game-dd-missing"],
  [sovereign.replaceAll('class="lang-dd"', 'class="broken-lang"'), "index.html", "lang-dd-missing"],
  [sovereign.replaceAll('class="site-search"', 'class="broken-search"'), "index.html", "site-search-missing"],
  [sovereign.replaceAll('name="as_sitesearch"', 'name="broken_sitesearch"'), "index.html", "search-sitesearch-missing"],
  [sovereign.replaceAll('<span class="lang-name">Deutsch</span>', ""), "index.html", "lang-list-incomplete"],
  [sovereign.replaceAll("data-consent-settings", "data-broken-settings"), "index.html", "privacy-settings-missing"],
  [knights.replaceAll("data-rail-ad", "data-broken-rail"), "sovereign-tower/knights.html", "rail-ad-slot-missing"],
  [sandustry.replace('<nav class="tome-chapters"', '<nav class="tome-chapters"><a href="/sovereign-tower/knights">intruder</a>'), "sandustry/materials.html", "sidebar-cross-game"],
  [sandustry.replaceAll("/sandustry/", "/sovereign-tower/"), "sandustry/materials.html", "footer-cross-game"],
  [moon.replace('<div class="moon-ruled">', '<div class="moon-ruled"><nav class="moon-nav"></nav>'), "moonlight-peaks/achievements.html", "moon-chrome-remnant"],
];
for (const [html, relative, expected] of faults)
  assert(inspect(html, relative).includes(expected), `negative fault was not caught: ${expected}`);

console.log(JSON.stringify({
  status: "pass",
  pages: htmlFiles.length,
  navigationSystems: ["sovereign-tower", "moonlight-peaks", "sandustry (per-game sidebar)"],
  topBar: ["header-brand", "game-dd", "lang-dd (6 langs)", "site-search", "privacy-settings"],
  rightRail: ["folio-toc", "folio-related", "ad-slot"],
  drawer: ["inert-closed", "focus-trap-open", "escape-return"],
  perGameSidebar: true,
  targetMinPx: 44,
  negativeFaults: faults.length,
}, null, 2));
