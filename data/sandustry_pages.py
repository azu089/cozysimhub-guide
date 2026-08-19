# -*- coding: utf-8 -*-
"""Sandustry 页面模块（cozysimhub 第 3 游戏 · 沙金工房）。
数据源：L0=官方 wiki（browser-bridge 抓取）+ Steam 免 key API（成就/新闻）。
语言：ko（主）+ en（差异化长尾）；zh 条件性延后。所有机制数据带 (version, date) 双戳。
"""
from pathlib import Path
from sandustry_materials import MATERIALS, MATERIALS_VERSION

def T(headers, rows, tag="DATA", heading=""):
    return {"type": "table", "tag": tag, "heading": heading, "body": "", "headers": headers, "rows": rows}

def S(heading, items, tag="STEP"):
    return {"type": "steps", "tag": tag, "heading": heading, "body": "", "items": items}

def N(heading, items, tag="NOTE"):
    return {"type": "list", "tag": tag, "heading": heading, "body": "", "items": items}

def F(items, heading="FAQ"):
    return {"type": "faq", "tag": "FAQ", "heading": heading, "body": "", "items": items}

def M(body, tag="NOTE"):
    return {"type": "note", "tag": tag, "heading": "", "body": body}

# ---------- 材料表 ----------
def _materials_table():
    headers = ["Material", "Density", "Type", "Obtained From", "Processed By", "Byproducts"]
    rows = []
    for m in MATERIALS:
        p = m["props"]
        rows.append([
            m["name"],
            p.get("Density", "TBD"),
            p.get("Matter Type", "TBD"),
            p.get("Obtained From", "TBD"),
            p.get("Processed By", "TBD"),
            p.get("Byproducts", "—"),
        ])
    return T(headers, rows, tag="MATERIALS", heading="All Materials")

def _materials_ko_table():
    headers = ["재료", "밀도", "유형", "획득처", "가공", "부산물"]
    rows = []
    for m in MATERIALS:
        p = m["props"]
        rows.append([
            m["name"],
            p.get("Density", "미확인"),
            p.get("Matter Type", "미확인"),
            p.get("Obtained From", "미확인"),
            p.get("Processed By", "미확인"),
            p.get("Byproducts", "—"),
        ])
    return T(headers, rows, tag="MATERIALS", heading="모든 재료")

def _materials_ja_table():
    headers = ["素材", "密度", "種類", "入手元", "加工方法", "副産物"]
    rows = []
    for m in MATERIALS:
        p = m["props"]
        rows.append([
            m["name"],
            p.get("Density", "未定"),
            p.get("Matter Type", "未定"),
            p.get("Obtained From", "未定"),
            p.get("Processed By", "未定"),
            p.get("Byproducts", "—"),
        ])
    return T(headers, rows, tag="MATERIALS", heading="全素材")

def _materials_fr_table():
    headers = ["Matériau", "Densité", "Type", "Obtenu depuis", "Transformé par", "Sous-produits"]
    rows = []
    for m in MATERIALS:
        p = m["props"]
        rows.append([
            m["name"],
            p.get("Density", "à compléter"),
            p.get("Matter Type", "à compléter"),
            p.get("Obtained From", "à compléter"),
            p.get("Processed By", "à compléter"),
            p.get("Byproducts", "—"),
        ])
    return T(headers, rows, tag="MATERIALS", heading="Tous les matériaux")

def _materials_de_table():
    headers = ["Material", "Dichte", "Typ", "Erhalten aus", "Verarbeitet durch", "Nebenprodukte"]
    rows = []
    for m in MATERIALS:
        p = m["props"]
        rows.append([
            m["name"],
            p.get("Density", "noch offen"),
            p.get("Matter Type", "noch offen"),
            p.get("Obtained From", "noch offen"),
            p.get("Processed By", "noch offen"),
            p.get("Byproducts", "—"),
        ])
    return T(headers, rows, tag="MATERIALS", heading="Alle Materialien")

# ---------- 首页 ----------
HOME_EN = {
    "slug": "sandustry",
    "title": "Sandustry Guide Hub",
    "metaTitle": "Sandustry Guide: Materials, Guides & Patch Log",
    "metaDescription": "Sandustry guide hub: materials, getting-started, Steam Deck & macOS guides, mobile answer, 16 achievements and EA patch log — Korean and English.",
    "intro": "Sandustry is an automation, exploration and base-building strategy game by Lantto Games, published by Hooded Horse. EA since August 13, 2026 on Steam, GOG, Microsoft Store and PC Game Pass; every pixel is a resource.",
    "sections": [
        N("What this hub covers", [
            {"text": "Getting started (Korean + English)", "href": "/sandustry/getting-started"},
            {"text": f"All {len(MATERIALS)} materials with density, type, source, processing and physics", "href": "/sandustry/materials"},
            {"text": "Mechanics: research, tools, energy and machines", "href": "/sandustry/mechanics"},
            {"text": "Steam Deck guide", "href": "/sandustry/steam-deck"},
            {"text": "macOS guide", "href": "/sandustry/macos"},
            {"text": "Mobile answer: no official mobile version", "href": "/sandustry/mobile"},
            {"text": "All 16 achievements with unlock rates", "href": "/sandustry/achievements"},
            {"text": "FAQ", "href": "/sandustry/faq"},
            {"text": "EA patch log & roadmap, API-driven", "href": "/sandustry/updates"},
        ]),
        M(f"Data version: {MATERIALS_VERSION['version']} (captured {MATERIALS_VERSION['captured']}). Sources: official wiki (L0) + Steam API (L0)."),
    ],
}

HOME_KO = {
    "slug": "sandustry",
    "title": "샌더스트리 가이드 허브",
    "metaTitle": "샌더스트리 가이드: 재료·시작·업적·패치",
    "metaDescription": "샌더스트리 가이드: 전체 재료, 시작 가이드, Steam Deck·macOS, 모바일 답변, 업적, EA 패치 로그.",
    "intro": "샌더스트리는 Lantto Games가 개발하고 Hooded Horse가 퍼블리싱한 자동화·탐험·기지 건설 전략 게임입니다. 2026년 8월 13일 Steam, GOG, Microsoft Store, PC Game Pass에서 얼리 액세스로 출시되었습니다.",
    "sections": [
        N("이 허브에서 다루는 내용", [
            {"text": "시작 가이드 (한국어 + 영어)", "href": "/ko/sandustry/getting-started"},
            {"text": f"전체 {len(MATERIALS)}개 재료의 밀도·유형·획득처·가공·물리 속성", "href": "/ko/sandustry/materials"},
            {"text": "메커닉스: 연구, 도구, 에너지", "href": "/ko/sandustry/mechanics"},
            {"text": "Steam Deck 가이드", "href": "/ko/sandustry/steam-deck"},
            {"text": "macOS 가이드", "href": "/ko/sandustry/macos"},
            {"text": "모바일 답변: 공식 모바일 버전 없음", "href": "/ko/sandustry/mobile"},
            {"text": "16개 업적과 달성률", "href": "/ko/sandustry/achievements"},
            {"text": "FAQ", "href": "/ko/sandustry/faq"},
            {"text": "EA 패치 로그 및 로드맵 (API 기반)", "href": "/ko/sandustry/updates"},
        ]),
        M(f"데이터 버전: {MATERIALS_VERSION['version']} ({MATERIALS_VERSION['captured']} 수집). 출처: 공식 위키 (L0) + Steam API (L0)."),
    ],
}

# ---------- Getting Started ----------
GETTING_STARTED_EN = {
    "slug": "sandustry/getting-started",
    "title": "Sandustry Getting Started",
    "metaTitle": "Sandustry Getting Started: First Factory & Materials",
    "metaDescription": "Sandustry getting-started guide: first factory, understanding materials, research and progression.",
    "intro": "This guide gets you from your first shovel to your first automated factory in Sandustry.",
    "sections": [
        S("First steps", [
            "Start by mining Dirt with your Shovel — Dirt is the primary source of Sand.",
            "Collect Sand and let Water turn it into Wet Sand; process toward Gold.",
            "Build a Collector to bank resources — Gold must be stored in Collector blocks to count toward your bank.",
            "Unlock Research with Gold and Fluxite — these are the two major progression materials.",
        ]),
        N("Progression loop", [
            "Mine → process (Water/Fire) → collect → research → build machines → automate.",
            "Gold and Fluxite drive research; see the materials table for every source and byproduct.",
        ]),
        M("Source: official wiki (L0). Version v0.5.4."),
    ],
}

GETTING_STARTED_KO = {
    "slug": "sandustry/getting-started",
    "title": "샌더스트리 시작 가이드",
    "metaTitle": "샌더스트리 시작 가이드",
    "metaDescription": "샌더스트리 시작 가이드: 첫 공장 건설, 재료 이해, 연구와 진행.",
    "intro": "이 가이드는 샌더스트리에서 첫 삽부터 첫 자동화 공장까지 안내합니다.",
    "sections": [
        S("첫 단계", [
            "삽(Shovel)으로 흙(Dirt)을 캐세요 — 흙은 모래(Sand)의 주요 공급원입니다.",
            "모래를 모으고 물(Water)로 젖은 모래(Wet Sand)로 만든 뒤 금(Gold)으로 가공하세요.",
            "수집기(Collector)를 지어 자원을 저장하세요 — 금은 수집기에 보관해야 은행에 집계됩니다.",
            "금과 플럭사이트(Fluxite)로 연구(Research)를 해금하세요 — 이 두 재료가 주요 진행 자원입니다.",
        ]),
        N("진행 루프", [
            "채굴 → 가공(물/불) → 수집 → 연구 → 기계 건설 → 자동화",
            "금과 플럭사이트가 연구를 이끕니다. 모든 재료의 획득처와 부산물은 재료 표를 참고하세요.",
        ]),
        M("출처: 공식 위키 (L0). 버전 v0.5.4."),
    ],
}

