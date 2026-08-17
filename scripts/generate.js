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
// 品类游戏注册表（CozySimHub hub）：卡片墙 / 游戏切换器 / JSON-LD ItemList 全部数据驱动
const GAMES = (() => {
  const p = path.join(ROOT, "data", "games.json");
  if (!fs.existsSync(p)) throw new Error("data/games.json missing — CozySimHub hub requires the game registry");
  const raw = JSON.parse(fs.readFileSync(p, "utf8"));
  if (!Array.isArray(raw.games) || !raw.games.length) throw new Error("data/games.json must contain a non-empty games array");
  return raw.games;
})();
const OUT = path.join(ROOT, "public");
const esc = KIT.esc;
const ADSENSE_FIXTURE_ENABLED = process.env.NODE_ENV === "test" && process.env.COZY_ADSENSE_FIXTURE === "enabled";
const ADSENSE_PUBLISHER_ID = /^pub-\d+$/.test(String(DATA.site.adsenseId || "").trim())
  ? String(DATA.site.adsenseId).trim()
  : "";
const ADSENSE_CLIENT_ID = ADSENSE_PUBLISHER_ID ? `ca-${ADSENSE_PUBLISHER_ID}` : "";
const ADSENSE_SERVING_ENABLED = Boolean(
  ADSENSE_CLIENT_ID && (
    ADSENSE_FIXTURE_ENABLED || (
      DATA.site.adsenseServing &&
      DATA.site.adsenseServing.enabled === true &&
      DATA.site.adsenseServing.providerReady === true &&
      DATA.site.adsenseServing.certifiedCmpReady === true
    )
  )
);
const ADSENSE_SCRIPT_SRC = ADSENSE_SERVING_ENABLED
  ? `https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=${ADSENSE_CLIENT_ID}`
  : "";
const LANGS = DATA.site.languages || ["en"];
const DEF = DATA.site.defaultLanguage || "en";
const CSS_V = crypto.createHash("md5").update(fs.readFileSync(path.join(ROOT, "templates", "style.css"), "utf8")).digest("hex").slice(0, 8);
const urlOf = KIT.createUrl({ domain: DATA.site.domain, defaultLang: DEF });
// 内部链接用相对路径（审计识别 inbound + 不依赖域名）；canonical/hreflang 仍用绝对 urlOf
const pageLangsOf = (slug) => {
  const p = DATA.pages.find(x => x.slug === slug);
  return (p && p.languages && p.languages.length) ? p.languages : LANGS;
};
const linkOf = (slug, lang) => {
  const p = String(slug).replace(/\.html$/, "").replace(/^\//, "");
  if (p === "" || p === "index") return lang === DEF ? "/" : `/${lang}/`;
  const pl = pageLangsOf(p);
  const useLang = pl.includes(lang) ? lang : DEF;
  return useLang === DEF ? `/${p}` : `/${useLang}/${p}`;
};
// 构建时间不是内容。默认固定到仓库已声明的内容校验日期；只有编辑者显式
// 提供 CONTENT_UPDATED_AT 时才推进，避免同一 commit 跨午夜生成整站不同产物。
const TODAY = process.env.CONTENT_UPDATED_AT || DATA.site.contentUpdatedAt;
if (!/^\d{4}-\d{2}-\d{2}$/.test(TODAY || "")) {
  throw new Error("data/site.json site.contentUpdatedAt or CONTENT_UPDATED_AT must be YYYY-MM-DD");
}
const COPYRIGHT_YEAR = TODAY.slice(0, 4);
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

/* 游戏徽记（品类站新增，禁 emoji —— spec §A.4）：月相 / 齿轮 */
const GAME_ICON = {
  "crown": ICON.crown,
  "moon": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M20 14.2A8.6 8.6 0 0 1 9.8 4 8.6 8.6 0 1 0 20 14.2z"/></svg>',
  "gear": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3.1"/><path d="M12 2.6v3M12 18.4v3M2.6 12h3M18.4 12h3M5.4 5.4l2.1 2.1M16.5 16.5l2.1 2.1M18.6 5.4l-2.1 2.1M7.5 16.5l-2.1 2.1"/></svg>',
};

/* ---------- 语言/站点文案 ---------- */
const NAV_I18N = {
  "en":    { home: "Home", guides: "Guides", ledgers: "The Ledger", tools: "Tools", search: "Search guides…", searchLabel: "Search guides", langLabel: "Language",
             p0: "Core guides", p1: "Deep dives", p2: "Quick answers", about: "About", privacy: "Privacy", contact: "Contact",
             footerNote: "Unofficial fan site — game and assets belong to WILD WITS GAMES / Curve Games.",
             footerSource: "Information verified against the official Steam store page, fan wiki data and community reports.", updated: "Updated", amazonTitle: "Game Gear", amazonNote: "As an Amazon Associate we earn from qualifying purchases. Prices and availability may change.", amazon1: "Gaming Keyboard", amazon2: "Gaming Mouse", amazon3: "Headset", amazon4: "Controller", amazon5: "Monitor" },
  "zh-CN": { home: "首页", guides: "攻略", ledgers: "手账", tools: "工具", search: "搜索攻略…", searchLabel: "搜索攻略", langLabel: "语言",
             p0: "核心攻略", p1: "深度拆解", p2: "快速答案", about: "关于", privacy: "隐私", contact: "联系",
             footerNote: "非官方粉丝站——游戏及相关资产归 WILD WITS GAMES / Curve Games 所有。",
             footerSource: "信息核对自 Steam 官方商店页、粉丝 wiki 数据与社区报告。", updated: "更新于", amazonTitle: "游戏装备", amazonNote: "作为亚马逊联盟伙伴，我们会从符合条件的购买中获得佣金。价格与库存可能随时变化。", amazon1: "游戏键盘", amazon2: "游戏鼠标", amazon3: "耳机", amazon4: "手柄", amazon5: "显示器" },
  "ja":    { home: "ホーム", guides: "攻略", ledgers: "手帳", tools: "ツール", search: "攻略を検索…", searchLabel: "攻略を検索", langLabel: "言語",
             p0: "コア攻略", p1: "深掘り", p2: "クイック回答", about: "このサイト", privacy: "プライバシー", contact: "お問い合わせ",
             footerNote: "非公式ファンサイト。ゲームおよび関連アセットは WILD WITS GAMES / Curve Games に帰属します。",
             footerSource: "情報は Steam 公式ストア・ファン wiki・コミュニティ報告で確認しています。", updated: "更新", amazonTitle: "ゲームギア", amazonNote: "Amazonアソシエイトとして、適格購入から手数料を得ることがあります。価格と在庫は変動します。", amazon1: "ゲーミングキーボード", amazon2: "ゲーミングマウス", amazon3: "ヘッドセット", amazon4: "コントローラー", amazon5: "モニター" },
  "ko":    { home: "홈", guides: "가이드", ledgers: "수첩", tools: "도구", search: "가이드 검색…", searchLabel: "가이드 검색", langLabel: "언어",
             p0: "핵심 가이드", p1: "심층 분석", p2: "빠른 답변", about: "소개", privacy: "개인정보", contact: "문의",
             footerNote: "비공식 팬 사이트. 게임 및 관련 자산은 WILD WITS GAMES / Curve Games에 귀속됩니다.",
             footerSource: "정보는 Steam 공식 스토어, 팬 위키, 커뮤니티 보고로 확인했습니다.", updated: "업데이트", amazonTitle: "게임 장비", amazonNote: "Amazon 어소시에이트로서 적격 구매로부터 수수료를 받습니다. 가격과 재고는 변동될 수 있습니다.", amazon1: "게이밍 키보드", amazon2: "게이밍 마우스", amazon3: "헤드셋", amazon4: "컨트롤러", amazon5: "모니터" },
  "fr":    { home: "Accueil", guides: "Guides", ledgers: "Registre", tools: "Outils", search: "Rechercher des guides…", searchLabel: "Rechercher des guides", langLabel: "Langue",
             p0: "Guides principaux", p1: "Analyses", p2: "Réponses rapides", about: "À propos", privacy: "Confidentialité", contact: "Contactez-nous",
             footerNote: "Site de fans non officiel — le jeu et ses ressources appartiennent à WILD WITS GAMES / Curve Games.",
             footerSource: "Informations vérifiées sur la page Steam officielle, les wikis de fans et les rapports de la communauté.", updated: "Mis à jour", amazonTitle: "Équipement de jeu", amazonNote: "En tant que partenaire Amazon, nous touchons une commission sur les achats éligibles. Prix et disponibilité peuvent changer.", amazon1: "Clavier gamer", amazon2: "Souris gamer", amazon3: "Casque", amazon4: "Manette", amazon5: "Écran" },
  "de":    { home: "Start", guides: "Guides", ledgers: "Register", tools: "Werkzeuge", search: "Guides suchen…", searchLabel: "Guides suchen", langLabel: "Sprache",
             p0: "Kern-Guides", p1: "Tiefe Analysen", p2: "Schnelle Antworten", about: "Über", privacy: "Datenschutz", contact: "Kontakt",
             footerNote: "Inoffizielle Fan-Seite — Spiel und Assets gehören WILD WITS GAMES / Curve Games.",
             footerSource: "Informationen geprüft gegen den offiziellen Steam-Store, Fan-Wikis und Community-Berichte.", updated: "Aktualisiert", amazonTitle: "Gaming-Ausrüstung", amazonNote: "Als Amazon-Partner verdienen wir an qualifizierten Käufen. Preise und Verfügbarkeit können sich ändern.", amazon1: "Gaming-Tastatur", amazon2: "Gaming-Maus", amazon3: "Headset", amazon4: "Controller", amazon5: "Monitor" },
};
const navI18n = l => NAV_I18N[l] || NAV_I18N.en;

/* ---------- 品类文案（CozySimHub hub，6 语 —— spec §E.2） ---------- */
const CATEGORY_I18N = {
  "en": {
    hubEyebrow: "CozySimHub · Cozy & Sim",
    hubTitle: "Cozy & Sim Game Guides",
    hubSub: "Data-first guides with filterable tables, verified sources and interactive tools — for cozy and simulation games.",
    ctaBrowse: "Browse all guides",
    ctaLatest: "What's new",
    secGames: "Featured games",
    secValue: "Why CozySimHub",
    v1Title: "Data-first tables",
    v1Text: "Every guide is a complete, filterable table — no one-line answers.",
    v2Title: "Verified sources",
    v2Text: "Facts traced to official store pages, wiki data and community reports.",
    v3Title: "Interactive tools",
    v3Text: "Trackers, matchers and calculators built on the same data.",
    secLatest: "Latest guides",
    allGuides: "All guides →",
    switchLabel: "Games",
    updated: "Updated",
    footerNote: "Unofficial fan site — games and assets belong to their respective owners.",
    brandSub: "Cozy & Sim Guide Hub"
  },
  "zh-CN": {
    hubEyebrow: "CozySimHub · Cozy 与模拟经营",
    hubTitle: "Cozy 与模拟经营游戏攻略",
    hubSub: "以可筛选表格、可核来源与交互工具为核心的数据化攻略，专注 cozy 与模拟经营游戏。",
    ctaBrowse: "浏览全部攻略",
    ctaLatest: "最新内容",
    secGames: "收录游戏",
    secValue: "为什么是 CozySimHub",
    v1Title: "数据化表格",
    v1Text: "每篇攻略都是可筛选的完整表格，拒绝一句话答案。",
    v2Title: "来源可核",
    v2Text: "事实溯源到官方商店页、wiki 数据与社区报告。",
    v3Title: "交互工具",
    v3Text: "同一数据上的追踪器、匹配器与计算器。",
    secLatest: "最新攻略",
    allGuides: "全部攻略 →",
    switchLabel: "游戏",
    updated: "更新于",
    footerNote: "非官方粉丝站——游戏及相关资产归各权利方所有。",
    brandSub: "Cozy 与模拟经营攻略中心"
  },
  "ja": {
    hubEyebrow: "CozySimHub · コージー・シム",
    hubTitle: "コージー・シムゲーム攻略",
    hubSub: "絞り込みできる表・検証済みソース・対話ツールを軸にしたデータ攻略サイト。",
    ctaBrowse: "全攻略を見る",
    ctaLatest: "最新情報",
    secGames: "収録ゲーム",
    secValue: "CozySimHub の特徴",
    v1Title: "データ第一",
    v1Text: "すべての攻略は絞り込みできる完全な表。",
    v2Title: "検証済みソース",
    v2Text: "公式ストア・wiki・コミュニティ報告に基づく。",
    v3Title: "対話ツール",
    v3Text: "同じデータ上のトラッカー・マッチャー・計算機。",
    secLatest: "最新攻略",
    allGuides: "全攻略 →",
    switchLabel: "ゲーム",
    updated: "更新",
    footerNote: "非公式ファンサイト。ゲームとアセットは各権利者に帰属します。",
    brandSub: "コージー・シム攻略ハブ"
  },
  "ko": {
    hubEyebrow: "CozySimHub · 코지·시뮬",
    hubTitle: "코지·시뮬 게임 공략",
    hubSub: "필터되는 표·검증된 출처·대화형 도구 중심의 데이터 공략 사이트.",
    ctaBrowse: "전체 공략 보기",
    ctaLatest: "최신 소식",
    secGames: "수록 게임",
    secValue: "CozySimHub 소개",
    v1Title: "데이터 우선",
    v1Text: "모든 공략은 필터 가능한 완전한 표.",
    v2Title: "검증된 출처",
    v2Text: "공식 스토어·위키·커뮤니티 보고 기반.",
    v3Title: "대화형 도구",
    v3Text: "같은 데이터 기반 트래커·매처·계산기.",
    secLatest: "최신 공략",
    allGuides: "전체 공략 →",
    switchLabel: "게임",
    updated: "업데이트",
    footerNote: "비공식 팬 사이트. 게임 및 자산은 각 권리자에게 귀속됩니다.",
    brandSub: "코지·시뮬 공략 허브"
  },
  "fr": {
    hubEyebrow: "CozySimHub · Cozy & sim",
    hubTitle: "Guides de jeux cozy et de simulation",
    hubSub: "Guides orientés données : tableaux filtrables, sources vérifiées et outils interactifs.",
    ctaBrowse: "Parcourir les guides",
    ctaLatest: "Nouveautés",
    secGames: "Jeux à l'affiche",
    secValue: "Pourquoi CozySimHub",
    v1Title: "Tableaux orientés données",
    v1Text: "Chaque guide est un tableau complet et filtrable.",
    v2Title: "Sources vérifiées",
    v2Text: "Faits tracés aux pages officielles, wikis et rapports.",
    v3Title: "Outils interactifs",
    v3Text: "Suivis, matcheurs et calculateurs sur les mêmes données.",
    secLatest: "Derniers guides",
    allGuides: "Tous les guides →",
    switchLabel: "Jeux",
    updated: "Mis à jour",
    footerNote: "Site de fans non officiel — jeux et ressources appartiennent à leurs propriétaires.",
    brandSub: "Hub de guides cozy & sim"
  },
  "de": {
    hubEyebrow: "CozySimHub · Cozy & Sim",
    hubTitle: "Cozy- & Simulations-Guides",
    hubSub: "Datenbasierte Guides mit filterbaren Tabellen, geprüften Quellen und interaktiven Tools.",
    ctaBrowse: "Alle Guides ansehen",
    ctaLatest: "Neuigkeiten",
    secGames: "Enthaltene Spiele",
    secValue: "Warum CozySimHub",
    v1Title: "Datenorientierte Tabellen",
    v1Text: "Jeder Guide ist eine vollständige, filterbare Tabelle.",
    v2Title: "Geprüfte Quellen",
    v2Text: "Fakten aus offiziellen Store-Seiten, Wikis und Community-Berichten.",
    v3Title: "Interaktive Tools",
    v3Text: "Tracker, Matcher und Rechner auf derselben Datenbasis.",
    secLatest: "Neueste Guides",
    allGuides: "Alle Guides →",
    switchLabel: "Spiele",
    updated: "Aktualisiert",
    footerNote: "Inoffizielle Fan-Seite — Spiele und Assets gehören ihren jeweiligen Eigentümern.",
    brandSub: "Cozy- & Sim-Guide-Hub"
  }
};
const catI18n = l => CATEGORY_I18N[l] || CATEGORY_I18N.en;

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
  // AdSense 所有权验证 meta —— 五个 EMD 站同款；未配 adsenseId 时零输出
  const adsenseMeta = ADSENSE_CLIENT_ID ? `<meta name="google-adsense-account" content="${esc(ADSENSE_CLIENT_ID)}" />` : "";
  const htmlLang = LANG_META[lang]?.html || lang;
  const isMoon = slug.startsWith("moonlight-peaks");
  // hreflang 语言集：页面声明 languages 则用它，否则全局 LANGS
  const _pageDef = DATA.pages.find(x => x.slug === slug);
  const hreflangLangs = (_pageDef && _pageDef.languages && _pageDef.languages.length) ? _pageDef.languages : LANGS;
  const MOON_CSS_V = crypto.createHash("md5").update(fs.readFileSync(path.join(ROOT, "templates", "style-moon.css"), "utf8")).digest("hex").slice(0, 8);
  const themeColor = isMoon ? "#171034" : "#3A3226";
  const fontLink = isMoon
    ? '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;600;700;800&family=Lora:wght@400;500;600&family=MedievalSharp&family=Spectral:wght@500;600&display=swap" rel="stylesheet" />'
    : '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Inter:wght@400;500;600;700&family=Caveat:wght@500;600&display=swap" rel="stylesheet" />';
  const cssLink = isMoon ? `<link rel="stylesheet" href="/css/style-moon.css?v=${MOON_CSS_V}" />` : `<link rel="stylesheet" href="/css/style.css?v=${CSS_V}" />`;
  return `<!DOCTYPE html>
<html lang="${htmlLang}">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>${esc(title)}</title>
<meta name="description" content="${esc(desc)}" />
<link rel="canonical" href="${urlOf(slug, lang)}" />${slug === "404" ? '<meta name="robots" content="noindex" />' : ""}
${KIT.hreflangTags({ langs: hreflangLangs, defaultLang: DEF, urlOf, slug })}
<meta name="theme-color" content="${themeColor}" />
${gsc}${adsenseMeta}
<meta property="og:type" content="website" />
<meta property="og:site_name" content="${esc(siteI18n(lang).name)}" />
<meta property="og:title" content="${esc(title)}" />
<meta property="og:description" content="${esc(desc)}" />
<meta property="og:url" content="${urlOf(slug, lang)}" />
<meta property="og:image" content="https://${DATA.site.domain}/images/hero.jpg" />
<meta name="twitter:card" content="summary_large_image" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
${fontLink}
${cssLink}
<link rel="icon" href="/favicon.svg" type="image/svg+xml" />
<link rel="icon" href="/favicon-32x32.png" sizes="32x32" type="image/png" />
<link rel="icon" href="/favicon-16x16.png" sizes="16x16" type="image/png" />
<link rel="apple-touch-icon" href="/apple-touch-icon.png" />
<script type="application/ld+json">${ld}</script>
</head>
<body>
<div class="app-shell">
`;
}

