# -*- coding: utf-8 -*-
"""内容补齐模块（docs/30 矩阵）：knights 深页 + guides 核心页 + walkthrough。
可靠风格：所有嵌套列表用变量，杜绝手写括号错误。"""
import json
from pathlib import Path
from content_data import KNIGHTS, KNIGHTS_BASIC, SCORE_THRESHOLDS

ROOT = Path(__file__).parent

def table(headers, rows):
    return {"type": "table", "tag": "DATA", "heading": "", "body": "", "headers": headers, "rows": rows}

def notes(heading, items):
    return {"type": "list", "tag": "NOTE", "heading": heading, "body": "", "items": items}

def faq_block(items):
    return {"type": "faq", "tag": "FAQ", "heading": "FAQ", "body": "", "items": items}

def _stats(k):
    if k.get("stats") is None:
        return "随机（Chester 每次判定重 roll 0–15）" if k["name"] == "Chester" else "待补"
    return " / ".join(str(x) for x in k["stats"])

def _all_knights_rows():
    rows = []
    for k in KNIGHTS:
        rows.append([k["name"], k.get("origin") or "待补", str(k.get("level") or "待补"), str(k.get("armor") or "待补"), _stats(k)])
    for name, b in KNIGHTS_BASIC.items():
        rows.append([name, b.get("origin") or "待补", str(b.get("level") or "待补"), str(b.get("armor") or "待补"), _stats({"name": name, "stats": b.get("stats")})])
    return rows

def build_knights_roster():
    rows = _all_knights_rows()
    en_note = [
        "Stats are 0–15. Level 1–15; each level-up adds one point to a stat below 15.",
        "Chester's stats are fully random, rerolled on every check.",
        "Alwena and Ari never resign; most others walk at −7 affinity.",
    ]
    en_faq = [
        ["Who has the highest starting stats?", "Daguez starts with 15 Strength; Edith and Epicrate have 12 in their best stat (MAG and WIT respectively)."],
        ["Can I recruit all 24 in one run?", "Yes — all are recruitable, but several (Dulahan, Alwena, Arron, Brunhilda) are tied to specific storylines or emergency events."],
        ["What do the stats do?", "Each quest requires one or more stats; higher stats beat the requirement and push the outcome toward success (see quest mechanics)."],
    ]
    zh_note = [
        "属性 0–15；等级 1–15，每升一级可在未满 15 的属性上投 1 点。",
        "Chester 的属性完全随机，每次判定重 roll。",
        "Alwena 和 Ari 永不辞职；其他人在好感 −7 时离开。",
    ]
    zh_faq = [
        ["谁的起始属性最高？", "Daguez 起始力量 15；Edith 和 Epicrate 各自最强项 12（MAG/WIT）。"],
        ["一周目能招满 24 位吗？", "可以——全部可招募，但 Dulahan、Alwena、Arron、Brunhilda 等绑定特定剧情或紧急事件。"],
        ["属性有什么用？", "每个任务要求一种或多种属性；属性压过需求能推动结果走向成功（见任务机制）。"],
    ]
    en_secs = [table(["Knight", "Origin", "Lv", "Armour", "Stats (STR/AGI/CHA/MAG/WIT/LCK)"], rows), notes("How to read the roster", en_note), faq_block(en_faq)]
    zh_secs = [table(["骑士", "出身", "等级", "护甲", "六维 (STR/AGI/CHA/MAG/WIT/LCK)"], rows), notes("如何读名单", zh_note), faq_block(zh_faq)]
    return {
        "slug": "sovereign-tower/knights/roster",
        "title": "Knight Roster — All 24 Knights",
        "metaTitle": "Sovereign Tower Knight Roster: All 24 Knights, Levels & Stats",
        "metaDescription": "The complete Sovereign Tower knight roster: all 24 knights with origin, starting level, armour and six stats.",
        "intro": "Every one of the 24 Sovereign Tower knights is recruitable. This roster gives you the full list at a glance — origin, starting level, armour and the six stats that drive quest scoring.",
        "sections": en_secs,
        "i18n": {"zh-CN": {"title": "骑士名单：全部 24 位", "metaTitle": "君王之塔 骑士名单：全部 24 位骑士、等级与六维", "metaDescription": "君王之塔完整骑士名单：全部 24 位骑士的出身、起始等级、护甲与六维属性。", "intro": "君王之塔的 24 位骑士全部可以招募。这份名单让你一览全貌——出身、起始等级、护甲，以及驱动任务得分的六维属性。", "sections": zh_secs}},
    }

def build_knights_tier():
    en_rows = [
        ["S", "Daguez, Edith, Childeric, Alwena", "Elite starting stats (15 STR / 12 MAG / 12 WIT), armour 8-9, or unique utility (Alwena's Intendant rumours)."],
        ["A", "Ari, Brunhilda, Epicrate, Dulahan, Chester", "Strong stats or powerful traits: Ari 13 AGI, Dulahan half damage, Chester all-type affinity."],
        ["B", "Angelica, Arron, Gwendan, Tarcus, Ursula", "Solid with story investment; Ursula's Immortal is niche-useful, Arron becomes Dragon Knight."],
        ["C", "Goberto, Gothild, Ligia, Oliver, Rufus, Silgur, The Wolf, Victoria, Zolta, others", "Situation-dependent; many gain value through traits or storylines (data incomplete — 待补)."],
    ]
    en_note = [
        "This is based on L0 starting stats; hidden traits and storylines can move a knight up.",
        "Chester's random stats make his tier situational — never rely on him for must-win quests.",
        "Arron's Dragon Knight evolution (kind path) is one of the strongest late-game boosts.",
    ]
    en_faq = [
        ["Who is the strongest knight?", "By starting stats: Daguez (15 STR), Edith (12 MAG) and Childeric (12 WIT, armour 9). By utility: Alwena reveals hidden traits."],
        ["Is there a 'best' team?", "No single team — quests ask for different stats. A balanced roster covering STR/AGI/MAG/WIT beats a stack of one stat."],
        ["Do hidden traits change tiers?", "Yes — several hidden traits (Speedster, Dragon Knight, Time Perception) are powerful once revealed."],
    ]
    zh_rows = [
        ["S", "Daguez、Edith、Childeric、Alwena", "精英起始属性（15 力量 / 12 魔法 / 12 智慧）、护甲 8-9，或独特功能（Alwena 挖流言）。"],
        ["A", "Ari、Brunhilda、Epicrate、Dulahan、Chester", "属性强或特质强：Ari 13 敏捷、Dulahan 受伤减半、Chester 全类型好感。"],
        ["B", "Angelica、Arron、Gwendan、Tarcus、Ursula", "投入剧情后扎实：Ursula 的 Immortal 有特殊价值，Arron 可成 Dragon Knight。"],
        ["C", "Goberto、Gothild、Ligia、Oliver、Rufus、Silgur、The Wolf、Victoria、Zolta 等", "视情况而定；许多靠特质或剧情增值（数据不全——待补）。"],
    ]
    zh_note = [
        "基于 L0 起始属性；隐藏特质与剧情可让骑士上移。",
        "Chester 随机属性使他的档位视情况而定——必胜任务别依赖他。",
        "Arron 的 Dragon Knight 进化（仁善线）是最强后期加成之一。",
    ]
    zh_faq = [
        ["谁最强？", "按起始属性：Daguez（15 力量）、Edith（12 魔法）、Childeric（12 智慧/护甲 9）。按功能：Alwena 能挖隐藏特质。"],
        ["有最佳阵容吗？", "没有固定阵容——任务要求不同属性。均衡覆盖 STR/AGI/MAG/WIT 胜过堆单一属性。"],
        ["隐藏特质会改变档位吗？", "会——Speedster、Dragon Knight、Time Perception 等隐藏特质一旦揭示相当强力。"],
    ]
    en_secs = [table(["Tier", "Knights", "Why"], en_rows), notes("Tiering caveats", en_note), faq_block(en_faq)]
    zh_secs = [table(["档位", "骑士", "理由"], zh_rows), notes("分级注意", zh_note), faq_block(zh_faq)]
    return {
        "slug": "sovereign-tower/knights/tier-list",
        "title": "Knight Tier List (Starting Stats)",
        "metaTitle": "Sovereign Tower Knight Tier List — Best Knights by Starting Stats",
        "metaDescription": "Sovereign Tower knight tier list based on starting stats and traits: S/A/B/C ranking of the 24 knights for quest success.",
        "intro": "A practical tier list based on starting stats, armour and early traits — not a pure damage chart, because story conditions and affinity matter as much as raw numbers.",
        "sections": en_secs,
        "i18n": {"zh-CN": {"title": "骑士分级（起始属性）", "metaTitle": "君王之塔 骑士分级：按起始属性评 S/A/B/C", "metaDescription": "君王之塔骑士分级：基于起始六维、护甲与早期特质的 S/A/B/C 排名。", "intro": "基于起始属性、护甲与早期特质的实用分级——不是纯伤害榜，因为剧情条件与好感与数值同样重要。", "sections": zh_secs}},
    }

