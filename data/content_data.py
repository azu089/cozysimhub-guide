# -*- coding: utf-8 -*-
"""Sovereign Tower 结构化数据（L0：raiderking 全页 + 知识库 + Steam 官方）。
所有数值均有来源；拿不到的标 None（生成时写"待补"）。"""

# 24 骑士完整名单（raiderking L0）
KNIGHT_NAMES = [
    "Alwena", "Angelica", "Ari", "Arron", "Brunhilda", "Chester", "Childeric",
    "Daguez", "Dulahan", "Edith", "Epicrate", "Gideon", "Goberto", "Gothild",
    "Gwendan Villador", "Ligia", "Oliver", "Rufus", "Silgur", "Tarcus",
    "The Wolf", "Ursula", "Victoria", "Zolta",
]

# 前 7 骑士完整档案（raiderking L0；其余六维/喜好待补）
KNIGHTS = [
    {
        "name": "Alwena", "title": "the Intendant",
        "origin": "Grest (Brizh)", "level": 12, "armor": 8, "never_resigns": True,
        "stats": [8, 9, 10, 0, 12, 7],
        "recruit": "一次性紧急事件：Act 2 之后，当圆桌可用骑士为 0 时（在册且不在任务中，死亡/辞职者除外）她会自愿加入。无法主动触发，没有第二次机会。永不死亡/永不辞职。",
        "known": ["Intendant（不能派 >1 cycle 的任务）", "Intimidating（Duel/Unethical/Intimidation +1；People Involved −1）", "Information Finder（Scouting/Track/Investigation +1）", "Brizh Connoisseur（任务在 Brizh 时得分加成）"],
        "hidden": [],
        "likes": ["Diplomacy", "Duel", "Relic Recovery"],
        "dislikes": [],
        "meals": ["Brizhian Butter Shortbread", "Crêpe"],
        "note": "唯一能挖其他骑士流言的人（一次一个，且只挖你不知道的）。",
    },
    {
        "name": "Angelica", "title": "of Clovermont",
        "origin": "Clovermont (Groveshire)", "level": 1, "armor": 5,
        "stats": [4, 8, 3, 0, 2, 7],
        "recruit": "开场剧情自动加入。",
        "known": ["Kind-Hearted（得分受任务对 People 满意度影响；Help/People Involved +1；Assassination/Unethical/Intimidation −1）", "Naive（Help +1；Diplomacy/Intimidation −1）"],
        "hidden": ["Fortunate（更好结果时有概率得分加成；Hunt/Assassination/Duel −1）†", "Animal Lover（Flying Creature/Cute Creature/Big Creature +1；Hunt −1）†"],
        "likes": ["Diplomacy", "Scouting"],
        "dislikes": ["Assassination †", "Ghost"],
        "sovereign_style": "喜欢 Kind，厌恶 Tyrannic",
        "meals": ["Préfou", "Crêpe"],
        "note": "君主风格：喜 Kind 恶 Tyrannic；恶 Ghost/Assassination。",
    },
    {
        "name": "Ari", "title": "the Griffin Rider",
        "origin": "Isle of Basalt", "level": 8, "armor": 6, "never_resigns": True,
        "stats": [5, 13, 8, 3, 8, 6],
        "recruit": "花 25 金币召唤（Basalt 兄弟的弟弟）。",
        "known": ["Griffin Rider（不能换坐骑）", "Scout（Relic Recovery/Scouting/Climbing/Woods/Track +1）"],
        "hidden": ["Speedster（得分加成随任务时长缩减）†", "Annoying（Diplomacy −1）†"],
        "likes": ["Scouting", "Relic Recovery", "Diplomacy（隐藏）"],
        "dislikes": ["Hunt"],
        "meals": ["Brizhian Butter Shortbread", "Crêpe"],
        "starting_gear": "坐骑 Columbus",
        "note": "永不辞职；坐骑 Columbus 使任务 −4 cycles。",
    },
    {
        "name": "Arron", "title": "of Drakovic",
        "origin": "Drakovic Castle", "level": 3, "armor": 7,
        "stats": [2, 2, 3, 6, 7, 8],
        "recruit": "无候选朝会——通过 Drakovic 剧情线加入。",
        "evolution": "两条互斥路线二选一：① 仁善线：在他仍 Neutral 时派去 Moonvale 的 Stop the baby dragon / Tame the baby dragon（或对话拿龙蛋后完成任意任务）→ STR+1/CHA+3/MAG+5/WIT+1，获得 Baby dragon 圣物和 Dragon Knight，失去 Timid。② 暴力线：完成他的骑士任务 quest_arron_ritual（需持有 Dragon Heart）→ STR+2/AGI+1/CHA+1/MAG+3，获得 Brutal，失去 Timid，最爱菜和辞职场景改变。",
        "known": ["Timid（独行时得分惩罚；Diplomacy/Competition/Crowd −1）"],
        "hidden": ["Short Target（任务中受伤 −1）†", "Educated（无直接得分效果，任务结局/对话读取）", "Dragon Expert（Dragon +1）"],
        "likes": ["Scouting", "Relic Recovery"],
        "dislikes": ["Diplomacy", "Crowd †"],
        "meals": ["Crêpe", "Brizhian Butter Shortbread"],
        "note": "剧情可得 Dragon Knight 特质（任意任务小加成，战斗翻倍）。",
    },
    {
        "name": "Brunhilda", "title": "the Hothead",
        "origin": "Fort Gavault", "level": 1, "armor": 6,
        "stats": [7, 2, 6, 7, 3, 0],
        "recruit": "Gavault 剧情线女儿侧（county_quest_gavault_2_daughter_side 到结局），无候选朝会。",
        "known": ["Fire Lady（任务在林地图时 +1 受伤）", "Heated（Unethical +1；Water/Woods −1）"],
        "hidden": ["Idol（成功时有概率 +1 People 满意度；Musical +1）†", "Popular（Crowd +1）†"],
        "likes": ["Hunt", "Crowd（隐藏）"],
        "dislikes": ["Diplomacy", "Water"],
        "sovereign_style": "喜欢 Audacious，厌恶 Wise",
        "meals": ["Galette-Saucisse", "Lion's Taco"],
        "note": "君主风格：喜 Audacious 恶 Wise。",
    },
    {
        "name": "Chester", "title": "the Jester",
        "origin": "Milkford", "level": 15, "armor": 6,
        "stats": None,  # 完全随机
        "recruit": "Clean Keeper Goose Part 2 任意特殊结局后出现（奶酪/马/Gwendan 三选一，各付 1 金币）——Chester 才是真正的奖品。",
        "known": ["Jester（属性完全随机，每次判定重 roll 0-15）"],
        "hidden": ["Happy To Be Here（享受所有任务类型，每次派任 +1.0 好感）†"],
        "likes": ["全部任务类型"],
        "dislikes": [],
        "meals": ["Galette-Saucisse", "Croque-Monsieur", "Préfou", "Crêpe", "Brizhian Butter Shortbread", "Lion's Taco"],
        "note": "随机属性 + 全类型好感 = 万能补位工具人。",
    },
    {
        "name": "Childeric", "title": "the Sentinel",
        "origin": "Almora", "level": 6, "armor": 9,
        "stats": [7, 4, 4, 0, 12, 4],
        "recruit": None,
        "known": ["Resourceful（每点 Wits 小得分加成）", "Tank（任务出发时每点护甲小得分加成）"],
        "hidden": ["Paranoid †", "Anxious †"],
        "likes": None,
        "dislikes": None,
        "meals": ["Crêpe", "Croque-Monsieur"],
        "note": "护甲 9 为全游最高。",
    },
]