# ---------- Materials ----------
MATERIALS_EN = {
    "slug": "sandustry/materials",
    "title": "All Sandustry Materials",
    "metaTitle": "All Sandustry Materials: Density & Sources",
    "metaDescription": "Every Sandustry material with density, matter type, source, processing and physics.",
    "intro": f"All {len(MATERIALS)} materials in Sandustry, with density, type, source, processing and physics from the official wiki.",
    "sections": [_materials_table(), M("Version: v0.5.4.")],
}

MATERIALS_KO = {
    "slug": "sandustry/materials",
    "title": "샌더스트리 전체 재료",
    "metaTitle": "샌더스트리 전체 재료",
    "metaDescription": "샌더스트리의 모든 재료: 밀도, 유형, 획득처, 가공, 물리 속성.",
    "intro": f"샌더스트리의 모든 재료 {len(MATERIALS)}종의 밀도, 유형, 획득처, 가공, 물리 속성 (공식 위키 출처).",
    "sections": [_materials_ko_table(), M("버전: v0.5.4.")],
}

# ---------- 差异化长尾 (en) ----------
STEAM_DECK_EN = {
    "slug": "sandustry/steam-deck",
    "title": "Sandustry on Steam Deck",
    "metaTitle": "Sandustry on Steam Deck: Settings & Performance",
    "metaDescription": "Run Sandustry on Steam Deck: performance, settings and control tips.",
    "intro": "Sandustry has native Linux support and is reported playable on Steam Deck. Here is how to get the best experience.",
    "sections": [
        N("Setup", [
            "Native Linux build — no Proton required.",
            "Playable per community reports (boilingsteam); official Valve compatibility rating not yet published.",
            "Use Steam Input to map controls — the game has no full controller support category.",
        ]),
        M("Source: L1 community reports + L0 platform facts. Version v0.5.4."),
    ],
}

MACOS_EN = {
    "slug": "sandustry/macos",
    "title": "Sandustry on macOS",
    "metaTitle": "Sandustry on macOS: Native Support & Bug",
    "metaDescription": "Sandustry native macOS support, the right-click bug and workarounds.",
    "intro": "Sandustry has a native macOS version. A right-click interaction bug has been reported by players — here is the workaround.",
    "sections": [
        N("Native support", [
            "Official macOS build — no translation layer.",
            "Known issue: right-click interactions can fail in some contexts (community reports).",
            "Workaround: rebind or use an alternative input until patched.",
        ]),
        M("Source: L1 community threads + L0 platform facts. Version v0.5.4."),
    ],
}

MOBILE_EN = {
    "slug": "sandustry/mobile",
    "title": "Is Sandustry on Mobile?",
    "metaTitle": "Is Sandustry on Mobile? No (Fake APK Warning)",
    "metaDescription": "Sandustry has no official mobile version. Fake APK download sites are scams.",
    "intro": "No — Sandustry has no official mobile version. Fake APK download pages are circulating; do not download from them.",
    "sections": [
        N("Official platforms", [
            "Steam, GOG, Microsoft Store and PC Game Pass.",
            "No Android/iOS version announced.",
            "Fake 'Sandustry APK' pages are scams — official sources only.",
        ]),
        M("Source: L0 official platforms + L1 fake-page observation."),
    ],
}

ACHIEVEMENTS_EN = {
    "slug": "sandustry/achievements",
    "title": "All Sandustry Achievements (16)",
    "metaTitle": "All 16 Sandustry Achievements (Rates)",
    "metaDescription": "All 16 Sandustry achievements and their global unlock rates.",
    "intro": "All 16 Sandustry achievements with global unlock rates from the official Steam API.",
    "sections": [
        T(["Achievement", "Unlock Rate"], [
            ["PROMOTION_PROTOCOL", "93.5%"],
            ["FLUX_IT_UP", "89.3%"],
            ["GOLD_IN_THE_BIN", "87.8%"],
            ["ANCIENT_TECHNOLOGY", "80.8%"],
            ["FIRST_BLOOM", "73.9%"],
            ["VOID_TOUCHED", "57.5%"],
            ["CRITTER_CATCHER", "50.9%"],
            ["FIRST_SPARK", "49.9%"],
            ["QUARTERMASTER", "42.3%"],
            ["STRATACORE_SECURED", "28.2%"],
            ["CONSERVATORY_CURATOR", "26.8%"],
            ["AURA_EXTRACTOR", "23.7%"],
            ["FULL_CIRCLE", "19.6%"],
            ["FINAL_SCHEMATIC", "16.4%"],
            ["VAULTKEEPER", "10.8%"],
            ["HELIODYNE_TYCOON", "0.4%"],
        ]),
        M("Source: Steam achievements API (L0). Captured 2026-08-17."),
    ],
}

# ---------- FAQ (ko) ----------
FAQ_EN = {
    "slug": "sandustry/faq",
    "title": "Sandustry FAQ",
    "metaTitle": "Sandustry FAQ: Korean, Mobile, Multiplayer",
    "metaDescription": "Sandustry frequently asked questions: Korean support, mobile version, multiplayer.",
    "intro": "Frequently asked questions about Sandustry.",
    "sections": [
        F([
            ["Does Sandustry support Korean?", "Yes. Korean (interface + subtitles) is officially supported."],
            ["Is there a mobile version?", "No. Beware fake APK download sites. Official platforms: Steam, GOG, Microsoft Store, PC Game Pass."],
            ["Is there multiplayer?", "No. It is a single-player game."],
            ["How do I get Gold?", "Gold is a byproduct of most processing. It must be stored in Collector blocks to count toward your bank."],
        ]),
    ],
}

FAQ_KO = {
    "slug": "sandustry/faq",
    "title": "샌더스트리 FAQ",
    "metaTitle": "샌더스트리 FAQ",
    "metaDescription": "샌더스트리 자주 묻는 질문: 한국어 지원, 모바일 버전, 멀티플레이어.",
    "intro": "샌더스트리에 대한 자주 묻는 질문입니다.",
    "sections": [
        F([
            ["샌더스트리는 한국어를 지원하나요?", "네. 한국어(인터페이스+자막)를 공식 지원합니다."],
            ["모바일 버전이 있나요?", "없습니다. 가짜 APK 다운로드 사이트에 주의하세요. 공식 플랫폼은 Steam, GOG, Microsoft Store, PC Game Pass입니다."],
            ["멀티플레이어가 있나요?", "없습니다. 싱글 플레이어 게임입니다."],
            ["금(Gold)은 어떻게 얻나요?", "대부분의 가공 과정의 부산물로 얻습니다. 수집기(Collector)에 보관해야 은행에 집계됩니다."],
        ]),
    ],
}

# ---------- 注册表 ----------
def build_sandustry_pages():
    return {
        "sandustry": {"en": HOME_EN, "ko": HOME_KO},
        "sandustry/getting-started": {"en": GETTING_STARTED_EN, "ko": GETTING_STARTED_KO},
        "sandustry/materials": {"en": MATERIALS_EN, "ko": MATERIALS_KO},
        "sandustry/steam-deck": {"en": STEAM_DECK_EN},
        "sandustry/macos": {"en": MACOS_EN},
        "sandustry/mobile": {"en": MOBILE_EN},
        "sandustry/achievements": {"en": ACHIEVEMENTS_EN},
        "sandustry/faq": {"en": None, "ko": FAQ_KO},
    }

# ---------- i18n 组装（对齐 moonlight _i18n 模式）----------
def _lang_page(lang_data, en_sections):
    # ko 为完整翻译：sections 是完整列表，整体替换（不逐 section 覆盖）
    return {
        "title": lang_data["title"],
        "metaTitle": lang_data.get("metaTitle", ""),
        "metaDescription": lang_data.get("metaDescription", ""),
        "intro": lang_data.get("intro", ""),
        "sections": lang_data.get("sections", en_sections),
    }

def _to_page(en, i18n_map):
    """en=EN 页面 dict（含 slug/title/intro/sections）；i18n_map={lang: {title, intro, sections}}。
    返回 site.json pages 条目（含 i18n 字段 + languages 白名单）。"""
    page_i18n = {}
    for lg, ld in (i18n_map or {}).items():
        if ld is None:
            continue
        page_i18n[lg] = _lang_page(ld, en["sections"])
    p = {
        "slug": en["slug"],
        "title": en["title"],
        "metaTitle": en.get("metaTitle", ""),
        "metaDescription": en.get("metaDescription", ""),
        "intro": en.get("intro", ""),
        "sections": en["sections"],
        # 语言白名单：en(默认) + zh-CN + ja + ko + fr + de（六语言全量，对齐站点全局语言）
        "languages": ["en", "zh-CN", "ja", "ko", "fr", "de"],
    }
    if page_i18n:
        p["i18n"] = page_i18n
    return p

def build_sandustry_pages():
    """返回 Sandustry 页面列表，供 build_content.py 追加到 d['pages']。"""
    reg = {
        "sandustry": (HOME_EN, {"ko": HOME_KO, "zh-CN": HOME_ZH, "ja": HOME_JA, "fr": HOME_FR, "de": HOME_DE}),
        "sandustry/getting-started": (GETTING_STARTED_EN, {"ko": GETTING_STARTED_KO, "zh-CN": GETTING_STARTED_ZH, "ja": GETTING_STARTED_JA, "fr": GETTING_STARTED_FR, "de": GETTING_STARTED_DE}),
        "sandustry/materials": (MATERIALS_EN, {"ko": MATERIALS_KO, "zh-CN": MATERIALS_ZH, "ja": MATERIALS_JA, "fr": MATERIALS_FR, "de": MATERIALS_DE}),
        "sandustry/steam-deck": (STEAM_DECK_EN, {"ko": STEAM_DECK_KO, "zh-CN": STEAM_DECK_ZH, "ja": STEAM_DECK_JA, "fr": STEAM_DECK_FR, "de": STEAM_DECK_DE}),
        "sandustry/macos": (MACOS_EN, {"ko": MACOS_KO, "zh-CN": MACOS_ZH, "ja": MACOS_JA, "fr": MACOS_FR, "de": MACOS_DE}),
        "sandustry/mobile": (MOBILE_EN, {"ko": MOBILE_KO, "zh-CN": MOBILE_ZH, "ja": MOBILE_JA, "fr": MOBILE_FR, "de": MOBILE_DE}),
        "sandustry/achievements": (ACHIEVEMENTS_EN, {"ko": ACHIEVEMENTS_KO, "zh-CN": ACHIEVEMENTS_ZH, "ja": ACHIEVEMENTS_JA, "fr": ACHIEVEMENTS_FR, "de": ACHIEVEMENTS_DE}),
        "sandustry/faq": (FAQ_EN, {"ko": FAQ_KO, "zh-CN": FAQ_ZH, "ja": FAQ_JA, "fr": FAQ_FR, "de": FAQ_DE}),
        "sandustry/updates": (UPDATES_EN, {"ko": UPDATES_KO, "zh-CN": UPDATES_ZH, "ja": UPDATES_JA, "fr": UPDATES_FR, "de": UPDATES_DE}),
        "sandustry/mechanics": (MECHANICS_EN, {"ko": MECHANICS_KO, "zh-CN": MECHANICS_ZH, "ja": MECHANICS_JA, "fr": MECHANICS_FR, "de": MECHANICS_DE}),
    }
    pages = []
    for slug, (en, i18n) in reg.items():
        if en is None and not i18n:
            continue
        if en is None:
            # FAQ ko-only：用 ko 结构（en 由 FAQ_EN 提供，已在上方处理）
            continue
        pages.append(_to_page(en, i18n))
    return pages