def build_guides_factions():
    en_rows = [
        ["Merchants", "Trade and wealth; quests and court decisions that boost the economy raise their satisfaction."],
        ["Mystics", "Magic and the arcane; rituals and magical quests please them."],
        ["Scholars", "Knowledge and research; research and investigation quests align with them."],
        ["Nobles", "Nobility and tradition; decisions favouring the aristocracy please them."],
        ["People", "The common folk; helping and kind decisions raise their standing."],
    ]
    en_note = [
        "A faction at zero satisfaction can trigger crisis events — keep all five above zero.",
        "Some knights gain or lose affinity based on faction balance (e.g. Epicrate and Tarcus score off the People/Nobility gap).",
        "You can also spend everything and betray everyone — the game explicitly allows it, but it locks certain endings.",
    ]
    en_faq = [
        ["Which faction should I prioritise?", "Keep People and Merchants healthy early (most quests and audiences touch them); then chase the faction your current storyline needs."],
        ["Do factions affect endings?", "Yes — the finale's faction balance feeds into which ending you unlock."],
        ["Can I fix a zeroed faction?", "Yes — run quests that please it and make kind court decisions; the meters recover over cycles."],
    ]
    zh_rows = [
        ["商人 Merchants", "贸易与财富；提振经济的任务和朝政决策提升其满意度。"],
        ["秘术师 Mystics", "魔法与秘术；仪式与魔法任务取悦他们。"],
        ["学者 Scholars", "知识与研究；调查与研究类任务契合他们。"],
        ["贵族 Nobles", "贵族与传统；偏向贵族的决策取悦他们。"],
        ["平民 People", "平民百姓；帮助与仁善的决策提升他们的地位。"],
    ]
    zh_note = [
        "满意度归零的派系可能触发危机事件——让五个都保持正数。",
        "部分骑士会根据派系平衡增减好感（如 Epicrate 和 Tarcus 以平民/贵族差计分）。",
        "也可以全花光然后背刺所有人——游戏明确允许，但会锁掉某些结局。",
    ]
    zh_faq = [
        ["应该优先哪个派系？", "前期保持平民和商人健康（大多数任务和朝会涉及它们）；然后追当前剧情需要的派系。"],
        ["派系影响结局吗？", "会——终局的派系平衡决定解锁哪个结局。"],
        ["归零的派系能救吗？", "能——派取悦它的任务 + 做仁善朝政决策，几个 cycle 就恢复。"],
    ]
    en_secs = [table(["Faction", "What drives it"], en_rows), notes("Balance strategies", en_note), faq_block(en_faq)]
    zh_secs = [table(["派系", "核心诉求"], zh_rows), notes("平衡策略", zh_note), faq_block(zh_faq)]
    return {"slug": "sovereign-tower/guides/factions", "title": "Factions Guide: Balance the Five", "metaTitle": "Sovereign Tower Factions Guide — Balance Merchants, Mystics, Scholars, Nobles & People", "metaDescription": "How Sovereign Tower's five factions work: Merchants, Mystics, Scholars, Nobles and People — balance strategies, crisis risks and ending impact.", "intro": "Sovereign Tower asks you to balance five factions: Merchants, Mystics, Scholars, Nobles and People. Each quest and court decision moves them, and a zeroed faction can trigger crisis events.", "sections": en_secs, "i18n": {"zh-CN": {"title": "派系攻略：平衡五大势力", "metaTitle": "君王之塔 派系攻略：平衡商人、秘术师、学者、贵族与平民", "metaDescription": "君王之塔五大派系怎么玩：商人、秘术师、学者、贵族、平民——平衡策略、危机风险与结局影响。", "intro": "君王之塔要求你平衡五大派系：商人、秘术师、学者、贵族、平民。每个任务和朝政决策都会影响它们，归零的派系可能触发危机事件。", "sections": zh_secs}}}

def build_guides_recruit():
    rows = []
    for k in KNIGHTS:
        rows.append([k["name"], k.get("recruit") or "待补"])
    for name, b in KNIGHTS_BASIC.items():
        note = b.get("note") or ""
        rows.append([name, note if any(x in note for x in ["招募", "出现", "可招", "加入"]) else "待补"])
    en_note = [
        "Several knights are story-gated: Dulahan (Goberto's death path), Arron (Drakovic storyline), Brunhilda (Gavault daughter side).",
        "Alwena joins only through a one-time emergency offer when the Round Table has zero available knights in Act 2+.",
        "Chester is the real prize of the Clean Keeper Goose Part 2 special outcome.",
    ]
    en_faq = [
        ["Are all 24 knights recruitable?", "Yes — all are recruitable, but several require specific storylines, deaths or emergency events."],
        ["Can I miss a knight?", "Yes — Alwena is a one-time offer; story knights can be lost if you don't progress their lines before the branch closes."],
        ["What's the earliest recruit?", "Angelica joins in the opening story; Ari can be summoned for 25 gold early."],
    ]
    zh_note = [
        "多位骑士剧情限定：Dulahan（Goberto 死亡线）、Arron（Drakovic 剧情）、Brunhilda（Gavault 女儿侧）。",
        "Alwena 只在 Act 2+ 圆桌可用骑士为 0 时一次性紧急加入。",
        "Chester 是 Clean Keeper Goose Part 2 特殊结局的真正奖品。",
    ]
    zh_faq = [
        ["24 位骑士都能招吗？", "可以——全部可招募，但多位需要特定剧情、死亡或紧急事件。"],
        ["会错过骑士吗？", "会——Alwena 是一次性机会；剧情骑士在分支关闭前没推进就会错过。"],
        ["最早能招谁？", "Angelica 开场加入；Ari 早期可花 25 金币召唤。"],
    ]
    en_secs = [table(["Knight", "Recruit condition"], rows), notes("Recruitment tips", en_note), faq_block(en_faq)]
    zh_secs = [table(["骑士", "招募条件"], rows), notes("招募技巧", zh_note), faq_block(zh_faq)]
    return {"slug": "sovereign-tower/guides/recruit-knights", "title": "Recruit Every Knight", "metaTitle": "Sovereign Tower: How to Recruit All Knights — Conditions & Windows", "metaDescription": "Recruit all 24 Sovereign Tower knights: recruit conditions, story gates, the Alwena emergency offer and Chester's goose quest prize.", "intro": "All 24 knights are recruitable, but the how varies: some join through the story, some through money, some through death paths or emergencies. Here is every recruit condition we know.", "sections": en_secs, "i18n": {"zh-CN": {"title": "招募全部骑士", "metaTitle": "君王之塔 怎么招募全部骑士：条件与窗口", "metaDescription": "招募君王之塔全部 24 位骑士：招募条件、剧情门槛、Alwena 紧急机会与 Chester 的鹅任务奖品。", "intro": "24 位骑士全部可招募，但方式各异：有的走剧情、有的花钱、有的走死亡线或紧急事件。这里是我们已知的每一条招募条件。", "sections": zh_secs}}}

