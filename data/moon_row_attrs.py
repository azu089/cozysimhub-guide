#!/usr/bin/env python3
"""
Moonlight Peaks 表格行属性机械推导（供前端筛选器用）。

为什么单独一个模块：
  筛选器需要每行带 data-* 属性才能过滤，但**属性必须从已有单元格机械推导，不新增任何事实**（铁律 3）。
  推导逻辑集中在这里，配 --check 可打印全表人工核对——这是 Doloc 鱼图鉴踩过坑后定下的做法。

⚠️ 核心约束：**每个属性只从它自己那一列取值，绝不扫整行**。
  Doloc 的教训：扫全行时 `Rainbow Trout` 的 "Rain" 被当成「需雨天」。
  这里同样有雷：鱼名 `Moonflutter` 含 "Moon"、地点 `Moonlit Pines River` 也含 "Moon"，
  若扫整行，Violet / Goliath 会被误判成「满月限定」。所以 moon 只从 Condition 列取。

用法：
  python3 data/moon_row_attrs.py --check     # 打印推导全表，人工核对
  （构建时由 build_content.py 调用 apply_row_attrs(pages)）
"""
import re
import sys


# ---- 通用：带词边界的整词匹配（避免子串误命中） ----
def _has(text, *words):
    t = (text or "").lower()
    return any(re.search(r"(?<![a-z])" + re.escape(w) + r"(?![a-z])", t) for w in words)


UNVERIFIED = "待补"


# ============================ 鱼类表 ============================
# 列序：Fish | Rarity | Location | Condition | Rod | Energy | Value
FISH_HEADER0 = "Fish"

_RARITY = [
    ("superrare", ("super rare",)),
    ("rare", ("rare",)),
    ("uncommon", ("uncommon",)),
    ("common", ("common",)),
]

# 地点键 → 该列里出现的原文片段（全部来自 Location 列实际文本）
_LOCATIONS = [
    ("silverveil",   ("silverveil",)),
    ("moonlit-pines", ("moonlit pines",)),
    ("luna-bay",     ("luna bay",)),
    ("pink-grove",   ("pink grove",)),
    ("underground",  ("underground", "cave of echoes", "crystal")),
    ("howling-marshes", ("howling marshes",)),
    ("misty-shores", ("misty",)),
    ("farm",         ("farm",)),
    ("anywhere",     ("any fishing spot", "most water")),
]


def fish_attrs(row):
    """从鱼类表一行推导筛选属性。row = [Fish, Rarity, Location, Condition, Rod, Energy, Value]"""
    _, rarity_c, loc_c, cond_c, rod_c = row[0], row[1], row[2], row[3], row[4]

    # 稀有度 ← 仅 Rarity 列（顺序重要：super rare 要先于 rare）
    rarity = next((k for k, ws in _RARITY if _has(rarity_c, *ws)), "")
    if not rarity:
        rarity = "unlisted"

    # 地点 ← 仅 Location 列（可多值）
    # ⚠️ 必须处理否定式：Whisper 的原文是「Most water (not Silverveil Lake)」，
    #    直接子串匹配会把它错标成 silverveil（人工核对时抓到的真实错误）。
    #    做法：先把 "not X" / "except X" 的括号段摘出来当排除名单，再在剩余文本里匹配。
    loc_raw = (loc_c or "").lower()
    excluded = " ".join(re.findall(r"(?:not|except|excluding)\s+([^)\],;]+)", loc_raw))
    loc_pos = re.sub(r"(?:not|except|excluding)\s+[^)\],;]+", " ", loc_raw)
    locs = [k for k, ws in _LOCATIONS
            if any(w in loc_pos for w in ws) and not any(w in excluded for w in ws)]
    if not locs:
        locs = ["unlisted"]

    # 以下全部 ← 仅 Condition 列
    cond = (cond_c or "").lower()
    season = []
    if _has(cond, "spring"):
        season.append("spring")
    if _has(cond, "summer"):
        season.append("summer")
    if _has(cond, "autumn", "fall"):
        season.append("autumn")
    if _has(cond, "winter"):
        season.append("winter")
    if "all seasons" in cond:
        season = ["allseason"]
    if not season:
        season = ["unlisted"]

    weather = "rain" if _has(cond, "rain") else ("anyweather" if "any weather" in cond else "unlisted")
    if "any time" in cond:
        time_ = "anytime"
    elif _has(cond, "evening", "night"):
        time_ = "evening"
    elif _has(cond, "morning", "day"):
        time_ = "day"
    else:
        time_ = "unlisted"
    moon = "fullmoon" if "full moon" in cond else ("bloodmoon" if "blood moon" in cond else "")
    size = "large" if "large fish" in cond else ""

    # 竿 ← 仅 Rod 列
    if _has(rod_c, "premium"):
        rod = "premium"
    elif "any rod" in (rod_c or "").lower():
        rod = "anyrod"
    else:
        rod = "unlisted"

    # 「待补」占位行单独可筛出（沿用 Doloc 基因表的 unlisted 处理）
    pending = UNVERIFIED in "".join(row)

    return {
        "rarity": rarity,
        "loc": " ".join(locs),
        "season": " ".join(season),
        "weather": weather,
        "time": time_,
        "moon": moon,
        "size": size,
        "rod": rod,
        "pending": "pending" if pending else "",
    }


