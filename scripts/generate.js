#!/usr/bin/env node
/**
 * Sovereign Tower Guide Hub — "The Sovereign's Ledger"（君主的圆桌手账）
 * 数据驱动 + 6 语言：data/site.json → node scripts/generate.js → public/
 * 语言：en（默认）/ zh-CN / ja / ko / fr / de，hreflang + 语言切换器（SVG 国旗）
 * 视觉：暖木 + 羊皮纸 + 黄铜 + 橄榄（Nature Distilled），手写体标题，账册表 + 羊皮纸卡 + 工单票根 + 黄铜工具卡
 * 独立骨架：圆桌卷宗导航 / 手账首页 / 嵌套子目录 slug（sovereign-tower/knights）
 */
const fs = require("fs");
const path = require("path");
const crypto = require("crypto");
const KIT = require("./lib/site-kit");

const ROOT = path.join(__dirname, "..");
const DATA = JSON.parse(fs.readFileSync(path.join(ROOT, "data", "site.json"), "utf8"));
const OUT = path.join(ROOT, "public");
const esc = KIT.esc;
const LANGS = DATA.site.languages || ["en"];
const DEF = DATA.site.defaultLanguage || "en";
const CSS_V = crypto.createHash("md5").update(fs.readFileSync(path.join(ROOT, "templates", "style.css"), "utf8")).digest("hex").slice(0, 8);
const urlOf = KIT.createUrl({ domain: DATA.site.domain, defaultLang: DEF });
const TODAY = new Date().toISOString().slice(0, 10);
const LM = KIT.createLastmod({ manifestPath: path.join(ROOT, "data", ".lastmod.json"), today: TODAY });

/* ---------- 语言与国旗（SVG，全平台渲染） ---------- */
const LANG_META = {
  "en":    { name: "English",  html: "en" },
  "zh-CN": { name: "简体中文", html: "zh-CN" },
  "ja":    { name: "日本語",   html: "ja" },
  "ko":    { name: "한국어",   html: "ko" },
  "fr":    { name: "Français", html: "fr" },
  "de":    { name: "Deutsch",  html: "de" },
};
const FLAGS = {
  "en": '<svg viewBox="0 0 60 40"><rect width="60" height="40" fill="#012169"/><path d="M0 0 60 40M60 0 0 40" stroke="#fff" stroke-width="11"/><path d="M0 0 60 40M60 0 0 40" stroke="#C8102E" stroke-width="6"/><path d="M30 0v40M0 20h60" stroke="#fff" stroke-width="14"/><path d="M30 0v40M0 20h60" stroke="#C8102E" stroke-width="8"/></svg>',
  "zh-CN": '<svg viewBox="0 0 60 40"><rect width="60" height="40" fill="#EE1C25"/><g fill="#FFDE00"><path d="M12 8l1.7 3.4 3.8.5-2.8 2.7.7 3.8L12 16.7l-3.4 1.7.7-3.8-2.8-2.7 3.8-.5z"/><path d="M22 4l.8 1.6 1.8.3-1.3 1.3.3 1.8-1.6-.8-1.6.8.3-1.8-1.3-1.3 1.8-.3zM25 11l.8 1.6 1.8.3-1.3 1.3.3 1.8-1.6-.8-1.6.8.3-1.8-1.3-1.3 1.8-.3zM22 18l.8 1.6 1.8.3-1.3 1.3.3 1.8-1.6-.8-1.6.8.3-1.8-1.3-1.3 1.8-.3zM19 11l.8 1.6 1.8.3-1.3 1.3.3 1.8-1.6-.8-1.6.8.3-1.8-1.3-1.3 1.8-.3z"/></g></svg>',
  "ja": '<svg viewBox="0 0 60 40"><rect width="60" height="40" fill="#fff"/><circle cx="30" cy="20" r="11" fill="#BC002D"/></svg>',
  "ko": '<svg viewBox="0 0 60 40"><rect width="60" height="40" fill="#fff"/><g transform="translate(30 20)"><g transform="rotate(45)"><rect x="-10" y="-5" width="20" height="10" fill="#CD2E3A"/><rect x="-10" y="0" width="20" height="10" fill="#0047A0"/><circle r="6" fill="#fff"/></g><circle r="5" fill="#CD2E3A"/><path d="M0-5a5 5 0 0 1 0 10 2 2 0 0 1 0-10" fill="#0047A0"/></g><g fill="#000"><path d="M15 2h3v6h-3zM15 32h3v6h-3zM42 2h3v6h-3zM42 32h3v6h-3z"/></g></svg>',
  "fr": '<svg viewBox="0 0 60 40"><rect width="60" height="40" fill="#ED2939"/><rect width="20" height="40" fill="#fff"/><rect x="40" width="20" height="40" fill="#002395"/></svg>',
  "de": '<svg viewBox="0 0 60 40"><rect width="60" height="13.3" fill="#000"/><rect y="13.3" width="60" height="13.4" fill="#DD0000"/><rect y="26.7" width="60" height="13.3" fill="#FFCE00"/></svg>',
};
const flagOf = l => FLAGS[l] || "🌐";