def build_guides_timerewind():
    en_note = [
        "The Demon in the cellar lets you turn back time when a cycle goes badly — re-roll decisions and rewrite fate.",
        "It is the game's core safety net: nothing is permanently lost if you can rewind.",
        "Rewinds let you explore branches within a run, but some outcomes are mutually exclusive even across rewinds.",
    ]
    en_note2 = [
        "After a critical failure that costs a knight or a faction crisis.",
        "Before a story branch you want to explore differently (e.g. the Act 2 murder investigation).",
        "To fix a faction balance mistake before it snowballs.",
    ]
    en_faq = [
        ["Is there a cost to rewinding?", "Rewinding is free-form in this game — it is designed as a safety net, not a penalty mechanic (待补 exact limits)."],
        ["Can I rewind forever?", "You can rewind to re-roll decisions across cycles; exact limits are still being verified."],
        ["Does rewind change endings?", "Yes — re-rolling key decisions (Dragon Knight ultimatum, murder investigation, Arthur alliance) changes which ending unlocks."],
    ]
    zh_note = [
        "地窖里的恶魔让你在 cycle 搞砸时回溯时间——重新决策、改写命运。",
        "这是游戏的核心安全网：能回溯就没什么永久损失。",
        "回溯让你在单周目内探索分支，但部分结果即使回溯也互斥。",
    ]
    zh_note2 = [
        "一次重大失败损失骑士或派系危机之后。",
        "想用不同方式探索剧情分支时（如 Act 2 谋杀调查）。",
        "派系平衡失误滚雪球之前。",
    ]
    zh_faq = [
        ["回溯有代价吗？", "本作回溯是自由式的——设计为安全网而非惩罚机制（确切上限待补）。"],
        ["能无限回溯吗？", "可以跨 cycle 回溯重新决策；确切限制仍在核实。"],
        ["回溯会改变结局吗？", "会——重 roll 关键决策（龙骑士通牒、谋杀调查、亚瑟王结盟）会改变解锁哪个结局。"],
    ]
    en_secs = [notes("How time rewind works", en_note), notes("When to rewind", en_note2), faq_block(en_faq)]
    zh_secs = [notes("时间回溯怎么运作", zh_note), notes("什么时候该回溯", zh_note2), faq_block(zh_faq)]
    return {"slug": "sovereign-tower/guides/time-rewind", "title": "Time Rewind Explained", "metaTitle": "Sovereign Tower Time Rewind: How It Works & When to Use It", "metaDescription": "Sovereign Tower's time rewind system: the cellar demon, re-rolling decisions, exploring branches and fixing mistakes.", "intro": "When fate turns against you, the Demon in the cellar lets you turn back time and rewrite it. Here is how Sovereign Tower's rewind system works and when it is worth using.", "sections": en_secs, "i18n": {"zh-CN": {"title": "时间回溯机制详解", "metaTitle": "君王之塔 时间回溯：怎么运作与何时使用", "metaDescription": "君王之塔时间回溯系统：地窖恶魔、重新决策、探索分支与修正失误。", "intro": "命运不顺时，地窖里的恶魔让你回溯时间改写命运。这里是君王之塔回溯系统的运作方式与使用时机。", "sections": zh_secs}}}

def build_guides_questsuccess():
    en_note = [
        "Match knight stats to the quest requirements — a knight whose stat beats the requirement contributes positive score.",
        "Stack liked quest types and conditions (+1.33 affinity each) to keep affinity healthy, which unlocks better assignments.",
        "Feed favourite meals (+1.5 affinity, +0.5 score) before risky quests.",
        "Level knights in the stats their favourite quests demand.",
    ]
    en_faq = [
        ["What score do I need for a critical success?", "+10 or higher. +5 is a great success (1.5× rewards), 0 is a bare success."],
        ["Which knight should I send?", "The one whose required stats exceed the quest requirement — with liked quest types and a favourite meal if possible."],
        ["Do quests fail permanently?", "A failed quest just returns a failure outcome; you can rewind or reassign next cycle. Dead knights are the real cost."],
    ]
    zh_note = [
        "把骑士属性匹配到任务需求——属性压过需求的骑士贡献正分。",
        "叠加喜欢的任务类型与条件（每个 +1.33 好感）保持好感健康，解锁更好的指派。",
        "高风险任务前喂最爱菜（+1.5 好感 +0.5 分）。",
        "升级骑士在最常做的任务所需属性上。",
    ]
    zh_faq = [
        ["Critical Success 需要多少分？", "+10 及以上。+5 = Great Success（奖励 ×1.5），0 = 普通成功。"],
        ["该派哪个骑士？", "派需求属性压过任务要求的骑士——尽量加上喜欢的任务类型和最爱菜。"],
        ["任务失败会永久损失吗？", "失败只是返回失败结果；可以回溯或下个 cycle 重新指派。真正代价是骑士死亡。"],
    ]
    en_secs = [table(["Score", "Threshold", "Reward"], SCORE_THRESHOLDS), notes("How to push quests to success", en_note), faq_block(en_faq)]
    zh_secs = [table(["得分", "阈值", "奖励"], SCORE_THRESHOLDS), notes("怎么把任务推向成功", zh_note), faq_block(zh_faq)]
    return {"slug": "sovereign-tower/guides/quest-success", "title": "Quest Success Strategies", "metaTitle": "Sovereign Tower: How to Succeed at Quests — Score Formula & Strategy", "metaDescription": "Push Sovereign Tower quests to success: stat matching, liked quest stacking, favourite meals and levelling — with the full score thresholds.", "intro": "Quests are the heart of Sovereign Tower. Matching the right knight to the right quest is the difference between critical success and a total wipe.", "sections": en_secs, "i18n": {"zh-CN": {"title": "任务成功策略", "metaTitle": "君王之塔 任务怎么成功：得分公式与策略", "metaDescription": "把君王之塔任务推向成功：属性匹配、叠加喜欢任务、最爱菜与升级——含完整得分阈值。", "intro": "任务是君王之塔的核心。把正确的骑士派到正确的任务，是 Critical Success 和全军覆没的区别。", "sections": zh_secs}}}