# 其余骑士基础信息（raiderking 属性词表 + 知识库 L0；六维待补）
KNIGHTS_BASIC = {
    "Daguez": {"origin": "Grest (Brizh)", "level": 1, "armor": 6, "stats": [15, 0, 0, 0, 0, 9],
        "known": ["My Sword!（不能换圣物）", "Problem Solver（每点 Strength 小得分加成）"],
        "hidden": ["Problem Solver", "Nitwit †"], "meals": ["Crêpe", "Galette-Saucisse", "Préfou"], "note": "满力量 15；巨剑锁定。"},
    "Dulahan": {"origin": "Anveld", "level": 1, "armor": 7, "stats": [8, 8, 0, 9, 0, 0],
        "known": ["Intangible（受伤减半）", "Clumsy（任务失败额外 +2 受伤）", "Inattentive"],
        "hidden": ["Demon"], "meals": ["全部 6 种"], "note": "Goberto 死后才出现（恶魔骑士）。"},
    "Edith": {"origin": "Avalon", "level": 8, "armor": 7, "stats": [7, 10, 3, 12, 7, 0],
        "known": ["Perfume（不能换圣物）", "Syphon"], "hidden": ["Possessed Sword †（每个完成的人杀任务小得分加成）", "Demonic Presence †"],
        "meals": ["Croque-Monsieur", "Brizhian Butter Shortbread"], "note": "MAG 12 并列最高；圣物 Dainself。"},
    "Epicrate": {"origin": "Brimwood Congregation", "level": 9, "armor": 6, "stats": [3, 3, 9, 9, 12, 3],
        "known": ["Revolutionar（得分受 People 与 Nobility 满意度差影响）"], "hidden": ["Time Perception（另一时间线已做过该任务时得分加成）"],
        "meals": None, "note": "Brimwood 起义历史人物。"},
    "Gideon": {"origin": None, "level": None, "armor": None, "stats": None,
        "known": ["Lasting Impression（同地点已成功过任务时得分加成）", "Protagonist（队友表现更好时得分加成）"],
        "hidden": None, "meals": None, "note": "中文资料：第 6 天可招。"},
    "Goberto": {"origin": None, "level": None, "armor": None, "stats": None,
        "known": ["Cheesemaker（装备奶酪时得分加成）", "Clumsy（任务失败额外 +2 受伤）"],
        "hidden": None, "meals": None, "note": "中文资料：第 2 天派他战死 → Dulahan 第 4 天出现。"},
    "Gothild": {"origin": None, "level": None, "armor": None, "stats": None,
        "known": ["Bodyguard（队友任务中受伤 −1）", "Believer（基于 Scholars 满意度的加成）"],
        "hidden": None, "meals": None, "note": None},
    "Gwendan Villador": {"origin": None, "level": 1, "armor": 6, "stats": None,
        "known": ["Noble Soul（得分受任务对 Nobility 满意度影响；升级为 True Noble Soul 后受所有满意度类别影响）", "In Debt（有概率减少任务金币收益）"],
        "hidden": ["Seductive", "Fear of the Dark †"], "meals": None, "note": "恶 Audacious；谋杀案疑凶（跨周目可变）。"},
    "Ligia": {"origin": None, "level": None, "armor": None, "stats": None,
        "known": ["Scholar（成功时有概率 +1 Scholars 满意度）", "Coastal（任务靠近海边时得分加成）"],
        "hidden": None, "meals": None, "note": None},
    "Oliver": {"origin": None, "level": None, "armor": None, "stats": None,
        "known": ["Overworked（得分惩罚随任务时长）", "Office Worker（金币奖励随任务时长增加）"],
        "hidden": None, "meals": None, "note": None},
    "Rufus": {"origin": None, "level": None, "armor": None, "stats": None,
        "known": ["Loyal（得分受队伍平均好感影响）", "Wolf Habits（任务少 1 cycle）"],
        "hidden": None, "meals": None, "note": "中文资料：第 6 天；与狼同行。"},
    "Silgur": {"origin": None, "level": None, "armor": None, "stats": None,
        "known": ["Patient（任务 >1 cycle 时得分加成）", "Poacher（有概率 +1 Merchants 满意度）"],
        "hidden": None, "meals": None, "note": "中文资料：第 7 天。"},
    "Tarcus": {"origin": None, "level": None, "armor": None, "stats": None,
        "known": ["Nobility Primes（得分受 Nobility 与 People 满意度差影响）", "Nobles Defender（有概率 +1 Nobility 满意度）"],
        "hidden": None, "meals": None, "note": None},
    "The Wolf": {"origin": None, "level": None, "armor": None, "stats": None,
        "known": ["Wolf（不能换坐骑）", "Loyal（得分受队伍平均好感影响）"],
        "hidden": None, "meals": None, "note": "中文资料：第 6 天。"},
    "Ursula": {"origin": None, "level": None, "armor": None, "stats": None,
        "known": ["Immortal（任务死亡后可再招募）", "Loner（独行任务得分加成）"],
        "hidden": None, "meals": None, "note": "中文资料：第 5 天。"},
    "Victoria": {"origin": None, "level": None, "armor": None, "stats": None,
        "known": ["Sadistic（人杀任务得分加成）", "Touchy（任务指派时好感损失翻倍）", "Victoria's Sword（不能换圣物）"],
        "hidden": None, "meals": None, "note": None},
    "Zolta": {"origin": None, "level": None, "armor": None, "stats": None,
        "known": ["Conductor（涉水任务得分惩罚 +1 受伤）", "Gambler（每点 Luck 小得分加成）"],
        "hidden": None, "meals": None, "note": None},
}