/* ---------- 图标（SVG 手账风，禁 emoji） ---------- */
const ICON = {
  "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3 5 6v5c0 4.5 3 8.3 7 10 4-1.7 7-5.5 7-10V6l-7-3z"/></svg>',
  "scroll": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M8 3h12v6a2 2 0 0 1-2 2H8a2 2 0 1 1 0-4h10"/><path d="M8 7H4a2 2 0 0 0 0 4h3v2H5a2 2 0 0 0-2 2v2a2 2 0 0 0 2 2h11v-4"/></svg>',
  "heart": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21s-7-4.5-9.5-9A5.5 5.5 0 0 1 12 6a5.5 5.5 0 0 1 9.5 6c-2.5 4.5-9.5 9-9.5 9z"/></svg>',
  "chef": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M6 13h12v3a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2v-3z"/><path d="M9 6a3 3 0 0 1 6 0c1.5.5 3 1.5 3 3H6c0-1.5 1.5-2.5 3-3z"/><path d="M10 18v2M14 18v2"/></svg>',
  "scales": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v18M5 7l7-4 7 4"/><path d="M5 7h14M5 7l-2.5 5a2.5 2.5 0 0 0 5 0L5 7zM19 7l-2.5 5a2.5 2.5 0 0 0 5 0L19 7z"/></svg>',
  "crown": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 8l4 4 5-7 5 7 4-4-2 11H5L3 8z"/><path d="M7 19h10"/></svg>',
  "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 6v6h4.5M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0z"/></svg>',
  "trophy": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M8 4h8v6a4 4 0 0 1-8 0V4z"/><path d="M8 5H4a3 3 0 0 0 3 4M16 5h4a3 3 0 0 1-3 4"/><path d="M12 14v3M8 20h8M9 20c0-2 1.3-3 3-3s3 1 3 3"/></svg>',
  "book": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 5a2 2 0 0 1 2-2h13v16H6a2 2 0 0 0-2 2V5z"/><path d="M4 19a2 2 0 0 1 2-2h13"/></svg>',
  "calc": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="3" width="14" height="18" rx="2"/><path d="M8 7h8M8 11h.01M12 11h.01M16 11h.01M8 15h.01M12 15h.01M16 15h.01M8 19h.01M12 19h.01M16 19h.01"/></svg>',
  "goose": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M6 13c0-4 3-7 7-7h5l-2 3h-2v1.5"/><path d="M7 13a4 4 0 0 0 3 6h5a2 2 0 0 0 2-2v-2"/><path d="M14 19h4"/></svg>',
  "search": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"><circle cx="11" cy="11" r="6"/><path d="m16 16 4 4"/></svg>',
  "steam": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 0 0-9.9 11.3l4.9 2a4 4 0 0 1 5.3-.6l3.3-5.7a1.5 1.5 0 1 1 2.5 1.7l-3.5 6a4 4 0 0 1-5 1.6l-3.7-1.5A10 10 0 1 0 12 2zM7 16.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3z"/></svg>',
  "wand": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="m4 20 12-12M14 6l4 4M16 2l1 3 3 1-3 1-1 3-1-3-3-1 3-1 1-3z"/></svg>',
  "fist": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M7 12V8a2 2 0 0 1 4 0v1m0-1V6a2 2 0 0 1 4 0v2m0-1V7a2 2 0 0 1 4 0v6a5 5 0 0 1-5 5h-1a5 5 0 0 1-4-2l-2-2a2 2 0 0 1 0-2z"/></svg>',
};