def _wt(slug, title, metaT, metaD, intro, en_secs, zh_secs, zh_intro=None):
    return {"slug": slug, "title": title, "metaTitle": metaT, "metaDescription": metaD, "intro": intro, "sections": en_secs, "i18n": {"zh-CN": {"title": title, "metaTitle": metaT, "metaDescription": metaD, "intro": zh_intro or intro, "sections": zh_secs}}}

def build_walkthrough_act0():
    en_steps = [
        ["Opening audience", "Arlin the advisor guides your first day on the throne. Answer the court's first petitions — early answers shape your first faction moves."],
        ["First knight", "Angelica joins during the opening story as Arlin's niece."],
        ["First quest", "Send Angelica on an early quest to learn the Round Table loop: assign, wait, read the outcome."],
    ]
    en_faq = [
        ["How long is the prologue?", "It covers the first cycle or two — enough to learn the audience → quest → rewind loop (待补 exact length)."],
        ["Can I fail the prologue?", "Not permanently — the rewind system lets you re-roll early decisions."],
    ]
    zh_steps = [
        ["开场朝会", "顾问阿林(Arlin) 引导你第一天登基。回应朝廷的第一批诉求——早期回答塑造你的第一步派系动向。"],
        ["第一位骑士", "Angelica 在开场剧情中加入（阿林的侄女）。"],
        ["第一个任务", "派 Angelica 执行早期任务，学习圆桌循环：指派、等待、查看结果。"],
    ]
    zh_faq = [
        ["序章多长？", "覆盖前一个或两个 cycle——足够学会朝会→任务→回溯循环（确切长度待补）。"],
        ["序章会失败吗？", "不会永久失败——回溯系统让你重 roll 早期决策。"],
    ]
    en_secs = [{"type": "steps", "tag": "STEP", "heading": "Prologue walkthrough", "body": "", "items": en_steps}, faq_block(en_faq)]
    zh_secs = [{"type": "steps", "tag": "STEP", "heading": "序章流程", "body": "", "items": zh_steps}, faq_block(zh_faq)]
    return _wt("sovereign-tower/walkthrough/act-0", "Act 0: Prologue Walkthrough", "Sovereign Tower Act 0 Prologue Walkthrough — First Day on the Throne", "How to play the Sovereign Tower prologue: opening audience, your first knight and the Round Table loop.", "The opening of Sovereign Tower sets you on the throne with Arlin the advisor guiding your first decisions. Here is the Act 0 prologue, step by step.", en_secs, zh_secs)

def build_walkthrough_gavault():
    en_note = [
        "Act 1's Gavault storyline follows the daughter's side: Brunhilda, the princess of Gavault, appears in this chain (county_quest_gavault_2_daughter_side onward).",
        "Brunhilda joins through the Gavault story, not a candidacy audience.",
        "Her liked quest is Hunt; she dislikes Diplomacy and Water — match her assignments to keep affinity up.",
    ]
    en_faq = [
        ["How do I recruit Brunhilda?", "Progress the Gavault storyline's daughter side branch — she appears in that chain."],
        ["What is Brunhilda good at?", "Hunt quests; her Fire Lady trait means she takes +1 damage in woods."],
    ]
    zh_note = [
        "Act 1 的加沃特剧情走女儿侧：加沃特公主 Brunhilda 在这条线出现（county_quest_gavault_2_daughter_side 起）。",
        "Brunhilda 通过加沃特剧情加入，不是候选朝会。",
        "她喜欢 Hunt 任务，厌恶 Diplomacy 和 Water——指派时匹配她的喜好以维持好感。",
    ]
    zh_faq = [
        ["怎么招募 Brunhilda？", "推进加沃特剧情的女儿侧分支——她在那条线出现。"],
        ["Brunhilda 擅长什么？", "Hunt 任务；她的 Fire Lady 特质意味着在林地多受 1 点伤害。"],
    ]
    en_secs = [notes("Gavault storyline (daughter's side)", en_note), faq_block(en_faq)]
    zh_secs = [notes("加沃特剧情（女儿侧）", zh_note), faq_block(zh_faq)]
    return _wt("sovereign-tower/walkthrough/act-1-gavault", "Act 1: Gavault Walkthrough", "Sovereign Tower Act 1 Gavault Walkthrough — Brunhilda's Storyline", "Walk the Act 1 Gavault storyline: the daughter's side, recruiting Brunhilda and her Hunt preferences.", "The Gavault chain in Act 1 leads to Brunhilda, the princess of Gavault. Follow the daughter's side to recruit her and know how to assign her well.", en_secs, zh_secs)

def build_walkthrough_groveshire():
    en_note = [
        "The Groveshire storyline centres on Angelica, who joins in the opening and is tied to the Goose quest line.",
        "Angelica likes Kind sovereign decisions and dislikes Tyrannic ones; she dislikes Assassination and Ghost quests.",
        "The Clean Keeper Goose Part 2 special outcomes (cheese, a horse or Gwendan) lead to Chester as the real prize.",
    ]
    en_faq = [
        ["What happens in Groveshire?", "The story follows Angelica's home county and the goose/beast quest line that connects to Chester's recruitment."],
        ["How do I get Chester?", "Finish a Clean Keeper Goose Part 2 special outcome — Chester is the actual prize."],
    ]
    zh_note = [
        "格罗夫郡剧情围绕 Angelica，她在开场加入，并与鹅任务线关联。",
        "Angelica 喜欢 Kind 君主决策、厌恶 Tyrannic；她厌恶 Assassination 和 Ghost 任务。",
        "Clean Keeper Goose Part 2 的特殊结局（奶酪/马/Gwendan）导向真正奖品 Chester。",
    ]
    zh_faq = [
        ["格罗夫郡发生什么？", "剧情跟随 Angelica 的家乡郡和鹅/野兽任务线，该线连接 Chester 的招募。"],
        ["怎么拿 Chester？", "完成 Clean Keeper Goose Part 2 特殊结局——Chester 是真正奖品。"],
    ]
    en_secs = [notes("Groveshire storyline", en_note), faq_block(en_faq)]
    zh_secs = [notes("格罗夫郡剧情", zh_note), faq_block(zh_faq)]
    return _wt("sovereign-tower/walkthrough/act-1-groveshire", "Act 1: Groveshire Walkthrough", "Sovereign Tower Act 1 Groveshire Walkthrough — Angelica & the Goose Line", "Walk the Act 1 Groveshire storyline: Angelica's county, the goose quest line and Chester's recruitment.", "The Groveshire chain follows Angelica and the goose/beast quest line that ends with Chester. Here is what we know about the route.", en_secs, zh_secs)