/* ---------- 语言切换器（含 SVG 国旗，修复下拉溢出） ---------- */
function langSwitcher(lang, slug) {
  const pl = pageLangsOf(slug);
  const items = pl.map(l =>
    `<a href="${linkOf(slug, l)}" class="${l === lang ? "active" : ""}"><span class="flag svg-flag">${flagOf(l)}</span><span class="lang-name">${LANG_META[l]?.name || l}</span></a>`
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
  const c = catI18n(lang);
  const G = GUIDE_GROUPS.en;
  const link = (slug, label, icon, folio, act) =>
    `<a href="${linkOf(slug, lang)}" class="${act ? "active" : ""}"><span class="folio-no">${folio}</span><span class="nav-ic">${ICON[icon] || ""}</span><span>${esc(label)}</span></a>`;
  const chap = (title, slugs) => `<div class="tome-chapter"><b>${esc(title)}</b>${slugs.map((s, i) => {
    const p = DATA.pages.find(x => x.slug === s);
    if (!p) return "";
    const t = pageOf(p, lang).title.replace(/\s*(Sovereign Tower|Sovereign|君王之塔)\s*/g, " ").replace(/\s+/g, " ").trim();
    const ic = s.includes("knights") ? "shield" : s.includes("romance") ? "heart" : s.includes("recipes") ? "chef" : s.includes("endings") ? "crown" : s.includes("secret") ? "fist" : s.includes("quest") && s.includes("mech") ? "scales" : s.includes("achievement") ? "trophy" : s.includes("tools") ? "calc" : s.includes("how-to-play") ? "book" : "wand";
    return link(s, t, ic, String(i + 1).padStart(2, "0"), s === active);
  }).join("")}</div>`;
  // hub 页侧栏不放君王之塔独占章节：改放「最新内容」快捷链接（spec §A.3）
  const chapters = active === "index" ? latestNav(lang) : `${chap(n.p0, G.p0)}${chap(n.p1, G.p1)}${chap(n.p2, G.p2)}`;
  const langItems = pageLangsOf(active || "index").map(l =>
    `<a href="${linkOf(active || "index", l)}" class="${l === lang ? "active" : ""}"><span class="flag svg-flag">${flagOf(l)}</span><span class="lang-name">${LANG_META[l]?.name || l}</span></a>`
  ).join("");
  return `<aside id="sovereign-navigation" class="tome-nav" aria-label="Ledger index">
  <a class="tome-brand" href="${linkOf("index", lang)}">
    <span class="brand-seal">${ICON.crown}</span>
    <span class="brand-name">${esc(siteI18n(lang).name)}<small>${esc(c.brandSub)}</small></span>
  </a>
  ${gameSwitch(lang, active)}
  ${chapters}
  <div class="tome-lang"><div class="lang-label">${esc(n.langLabel)}</div>${langItems}</div>
  ${(active || "").startsWith("sandustry") ? `<p class="lang-note">${lang === "zh-CN" ? "可用语言：English · 한국어 · 简体中文" : lang === "ko" ? "가능한 언어: English · 한국어 · 简体中文" : "Available in: English · 한국어 · 简体中文"}</p>` : ""}
</aside>`;
}

const CONSENT_I18N = {
  "en": { settings: "Privacy settings", title: "Privacy choices", intro: "Choose whether this site may load optional analytics. Advertising providers are currently disabled.", introOn: "Choose whether this site may load optional analytics and advertising.", analytics: "Analytics", analyticsHelp: "If enabled, Google Analytics 4 may process your IP address, device/browser details, page, referrer, approximate region and identifiers for measurement.", ads: "Advertising", adsHelp: "Google AdSense serving and Adsterra are currently disabled, so no advertising script will load. A future provider change must use a new consent version.", adsHelpOn: "If enabled, advertising from Adsterra may load. Google AdSense serving is currently disabled. A future provider change must use a new consent version.", accept: "Accept available", reject: "Reject", manage: "Manage options", save: "Save choices", withdraw: "Withdraw optional consent", close: "Close privacy choices" },
  "zh-CN": { settings: "隐私设置", title: "隐私选择", intro: "请选择本站是否可以加载可选统计服务。广告服务目前均已关闭。", introOn: "请选择本站是否可以加载可选统计服务与广告。", analytics: "统计分析", analyticsHelp: "启用后，Google Analytics 4 可能为统计处理 IP 地址、设备/浏览器信息、访问页面、来源页面、大致地区与标识符。", ads: "广告", adsHelp: "Google AdSense 投放与 Adsterra 目前均已关闭，不会加载广告脚本；未来如更换服务商，必须使用新的同意版本。", adsHelpOn: "同意后，Adsterra 广告可能会加载；Google AdSense 投放目前仍关闭。未来如更换服务商，必须使用新的同意版本。", accept: "同意可用项目", reject: "不同意", manage: "管理选项", save: "保存选择", withdraw: "撤回可选同意", close: "关闭隐私选择" },
  "ja": { settings: "プライバシー設定", title: "プライバシーの選択", intro: "任意のアクセス解析を読み込むか選択してください。広告サービスは現在無効です。", introOn: "任意のアクセス解析と広告を読み込むか選択してください。", analytics: "アクセス解析", analyticsHelp: "有効にすると、Google Analytics 4 が測定のため IP アドレス、端末・ブラウザー情報、閲覧ページ、参照元、おおよその地域、識別子を処理する場合があります。", ads: "広告", adsHelp: "Google AdSense の配信と Adsterra は現在無効で、広告スクリプトは読み込まれません。将来プロバイダーを変更する場合は新しい同意バージョンが必要です。", adsHelpOn: "同意すると Adsterra の広告が読み込まれる場合があります。Google AdSense の配信は現在無効です。将来プロバイダーを変更する場合は新しい同意バージョンが必要です。", accept: "利用可能な項目に同意", reject: "同意しない", manage: "設定を管理", save: "選択を保存", withdraw: "任意の同意を撤回", close: "プライバシー設定を閉じる" },
  "ko": { settings: "개인정보 설정", title: "개인정보 선택", intro: "선택적 분석 서비스의 로드를 허용할지 선택하세요. 광고 서비스는 현재 비활성화되어 있습니다.", introOn: "선택적 분석 서비스와 광고의 로드를 허용할지 선택하세요.", analytics: "분석", analyticsHelp: "활성화하면 Google Analytics 4가 측정을 위해 IP 주소, 기기·브라우저 정보, 방문 페이지, 유입 경로, 대략적인 지역과 식별자를 처리할 수 있습니다.", ads: "광고", adsHelp: "Google AdSense 게재와 Adsterra는 현재 비활성화되어 광고 스크립트가 로드되지 않습니다. 향후 공급자 변경 시 새 동의 버전이 필요합니다.", adsHelpOn: "동의하면 Adsterra 광고가 로드될 수 있습니다. Google AdSense 게재는 현재 비활성화되어 있습니다. 향후 공급자 변경 시 새 동의 버전이 필요합니다.", accept: "사용 가능한 항목 동의", reject: "거부", manage: "옵션 관리", save: "선택 저장", withdraw: "선택적 동의 철회", close: "개인정보 선택 닫기" },
  "fr": { settings: "Réglages de confidentialité", title: "Choix de confidentialité", intro: "Choisissez si ce site peut charger l'analyse facultative. Les services publicitaires sont actuellement désactivés.", introOn: "Choisissez si ce site peut charger l'analyse facultative et la publicité.", analytics: "Analyse", analyticsHelp: "Si elle est activée, Google Analytics 4 peut traiter l'adresse IP, les informations de l'appareil et du navigateur, la page, le référent, la région approximative et des identifiants à des fins de mesure.", ads: "Publicité", adsHelp: "La diffusion Google AdSense et Adsterra sont actuellement désactivées : aucun script publicitaire n'est chargé. Tout futur changement de fournisseur devra utiliser une nouvelle version de consentement.", adsHelpOn: "Si elle est activée, la publicité Adsterra peut se charger. La diffusion Google AdSense est actuellement désactivée. Tout futur changement de fournisseur devra utiliser une nouvelle version de consentement.", accept: "Accepter les options disponibles", reject: "Refuser", manage: "Gérer les options", save: "Enregistrer", withdraw: "Retirer le consentement facultatif", close: "Fermer les choix de confidentialité" },
  "de": { settings: "Datenschutzeinstellungen", title: "Datenschutzauswahl", intro: "Wählen Sie, ob diese Website optionale Analyse laden darf. Werbedienste sind derzeit deaktiviert.", introOn: "Wählen Sie, ob diese Website optionale Analyse und Werbung laden darf.", analytics: "Analyse", analyticsHelp: "Bei Aktivierung kann Google Analytics 4 IP-Adresse, Geräte- und Browserdaten, besuchte Seite, Referrer, ungefähre Region und Kennungen zur Messung verarbeiten.", ads: "Werbung", adsHelp: "Google-AdSense-Auslieferung und Adsterra sind derzeit deaktiviert; es wird kein Werbeskript geladen. Ein künftiger Anbieterwechsel erfordert eine neue Einwilligungsversion.", adsHelpOn: "Bei Zustimmung können Anzeigen von Adsterra geladen werden. Die Google-AdSense-Auslieferung ist derzeit deaktiviert. Ein künftiger Anbieterwechsel erfordert eine neue Einwilligungsversion.", accept: "Verfügbare Optionen akzeptieren", reject: "Ablehnen", manage: "Optionen verwalten", save: "Auswahl speichern", withdraw: "Optionale Einwilligung widerrufen", close: "Datenschutzauswahl schließen" }
};

function consentUi(lang) {
  const t = CONSENT_I18N[lang] || CONSENT_I18N.en;
  const rawAdsterra = String(DATA.site.adsterra || "");
  const adsterraSrc = (rawAdsterra.match(/src="([^"]*\/invoke\.js)"/) || [])[1] || "";
  const adsterraContainer = (rawAdsterra.match(/id="(container-[^"]+)"/) || [])[1] || "";
  const advertisingAvailable = Boolean(ADSENSE_SCRIPT_SRC || adsterraSrc);
  const cfg = JSON.stringify({ gaId: DATA.site.gaId || "", adsenseSrc: ADSENSE_SCRIPT_SRC, adsterraSrc, adsterraContainer, advertisingAvailable });
  const intro = advertisingAvailable ? (t.introOn || t.intro) : t.intro;
  const adsHelp = advertisingAvailable ? (t.adsHelpOn || t.adsHelp) : t.adsHelp;
  return `<button type="button" class="privacy-settings" data-consent-settings aria-haspopup="dialog" aria-controls="privacy-consent-dialog" aria-expanded="false">${esc(t.settings)}</button>
  <dialog id="privacy-consent-dialog" class="consent-dialog" data-consent-dialog aria-labelledby="privacy-consent-title">
    <div class="consent-card">
      <button type="button" class="consent-close" data-consent-close aria-label="${esc(t.close)}">×</button>
      <h2 id="privacy-consent-title" tabindex="-1">${esc(t.title)}</h2><p>${esc(intro)}</p>
      <div class="consent-summary"><b>${esc(t.analytics)}</b><span>${esc(t.analyticsHelp)}</span><b>${esc(t.ads)}</b><span>${esc(adsHelp)}</span></div>
      <div class="consent-manage" data-consent-manage hidden>
        <label><input type="checkbox" data-consent-analytics> <span><b>${esc(t.analytics)}</b><small>${esc(t.analyticsHelp)}</small></span></label>
        <label><input type="checkbox" data-consent-advertising> <span><b>${esc(t.ads)}</b><small>${esc(adsHelp)}</small></span></label>
      </div>
      <div class="consent-actions">
        <button type="button" data-consent-accept>${esc(t.accept)}</button>
        <button type="button" data-consent-reject>${esc(t.reject)}</button>
        <button type="button" data-consent-manage-open>${esc(t.manage)}</button>
        <button type="button" data-consent-save hidden>${esc(t.save)}</button>
        <button type="button" data-consent-withdraw hidden>${esc(t.withdraw)}</button>
      </div>
    </div>
  </dialog><div id="consent-ad-slot" aria-hidden="true"></div>
  <script>
  (function(){
    var cfg=${cfg}, key="cozysimhub-consent-v1", dialog=document.querySelector("[data-consent-dialog]");
    var settings=document.querySelector("[data-consent-settings]"), opener=null, loaded={analytics:false,adsense:false,adsterra:false};
    function read(){try{var v=JSON.parse(localStorage.getItem(key)||"null");return v&&typeof v.analytics==="boolean"&&typeof v.advertising==="boolean"?v:null;}catch(_){return null;}}
    function loadAnalytics(){if(loaded.analytics||!cfg.gaId)return;loaded.analytics=true;window.dataLayer=window.dataLayer||[];window.gtag=window.gtag||function(){dataLayer.push(arguments);};gtag("js",new Date());gtag("config",cfg.gaId);var s=document.createElement("script");s.async=true;s.src="https://www.googletagmanager.com/gtag/js?id="+encodeURIComponent(cfg.gaId);document.head.appendChild(s);}
    function loadAdvertising(){var slot=document.getElementById("consent-ad-slot");if(cfg.adsenseSrc&&!loaded.adsense){loaded.adsense=true;var g=document.createElement("script");g.async=true;g.crossOrigin="anonymous";g.src=cfg.adsenseSrc;slot.appendChild(g);}if(cfg.adsterraSrc&&!loaded.adsterra){loaded.adsterra=true;if(cfg.adsterraContainer){var d=document.createElement("div");d.id=cfg.adsterraContainer;slot.appendChild(d);}var a=document.createElement("script");a.async=true;a.setAttribute("data-cfasync","false");a.src=cfg.adsterraSrc;slot.appendChild(a);}}
    function apply(v){if(v&&v.analytics)loadAnalytics();if(v&&v.advertising&&cfg.advertisingAvailable)loadAdvertising();}
    function close(){if(dialog.open)dialog.close();settings.setAttribute("aria-expanded","false");if(opener&&opener.focus)opener.focus();}
    function open(source){opener=source||document.activeElement;var v=read();dialog.querySelector("[data-consent-analytics]").checked=!!(v&&v.analytics);var advertising=dialog.querySelector("[data-consent-advertising]");advertising.checked=!!(v&&v.advertising&&cfg.advertisingAvailable);advertising.disabled=!cfg.advertisingAvailable;dialog.querySelector("[data-consent-manage]").hidden=true;dialog.querySelector("[data-consent-save]").hidden=true;dialog.querySelector("[data-consent-withdraw]").hidden=!v;settings.setAttribute("aria-expanded","true");dialog.showModal();dialog.querySelector("#privacy-consent-title").focus();}
    function save(v){v.advertising=!!(v.advertising&&cfg.advertisingAvailable);localStorage.setItem(key,JSON.stringify(v));apply(v);close();}
    settings.addEventListener("click",function(){open(settings);});
    dialog.querySelector("[data-consent-close]").addEventListener("click",close);
    dialog.querySelector("[data-consent-accept]").addEventListener("click",function(){save({analytics:true,advertising:cfg.advertisingAvailable});});
    dialog.querySelector("[data-consent-reject]").addEventListener("click",function(){save({analytics:false,advertising:false});});
    dialog.querySelector("[data-consent-manage-open]").addEventListener("click",function(){dialog.querySelector("[data-consent-manage]").hidden=false;dialog.querySelector("[data-consent-save]").hidden=false;});
    dialog.querySelector("[data-consent-save]").addEventListener("click",function(){save({analytics:dialog.querySelector("[data-consent-analytics]").checked,advertising:dialog.querySelector("[data-consent-advertising]").checked});});
    dialog.querySelector("[data-consent-withdraw]").addEventListener("click",function(){save({analytics:false,advertising:false});});
    dialog.addEventListener("cancel",function(){setTimeout(function(){settings.setAttribute("aria-expanded","false");if(opener&&opener.focus)opener.focus();},0);});
    var initial=read();if(initial)apply(initial);else setTimeout(function(){open(settings);},0);
  })();
  </script>`;
}
function renderAmazonAffiliate(lang) {
  const n = navI18n(lang);
  const tag = "cozysimhub20-20";
  const items = [
    { label: n.amazon1, q: "gaming keyboard" },
    { label: n.amazon2, q: "gaming mouse" },
    { label: n.amazon3, q: "gaming headset" },
    { label: n.amazon4, q: "game controller" },
    { label: n.amazon5, q: "gaming monitor" }
  ];
  const links = items.map(it => `<a href="https://www.amazon.com/s?k=${encodeURIComponent(it.q)}&tag=${tag}" target="_blank" rel="sponsored noopener nofollow">${esc(it.label)}</a>`).join("");
  return `<div class="amazon-gear">
    <h3>${esc(n.amazonTitle)}</h3>
    <div class="amazon-gear-links">${links}</div>
    <p class="aff-note">${esc(n.amazonNote)}</p>
  </div>`;
}

function footer(lang, slug) {
  const n = navI18n(lang);
  const c = catI18n(lang);
  const key = DATA.pages.slice(0, 8).map(p => `<a href="${linkOf(p.slug, lang)}">${esc(pageOf(p, lang).title)}</a>`).join("");
  const steamHref = (slug || "").startsWith("sandustry")
    ? "https://store.steampowered.com/app/2764460/Sandustry/"
    : DATA.game.steamUrl;
  return `<footer class="colophon">
  <div>
    <h3>${esc(siteI18n(lang).name)}</h3>
    <p>${esc(slug === "index" ? c.footerNote : n.footerNote)}</p>
    <p>${esc(n.footerSource)} · ${esc(n.updated)} ${TODAY}</p>
  </div>
  <div>
    <div class="colophon-links">
      <a href="${linkOf("about", lang)}">${esc(n.about)}</a>
      <a href="${linkOf("privacy", lang)}">${esc(n.privacy)}</a>
      <a href="${linkOf("contact", lang)}">${esc(n.contact)}</a>
      <a href="${esc(steamHref)}" target="_blank" rel="noopener">Steam ↗</a>
      ${key}
    </div>
    <p class="colophon-legal">© ${COPYRIGHT_YEAR} ${esc(DATA.site.domain)} · ${lang === "zh-CN" ? "非官方粉丝站" : "Unofficial fan site"}</p>
  </div>
  ${renderAmazonAffiliate(lang)}
</footer>
${KIT.decisionEventsScript()}
<script>
document.addEventListener('DOMContentLoaded', function(){
  var toggle = document.querySelector('.tome-nav-toggle');
  var nav = document.querySelector('.tome-nav');
  var overlay = document.querySelector('.tome-nav-overlay');
  if (toggle && nav && overlay) {
    function setNavigation(open, returnFocus){nav.classList.toggle('open',open);overlay.classList.toggle('show',open);toggle.setAttribute('aria-expanded',open?'true':'false');if(!open&&returnFocus)toggle.focus();}
    toggle.addEventListener('click', function(){ setNavigation(!nav.classList.contains('open'), false); });
    overlay.addEventListener('click', function(){ setNavigation(false, true); });
    document.addEventListener('keydown', function(e){ if (e.key === 'Escape' && nav.classList.contains('open')) { setNavigation(false, true); } });
  }
  var obs = new IntersectionObserver(function(es){
    es.forEach(function(en){ if(en.isIntersecting){ en.target.classList.add('in'); obs.unobserve(en.target); } });
  }, {threshold:.08});
  document.querySelectorAll('.reveal').forEach(function(el){ obs.observe(el); });
  var tocLinks = Array.prototype.slice.call(document.querySelectorAll('.page-folio nav a'));
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
${consentUi(lang)}`;
}
/* ---------- Section 渲染（手账组件语言） ---------- */
function renderSection(s, lang) {
  const escTxt = esc(s.heading || "");
  const secId = s._tocId ? ` id="${s._tocId}"` : "";
  const tag = s.tag ? `<span class="tag">${esc(s.tag)}</span>` : "";
  switch (s.type) {
    case "steps": {
      const items = (s.items || []).map((it, i) =>
        `<li class="work-ticket reveal">
          <span class="ticket-no">№ ${String(i + 1).padStart(2, "0")}</span>
          <div class="ticket-body"><h3>${esc(it[0])}</h3><p>${esc(it[1])}</p></div>
        </li>`).join("");
      return `<section class="ledger-section"${secId}><div class="section-head">${tag}<h2>${escTxt}</h2></div><ol class="work-tickets">${items}</ol></section>`;
    }
    case "list": {
      const items = (s.items || []).map(it =>
        (it && typeof it === "object" && it.href)
          ? `<li><a href="${esc(it.href)}">${esc(it.text)}</a></li>`
          : `<li>${esc(it)}</li>`).join("");
      return `<section class="ledger-section"${secId}><div class="section-head">${tag}<h2>${escTxt}</h2></div><ul class="ledger-notes">${items}</ul></section>`;
    }
    case "table": {
      const th = (s.headers || []).map(h => `<th scope="col">${esc(h)}</th>`).join("");
      const tr = (s.rows || []).map(r => `<tr>${r.map(c => `<td>${esc(c)}</td>`).join("")}</tr>`).join("");
      return `<section class="ledger-section"${secId}><div class="section-head">${tag}<h2>${escTxt}</h2></div><div class="ledger-table-wrap"><table class="ledger-table"><thead><tr>${th}</tr></thead><tbody>${tr}</tbody></table></div></section>`;
    }
    case "faq": {
      const items = (s.items || []).map((qa, i) =>
        `<details class="faq-item" ${i === 0 ? "open" : ""}><summary>${esc(qa[0])}</summary><p>${esc(qa[1])}</p></details>`).join("");
      return `<section class="ledger-section"${secId}><div class="section-head">${tag}<h2>${escTxt}</h2></div><div class="faq-list">${items}</div></section>`;
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

/* ---------- 首页（品类枢纽 hub 四段式 —— spec §A.1） ---------- */
/* 本地 JSON-LD 构造器（不改 site-kit；spec §D.1） */
function ldOrganization() {
  return { "@context": "https://schema.org", "@type": "Organization", name: "CozySimHub", url: `https://${DATA.site.domain}/` };
}
function ldVideoGame(g, lang) {
  const langs = (g.languages && g.languages.length) ? g.languages : LANGS;
  const useLang = langs.includes(lang) ? lang : DEF;   // 只指向真实存在的语言 URL
  const item = { "@type": "VideoGame", name: g.name, url: urlOf(g.hubSlug, useLang), inLanguage: "en" };
  const m = g.videoGame || {};
  if (m.genre) item.genre = m.genre;
  if (m.developer) item.developer = m.developer;
  if (m.publisher) item.publisher = m.publisher;
  if (m.datePublished) item.datePublished = m.datePublished;
  if (m.image) item.image = `https://${DATA.site.domain}${m.image}`;
  return item;
}
function ldItemList(games, lang) {
  return {
    "@context": "https://schema.org", "@type": "ItemList",
    name: catI18n(lang).hubTitle,
    itemListElement: games.map((g, i) => ({ "@type": "ListItem", position: i + 1, item: ldVideoGame(g, lang) }))
  };
}

/* 最新内容：从 games.json latest 收集（数据驱动，不硬编码 —— spec §A.5） */
function latestItems(lang, max = 6) {
  const rows = [];
  for (const g of GAMES) {
    for (const it of (g.latest || [])) {
      const p = DATA.pages.find(x => x.slug === it.slug);
      if (!p) continue;
      rows.push({ game: g, slug: it.slug, date: it.date || TODAY });
    }
  }
  rows.sort((a, b) => (b.date || "").localeCompare(a.date || ""));
  return rows.slice(0, max);
}
function latestListHtml(lang) {
  const c = catI18n(lang);
  return latestItems(lang).map(({ game, slug, date }) => {
    const p = DATA.pages.find(x => x.slug === slug);
    const title = pageOf(p, lang).title;
    const gname = game.nameI18n[lang] || game.name;
    return `<div class="latest-item"><span class="latest-tag" data-accent="${esc(game.accent)}">${esc(gname)}</span><a href="${linkOf(slug, lang)}">${esc(title)}</a><span class="latest-date">${esc(c.updated)} ${esc(date)}</span></div>`;
  }).join("");
}
/* hub 页侧栏「最新内容」快捷链接（spec §A.3：章节区可空或放最新链接） */
function latestNav(lang) {
  const c = catI18n(lang);
  const items = latestItems(lang, 5).map(({ game, slug }) => {
    const p = DATA.pages.find(x => x.slug === slug);
    if (!p) return "";
    return `<a href="${linkOf(slug, lang)}"><span class="folio-no">${GAME_ICON[game.icon] || ""}</span><span>${esc(pageOf(p, lang).title)}</span></a>`;
  }).join("");
  return `<div class="tome-chapter"><b>${esc(c.secLatest)}</b>${items}</div>`;
}

/* 游戏切换器（tome-nav 顶部，品牌下方 —— spec §A.3） */
function gameSwitch(lang, active) {
  const c = catI18n(lang);
  const items = GAMES.map(g => {
    const name = g.nameI18n[lang] || g.name;
    const current = (active || "").startsWith(g.id);
    return `<a class="game-switch-item${current ? " active" : ""}" href="${linkOf(g.hubSlug, lang)}"${current ? ' aria-current="page"' : ""}>${GAME_ICON[g.icon] || ICON.crown}<span>${esc(name)}</span></a>`;
  }).join("");
  return `<nav class="game-switch" aria-label="${esc(c.switchLabel)}">${items}</nav>`;
}

/* 游戏卡片（spec §A.2） */
function gameCard(g, lang) {
  const c = catI18n(lang);
  const name = g.nameI18n[lang] || g.name;
  const tagline = g.taglineI18n[lang] || g.taglineI18n.en || "";
  const hub = linkOf(g.hubSlug, lang);
  const badges = (g.badges || []).map(b => {
    const label = (b.labelI18n || {})[lang] || (b.labelI18n || {}).en || "";
    return `<li class="badge"><b>${esc(b.value)}</b>${label ? ` ${esc(label)}` : ""}</li>`;
  }).join("");
  const links = (g.coreLinks || []).map(slug => {
    const p = DATA.pages.find(x => x.slug === slug);
    if (!p) return "";
    return `<li><a href="${linkOf(slug, lang)}">${esc(pageOf(p, lang).title)}</a></li>`;
  }).join("");
  // 封面带：cover.src 存在才渲染位图（width/height 防 CLS），否则渐变 + SVG 徽记（spec §B.2.4）
  const cover = g.cover
    ? `<a class="game-cover" href="${hub}"><img class="game-cover-img" src="${esc(g.cover.src)}" srcset="${esc(g.cover.src.replace(/\.jpg$/, "-640.jpg 640w, ") + g.cover.src.replace(/\.jpg$/, "-1280.jpg 1280w, ") + g.cover.src + " 1600w")}" sizes="(max-width: 720px) 640px, 1280px" alt="${esc(g.cover.alt || name)}" width="${esc(g.cover.width)}" height="${esc(g.cover.height)}" loading="lazy" /></a>`
    : `<a class="game-cover game-cover-icon" style="background:linear-gradient(135deg,var(--accent-${g.accent}-tint),var(--accent-${g.accent}))" href="${hub}" aria-hidden="true" tabindex="-1">${GAME_ICON[g.icon] || ICON.crown}</a>`;
  return `<article class="game-card" data-game="${esc(g.id)}">
    ${cover}
    <div class="game-body">
      <h2 class="game-name">${esc(name)}</h2>
      ${tagline ? `<p class="game-tagline">${esc(tagline)}</p>` : ""}
      ${badges ? `<ul class="game-badges">${badges}</ul>` : ""}
      ${links ? `<ul class="game-links">${links}</ul>` : ""}
      <a class="game-all" href="${hub}">${esc(c.allGuides)}</a>
    </div>
  </article>`;
}

/* 品类价值主张（spec §A.1 段 3） */
function valueGrid(lang) {
  const c = catI18n(lang);
  const items = [
    { icon: "scroll", title: c.v1Title, text: c.v1Text },
    { icon: "book", title: c.v2Title, text: c.v2Text },
    { icon: "calc", title: c.v3Title, text: c.v3Text }
  ].map(v => `<div class="value-item"><span class="value-ic">${ICON[v.icon]}</span><h3>${esc(v.title)}</h3><p>${esc(v.text)}</p></div>`).join("");
  return `<div class="value-grid">${items}</div>`;
}

function renderHome(lang) {
  const t = pageOf(DATA.pages.find(p => p.slug === "index"), lang);
  const c = catI18n(lang);
  const cards = GAMES.map(g => gameCard(g, lang)).join("");
  const body = `<div class="app-main"><button class="tome-nav-toggle" type="button" aria-label="Toggle ledger" aria-controls="sovereign-navigation" aria-expanded="false"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 6h16M4 12h16M4 18h16"/></svg>${lang === "zh-CN" ? "圆桌手账目录" : "Ledger Index"}</button>
<div class="tome-nav-overlay"></div>
<main class="page-main hub-main">
  <section class="hub-hero">
    <span class="hub-eyebrow reveal">${esc(c.hubEyebrow)}</span>
    <h1 class="hub-title reveal" style="transition-delay:.04s">${esc(c.hubTitle)}</h1>
    <p class="hub-sub reveal" style="transition-delay:.08s">${esc(c.hubSub)}</p>
    <div class="hub-cta">
      <a class="btn btn-primary" href="#games">${esc(c.ctaBrowse)}</a>
      <a class="btn btn-ghost" href="#latest">${esc(c.ctaLatest)}</a>
    </div>
  </section>
  <section id="games" class="hub-section reveal">
    <h2 class="hub-section-title">${esc(c.secGames)}</h2>
    <div class="game-grid">${cards}</div>
  </section>
  <section class="hub-section hub-value reveal">
    <h2 class="hub-section-title">${esc(c.secValue)}</h2>
    ${valueGrid(lang)}
  </section>
  <section id="latest" class="hub-section hub-latest reveal">
    <h2 class="hub-section-title">${esc(c.secLatest)}</h2>
    <div class="latest-list">${latestListHtml(lang)}</div>
  </section>
</main>`;
  const ld = [ldOrganization(), ldItemList(GAMES, lang)];
  return head(t.metaTitle || t.title, t.metaDescription, ld, "index", lang) + header(lang, "index") + body + footer(lang, "index");
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
  // 章回目录（sections 的 heading 生成 TOC）
  const secs = t.sections || [];
  const tocEntries = secs.map((s, i) => {
    if (!s.heading) return "";
    const id = `sec-${i}`;
    return `<a href="#${id}"><span class="toc-no">${String(i + 1).padStart(2, "0")}</span><span>${esc(s.heading)}</span></a>`;
  }).filter(Boolean);
  const tocItems = tocEntries.join("");
  // 搜索框只在目录足够长（>=5 条）时渲染；短目录（如 Sandustry 0-3 条）不显示，避免占位空洞
  const tocSearchHtml = tocEntries.length >= 5
    ? `<div class="toc-search"><input type="search" placeholder="${esc(navI18n(lang).search)}" aria-label="${esc(navI18n(lang).searchLabel)}" onkeyup="var q=this.value.toLowerCase();document.querySelectorAll('.page-folio nav a').forEach(function(a){a.style.display=a.textContent.toLowerCase().includes(q)?'':'none';});" /></div>`
    : "";
  const sections = secs.map((s, i) => {
    const withId = { ...s, _tocId: `sec-${i}` };
    return renderSection(withId, lang);
  }).join("");
  const imgMap = { "sovereign-tower/how-to-play": "how-to-play", "sovereign-tower/knights": "knights", "sovereign-tower/secret-knights": "secret-knights", "sovereign-tower/romance": "romance", "sovereign-tower/endings": "endings", "sovereign-tower/recipes": "recipes", "sovereign-tower/quest-mechanics": "quest-mechanics", "sovereign-tower/achievements": "achievements" };
  const pageImg = imgMap[p.slug];
  const art = pageImg ? `<img class="page-art reveal" src="/images/${pageImg}-640.jpg" srcset="/images/${pageImg}-640.jpg 640w, /images/${pageImg}-1280.jpg 1280w, /images/${pageImg}.jpg 1600w" sizes="(max-width: 720px) 640px, 1280px" alt="${esc(t.title)}" width="900" height="506" loading="lazy" />` : "";
  const body = `<div class="app-main"><button class="tome-nav-toggle" type="button" aria-label="Toggle ledger" aria-controls="sovereign-navigation" aria-expanded="false"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 6h16M4 12h16M4 18h16"/></svg>${lang === "zh-CN" ? "圆桌手账目录" : "Ledger Index"}</button>
<div class="tome-nav-overlay"></div>
<main class="page-main"><div class="page-shell">
  <aside class="page-folio reveal">
    <div class="folio-cap">${isTool ? (lang === "zh-CN" ? "工具" : "Tools") : (lang === "zh-CN" ? "章回" : "Folio")}</div>
    ${tocSearchHtml}
    <nav>${tocItems}</nav>
  </aside>
  <article class="page-leaf">
    <div class="page-head reveal">
      <span class="leaf-tag">${isTool ? (lang === "zh-CN" ? "工具" : "Tool") : (lang === "zh-CN" ? "圆桌手账" : "Ledger")}</span>
      <h1>${esc(t.title)}</h1>
      ${art}
      <p class="page-intro">${esc(t.intro || "")}</p>
    </div>
    ${sections}
  </article>
  </div></main>`;
  return head(t.metaTitle || t.title, t.metaDescription, ld, p.slug, lang) + header(lang, p.slug) + body + footer(lang, p.slug);
}
/* ---------- 静态页（about/privacy/contact） ---------- */
function renderStatic(slug, lang) {
  const n = navI18n(lang);
  const titleMap = {
    "about": n.about, "privacy": n.privacy, "contact": n.contact,
    "404": `${siteI18n(lang).name} — 404`
  };
  const BODY_I18N = {
    "en": {
      "about": `${esc(siteI18n(lang).name)} is an unofficial fan resource for Sovereign Tower (君王之塔). We research every page against the official Steam store page, fan wiki data and community reports, and clearly mark anything still being verified.`,
      "privacy": "Before you choose, this site does not request Google Analytics 4, Google AdSense serving or Adsterra. If you allow analytics, GA4 may process your IP address, device and browser information, visited page, referrer, approximate region, and cookies or similar identifiers for measurement. Your choice is stored locally in your browser under cozysimhub-consent-v1; reject keeps optional providers blocked. The persistent Privacy settings control lets you change or withdraw your choice, which prevents new optional-provider requests on later page loads. Google AdSense ownership metadata and ads.txt are configured, but ad serving is disabled; Adsterra may load only if you accept advertising, and Google AdSense serving remains disabled. Google Fonts stylesheets load independently before your choice and Google may receive standard network data. Cloudflare hosting may keep standard access logs. We do not claim to use a Google-certified CMP.",
      "contact": "Corrections or questions? Contact us via the site's GitHub repository or email.",
      "404": "The page you are looking for was not found. Return to the guide hub."
    },
    "zh-CN": {
      "about": "本站是非官方粉丝资源站，服务于《君王之塔》(Sovereign Tower)。我们逐页核对 Steam 官方商店页、粉丝 wiki 数据与社区报告，未核实的部分明确标注。",
      "privacy": "在您作出选择前，本站不会请求 Google Analytics 4、Google AdSense 投放或 Adsterra。若允许统计分析，GA4 可能为统计处理您的 IP 地址、设备和浏览器信息、访问页面、来源页面、大致地区，以及 Cookie 或类似标识符。您的选择仅以 cozysimhub-consent-v1 保存在本地浏览器中；选择不同意会继续阻止所有可选服务。您可随时使用固定显示的“隐私设置”更改或撤回选择，撤回后后续页面加载不会再发出新的可选服务请求。Google AdSense 仅配置了所有权验证元数据与 ads.txt，广告投放仍关闭；Adsterra 仅在您同意广告后可能加载，Google AdSense 投放保持关闭。Google Fonts 样式表会在选择前独立加载，Google 可能收到常规网络数据；Cloudflare 托管服务也可能保留标准访问日志。本站不声称使用 Google 认证的 CMP。",
      "contact": "勘误或疑问？请通过本站 GitHub 仓库或邮箱联系。",
      "404": "未找到您访问的页面。返回攻略中心。"
    },
    "ja": {
      "about": "当サイトは『ソブリンタワー』(Sovereign Tower) の非公式ファンサイトです。Steam公式ストア・ファンwiki・コミュニティ報告を基準に各ページを調査し、未検証の内容は明記しています。",
      "privacy": "選択前に、当サイトは Google Analytics 4、Google AdSense の広告配信、Adsterra を要求しません。アクセス解析を許可すると、GA4 が測定のため IP アドレス、端末・ブラウザー情報、閲覧ページ、参照元、おおよその地域、Cookie または類似識別子を処理する場合があります。選択はブラウザー内に cozysimhub-consent-v1 として保存され、拒否すると任意サービスはブロックされたままです。常時表示されるプライバシー設定から変更・撤回でき、撤回後のページ読み込みでは新たな任意サービス要求を防ぎます。Google AdSense は所有権確認メタデータと ads.txt のみ設定済みで広告配信は無効、Adsterra は広告への同意後にのみ読み込まれる場合があり、Google AdSense の配信は無効のままです。Google Fonts のスタイルシートは選択前に独立して読み込まれ、Google が標準的なネットワークデータを受け取る場合があります。Cloudflare は標準アクセスログを保持する場合があります。当サイトは Google 認定 CMP の使用をうたいません。",
      "contact": "誤りや質問は、GitHub リポジトリまたはメールでご連絡ください。",
      "404": "お探しのページは見つかりませんでした。攻略センターへ戻る。"
    },
    "ko": {
      "about": "이 사이트는 『소버린 타워』(Sovereign Tower)의 비공식 팬 리소스입니다. Steam 공식 스토어, 팬 위키, 커뮤니티 보고를 기준으로 조사하며, 검증되지 않은 내용은 명확히 표시합니다.",
      "privacy": "선택 전에는 Google Analytics 4, Google AdSense 광고 게재 또는 Adsterra를 요청하지 않습니다. 분석을 허용하면 GA4가 측정을 위해 IP 주소, 기기·브라우저 정보, 방문 페이지, 유입 경로, 대략적인 지역과 쿠키 또는 유사 식별자를 처리할 수 있습니다. 선택은 브라우저에 cozysimhub-consent-v1로 로컬 저장되며, 거부하면 선택적 공급자가 계속 차단됩니다. 항상 표시되는 개인정보 설정에서 변경하거나 철회할 수 있고, 철회 후의 페이지 로드에서는 새로운 선택적 공급자 요청이 차단됩니다. Google AdSense는 소유권 확인 메타데이터와 ads.txt만 설정되어 있고 광고 게재는 비활성화되어 있으며, Adsterra는 광고에 동의한 경우에만 로드될 수 있고 Google AdSense 게재는 비활성화 상태로 유지됩니다. Google Fonts 스타일시트는 선택 전에 별도로 로드되어 Google이 표준 네트워크 데이터를 받을 수 있습니다. Cloudflare 호스팅은 표준 접속 로그를 보관할 수 있습니다. 이 사이트는 Google 인증 CMP 사용을 주장하지 않습니다.",
      "contact": "오류나 문의는 GitHub 리포지토리 또는 이메일로 연락해 주세요.",
      "404": "요청하신 페이지를 찾을 수 없습니다. 가이드 허브로 돌아가기."
    },
    "fr": {
      "about": "Ce site est une ressource de fans non officielle pour Sovereign Tower (君王之塔). Nous vérifions chaque page sur la page Steam officielle, les wikis de fans et les rapports de la communauté.",
      "privacy": "Avant votre choix, ce site ne demande ni Google Analytics 4, ni diffusion Google AdSense, ni Adsterra. Si vous autorisez l'analyse, GA4 peut traiter l'adresse IP, les informations de l'appareil et du navigateur, la page visitée, le référent, la région approximative et des cookies ou identifiants similaires pour la mesure. Votre choix est stocké localement dans le navigateur sous cozysimhub-consent-v1 ; un refus maintient les services facultatifs bloqués. Le bouton permanent Réglages de confidentialité permet de modifier ou retirer ce choix, empêchant de nouvelles requêtes facultatives lors des chargements suivants. Les métadonnées de propriété Google AdSense et ads.txt sont configurées, mais la diffusion publicitaire est désactivée ; Adsterra ne peut se charger que si vous acceptez la publicité, et la diffusion Google AdSense reste désactivée. Les feuilles de style Google Fonts se chargent séparément avant le choix et Google peut recevoir des données réseau standard. L'hébergement Cloudflare peut conserver des journaux d'accès standard. Ce site ne prétend pas utiliser une CMP certifiée par Google.",
      "contact": "Corrections ou questions ? Contactez-nous via le dépôt GitHub ou par e-mail.",
      "404": "Page introuvable. Retour au hub de guides."
    },
    "de": {
      "about": "Diese Seite ist eine inoffizielle Fan-Ressource für Sovereign Tower (君王之塔). Wir prüfen jede Seite gegen den offiziellen Steam-Store, Fan-Wikis und Community-Berichte.",
      "privacy": "Vor Ihrer Auswahl fordert diese Website weder Google Analytics 4 noch Google-AdSense-Auslieferung oder Adsterra an. Wenn Sie Analyse erlauben, kann GA4 IP-Adresse, Geräte- und Browserdaten, besuchte Seite, Referrer, ungefähre Region sowie Cookies oder ähnliche Kennungen zur Messung verarbeiten. Ihre Auswahl wird als cozysimhub-consent-v1 lokal im Browser gespeichert; eine Ablehnung hält optionale Anbieter blockiert. Über die ständig sichtbaren Datenschutzeinstellungen können Sie die Auswahl ändern oder widerrufen; danach werden bei späteren Seitenaufrufen keine neuen optionalen Anbieteranfragen gesendet. Für Google AdSense sind nur Eigentumsmetadaten und ads.txt eingerichtet, die Anzeigenauslieferung ist deaktiviert; Adsterra kann nur geladen werden, wenn Sie Werbung akzeptieren, und die Google-AdSense-Auslieferung bleibt deaktiviert. Google-Fonts-Stylesheets werden unabhängig vor der Auswahl geladen und Google kann Standard-Netzwerkdaten erhalten. Cloudflare-Hosting kann Standard-Zugriffsprotokolle führen. Diese Website behauptet nicht, eine von Google zertifizierte CMP zu verwenden.",
      "contact": "Korrekturen oder Fragen? Kontakt über das GitHub-Repository oder per E-Mail.",
      "404": "Seite nicht gefunden. Zurück zum Guide-Hub."
    }
  };
  const bodyMap = BODY_I18N[lang] || BODY_I18N.en;
  const body = `<div class="app-main"><button class="tome-nav-toggle" type="button" aria-label="Toggle ledger" aria-controls="sovereign-navigation" aria-expanded="false"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 6h16M4 12h16M4 18h16"/></svg>${lang === "zh-CN" ? "圆桌手账目录" : "Ledger Index"}</button>
<div class="tome-nav-overlay"></div>
<main class="page-main"><div class="page-shell"><article class="page-leaf"><div class="page-head"><h1>${esc(titleMap[slug])}</h1></div><p>${bodyMap[slug]}</p></article></div></main>`;
  const dhi = lang.startsWith("zh") || lang.startsWith("ja") || lang.startsWith("ko") ? 78 : 158;
  const desc = bodyMap[slug].length > dhi ? bodyMap[slug].slice(0, dhi - 1).trimEnd() + "…" : bodyMap[slug];
  return head(titleMap[slug], desc, [], slug, lang) + header(lang, slug) + body + footer(lang, slug);
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


/* ================= 月光档案室主题（Moonlight Peaks · 独立骨架） ================= */
const MOON_LABELS = {
  "en": { data: "The Ledger", deep: "Deep Dives", quick: "Quick Answers", search: "Search this table…", langLabel: "Language", home: "Moonlight Peaks", hub: "Back to Sovereign Tower Hub", footerNote: "Unofficial fan site — Moonlight Peaks and its assets belong to Little Chicken / XSEED Games / Marvelous Europe.",
          footerSource: "Information verified against the official Steam store page and cited guides.", updated: "Updated", ledger: "The Moonlit Ledger" },
  "zh-CN": { data: "数据账页", deep: "深潜", quick: "快答", search: "搜索本表…", langLabel: "语言", home: "月光小镇", hub: "返回君王之塔攻略中心", footerNote: "非官方粉丝站——《月光小镇》及相关资产归 Little Chicken / XSEED Games / Marvelous Europe 所有。",
             footerSource: "信息核对自 Steam 官方商店页与标注来源的攻略。", updated: "更新于", ledger: "月光档案室" },
  "ja": { data: "データ帳簿", deep: "深掘り", quick: "クイック", search: "この表を検索…", langLabel: "言語", home: "ムーンライトピークス", hub: "ソブリンタワー攻略ハブへ戻る", footerNote: "非公式ファンサイト。本ゲームおよび関連アセットは Little Chicken / XSEED Games / Marvelous Europe に帰属します。",
          footerSource: "情報は Steam 公式ストアと引用元ガイドで確認。", updated: "更新", ledger: "月光の帳簿" },
  "ko": { data: "데이터 장부", deep: "심층", quick: "빠른 답변", search: "이 표 검색…", langLabel: "언어", home: "문라이트 피크스", hub: "소버린 타워 허브로 돌아가기", footerNote: "비공식 팬 사이트. 게임 및 관련 자산은 Little Chicken / XSEED Games / Marvelous Europe에 귀속됩니다.",
          footerSource: "정보는 Steam 공식 스토어와 인용된 가이드로 확인했습니다.", updated: "업데이트", ledger: "문빛 장부" },
  "fr": { data: "Le registre", deep: "Analyses", quick: "Réponses rapides", search: "Rechercher dans ce tableau…", langLabel: "Langue", home: "Moonlight Peaks", hub: "Retour au hub Sovereign Tower", footerNote: "Site de fans non officiel — Moonlight Peaks et ses ressources appartiennent à Little Chicken / XSEED Games / Marvelous Europe.",
          footerSource: "Informations vérifiées sur la page Steam officielle et les guides cités.", updated: "Mis à jour", ledger: "Le registre au clair de lune" },
  "de": { data: "Das Register", deep: "Tiefe Analysen", quick: "Schnelle Antworten", search: "Diese Tabelle durchsuchen…", langLabel: "Sprache", home: "Moonlight Peaks", hub: "Zurück zum Sovereign-Tower-Hub", footerNote: "Inoffizielle Fan-Seite — Moonlight Peaks und seine Assets gehören Little Chicken / XSEED Games / Marvelous Europe.",
          footerSource: "Informationen geprüft gegen den offiziellen Steam-Store und zitierte Guides.", updated: "Aktualisiert", ledger: "Das Mond-Register" },
};
const moonTxt = l => MOON_LABELS[l] || MOON_LABELS.en;

/* 月相 SVG（n=0 新月 … 7 满月） */
function moonPhaseIcon(n, cls) {
  const pct = n / 7;
  return `<svg class="moon-phase ${cls || ""}" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="currentColor" opacity="0.18"/><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="1.4"/><path d="M12 3a9 9 0 0 1 0 18c${(pct * 6).toFixed(1)} 0 ${(pct * 9).toFixed(1)}-${(pct * 4).toFixed(1)} 0-${(pct * 4.5).toFixed(1)}z" fill="currentColor" opacity="0.9"/></svg>`;
}

const MOON_GROUPS = {
  data: ["moonlight-peaks/characters", "moonlight-peaks/how-to-play", "moonlight-peaks/gifts", "moonlight-peaks/romance", "moonlight-peaks/fishing", "moonlight-peaks/flowers", "moonlight-peaks/tools", "moonlight-peaks/achievements"],
  deep: ["moonlight-peaks/spells", "moonlight-peaks/walkthrough", "moonlight-peaks/relationships", "moonlight-peaks/villagers", "moonlight-peaks/potions", "moonlight-peaks/museum", "moonlight-peaks/breeding"],
  quick: ["moonlight-peaks/updates", "moonlight-peaks/steam-deck", "moonlight-peaks/console", "moonlight-peaks/system-requirements", "moonlight-peaks/faq"],
};
const MOON_PHASE_BY = {};
MOON_GROUPS.data.forEach((s, i) => MOON_PHASE_BY[s] = 1 + i);
MOON_GROUPS.deep.forEach((s, i) => MOON_PHASE_BY[s] = 1 + i);
MOON_GROUPS.quick.forEach((s, i) => MOON_PHASE_BY[s] = 1 + i);

function moonHeader(lang, active) {
  const t = moonTxt(lang);
  const n = navI18n(lang);
  const item = (slug, label) => {
    const p = DATA.pages.find(x => x.slug === slug);
    if (!p) return "";
    const name = pageOf(p, lang).title.replace(/\s*(Moonlight Peaks|Moonlight|月光小镇)\s*/g, " ").replace(/\s+/g, " ").trim();
    const phase = MOON_PHASE_BY[slug] || 4;
    return `<a class="moon-nav-item ${slug === active ? "active" : ""}" href="${linkOf(slug, lang)}">${moonPhaseIcon(phase, slug === active ? "glow" : "")}<span>${esc(name)}</span></a>`;
  };
  const group = (title, slugs) => `<div class="moon-nav-group"><b>${esc(title)}</b><div class="moon-nav-items">${slugs.map(s => item(s, "")).join("")}</div></div>`;
  const body = `${group(t.data, MOON_GROUPS.data)}${group(t.deep, MOON_GROUPS.deep)}${group(t.quick, MOON_GROUPS.quick)}`;
  const langItems = LANGS.map(l =>
    `<a href="${linkOf(active || "moonlight-peaks", l)}" class="${l === lang ? "active" : ""}"><span class="flag svg-flag">${flagOf(l)}</span><span class="lang-name">${LANG_META[l]?.name || l}</span></a>`
  ).join("");
  return `<header class="moon-head">
  <a class="moon-brand" href="${linkOf("moonlight-peaks", lang)}">
    <span class="brand-moon">${moonPhaseIcon(7)}</span>
    <span class="brand-name">${esc(t.ledger)}<small>${esc(t.home)}</small></span>
  </a>
  <button class="moon-nav-toggle" type="button" aria-label="Toggle menu" aria-controls="moonlight-navigation" aria-expanded="false"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 6h16M4 12h16M4 18h16"/></svg></button>
  <nav id="moonlight-navigation" class="moon-nav" aria-label="Moonlight Peaks index">${body}
    <div class="moon-lang"><span class="lang-label">${esc(t.langLabel)}</span>${langItems}</div>
    <a class="moon-hub-link" href="${linkOf("index", lang)}">${esc(t.hub)}</a>
  </nav>
</header>`;
}

function moonFooter(lang) {
  const t = moonTxt(lang);
  const n = navI18n(lang);
  const quick = MOON_GROUPS.quick.concat(MOON_GROUPS.data.slice(0, 3));
  const links = quick.map(s => { const p = DATA.pages.find(x => x.slug === s); return p ? `<a href="${linkOf(s, lang)}">${esc(pageOf(p, lang).title)}</a>` : ""; }).join("") + `<a href="${linkOf("sandustry", lang)}">${lang === "zh-CN" ? "⛏️ 沙金工业" : lang === "ko" ? "⛏️ 샌더스트리" : "⛏️ Sandustry"}</a>`;
  return `<footer class="moon-colophon">
  <div>
    <h3>${esc(t.ledger)}</h3>
    <p>${esc(t.footerNote)}</p>
    <p>${esc(t.footerSource)} · ${esc(t.updated)} ${TODAY}</p>
  </div>
  <div>
    <div class="moon-colophon-links">
      <a href="${linkOf("about", lang)}">${esc(n.about)}</a>
      <a href="${linkOf("privacy", lang)}">${esc(n.privacy)}</a>
      <a href="${linkOf("contact", lang)}">${esc(n.contact)}</a>
      <a href="${esc(DATA.game.steamUrl.replace("4113940", "2209900"))}" target="_blank" rel="noopener">Steam ↗</a>
      ${links}
    </div>
    <p class="colophon-legal">© ${COPYRIGHT_YEAR} ${esc(DATA.site.domain)} · ${lang === "zh-CN" ? "非官方粉丝站" : "Unofficial fan site"}</p>
  </div>
</footer>
${KIT.decisionEventsScript()}
${consentUi(lang)}`;
}

/* 月光页 Section 渲染 */
function renderMoonSection(s, lang, slug) {
  const escTxt = esc(s.heading || "");
  const secId = s._tocId ? ` id="${s._tocId}"` : "";
  const tag = s.tag ? `<span class="tag">${esc(s.tag)}</span>` : "";
  switch (s.type) {
    case "table": {
      const th = (s.headers || []).map(h => `<th scope="col">${esc(h)}</th>`).join("");
      // rowAttrs 由 data/moon_row_attrs.py 从「各自那一列」机械推导（不新增事实），
      // 渲染成 data-* 供筛选器用；无 JS 时这些属性对读者与爬虫完全无影响。
      const attrs = s.rowAttrs || [];
      const tr = (s.rows || []).map((r, i) => {
        const a = attrs[i] || {};
        const da = Object.keys(a).filter(k => a[k]).map(k => ` data-${k}="${esc(a[k])}"`).join("");
        return `<tr${da}>${r.map(c => `<td>${esc(c)}</td>`).join("")}</tr>`;
      }).join("");
      const tracker = slug === "moonlight-peaks/achievements" ? ' data-tracker="ach"' : "";
      const kind = s.filterKind ? ` data-filter="${esc(s.filterKind)}"` : "";
      return `<section class="moon-section"${secId}><div class="section-head">${tag}<h2>${escTxt}</h2></div><div class="moon-table-wrap"${tracker}${kind}><table class="moon-table"><thead><tr>${th}</tr></thead><tbody>${tr}</tbody></table></div></section>`;
    }
    case "steps": {
      const items = (s.items || []).map((it, i) =>
        `<li class="moon-entry reveal"><span class="moon-entry-no">${moonPhaseIcon(Math.min(7, i + 1))}</span><div class="moon-entry-body"><h3>${esc(it[0])}</h3><p>${esc(it[1])}</p></div></li>`).join("");
      return `<section class="moon-section"${secId}><div class="section-head">${tag}<h2>${escTxt}</h2></div><ol class="moon-entries">${items}</ol></section>`;
    }
    case "list": {
      const items = (s.items || []).map(it =>
        (it && typeof it === "object" && it.href)
          ? `<li><a href="${esc(it.href)}">${esc(it.text)}</a></li>`
          : `<li>${esc(it)}</li>`).join("");
      return `<section class="moon-section"${secId}><div class="section-head">${tag}<h2>${escTxt}</h2></div><ul class="moon-notes">${items}</ul></section>`;
    }
    case "cards": {
      const items = (s.items || []).map(c => {
        const href = c.slug ? linkOf(c.slug, lang) : linkOf("moonlight-peaks/romance", lang);
        return `<a class="char-card" href="${href}"><span class="char-card-name">${esc(c.name)}</span><span class="char-card-sub">${esc(c.sub || "")}</span></a>`;
      }).join("");
      return `<section class="moon-section"${secId}><div class="section-head">${tag}<h2>${escTxt}</h2></div><div class="moon-cards">${items}</div></section>`;
    }
    case "faq": {
      const items = (s.items || []).map((qa, i) =>
        `<details class="moon-faq" ${i === 0 ? "open" : ""}><summary>${esc(qa[0])}</summary><p>${esc(qa[1])}</p></details>`).join("");
      return `<section class="moon-section"${secId}><div class="section-head">${tag}<h2>${escTxt}</h2></div><div class="moon-faq-list">${items}</div></section>`;
    }
    case "note": {
      return `<aside class="moon-abstract reveal">${tag}<p>${esc(s.body || "")}</p></aside>`;
    }
    default:
      return "";
  }
}

function renderMoonPage(p, lang) {
  const t = pageOf(p, lang);
  const page = { ...t, slug: p.slug };
  const ld = [
    KIT.ld.article({ page, lang, urlOf, siteName: siteI18n(lang).name, datePublished: TODAY, dateModified: KIT.LASTMOD_TOKEN }),
    KIT.ld.breadcrumb({ page, lang, urlOf, homeName: moonTxt(lang).home })
  ];
  const secs = t.sections || [];
  const sections = secs.map((s, i) => renderMoonSection({ ...s, _tocId: `sec-${i}` }, lang, p.slug)).join("");
  const isHome = p.slug === "moonlight-peaks";
  const headArt = isHome
    ? `<div class="moon-hero reveal"><h1>${esc(t.title)}</h1><p class="page-intro">${esc(t.intro || "")}</p></div>`
    : `<div class="moon-head reveal"><span class="moon-eyebrow">${esc(moonTxt(lang).ledger)}</span><h1>${esc(t.title)}</h1><p class="page-intro">${esc(t.intro || "")}</p></div>`;
  const body = `<main class="moon-main"><div class="moon-ruled">
    <article class="moon-article">${headArt}${sections}</article>
  </div></main>`;
  return head(t.metaTitle || t.title, t.metaDescription, ld, p.slug, lang) + moonHeader(lang, p.slug) + body + moonFooter(lang) + MOON_JS + "</body></html>";
}

/* 月光交互工具 UI 文案 —— 6 语。
   原则：**通用词翻译，游戏专有名词保留英文**。
   Silverveil Lake / Luna Bay 这类地名没有官方中日韩译名，自己编=违反铁律 3；
   而 Full Moon / Rain / Large fish / 稀有度 这些是通用词，翻译无风险且对 ko/ja 用户价值最大。 */
const MOON_UI = {
  "en":    { search: "Search this table…", searchAria: "Search table", reset: "Reset", showing: "Showing {n} of {t}", none: "No rows match — try clearing a filter.",
             gRarity: "Rarity", gLoc: "Location", gCond: "Condition", gRod: "Rod", gTier: "Gift tier",
             common: "Common", uncommon: "Uncommon", rare: "Rare", superrare: "Super Rare",
             fullmoon: "Full Moon", rain: "Rain", large: "Large fish", evening: "Evening", allseason: "All seasons",
             anyrod: "Any rod", premium: "Premium rod", pending: "Data pending",
             loved: "Loved", liked: "Liked", disliked: "Disliked",
             achDone: "Done {d} / {n}", achHide: "Hide completed", achReset: "Reset progress", achMark: "Mark as done" },
  "zh-CN": { search: "搜索本表…", searchAria: "搜索本表", reset: "重置", showing: "显示 {n} / {t} 条", none: "没有匹配的条目 —— 试试取消一个筛选。",
             gRarity: "稀有度", gLoc: "地点", gCond: "条件", gRod: "鱼竿", gTier: "礼物档",
             common: "普通", uncommon: "少见", rare: "稀有", superrare: "超稀有",
             fullmoon: "满月", rain: "雨天", large: "大型鱼", evening: "傍晚", allseason: "全季节",
             anyrod: "任意竿", premium: "高级竿", pending: "数据待补",
             loved: "最爱", liked: "喜欢", disliked: "讨厌",
             achDone: "已完成 {d} / {n}", achHide: "隐藏已完成", achReset: "重置进度", achMark: "标记完成" },
  "ja":    { search: "この表を検索…", searchAria: "表を検索", reset: "リセット", showing: "{t} 件中 {n} 件", none: "該当なし —— フィルターを外してみてください。",
             gRarity: "レア度", gLoc: "場所", gCond: "条件", gRod: "竿", gTier: "好み",
             common: "コモン", uncommon: "アンコモン", rare: "レア", superrare: "超レア",
             fullmoon: "満月", rain: "雨", large: "大型魚", evening: "夕方", allseason: "全季節",
             anyrod: "どの竿でも", premium: "プレミアム竿", pending: "データ未確認",
             loved: "大好き", liked: "好き", disliked: "嫌い",
             achDone: "達成 {d} / {n}", achHide: "達成済みを隠す", achReset: "進捗をリセット", achMark: "達成済みにする" },
  "ko":    { search: "이 표에서 검색…", searchAria: "표 검색", reset: "초기화", showing: "{t}개 중 {n}개", none: "일치하는 항목이 없습니다 —— 필터를 해제해 보세요.",
             gRarity: "희귀도", gLoc: "장소", gCond: "조건", gRod: "낚싯대", gTier: "선물 반응",
             common: "일반", uncommon: "고급", rare: "희귀", superrare: "초희귀",
             fullmoon: "보름달", rain: "비", large: "대형 어류", evening: "저녁", allseason: "모든 계절",
             anyrod: "아무 낚싯대", premium: "프리미엄 낚싯대", pending: "데이터 미확인",
             loved: "매우 좋아함", liked: "좋아함", disliked: "싫어함",
             achDone: "달성 {d} / {n}", achHide: "달성 항목 숨기기", achReset: "진행도 초기화", achMark: "달성 표시" },
  "fr":    { search: "Rechercher dans ce tableau…", searchAria: "Rechercher", reset: "Réinitialiser", showing: "{n} sur {t}", none: "Aucun résultat — retirez un filtre.",
             gRarity: "Rareté", gLoc: "Lieu", gCond: "Condition", gRod: "Canne", gTier: "Préférence",
             common: "Commun", uncommon: "Peu commun", rare: "Rare", superrare: "Très rare",
             fullmoon: "Pleine lune", rain: "Pluie", large: "Gros poisson", evening: "Soirée", allseason: "Toutes saisons",
             anyrod: "N'importe quelle canne", premium: "Canne premium", pending: "Données à confirmer",
             loved: "Adoré", liked: "Aimé", disliked: "Détesté",
             achDone: "Fait {d} / {n}", achHide: "Masquer les obtenus", achReset: "Réinitialiser", achMark: "Marquer comme fait" },
  "de":    { search: "In dieser Tabelle suchen…", searchAria: "Tabelle durchsuchen", reset: "Zurücksetzen", showing: "{n} von {t}", none: "Keine Treffer — Filter entfernen.",
             gRarity: "Seltenheit", gLoc: "Ort", gCond: "Bedingung", gRod: "Rute", gTier: "Vorliebe",
             common: "Gewöhnlich", uncommon: "Ungewöhnlich", rare: "Selten", superrare: "Sehr selten",
             fullmoon: "Vollmond", rain: "Regen", large: "Großer Fisch", evening: "Abend", allseason: "Alle Jahreszeiten",
             anyrod: "Beliebige Rute", premium: "Premium-Rute", pending: "Daten ausstehend",
             loved: "Geliebt", liked: "Gemocht", disliked: "Ungeliebt",
             achDone: "Erledigt {d} / {n}", achHide: "Erledigte ausblenden", achReset: "Fortschritt zurücksetzen", achMark: "Als erledigt markieren" }
};
/* 地点是游戏专有名词 → 全语言保留英文原名（与表格单元格一致，便于对照） */
const MOON_LOC_LABELS = {
  "silverveil": "Silverveil Lake", "moonlit-pines": "Moonlit Pines River", "luna-bay": "Luna Bay",
  "pink-grove": "Pink Grove", "underground": "Underground / Caves", "howling-marshes": "Howling Marshes",
  "misty-shores": "Misty Shores", "farm": "Farm rivers", "anywhere": "Anywhere"
};

/* 月光交互 JS（渐进增强：HTML 表格一个字不改，筛选器全靠 JS 加） */
const MOON_JS = `<script>
(function(){
  var UI = ${JSON.stringify(MOON_UI)};
  var LOC = ${JSON.stringify(MOON_LOC_LABELS)};
  var t = UI[document.documentElement.lang] || UI.en;
  var fmt = function(s, o){ return s.replace(/\\{(\\w+)\\}/g, function(_, k){ return o[k]; }); };

  function chip(label, group, value){
    var b = document.createElement('button');
    b.type = 'button';
    b.className = 'moon-chip';
    b.textContent = label;
    b.dataset.group = group;
    b.dataset.value = value;
    b.setAttribute('aria-pressed', 'false');
    return b;
  }

  /* 通用筛选引擎：组内 OR，组间 AND；搜索与筛选叠加 */
  function buildFilter(wrap, table, groups, opts){
    opts = opts || {};
    var rows = Array.prototype.slice.call(table.querySelectorAll('tbody tr'));
    if (!rows.length) return;
    var bar = document.createElement('div');
    bar.className = 'moon-filter';

    var searchRow = document.createElement('div');
    searchRow.className = 'moon-filter-search';
    var input = document.createElement('input');
    input.type = 'search';
    input.className = 'moon-search';
    input.placeholder = t.search;
    input.setAttribute('aria-label', t.searchAria);
    var resetBtn = document.createElement('button');
    resetBtn.type = 'button';
    resetBtn.className = 'moon-reset';
    resetBtn.textContent = t.reset;
    searchRow.appendChild(input);
    searchRow.appendChild(resetBtn);
    bar.appendChild(searchRow);

    var active = {};
    groups.forEach(function(g){
      if (!g.values.length) return;
      active[g.key] = [];
      var row = document.createElement('div');
      row.className = 'moon-chip-row';
      if (g.label) {
        var lab = document.createElement('span');
        lab.className = 'moon-chip-label';
        lab.textContent = g.label;
        row.appendChild(lab);
      }
      g.values.forEach(function(v){
        var c = chip(v.label, g.key, v.value);
        c.addEventListener('click', function(){
          var arr = active[g.key];
          var i = arr.indexOf(v.value);
          if (i > -1) { arr.splice(i, 1); c.setAttribute('aria-pressed', 'false'); }
          else { arr.push(v.value); c.setAttribute('aria-pressed', 'true'); }
          apply();
        });
        row.appendChild(c);
      });
      bar.appendChild(row);
    });

    var count = document.createElement('p');
    count.className = 'moon-count';
    count.setAttribute('aria-live', 'polite');
    bar.appendChild(count);

    var empty = document.createElement('p');
    empty.className = 'moon-empty';
    empty.textContent = t.none;
    empty.hidden = true;

    function apply(){
      var q = input.value.trim().toLowerCase();
      var shown = 0;
      rows.forEach(function(tr){
        var ok = true;
        for (var k in active) {
          var sel = active[k];
          if (!sel.length) continue;
          var have = (tr.dataset[k] || '').split(' ');
          if (!sel.some(function(v){ return have.indexOf(v) > -1; })) { ok = false; break; }
        }
        if (ok && q) ok = opts.match ? opts.match(tr, q, active) : tr.textContent.toLowerCase().indexOf(q) > -1;
        tr.hidden = !ok;
        if (ok) shown++;
      });
      count.textContent = fmt(t.showing, { n: shown, t: rows.length });
      empty.hidden = shown !== 0;
    }

    resetBtn.addEventListener('click', function(){
      input.value = '';
      for (var k in active) active[k] = [];
      bar.querySelectorAll('.moon-chip').forEach(function(c){ c.setAttribute('aria-pressed', 'false'); });
      apply();
    });
    input.addEventListener('input', apply);

    wrap.insertBefore(bar, table.parentNode === wrap ? table : wrap.firstChild);
    wrap.appendChild(empty);
    apply();
  }

  /* 从行属性里收集实际出现过的值 —— 不硬编码，数据变了筛选项自动跟着变 */
  function valuesOf(rows, key, labeler){
    var seen = [];
    rows.forEach(function(tr){
      (tr.dataset[key] || '').split(' ').forEach(function(v){
        if (v && seen.indexOf(v) < 0) seen.push(v);
      });
    });
    return seen.filter(function(v){ return v !== 'unlisted'; })
               .map(function(v){ return { value: v, label: labeler(v) }; });
  }

  /* —— 鱼图鉴：稀有度 / 地点 / 条件 / 竿 —— */
  document.querySelectorAll('[data-filter="fish"]').forEach(function(w){
    var table = w.querySelector('table');
    if (!table) return;
    var rows = Array.prototype.slice.call(table.querySelectorAll('tbody tr'));
    var order = ['common', 'uncommon', 'rare', 'superrare'];
    var rarity = valuesOf(rows, 'rarity', function(v){ return t[v] || v; })
      .sort(function(a, b){ return order.indexOf(a.value) - order.indexOf(b.value); });
    var loc = valuesOf(rows, 'loc', function(v){ return LOC[v] || v; });
    var cond = [];
    ['moon', 'weather', 'size', 'time'].forEach(function(k){
      valuesOf(rows, k, function(v){ return t[v] || v; }).forEach(function(v){
        if (['anyweather', 'anytime'].indexOf(v.value) < 0) cond.push({ value: v.value, key: k, label: v.label });
      });
    });
    var rod = valuesOf(rows, 'rod', function(v){ return t[v] || v; });
    buildFilter(w, table, [
      { key: 'rarity', label: t.gRarity, values: rarity },
      { key: 'loc', label: t.gLoc, values: loc },
      { key: 'moon', label: t.gCond, values: cond.filter(function(c){ return c.key === 'moon'; }) },
      { key: 'weather', label: '', values: cond.filter(function(c){ return c.key === 'weather'; }) },
      { key: 'size', label: '', values: cond.filter(function(c){ return c.key === 'size'; }) },
      { key: 'rod', label: t.gRod, values: rod }
    ]);
  });

  /* —— 礼物矩阵：搜一个物品，看谁最爱/喜欢/讨厌它（反查，竞品没有） —— */
  document.querySelectorAll('[data-filter="gift"]').forEach(function(w){
    var table = w.querySelector('table');
    if (!table) return;
    var COLS = { hasloved: 1, hasliked: 2, hasdisliked: 3 };
    buildFilter(w, table, [
      { key: 'has', label: t.gTier, values: [
        { value: 'hasloved', label: t.loved },
        { value: 'hasliked', label: t.liked },
        { value: 'hasdisliked', label: t.disliked }
      ] }
    ], {
      // 选了「讨厌」再搜 Trash → 只列出讨厌 Trash 的角色（把搜索限定在选中的列里）
      match: function(tr, q, active) {
        var sel = (active.has || []).filter(function(k){ return COLS[k]; });
        if (!sel.length) return tr.textContent.toLowerCase().indexOf(q) > -1;
        return sel.some(function(k){
          var cell = tr.cells[COLS[k]];
          return cell && cell.textContent.toLowerCase().indexOf(q) > -1;
        });
      }
    });
  });

  /* —— 其余长表：只给搜索（无结构化属性可筛） —— */
  document.querySelectorAll('.moon-table-wrap:not([data-filter])').forEach(function(w){
    var table = w.querySelector('table');
    if (!table || table.rows.length < 7) return;
    buildFilter(w, table, []);
  });

  /* —— 59 成就追踪器 —— */
  document.querySelectorAll('[data-tracker="ach"]').forEach(function(w){
    var table = w.querySelector('table');
    if (!table) return;
    var key = 'mp-ach-v1';
    var done = {};
    try { done = JSON.parse(localStorage.getItem(key) || '{}'); } catch(e){}
    var rows = Array.prototype.slice.call(table.querySelectorAll('tbody tr'));
    if (!rows.length) return;

    // 复选框必须放进真正的 <td>，否则会被当成匿名单元格塞进行首，整表错列一格
    var headRow = table.querySelector('thead tr');
    if (headRow) {
      var th = document.createElement('th');
      th.className = 'ach-col';
      th.setAttribute('scope', 'col');
      th.innerHTML = '<span class="visually-hidden">' + t.achMark + '</span>';
      headRow.insertBefore(th, headRow.firstChild);
    }

    var panel = document.createElement('div');
    panel.className = 'ach-panel';
    var barWrap = document.createElement('div');
    barWrap.className = 'ach-progress';
    var bar = document.createElement('div');
    bar.className = 'ach-bar';
    barWrap.appendChild(bar);
    var meta = document.createElement('p');
    meta.className = 'ach-meta';
    var ctrls = document.createElement('div');
    ctrls.className = 'ach-ctrls';
    var hideLab = document.createElement('label');
    hideLab.className = 'ach-hide';
    var hideCb = document.createElement('input');
    hideCb.type = 'checkbox';
    hideLab.appendChild(hideCb);
    hideLab.appendChild(document.createTextNode(' ' + t.achHide));
    var resetB = document.createElement('button');
    resetB.type = 'button';
    resetB.className = 'moon-reset';
    resetB.textContent = t.achReset;
    ctrls.appendChild(hideLab);
    ctrls.appendChild(resetB);
    panel.appendChild(barWrap);
    panel.appendChild(meta);
    panel.appendChild(ctrls);

    function refresh(){
      var n = rows.length, d = 0;
      rows.forEach(function(tr){ if (done[tr.dataset.ach]) d++; });
      bar.style.width = (n ? (d / n * 100) : 0) + '%';
      barWrap.setAttribute('role', 'progressbar');
      barWrap.setAttribute('aria-valuenow', String(d));
      barWrap.setAttribute('aria-valuemin', '0');
      barWrap.setAttribute('aria-valuemax', String(n));
      meta.textContent = fmt(t.achDone, { d: d, n: n });
      // 用独立 class 而不是 hidden：搜索框也在用 hidden，两者互不覆盖
      rows.forEach(function(tr){
        tr.classList.toggle('ach-hidden', hideCb.checked && !!done[tr.dataset.ach]);
      });
      try { localStorage.setItem(key, JSON.stringify(done)); } catch(e){}
    }

    rows.forEach(function(tr, i){
      var name = ((tr.cells[0] && tr.cells[0].textContent) || '').trim() || ('row-' + i);
      tr.dataset.ach = name;
      var td = document.createElement('td');
      td.className = 'ach-col';
      var cb = document.createElement('input');
      cb.type = 'checkbox';
      cb.className = 'ach-cb';
      cb.setAttribute('aria-label', t.achMark + ': ' + name);
      cb.checked = !!done[name];
      cb.addEventListener('change', function(){
        done[name] = cb.checked;
        if (!cb.checked) delete done[name];
        refresh();
      });
      td.appendChild(cb);
      tr.insertBefore(td, tr.firstChild);
    });

    hideCb.addEventListener('change', refresh);
    resetB.addEventListener('click', function(){
      done = {};
      table.querySelectorAll('.ach-cb').forEach(function(c){ c.checked = false; });
      hideCb.checked = false;
      refresh();
    });

    w.insertBefore(panel, w.firstChild);
    refresh();
  });
  // 移动端导航
  var tog = document.querySelector('.moon-nav-toggle');
  var nav = document.querySelector('.moon-nav');
  if (tog && nav) {
    function setMoonNavigation(open, returnFocus){nav.classList.toggle('open',open);tog.setAttribute('aria-expanded',open?'true':'false');if(!open&&returnFocus)tog.focus();}
    tog.addEventListener('click', function(){
      setMoonNavigation(!nav.classList.contains('open'), false);
    });
    document.addEventListener('keydown', function(e){if(e.key==='Escape'&&nav.classList.contains('open'))setMoonNavigation(false,true);});
  }
  // reveal 动画
  var obs = new IntersectionObserver(function(es){
    es.forEach(function(en){ if (en.isIntersecting) { en.target.classList.add('in'); obs.unobserve(en.target); } });
  }, {threshold:.08});
  document.querySelectorAll('.moon-entry.reveal').forEach(function(el){ obs.observe(el); });
})();
</script>`;

/* ---------- 构建 ---------- */
function build() {
  if (fs.existsSync(OUT)) fs.rmSync(OUT, { recursive: true, force: true });
  const all = [];
  // 首页
  for (const lang of LANGS) all.push({ html: renderHome(lang), path: lang === DEF ? "index.html" : `${lang}/index.html`, url: urlOf("index", lang) });
  // 内容页（index 已由 renderHome 生成，跳过；moonlight-peaks/* 走月光主题）
  for (const p of DATA.pages) {
    if (p.slug === "index") continue;
    const pageLangs = (p.languages && p.languages.length) ? p.languages : LANGS;
    for (const lang of pageLangs) {
      const isMoon = p.slug.startsWith("moonlight-peaks");
      const html = isMoon ? renderMoonPage(p, lang) : (renderPage(p, lang) + (p.slug.startsWith("sovereign-tower/tools/") ? TOOL_JS : "") + "</div></body></html>");
      const base = lang === DEF ? `${p.slug}` : `${lang}/${p.slug}`;
      all.push({ html, path: `${base}.html`, url: urlOf(p.slug, lang) });
    }
  }
  // 静态页
  for (const slug of ["about", "privacy", "contact"]) {
    for (const lang of LANGS) {
      const html = renderStatic(slug, lang) + "</div></body></html>";
      all.push({ html, path: lang === DEF ? `${slug}.html` : `${lang}/${slug}.html`, url: urlOf(slug, lang) });
    }
  }
  // 写文件
  for (const f of all) {
    const p = path.join(OUT, f.path);
    fs.mkdirSync(path.dirname(p), { recursive: true });
    fs.writeFileSync(p, LM.stamp(f.url, f.html));
  }
  // 复制静态资源
  fs.mkdirSync(path.join(OUT, "css"), { recursive: true });
  fs.copyFileSync(path.join(ROOT, "templates", "style.css"), path.join(OUT, "css", "style.css"));
  fs.copyFileSync(path.join(ROOT, "templates", "style-moon.css"), path.join(OUT, "css", "style-moon.css"));
  for (const f of ["_headers", "llms.txt"]) {
    const src = path.join(ROOT, "templates", f);
    if (fs.existsSync(src)) fs.copyFileSync(src, path.join(OUT, f));
  }
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
    for (const p of DATA.pages) {
      if (p.slug !== "index") {
        const pl = (p.languages && p.languages.length) ? p.languages : LANGS;
        if (pl.includes(lang)) urls.push(urlOf(p.slug, lang));
      }
    }
    for (const slug of ["about", "privacy", "contact"]) urls.push(urlOf(slug, lang));
  }
  const sitemap = `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${urls.map(u => `  <url><loc>${esc(u)}</loc><lastmod>${LM.dateFor(u)}</lastmod></url>`).join("\n")}\n</urlset>\n`;
  fs.writeFileSync(path.join(OUT, "sitemap.xml"), sitemap);
  LM.save();
  // robots.txt
  fs.writeFileSync(path.join(OUT, "robots.txt"), `User-agent: *\nAllow: /\nSitemap: https://${DATA.site.domain}/sitemap.xml\n`);
  KIT.writeIndexNowKey(OUT, DATA.site.indexNowKey);
  KIT.writeAds(OUT, DATA.site.adsenseId);   // 未配 adsenseId 时不产出空 ads.txt（审计会拦空文件）
  // 404
  fs.writeFileSync(path.join(OUT, "404.html"), renderStatic("404", DEF) + "</body></html>");
  console.log(`✓ built ${all.length} files (${LANGS.length} langs, ${DATA.pages.length + 3} pages)`);
}

build();