# ============================ 礼物表 ============================
# 列序：Character | Loved Gifts | Liked Gifts | Disliked Gifts
GIFT_HEADER0 = "Character"


def gift_attrs(row):
    """礼物表不做任何品类归类（那会引入判断），只标注每列是否有数据，供「只看有数据的行」用。"""
    loved, liked, disliked = (row[1] or ""), (row[2] or ""), (row[3] or "")
    has = []
    if loved.strip() and UNVERIFIED not in loved:
        has.append("hasloved")
    if liked.strip() and UNVERIFIED not in liked:
        has.append("hasliked")
    if disliked.strip() and UNVERIFIED not in disliked:
        has.append("hasdisliked")
    return {"has": " ".join(has) or "unlisted"}


# ============================ 应用 ============================
# slug → (识别用表头首列, 推导函数, 筛选器类型)
TABLE_SPECS = {
    "moonlight-peaks/fishing": (FISH_HEADER0, fish_attrs, "fish"),
    "moonlight-peaks/gifts": (GIFT_HEADER0, gift_attrs, "gift"),
}


def _apply_to_sections(sections, header0, fn, kind):
    """给匹配的 table section 挂 rowAttrs + filterKind；表格的 headers/rows 一个字都不改。"""
    hit = 0
    for s in sections or []:
        if s.get("type") != "table":
            continue
        rows = s.get("rows") or []
        if not rows or len(rows[0]) < 4:
            continue
        # 用**基准列数 + 首行形态**识别目标表：i18n 版本表头被翻译了，不能靠表头文字认
        if len(rows[0]) != (7 if kind == "fish" else 4):
            continue
        s["rowAttrs"] = [fn(r) for r in rows]
        s["filterKind"] = kind
        hit += 1
    return hit


def apply_row_attrs(pages):
    """就地给 pages（含各语言 i18n.sections）挂 rowAttrs。幂等。"""
    total = 0
    for p in pages:
        spec = TABLE_SPECS.get(p.get("slug"))
        if not spec:
            continue
        header0, fn, kind = spec
        total += _apply_to_sections(p.get("sections"), header0, fn, kind)
        for _lang, t in (p.get("i18n") or {}).items():
            total += _apply_to_sections(t.get("sections"), header0, fn, kind)
    return total


# ============================ 人工核对 ============================
def _check():
    import json
    import os
    here = os.path.dirname(os.path.abspath(__file__))
    d = json.load(open(os.path.join(here, "site.json"), encoding="utf-8"))
    pages = {p["slug"]: p for p in d["pages"]}

    for slug, (header0, fn, kind) in TABLE_SPECS.items():
        p = pages.get(slug)
        if not p:
            print(f"!! 找不到 {slug}")
            continue
        for s in p["sections"]:
            if s.get("type") != "table":
                continue
            rows = s.get("rows") or []
            if not rows or len(rows[0]) != (7 if kind == "fish" else 4):
                continue
            print(f"\n{'='*100}\n{slug}  —— {len(rows)} 行，逐行核对推导结果\n{'='*100}")
            for r in rows:
                a = fn(r)
                print(f"{r[0][:22]:24} {json.dumps(a, ensure_ascii=False)}")
                print(f"{'':24} 源: " + " | ".join(c[:34] for c in r[1:5]))
            break


if __name__ == "__main__":
    if "--check" in sys.argv:
        _check()
    else:
        print(__doc__)