def build_walkthrough_beasthunt():
    en_note = [
        "The Beast Hunt connects to Ari and The Wolf — both are tied to wolf/beast quest lines.",
        "Ari is a Griffin Rider (mount locked) and a strong Scout; he dislikes Hunt.",
        "The Wolf has the Wolf trait (mount locked) and is Loyal — score scales with party average affinity.",
        "Beast Hunt routes are still being verified in detail (待补 exact steps).",
    ]
    en_faq = [
        ["Which knights are best for beast hunts?", "Goberto, Rufus and Silgur prefer hunts; Angelica dislikes them."],
        ["How do I get The Wolf?", "Reported through the beast/wolf route; exact steps are still being verified (待补)."],
    ]
    zh_note = [
        "野兽狩猎连接 Ari 和 The Wolf——两者都与狼/野兽任务线相关。",
        "Ari 是 Griffin Rider（坐骑锁定）和强力 Scout；他厌恶 Hunt。",
        "The Wolf 有 Wolf 特质（坐骑锁定）和 Loyal——得分随队伍平均好感缩放。",
        "野兽狩猎路线的详细步骤仍在核实（待补）。",
    ]
    zh_faq = [
        ["野兽狩猎哪些骑士最好？", "Goberto、Rufus、Silgur 偏好狩猎；Angelica 厌恶。"],
        ["怎么拿 The Wolf？", "报告称通过野兽/狼路线；确切步骤仍在核实（待补）。"],
    ]
    en_secs = [notes("Beast Hunt guide", en_note), faq_block(en_faq)]
    zh_secs = [notes("野兽狩猎攻略", zh_note), faq_block(zh_faq)]
    return _wt("sovereign-tower/walkthrough/beast-hunt", "Beast Hunt Walkthrough", "Sovereign Tower Beast Hunt Walkthrough — Ari, The Wolf & Hunting Routes", "Beast hunt routes in Sovereign Tower: Ari and The Wolf recruitment, best knights for hunts and what to avoid.", "The Beast Hunt in Sovereign Tower connects Ari, The Wolf and the hunting quest line. Use the right knights and know the wolf routes.", en_secs, zh_secs)

def build_walkthrough_goosequest():
    en_note = [
        "The Clean Keeper Goose quest has special outcomes (cheese, a horse or Gwendan) that each pay 1 gold — but Chester is the actual prize.",
        "Chester has completely random stats and enjoys all quest types (+1.0 affinity per assignment).",
        "The goose route is the only confirmed path to Chester so far.",
    ]
    en_faq = [
        ["How do I start the goose quest?", "It appears as the Clean Keeper Goose line; the Part 2 special outcome triggers Chester (待补 exact trigger)."],
        ["Is Chester worth it?", "Yes — he never minds any assignment (all-type affinity) and his random stats make him a wildcard."],
    ]
    zh_note = [
        "Clean Keeper Goose 任务有特殊结局（奶酪/马/Gwendan），各付 1 金币——但真正奖品是 Chester。",
        "Chester 属性完全随机，享受所有任务类型（每次指派 +1.0 好感）。",
        "鹅路线是目前唯一确认能拿到 Chester 的路径。",
    ]
    zh_faq = [
        ["怎么开始鹅任务？", "以 Clean Keeper Goose 线出现；Part 2 特殊结局触发 Chester（确切触发条件待补）。"],
        ["Chester 值得吗？", "值得——他从不介意任何指派（全类型好感），随机属性让他成为万能补位。"],
    ]
    en_secs = [notes("Goose quest guide", en_note), faq_block(en_faq)]
    zh_secs = [notes("鹅任务攻略", zh_note), faq_block(zh_faq)]
    return _wt("sovereign-tower/walkthrough/goose-quest", "Goose Quest Walkthrough", "Sovereign Tower Goose Quest Walkthrough — How to Get Chester", "The Clean Keeper Goose quest in Sovereign Tower: special outcomes and how it leads to recruiting Chester.", "The Clean Keeper Goose quest line ends with Chester — the knight with random stats who loves every assignment. Here is the route as we know it.", en_secs, zh_secs)

def build_walkthrough_rebellion():
    en_note = [
        "The Rebellion storyline connects to Epicrate of Brimwood, a revolutionary figure from the Brimwood Congregation.",
        "Epicrate's Revolutionar trait scores off the difference between People and Nobility satisfaction — balance them for her.",
        "Her hidden Time Perception gives a score bonus if she already has the quest in another timeline (use rewind to exploit it).",
    ]
    en_faq = [
        ["What is the Rebellion?", "A storyline tied to Epicrate and Brimwood; exact branch steps are still being verified (待补)."],
        ["How should I use Epicrate?", "Keep People and Nobility balanced so her Revolutionar score stays positive."],
    ]
    zh_note = [
        "叛乱剧情连接 Brimwood 教团的革命人物 Epicrate。",
        "Epicrate 的 Revolutionar 特质以平民与贵族满意度之差计分——为她说保持两者平衡。",
        "她的隐藏 Time Perception：另一时间线已做过该任务时得分加成（用回溯利用它）。",
    ]
    zh_faq = [
        ["叛乱是什么？", "与 Epicrate 和 Brimwood 相关的剧情线；确切分支步骤仍在核实（待补）。"],
        ["怎么用 Epicrate？", "保持平民与贵族平衡，让她的 Revolutionar 得分保持正值。"],
    ]
    en_secs = [notes("Rebellion storyline", en_note), faq_block(en_faq)]
    zh_secs = [notes("叛乱剧情", zh_note), faq_block(zh_faq)]
    return _wt("sovereign-tower/walkthrough/rebellion", "Rebellion Walkthrough", "Sovereign Tower Rebellion Walkthrough — Epicrate & Brimwood", "The Rebellion storyline in Sovereign Tower: Epicrate of Brimwood, her Revolutionar trait and the People/Nobility balance.", "The Rebellion chain follows Epicrate and Brimwood. Balance People and Nobility to get the most from her revolutionary scoring.", en_secs, zh_secs)

def build_systems_annexes():
    en_note = [
        "Annexes are buildings that add systems to your tower: Carina's Forge repairs and crafts gear, the Witch's Alchemy Room makes consumables.",
        "Building and upgrading annexes unlocks more knights, tools and story.",
        "Exact annex lists and costs are still being verified (待补).",
    ]
    en_faq = [
        ["What do annexes do?", "They add systems — the Forge for gear, the Alchemy Room for consumables — and unlock progression."],
        ["Which annex first?", "The Forge is the reported priority for keeping knights' armour repaired (待补 exact unlock)."],
    ]
    zh_note = [
        "Annexes 是为高塔新增系统的建筑：Carina's Forge 锻炉修理/制作装备，Witch's Alchemy Room 炼金室制作消耗品。",
        "建造和升级附属建筑会解锁更多骑士、工具与剧情。",
        "确切的附属建筑清单与成本仍在核实（待补）。",
    ]
    zh_faq = [
        ["附属建筑有什么用？", "它们新增系统——锻炉做装备、炼金室做消耗品——并解锁进度。"],
        ["先建哪个？", "报告称锻炉优先，用于保持骑士护甲维修（确切解锁待补）。"],
    ]
    en_secs = [notes("Annexes & building", en_note), faq_block(en_faq)]
    zh_secs = [notes("附属建筑与扩建", zh_note), faq_block(zh_faq)]
    return _wt("sovereign-tower/systems/annexes", "Annexes & Building Guide", "Sovereign Tower Annexes Guide — Forge, Alchemy Room & Upgrades", "Sovereign Tower annexes: Carina's Forge, the Witch's Alchemy Room and how building unlocks progression.", "Annexes are the buildings that expand your tower's systems. The Forge handles gear, the Alchemy Room makes consumables — and both unlock new tools and story.", en_secs, zh_secs)