# 6 种菜（raiderking L0）
RECIPES = [
    {"en": "Galette-Saucisse", "zh": "香肠荞麦饼", "desc_en": "Sausage buckwheat galette — a Brizh street staple.", "desc_zh": "香肠荞麦饼——布里兹的街头主食。"},
    {"en": "Croque-Monsieur", "zh": "法式三明治", "desc_en": "Ham & cheese toasted sandwich, the classic comfort.", "desc_zh": "火腿奶酪烤三明治，经典治愈系。"},
    {"en": "Préfou", "zh": "蒜香面包", "desc_en": "Garlic bread baked in butter — a tavern favourite.", "desc_zh": "黄油烤蒜香面包——酒馆最爱。"},
    {"en": "Crêpe", "zh": "可丽饼", "desc_en": "Thin French pancake, sweet or savoury.", "desc_zh": "法式薄饼，可甜可咸。"},
    {"en": "Brizhian Butter Shortbread", "zh": "布里兹黄油酥饼", "desc_en": "Rich buttery shortbread from Brizh.", "desc_zh": "布里兹的浓郁黄油酥饼。"},
    {"en": "Lion's Taco", "zh": "狮子玉米饼", "desc_en": "A bold taco with a lion's share of filling.", "desc_zh": "馅料十足的豪迈玉米饼。"},
]