# ---------- Updates (patch log, API-driven) ----------
UPDATES_ROWS = [
    ["v0.5.4 (Update #1)", "2026-08-16", "Better filter editing, Tier 5 softlock fixes, red-block temporary removal, zoom keybinds"],
    ["v0.5.3 (Hotfix)", "2026-08-14", "Better logging, memory optimizations, clearer objectives"],
    ["EA Launch", "2026-08-13", "Sandustry enters Early Access on Steam, GOG, Microsoft Store and PC Game Pass"],
]
UPDATES_EN = {
    "slug": "sandustry/updates",
    "title": "Sandustry Updates & Patch Notes",
    "metaTitle": "Sandustry Patch Notes: v0.5.4 & v0.5.3",
    "metaDescription": "The latest Sandustry patch notes: v0.5.4 (filter editing, Tier 5 fixes), v0.5.3 hotfix and the EA launch — updated as new patches drop.",
    "intro": "Lantto Games ships frequent Early Access patches. This page tracks the latest patch notes from the official Steam news; it is updated whenever a new update ships.",
    "sections": [
        T(["Version", "Date", "Highlights"], UPDATES_ROWS, heading="Patch history"),
        N("How to update", [
            "Steam: updates install automatically when you launch the game.",
            "GOG / Microsoft Store / PC Game Pass: console- and store-side patches may follow the Steam release.",
        ]),
        M("Source: official Steam news (ISteamNews API, L0). Data version v0.5.4 (2026-08-17)."),
    ],
}
UPDATES_KO = {
    "slug": "sandustry/updates",
    "title": "샌더스트리 업데이트 및 패치 노트",
    "metaTitle": "샌더스트리 패치 노트",
    "metaDescription": "샌더스트리 최신 패치 노트: v0.5.4(필터 편집, Tier 5 수정), v0.5.3 핫픽스, EA 출시 — 새 패치마다 업데이트됩니다.",
    "intro": "Lantto Games는 잦은 얼리 액세스 패치를 제공합니다. 이 페이지는 공식 Steam 뉴스의 최신 패치 노트를 정리하며, 새 업데이트가 나올 때마다 갱신됩니다.",
    "sections": [
        T(["버전", "날짜", "주요 내용"], UPDATES_ROWS, heading="패치 기록"),
        N("업데이트 방법", [
            "Steam: 게임 실행 시 업데이트가 자동으로 설치됩니다.",
            "GOG / Microsoft Store / PC Game Pass: 스토어 패치는 Steam 릴리스를 따를 수 있습니다.",
        ]),
        M("출처: 공식 Steam 뉴스 (ISteamNews API, L0). 데이터 버전 v0.5.4 (2026-08-17)."),
    ],
}

# ---------- Mechanics (research/tools/energy) ----------
MECHANICS_EN = {
    "slug": "sandustry/mechanics",
    "title": "Sandustry Mechanics: Research, Tools, Energy",
    "metaTitle": "Sandustry Mechanics: Research & Tools",
    "metaDescription": "Sandustry core mechanics: research progression, tool tiers, energy and machines.",
    "intro": "The core loops of Sandustry: research with Gold and Fluxite, tool upgrades, and energy-driven machines.",
    "sections": [
        N("Research", [
            "Gold and Fluxite are the two major progression materials — Gold is used to Research new technologies.",
            "Gold is counted toward your bank only when stored in Collector blocks.",
        ]),
        N("Tools", [
            "Tools include Shovel, Gun, Rocket Launcher, Drill, Laser, Void Gun, Grabber, Flamethrower, Cryoblaster, Corraller, Vacuum, Grappling Hook, Demolisher, Marquee and Pipe Remover.",
            "Higher-tier tools unlock faster mining and processing.",
        ]),
        N("Machines & Energy", [
            "Machines: Conveyor Belt (and Mk.2), Launcher, Filter, Shaker, Kinetic Press, Planter Box, Collector, Pipe, Pump, Liquid Vent, Flux Emanator, Steam Dryer, Sweeper Drone.",
            "Energy powers machines; manage production chains to automate progressively.",
        ]),
        M("Source: official wiki (L0). Data version v0.5.4 (2026-08-17)."),
    ],
}
MECHANICS_KO = {
    "slug": "sandustry/mechanics",
    "title": "샌더스트리 메커닉스: 연구, 도구, 에너지",
    "metaTitle": "샌더스트리 메커닉스",
    "metaDescription": "샌더스트리 핵심 메커닉스: 금·플럭사이트 연구, 도구 단계, 에너지 기계.",
    "intro": "샌더스트리의 핵심 루프: 금과 플럭사이트로 연구, 도구 업그레이드, 에너지 기계.",
    "sections": [
        N("연구", [
            "금(Gold)과 플럭사이트(Fluxite)가 주요 진행 자원입니다 — 금은 새 기술 연구에 사용됩니다.",
            "금은 수집기(Collector)에 보관해야 은행에 집계됩니다.",
        ]),
        N("도구", [
            "도구: 삽(Shovel), 총(Gun), 로켓 발사기, 드릴, 레이저, 보이드 건, 그래버, 화염방사기, 극저온 블래스터, 코랄러, 진공, 그래플링 훅, 철거기, 마키, 파이프 리무버.",
            "상위 단계 도구는 더 빠른 채굴과 가공을 제공합니다.",
        ]),
        N("기계와 에너지", [
            "기계: 컨베이어 벨트(Mk.2), 런처, 필터, 셰이커, 키네틱 프레스, 플랜터 박스, 수집기, 파이프, 펌프, 액체 벤트, 플럭스 이머네이터, 스팀 드라이어, 스위퍼 드론.",
            "에너지가 기계를 구동합니다. 생산 체인을 관리해 점진적으로 자동화하세요.",
        ]),
        M("출처: 공식 위키 (L0). 데이터 버전 v0.5.4 (2026-08-17)."),
    ],
}

# ---------- en-only 页的 ko i18n（P1-3：ko 主语言不得英文回退）----------
STEAM_DECK_KO = {
    "slug": "sandustry/steam-deck",
    "title": "Steam Deck에서 샌더스트리 플레이하기",
    "metaTitle": "샌더스트리 Steam Deck",
    "metaDescription": "Steam Deck에서 샌더스트리 실행: 성능, 설정, 컨트롤 팁.",
    "intro": "샌더스트리는 네이티브 리눅스 빌드를 지원하며 Steam Deck에서 플레이 가능한 것으로 알려져 있습니다.",
    "sections": [
        N("설정", [
            "네이티브 리눅스 빌드 — Proton 불필요.",
            "커뮤니티 보고에 따르면 플레이 가능(boilingsteam); 공식 Valve 호환 등급은 아직 미발표.",
            "Steam Input으로 컨트롤 매핑 — 이 게임은 전체 컨트롤러 지원 카테고리가 없습니다.",
        ]),
        M("출처: L1 커뮤니티 보고 + L0 플랫폼 사실. 버전 v0.5.4."),
    ],
}
MACOS_KO = {
    "slug": "sandustry/macos",
    "title": "macOS에서 샌더스트리 플레이하기",
    "metaTitle": "샌더스트리 macOS 가이드",
    "metaDescription": "샌더스트리 네이티브 macOS 지원, 우클릭 버그와 해결 방법.",
    "intro": "샌더스트리는 네이티브 macOS 버전이 있습니다. 플레이어들이 보고한 우클릭 상호작용 버그의 해결 방법을 안내합니다.",
    "sections": [
        N("네이티브 지원", [
            "공식 macOS 빌드 — 변환 레이어 불필요.",
            "알려진 문제: 일부 상황에서 우클릭 상호작용이 실패할 수 있음(커뮤니티 보고).",
            "해결: 패치될 때까지 리바인드 또는 대체 입력 사용.",
        ]),
        M("출처: L1 커뮤니티 스레드 + L0 플랫폼 사실. 버전 v0.5.4."),
    ],
}
MOBILE_KO = {
    "slug": "sandustry/mobile",
    "title": "샌더스트리 모바일 버전이 있나요?",
    "metaTitle": "샌더스트리 모바일 답변",
    "metaDescription": "샌더스트리에는 공식 모바일 버전이 없습니다. 가짜 APK 다운로드 사이트는 사기입니다.",
    "intro": "아니요 — 샌더스트리에는 공식 모바일 버전이 없습니다. 가짜 APK 다운로드 페이지가 유포되고 있으니 다운로드하지 마세요.",
    "sections": [
        N("공식 플랫폼", [
            "Steam, GOG, Microsoft Store, PC Game Pass.",
            "Android/iOS 버전은 발표되지 않았습니다.",
            "'Sandustry APK' 페이지는 사기입니다 — 공식 출처만 이용하세요.",
        ]),
        M("출처: L0 공식 플랫폼 + L1 가짜 페이지 관찰."),
    ],
}
ACHIEVEMENTS_KO = {
    "slug": "sandustry/achievements",
    "title": "샌더스트리 전체 업적 (16개)",
    "metaTitle": "샌더스트리 16개 업적",
    "metaDescription": "샌더스트리 16개 업적과 글로벌 달성률.",
    "intro": "샌더스트리 16개 업적과 글로벌 달성률 (공식 Steam API 출처).",
    "sections": [
        T(["업적", "달성률"], [
            ["PROMOTION_PROTOCOL", "93.5%"], ["FLUX_IT_UP", "89.3%"], ["GOLD_IN_THE_BIN", "87.8%"],
            ["ANCIENT_TECHNOLOGY", "80.8%"], ["FIRST_BLOOM", "73.9%"], ["VOID_TOUCHED", "57.5%"],
            ["CRITTER_CATCHER", "50.9%"], ["FIRST_SPARK", "49.9%"], ["QUARTERMASTER", "42.3%"],
            ["STRATACORE_SECURED", "28.2%"], ["CONSERVATORY_CURATOR", "26.8%"], ["AURA_EXTRACTOR", "23.7%"],
            ["FULL_CIRCLE", "19.6%"], ["FINAL_SCHEMATIC", "16.4%"], ["VAULTKEEPER", "10.8%"],
            ["HELIODYNE_TYCOON", "0.4%"],
        ]),
        M("출처: Steam 업적 API (L0). 2026-08-17 수집."),
    ],
}