def build_systems_roundtable():
    en_note = [
        "The Round Table is where you assign knights to quests each cycle.",
        "Capacity grows with the story: Act 1 = 6 knights, Act 2 = 8, Act 3 = 10.",
        "Assign the right knight to the right quest — stats, liked quest types and favourite meals all feed the score.",
    ]
    en_faq = [
        ["How does the Round Table work?", "Each cycle you assign available knights to quests; outcomes return as Critical/Success/Failure."],
        ["Can the table be empty?", "Yes — if you have zero available knights in Act 2+, Alwena offers herself once as an emergency recruit."],
    ]
    zh_note = [
        "圆桌是每 cycle 给骑士指派任务的地方。",
        "容量随剧情增长：Act 1 = 6 骑士，Act 2 = 8，Act 3 = 10。",
        "把正确的骑士派到正确的任务——属性、喜欢的任务类型与最爱菜都喂给得分。",
    ]
    zh_faq = [
        ["圆桌怎么运作？", "每 cycle 把可用骑士指派给任务；结果返回 Critical/Success/Failure。"],
        ["圆桌会空吗？", "会——如果 Act 2+ 可用骑士为 0，Alwena 会一次性紧急自荐。"],
    ]
    en_secs = [notes("Round Table system", en_note), faq_block(en_faq)]
    zh_secs = [notes("圆桌系统", zh_note), faq_block(zh_faq)]
    return _wt("sovereign-tower/systems/round-table", "Round Table System Guide", "Sovereign Tower Round Table — Quest Assignment & Capacity", "How Sovereign Tower's Round Table works: capacity per act, quest assignment and emergency recruitment.", "The Round Table is the heart of Sovereign Tower — where knights go out on quests each cycle. Here is how the system works.", en_secs, zh_secs)

def build_systems_questoutcomes():
    en_note = [
        "Quest outcomes return as Critical Success / Great Success / Success / Major Failure / Critical Failure / Unexpected Outcome.",
        "Score thresholds: +10 critical, +5 great, 0 success, −5 major failure, −10 critical failure.",
        "Great and critical successes multiply rewards by 1.5× and 2×.",
        "Unexpected Outcomes are special events triggered by traits or story keys — worth exploring.",
    ]
    en_faq = [
        ["What is an Unexpected Outcome?", "A special result triggered by certain traits or story conditions — different from a plain success or failure."],
        ["How do I get great or critical successes?", "Match knight stats well above the quest requirements and stack liked conditions."],
    ]
    zh_note = [
        "任务结果返回 Critical Success / Great Success / Success / Major Failure / Critical Failure / Unexpected Outcome。",
        "得分阈值：+10 critical、+5 great、0 success、−5 major failure、−10 critical failure。",
        "Great 和 critical 成功把奖励乘以 1.5× 和 2×。",
        "Unexpected Outcome 是由特质或剧情键触发的特殊事件——值得探索。",
    ]
    zh_faq = [
        ["什么是 Unexpected Outcome？", "由特定特质或剧情条件触发的特殊结果——不同于普通成功或失败。"],
        ["怎么拿 great 或 critical 成功？", "让骑士属性远高于任务需求，并叠加喜欢的条件。"],
    ]
    en_secs = [notes("Quest outcomes explained", en_note), faq_block(en_faq)]
    zh_secs = [notes("任务结果详解", zh_note), faq_block(zh_faq)]
    return _wt("sovereign-tower/systems/quest-outcomes", "Quest Outcomes Explained", "Sovereign Tower Quest Outcomes — Thresholds, Rewards & Unexpected", "Sovereign Tower quest outcomes: critical/great/success/failure thresholds, reward multipliers and Unexpected Outcomes.", "Every quest in Sovereign Tower returns one of six outcomes. Here are the thresholds, rewards and what triggers Unexpected Outcomes.", en_secs, zh_secs)

def build_systems_kingdommap():
    en_note = [
        "Sovereign Tower's kingdom spans several regions: Brizh, Clovermont/Groveshire, Fort Gavault, Drakovic Castle, Avalon, Almora, Brimwood and more.",
        "Region names come from the knight origins — each knight's homeland is a quest location that can add flavour bonuses (e.g. Alwena's Brizh Connoisseur).",
        "A full interactive kingdom map is not yet verified (待补).",
    ]
    en_faq = [
        ["Why do regions matter?", "Some traits give score bonuses by region (e.g. Brizh Connoisseur); matching knights to their homeland quests can help."],
        ["Is there a map?", "The in-game kingdom map exists (System: kingdom-map) but exact layout is still being verified (待补)."],
    ]
    zh_note = [
        "君王之塔的王国横跨多个地区：Brizh、Clovermont/Groveshire、Fort Gavault、Drakovic Castle、Avalon、Almora、Brimwood 等。",
        "地区名来自骑士出身——每位骑士的家乡是任务地点，可能带来风味加成（如 Alwena 的 Brizh Connoisseur）。",
        "完整的交互式王国地图尚未核实（待补）。",
    ]
    zh_faq = [
        ["地区为什么重要？", "部分特质按地区给得分加成（如 Brizh Connoisseur）；把骑士派到家乡任务可能有帮助。"],
        ["有地图吗？", "游戏内有王国地图（kingdom-map 系统），但确切布局仍在核实（待补）。"],
    ]
    en_secs = [notes("Kingdom regions", en_note), faq_block(en_faq)]
    zh_secs = [notes("王国地区", zh_note), faq_block(zh_faq)]
    return _wt("sovereign-tower/systems/kingdom-map", "Kingdom Map & Regions", "Sovereign Tower Kingdom Map — Regions, Homelands & Bonuses", "Sovereign Tower's kingdom regions: Brizh, Groveshire, Gavault, Drakovic and more — plus region-based trait bonuses.", "Sovereign Tower's kingdom spans regions tied to each knight's homeland. Some traits reward assigning knights to their home regions.", en_secs, zh_secs)

def build_systems_audience():
    en_note = [
        "Each cycle starts with a morning court (audience): citizens bring petitions from gardening to demon hunting.",
        "How you answer shapes faction satisfaction and knight opinions.",
        "Court decisions apply Sovereign archetype tags (Tyrannic, Wise, Kind, Audacious, Omniscient) that some knights approve or dislike.",
    ]
    en_faq = [
        ["What should I do in the audience?", "Answer thoughtfully — every decision moves a faction and applies a sovereign tag that knights react to."],
        ["Do audience answers lock anything?", "They feed faction meters and knight affinity; extreme choices can set up crisis events or special endings."],
    ]
    zh_note = [
        "每 cycle 从早朝（朝会）开始：市民带来园艺到驱魔的诉求。",
        "你的回答方式影响派系满意度与骑士看法。",
        "朝政决策应用君主标签（Tyrannic、Wise、Kind、Audacious、Omniscient），部分骑士会认可或反感。",
    ]
    zh_faq = [
        ["朝会该怎么做？", "用心回答——每个决策都会推动派系并应用骑士反应的君主标签。"],
        ["朝会答案会锁定什么吗？", "它们喂给派系表和骑士好感；极端选择可能设置危机事件或特殊结局。"],
    ]
    en_secs = [notes("Morning court / audience", en_note), faq_block(en_faq)]
    zh_secs = [notes("早朝 / 朝会", zh_note), faq_block(zh_faq)]
    return _wt("sovereign-tower/systems/audience", "Audience (Morning Court) Guide", "Sovereign Tower Audience — Morning Court, Petitions & Sovereign Tags", "The Sovereign Tower morning court: petitions, faction moves and the sovereign archetype tags knights react to.", "Every cycle opens with the morning court. Your answers move factions and apply sovereign tags that knights approve or dislike.", en_secs, zh_secs)

