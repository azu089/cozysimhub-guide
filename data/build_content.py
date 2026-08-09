# -*- coding: utf-8 -*-
"""Sovereign Tower Guide Hub — site.json 重建（幂等）。
en 为默认语言（数据层），zh-CN 为中文翻译；i18n 框架含 ja/ko/fr/de（正文翻译后续批次）。
数据源：data/content_data.py（L0：raiderking 全页 + 知识库 + Steam 官方）。
"""
import json, copy
from pathlib import Path
from content_data import (
    KNIGHT_NAMES, KNIGHTS, KNIGHTS_BASIC, RECIPES, QUEST_TYPES, QUEST_CONDITIONS,
    SOVEREIGN_TAGS, XP_TABLE, SCORE_THRESHOLDS, FACTIONS,
)

ROOT = Path(__file__).parent
d = json.loads((ROOT / "site.base.json").read_text(encoding="utf8"))

def table(headers, rows):
    return {"type": "table", "tag": "DATA", "heading": "", "body": "", "headers": headers, "rows": rows}

def steps(heading, items, tag="STEP"):
    return {"type": "steps", "tag": tag, "heading": heading, "body": "", "items": items}

def notes(heading, items):
    return {"type": "list", "tag": "NOTE", "heading": heading, "body": "", "items": items}

def faq_block(items):
    return {"type": "faq", "tag": "FAQ", "heading": "FAQ", "body": "", "items": items}

# ---------- 页面：how-to-play ----------
def build_how_to_play():
    en = {
        "slug": "sovereign-tower/how-to-play",
        "title": "How to Play Sovereign Tower",
        "metaTitle": "How to Play Sovereign Tower: Core Loop, Systems & Beginner Tips",
        "metaDescription": "New to Sovereign Tower? Learn the court-audience → Round Table → quest result loop, the five factions, time rewind, annex building and the quest score formula.",
        "intro": "Sovereign Tower is a story-rich Round Table management RPG: you rule a magical tower, recruit eccentric knights, assign quests and balance five factions — and when fate turns against you, you turn back time and rewrite it.",
        "sections": [
            steps("The Five-Step Core Loop", [
                ["Morning court", "Each cycle starts with an audience. Citizens bring requests — from gardening to demon hunting. How you answer shapes faction satisfaction and knight opinions."],
                ["Assign the Round Table", "Send knights on quests. Match knight stats to quest requirements to push the outcome toward success (see the score formula below)."],
                ["Read the outcome", "Quests return Critical Success / Success / Failure / Unexpected Outcome. Great and critical successes multiply rewards."],
                ["Turn back time", "If a cycle went badly, the Demon in the cellar lets you rewind time and re-roll your decisions. Rewind is the game's core safety net."],
                ["Expand the Tower", "Build Annexes (Carina's Forge, Witch's Alchemy Room) and upgrade to unlock more knights, tools and story."],
            ]),
            table(["Resource", "What it does"], [
                ["Treasury", "Gold for summons, gear and construction. Quest rewards and faction choices feed it."],
                ["Merchants / Mystics / Scholars / Nobles / People", "Five faction meters. Balance them, or spend them all and betray everyone — the game lets you."],
                ["Round Table capacity", "Grows with the story: Act 1 = 6 knights, Act 2 = 8, Act 3 = 10."],
                ["Annexes", "Buildings that add systems: the Forge repairs/crafts gear, the Alchemy Room makes consumables."],
            ]),
            notes("Beginner mistakes to avoid", [
                "Assigning knights to quests they hate: disliked quest types drain affinity (−0.75 each), and at −7 affinity a knight resigns.",
                "Ignoring faction balance: a faction at zero satisfaction can trigger crisis events.",
                "Forgetting the score formula: send a knight whose stats beat the quest requirements, not just any available knight.",
                "Missing the 48-hour early window: recruit story knights (Dulahan, Arron, Brunhilda) by progressing their specific storylines.",
            ]),
            faq_block([
                ["Do I need to worry about time limits?", "No — Sovereign Tower is playable without timed input (official Steam feature). You can rewind to re-roll decisions, so nothing is permanently lost."],
                ["Can knights die permanently?", "Most knights can die on quests and stay dead that run. Ursula is Immortal (re-recruitable after death); Alwena and Ari never resign."],
                ["What are the five faction meters?", "Merchants, Mystics, Scholars, Nobles and People. Quests and court decisions move them; some knights gain or lose affinity based on how you balance them."],
            ]),
        ],
        "i18n": {"zh-CN": {
            "title": "君王之塔 入门攻略",
            "metaTitle": "君王之塔 怎么玩：核心循环、系统与新手技巧",
            "metaDescription": "君王之塔 Sovereign Tower 新手入门：早朝→圆桌→任务结果→时间回溯→扩建高塔的五步循环、五大派系、任务得分公式与新手常见错误。",
            "intro": "《君王之塔》是一款剧情丰富的圆桌管理 RPG：你统治一座魔法高塔，招募性格各异的骑士、分配任务、平衡五大派系——命运不顺就回溯时间，改写结局。",
            "sections": [
                steps("五步核心循环", [
                    ["早朝听政", "每个 cycle 从早朝开始，臣民带来诉求——从园艺到驱魔。你的回答方式影响派系满意度与骑士看法。"],
                    ["分配圆桌任务", "派骑士执行任务。把骑士属性匹配到任务需求，才能把结果推向成功（见下方得分公式）。"],
                    ["查看任务结果", "任务回报分为 Critical Success / Success / Failure / Unexpected Outcome。Great 和 Critical 成功会翻倍奖励。"],
                    ["时间回溯", "如果这一 cycle 搞砸了，地窖里的恶魔让你回溯时间重新决策。回溯是游戏的核心安全网。"],
                    ["扩建高塔", "建造 Annexes（Carina's Forge 锻炉、Witch's Alchemy Room 炼金室）并升级，解锁更多骑士、工具与剧情。"],
                ]),
                table(["资源", "作用"], [
                    ["国库 Treasury", "金币用于召唤、装备与建造。任务奖励和派系选择会补充它。"],
                    ["商人 / 秘术师 / 学者 / 贵族 / 平民", "五大派系好感条。可以平衡它们，也可以全花光然后背刺所有人——游戏允许。"],
                    ["圆桌容量", "随剧情增长：Act 1 = 6 骑士，Act 2 = 8，Act 3 = 10。"],
                    ["Annexes 附属建筑", "新增系统的建筑：锻炉修理/制作装备，炼金室制作消耗品。"],
                ]),
                notes("新手常见错误", [
                    "派骑士去做他们讨厌的任务：厌恶的任务类型会掉好感（每个 −0.75），好感降到 −7 骑士会辞职。",
                    "忽视派系平衡：某个派系满意度归零可能触发危机事件。",
                    "忘记得分公式：要派属性压过任务需求的骑士，而不是随便派一个空闲的人。",
                    "错过 48 小时早期窗口：剧情骑士（Dulahan、Arron、Brunhilda）要靠推进特定剧情线才能招募。",
                ]),
                faq_block([
                    ["有时间限制吗？", "没有——君王之塔官方特性是「无需限时输入」。你可以随时回溯重新决策，不会永久损失。"],
                    ["骑士会永久死亡吗？", "多数骑士会在任务中死亡并在本次周目保持死亡。Ursula 是 Immortal（死后可再招募）；Alwena 和 Ari 永不辞职。"],
                    ["五大派系是什么？", "商人、秘术师、学者、贵族、平民。任务和朝政决策会影响它们；部分骑士会根据你的派系平衡获得或失去好感。"],
                ]),
            ],
        }},
    }
    return en

