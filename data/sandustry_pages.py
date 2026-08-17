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
            p.get("Density", "待补"),
            p.get("Matter Type", "待补"),
            p.get("Obtained From", "待补"),
            p.get("Processed By", "待补"),
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
    "metaDescription": "샌더스트리 가이드 허브: 전체 재료 속성, 시작 가이드, Steam Deck·macOS 가이드, 모바일 답변, 16개 업적, EA 패치 로그 — 한국어와 영어.",
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
        # 语言白名单：en(默认) + ko(主) + zh-CN(条件性)；ja/fr/de 不生成（G2 语言策略）
        "languages": ["en", "ko", "zh-CN"],
    }
    if page_i18n:
        p["i18n"] = page_i18n
    return p

def build_sandustry_pages():
    """返回 Sandustry 页面列表，供 build_content.py 追加到 d['pages']。"""
    reg = {
        "sandustry": (HOME_EN, {"ko": HOME_KO, "zh-CN": HOME_ZH}),
        "sandustry/getting-started": (GETTING_STARTED_EN, {"ko": GETTING_STARTED_KO, "zh-CN": GETTING_STARTED_ZH}),
        "sandustry/materials": (MATERIALS_EN, {"ko": MATERIALS_KO, "zh-CN": MATERIALS_ZH}),
        "sandustry/steam-deck": (STEAM_DECK_EN, {"ko": STEAM_DECK_KO, "zh-CN": STEAM_DECK_ZH}),
        "sandustry/macos": (MACOS_EN, {"ko": MACOS_KO, "zh-CN": MACOS_ZH}),
        "sandustry/mobile": (MOBILE_EN, {"ko": MOBILE_KO, "zh-CN": MOBILE_ZH}),
        "sandustry/achievements": (ACHIEVEMENTS_EN, {"ko": ACHIEVEMENTS_KO, "zh-CN": ACHIEVEMENTS_ZH}),
        "sandustry/faq": (FAQ_EN, {"ko": FAQ_KO, "zh-CN": FAQ_ZH}),
        "sandustry/updates": (UPDATES_EN, {"ko": UPDATES_KO, "zh-CN": UPDATES_ZH}),
        "sandustry/mechanics": (MECHANICS_EN, {"ko": MECHANICS_KO, "zh-CN": MECHANICS_ZH}),
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