# ---------- zh-CN 完整 i18n（G2 条件性第二语言；表格正确 schema + 链接 cover + FAQ 数组）----------
HOME_ZH = {
    "slug": "sandustry",
    "title": "沙金工业攻略中心",
    "metaTitle": "沙金工业攻略：材料·入门·成就·补丁",
    "metaDescription": "沙金工业攻略中心：全部材料属性、入门指南、Steam Deck 与 macOS 指南、手机版答案、16 个成就与 EA 补丁日志 — 中文版。",
    "intro": "《沙金工业》是 Lantto Games 开发、Hooded Horse 发行的自动化·探索·基地建设策略游戏。2026年8月13日在 Steam、GOG、Microsoft Store 与 PC Game Pass 开启抢先体验。",
    "sections": [
        N("本中心涵盖内容", [
            {"text": "入门指南（中文 + 韩语 + 英语）", "href": "/zh-CN/sandustry/getting-started"},
            {"text": f"全部 {len(MATERIALS)} 种材料的密度、类型、获取、加工与物理属性", "href": "/zh-CN/sandustry/materials"},
            {"text": "机制：研究、工具、能量与机器", "href": "/zh-CN/sandustry/mechanics"},
            {"text": "Steam Deck 指南", "href": "/zh-CN/sandustry/steam-deck"},
            {"text": "macOS 指南", "href": "/zh-CN/sandustry/macos"},
            {"text": "手机版答案：没有官方手机版", "href": "/zh-CN/sandustry/mobile"},
            {"text": "16 个成就与解锁率", "href": "/zh-CN/sandustry/achievements"},
            {"text": "常见问题", "href": "/zh-CN/sandustry/faq"},
            {"text": "EA 补丁日志与路线图", "href": "/zh-CN/sandustry/updates"},
        ]),
        M(f"数据版本：{MATERIALS_VERSION['version']}（{MATERIALS_VERSION['captured']} 采集）。来源：官方维基（L0）+ Steam API（L0）。"),
    ],
}
GETTING_STARTED_ZH = {
    "slug": "sandustry/getting-started",
    "title": "沙金工业入门指南",
    "metaTitle": "沙金工业入门指南",
    "metaDescription": "沙金工业入门指南：从第一把铲子到第一座自动化工厂。",
    "intro": "本指南带您从沙金工业的第一把铲子走到第一座自动化工厂。",
    "sections": [
        S("第一步", [
            "先用铲子（Shovel）挖土（Dirt）——土是沙子（Sand）的主要来源。",
            "收集沙子，用火或水加工成湿沙（Wet Sand），再向金（Gold）转化。",
            "建造收集器（Collector）储存资源——金必须存入收集器才会计入银行。",
            "用金与萤石（Fluxite）解锁研究（Research）——这两种是主要推进材料。",
        ]),
        N("发展循环", [
            "挖矿 → 加工（水/火）→ 收集 → 研究 → 建造机器 → 自动化",
            "金与萤石推动研究；全部材料的获取与副产品见材料表。",
        ]),
        M("来源：官方维基（L0）。版本 v0.5.4。"),
    ],
}
MATERIALS_ZH = {
    "slug": "sandustry/materials",
    "title": "沙金工业全部材料",
    "metaTitle": "沙金工业全部材料",
    "metaDescription": "沙金工业每种材料的密度、类型、获取、加工与物理属性。",
    "intro": f"沙金工业全部 {len(MATERIALS)} 种材料：密度、类型、获取、加工与物理属性（官方维基来源）。",
    "sections": [
        T(["材料", "密度", "类型", "获取", "加工", "副产品"], [[m["name"], m["props"].get("Density","待补"), m["props"].get("Matter Type","待补"), m["props"].get("Obtained From","待补"), m["props"].get("Processed By","待补"), m["props"].get("Byproducts","—")] for m in MATERIALS], heading="全部材料"),
        M("版本：v0.5.4。"),
    ],
}
STEAM_DECK_ZH = {
    "slug": "sandustry/steam-deck",
    "title": "Steam Deck 上玩沙金工业",
    "metaTitle": "沙金工业 Steam Deck 指南",
    "metaDescription": "在 Steam Deck 上运行沙金工业：性能、设置与操作建议。",
    "intro": "沙金工业提供原生 Linux 版，社区报告在 Steam Deck 上可玩。以下是最佳体验设置。",
    "sections": [
        N("设置", [
            "原生 Linux 构建 — 无需 Proton。",
            "社区报告可玩（boilingsteam）；官方 Valve 兼容评级尚未发布。",
            "使用 Steam Input 映射操作 — 游戏没有完整手柄支持类别。",
        ]),
        M("来源：L1 社区报告 + L0 平台事实。版本 v0.5.4。"),
    ],
}
MACOS_ZH = {
    "slug": "sandustry/macos",
    "title": "macOS 上玩沙金工业",
    "metaTitle": "沙金工业 macOS 指南",
    "metaDescription": "沙金工业原生 macOS 支持与右键 Bug 规避。",
    "intro": "沙金工业有原生 macOS 版本。玩家报告了右键交互 Bug——这里提供规避方法。",
    "sections": [
        N("原生支持", [
            "官方 macOS 构建 — 无需转换层。",
            "已知问题：部分情境下右键交互会失败（社区报告）。",
            "规避：在补丁发布前重新绑定或改用其他输入方式。",
        ]),
        M("来源：L1 社区帖子 + L0 平台事实。版本 v0.5.4。"),
    ],
}
MOBILE_ZH = {
    "slug": "sandustry/mobile",
    "title": "沙金工业有手机版吗？",
    "metaTitle": "沙金工业手机版答案",
    "metaDescription": "沙金工业没有官方手机版。谨防假冒 APK 网站。",
    "intro": "没有——沙金工业没有官方手机版。网上流传的假冒 APK 下载页是骗局，请勿下载。",
    "sections": [
        N("官方平台", [
            "Steam、GOG、Microsoft Store 与 PC Game Pass。",
            "未公布 Android/iOS 版本。",
            "“沙金工业 APK”页面是骗局——只使用官方来源。",
        ]),
        M("来源：L0 官方平台 + L1 假冒页面观察。"),
    ],
}
ACHIEVEMENTS_ZH = {
    "slug": "sandustry/achievements",
    "title": "沙金工业全部成就（16个）",
    "metaTitle": "沙金工业 16 个成就",
    "metaDescription": "沙金工业 16 个成就与全球解锁率。",
    "intro": "沙金工业 16 个成就与全球解锁率（官方 Steam API 来源）。",
    "sections": [
        T(["成就", "解锁率"], [
            ["PROMOTION_PROTOCOL", "93.5%"], ["FLUX_IT_UP", "89.3%"], ["GOLD_IN_THE_BIN", "87.8%"],
            ["ANCIENT_TECHNOLOGY", "80.8%"], ["FIRST_BLOOM", "73.9%"], ["VOID_TOUCHED", "57.5%"],
            ["CRITTER_CATCHER", "50.9%"], ["FIRST_SPARK", "49.9%"], ["QUARTERMASTER", "42.3%"],
            ["STRATACORE_SECURED", "28.2%"], ["CONSERVATORY_CURATOR", "26.8%"], ["AURA_EXTRACTOR", "23.7%"],
            ["FULL_CIRCLE", "19.6%"], ["FINAL_SCHEMATIC", "16.4%"], ["VAULTKEEPER", "10.8%"],
            ["HELIODYNE_TYCOON", "0.4%"],
        ]),
        M("来源：Steam 成就 API（L0）。2026-08-17 采集。"),
    ],
}
FAQ_ZH = {
    "slug": "sandustry/faq",
    "title": "沙金工业 FAQ",
    "metaTitle": "沙金工业 FAQ",
    "metaDescription": "沙金工业常见问题：韩语支持、手机版、多人。",
    "intro": "沙金工业常见问题解答。",
    "sections": [
        F([
            ["沙金工业支持韩语吗？", "支持。官方提供韩语（界面+字幕）。"],
            ["有手机版吗？", "没有。谨防假冒 APK 下载站。官方平台：Steam、GOG、Microsoft Store、PC Game Pass。"],
            ["支持多人吗？", "不支持。这是单人游戏。"],
            ["如何获得金（Gold）？", "金是大多数加工的副产品。必须存入收集器（Collector）才会计入银行。"],
        ]),
    ],
}
UPDATES_ZH = {
    "slug": "sandustry/updates",
    "title": "沙金工业更新日志",
    "metaTitle": "沙金工业补丁日志",
    "metaDescription": "沙金工业最新补丁：v0.5.4、v0.5.3 与 EA 发布。",
    "intro": "Lantto Games 频繁发布抢先体验补丁。本页整理官方 Steam 新闻的最新补丁说明，每次更新都会刷新。",
    "sections": [
        T(["版本", "日期", "主要内容"], [
            ["v0.5.4（更新 #1）", "2026-08-16", "更好的过滤器编辑、Tier 5 软锁修复、红块临时移除、缩放快捷键"],
            ["v0.5.3（热修复）", "2026-08-14", "更好的日志、内存优化、更清晰的目标"],
            ["EA 发布", "2026-08-13", "沙金工业在 Steam、GOG、Microsoft Store 与 PC Game Pass 开启抢先体验"],
        ], heading="补丁记录"),
        N("更新方法", [
            "Steam：启动游戏时自动安装更新。",
            "GOG / Microsoft Store / PC Game Pass：商店端补丁可能晚于 Steam 发布。",
        ]),
        M("来源：官方 Steam 新闻（ISteamNews API，L0）。数据版本 v0.5.4（2026-08-17）。"),
    ],
}
MECHANICS_ZH = {
    "slug": "sandustry/mechanics",
    "title": "沙金工业机制：研究、工具、能量",
    "metaTitle": "沙金工业机制",
    "metaDescription": "沙金工业核心机制：研究推进、工具等级、能量机器。",
    "intro": "沙金工业的核心循环：用金与萤石研究、工具升级、能量驱动的机器。",
    "sections": [
        N("研究", [
            "金与萤石是两种主要推进材料——金用于研究新技术。",
            "金只有存入收集器（Collector）才会计入银行。",
        ]),
        N("工具", [
            "工具包括：铲子、枪、火箭发射器、钻头、激光、虚空枪、抓取器、火焰喷射器、低温爆破器、驱赶器、真空、抓钩、拆除器、标牌与管道移除器。",
            "更高级工具解锁更快的挖掘与加工。",
        ]),
        N("机器与能量", [
            "机器：传送带（及 Mk.2）、发射器、过滤器、振动筛、动能压机、种植箱、收集器、管道、泵、液体通风口、萤石发射器、蒸汽烘干机、清扫无人机。",
            "能量驱动机器；管理生产链以逐步自动化。",
        ]),
        M("来源：官方维基（L0）。数据版本 v0.5.4（2026-08-17）。"),
    ],
}