# ---------- 页面：quest-mechanics ----------
def build_quest_mechanics():
    en = {
        "slug": "sovereign-tower/quest-mechanics",
        "title": "Quest Mechanics & Score Formula",
        "metaTitle": "Sovereign Tower Quest Mechanics: Score Formula, Thresholds, XP & Affinity",
        "metaDescription": "How quest scoring works in Sovereign Tower: the (stat − requirement) × 0.66 formula, success thresholds, XP table, affinity, quest types and conditions.",
        "intro": "Every quest in Sovereign Tower asks for one or more stats. Matching the right knight to the right quest is the difference between a critical success and a total wipe — here is exactly how the maths works.",
        "sections": [
            table(["Mechanic", "Rule"], [
                ["Stat contribution", "For each required stat: roughly (knight stat − quest requirement) × 0.66, divided across the party, scaled by how demanding the requirement is. Exactly matching gives a small +0.22 base."],
                ["Stat clamp", "The stat value used in scoring is always clamped to 0–15, including equipment bonuses."],
                ["Affinity effect", "Liked quest type/condition: +1.33 affinity each. Disliked: −0.75 each. They stack — a quest of the right type with two liked conditions is worth close to +4 affinity."],
                ["Meal bonus", "Feeding a knight a favourite meal: +1.5 affinity and +0.5 quest score, permanently recording their taste."],
            ]),
            table(["Score", "Threshold", "Reward"], SCORE_THRESHOLDS),
            table(["Level", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"],
                  [["Total XP", *[str(x) for x in XP_TABLE]]]),
            notes("Where XP comes from", [
                "Quest outcomes: failure = 0, bare success = 1×, great success = 1.5×, critical success = 2×.",
                "Sending a knight to the Training Ground for a cycle instead of a quest.",
                "Each level-up lets you spend one point in any stat that isn't already 15.",
            ]),
            table(["Quest type", ""], [[t, "One of the 11 quest archetypes"] for t in QUEST_TYPES]),
            table(["Quest condition", ""], [[c, "A modifier that adds score requirements or changes outcomes"] for c in QUEST_CONDITIONS]),
            notes("Sovereign archetypes", [f"{t}: some knights approve or disapprove of your ruling style; decisions in audiences apply these tags." for t in SOVEREIGN_TAGS]),
            faq_block([
                ["What score do I need for a critical success?", "+10 or higher. +5 is a great success (1.5× rewards), 0 is a bare success, −5 is a major failure and −10 is a critical failure."],
                ["Can affinity drop so far a knight leaves?", "Yes — at −7 affinity most knights queue a resignation audience and walk out. Alwena and Ari have a −1500 threshold: they never resign."],
                ["How many quest types are there?", "11 types and 21 conditions, per the fan wiki data. A quest can combine a type with several conditions."],
            ]),
        ],
        "i18n": {"zh-CN": {
            "title": "任务机制与得分公式",
            "metaTitle": "君王之塔 任务机制：得分公式、阈值、经验与好感",
            "metaDescription": "君王之塔任务得分怎么算：(骑士属性 − 任务需求) × 0.66、成功阈值、经验表、好感机制、11 种任务类型与 21 种任务条件。",
            "intro": "君王之塔的每个任务都会要求一种或多种属性。把正确的骑士派到正确的任务，是「Critical Success」和「全军覆没」的区别——这里给出精确的数学。",
            "sections": [
                table(["机制", "规则"], [
                    ["属性贡献", "每个需求属性约等于：(骑士属性 − 任务需求) × 0.66，按队伍分摊，再按需求难度缩放。刚好匹配给 +0.22 基础正值。"],
                    ["属性钳制", "参与得分的属性值永远钳制在 0–15（含装备加成）。"],
                    ["好感影响", "喜欢的任务类型/条件：每个 +1.33 好感；厌恶的：每个 −0.75。可叠加——类型对且带两个喜欢条件的任务价值接近 +4 好感。"],
                    ["喂菜加成", "喂骑士最爱菜：+1.5 好感 +0.5 任务分，并永久记录口味。"],
                ]),
                table(["得分", "阈值", "奖励"], [["Critical Success", "+10", "奖励 ×2"], ["Great Success", "+5", "奖励 ×1.5"], ["Success", "0", "奖励 ×1"], ["Major Failure", "−5", "无奖励"], ["Critical Failure", "−10", "无奖励"]]),
                table(["等级", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"],
                      [["累计经验", *[str(x) for x in XP_TABLE]]]),
                notes("经验来源", [
                    "任务结果：失败 = 0，普通成功 = 1×，Great = 1.5×，Critical = 2×。",
                    "把一个 cycle 用于训练场（Training Ground）而不是任务。",
                    "每升一级可在任意未满 15 的属性上投入 1 点。",
                ]),
                table(["任务类型", ""], [[t, "11 种任务原型之一"] for t in QUEST_TYPES]),
                table(["任务条件", ""], [[c, "增加得分要求或改变结果的修饰项"] for c in QUEST_CONDITIONS]),
                notes("君主标签", [f"{t}：部分骑士会认可或反感你的统治风格；朝政决策会应用这些标签。" for t in SOVEREIGN_TAGS]),
                faq_block([
                    ["多少分算 Critical Success？", "+10 及以上。+5 = Great Success（奖励 ×1.5），0 = 普通成功，−5 = Major Failure，−10 = Critical Failure。"],
                    ["好感太低骑士会离开吗？", "会——好感降到 −7，多数骑士会排队递交辞呈并离开。Alwena 和 Ari 阈值 −1500：永不辞职。"],
                    ["共有多少种任务类型？", "11 种类型 + 21 种条件（依据粉丝 wiki 数据）。一个任务可以组合类型与多个条件。"],
                ]),
            ],
        }},
    }
    return en

# ---------- 页面：knights（核心 P0）----------
def _knight_stats_str(k):
    if k.get("stats") is None:
        return "随机（Chester 每次判定重 roll 0–15）" if k["name"] == "Chester" else "待补"
    return " / ".join(str(x) for x in k["stats"])

def _knight_row(k):
    return [k["name"], k.get("origin") or "待补", str(k.get("level") or "待补"), str(k.get("armor") or "待补"),
            _knight_stats_str(k), "，".join(k.get("meals") or ["待补"]), k.get("note") or ""]

def build_knights():
    rows = [_knight_row(k) for k in KNIGHTS]
    for name, b in KNIGHTS_BASIC.items():
        rows.append([name, b.get("origin") or "待补", str(b.get("level") or "待补"), str(b.get("armor") or "待补"),
                     _knight_stats_str({"name": name, "stats": b.get("stats")}),
                     "，".join(b.get("meals") or ["待补"]), b.get("note") or ""])
    en = {
        "slug": "sovereign-tower/knights",
        "title": "All Knights, Stats & Traits",
        "metaTitle": "Sovereign Tower All 24 Knights: Stats, Hidden Traits, Favorite Meals & Recruit",
        "metaDescription": "Every Sovereign Tower knight: the full 24-knight roster with six stats, known and hidden traits, favorite meals, recruit conditions and quest preferences.",
        "intro": "All 24 knights in Sovereign Tower are recruitable. Every knight has six stats (STR/AGI/CHA/MAG/WIT/LCK, all 0–15), a set of known traits, hidden traits that are active from day one, favorite meals and quest preferences. This is the complete roster.",
        "sections": [
            table(["Knight", "Origin", "Lv", "Armor", "Stats (STR/AGI/CHA/MAG/WIT/LCK)", "Favorite meals", "Notes"], rows),
            notes("How to read a knight", [
                "Stats are on a 0–15 scale. Level 1–15; each level-up adds one point to any stat below 15.",
                "Known traits are visible the moment you recruit. Hidden traits are fully active in the maths from day one but invisible until revealed via conversations, quest outcomes or story events.",
                "† marks traits Alwena can reveal as Intendant rumours — one at a time, only ones you don't already know.",
                "Likes give +1.33 affinity per assignment; dislikes −0.75. Feeding a favourite meal gives +1.5 affinity and +0.5 quest score.",
            ]),
            faq_block([
                ["Which knight has the highest stats?", "Daguez starts with 15 Strength; Edith and Epicrate have 12 in their best stat (MAG and WIT). Chester has completely random stats, rerolled every check."],
                ["Which knights never resign?", "Alwena and Ari have a resignation threshold of −1500 — they never leave. Everyone else walks at −7 affinity."],
                ["How do I unlock hidden traits?", "Mostly through free-time conversations, quest outcomes and story events. Alwena's Intendant rumours reveal specific hidden traits one at a time."],
            ]),
        ],
        "i18n": {"zh-CN": {
            "title": "全部 24 位骑士：属性与特质",
            "metaTitle": "君王之塔 全部 24 位骑士：六维属性、隐藏特质、最爱菜与招募条件",
            "metaDescription": "君王之塔全部 24 位骑士：六维属性（STR/AGI/CHA/MAG/WIT/LCK）、已知与隐藏特质、最爱菜、招募条件与任务偏好完整清单。",
            "intro": "君王之塔的 24 位骑士全部可以招募。每位骑士有六维属性（STR/AGI/CHA/MAG/WIT/LCK，全 0–15）、一组已知特质、从第一天就生效的隐藏特质、最爱菜与任务偏好。这是完整名单。",
            "sections": [
                table(["骑士", "出身", "等级", "护甲", "六维 (STR/AGI/CHA/MAG/WIT/LCK)", "最爱菜", "备注"], rows),
                notes("如何读骑士档案", [
                    "属性 0–15；等级 1–15，每升一级可在任意未满 15 的属性上投 1 点。",
                    "已知特质在招募瞬间可见。隐藏特质从第一天就在数值里生效，但需要通过对话、任务结果或剧情事件解锁显示。",
                    "† 标记 = Alwena 可以挖出的 Intendant 流言——一次一个，且只挖你还不知道的。",
                    "喜欢的任务每次派任 +1.33 好感；厌恶的 −0.75。喂最爱菜 +1.5 好感 +0.5 任务分。",
                ]),
                faq_block([
                    ["哪个骑士属性最高？", "Daguez 起始力量 15；Edith 和 Epicrate 在各自最强项（MAG 12 / WIT 12）。Chester 属性完全随机，每次判定重 roll。"],
                    ["哪些骑士永不辞职？", "Alwena 和 Ari 的辞职阈值是 −1500——永不离开。其他人在好感 −7 时离开。"],
                    ["怎么解锁隐藏特质？", "主要通过空闲对话、任务结果和剧情事件。Alwena 的 Intendant 流言能逐个揭示特定隐藏特质。"],
                ]),
            ],
        }},
    }
    return en

# ---------- 页面：secret-knights ----------
def build_secret_knights():
    en = {
        "slug": "sovereign-tower/secret-knights",
        "title": "Secret Knights & How to Recruit Them",
        "metaTitle": "Sovereign Tower Secret Knights: Dulahan, Chester, Alwena & Special Recruit Conditions",
        "metaDescription": "How to recruit Sovereign Tower's special knights: Dulahan (after Goberto dies), Chester (goose quest), Alwena (emergency), Ari, Arron and Brunhilda.",
        "intro": "Several knights in Sovereign Tower don't join through a normal candidacy audience. Their recruit conditions are tied to specific storylines, deaths or emergency events — miss the window and you lose them that run.",
        "sections": [
            table(["Knight", "Recruit condition", "Window"], [
                ["Dulahan", "Complete Goberto's death path — Dulahan appears as the demon knight from day 4 of that route.", "Story-gated; one per run"],
                ["Chester", "Finish any Clean Keeper Goose Part 2 special outcome (cheese, a horse or Gwendan; each pays 1 gold). Chester is the real prize.", "Goose quest line"],
                ["Alwena", "One-time emergency: open the Round Table with zero available knights in Act 2 or later. Cannot be triggered on demand; no second chance.", "Act 2+ emergency only"],
                ["Ari", "Summon him for 25 gold as the younger brother of the Basalt brothers.", "Always available once story permits"],
                ["Arron", "Arrives through the Drakovic storyline (no candidacy audience).", "Story-gated"],
                ["Brunhilda", "Gavault storyline, daughter's side branch.", "Story-gated"],
            ]),
            notes("Why these matter", [
                "Dulahan is the only demon knight: Intangible (half damage), plus the full 6-dish favourite list — a superb quest engine if you can keep Goberto alive through his death path.",
                "Alwena reveals other knights' rumoured traits — losing her means losing that intelligence tool for the whole run.",
                "Chester's random stats make him a wildcard: never rely on him for a must-succeed quest, but he never minds what you assign.",
            ]),
            faq_block([
                ["Can I recruit Dulahan without killing Goberto?", "Per the fan wiki data, Dulahan appears specifically on Goberto's death path. There is no confirmed alternative recruit route yet (待补 if unverified)."],
                ["Is Alwena missable?", "Yes — the emergency offer happens only when the Round Table has zero available knights in Act 2 or later, once. If you never hit that state, you never get her."],
                ["Are there other secret knights?", "The Bard / Hildegard appears in the fan wiki as a secret knight; exact recruit steps are still being verified."],
            ]),
        ],
        "i18n": {"zh-CN": {
            "title": "隐藏骑士与招募方法",
            "metaTitle": "君王之塔 隐藏骑士招募：Dulahan、Chester、Alwena 与特殊条件",
            "metaDescription": "君王之塔特殊骑士招募方法：Dulahan（Goberto 死后）、Chester（鹅任务）、Alwena（紧急事件）、Ari、Arron、Brunhilda。",
            "intro": "君王之塔中有几位骑士不通过普通候选朝会加入。他们的招募条件绑定特定剧情、死亡事件或紧急事件——错过窗口，本周目就再也拿不到。",
            "sections": [
                table(["骑士", "招募条件", "窗口"], [
                    ["Dulahan", "完成 Goberto 的死亡路线——Dulahan 会作为恶魔骑士在该路线第 4 天出现。", "剧情限定；每周目一次"],
                    ["Chester", "完成任意 Clean Keeper Goose Part 2 特殊结局（奶酪/马/Gwendan 三选一，各付 1 金币）。Chester 才是真正的奖品。", "鹅任务线"],
                    ["Alwena", "一次性紧急事件：Act 2 之后圆桌可用骑士为 0 时触发。无法主动触发，没有第二次机会。", "仅 Act 2+ 紧急状态"],
                    ["Ari", "花 25 金币召唤（Basalt 兄弟的弟弟）。", "剧情解锁后随时"],
                    ["Arron", "通过 Drakovic 剧情线加入（无候选朝会）。", "剧情限定"],
                    ["Brunhilda", "Gavault 剧情女儿侧分支。", "剧情限定"],
                ]),
                notes("为什么重要", [
                    "Dulahan 是唯一的恶魔骑士：Intangible（受伤减半）+ 全 6 种最爱菜——只要能走完 Goberto 死亡路线，他就是顶级任务引擎。",
                    "Alwena 能挖出其他骑士的流言特质——失去她就等于失去整局的侦查工具。",
                    "Chester 随机属性 = 万能补位：必成任务别靠他，但他从不介意你派什么。",
                ]),
                faq_block([
                    ["不杀 Goberto 能招 Dulahan 吗？", "依据粉丝 wiki 数据，Dulahan 只在 Goberto 死亡路线出现。目前没有确认的替代招募路线（未核实则标待补）。"],
                    ["Alwena 会错过吗？", "会——紧急招募只在 Act 2+ 圆桌可用骑士为 0 时触发一次。如果从不进入该状态，就永远拿不到她。"],
                    ["还有别的隐藏骑士吗？", "The Bard / Hildegard 出现在粉丝 wiki 的隐藏骑士列表；具体招募步骤仍在核实中。"],
                ]),
            ],
        }},
    }
    return en

# ---------- 页面：recipes ----------
def build_recipes():
    rows = [[r["en"], r["zh"], r["desc_zh"]] for r in RECIPES]
    fav_rows = []
    for k in KNIGHTS:
        fav_rows.append([k["name"], "、".join(k.get("meals") or ["待补"])])
    for name, b in KNIGHTS_BASIC.items():
        fav_rows.append([name, "、".join(b.get("meals") or ["待补"])])
    en = {
        "slug": "sovereign-tower/recipes",
        "title": "All Recipes & Each Knight's Favorite Meal",
        "metaTitle": "Sovereign Tower All 6 Recipes & Knight Favorite Meals (+1.5 Affinity Guide)",
        "metaDescription": "All six Sovereign Tower dishes and which knight loves each meal. Feeding a favourite meal gives +1.5 affinity and +0.5 quest score.",
        "intro": "There are exactly six dishes in Sovereign Tower. Feeding a knight a favourite meal gives +1.5 affinity and +0.5 quest score, and permanently records their taste — so the meal table is worth learning by heart.",
        "sections": [
            table(["Dish (EN)", "Dish (中文)", "Description"], rows),
            table(["Knight", "Favorite meals"], fav_rows),
            notes("Feeding rules", [
                "Each knight has 1–2 favourite dishes (Chester and Dulahan love all six).",
                "A liked meal = +1.5 affinity and +0.5 quest score, permanently recorded.",
                "Feeding happens during free time — affinity gates these conversations, so keep liked assignments coming.",
            ]),
            faq_block([
                ["Which knights love every dish?", "Chester and Dulahan have all six dishes as favourites."],
                ["Does feeding affect quest score?", "Yes — +0.5 quest score per liked meal, on top of the +1.5 affinity."],
                ["Can a knight change favourite meals?", "Arron's violent evolution path changes his liked meals and resignation scene; other knights' tastes are fixed."],
            ]),
        ],
        "i18n": {"zh-CN": {
            "title": "全部菜谱与骑士最爱菜",
            "metaTitle": "君王之塔 全部 6 种菜谱与骑士最爱菜（+1.5 好感攻略）",
            "metaDescription": "君王之塔全部 6 种菜 + 每位骑士最爱菜对照。喂对最爱菜 +1.5 好感 +0.5 任务分。",
            "intro": "君王之塔一共只有 6 种菜。喂骑士最爱菜 +1.5 好感 +0.5 任务分，并永久记录口味——所以这张菜谱表值得记牢。",
            "sections": [
                table(["菜（英文）", "菜（中文）", "描述"], rows),
                table(["骑士", "最爱菜"], fav_rows),
                notes("喂菜规则", [
                    "每位骑士有 1–2 个最爱菜（Chester 和 Dulahan 全 6 种都爱）。",
                    "喂对 = +1.5 好感 +0.5 任务分，永久记录。",
                    "喂菜发生在空闲时间——好感决定能否进入这些对话，所以要持续派他们喜欢的任务。",
                ]),
                faq_block([
                    ["哪些骑士爱所有菜？", "Chester 和 Dulahan 的 6 种菜全是最爱。"],
                    ["喂菜影响任务分吗？", "会——每个最爱菜 +0.5 任务分（在 +1.5 好感之外）。"],
                    ["骑士会改变最爱菜吗？", "Arron 的暴力进化路线会改变他的最爱菜和辞职场景；其他骑士口味固定。"],
                ]),
            ],
        }},
    }
    return en

# ---------- 页面：romance ----------
def build_romance():
    en = {
        "slug": "sovereign-tower/romance",
        "title": "Romance Guide & Hidden Conditions",
        "metaTitle": "Sovereign Tower Romance Guide: Hidden Conditions, Lady of the Tower & Arthur",
        "metaDescription": "Sovereign Tower romance guide: hidden conditions, the Lady of the Tower stone statue line, Angelica's route, the Arthur marriage ending and how affinity gates romance.",
        "intro": "Romance in Sovereign Tower is gated by affinity, free-time conversations and specific story choices — and several routes have hidden conditions the game never tells you about.",
        "sections": [
            notes("How romance works", [
                "Affinity gates free-time conversations, which is how you unlock most of a knight's story — including romance scenes.",
                "Assign liked quests (+1.33 each), feed favourite meals (+1.5) and match the knight's liked sovereign archetype to raise affinity safely.",
                "Romance options appear in dialogue once a knight's story has progressed far enough; pushing affinity without story progress stalls the route."]),
            table(["Route", "Known conditions", "Status"], [
                ["Lady of the Tower (stone statue)", "Official selling point — a romanceable stone statue linked to the tower's secrets.", "Verified concept (Steam L0); full steps 待补"],
                ["Angelica", "Opening-story recruit; Kind-Hearted route, likes Kind sovereign style.", "Route confirmed; hidden steps 待补"],
                ["Arthur (marriage ending)", "Community videos show a marriage ending with Arthur.", "Exists (Bilibili L0); exact conditions 待补"],
                ["Gideon / others", "Steam community threads ask about 'how to romance the werewolf knight' and secret conditions.", "Community-reported; 待补"],
            ]),
            faq_block([
                ["Why isn't my romance progressing?", "The most common cause is stalled affinity or story. Check the knight's affinity isn't stuck, keep liked assignments coming and advance their story via free-time conversations."],
                ["Can I romance multiple knights?", "Community reports differ per route; some routes appear mutually exclusive (待补 until verified in-game)."],
                ["Does the Arthur marriage ending require specific faction balance?", "Community videos exist but exact prerequisites are unverified — treat as 待补."],
            ]),
        ],
        "i18n": {"zh-CN": {
            "title": "恋爱攻略与隐藏条件",
            "metaTitle": "君王之塔 恋爱攻略：隐藏条件、高塔石像线、Angelica 与亚瑟王",
            "metaDescription": "君王之塔恋爱攻略：好感如何解锁恋爱、高塔石像 Lady of the Tower 浪漫线、Angelica 路线、亚瑟王联姻结局与隐藏条件。",
            "intro": "君王之塔的恋爱由好感、空闲对话和特定剧情选择共同解锁——而且好几条路线存在游戏从不明说的隐藏条件。",
            "sections": [
                notes("恋爱怎么运作", [
                    "好感决定能否进入空闲对话，而空闲对话是解锁骑士故事（包括恋爱场景）的主要方式。",
                    "派喜欢的任务（每个 +1.33）、喂最爱菜（+1.5）、匹配骑士喜欢的君主风格，才能安全拉高好感。",
                    "骑士故事推进足够后，对话中才会出现恋爱选项；好感够但剧情没推进，路线会卡住。"]),
                table(["路线", "已知条件", "状态"], [
                    ["高塔石像 Lady of the Tower", "官方卖点——一尊与高塔秘密相关的可恋爱石像。", "概念已确认（Steam L0）；完整步骤待补"],
                    ["Angelica", "开场剧情招募；Kind-Hearted 路线，喜欢 Kind 君主风格。", "路线确认；隐藏步骤待补"],
                    ["亚瑟王（联姻结局）", "社区视频展示与亚瑟王联姻的结局。", "存在（B站 L0）；确切条件待补"],
                    ["Gideon / 其他人", "Steam 社区高频问「狼人骑士怎么恋爱」与隐藏条件。", "社区报告；待补"],
                ]),
                faq_block([
                    ["为什么我的恋爱不推进？", "最常见原因是好感或剧情卡住。检查骑士好感是否停滞，持续派喜欢的任务，并通过空闲对话推进他们的故事。"],
                    ["能同时攻略多个人吗？", "社区报告显示不同路线行为不同；部分路线似乎互斥（游戏内核实前标待补）。"],
                    ["亚瑟王联姻结局需要特定派系平衡吗？", "社区视频存在，但确切前置未核实——标待补。"],
                ]),
            ],
        }},
    }
    return en

# ---------- 页面：endings ----------
def build_endings():
    en = {
        "slug": "sovereign-tower/endings",
        "title": "All Endings & Hidden Ending",
        "metaTitle": "Sovereign Tower All Endings: Conquest, King Slayer, Hidden & Alt Endings",
        "metaDescription": "Sovereign Tower endings guide: conquest ending, King Slayer resolution, hidden/alt endings, and the branching structure that decides your fate.",
        "intro": "Sovereign Tower is a branching game with multiple endings. Some are simple route outcomes; others are hidden behind specific decisions, faction balances or romance lines.",
        "sections": [
            table(["Ending / route", "What's known", "Status"], [
                ["Conquest ending (一周目征服结局)", "Community Bilibili video shows a first-run conquest ending.", "Exists (L0 video); conditions 待补"],
                ["King Slayer resolution", "A resolution path involving the King Slayer, covered by fan sites.", "Covered by whisperofthehouse (L0); steps 待补"],
                ["Hidden / alt ending", "Steam community: 'How to get the secret alt ending' (7 replies).", "Community-reported; steps 待补"],
                ["Arthur marriage ending", "Marriage ending with Arthur shown in community videos.", "Exists (L0); conditions 待补"],
                ["Gwendan murder route", "The Act 2 murder investigation affects who lives/dies and which endings unlock.", "First casualty achievement 72.3% — most players haven't finished it (L0)"],
            ]),
            notes("How endings branch", [
                "Key decisions (Dragon Knight ultimatum at Cycle 4, the Act 2 murder, Kutnar's fate, Arthur alliance) lock or unlock ending paths.",
                "The time-rewind system means you can re-roll decisions within a run, but some branches are mutually exclusive.",
                "Faction balance at the finale, and which knights survived, both feed into which ending you get."]),
            faq_block([
                ["How many endings are there?", "A full verified count is 待补. Community videos confirm at least conquest, King Slayer, hidden/alt and Arthur marriage endings."],
                ["Can I see every ending in one run?", "No — several routes are mutually exclusive. Use New Game+ and the rewind system to explore branches across runs."],
                ["Does the Act 2 murder affect endings?", "Yes — the murder investigation (Gwendan's questline) changes who survives and which resolutions unlock; only ~27.7% of players have completed it (achievement rate)."],
            ]),
        ],
        "i18n": {"zh-CN": {
            "title": "全部结局与隐藏结局",
            "metaTitle": "君王之塔 全结局：征服结局、King Slayer、隐藏结局与分支结构",
            "metaDescription": "君王之塔全结局攻略：征服结局、King Slayer 决议、隐藏/替代结局，以及决定命运的分支结构。",
            "intro": "君王之塔是一款多分支多结局游戏。有些结局是简单路线结果；有些藏在特定决策、派系平衡或恋爱线后面。",
            "sections": [
                table(["结局 / 路线", "已知信息", "状态"], [
                    ["征服结局（一周目）", "社区 B 站视频展示一周目征服结局。", "存在（L0 视频）；条件待补"],
                    ["King Slayer 决议", "涉及 King Slayer 的决议路径，粉丝站有覆盖。", "whisperofthehouse 覆盖（L0）；步骤待补"],
                    ["隐藏 / 替代结局", "Steam 社区：「How to get the secret alt ending」（7 回复）。", "社区报告；步骤待补"],
                    ["亚瑟王联姻结局", "社区视频展示与亚瑟王联姻的结局。", "存在（L0）；条件待补"],
                    ["Gwendan 谋杀线", "Act 2 谋杀调查影响谁存活/死亡以及解锁哪些结局。", "首杀成就达成率 72.3%——多数玩家没做完（L0）"],
                ]),
                notes("结局怎么分支", [
                    "关键决策（Cycle 4 龙骑士最后通牒、Act 2 谋杀、Kutnar 去留、亚瑟王结盟）会锁定或解锁结局路径。",
                    "时间回溯系统允许你在单局内重 roll 决策，但部分分支互斥。",
                    "终局的派系平衡与存活骑士名单共同决定你拿到哪个结局。"]),
                faq_block([
                    ["一共有多少结局？", "完整已核实数量待补。社区视频确认至少有征服、King Slayer、隐藏/替代、亚瑟王联姻等结局。"],
                    ["一周目能看完全部结局吗？", "不能——多条路线互斥。用 New Game+ 和回溯系统跨周目探索分支。"],
                    ["Act 2 谋杀会影响结局吗？", "会——谋杀调查（Gwendan 任务线）改变谁存活并解锁哪些决议；只有约 27.7% 的玩家完成过（成就率）。"],
                ]),
            ],
        }},
    }
    return en

# ---------- 页面：achievements ----------
def build_achievements():
    highlighted = [
        "A New Sovereign", "That's One Thing Sorted", "Good Things Come In Three", "A Successful Hunt",
        "And Thus, the Revolution Came to an End", "How to Deal With Dragons", "HURRAY! HURRAY!",
        "The Grand Derby", "It's a Mess", "How to Train Your Griffin",
    ]
    en = {
        "slug": "sovereign-tower/achievements",
        "title": "All 75 Achievements",
        "metaTitle": "Sovereign Tower All 75 Achievements: Full List & Roadmap (How Cute Guide)",
        "metaDescription": "Sovereign Tower has 75 Steam achievements. See the highlighted 10, the How Cute route and what the achievement data says about the game's hardest content.",
        "intro": "Sovereign Tower ships with 75 Steam achievements. The full list is still being verified from Steam Community data (待补), but the highlighted 10 and several important ones are confirmed.",
        "sections": [
            notes("Key facts", [
                "75 achievements total (Steam L0); 10 are 'highlighted' (Steam L0).",
                "First casualty (murder-line completion) sits at 72.3% achievement rate — the murder investigation is the most-skipped major branch.",
                "How Cute: requires an Arron who never ate a dragon heart + the empathy route + Act III. Choose EMPATHY ROUTE on Moonvale's 3rd mission (don't kill the baby dragon) → accept different quests → gain Dragon Knight perk."]),
            table(["Highlighted achievement", "What it suggests"], [[h, "Part of the game's showcased progression"] for h in highlighted]),
            faq_block([
                ["How do I get How Cute?", "Keep Arron on the kind path (never eat a dragon heart), pick the EMPATHY ROUTE on Moonvale's 3rd mission, then continue into Act III on the empathy route."],
                ["What's the hardest achievement?", "Per achievement-rate data, the murder-line completion (first casualty, 72.3%) is the most-skipped — a strong candidate."],
                ["Is the full list available?", "The complete 75-achievement table is 待补 (Steam Community is rate-limited; we're verifying via SteamDB/community sources)."],
            ]),
        ],
        "i18n": {"zh-CN": {
            "title": "全部 75 个成就",
            "metaTitle": "君王之塔 全部 75 个成就：完整列表与路线图（How Cute 攻略）",
            "metaDescription": "君王之塔共有 75 个 Steam 成就。查看重点 10 个、How Cute 路线，以及成就率数据揭示的游戏最难内容。",
            "intro": "君王之塔共 75 个 Steam 成就。完整列表仍在从 Steam 社区数据核实中（待补），但重点 10 个和几个关键成就已确认。",
            "sections": [
                notes("关键事实", [
                    "共 75 个成就（Steam L0）；10 个为 highlighted 重点（Steam L0）。",
                    "first casualty（谋杀线完成）成就率 72.3%——谋杀调查是最多人跳过的重大分支。",
                    "How Cute：需要没吃龙心的 Arron + 共情路线 + Act III。Moonvale 第 3 任务选 EMPATHY ROUTE（不杀幼龙）→ 接受不同任务 → 获得 Dragon Knight 特质。"]),
                table(["重点成就", "含义"], [[h, "游戏展示的进度节点之一"] for h in highlighted]),
                faq_block([
                    ["How Cute 怎么拿？", "让 Arron 走仁善线（从不吃龙心），Moonvale 第 3 任务选 EMPATHY ROUTE，然后沿共情路线推进到 Act III。"],
                    ["最难成就是什么？", "按成就率数据，谋杀线完成（first casualty，72.3%）是最多人跳过的——是最有力候选。"],
                    ["完整列表在哪？", "完整 75 成就表待补（Steam 社区限流；我们正通过 SteamDB/社区源核实）。"],
                ]),
            ],
        }},
    }
    return en

# ---------- 页面：首页（品类 Hub 雏形）----------
def build_home():
    en = {
        "slug": "index",
        "title": "Sovereign Tower Guide Hub",
        "metaTitle": "Sovereign Tower (君王之塔) Guide: All Knights, Recipes, Endings & Tools",
        "metaDescription": "Complete Sovereign Tower guides: all 24 knights with stats and hidden traits, the 6 recipes, every ending, quest mechanics, romance and interactive tools.",
        "intro": "A fan-made guide hub for Sovereign Tower (君王之塔), the Round Table management RPG by WILD WITS GAMES / Curve Games. Start with the knights roster, then dive into recipes, endings and our interactive tools.",
        "sections": [
            notes("What's inside", [
                "All 24 knights — six stats, hidden traits, favourite meals and recruit conditions.",
                "Secret knights like Dulahan, Chester and Alwena and how to get them.",
                "The full quest score formula, XP table and affinity rules.",
                "All 6 recipes and each knight's favourite meal.",
                "Interactive tools: Knight Quest Matcher and Affinity Calculator.",
                "More cozy/sim game hubs are on the way — this is the first one."]),
            faq_block([
                ["Is this an official site?", "No — this is an unofficial fan resource. Game and assets belong to WILD WITS GAMES / Curve Games."],
                ["What language is the game in?", "Official languages: English, French, German, Japanese, Korean, Simplified Chinese. Our guides cover all six."],
                ["What's new in the game?", "Released 2026-08-06; launch sale 15% off until 2026-08-20. 75 achievements, Steam Deck Verified."],
            ]),
        ],
        "i18n": {"zh-CN": {
            "title": "君王之塔 攻略中心",
            "metaTitle": "君王之塔 Sovereign Tower 攻略：全部骑士、菜谱、结局与工具",
            "metaDescription": "君王之塔完整攻略：全部 24 位骑士属性与隐藏特质、6 种菜谱、全结局、任务机制、恋爱攻略与交互工具。",
            "intro": "《君王之塔》（Sovereign Tower）圆桌管理 RPG 的非官方攻略中心，开发者 WILD WITS GAMES / 发行 Curve Games。从骑士名单开始，再深入菜谱、结局与交互工具。",
            "sections": [
                notes("站内内容", [
                    "全部 24 位骑士——六维属性、隐藏特质、最爱菜与招募条件。",
                    "隐藏骑士（Dulahan、Chester、Alwena 等）的获取方法。",
                    "完整的任务得分公式、经验表与好感规则。",
                    "全部 6 种菜与每位骑士的最爱菜。",
                    "交互工具：骑士-任务匹配器与好感计算器。",
                    "更多 cozy/sim 游戏攻略中心即将上线——这是第一个。"]),
                faq_block([
                    ["这是官方站吗？", "不是——这是非官方粉丝资源站。游戏及相关资产归 WILD WITS GAMES / Curve Games 所有。"],
                    ["游戏支持什么语言？", "官方语言：英语、法语、德语、日语、韩语、简体中文。我们的攻略覆盖全部 6 种。"],
                    ["游戏有什么新内容？", "2026-08-06 发售；首发特惠 -15% 至 2026-08-20。75 个成就，Steam Deck Verified。"],
                ]),
            ],
        }},
    }
    # ja/ko/fr/de 翻译（data/i18n_home.json）
    import json as _json
    _i18n_home = _json.loads((ROOT / "i18n_home.json").read_text(encoding="utf8"))
    for lang, t in _i18n_home.items():
        en.setdefault("i18n", {})[lang] = {
            "title": t["title"], "metaTitle": t["metaTitle"], "metaDescription": t["metaDescription"], "intro": t["intro"],
            "sections": [
                {"type": "list", "tag": "NOTE", "heading": t["note_title"], "body": "", "items": t["note_items"]},
                {"type": "faq", "tag": "FAQ", "heading": t["faq_title"], "body": "", "items": t["faq_items"]},
            ],
        }
    return en

# ---------- 页面：工具页（quest-matcher / affinity-calc）----------
def build_tool_quest_matcher():
    en = {
        "slug": "sovereign-tower/tools/quest-matcher",
        "title": "Knight Quest Matcher",
        "metaTitle": "Sovereign Tower Knight Quest Matcher — Pick the Best Knight for Any Quest",
        "metaDescription": "Interactive tool: match Sovereign Tower knights to quest types and conditions, see who likes the quest and who dislikes it before you assign.",
        "intro": "Pick a quest type (and optionally a condition) to see which knights are a good fit — based on their liked/disliked quest preferences and key traits. All data is from the fan wiki roster.",
        "sections": [
            {"type": "questmatcher", "tag": "TOOL", "heading": "Knight Quest Matcher", "body": "", "items": []},
            notes("How to use", [
                "Choose a quest type from the dropdown. The table shows every knight, their affinity reaction to that quest type, and their special traits.",
                "Liked quest types give +1.33 affinity; disliked −0.75. Stacking liked conditions can push a quest to ~+4 affinity.",
                "Cross-check the knight's traits: e.g. Dulahan halves damage but takes +2 on failure (Clumsy); Gwendan dislikes Relic Recovery."]),
        ],
        "i18n": {"zh-CN": {
            "title": "骑士-任务匹配器",
            "metaTitle": "君王之塔 骑士-任务匹配器：为任意任务挑选最佳骑士",
            "metaDescription": "交互工具：按任务类型与条件筛选君王之塔骑士，在指派前查看谁喜欢这个任务、谁讨厌它。",
            "intro": "选择任务类型（可选条件），查看哪些骑士最合适——基于他们喜欢/厌恶的任务偏好与关键特质。数据来自粉丝 wiki 名单。",
            "sections": [
                {"type": "questmatcher", "tag": "TOOL", "heading": "骑士-任务匹配器", "body": "", "items": []},
                notes("使用方法", [
                    "从下拉框选择任务类型。表格会显示每位骑士对该任务类型的好感反应与特殊特质。",
                    "喜欢的任务类型 +1.33 好感；厌恶的 −0.75。叠加喜欢的条件可把单个任务推到约 +4 好感。",
                    "交叉核对骑士特质：例如 Dulahan 受伤减半但失败额外 +2 受伤（Clumsy）；Gwendan 厌恶 Relic Recovery。"]),
            ],
        }},
    }
    return en

def build_tool_affinity():
    en = {
        "slug": "sovereign-tower/tools/affinity-calc",
        "title": "Affinity Calculator",
        "metaTitle": "Sovereign Tower Affinity Calculator — Track Knight Affinity & Resignation Risk",
        "metaDescription": "Interactive tool: estimate a knight's affinity change from quest assignments, favourite meals and sovereign style choices, and see how close they are to resigning.",
        "intro": "Estimate how a knight's affinity moves: +1.33 per liked quest type, −0.75 per disliked, +1.5 per favourite meal, plus sovereign-style bonuses. At −7 most knights resign.",
        "sections": [
            {"type": "affinitycalc", "tag": "TOOL", "heading": "Affinity Calculator", "body": "", "items": []},
            notes("Rules built into the calculator", [
                "Liked quest type or condition: +1.33 affinity each. Disliked: −0.75 each.",
                "Favourite meal: +1.5 affinity and +0.5 quest score.",
                "Resignation threshold: −7 for almost everyone; Alwena and Ari never resign (−1500).",
                "This is a planning aid — actual in-game values may vary (待补 if a rule is unverified)."]),
        ],
        "i18n": {"zh-CN": {
            "title": "好感计算器",
            "metaTitle": "君王之塔 好感计算器：追踪骑士好感与辞职风险",
            "metaDescription": "交互工具：估算任务指派、最爱菜与君主风格选择对骑士好感的改变，以及距离辞职还有多远。",
            "intro": "估算骑士好感变化：喜欢的任务类型每个 +1.33、厌恶的 −0.75、最爱菜 +1.5、外加君主风格加成。好感降到 −7 多数骑士会辞职。",
            "sections": [
                {"type": "affinitycalc", "tag": "TOOL", "heading": "好感计算器", "body": "", "items": []},
                notes("内置规则", [
                    "喜欢的任务类型/条件：每个 +1.33 好感。厌恶的：每个 −0.75。",
                    "最爱菜：+1.5 好感 +0.5 任务分。",
                    "辞职阈值：多数人 −7；Alwena 和 Ari 永不辞职（−1500）。",
                    "这是规划辅助——实际游戏内数值可能不同（规则未核实时标待补）。"]),
            ],
        }},
    }
    return en

# ---------- 组装 ----------
ALL_PAGES = [
    build_home(),
    build_how_to_play(),
    build_knights(),
    build_secret_knights(),
    build_romance(),
    build_endings(),
    build_recipes(),
    build_quest_mechanics(),
    build_achievements(),
    build_tool_quest_matcher(),
    build_tool_affinity(),
]

# ja/ko/fr/de 页面翻译（data/i18n_pages.json）
import json as _j2
_i18n_pages = _j2.loads((ROOT / "i18n_pages.json").read_text(encoding="utf8"))
for _page in ALL_PAGES:
    _tr = _i18n_pages.get(_page["slug"])
    if not _tr:
        continue
    for _lang, _t in _tr.items():
        _secs = _t.get("sections") or []
        # knights 页：表头翻译（若有 table_head，构造翻译表格）
        if _t.get("table_head") and _page["slug"] == "sovereign-tower/knights":
            _src = [s for s in _page["sections"] if s.get("type") == "table" and s.get("headers") and s["headers"][0] == "Knight"]
            if _src:
                _secs = [{"type": "table", "tag": "DATA", "heading": "", "body": "", "headers": _t["table_head"], "rows": _src[0]["rows"]}] + _secs
        _page.setdefault("i18n", {})[_lang] = {
            "title": _t.get("title"), "metaTitle": _t.get("metaTitle"), "metaDescription": _t.get("metaDescription"), "intro": _t.get("intro"),
            "sections": _secs,
        }

existing = {p["slug"]: i for i, p in enumerate(d["pages"])}
for page in ALL_PAGES:
    if page["slug"] in existing:
        d["pages"][existing[page["slug"]]] = page  # 用真实内容覆盖骨架
    else:
        d["pages"].append(page)

# --- ja/ko sections 翻译合并（data/i18n_sections.json）---
import json as _j3
_i18n_sec = _j3.loads((ROOT / "i18n_sections.json").read_text(encoding="utf8"))
for _sp, _langs in _i18n_sec.items():
    for _pp in d["pages"]:
        if _pp.get("slug") != _sp: continue
        for _lg, _secs in _langs.items():
            if _lg in _pp.get("i18n", {}):
                _pp["i18n"][_lg]["sections"] = _secs

# --- meta 自动补全（ja/ko/fr/de 缺 metaTitle/metaDescription 时从 title/intro 生成并截断）---
def _clip(s, n):
    s = (s or "").strip()
    return s if len(s) <= n else s[: n - 1].rstrip() + "…"

# 默认语言页面 meta 截断（en/fr/de 60 字符）
for _p in d["pages"]:
    _lim0 = 35 if _p.get("slug", "").startswith(("zh", "ja", "ko")) else 55
    if _p.get("metaTitle") and len(_p["metaTitle"]) > _lim0:
        _p["metaTitle"] = _clip(_p["metaTitle"], _lim0)
    _dhi0 = 78 if _p.get("slug", "").startswith(("zh", "ja", "ko")) else 158
    if _p.get("metaDescription") and len(_p["metaDescription"]) > _dhi0:
        _p["metaDescription"] = _clip(_p.get("intro") or _p["title"], _dhi0)

for _p in d["pages"]:
    _i18n = _p.get("i18n") or {}
    for _lang, _t in _i18n.items():
        _base = _p
        _title = _t.get("title") or _p.get("title") or ""
        _intro = _t.get("intro") or _p.get("intro") or ""
        # metaTitle：若无或超长则生成
        _mt = _t.get("metaTitle")
        _lim = 35 if _lang.startswith(("zh", "ja", "ko")) else 55
        if not _mt or len(_mt) > _lim:
            _t["metaTitle"] = _clip(_title, _lim)
        # metaDescription：若无或超长则从 intro 生成
        _md = _t.get("metaDescription")
        _dhi = 78 if _lang.startswith(("zh", "ja", "ko")) else 158
        if not _md or len(_md) > _dhi:
            _t["metaDescription"] = _clip(_intro or _title, _dhi)

# 输出
(ROOT / "site.json").write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf8")
print(f"langs: {d['site']['languages']}")
print(f"pages: {len(d['pages'])}")
print("built:", ", ".join(p['slug'] for p in d['pages']))