def build_updates_log():
    en_note = [
        "Released 2026-08-06 (v1.0, not early access).",
        "Launch sale: 15% off until 2026-08-20 (¥57.80 in CN).",
        "2 DLCs are attached (appids 4870280 / 4911710) — content still being verified (待补).",
        "This page is the change log for our guides — it updates as we verify new mechanics.",
    ]
    en_faq = [
        ["When was Sovereign Tower released?", "2026-08-06, as a full release (not early access)."],
        ["What is in the DLCs?", "Two DLC entries exist on Steam; their contents are still being verified (待补)."],
    ]
    zh_note = [
        "2026-08-06 发售（v1.0，非抢先体验）。",
        "首发特惠：-15% 至 2026-08-20（国区 ¥57.80）。",
        "已挂 2 个 DLC（appid 4870280 / 4911710）——内容仍在核实（待补）。",
        "本页是我们的攻略更新日志——每当我们核实新机制就更新。",
    ]
    zh_faq = [
        ["君王之塔什么时候发售？", "2026-08-06，正式版（非抢先体验）。"],
        ["DLC 有什么？", "Steam 上有 2 个 DLC 条目；内容仍在核实（待补）。"],
    ]
    en_secs = [notes("Release & updates", en_note), faq_block(en_faq)]
    zh_secs = [notes("发售与更新", zh_note), faq_block(zh_faq)]
    return _wt("sovereign-tower/updates", "Release & Update Log", "Sovereign Tower Release & Update Log", "Sovereign Tower release info and our guide update log: v1.0 launch, sale and DLC status.", "The Sovereign Tower changelog: release date, sale status, DLC and what we are verifying next.", en_secs, zh_secs)

# ================= review + items 板块 =================

def build_review_sysreq():
    en_rows = [
        ["Minimum", "Windows 10 / i5-4670K / 4GB RAM / GT 1030 2GB / DX12 / 3GB"],
        ["Recommended", "Windows 11 / i5-9600K / 8GB RAM / GTX 1060 6GB / DX12 / 3GB"],
        ["Linux / Steam Deck", "SteamOS 3.8.10 / Zen2 4c8t / 4-8GB / RDNA2 8CU (Deck Verified)"],
    ]
    en_faq = [
        ["Does it run on Mac?", "No official macOS support — Windows and Linux/SteamOS only."],
        ["Is it Steam Deck verified?", "Yes, per the official store page (Steam Deck Verified)."],
    ]
    zh_rows = [
        ["最低配置", "Windows 10 / i5-4670K / 4GB 内存 / GT 1030 2GB / DX12 / 3GB"],
        ["推荐配置", "Windows 11 / i5-9600K / 8GB 内存 / GTX 1060 6GB / DX12 / 3GB"],
        ["Linux / Steam Deck", "SteamOS 3.8.10 / Zen2 4c8t / 4-8GB / RDNA2 8CU（Deck Verified）"],
    ]
    zh_faq = [
        ["支持 Mac 吗？", "官方不支持 macOS——仅 Windows 和 Linux/SteamOS。"],
        ["Steam Deck 验证了吗？", "验证了（官方商店页 Steam Deck Verified）。"],
    ]
    en_secs = [table(["", "Requirements"], en_rows), faq_block(en_faq)]
    zh_secs = [table(["", "配置要求"], zh_rows), faq_block(zh_faq)]
    return _wt("sovereign-tower/review/system-requirements", "System Requirements", "Sovereign Tower System Requirements — Min, Recommended & Steam Deck", "Sovereign Tower system requirements: minimum, recommended and Steam Deck specs from the official store page.", "Sovereign Tower runs on Windows and Linux/SteamOS. Here are the official minimum, recommended and Steam Deck specs.", en_secs, zh_secs, "君王之塔支持 Windows 和 Linux/SteamOS。这里是官方最低、推荐与 Steam Deck 配置。")

def build_review_overview():
    en_rows = [
        ["Metacritic", "86 (store-page field)"],
        ["Steam rating", "Very Positive — 90% of 700+ reviews"],
        ["Release", "2026-08-06 (full release, not early access)"],
        ["Genre", "Indie / RPG — Round Table management"],
        ["Publisher", "Curve Games"],
    ]
    en_note = [
        "Reviews praise the witty, sharp writing, the Round Table quest loop and the time-rewind safety net.",
        "Some players find the rewind mechanic's learning curve steep (per a Chinese hands-on review).",
        "Unexpected outcomes and hidden traits keep replays interesting.",
    ]
    en_faq = [
        ["Is Sovereign Tower worth it?", "Strong reviews (Metacritic 86, 90% positive on Steam) for a management-RPG crowd that likes narrative and rewind mechanics."],
        ["Is it like Reigns?", "It has a similar 'assign and see' court rhythm, but with deeper knight stats, quest scoring and story branches."],
    ]
    zh_rows = [
        ["Metacritic", "86（商店页字段）"],
        ["Steam 评价", "特别好评——700+ 评测中 90% 好评"],
        ["发售", "2026-08-06（正式版，非抢先体验）"],
        ["类型", "独立 / RPG——圆桌管理"],
        ["发行商", "Curve Games"],
    ]
    zh_note = [
        "评测称赞毒舌而敏锐的文案、圆桌任务循环和时间回溯安全网。",
        "部分玩家觉得回溯机制的入门曲线陡（中文体验文）。",
        "Unexpected Outcome 和隐藏特质让重玩更有趣。",
    ]
    zh_faq = [
        ["君王之塔值得买吗？", "评测很强（Metacritic 86、Steam 90% 好评）——适合喜欢叙事和回溯机制的管理 RPG 玩家。"],
        ["像 Reigns 吗？", "有类似的「指派与查看」宫廷节奏，但骑士属性、任务得分和剧情分支更深。"],
    ]
    en_secs = [table(["Metric", "Value"], en_rows), notes("What reviews say", en_note), faq_block(en_faq)]
    zh_secs = [table(["指标", "数值"], zh_rows), notes("评测说了什么", zh_note), faq_block(zh_faq)]
    return _wt("sovereign-tower/review/overview", "Review Overview", "Sovereign Tower Review — Metacritic 86, Steam 90% Positive", "Sovereign Tower review overview: Metacritic 86, Steam 90% positive, what critics and players praise.", "Sovereign Tower landed strong reviews at launch. Here is the overview — scores, what's praised and who it's for.", en_secs, zh_secs)

