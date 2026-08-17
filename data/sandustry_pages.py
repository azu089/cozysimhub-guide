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
    "metaTitle": "Sandustry Guide: Materials, Getting Started, Steam Deck, Achievements & Patch Log",
    "metaDescription": "Sandustry guide hub: all materials with properties, getting-started, Steam Deck and macOS guides, mobile answer, 16 achievements, EA patch log — Korean and English.",
    "intro": "Sandustry is an automation, exploration and base-building strategy game by Lantto Games, published by Hooded Horse. EA since August 13, 2026 on Steam, GOG, Microsoft Store and PC Game Pass; every pixel is a resource.",
    "sections": [
        N("What this hub covers", [
            "Getting started (Korean + English)",
            f"All {len(MATERIALS)} materials with density, type, source, processing and physics",
            "Steam Deck and macOS guides",
            "Mobile answer: no official mobile version — beware fake APK sites",
            "All 16 achievements with unlock rates",
            "EA patch log & roadmap, API-driven",
        ]),
        M(f"Data version: {MATERIALS_VERSION['version']} (captured {MATERIALS_VERSION['captured']}). Sources: official wiki (L0) + Steam API (L0)."),
    ],
}

HOME_KO = {
    "slug": "sandustry",
    "title": "샌더스트리 가이드 허브",
    "metaTitle": "샌더스트리 가이드: 재료, 시작 가이드, Steam Deck, 업적, 패치 로그",
    "metaDescription": "샌더스트리 가이드 허브: 전체 재료 속성, 시작 가이드, Steam Deck·macOS 가이드, 모바일 답변, 16개 업적, EA 패치 로그 — 한국어와 영어.",
    "intro": "샌더스트리는 Lantto Games가 개발하고 Hooded Horse가 퍼블리싱한 자동화·탐험·기지 건설 전략 게임입니다. 2026년 8월 13일 Steam, GOG, Microsoft Store, PC Game Pass에서 얼리 액세스로 출시되었습니다.",
    "sections": [
        N("이 허브에서 다루는 내용", [
            "시작 가이드 (한국어 + 영어)",
            f"전체 {len(MATERIALS)}개 재료의 밀도·유형·획득처·가공·물리 속성",
            "Steam Deck 및 macOS 가이드",
            "모바일 답변: 공식 모바일 버전 없음 — 가짜 APK 사이트 주의",
            "16개 업적과 달성률",
            "EA 패치 로그 및 로드맵 (API 기반)",
        ]),
        M(f"데이터 버전: {MATERIALS_VERSION['version']} ({MATERIALS_VERSION['captured']} 수집). 출처: 공식 위키 (L0) + Steam API (L0)."),
    ],
}

# ---------- Getting Started ----------
GETTING_STARTED_EN = {
    "slug": "sandustry/getting-started",
    "title": "Sandustry Getting Started",
    "metaTitle": "Sandustry Getting Started Guide: First Factory, Materials, Research",
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
    "metaTitle": "샌더스트리 시작 가이드: 첫 공장, 재료, 연구",
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
    "metaTitle": "All Sandustry Materials: Density, Sources, Processing, Physics",
    "metaDescription": "Every Sandustry material with density, matter type, source, processing and physics.",
    "intro": f"All {len(MATERIALS)} materials in Sandustry, with density, type, source, processing and physics from the official wiki.",
    "sections": [_materials_table(), M("Version: v0.5.4.")],
}

MATERIALS_KO = {
    "slug": "sandustry/materials",
    "title": "샌더스트리 전체 재료",
    "metaTitle": "샌더스트리 전체 재료: 밀도, 획득처, 가공, 물리",
    "metaDescription": "샌더스트리의 모든 재료: 밀도, 유형, 획득처, 가공, 물리 속성.",
    "intro": f"샌더스트리의 모든 재료 {len(MATERIALS)}종의 밀도, 유형, 획득처, 가공, 물리 속성 (공식 위키 출처).",
    "sections": [_materials_ko_table(), M("버전: v0.5.4.")],
}

# ---------- 差异化长尾 (en) ----------
STEAM_DECK_EN = {
    "slug": "sandustry/steam-deck",
    "title": "Sandustry on Steam Deck",
    "metaTitle": "Sandustry on Steam Deck: Settings, Performance & Controls",
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
    "metaTitle": "Sandustry on macOS: Native Support & Right-Click Bug",
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
    "metaTitle": "Is Sandustry on Mobile? No — Beware Fake APK Sites",
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
    "metaTitle": "All 16 Sandustry Achievements with Unlock Rates",
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
FAQ_KO = {
    "slug": "sandustry/faq",
    "title": "샌더스트리 FAQ",
    "metaTitle": "샌더스트리 FAQ: 한국어 지원, 모바일, 멀티플레이어",
    "metaDescription": "샌더스트리 자주 묻는 질문: 한국어 지원, 모바일 버전, 멀티플레이어.",
    "intro": "샌더스트리에 대한 자주 묻는 질문입니다.",
    "sections": [
        F([
            {"q": "샌더스트리는 한국어를 지원하나요?", "a": "네. 한국어(인터페이스+자막)를 공식 지원합니다."},
            {"q": "모바일 버전이 있나요?", "a": "없습니다. 가짜 APK 다운로드 사이트에 주의하세요. 공식 플랫폼은 Steam, GOG, Microsoft Store, PC Game Pass입니다."},
            {"q": "멀티플레이어가 있나요?", "a": "없습니다. 싱글 플레이어 게임입니다."},
            {"q": "금(Gold)은 어떻게 얻나요?", "a": "대부분의 가공 과정의 부산물로 얻습니다. 수집기(Collector)에 보관해야 은행에 집계됩니다."},
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
    """en=EN 页面 dict（含 slug/title/intro/sections）；i18n_map={lang: {title, intro, sections: {idx: ov}}}。
    返回 site.json pages 条目（含 i18n 字段）。"""
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
    }
    if page_i18n:
        p["i18n"] = page_i18n
    return p

def build_sandustry_pages():
    """返回 Sandustry 页面列表，供 build_content.py 追加到 d['pages']。"""
    reg = {
        "sandustry": (HOME_EN, {"ko": HOME_KO}),
        "sandustry/getting-started": (GETTING_STARTED_EN, {"ko": GETTING_STARTED_KO}),
        "sandustry/materials": (MATERIALS_EN, {"ko": MATERIALS_KO}),
        "sandustry/steam-deck": (STEAM_DECK_EN, {}),
        "sandustry/macos": (MACOS_EN, {}),
        "sandustry/mobile": (MOBILE_EN, {}),
        "sandustry/achievements": (ACHIEVEMENTS_EN, {}),
        "sandustry/faq": (FAQ_KO, {}),  # en fallback: None => FAQ 只有 ko
    }
    pages = []
    for slug, (en, i18n) in reg.items():
        if en is None and not i18n:
            continue
        if en is None:
            # FAQ ko-only：用 ko 结构 + i18n 空（ko 作为主语言由外层处理）
            pages.append({
                "slug": slug,
                "title": i18n["ko"]["title"],
                "metaTitle": i18n["ko"].get("metaTitle", ""),
                "metaDescription": i18n["ko"].get("metaDescription", ""),
                "intro": i18n["ko"].get("intro", ""),
                "sections": i18n["ko"]["sections"],
            })
            continue
        pages.append(_to_page(en, i18n))
    return pages