/* ---------- 语言/站点文案 ---------- */
const NAV_I18N = {
  "en":    { home: "Home", guides: "Guides", ledgers: "The Ledger", tools: "Tools", search: "Search guides…", searchLabel: "Search guides", langLabel: "Language",
             p0: "Core guides", p1: "Deep dives", p2: "Quick answers", about: "About", privacy: "Privacy", contact: "Contact",
             footerNote: "Unofficial fan site — game and assets belong to WILD WITS GAMES / Curve Games.",
             footerSource: "Information verified against the official Steam store page, fan wiki data and community reports.", updated: "Updated" },
  "zh-CN": { home: "首页", guides: "攻略", ledgers: "手账", tools: "工具", search: "搜索攻略…", searchLabel: "搜索攻略", langLabel: "语言",
             p0: "核心攻略", p1: "深度拆解", p2: "快速答案", about: "关于", privacy: "隐私", contact: "联系",
             footerNote: "非官方粉丝站——游戏及相关资产归 WILD WITS GAMES / Curve Games 所有。",
             footerSource: "信息核对自 Steam 官方商店页、粉丝 wiki 数据与社区报告。", updated: "更新于" },
  "ja":    { home: "ホーム", guides: "攻略", ledgers: "手帳", tools: "ツール", search: "攻略を検索…", searchLabel: "攻略を検索", langLabel: "言語",
             p0: "コア攻略", p1: "深掘り", p2: "クイック回答", about: "このサイト", privacy: "プライバシー", contact: "お問い合わせ",
             footerNote: "非公式ファンサイト。ゲームおよび関連アセットは WILD WITS GAMES / Curve Games に帰属します。",
             footerSource: "情報は Steam 公式ストア・ファン wiki・コミュニティ報告で確認しています。", updated: "更新" },
  "ko":    { home: "홈", guides: "가이드", ledgers: "수첩", tools: "도구", search: "가이드 검색…", searchLabel: "가이드 검색", langLabel: "언어",
             p0: "핵심 가이드", p1: "심층 분석", p2: "빠른 답변", about: "소개", privacy: "개인정보", contact: "문의",
             footerNote: "비공식 팬 사이트. 게임 및 관련 자산은 WILD WITS GAMES / Curve Games에 귀속됩니다.",
             footerSource: "정보는 Steam 공식 스토어, 팬 위키, 커뮤니티 보고로 확인했습니다.", updated: "업데이트" },
  "fr":    { home: "Accueil", guides: "Guides", ledgers: "Registre", tools: "Outils", search: "Rechercher des guides…", searchLabel: "Rechercher des guides", langLabel: "Langue",
             p0: "Guides principaux", p1: "Analyses", p2: "Réponses rapides", about: "À propos", privacy: "Confidentialité", contact: "Contact",
             footerNote: "Site de fans non officiel — le jeu et ses ressources appartiennent à WILD WITS GAMES / Curve Games.",
             footerSource: "Informations vérifiées sur la page Steam officielle, les wikis de fans et les rapports de la communauté.", updated: "Mis à jour" },
  "de":    { home: "Start", guides: "Guides", ledgers: "Register", tools: "Werkzeuge", search: "Guides suchen…", searchLabel: "Guides suchen", langLabel: "Sprache",
             p0: "Kern-Guides", p1: "Tiefe Analysen", p2: "Schnelle Antworten", about: "Über", privacy: "Datenschutz", contact: "Kontakt",
             footerNote: "Inoffizielle Fan-Seite — Spiel und Assets gehören WILD WITS GAMES / Curve Games.",
             footerSource: "Informationen geprüft gegen den offiziellen Steam-Store, Fan-Wikis und Community-Berichte.", updated: "Aktualisiert" },
};
const navI18n = l => NAV_I18N[l] || NAV_I18N.en;

const pageOf = (page, lang) => {
  if (lang === DEF || !page.i18n || !page.i18n[lang]) {
    return { title: page.title, metaTitle: page.metaTitle, metaDescription: page.metaDescription, intro: page.intro, sections: page.sections };
  }
  const t = page.i18n[lang];
  return { title: t.title || page.title, metaTitle: t.metaTitle || page.metaTitle, metaDescription: t.metaDescription || page.metaDescription, intro: t.intro || page.intro, sections: (t.sections && t.sections.length) ? t.sections : page.sections };
};
const siteI18n = lang => {
  const s = (DATA.site.i18n && DATA.site.i18n[lang]) || {};
  return { name: s.name || DATA.site.name, description: s.description || DATA.site.description };
};

/* ---------- 工具页数据（从 site.json 注入，供 JS 交互） ---------- */
const KNIGHT_DATA = (() => {
  const p = DATA.pages.find(x => x.slug === "sovereign-tower/knights");
  if (!p) return [];
  const tbl = (p.sections || []).find(s => s.type === "table" && s.headers && s.headers[0] === "Knight");
  if (!tbl) return [];
  return tbl.rows.map(r => ({ name: r[0], origin: r[1], level: r[2], armor: r[3], stats: r[4], meals: r[5], note: r[6] }));
})();