# ---------- ja（日本語）完整 i18n ----------
HOME_JA = {
    "slug": "sandustry",
    "title": "サンダストリー 攻略ハブ",
    "metaTitle": "サンダストリー攻略：素材・ガイド・パッチログ",
    "metaDescription": "サンダストリー攻略ハブ：素材、はじめ方、Steam Deck・macOS ガイド、モバイル版の回答、16個の実績と EA パッチログ。",
    "intro": "サンダストリーは、Lantto Games が開発し Hooded Horse がパブリッシングする、自動化・探索・基地建設のストラテジーゲームです。2026年8月13日より Steam、GOG、Microsoft Store、PC Game Pass で早期アクセス配信中。あらゆるピクセルが資源になります。",
    "sections": [
        N("このハブで扱う内容", [
            {"text": "はじめ方ガイド（日本語＋英語）", "href": "/ja/sandustry/getting-started"},
            {"text": f"全 {len(MATERIALS)} 種の素材の密度・種類・入手元・加工・物理特性", "href": "/ja/sandustry/materials"},
            {"text": "メカニクス：研究・ツール・エネルギー・機械", "href": "/ja/sandustry/mechanics"},
            {"text": "Steam Deck ガイド", "href": "/ja/sandustry/steam-deck"},
            {"text": "macOS ガイド", "href": "/ja/sandustry/macos"},
            {"text": "モバイル版の回答：公式モバイル版はなし", "href": "/ja/sandustry/mobile"},
            {"text": "全 16 個の実績と解除率", "href": "/ja/sandustry/achievements"},
            {"text": "よくある質問", "href": "/ja/sandustry/faq"},
            {"text": "EA パッチログとロードマップ（API 連動）", "href": "/ja/sandustry/updates"},
        ]),
        M(f"データバージョン: {MATERIALS_VERSION['version']}（{MATERIALS_VERSION['captured']} 取得）。出典: 公式 Wiki (L0) + Steam API (L0)。"),
    ],
}
GETTING_STARTED_JA = {
    "slug": "sandustry/getting-started",
    "title": "サンダストリー はじめ方",
    "metaTitle": "サンダストリー はじめ方：最初の工場と素材",
    "metaDescription": "サンダストリーのはじめ方ガイド：最初の工場、素材の理解、研究と進行。",
    "intro": "このガイドでは、最初のシャベルから最初の自動化工場までを案内します。",
    "sections": [
        S("最初のステップ", [
            "シャベル（Shovel）で土（Dirt）を掘りましょう — 土は砂（Sand）の主な供給源です。",
            "砂を集め、水（Water）で湿った砂（Wet Sand）に変え、金（Gold）へと加工していきます。",
            "コレクター（Collector）を建設して資源を貯めましょう — 金はコレクターに格納して初めてバンクに計上されます。",
            "金とフラクサイト（Fluxite）で研究（Research）を解放しましょう — この2つが主な進行用資源です。",
        ]),
        N("進行のループ", [
            "採掘 → 加工（水/火）→ 収集 → 研究 → 機械の建設 → 自動化",
            "金とフラクサイトが研究を前進させます。各素材の入手元と副産物は素材表をご覧ください。",
        ]),
        M("出典: 公式 Wiki (L0)。バージョン v0.5.4。"),
    ],
}
MATERIALS_JA = {
    "slug": "sandustry/materials",
    "title": "サンダストリーの全素材",
    "metaTitle": "サンダストリーの全素材：密度と入手元",
    "metaDescription": "サンダストリーの全素材：密度、物質の種類、入手元、加工、物理特性。",
    "intro": f"サンダストリーの全 {len(MATERIALS)} 種の素材。密度・種類・入手元・加工・物理特性（公式 Wiki 出典）。",
    "sections": [_materials_ja_table(), M("バージョン: v0.5.4。")],
}
STEAM_DECK_JA = {
    "slug": "sandustry/steam-deck",
    "title": "Steam Deck でサンダストリーをプレイ",
    "metaTitle": "Steam Deck 版サンダストリー：設定と性能",
    "metaDescription": "Steam Deck でサンダストリーを動かす：性能、設定、操作のヒント。",
    "intro": "サンダストリーはネイティブ Linux 対応で、Steam Deck でプレイ可能との報告があります。最適な体験を得る方法を紹介します。",
    "sections": [
        N("セットアップ", [
            "ネイティブ Linux ビルド — Proton は不要です。",
            "コミュニティ報告（boilingsteam）ではプレイ可能。Valve 公式の互換性評価はまだ公開されていません。",
            "Steam Input で操作を割り当てましょう — このゲームは完全なコントローラー対応カテゴリを持っていません。",
        ]),
        M("出典: L1 コミュニティ報告 + L0 プラットフォーム事実。バージョン v0.5.4。"),
    ],
}
MACOS_JA = {
    "slug": "sandustry/macos",
    "title": "macOS でサンダストリーをプレイ",
    "metaTitle": "macOS 版サンダストリー：ネイティブ対応と不具合",
    "metaDescription": "サンダストリーの macOS ネイティブ対応、右クリックの不具合と回避策。",
    "intro": "サンダストリーにはネイティブ macOS 版があります。右クリック操作の不具合がプレイヤーから報告されています — 回避策を紹介します。",
    "sections": [
        N("ネイティブ対応", [
            "公式 macOS ビルド — 変換レイヤーは不要です。",
            "既知の問題: 一部の場面で右クリック操作が失敗することがあります（コミュニティ報告）。",
            "回避策: パッチが配信されるまで、キー再割り当てや別の入力をお使いください。",
        ]),
        M("出典: L1 コミュニティスレッド + L0 プラットフォーム事実。バージョン v0.5.4。"),
    ],
}
MOBILE_JA = {
    "slug": "sandustry/mobile",
    "title": "サンダストリーにモバイル版はある？",
    "metaTitle": "サンダストリーのモバイル版：なし（偽 APK に注意）",
    "metaDescription": "サンダストリーに公式モバイル版はありません。偽 APK 配布サイトは詐欺です。",
    "intro": "いいえ — サンダストリーに公式モバイル版はありません。偽の APK ダウンロードページが出回っています。ダウンロードしないでください。",
    "sections": [
        N("公式プラットフォーム", [
            "Steam、GOG、Microsoft Store、PC Game Pass。",
            "Android/iOS 版の発表はありません。",
            "偽の「Sandustry APK」ページは詐欺です — 公式ソースのみ利用してください。",
        ]),
        M("出典: L0 公式プラットフォーム + L1 偽ページ観察。"),
    ],
}
ACHIEVEMENTS_JA = {
    "slug": "sandustry/achievements",
    "title": "サンダストリーの全実績（16個）",
    "metaTitle": "サンダストリーの全16実績（解除率）",
    "metaDescription": "サンダストリーの全16個の実績とグローバル解除率。",
    "intro": "サンダストリーの全16個の実績と、公式 Steam API によるグローバル解除率。",
    "sections": [
        T(["実績", "解除率"], [
            ["PROMOTION_PROTOCOL", "93.5%"], ["FLUX_IT_UP", "89.3%"], ["GOLD_IN_THE_BIN", "87.8%"],
            ["ANCIENT_TECHNOLOGY", "80.8%"], ["FIRST_BLOOM", "73.9%"], ["VOID_TOUCHED", "57.5%"],
            ["CRITTER_CATCHER", "50.9%"], ["FIRST_SPARK", "49.9%"], ["QUARTERMASTER", "42.3%"],
            ["STRATACORE_SECURED", "28.2%"], ["CONSERVATORY_CURATOR", "26.8%"], ["AURA_EXTRACTOR", "23.7%"],
            ["FULL_CIRCLE", "19.6%"], ["FINAL_SCHEMATIC", "16.4%"], ["VAULTKEEPER", "10.8%"],
            ["HELIODYNE_TYCOON", "0.4%"],
        ]),
        M("出典: Steam 実績 API (L0)。2026-08-17 取得。"),
    ],
}
FAQ_JA = {
    "slug": "sandustry/faq",
    "title": "サンダストリー FAQ",
    "metaTitle": "サンダストリー FAQ：韓国語・モバイル・マルチ",
    "metaDescription": "サンダストリーのよくある質問：韓国語対応、モバイル版、マルチプレイ。",
    "intro": "サンダストリーについてのよくある質問。",
    "sections": [
        F([
            ["サンダストリーは韓国語に対応していますか？", "はい。韓国語（インターフェース＋字幕）を公式にサポートしています。"],
            ["モバイル版はありますか？", "ありません。偽の APK ダウンロードサイトにご注意ください。公式プラットフォームは Steam、GOG、Microsoft Store、PC Game Pass です。"],
            ["マルチプレイはありますか？", "ありません。シングルプレイのゲームです。"],
            ["金（Gold）はどうやって入手しますか？", "金はほとんどの加工の副産物として得られます。コレクター（Collector）ブロックに格納して初めてバンクに計上されます。"],
        ], heading="よくある質問"),
    ],
}
UPDATES_JA = {
    "slug": "sandustry/updates",
    "title": "サンダストリー アップデートとパッチノート",
    "metaTitle": "サンダストリー パッチノート：v0.5.4 と v0.5.3",
    "metaDescription": "サンダストリー最新パッチノート：v0.5.4（フィルター編集、Tier 5 修正）、v0.5.3 修正、EA リリース。",
    "intro": "Lantto Games は早期アクセスのパッチを頻繁に配信しています。このページでは公式 Steam ニュースの最新パッチノートを追跡し、新しいアップデートが配信されるたびに更新されます。",
    "sections": [
        T(["バージョン", "日付", "主な内容"], [
            ["v0.5.4（アップデート #1）", "2026-08-16", "フィルター編集の改善、Tier 5 のソフトロック修正、赤ブロックの一時削除、ズームのキー割り当て"],
            ["v0.5.3（ホットフィックス）", "2026-08-14", "ログの改善、メモリ最適化、より明確な目標"],
            ["EA リリース", "2026-08-13", "サンダストリーが Steam、GOG、Microsoft Store、PC Game Pass で早期アクセス開始"],
        ], heading="パッチ履歴"),
        N("更新方法", [
            "Steam：ゲームを起動すると更新が自動でインストールされます。",
            "GOG / Microsoft Store / PC Game Pass：ストア側のパッチは Steam 版のリリースに後続する場合があります。",
        ]),
        M("出典: 公式 Steam ニュース (ISteamNews API, L0)。データバージョン v0.5.4 (2026-08-17)。"),
    ],
}
MECHANICS_JA = {
    "slug": "sandustry/mechanics",
    "title": "サンダストリーのメカニクス：研究・ツール・エネルギー",
    "metaTitle": "サンダストリーのメカニクス：研究とツール",
    "metaDescription": "サンダストリーのコアメカニクス：研究の進行、ツールの段階、エネルギーと機械。",
    "intro": "サンダストリーのコアループ：金とフラクサイトによる研究、ツールのアップグレード、エネルギーで動く機械。",
    "sections": [
        N("研究", [
            "金（Gold）とフラクサイト（Fluxite）は主要な進行用資源です — 金は新技術の研究に使われます。",
            "金はコレクター（Collector）ブロックに格納して初めてバンクに計上されます。",
        ]),
        N("ツール", [
            "ツールには、シャベル、ガン、ロケットランチャー、ドリル、レーザー、ヴォイドガン、グラバー、火炎放射器、クライオブラスター、コララー、バキューム、グラップリングフック、デモリッシャー、マーキー、パイプリムーバーがあります。",
            "上位のツールは、より速い採掘と加工を解放します。",
        ]),
        N("機械とエネルギー", [
            "機械：コンベアベルト（Mk.2 含む）、ランチャー、フィルター、シェーカー、キネティックプレス、プランターボックス、コレクター、パイプ、ポンプ、液体ベント、フラックスエマネーター、スチームドライヤー、スイーパードローン。",
            "エネルギーが機械を動かします。生産チェーンを管理して段階的に自動化しましょう。",
        ]),
        M("出典: 公式 Wiki (L0)。データバージョン v0.5.4 (2026-08-17)。"),
    ],
}