def build_review_releasedemo():
    en_note = [
        "Released 2026-08-06 as a full v1.0 (not early access).",
        "A demo was available before launch (official Demo Trailer exists).",
        "Launch sale: 15% off until 2026-08-20.",
        "Two DLCs are attached (待补 contents).",
    ]
    en_faq = [
        ["Is there a demo?", "Yes — a demo was available pre-launch; check the Steam page for current demo status."],
        ["When is the next update?", "Follow the in-game updates and our update log; patch cadence is still being tracked (待补)."],
    ]
    zh_note = [
        "2026-08-06 作为完整 v1.0 发售（非抢先体验）。",
        "发售前有 demo（官方 Demo Trailer 存在）。",
        "首发特惠：-15% 至 2026-08-20。",
        "已挂 2 个 DLC（内容待补）。",
    ]
    zh_faq = [
        ["有 demo 吗？", "有——发售前开放过 demo；当前 demo 状态看 Steam 页。"],
        ["下次更新什么时候？", "关注游戏内更新和我们的更新日志；补丁节奏仍在追踪（待补）。"],
    ]
    en_secs = [notes("Release & demo", en_note), faq_block(en_faq)]
    zh_secs = [notes("发售与 demo", zh_note), faq_block(zh_faq)]
    return _wt("sovereign-tower/review/release-demo", "Release & Demo Info", "Sovereign Tower Release, Demo & Availability", "Sovereign Tower release and demo info: v1.0 date, demo availability, sale and DLC status.", "When did Sovereign Tower come out, is there a demo, and what's the DLC situation? Everything about availability.", en_secs, zh_secs)

def build_review_soundtrack():
    en_note = [
        "The game's official tags include soundtrack-adjacent qualities; the launch trailer features original music (待补 exact composer/album).",
        "Soundtrack details (composer, track list, availability on streaming) are still being verified (待补).",
        "Check the Steam store page and the game's official channels for soundtrack news.",
    ]
    en_faq = [
        ["Is there an official soundtrack?", "Not yet confirmed publicly (待补) — check the Steam page and developer channels."],
        ["Who composed the music?", "Still being verified (待补)."],
    ]
    zh_note = [
        "游戏官方标签包含原声相关的品质；启动预告片带有原创音乐（确切作曲人/专辑待补）。",
        "原声细节（作曲人、曲目、流媒体上架）仍在核实（待补）。",
        "查看 Steam 商店页和官方渠道获取原声消息。",
    ]
    zh_faq = [
        ["有官方原声吗？", "尚未公开确认（待补）——查看 Steam 页和开发者渠道。"],
        ["音乐谁作曲？", "仍在核实（待补）。"],
    ]
    en_secs = [notes("Soundtrack status", en_note), faq_block(en_faq)]
    zh_secs = [notes("原声状态", zh_note), faq_block(zh_faq)]
    return _wt("sovereign-tower/review/soundtrack", "Soundtrack Info", "Sovereign Tower Soundtrack — Music & Composer", "Sovereign Tower soundtrack status: what's known about the music, composer and availability.", "The music of Sovereign Tower adds a lot to its tone. Here is what we know so far about the soundtrack.", en_secs, zh_secs)

def build_items_overview():
    en_note = [
        "Sovereign Tower has consumables and crafting gear across the tower's systems (Forge, Alchemy Room).",
        "Item lists are still being verified in-game (待补) — this overview will grow as we confirm items.",
        "Key item families reported: consumables (potions, food) and crafting gear (weapons, armour materials).",
    ]
    en_faq = [
        ["What items exist in the game?", "Consumables and crafting gear are confirmed families; the full list is still being verified (待补)."],
        ["Where do I get items?", "The Forge crafts gear and the Alchemy Room makes consumables (exact recipes 待补)."],
    ]
    zh_note = [
        "君王之塔在塔的系统（锻炉、炼金室）里有消耗品和锻造装备。",
        "物品清单仍在游戏内核实（待补）——本总览会随确认增长。",
        "已报告的关键物品族：消耗品（药水、食物）和锻造装备（武器、护甲材料）。",
    ]
    zh_faq = [
        ["游戏里有什么物品？", "已确认消耗品和锻造装备两类；完整清单仍在核实（待补）。"],
        ["物品从哪来？", "锻炉做装备、炼金室做消耗品（确切配方待补）。"],
    ]
    en_secs = [notes("Items overview", en_note), faq_block(en_faq)]
    zh_secs = [notes("物品总览", zh_note), faq_block(zh_faq)]
    return _wt("sovereign-tower/items/overview", "Items Overview", "Sovereign Tower Items Overview — Consumables & Crafting Gear", "Sovereign Tower items overview: consumables and crafting gear families, where to get them and what we're verifying.", "An overview of Sovereign Tower's items — consumables and crafting gear — with what we've confirmed so far.", en_secs, zh_secs)

def build_items_consumables():
    en_note = [
        "The Witch's Alchemy Room makes consumables (potions, food) for quests and recovery.",
        "Consumable recipes and effects are still being verified (待补).",
        "Favourite meals give +1.5 affinity and +0.5 quest score — food is the most confirmed consumable family.",
    ]
    en_faq = [
        ["What consumables are there?", "Potions and food are reported; the full list is still being verified (待补)."],
        ["Are meals consumables?", "Yes — the 6 dishes are food consumables; feeding favourites boosts affinity and score."],
    ]
    zh_note = [
        "炼金室制作消耗品（药水、食物），用于任务和恢复。",
        "消耗品配方和效果仍在核实（待补）。",
        "最爱菜给 +1.5 好感和 +0.5 任务分——食物是最确认的消耗品族。",
    ]
    zh_faq = [
        ["有什么消耗品？", "已报告药水和食物；完整清单仍在核实（待补）。"],
        ["菜算消耗品吗？", "算——6 种菜是食物消耗品；喂最爱菜加好感与得分。"],
    ]
    en_secs = [notes("Consumables guide", en_note), faq_block(en_faq)]
    zh_secs = [notes("消耗品攻略", zh_note), faq_block(zh_faq)]
    return _wt("sovereign-tower/items/consumables", "Consumables Guide", "Sovereign Tower Consumables — Potions & Food", "Sovereign Tower consumables: potions and food from the Alchemy Room, effects and the favourite-meal bonus.", "Consumables in Sovereign Tower come from the Alchemy Room. Here is what we know about potions and food.", en_secs, zh_secs)

def build_items_craftinggear():
    en_note = [
        "Carina's Forge repairs and crafts gear; armour acts as hit points for quest damage.",
        "Gear crafting recipes and upgrade paths are still being verified (待补).",
        "Childeric starts with armour 9 (highest) — a strong tank for damage-heavy quests.",
    ]
    en_faq = [
        ["How does the Forge work?", "It repairs and crafts gear; exact recipes and slots are still being verified (待补)."],
        ["What does armour do?", "It is the hit points for quest damage — keep knights' armour repaired before risky quests."],
    ]
    zh_note = [
        "Carina's Forge 锻炉修理/制作装备；护甲是任务伤害的生命值。",
        "装备制作配方和升级路线仍在核实（待补）。",
        "Childeric 起始护甲 9（全游最高）——是伤害型任务的强力坦克。",
    ]
    zh_faq = [
        ["锻炉怎么运作？", "它修理/制作装备；确切配方和槽位仍在核实（待补）。"],
        ["护甲有什么用？", "它是任务伤害的生命值——高风险任务前保持骑士护甲维修。"],
    ]
    en_secs = [notes("Crafting & gear", en_note), faq_block(en_faq)]
    zh_secs = [notes("锻造与装备", zh_note), faq_block(zh_faq)]
    return _wt("sovereign-tower/items/crafting-gear", "Crafting & Gear Guide", "Sovereign Tower Crafting Gear — Forge, Armour & Upgrades", "Sovereign Tower crafting and gear: Carina's Forge, armour as quest hit points and what we know about recipes.", "Crafting and gear in Sovereign Tower revolve around the Forge. Armour is your knights' hit points for quest damage.", en_secs, zh_secs)