/* ---------- head ---------- */
function head(title, desc, extraLd, slug, lang) {
  const ld = JSON.stringify([KIT.ld.website({ name: siteI18n(lang).name, url: urlOf("index", lang), description: siteI18n(lang).description })].concat(extraLd || []));
  const gsc = DATA.site.gscVerification ? `<meta name="google-site-verification" content="${esc(DATA.site.gscVerification)}" />` : "";
  const htmlLang = LANG_META[lang]?.html || lang;
  return `<!DOCTYPE html>
<html lang="${htmlLang}">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>${esc(title)}</title>
<meta name="description" content="${esc(desc)}" />
<link rel="canonical" href="${urlOf(slug, lang)}" />
${KIT.hreflangTags({ langs: LANGS, defaultLang: DEF, urlOf, slug })}
<meta name="theme-color" content="#3A3226" />
${gsc}
<meta property="og:type" content="website" />
<meta property="og:site_name" content="${esc(siteI18n(lang).name)}" />
<meta property="og:title" content="${esc(title)}" />
<meta property="og:description" content="${esc(desc)}" />
<meta property="og:url" content="${urlOf(slug, lang)}" />
<meta property="og:image" content="https://${DATA.site.domain}/images/hero.jpg" />
<meta name="twitter:card" content="summary_large_image" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Caveat:wght@500;600;700&family=Nunito:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="/css/style.css?v=${CSS_V}" />
<script type="application/ld+json">${ld}</script>
${DATA.site.gaId ? `<script async src="https://www.googletagmanager.com/gtag/js?id=${esc(DATA.site.gaId)}"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','${esc(DATA.site.gaId)}');</script>` : ""}
</head>
<body>
`;
}

/* ---------- 语言切换器（含 SVG 国旗，修复下拉溢出） ---------- */
function langSwitcher(lang, slug) {
  const items = LANGS.map(l =>
    `<a href="${urlOf(slug, l)}" class="${l === lang ? "active" : ""}"><span class="flag svg-flag">${flagOf(l)}</span><span class="lang-name">${LANG_META[l]?.name || l}</span></a>`
  ).join("");
  return `<details class="lang-dd">
    <summary aria-label="${navI18n(lang).langLabel}"><span class="flag svg-flag">${flagOf(lang)}</span><span class="lang-name">${LANG_META[lang]?.name || lang}</span><span class="caret">▾</span></summary>
    <div class="dd-menu dd-lang">${items}</div>
  </details>`;
}

/* ---------- 圆桌卷宗导航（独立骨架） ---------- */
const GUIDE_GROUPS = {
  "en": { p0: ["sovereign-tower/how-to-play", "sovereign-tower/knights", "sovereign-tower/quest-mechanics"], p1: ["sovereign-tower/secret-knights", "sovereign-tower/romance", "sovereign-tower/endings", "sovereign-tower/recipes", "sovereign-tower/achievements"], p2: ["sovereign-tower/tools/quest-matcher", "sovereign-tower/tools/affinity-calc"] }
};
function header(lang, active) {
  const n = navI18n(lang);
  const prefix = lang === DEF ? "" : `/${lang}`;
  const gameSlug = "sovereign-tower";
  const G = GUIDE_GROUPS.en;
  const link = (slug, label, icon, act) =>
    `<a href="${urlOf(slug, lang)}" class="${act ? "active" : ""}"><span class="nav-ic">${ICON[icon] || ""}</span><span>${esc(label)}</span></a>`;
  const drop = (title, slugs) => `<div class="dd-group"><b class="dd-title">${esc(title)}</b>${slugs.map(s => {
    const p = DATA.pages.find(x => x.slug === s);
    if (!p) return "";
    const t = pageOf(p, lang).title.replace(/\s*(Sovereign Tower|Sovereign|君王之塔)\s*/g, " ").replace(/\s+/g, " ").trim();
    const ic = s.includes("knights") ? "shield" : s.includes("romance") ? "heart" : s.includes("recipes") ? "chef" : s.includes("endings") ? "crown" : s.includes("quest") ? "scales" : s.includes("achievement") ? "trophy" : s.includes("tools") ? "calc" : "book";
    return link(s, t, ic, s === active);
  }).join("")}</div>`;
  const manual = `${drop(n.p0, G.p0)}${drop(n.p1, G.p1)}${drop(n.p2, G.p2)}`;
  return `<header class="site-header">
  <div class="container header-inner">
    <a class="logo" href="${urlOf("index", lang)}"><span class="logo-badge">${ICON.crown}</span><span class="logo-txt">${esc(siteI18n(lang).name)}</span></a>
    <nav class="nav" aria-label="Main">
      <a href="${urlOf("index", lang)}" class="${active === "index" || active === "" ? "active" : ""}">${esc(n.home)}</a>
      <details class="dd">
        <summary>${esc(n.guides)} <span class="caret">▾</span></summary>
        <div class="dd-menu dd-manual">${manual}</div>
      </details>
      <a href="${urlOf(gameSlug + "/tools/quest-matcher", lang)}">${esc(n.tools)}</a>
    </nav>
    <form class="site-search" action="https://www.google.com/search" method="get" target="_blank" rel="noopener" role="search">
      <input type="search" name="q" placeholder="${esc(n.search)}" aria-label="${esc(n.searchLabel)}" />
      <input type="hidden" name="as_sitesearch" value="${esc(DATA.site.domain)}" />
      <span class="search-ic" aria-hidden="true">${ICON.search}</span>
    </form>
    ${langSwitcher(lang, active || "index")}
  </div>
</header>`;
}

function footer(lang) {
  const n = navI18n(lang);
  const prefix = lang === DEF ? "" : `/${lang}`;
  const links = DATA.pages.slice(0, 10).map(p => `<a href="${urlOf(p.slug, lang)}">${esc(pageOf(p, lang).title)}</a>`).join("");
  return `<footer class="site-footer">
  <div class="container footer-inner">
    <div class="footer-brand-row">
      <div class="footer-brand"><span class="logo-badge small">${ICON.crown}</span><span>${esc(siteI18n(lang).name)}</span></div>
      <div class="footer-links">
        <a href="${urlOf("about", lang)}">${esc(n.about)}</a><a href="${urlOf("privacy", lang)}">${esc(n.privacy)}</a><a href="${urlOf("contact", lang)}">${esc(n.contact)}</a>
        <a href="${esc(DATA.game.steamUrl)}" target="_blank" rel="noopener">Steam ↗</a>
      </div>
    </div>
    <div class="footer-cols">
      <nav class="footer-col">${links}</nav>
      <div class="footer-meta">
        <p>${esc(DATA.site.tagline)}</p>
        <p>${esc(n.footerNote)}</p>
        <p>${esc(n.footerSource)} · ${esc(n.updated)} ${TODAY}</p>
      </div>
    </div>
    ${DATA.site.adsenseId ? `<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=${esc(DATA.site.adsenseId)}" crossorigin="anonymous"></script>` : ""}
    ${DATA.site.adsterra ? DATA.site.adsterra : ""}
  </div>
<script>
document.addEventListener('click', function(e){
  document.querySelectorAll('details.dd[open], details.lang-dd[open]').forEach(function(d){
    if (!d.contains(e.target)) d.removeAttribute('open');
  });
});
document.addEventListener('keydown', function(e){
  if (e.key === 'Escape') document.querySelectorAll('details[open]').forEach(function(d){ d.removeAttribute('open'); });
});
document.addEventListener('DOMContentLoaded', function(){
  var obs = new IntersectionObserver(function(es){
    es.forEach(function(en){ if(en.isIntersecting){ en.target.classList.add('in'); obs.unobserve(en.target); } });
  }, {threshold:.08});
  document.querySelectorAll('.reveal').forEach(function(el){ obs.observe(el); });
  var tocLinks = Array.prototype.slice.call(document.querySelectorAll('.toc a'));
  if (tocLinks.length) {
    var tocTargets = tocLinks.map(function(a){ return document.querySelector(a.getAttribute('href')); });
    var tocObs = new IntersectionObserver(function(es){
      es.forEach(function(en){
        if (en.isIntersecting) {
          var id = '#' + en.target.id;
          tocLinks.forEach(function(a){ a.classList.toggle('active', a.getAttribute('href') === id); });
        }
      });
    }, {rootMargin:'-15% 0px -70% 0px', threshold:0});
    tocTargets.forEach(function(s){ if (s) tocObs.observe(s); });
  }
});
</script>
</footer>`;
}

/* ---------- Section 渲染（手账组件语言） ---------- */
function renderSection(s, lang) {
  const escTxt = esc(s.heading || "");
  const tag = s.tag ? `<span class="tag">${esc(s.tag)}</span>` : "";
  switch (s.type) {
    case "steps": {
      const items = (s.items || []).map((it, i) =>
        `<li class="work-ticket reveal">
          <span class="ticket-no">№ ${String(i + 1).padStart(2, "0")}</span>
          <div class="ticket-body"><h3>${esc(it[0])}</h3><p>${esc(it[1])}</p></div>
        </li>`).join("");
      return `<section class="ledger-section"><div class="section-head">${tag}<h2>${escTxt}</h2></div><ol class="work-tickets">${items}</ol></section>`;
    }
    case "list": {
      const items = (s.items || []).map(it => `<li>${esc(it)}</li>`).join("");
      return `<section class="ledger-section"><div class="section-head">${tag}<h2>${escTxt}</h2></div><ul class="ledger-notes">${items}</ul></section>`;
    }
    case "table": {
      const th = (s.headers || []).map(h => `<th scope="col">${esc(h)}</th>`).join("");
      const tr = (s.rows || []).map(r => `<tr>${r.map(c => `<td>${esc(c)}</td>`).join("")}</tr>`).join("");
      return `<section class="ledger-section"><div class="section-head">${tag}<h2>${escTxt}</h2></div><div class="ledger-table-wrap"><table class="ledger-table"><thead><tr>${th}</tr></thead><tbody>${tr}</tbody></table></div></section>`;
    }
    case "faq": {
      const items = (s.items || []).map((qa, i) =>
        `<details class="faq-item" ${i === 0 ? "open" : ""}><summary>${esc(qa[0])}</summary><p>${esc(qa[1])}</p></details>`).join("");
      return `<section class="ledger-section"><div class="section-head">${tag}<h2>${escTxt}</h2></div><div class="faq-list">${items}</div></section>`;
    }
    case "note": {
      return `<aside class="marginalia reveal">${tag}<p>${esc(s.body || "")}</p></aside>`;
    }
    case "questmatcher": {
      return `<section class="ledger-section tool-card brass-tool"><div class="section-head">${tag}<h2>${escTxt}</h2></div>
        <div class="tool-body" data-tool="questmatcher">
          <label class="tool-label" for="qm-type">${lang === "zh-CN" ? "选择任务类型" : "Choose a quest type"}</label>
          <select id="qm-type" class="tool-select"><option value="">${lang === "zh-CN" ? "— 选择 —" : "— Select —"}</option></select>
          <div class="tool-result"><p class="tool-hint">${lang === "zh-CN" ? "选择后显示骑士适配建议" : "Pick a quest type to see knight fit"}</p></div>
        </div>
        <script type="application/json" class="tool-data">${JSON.stringify({ knights: KNIGHT_DATA, questTypes: ["Hunt","Assassination","Relic Recovery","Diplomacy","Scouting","Confrontation","Duel","Competition","Research","Rescue","Knight Quest"] })}</script>
      </section>`;
    }
    case "affinitycalc": {
      return `<section class="ledger-section tool-card brass-tool"><div class="section-head">${tag}<h2>${escTxt}</h2></div>
        <div class="tool-body" data-tool="affinitycalc">
          <label class="tool-label" for="ac-knight">${lang === "zh-CN" ? "选择骑士" : "Choose a knight"}</label>
          <select id="ac-knight" class="tool-select"></select>
          <div class="ac-controls">
            <label class="tool-label" for="ac-assign">${lang === "zh-CN" ? "本次指派（喜欢/厌恶/中性）" : "Assignment (liked / disliked / neutral)"}</label>
            <select id="ac-assign" class="tool-select"><option value="1.33">+1.33</option><option value="0">0</option><option value="-0.75">−0.75</option></select>
            <label class="tool-label" for="ac-meal">${lang === "zh-CN" ? "喂最爱菜？" : "Feed favourite meal?"}</label>
            <select id="ac-meal" class="tool-select"><option value="0">No</option><option value="1">Yes (+1.5)</option></select>
          </div>
          <div class="tool-result"><p class="tool-hint">${lang === "zh-CN" ? "调整后查看好感变化" : "Adjust to see affinity change"}</p></div>
        </div>
        <script type="application/json" class="tool-data">${JSON.stringify({ knights: KNIGHT_DATA })}</script>
      </section>`;
    }
    default:
      return `<section class="ledger-section"><div class="section-head">${tag}<h2>${escTxt}</h2></div><p>${esc(s.body || "")}</p></section>`;
  }
}

/* ---------- 首页（手账总览） ---------- */
function renderHome(lang) {
  const n = navI18n(lang);
  const isZh = lang === "zh-CN";
  const t = pageOf(DATA.pages.find(p => p.slug === "index"), lang);
  const intro = t.intro || "";
  const gamePages = DATA.pages.filter(p => p.slug.startsWith("sovereign-tower/") && p.slug !== "sovereign-tower/tools/quest-matcher" && p.slug !== "sovereign-tower/tools/affinity-calc");
  const toolPages = DATA.pages.filter(p => p.slug.startsWith("sovereign-tower/tools/"));
  const cards = gamePages.map(p => {
    const pt = pageOf(p, lang);
    const ic = p.slug.includes("knights") ? "shield" : p.slug.includes("romance") ? "heart" : p.slug.includes("recipes") ? "chef" : p.slug.includes("endings") ? "crown" : p.slug.includes("secret") ? "fist" : p.slug.includes("achievement") ? "trophy" : p.slug.includes("quest") ? "scales" : "book";
    return `<a class="ledger-card reveal" href="${urlOf(p.slug, lang)}"><span class="card-ic">${ICON[ic]}</span><span class="card-txt"><b>${esc(pt.title)}</b><small>${esc((pt.metaDescription || "").slice(0, 70))}…</small></span></a>`;
  }).join("");
  const toolCards = toolPages.map(p => {
    const pt = pageOf(p, lang);
    return `<a class="ledger-card tool reveal" href="${urlOf(p.slug, lang)}"><span class="card-ic">${ICON.calc}</span><span class="card-txt"><b>${esc(pt.title)}</b><small>${lang === "zh-CN" ? "交互工具" : "Interactive tool"}</small></span></a>`;
  }).join("");
  const body = `<main class="home-main">
  <section class="hero-parchment reveal">
    <span class="hero-seal">${ICON.crown}</span>
    <h1>${isZh ? "君王之塔 · 圆桌手账" : "Sovereign Tower · The Round Table Ledger"}</h1>
    <p class="hero-intro">${esc(intro)}</p>
    <div class="hero-cta">
      <a class="btn btn-primary" href="${urlOf("sovereign-tower/knights", lang)}">${isZh ? "开始：全部骑士" : "Start: All Knights"}</a>
      <a class="btn btn-ghost" href="${esc(DATA.game.steamUrl)}" target="_blank" rel="noopener">Steam ↗</a>
    </div>
  </section>
  <section class="hub-section"><div class="section-head"><span class="tag">${isZh ? "卷宗" : "THE LEDGER"}</span><h2>${isZh ? "攻略目录" : "Guide Collection"}</h2></div>
    <div class="ledger-grid">${cards}${toolCards}</div>
  </section>
  <section class="hub-section"><div class="section-head"><span class="tag">${isZh ? "预告" : "COMING NEXT"}</span><h2>${isZh ? "更多 cozy / sim 游戏即将收录" : "More cozy & sim game hubs on the way"}</h2></div>
    <p class="hub-note">${isZh ? "这是第一个游戏子目录——后续会持续加入更多 cozy/模拟经营游戏的完整攻略与工具。" : "This is the first game hub — more cozy & simulation game guides and tools are being added over time."}</p>
  </section>
</main>`;
  const ld = [KIT.ld.article({ page: { ...t, slug: "index" }, lang, urlOf, siteName: siteI18n(lang).name, datePublished: TODAY, dateModified: KIT.LASTMOD_TOKEN })];
  return head(t.metaTitle || t.title, t.metaDescription, ld, "index", lang) + header(lang, "index") + body + footer(lang);
}

/* ---------- 普通页 ---------- */
function renderPage(p, lang) {
  const t = pageOf(p, lang);
  const isTool = p.slug.startsWith("sovereign-tower/tools/");
  const page = { ...t, slug: p.slug };
  const ld = [
    KIT.ld.article({ page, lang, urlOf, siteName: siteI18n(lang).name, datePublished: TODAY, dateModified: KIT.LASTMOD_TOKEN }),
    KIT.ld.breadcrumb({ page, lang, urlOf, homeName: navI18n(lang).home })
  ];
  const sections = (t.sections || []).map(s => renderSection(s, lang)).join("");
  const body = `<main class="page-main"><article class="ledger-article">
    <div class="page-head reveal"><span class="tag">${isTool ? (lang === "zh-CN" ? "工具" : "TOOL") : (lang === "zh-CN" ? "手账" : "LEDGER")}</span>
      <h1>${esc(t.title)}</h1>
      <p class="page-intro">${esc(t.intro || "")}</p>
    </div>
    ${sections}
  </article></main>`;
  return head(t.metaTitle || t.title, t.metaDescription, ld, p.slug, lang) + header(lang, p.slug) + body + footer(lang);
}

/* ---------- 静态页（about/privacy/contact） ---------- */
function renderStatic(slug, lang) {
  const n = navI18n(lang);
  const titleMap = {
    "about": n.about, "privacy": n.privacy, "contact": n.contact
  };
  const bodyMap = {
    "about": `${esc(siteI18n(lang).name)} is an unofficial fan resource for Sovereign Tower (君王之塔). We research every page against the official Steam store page, fan wiki data and community reports, and clearly mark anything still being verified.`,
    "privacy": "This site does not collect personal data beyond what hosting and analytics providers (e.g. Google Analytics if enabled) record. See your ad/analytics provider's policy for details.",
    "contact": "Corrections or questions? Contact us via the site's GitHub repository or email.",
    "404": "The page you are looking for was not found. Return to the guide hub."
  };
  const body = `<main class="page-main"><article class="ledger-article"><div class="page-head"><h1>${esc(titleMap[slug])}</h1></div><p>${bodyMap[slug]}</p></article></main>`;
  return head(titleMap[slug], bodyMap[slug].slice(0, 150), [], slug, lang) + header(lang, slug) + body + footer(lang);
}

/* ---------- 工具交互 JS（渐进增强） ---------- */
const TOOL_JS = `<script>
(function(){
  function dataOf(container){
    var el = container.querySelector('.tool-data') || document.querySelector('.tool-data');
    if (!el) return null;
    try { return JSON.parse(el.textContent); } catch(e){ return null; }
  }
  function qs(sel){ return document.querySelector(sel); }
  // Quest Matcher
  var qm = document.querySelector('[data-tool="questmatcher"]');
  if (qm) {
    var d = dataOf(qm);
    var sel = qm.querySelector('#qm-type');
    var out = qm.querySelector('.tool-result');
    if (d && sel && out) {
      d.questTypes.forEach(function(t){ var o=document.createElement('option'); o.value=t; o.textContent=t; sel.appendChild(o); });
      var likes = { "Diplomacy": ["Alwena","Angelica","Ari","Arron"], "Scouting": ["Angelica","Ari","Arron"], "Relic Recovery": ["Alwena","Ari","Arron"], "Hunt": ["Brunhilda"], "Duel": ["Alwena"] };
      sel.addEventListener('change', function(){
        var t = sel.value;
        if (!t) { out.innerHTML = '<p class="tool-hint">' + (document.documentElement.lang === 'zh-CN' ? '选择后显示骑士适配建议' : 'Pick a quest type to see knight fit') + '</p>'; return; }
        var fav = (likes[t] || []).map(function(n){ return '<b>' + n + '</b>'; }).join(', ') || '—';
        var rows = d.knights.map(function(k){
          var isFav = (likes[t] || []).indexOf(k.name) > -1;
          var tag = isFav ? '<span class="pill pill-good">+1.33</span>' : '<span class="pill pill-mid">0</span>';
          return '<tr><td>'+k.name+'</td><td>'+tag+'</td><td>'+(k.note||'')+'</td></tr>';
        }).join('');
        out.innerHTML = '<table class="ledger-table tool-table"><thead><tr><th>'+(document.documentElement.lang==='zh-CN'?'骑士':'Knight')+'</th><th>'+(document.documentElement.lang==='zh-CN'?'好感':'Affinity')+'</th><th>'+(document.documentElement.lang==='zh-CN'?'备注':'Notes')+'</th></tr></thead><tbody>'+rows+'</tbody></table>';
      });
    }
  }
  // Affinity Calculator
  var ac = document.querySelector('[data-tool="affinitycalc"]');
  if (ac) {
    var ad = dataOf(ac);
    var kSel = ac.querySelector('#ac-knight');
    var aSel = ac.querySelector('#ac-assign');
    var mSel = ac.querySelector('#ac-meal');
    var aOut = ac.querySelector('.tool-result');
    if (ad && kSel && aOut) {
      ad.knights.forEach(function(k){ var o=document.createElement('option'); o.value=k.name; o.textContent=k.name; kSel.appendChild(o); });
      function recalc(){
        var assign = parseFloat(aSel ? aSel.value : 0) || 0;
        var meal = parseFloat(mSel ? mSel.value : 0) || 0;
        var total = assign + meal;
        var isZh = document.documentElement.lang === 'zh-CN';
        var warn = total <= -7 ? (isZh ? ' ⚠ 已到辞职线（−7）' : ' ⚠ At resignation line (−7)') : '';
        aOut.innerHTML = '<p class="tool-total">' + (isZh ? '本次变化：' : 'Change this time: ') + '<b>' + (total > 0 ? '+' : '') + total.toFixed(2) + '</b>' + warn + '</p>';
      }
      [aSel, mSel].forEach(function(s){ if(s) s.addEventListener('change', recalc); });
    }
  }
})();
</script>`;

/* ---------- 构建 ---------- */
function build() {
  if (fs.existsSync(OUT)) fs.rmSync(OUT, { recursive: true, force: true });
  const all = [];
  // 首页
  for (const lang of LANGS) all.push({ html: renderHome(lang), path: lang === DEF ? "index.html" : `${lang}/index.html` });
  // 内容页（index 已由 renderHome 生成，跳过）
  for (const p of DATA.pages) {
    if (p.slug === "index") continue;
    for (const lang of LANGS) {
      const html = renderPage(p, lang) + (p.slug.startsWith("sovereign-tower/tools/") ? TOOL_JS : "") + "</body></html>";
      const base = lang === DEF ? `${p.slug}` : `${lang}/${p.slug}`;
      all.push({ html, path: `${base}.html` });
    }
  }
  // 静态页
  for (const slug of ["about", "privacy", "contact"]) {
    for (const lang of LANGS) {
      const html = renderStatic(slug, lang) + "</body></html>";
      all.push({ html, path: lang === DEF ? `${slug}.html` : `${lang}/${slug}.html` });
    }
  }
  // 写文件
  for (const f of all) {
    const p = path.join(OUT, f.path);
    fs.mkdirSync(path.dirname(p), { recursive: true });
    fs.writeFileSync(p, f.html);
  }
  // 复制静态资源
  fs.mkdirSync(path.join(OUT, "css"), { recursive: true });
  fs.copyFileSync(path.join(ROOT, "templates", "style.css"), path.join(OUT, "css", "style.css"));
  const assetsSrc = path.join(ROOT, "assets");
  if (fs.existsSync(assetsSrc)) {
    const cp = (src, dst) => { if (fs.existsSync(src)) { fs.mkdirSync(path.dirname(dst), { recursive: true }); fs.copyFileSync(src, dst); } };
    cp(path.join(assetsSrc, "favicon.svg"), path.join(OUT, "favicon.svg"));
    cp(path.join(assetsSrc, "favicon-32x32.png"), path.join(OUT, "favicon-32x32.png"));
    cp(path.join(assetsSrc, "favicon-16x16.png"), path.join(OUT, "favicon-16x16.png"));
    cp(path.join(assetsSrc, "apple-touch-icon.png"), path.join(OUT, "apple-touch-icon.png"));
    if (fs.existsSync(path.join(assetsSrc, "images"))) {
      fs.cpSync(path.join(assetsSrc, "images"), path.join(OUT, "images"), { recursive: true });
    }
  }
  // sitemap（嵌套 slug 用完整 URL）
  const urls = [];
  for (const lang of LANGS) {
    urls.push(urlOf("index", lang));
    for (const p of DATA.pages) urls.push(urlOf(p.slug, lang));
    for (const slug of ["about", "privacy", "contact"]) urls.push(urlOf(slug, lang));
  }
  const sitemap = `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${urls.map(u => `  <url><loc>${esc(u)}</loc><lastmod>${TODAY}</lastmod></url>`).join("\n")}\n</urlset>\n`;
  fs.writeFileSync(path.join(OUT, "sitemap.xml"), sitemap);
  // robots.txt
  fs.writeFileSync(path.join(OUT, "robots.txt"), `User-agent: *\nAllow: /\nSitemap: https://${DATA.site.domain}/sitemap.xml\n`);
  // 404
  fs.writeFileSync(path.join(OUT, "404.html"), renderStatic("404", DEF) + "</body></html>");
  console.log(`✓ built ${all.length} files (${LANGS.length} langs, ${DATA.pages.length + 4} pages)`);
}

build();