# ---------- fr（Français）完整 i18n ----------
HOME_FR = {
    "slug": "sandustry",
    "title": "Guide Sandustry",
    "metaTitle": "Guide Sandustry : matériaux, guides et notes de patch",
    "metaDescription": "Le hub de guides Sandustry : matériaux, prise en main, guides Steam Deck et macOS, réponse mobile, 16 succès et journal des patchs EA.",
    "intro": "Sandustry est un jeu de stratégie d'automatisation, d'exploration et de construction de base développé par Lantto Games et édité par Hooded Horse. En accès anticipé depuis le 13 août 2026 sur Steam, GOG, Microsoft Store et PC Game Pass ; chaque pixel est une ressource.",
    "sections": [
        N("Ce que couvre ce hub", [
            {"text": "Prise en main (français + anglais)", "href": "/fr/sandustry/getting-started"},
            {"text": f"Les {len(MATERIALS)} matériaux : densité, type, source, transformation et physique", "href": "/fr/sandustry/materials"},
            {"text": "Mécaniques : recherche, outils, énergie et machines", "href": "/fr/sandustry/mechanics"},
            {"text": "Guide Steam Deck", "href": "/fr/sandustry/steam-deck"},
            {"text": "Guide macOS", "href": "/fr/sandustry/macos"},
            {"text": "Réponse mobile : aucune version mobile officielle", "href": "/fr/sandustry/mobile"},
            {"text": "Les 16 succès avec leurs taux de déblocage", "href": "/fr/sandustry/achievements"},
            {"text": "FAQ", "href": "/fr/sandustry/faq"},
            {"text": "Journal des patchs EA et feuille de route (via API)", "href": "/fr/sandustry/updates"},
        ]),
        M(f"Version des données : {MATERIALS_VERSION['version']} (capturées le {MATERIALS_VERSION['captured']}). Sources : wiki officiel (L0) + API Steam (L0)."),
    ],
}
GETTING_STARTED_FR = {
    "slug": "sandustry/getting-started",
    "title": "Débuter sur Sandustry",
    "metaTitle": "Débuter sur Sandustry : première usine et matériaux",
    "metaDescription": "Guide de prise en main de Sandustry : première usine, comprendre les matériaux, recherche et progression.",
    "intro": "Ce guide vous mène de votre première pelle à votre première usine automatisée dans Sandustry.",
    "sections": [
        S("Premiers pas", [
            "Commencez par miner de la terre (Dirt) avec votre pelle (Shovel) — la terre est la principale source de sable (Sand).",
            "Récupérez le sable et laissez l'eau (Water) le transformer en sable mouillé (Wet Sand) ; progressez vers l'or (Gold).",
            "Construisez un collecteur (Collector) pour stocker les ressources — l'or doit être rangé dans des blocs Collector pour compter dans votre banque.",
            "Débloquez la recherche (Research) avec l'or et la fluxite (Fluxite) — ce sont les deux principales ressources de progression.",
        ]),
        N("Boucle de progression", [
            "Miner → transformer (eau/feu) → collecter → rechercher → construire des machines → automatiser.",
            "L'or et la fluxite font avancer la recherche ; consultez le tableau des matériaux pour chaque source et sous-produit.",
        ]),
        M("Source : wiki officiel (L0). Version v0.5.4."),
    ],
}
MATERIALS_FR = {
    "slug": "sandustry/materials",
    "title": "Tous les matériaux de Sandustry",
    "metaTitle": "Tous les matériaux de Sandustry : densité et sources",
    "metaDescription": "Chaque matériau de Sandustry avec densité, type de matière, source, transformation et physique.",
    "intro": f"Les {len(MATERIALS)} matériaux de Sandustry, avec densité, type, source, transformation et physique tirés du wiki officiel.",
    "sections": [_materials_fr_table(), M("Version : v0.5.4.")],
}
STEAM_DECK_FR = {
    "slug": "sandustry/steam-deck",
    "title": "Sandustry sur Steam Deck",
    "metaTitle": "Sandustry sur Steam Deck : réglages et performances",
    "metaDescription": "Jouer à Sandustry sur Steam Deck : performances, réglages et conseils de contrôles.",
    "intro": "Sandustry bénéficie d'un support Linux natif et serait jouable sur Steam Deck. Voici comment obtenir la meilleure expérience.",
    "sections": [
        N("Configuration", [
            "Build Linux natif — aucun Proton requis.",
            "Jouable selon les retours de la communauté (boilingsteam) ; l'évaluation officielle de compatibilité Valve n'est pas encore publiée.",
            "Utilisez Steam Input pour mapper les contrôles — le jeu n'a pas de catégorie de prise en charge complète de la manette.",
        ]),
        M("Source : retours communautaires L1 + faits de plateforme L0. Version v0.5.4."),
    ],
}
MACOS_FR = {
    "slug": "sandustry/macos",
    "title": "Sandustry sur macOS",
    "metaTitle": "Sandustry sur macOS : support natif et bug",
    "metaDescription": "Le support macOS natif de Sandustry, le bug de clic droit et les solutions de contournement.",
    "intro": "Sandustry dispose d'une version macOS native. Un bug d'interaction au clic droit a été signalé par les joueurs — voici la solution.",
    "sections": [
        N("Support natif", [
            "Build macOS officiel — aucune couche de traduction.",
            "Problème connu : les interactions au clic droit peuvent échouer dans certains contextes (retours communautaires).",
            "Contournement : rebindez ou utilisez une autre entrée jusqu'à ce qu'un correctif sorte.",
        ]),
        M("Source : fils communautaires L1 + faits de plateforme L0. Version v0.5.4."),
    ],
}
MOBILE_FR = {
    "slug": "sandustry/mobile",
    "title": "Sandustry est-il disponible sur mobile ?",
    "metaTitle": "Sandustry sur mobile ? Non (avertissement faux APK)",
    "metaDescription": "Sandustry n'a aucune version mobile officielle. Les sites de téléchargement d'APK contrefaits sont des arnaques.",
    "intro": "Non — Sandustry n'a aucune version mobile officielle. De fausses pages de téléchargement d'APK circulent ; ne les téléchargez pas.",
    "sections": [
        N("Plateformes officielles", [
            "Steam, GOG, Microsoft Store et PC Game Pass.",
            "Aucune version Android/iOS annoncée.",
            "Les fausses pages « Sandustry APK » sont des arnaques — sources officielles uniquement.",
        ]),
        M("Source : plateformes officielles L0 + observation de fausses pages L1."),
    ],
}
ACHIEVEMENTS_FR = {
    "slug": "sandustry/achievements",
    "title": "Tous les succès Sandustry (16)",
    "metaTitle": "Les 16 succès Sandustry (taux)",
    "metaDescription": "Les 16 succès Sandustry et leurs taux de déblocage mondiaux.",
    "intro": "Les 16 succès Sandustry avec leurs taux de déblocage mondiaux issus de l'API Steam officielle.",
    "sections": [
        T(["Succès", "Taux de déblocage"], [
            ["PROMOTION_PROTOCOL", "93.5%"], ["FLUX_IT_UP", "89.3%"], ["GOLD_IN_THE_BIN", "87.8%"],
            ["ANCIENT_TECHNOLOGY", "80.8%"], ["FIRST_BLOOM", "73.9%"], ["VOID_TOUCHED", "57.5%"],
            ["CRITTER_CATCHER", "50.9%"], ["FIRST_SPARK", "49.9%"], ["QUARTERMASTER", "42.3%"],
            ["STRATACORE_SECURED", "28.2%"], ["CONSERVATORY_CURATOR", "26.8%"], ["AURA_EXTRACTOR", "23.7%"],
            ["FULL_CIRCLE", "19.6%"], ["FINAL_SCHEMATIC", "16.4%"], ["VAULTKEEPER", "10.8%"],
            ["HELIODYNE_TYCOON", "0.4%"],
        ]),
        M("Source : API des succès Steam (L0). Capturé le 2026-08-17."),
    ],
}
FAQ_FR = {
    "slug": "sandustry/faq",
    "title": "FAQ Sandustry",
    "metaTitle": "FAQ Sandustry : coréen, mobile, multijoueur",
    "metaDescription": "Questions fréquentes sur Sandustry : support coréen, version mobile, multijoueur.",
    "intro": "Questions fréquemment posées sur Sandustry.",
    "sections": [
        F([
            ["Sandustry prend-il en charge le coréen ?", "Oui. Le coréen (interface + sous-titres) est officiellement pris en charge."],
            ["Y a-t-il une version mobile ?", "Non. Méfiez-vous des faux sites de téléchargement d'APK. Plateformes officielles : Steam, GOG, Microsoft Store, PC Game Pass."],
            ["Y a-t-il du multijoueur ?", "Non. C'est un jeu solo."],
            ["Comment obtenir de l'or (Gold) ?", "L'or est un sous-produit de la plupart des transformations. Il doit être rangé dans des blocs Collector pour compter dans votre banque."],
        ], heading="Questions fréquentes"),
    ],
}
UPDATES_FR = {
    "slug": "sandustry/updates",
    "title": "Mises à jour et notes de patch Sandustry",
    "metaTitle": "Notes de patch Sandustry : v0.5.4 et v0.5.3",
    "metaDescription": "Les dernières notes de patch Sandustry : v0.5.4 (filtres, corrections Tier 5), le correctif v0.5.3 et le lancement EA.",
    "intro": "Lantto Games publie de fréquents correctifs d'accès anticipé. Cette page suit les dernières notes de patch des actualités Steam officielles ; elle est mise à jour à chaque nouvelle mise à jour.",
    "sections": [
        T(["Version", "Date", "Points clés"], [
            ["v0.5.4 (Mise à jour n°1)", "2026-08-16", "Meilleure édition des filtres, corrections de blocage du Tier 5, retrait temporaire des blocs rouges, raccourcis de zoom"],
            ["v0.5.3 (Correctif)", "2026-08-14", "Meilleurs journaux, optimisations mémoire, objectifs plus clairs"],
            ["Lancement EA", "2026-08-13", "Sandustry entre en accès anticipé sur Steam, GOG, Microsoft Store et PC Game Pass"],
        ], heading="Historique des patchs"),
        N("Comment mettre à jour", [
            "Steam : les mises à jour s'installent automatiquement au lancement du jeu.",
            "GOG / Microsoft Store / PC Game Pass : les correctifs côté boutique peuvent suivre la sortie Steam.",
        ]),
        M("Source : actualités Steam officielles (API ISteamNews, L0). Version des données v0.5.4 (2026-08-17)."),
    ],
}
MECHANICS_FR = {
    "slug": "sandustry/mechanics",
    "title": "Mécaniques de Sandustry : recherche, outils, énergie",
    "metaTitle": "Mécaniques de Sandustry : recherche et outils",
    "metaDescription": "Les mécaniques de base de Sandustry : progression de la recherche, niveaux d'outils, énergie et machines.",
    "intro": "Les boucles centrales de Sandustry : la recherche avec l'or et la fluxite, les améliorations d'outils et les machines alimentées en énergie.",
    "sections": [
        N("Recherche", [
            "L'or (Gold) et la fluxite (Fluxite) sont les deux principales ressources de progression — l'or sert à rechercher de nouvelles technologies.",
            "L'or ne compte dans votre banque que lorsqu'il est rangé dans des blocs Collector.",
        ]),
        N("Outils", [
            "Les outils comprennent la pelle (Shovel), le pistolet (Gun), le lance-roquettes (Rocket Launcher), la perceuse (Drill), le laser (Laser), le pistolet du vide (Void Gun), le grappin (Grabber), le lance-flammes (Flamethrower), le cryoblaster (Cryoblaster), le corraller (Corraller), l'aspirateur (Vacuum), le grappin (Grappling Hook), le démolisseur (Demolisher), le marquee (Marquee) et le retire-tuyau (Pipe Remover).",
            "Les outils de niveau supérieur débloquent une extraction et une transformation plus rapides.",
        ]),
        N("Machines et énergie", [
            "Machines : tapis roulant (Conveyor Belt, et Mk.2), lanceur (Launcher), filtre (Filter), secoueur (Shaker), presse cinétique (Kinetic Press), bac à planter (Planter Box), collecteur (Collector), tuyau (Pipe), pompe (Pump), évent à liquide (Liquid Vent), émanateur de flux (Flux Emanator), séchoir à vapeur (Steam Dryer), drone balayeur (Sweeper Drone).",
            "L'énergie alimente les machines ; gérez les chaînes de production pour automatiser progressivement.",
        ]),
        M("Source : wiki officiel (L0). Version des données v0.5.4 (2026-08-17)."),
    ],
}