# 任务类型（raiderking L0）
QUEST_TYPES = [
    "Hunt", "Assassination", "Relic Recovery", "Diplomacy", "Scouting",
    "Confrontation", "Duel", "Competition", "Research", "Rescue", "Knight Quest",
]

# 任务条件（raiderking L0，21 项）
QUEST_CONDITIONS = [
    "Flying Creature", "Water", "Cute Creature", "Climbing", "Woods", "Crowd",
    "Cave", "Ghost", "Track", "Big Creature", "Magic Ritual", "Heavy Lifting",
    "Investigation", "Help", "At Night", "Musical", "Unethical", "Dragon",
    "Need Flying Mount", "Intimidation", "People Involved",
]

# 君主标签（raiderking L0）
SOVEREIGN_TAGS = ["Tyrannic", "Wise", "Kind", "Audacious", "Omniscient"]

# XP 表（raiderking L0）
XP_TABLE = [0, 12, 25, 40, 58, 77, 97, 117, 138, 160, 183, 207, 235, 265, 300]

# 得分阈值（raiderking L0）
SCORE_THRESHOLDS = [
    ("Critical Success", "+10", "奖励 ×2"),
    ("Great Success", "+5", "奖励 ×1.5"),
    ("Success", "0", "奖励 ×1"),
    ("Major Failure", "−5", "无奖励"),
    ("Critical Failure", "−10", "无奖励"),
]

# 派系（Steam L0）
FACTIONS = [
    {"en": "Merchants", "zh": "商人"},
    {"en": "Mystics", "zh": "秘术师"},
    {"en": "Scholars", "zh": "学者"},
    {"en": "Nobles", "zh": "贵族"},
    {"en": "People", "zh": "平民"},
]