# ---------- de（Deutsch）完整 i18n ----------
HOME_DE = {
    "slug": "sandustry",
    "title": "Sandustry-Guide-Hub",
    "metaTitle": "Sandustry-Guide: Materialien, Guides & Patch-Protokoll",
    "metaDescription": "Sandustry-Guide-Hub: Materialien, Einstieg, Steam-Deck- und macOS-Guides, Mobile-Antwort, 16 Erfolge und EA-Patch-Protokoll.",
    "intro": "Sandustry ist ein Automations-, Erkundungs- und Basisbau-Strategiespiel von Lantto Games, veröffentlicht von Hooded Horse. Seit dem 13. August 2026 im Early Access auf Steam, GOG, Microsoft Store und PC Game Pass; jeder Pixel ist eine Ressource.",
    "sections": [
        N("Was dieser Hub abdeckt", [
            {"text": "Einstieg (Deutsch + Englisch)", "href": "/de/sandustry/getting-started"},
            {"text": f"Alle {len(MATERIALS)} Materialien mit Dichte, Typ, Quelle, Verarbeitung und Physik", "href": "/de/sandustry/materials"},
            {"text": "Mechanik: Forschung, Werkzeuge, Energie und Maschinen", "href": "/de/sandustry/mechanics"},
            {"text": "Steam-Deck-Guide", "href": "/de/sandustry/steam-deck"},
            {"text": "macOS-Guide", "href": "/de/sandustry/macos"},
            {"text": "Mobile-Antwort: keine offizielle Mobile-Version", "href": "/de/sandustry/mobile"},
            {"text": "Alle 16 Erfolge mit Freischaltraten", "href": "/de/sandustry/achievements"},
            {"text": "FAQ", "href": "/de/sandustry/faq"},
            {"text": "EA-Patch-Protokoll & Roadmap (API-basiert)", "href": "/de/sandustry/updates"},
        ]),
        M(f"Datenversion: {MATERIALS_VERSION['version']} (erfasst am {MATERIALS_VERSION['captured']}). Quellen: offizielles Wiki (L0) + Steam-API (L0)."),
    ],
}
GETTING_STARTED_DE = {
    "slug": "sandustry/getting-started",
    "title": "Sandustry-Einstieg",
    "metaTitle": "Sandustry-Einstieg: erste Fabrik & Materialien",
    "metaDescription": "Sandustry-Einstiegsguide: erste Fabrik, Materialien verstehen, Forschung und Fortschritt.",
    "intro": "Dieser Guide bringt dich von deiner ersten Schaufel bis zu deiner ersten automatisierten Fabrik in Sandustry.",
    "sections": [
        S("Erste Schritte", [
            "Grabe zuerst Erde (Dirt) mit deiner Schaufel (Shovel) — Erde ist die Hauptquelle für Sand.",
            "Sammle Sand und lass Wasser (Water) ihn zu nassem Sand (Wet Sand) machen; arbeite dich zu Gold vor.",
            "Baue einen Sammler (Collector), um Ressourcen zu lagern — Gold muss in Collector-Blöcken liegen, um auf dein Konto zu zählen.",
            "Schalte die Forschung (Research) mit Gold und Fluxit (Fluxite) frei — das sind die zwei wichtigsten Fortschrittsmaterialien.",
        ]),
        N("Fortschritts-Schleife", [
            "Abbauen → verarbeiten (Wasser/Feuer) → sammeln → forschen → Maschinen bauen → automatisieren.",
            "Gold und Fluxit treiben die Forschung an; sieh dir die Materialtabelle für jede Quelle und jedes Nebenprodukt an.",
        ]),
        M("Quelle: offizielles Wiki (L0). Version v0.5.4."),
    ],
}
MATERIALS_DE = {
    "slug": "sandustry/materials",
    "title": "Alle Sandustry-Materialien",
    "metaTitle": "Alle Sandustry-Materialien: Dichte & Quellen",
    "metaDescription": "Jedes Sandustry-Material mit Dichte, Materietyp, Quelle, Verarbeitung und Physik.",
    "intro": f"Alle {len(MATERIALS)} Materialien in Sandustry, mit Dichte, Typ, Quelle, Verarbeitung und Physik aus dem offiziellen Wiki.",
    "sections": [_materials_de_table(), M("Version: v0.5.4.")],
}
STEAM_DECK_DE = {
    "slug": "sandustry/steam-deck",
    "title": "Sandustry auf dem Steam Deck",
    "metaTitle": "Sandustry auf dem Steam Deck: Einstellungen & Leistung",
    "metaDescription": "Sandustry auf dem Steam Deck spielen: Leistung, Einstellungen und Steuerungs-Tipps.",
    "intro": "Sandustry unterstützt Linux nativ und ist Berichten zufolge auf dem Steam Deck spielbar. So holst du das beste Erlebnis heraus.",
    "sections": [
        N("Einrichtung", [
            "Nativer Linux-Build — kein Proton nötig.",
            "Laut Community-Berichten (boilingsteam) spielbar; die offizielle Valve-Kompatibilitätsbewertung ist noch nicht veröffentlicht.",
            "Nutze Steam Input zum Belegen der Steuerung — das Spiel hat keine Kategorie für vollständige Controller-Unterstützung.",
        ]),
        M("Quelle: L1-Community-Berichte + L0-Plattformfakten. Version v0.5.4."),
    ],
}
MACOS_DE = {
    "slug": "sandustry/macos",
    "title": "Sandustry auf macOS",
    "metaTitle": "Sandustry auf macOS: nativer Support & Bug",
    "metaDescription": "Nativer macOS-Support für Sandustry, der Rechtsklick-Bug und Workarounds.",
    "intro": "Sandustry hat eine native macOS-Version. Spieler melden einen Rechtsklick-Interaktionsbug — hier ist der Workaround.",
    "sections": [
        N("Nativer Support", [
            "Offizieller macOS-Build — keine Übersetzungsschicht.",
            "Bekanntes Problem: Rechtsklick-Interaktionen können in manchen Kontexten fehlschlagen (Community-Berichte).",
            "Workaround: Belege die Taste neu oder nutze eine alternative Eingabe, bis ein Patch erscheint.",
        ]),
        M("Quelle: L1-Community-Threads + L0-Plattformfakten. Version v0.5.4."),
    ],
}
MOBILE_DE = {
    "slug": "sandustry/mobile",
    "title": "Gibt es Sandustry für Mobilgeräte?",
    "metaTitle": "Sandustry für Mobilgeräte? Nein (Warnung vor Fake-APKs)",
    "metaDescription": "Sandustry hat keine offizielle Mobile-Version. Fake-APK-Downloadseiten sind Betrug.",
    "intro": "Nein — Sandustry hat keine offizielle Mobile-Version. Gefälschte APK-Downloadseiten kursieren; lade nichts von ihnen herunter.",
    "sections": [
        N("Offizielle Plattformen", [
            "Steam, GOG, Microsoft Store und PC Game Pass.",
            "Keine Android-/iOS-Version angekündigt.",
            "Gefälschte „Sandustry-APK“-Seiten sind Betrug — nur offizielle Quellen nutzen.",
        ]),
        M("Quelle: L0-offizielle Plattformen + L1-Beobachtung von Fake-Seiten."),
    ],
}
ACHIEVEMENTS_DE = {
    "slug": "sandustry/achievements",
    "title": "Alle Sandustry-Erfolge (16)",
    "metaTitle": "Alle 16 Sandustry-Erfolge (Raten)",
    "metaDescription": "Alle 16 Sandustry-Erfolge und ihre globalen Freischaltraten.",
    "intro": "Alle 16 Sandustry-Erfolge mit globalen Freischaltraten aus der offiziellen Steam-API.",
    "sections": [
        T(["Erfolg", "Freischaltrate"], [
            ["PROMOTION_PROTOCOL", "93.5%"], ["FLUX_IT_UP", "89.3%"], ["GOLD_IN_THE_BIN", "87.8%"],
            ["ANCIENT_TECHNOLOGY", "80.8%"], ["FIRST_BLOOM", "73.9%"], ["VOID_TOUCHED", "57.5%"],
            ["CRITTER_CATCHER", "50.9%"], ["FIRST_SPARK", "49.9%"], ["QUARTERMASTER", "42.3%"],
            ["STRATACORE_SECURED", "28.2%"], ["CONSERVATORY_CURATOR", "26.8%"], ["AURA_EXTRACTOR", "23.7%"],
            ["FULL_CIRCLE", "19.6%"], ["FINAL_SCHEMATIC", "16.4%"], ["VAULTKEEPER", "10.8%"],
            ["HELIODYNE_TYCOON", "0.4%"],
        ]),
        M("Quelle: Steam-Erfolge-API (L0). Erfasst am 2026-08-17."),
    ],
}
FAQ_DE = {
    "slug": "sandustry/faq",
    "title": "Sandustry-FAQ",
    "metaTitle": "Sandustry-FAQ: Koreanisch, Mobile, Multiplayer",
    "metaDescription": "Häufig gestellte Fragen zu Sandustry: Koreanisch-Support, Mobile-Version, Multiplayer.",
    "intro": "Häufig gestellte Fragen zu Sandustry.",
    "sections": [
        F([
            ["Unterstützt Sandustry Koreanisch?", "Ja. Koreanisch (Oberfläche + Untertitel) wird offiziell unterstützt."],
            ["Gibt es eine Mobile-Version?", "Nein. Vorsicht vor gefälschten APK-Downloadseiten. Offizielle Plattformen: Steam, GOG, Microsoft Store, PC Game Pass."],
            ["Gibt es Multiplayer?", "Nein. Es ist ein Einzelspieler-Spiel."],
            ["Wie bekomme ich Gold?", "Gold ist ein Nebenprodukt der meisten Verarbeitungsprozesse. Es muss in Collector-Blöcken gelagert werden, um auf dein Konto zu zählen."],
        ], heading="Häufig gestellte Fragen"),
    ],
}
UPDATES_DE = {
    "slug": "sandustry/updates",
    "title": "Sandustry-Updates & Patch-Notes",
    "metaTitle": "Sandustry-Patch-Notes: v0.5.4 & v0.5.3",
    "metaDescription": "Die neuesten Sandustry-Patch-Notes: v0.5.4 (Filter-Bearbeitung, Tier-5-Fixes), v0.5.3-Hotfix und der EA-Start — aktualisiert mit jedem neuen Patch.",
    "intro": "Lantto Games veröffentlicht regelmäßig Early-Access-Patches. Diese Seite verfolgt die neuesten Patch-Notes aus den offiziellen Steam-News und wird bei jedem neuen Update aktualisiert.",
    "sections": [
        T(["Version", "Datum", "Highlights"], [
            ["v0.5.4 (Update #1)", "2026-08-16", "Bessere Filter-Bearbeitung, Tier-5-Softlock-Fixes, vorübergehende Entfernung roter Blöcke, Zoom-Tastenbelegungen"],
            ["v0.5.3 (Hotfix)", "2026-08-14", "Besseres Logging, Speicher-Optimierungen, klarere Ziele"],
            ["EA-Start", "2026-08-13", "Sandustry startet in den Early Access auf Steam, GOG, Microsoft Store und PC Game Pass"],
        ], heading="Patch-Verlauf"),
        N("So aktualisierst du", [
            "Steam: Updates werden beim Spielstart automatisch installiert.",
            "GOG / Microsoft Store / PC Game Pass: Store-seitige Patches können der Steam-Veröffentlichung folgen.",
        ]),
        M("Quelle: offizielle Steam-News (ISteamNews-API, L0). Datenversion v0.5.4 (2026-08-17)."),
    ],
}
MECHANICS_DE = {
    "slug": "sandustry/mechanics",
    "title": "Sandustry-Mechanik: Forschung, Werkzeuge, Energie",
    "metaTitle": "Sandustry-Mechanik: Forschung & Werkzeuge",
    "metaDescription": "Sandustry-Kernmechaniken: Forschungsfortschritt, Werkzeugstufen, Energie und Maschinen.",
    "intro": "Die Kernschleifen von Sandustry: Forschung mit Gold und Fluxit, Werkzeug-Upgrades und energiebetriebene Maschinen.",
    "sections": [
        N("Forschung", [
            "Gold und Fluxit sind die zwei wichtigsten Fortschrittsmaterialien — Gold wird zum Erforschen neuer Technologien verwendet.",
            "Gold zählt nur dann auf dein Konto, wenn es in Collector-Blöcken gelagert wird.",
        ]),
        N("Werkzeuge", [
            "Zu den Werkzeugen gehören Schaufel (Shovel), Gun, Raketenwerfer (Rocket Launcher), Bohrer (Drill), Laser, Void Gun, Grabber, Flammenwerfer (Flamethrower), Cryoblaster, Corraller, Vacuum, Grappling Hook, Demolisher, Marquee und Pipe Remover.",
            "Höherstufige Werkzeuge schalten schnelleres Abbauen und Verarbeiten frei.",
        ]),
        N("Maschinen & Energie", [
            "Maschinen: Förderband (Conveyor Belt, und Mk.2), Launcher, Filter, Shaker, Kinetic Press, Planter Box, Collector, Pipe, Pump, Liquid Vent, Flux Emanator, Steam Dryer, Sweeper Drone.",
            "Energie treibt die Maschinen an; verwalte Produktionsketten, um Schritt für Schritt zu automatisieren.",
        ]),
        M("Quelle: offizielles Wiki (L0). Datenversion v0.5.4 (2026-08-17)."),
    ],
}
