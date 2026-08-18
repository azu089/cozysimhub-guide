# -*- coding: utf-8 -*-
"""Moonlight Peaks 页面模块（cozysimhub 第 2 游戏 · 月光档案室主题）。
数据源分级：L1=Steam 官方 appdetails / Marvelous 官方；L2=thegamer/gamer.org/screenhype/
sportsrant/gamewatcher/IGN/bonus-action/intoindiegames/vgspoilers/gematsu（采集见 work/bench-moonlight-peaks/）。
规则：专有名词（物品/角色/地点）单元格保留英文；表头/正文/FAQ 全翻译；
拿不到的数据标「待补」。zh-CN 关键表用「中文 (EN)」双语单元格。
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent

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

def lang_page(lang_data, en_sections):
    """用紧凑覆盖表生成语言版 page：sections 只覆盖已翻译的字段（heading/headers/items/body/rows），
    未覆盖字段（表格 rows 等）继承 EN。"""
    secs = []
    for i, es in enumerate(en_sections):
        ov = (lang_data.get("sections") or {}).get(i, {})
        sec = dict(es)
        for k in ("heading", "headers", "items", "body", "rows"):
            if k in ov:
                sec[k] = ov[k]
        secs.append(sec)
    return {
        "title": lang_data["title"],
        "metaTitle": lang_data.get("metaTitle", ""),
        "metaDescription": lang_data.get("metaDescription", ""),
        "intro": lang_data.get("intro", ""),
        "sections": secs,
    }

def _i18n(langs, en_sections):
    return {lg: lang_page(d, en_sections) for lg, d in langs.items()}

# =====================================================================
# HOME
# =====================================================================
HOME_EN = {
    "slug": "moonlight-peaks",
    "title": "Moonlight Peaks Guide Hub",
    "metaTitle": "Moonlight Peaks Guide: Gifts, Romance, Fishing, Flowers & Tools",
    "metaDescription": "Complete Moonlight Peaks guide hub: all 23 romanceable characters with gifts, 22 fish, every flower, tool upgrades, 59 achievements and a full walkthrough — in 6 languages.",
    "intro": "Moonlight Peaks is a cozy gothic life-sim by Little Chicken, published by XSEED Games and Marvelous Europe: raise mystical crops at night, brew potions, fish under the full moon, and romance werewolves, witches, mermaids and more in the town of Moonlight Peaks.",
    "sections": [
        N("What this hub covers", [
            "All 23 romanceable characters with loved / liked / disliked gifts and heart events.",
            "All 22 fish — locations, seasons, weather and moon-phase conditions, plus rod upgrades.",
            "Every flower with season, location, value and who to gift it to.",
            "Tool upgrades (Copper / Iron / Gold), spells, potions and the full 59-achievement list.",
            "A part-by-part main story walkthrough and the latest patch notes.",
        ]),
        T(["Guide", "What you'll find"], [
            ["Gift Guide", "Every character's loved / liked / disliked gifts with a searchable table."],
            ["Romance Guide", "All 23 dateable characters, heart levels, dates, marriage and vampire conversion."],
            ["Fishing Guide", "All fish, locations, full-moon exclusives and rod upgrades."],
            ["Flower Guide", "Every flower by season, location and value."],
            ["Tool Upgrades", "Copper / Iron / Gold costs and materials for every tool."],
            ["Achievements", "All 59 achievements and how to unlock them."],
            ["Walkthrough", "The main story step by step, part 1 to 8."],
        ]),
        N("Latest updates", [
            "Patch 1.1.45 (2026-07-21): photosensitivity warning, Star Gazing widescreen fix, 'Back to the Den' retroactive unlock — more improvements planned for 1.2.",
            "Patch 1.1.44 (2026-07-16): embroidery table visibility, all-season tree seeds, rainy-night crop fix, save-corruption fix.",
            "Moonlight Peaks launched July 6–7, 2026 on PC (Steam), Switch, Switch 2 and Google Play Games; sales passed 200,000 by July 26.",
        ]),
        F([
            ["Is this an official site?", "No — this is an unofficial fan resource. Moonlight Peaks and its assets belong to Little Chicken / XSEED Games / Marvelous Europe."],
            ["Which languages does the game support?", "Official languages: English, German, Japanese, Korean, Simplified Chinese and Traditional Chinese. Our guides cover all hub languages."],
            ["How many characters can you romance?", "23 romanceable characters at launch (July 7, 2026), including secret and hidden candidates."],
            ["How much does Moonlight Peaks cost?", "US$34.99 on Steam (full price at time of writing)."],
        ]),
    ],
}

HOME_I18N = {
    "zh-CN": {
        "title": "月光小镇 攻略中心",
        "metaTitle": "月光小镇攻略：礼物·恋爱·钓鱼·花卉·工具全指南",
        "metaDescription": "《月光小镇》Moonlight Peaks 完整攻略中心：23 位可攻略角色的礼物全表、22 种鱼、全部花卉、工具升级、59 个成就与分章主线流程，6 语言覆盖。",
        "intro": "《月光小镇》Moonlight Peaks 是 Little Chicken 开发、XSEED Games 与 Marvelous Europe 发行的哥特田园生活模拟：在夜晚种植魔法作物、熬制药水、满月下钓鱼，与狼人、女巫、人鱼甚至更多居民恋爱。",
        "sections": {
            0: {"heading": "本站覆盖内容"},
            1: {"heading": "攻略索引", "headers": ["攻略", "内容"], "rows": [
                ["礼物全表", "全部角色 喜欢/讨厌 礼物，可搜索筛选。"],
                ["恋爱指南", "23 位可攻略角色、心数、约会、结婚与转化为吸血鬼。"],
                ["钓鱼图鉴", "全部鱼类、钓点、满月专属与鱼竿升级。"],
                ["花卉全表", "按季节/地点/价格列出每种花。"],
                ["工具升级", "铜/铁/金 各工具的价格与材料。"],
                ["成就列表", "全部 59 个成就与解锁方法。"],
                ["主线流程", "主线故事第 1–8 部分逐步攻略。"],
            ]},
            2: {"heading": "最新更新"},
            3: {},
        },
    },
}

HOME_I18N.update({
    "ja": {
        "title": "ムーンライトピークス 攻略ハブ",
        "metaTitle": "ムーンライトピークス攻略：贈り物・恋愛・釣り・花・ツール",
        "metaDescription": "『Moonlight Peaks』完全攻略ハブ：恋愛対象23人の贈り物、全22種の魚、花、道具強化、実績59個、ストーリー攻略を6言語で。",
        "intro": "『Moonlight Peaks』は Little Chicken 開発、XSEED Games / Marvelous Europe 発売のゴシック系スローライフ：夜に不思議な作物を育て、ポーションを作り、満月の夜に釣りをし、狼人や魔女、人魚たちと恋愛も楽しめる。",
        "sections": {
            0: {"heading": "このハブの内容"},
            1: {"heading": "ガイド一覧", "headers": ["ガイド", "内容"]},
            2: {"heading": "最新アップデート"},
        },
    },
    "ko": {
        "title": "문라이트 피크스 가이드 허브",
        "metaTitle": "문라이트 피크스 공략: 선물·연애·낚시·꽃·도구",
        "metaDescription": "『문라이트 피크스』완전 공략 허브: 연애 가능 캐릭터 23명의 선물, 물고기 22종, 꽃, 도구 강화, 업적 59개, 메인 스토리 공략을 6개 언어로.",
        "intro": "『문라이트 피크스』는 Little Chicken이 개발하고 XSEED Games / Marvelous Europe이 배급하는 고딕 감성 라이프 시뮬: 밤에 신비한 작물을 키우고, 물약을 만들고, 보름달 아래 낚시를 하고, 늑대인간·마녀·인어들과 연애할 수 있다.",
        "sections": {
            0: {"heading": "이 허브의 내용"},
            1: {"heading": "가이드 목록", "headers": ["가이드", "내용"]},
            2: {"heading": "최신 업데이트"},
        },
    },
    "fr": {
        "title": "Guide Hub de Moonlight Peaks",
        "metaTitle": "Moonlight Peaks : guide cadeaux, romance, pêche, fleurs et outils",
        "metaDescription": "Le hub de guides complet pour Moonlight Peaks : les 23 personnages romantiques et leurs cadeaux, les 22 poissons, toutes les fleurs, les améliorations d'outils, les 59 succès et la soluce — en 6 langues.",
        "intro": "Moonlight Peaks est un life-sim gothique cosy de Little Chicken, édité par XSEED Games et Marvelous Europe : cultivez des cultures mystiques la nuit, brassez des potions, pêchez sous la pleine lune et romancez loups-garous, sorcières et sirènes.",
        "sections": {
            0: {"heading": "Contenu de ce hub"},
            1: {"heading": "Index des guides", "headers": ["Guide", "Contenu"]},
            2: {"heading": "Dernières mises à jour"},
        },
    },
    "de": {
        "title": "Moonlight Peaks Guide-Hub",
        "metaTitle": "Moonlight Peaks: Geschenke, Romanzen, Angeln, Blumen und Werkzeuge",
        "metaDescription": "Der komplette Moonlight-Peaks-Guide-Hub: alle 23 romantischen Charaktere mit Geschenken, 22 Fische, alle Blumen, Werkzeug-Upgrades, 59 Erfolge und Komplettlösung — in 6 Sprachen.",
        "intro": "Moonlight Peaks ist ein gemütliches Gothic-Life-Sim von Little Chicken, veröffentlicht von XSEED Games und Marvelous Europe: Baue nachts mystische Pflanzen an, braue Tränke, angle bei Vollmond und verliebe dich in Werwölfe, Hexen und Meerjungfrauen.",
        "sections": {
            0: {"heading": "Was dieser Hub abdeckt"},
            1: {"heading": "Guide-Index", "headers": ["Guide", "Inhalt"]},
            2: {"heading": "Neueste Updates"},
        },
    },
})

# =====================================================================
# HOW TO PLAY
# =====================================================================
HTP_EN = {
    "slug": "moonlight-peaks/how-to-play",
    "title": "How to Play Moonlight Peaks",
    "metaTitle": "How to Play Moonlight Peaks: Core Loop, First Days & Money",
    "metaDescription": "New to Moonlight Peaks? Learn the night-farming loop, energy and mana, how to unlock fishing and magic, make money fast and avoid beginner mistakes.",
    "intro": "In Moonlight Peaks you play Dracula's child who moves to a sleepy gothic town to run a farm: plant mystical crops at night, brew potions, cast spells, fish, keep animals and build friendships — the town's story unlocks step by step as you settle in.",
    "sections": [
        S("The Daily Loop (Night Shift)", [
            ["Wake at dusk", "Each day runs through the night. Plan your energy (green bar) and mana (star symbols below it) before heading out."],
            ["Farm & forage", "Dig soil, plant seeds (assign them from your backpack), water crops and harvest. Glowy spiral tiles hide recipes and items when dug."],
            ["Talk to townsfolk", "Talking and giving one liked gift per day raises hearts. Many story quests start from letters and town conversations."],
            ["Fish, mine, catch bugs", "Fishing (from your second night), mining ore in caves and catching soul blobs with the bug net feed the museum and your wallet."],
            ["Ship and sell", "Chester the monster ships your products. Job-board requests and night sales are your best early income."],
        ]),
        S("Your First Three Days", [
            ["Day 1 — Orlock's Wine Scheme", "Pour water on the man outside your house, meet Viktor in the dome, plant Blood Grapes, craft a Keg (20 wood) and turn the grapes into Red Wine."],
            ["Day 2 — Meet the town", "Register at the Town Hall, meet the residents, and find Noel by the coast: complete his fishing challenge to keep the Fishing Rod (plus 250 Coins)."],
            ["Day 3 — Animals & storage", "Luna's letter unlocks farm creatures: buy a barn (4,000 Coins at Ridge's shop), then adopt Cheekens from Luna's farm."],
        ]),
        T(["System", "How it works"], [
            ["Energy", "Spent by every action; rest or eat to recover. Upgrade it with purchases at Webb of Wonders."],
            ["Mana", "Spent by spells. Restore it with Mana Potions or a Mana Extractor (from the 'Quest for Mana' chain)."],
            ["Heart levels", "One gift per character per day. Gifts they love give the biggest boost; disliked gifts barely count."],
            ["Shipments", "Chester ships products at night — watch for the sale-big achievement at 9,000+ Coins in one night."],
        ]),
        N("Beginner mistakes to avoid", [
            "Casting the fishing hook too close — fish get startled and flee. Cast at a distance, then reel in gently.",
            "Spending all your money before unlocking the barn (4,000 Coins) and the first tool upgrades.",
            "Ignoring the job board: simple requests earn coins and free items every day.",
            "Skipping the glowy spiral tiles — they hold recipes and useful items.",
        ]),
        F([
            ["When do I unlock fishing?", "On your second night, Noel challenges you near the coast ('Outfish The Fisherman'). Complete it to keep the Fishing Rod and earn 250 Coins."],
            ["When do I unlock magic?", "Complete 'The Magic of Crops' (a letter from Luna in Spring). Luna teaches you Aquaflux I and repairs your Fixed Wand."],
            ["How do I make money fast?", "Process raw materials (grapes → wine, milk → cheese), check the job board daily, and sell high-value fish like Armour (280 Coins)."],
            ["Can I play at my own pace?", "Yes — there are no strict time limits; the story advances by sleeping and visiting town."],
        ]),
    ],
}

HTP_I18N = {
    "zh-CN": {
        "title": "月光小镇 怎么玩",
        "metaTitle": "月光小镇怎么玩：核心循环·开局三天·赚钱",
        "metaDescription": "《月光小镇》新手入门：夜间种田核心循环、体力与魔力、钓鱼与魔法解锁、快速赚钱与常见误区。",
        "intro": "在《月光小镇》里，你扮演德古拉的孩子，搬进一座沉睡的哥特小镇经营农场：夜晚种植魔法作物、熬制药水、施法、钓鱼、饲养动物并结交朋友——小镇的故事会随你的安顿逐步展开。",
        "sections": {
            0: {"heading": "每日循环（夜班）", "items": [
                ["黄昏醒来", "每天从夜间开始。出门前规划体力（绿条）与魔力（其下的星标）。"],
                ["种田与采集", "翻地、播种（从背包分配到工具槽）、浇水、收获。发光的螺旋地砖能挖出配方与物品。"],
                ["与居民交谈", "每天交谈并赠送一件喜欢的礼物可提升心数。许多剧情任务由信件与对话触发。"],
                ["钓鱼·采矿·捕虫", "第二天晚上解锁钓鱼；洞穴采矿石；用捕虫网抓灵魂团——三者同时养博物馆与钱包。"],
                ["出货与售卖", "Chester 会在夜间帮你出货。任务板与夜间大额售卖是最早的收入来源。"],
            ]},
            1: {"heading": "开局三天", "items": [
                ["第一天 — Orlock 的葡萄酒计划", "给屋外的人浇水，去穹顶建筑找 Viktor，种下血葡萄，制作木桶（20 木材），把葡萄酿成红酒。"],
                ["第二天 — 逛小镇", "去市政厅登记、认识居民，并在海岸找到 Noel：完成钓鱼挑战即可保留鱼竿（另得 250 金币）。"],
                ["第三天 — 动物与储物", "Luna 来信解锁动物：在 Ridge 的店里买谷仓（4,000 金币），再去 Luna 的农场领养 Cheekens。"],
            ]},
            2: {"headers": ["系统", "机制"], "rows": [
                ["体力 Energy", "每个动作都会消耗；休息或进食恢复。可在 Webb of Wonders 购买上限提升。"],
                ["魔力 Mana", "施法消耗；用魔力药水或魔力萃取器恢复（来自“魔力任务”任务链）。"],
                ["心数 Heart", "每个角色每天只能送一次礼物；喜欢的礼物加成最大，讨厌的几乎不计。"],
                ["出货 Shipments", "Chester 夜间出货——一晚卖出 9,000+ 金币可触发大额售卖成就。"],
            ]},
            3: {"heading": "新手常见误区"},
            4: {},
        },
    },
}

HTP_I18N.update({
    "ja": {
        "title": "ムーンライトピークス の遊び方",
        "metaTitle": "ムーンライトピークスの遊び方：基本ループ・序盤3日・金策",
        "metaDescription": "『Moonlight Peaks』初心者向け：夜の農作業ループ、体力とマナ、釣りと魔法の解放、効率的な金策とよくある失敗を解説。",
        "intro": "『Moonlight Peaks』では、ドラキュラの子としてゴシックな田舎町に移り住み農場を営みます。夜に不思議な作物を育て、ポーションを作り、魔法を使い、釣りをし、動物を飼い、住民と交流。町の物語は少しずつ開かれていきます。",
        "sections": {
            0: {"heading": "1日の流れ（夜勤）", "items": [
                ["夕暮れに起床", "1日は夜から始まります。出かける前に体力（緑バー）とマナ（下の星）を計画しましょう。"],
                ["畑と採取", "土を掘り、種をまき（バックパックから道具スロットへ）、水をやり、収穫。光る渦巻きタイルを掘るとレシピやアイテム。"],
                ["住民と話す", "毎日会話と好きな贈り物1つでハートが上昇。多くのストーリークエストは手紙と会話から始まります。"],
                ["釣り・採掘・虫取り", "2日目の夜に釣り解禁。洞窟で鉱石、虫取り網でソウルブロブを捕獲。博物館と収入に。"],
                ["出荷と販売", "Chester が夜に商品を出荷。依頼板と夜の大口販売が序盤の稼ぎの中心。"],
            ]},
            1: {"heading": "最初の3日間", "items": [
                ["1日目 — Orlock のワイン計画", "家の外の男に水をかけ、ドームの Viktor に会い、Blood Grapes を植え、樽（木材20）を作り、赤ワインに。"],
                ["2日目 — 町を巡る", "タウンホールで登録し、住民に会い、海岸で Noel の釣りチャレンジをクリアして釣り竿を入手（+250コイン）。"],
                ["3日目 — 動物と保管庫", "Luna の手紙で動物が解放。Ridge の店で納屋（4,000コイン）を買い、Luna の農場で Cheekens を。"],
            ]},
            2: {"headers": ["システム", "仕組み"], "rows": [
                ["体力", "すべての行動で消費。休息か食事で回復。Webb of Wonders で上限を強化可能。"],
                ["マナ", "魔法で消費。マナポーションかマナ抽出器で回復（「Quest for Mana」で解放）。"],
                ["ハート", "キャラごとに1日1つの贈り物。大好物は最大、嫌いな物はほぼ増えません。"],
                ["出荷", "Chester が夜に出荷。一晩で9,000コイン以上売ると達成実績。"],
            ]},
            3: {"heading": "初心者がやりがちな失敗"},
        },
    },
    "ko": {
        "title": "문라이트 피크스 하는 법",
        "metaTitle": "문라이트 피크스 하는 법: 핵심 루프·첫 3일·돈 벌기",
        "metaDescription": "『문라이트 피크스』입문 가이드: 밤 농사 핵심 루프, 체력과 마나, 낚시·마법 해금, 빠른 돈벌이와 흔한 실수.",
        "intro": "『문라이트 피크스』에서 당신은 드라큘라의 자식으로 고딕풍 작은 마을에 이사 와 농장을 운영합니다. 밤에 신비한 작물을 키우고, 물약을 만들고, 마법을 쓰고, 낚시를 하고, 동물을 기르며 주민과 친해지면 마을의 이야기가 하나씩 열립니다.",
        "sections": {
            0: {"heading": "하루 루프(야간 근무)", "items": [
                ["해질녘에 기상", "하루는 밤부터 시작합니다. 나가기 전에 체력(초록 막대)과 마나(아래 별)를 계획하세요."],
                ["농사와 채집", "땅을 파고, 씨앗을 심고(가방에서 도구 칸으로), 물을 주고, 수확합니다. 빛나는 나선 타일을 파면 레시피와 아이템."],
                ["주민과 대화", "매일 대화와 좋아하는 선물 1개로 하트가 오릅니다. 많은 스토리 퀘스트는 편지와 대화로 시작됩니다."],
                ["낚시·채광·벌레", "둘째 날 밤 낚시 해금. 동굴에서 광석, 벌레망으로 소울 블롭을 잡아 박물관과 수입에."],
                ["출하와 판매", "Chester가 밤에 상품을 출하합니다. 게시판 의뢰와 밤 대량 판매가 초반 수입의 핵심."],
            ]},
            1: {"heading": "첫 3일", "items": [
                ["1일차 — Orlock의 와인 계획", "집 밖의 남자에게 물을 붓고, 돔 건물의 Viktor를 만나 Blood Grapes를 심고, 술통(나무 20)을 만들어 레드 와인으로."],
                ["2일차 — 마을 탐방", "타운홀에서 등록하고 주민들을 만나고, 해안의 Noel 낚시 도전을 클리어해 낚싯대 획득(+250코인)."],
                ["3일차 — 동물과 창고", "Luna의 편지로 동물 해금. Ridge 상점에서 헛간(4,000코인)을 사고 Luna 농장에서 Cheekens 입양."],
            ]},
            2: {"headers": ["시스템", "방식"], "rows": [
                ["체력", "모든 행동이 소모. 휴식이나 식사로 회복. Webb of Wonders에서 상한 증가."],
                ["마나", "마법이 소모. 마나 물약이나 마나 추출기로 회복('Quest for Mana' 연쇄 퀘스트)."],
                ["하트", "캐릭터당 하루 선물 1개. 좋아하는 선물이 가장 크고, 싫어하는 선물은 거의 안 오릅니다."],
                ["출하", "Chester가 밤에 출하. 한밤에 9,000코인 이상 판매하면 업적."],
            ]},
            3: {"heading": "초보자 흔한 실수"},
        },
    },
    "fr": {
        "title": "Comment jouer à Moonlight Peaks",
        "metaTitle": "Moonlight Peaks : boucle de jeu, premiers jours et argent",
        "metaDescription": "Débuter dans Moonlight Peaks : la boucle de jeu nocturne, l'énergie et le mana, débloquer pêche et magie, gagner de l'argent vite et éviter les erreurs de débutant.",
        "intro": "Dans Moonlight Peaks vous incarnez l'enfant de Dracula qui s'installe dans une ville gothique pour gérer une ferme : cultivez la nuit, brassez des potions, lancez des sorts, pêchez, élevez des animaux et tissez des liens — l'histoire de la ville se dévoile au fil de votre installation.",
        "sections": {
            0: {"heading": "La boucle quotidienne (service de nuit)", "items": [
                ["Réveil au crépuscule", "Chaque journée commence la nuit. Planifiez énergie (barre verte) et mana (étoiles) avant de sortir."],
                ["Cultiver et récolter", "Creusez, plantez (depuis le sac), arrosez, récoltez. Les tuiles spirales brillantes cachent recettes et objets."],
                ["Parler aux habitants", "Discuter et offrir un cadeau aimé par jour augmente les cœurs. Beaucoup de quêtes viennent de lettres et conversations."],
                ["Pêcher, miner, attraper", "Pêche dès la 2e nuit ; minez dans les grottes ; attrapez les Soul Blobs au filet. Tout nourrit le musée et vos finances."],
                ["Expédier et vendre", "Chester expédie vos produits la nuit. Le tableau des contrats et les grosses ventes nocturnes sont vos meilleurs revenus."],
            ]},
            1: {"heading": "Vos trois premiers jours", "items": [
                ["Jour 1 — Le vin d'Orlock", "Versez de l'eau sur l'homme devant chez vous, trouvez Viktor, plantez des Blood Grapes, fabriquez un tonneau (20 bois) et faites du vin rouge."],
                ["Jour 2 — Visitez la ville", "Inscrivez-vous à l'Hôtel de Ville, rencontrez les habitants et trouvez Noel : réussissez son défi de pêche pour garder la canne (+250 pièces)."],
                ["Jour 3 — Animaux et stockage", "La lettre de Luna débloque les animaux : achetez une grange (4 000 pièces chez Ridge) puis adoptez des Cheekens."],
            ]},
            2: {"headers": ["Système", "Fonctionnement"], "rows": [
                ["Énergie", "Chaque action en consomme ; repos ou nourriture. Augmentez-la chez Webb of Wonders."],
                ["Mana", "Consommé par les sorts ; restaurez-le avec des potions ou l'extracteur de mana (quête 'Quest for Mana')."],
                ["Cœurs", "Un cadeau par personnage et par jour. Les cadeaux aimés boostent ; les détestés comptent à peine."],
                ["Expéditions", "Chester expédie la nuit — l'exploit des 9 000+ pièces en une nuit."],
            ]},
            3: {"heading": "Erreurs de débutant à éviter"},
        },
    },
    "de": {
        "title": "Moonlight Peaks spielen",
        "metaTitle": "Moonlight Peaks: Spielablauf, erste Tage und Geld",
        "metaDescription": "Neu bei Moonlight Peaks? Lerne den Nachtanbau, Energie und Mana, wie du Angeln und Magie freischaltest, schnell Geld machst und Anfängerfehler vermeidest.",
        "intro": "In Moonlight Peaks spielst du Draculas Kind, das in eine schläfrige Gothic-Stadt zieht, um einen Bauernhof zu führen: Baue nachts mystische Pflanzen an, braue Tränke, wirke Zauber, angle, halte Tiere und knüpfe Freundschaften — die Stadtgeschichte öffnet sich Schritt für Schritt.",
        "sections": {
            0: {"heading": "Der Tagesablauf (Nachtschicht)", "items": [
                ["Im Dämmerlicht aufwachen", "Jeder Tag beginnt in der Nacht. Plane Energie (grüner Balken) und Mana (Sterne) vor dem Aufbruch."],
                ["Anbauen & Sammeln", "Boden graben, Samen pflanzen (aus dem Rucksack), gießen, ernten. Glühende Spiral-Fliesen verbergen Rezepte und Items."],
                ["Mit Bewohnern reden", "Täglich reden und ein gemochtes Geschenk geben erhöht Herzen. Viele Story-Quests starten per Brief und Gespräch."],
                ["Angeln, Erz, Insekten", "Angeln ab der zweiten Nacht; Erz in Höhlen; Soul Blobs mit dem Kescher — alles füllt Museum und Geldbeutel."],
                ["Versand & Verkauf", "Chester versendet nachts. Auftragsbrett und große Nachtverkäufe sind dein bestes frühes Einkommen."],
            ]},
            1: {"heading": "Deine ersten drei Tage", "items": [
                ["Tag 1 — Orlocks Weinplan", "Gieße Wasser über den Mann vor deinem Haus, triff Viktor, pflanze Blood Grapes, baue ein Fass (20 Holz) und mach Rotwein."],
                ["Tag 2 — Stadt erkunden", "Registriere dich im Rathaus, triff die Bewohner und finde Noel an der Küste: Schließe seine Angel-Herausforderung ab, um die Rute zu behalten (+250 Münzen)."],
                ["Tag 3 — Tiere & Lager", "Lunas Brief schaltet Tiere frei: Kaufe eine Scheune (4.000 Münzen bei Ridge) und adoptiere Cheekens von Lunas Hof."],
            ]},
            2: {"headers": ["System", "Funktionsweise"], "rows": [
                ["Energie", "Jede Aktion kostet Energie; Schlaf oder Essen regeneriert. Maximalwert bei Webb of Wonders kaufbar."],
                ["Mana", "Zauber kosten Mana; regeneriere mit Tränken oder dem Mana-Extraktor ('Quest for Mana')."],
                ["Herzen", "Ein Geschenk pro Charakter und Tag. Geliebte Geschenke geben am meisten; gehasste fast nichts."],
                ["Versand", "Chester verschickt nachts — der 9.000+-Münzen-Erfolg in einer Nacht."],
            ]},
            3: {"heading": "Anfängerfehler vermeiden"},
        },
    },
})

# =====================================================================
# GIFTS（全角色礼物表 · 核心差异化）
# 数据源：gamer.org 全表（L2）+ thegamer 部分（L2），G1/G2 已确认中文侧无全表
# =====================================================================
GIFT_ROWS_EN = [
    ["Orlock", "Red Rose, Red Wine, White Wine, Mana Wine", "Beer, Eggnog, Cupcakes, Irish Coffee", "Trash, Wood, Ore"],
    ["Jada", "Pink Azalea, Pink Plumeria, Yellow Azalea, Yellow Plumeria", "Coffee, Flowers, Dairy Products, Jam, Juice", "Magical Items, Gold Ingot"],
    ["Evan", "Black Tulips", "Coffee, Flat Cap, Flowers, Tea, Desserts", "Trash, Ore, Wood"],
    ["Sabrina", "Purple Flowers, Flower Pots, Mana Items", "Witch Hat, Diamond, Houseplants", "Trash, Ore, Fish"],
    ["Luna", "Any Flowers", "Flower Pots, Houseplants, Mana Items, Juices", "Trash, Wood, Ore"],
    ["Samael", "Red Rose, Red Wine, White Wine, Poppies", "Diamond, Flowers, Gold Ingot, Mana Items", "Pink Flowers, Trash"],
    ["Fiona", "White Tulips", "Witch Hat, Mana Essence, Desserts, Jam", "Trash, Ore, Wood"],
    ["Mina", "Pink Flowers, Red Rose", "Flower Pots, Houseplants, Dairy Products", "Fish Dishes, Trash"],
    ["Dragan", "Purple Moonlight Flower, Blue Moonlight Flower", "Moon Crystal, Void Items, Hats", "Trash, Ore, Wood"],
    ["Winston", "Blue Azalea", "Other Flowers, Flower Pots, Soups, Juices", "Trash, Ore, Shells"],
    ["Alina", "Black Rose, Black Tulips, Black Azalea, Black Plumeria", "Diamond, Golden Egg, Blue and Yellow Flowers", "Trash, Fish, Wood"],
    ["Saga", "Purple Chthonia, Blue Chthonia, Moonlight Flowers", "Tea, Golden Egg, Diamond, Jam, Wine", "Trash, Wood, Ore"],
    ["Kim", "Pink and White Flowers", "Black, Red and Purple Flowers, Coffee", "Trash, Wood, Ore"],
    ["Llemi", "Pink Plumeria, Gold Ingot, Custom Bouquet", "Cupid, Heartstone, Rose Quartz", "Black Flowers, Trash"],
    ["Rei", "Yellow Flowers", "Flower Pots, Houseplants, Juices", "Honey, Trash"],
    ["Persephone", "Any Flowers", "Houseplants, Coffee, Rose Quartz, Soups", "Fish, Trash"],
    ["Noel", "Mana Coffee, Mana Wine, Mana Potion", "Mana Chocolate, Mana Moon Cupcake, Diamond", "Fish, Trash"],
    ["Ludo", "Black Flowers", "Flower Pots, Pizza, Coffee, Jam", "Trash, Ore"],
    ["Brooke", "White Rose, Top Hat", "Dairy Products, Juices, Hats", "Trash, Ore, Fish"],
    ["Te", "Pink Flowers", "Flower Pots, Accessories, Coffee, Jam", "Trash, Ore"],
    ["Pumpkin Head", "Pumpkin, Pumpkin Dishes", "Honey, Juices, Milkshakes", "Trash, Ore"],
    ["Aras", "Purple Moonlight Flower, Blue Moonlight Flower", "Diamond, Golden Egg, Black and Blue Flowers", "Hats, Clothing, Trash"],
    ["Moon Goddess", "Blue Moonlight Flower", "Purple Moonlight Flower, Mana Moon Cupcake", "Trash, Wood, Ore"],
    ["Skull Girl", "Any Flowers", "Insects, Houseplants, Food, Clothing", "Trash, Ore"],
    ["Spine", "Blue Flowers", "Flower Pots, Beer, Jam, Wine", "Trash, Fish, Insects"],
    ["Elvira", "Red Rose", "Diamond, Formal Hat, Gold Ingot", "Trash, Ore, Wood"],
    ["Death", "Any Trash", "Any Hats, Eggnog, Eggs, Bread", "Diamond, Golden Egg, Fertilizer"],
]
GIFT_I18N_HEADERS = {
    "zh-CN": ["角色", "最爱礼物", "喜欢礼物", "讨厌礼物"],
    "ja": ["キャラクター", "大好物", "好物", "嫌いな物"],
    "ko": ["캐릭터", "최애 선물", "좋아하는 선물", "싫어하는 선물"],
    "fr": ["Personnage", "Cadeaux adorés", "Cadeaux aimés", "Cadeaux détestés"],
    "de": ["Charakter", "Geliebte Geschenke", "Gemochte Geschenke", "Gehasste Geschenke"],
}
GIFTS_EN = {
    "slug": "moonlight-peaks/gifts",
    "title": "Moonlight Peaks Gift Guide: All Characters",
    "metaTitle": "All Moonlight Peaks Gifts: Loved, Liked & Hated for Every Character",
    "metaDescription": "Every character's gift preferences in Moonlight Peaks: loved, liked and hated gifts for all 23 romanceable characters and key NPCs — searchable and sortable.",
    "intro": "Giving characters gifts they love is the fastest way to raise hearts in Moonlight Peaks. Every resident has four gift tiers — Loved, Liked, Neutral and Disliked. This is the complete gift table we've verified from multiple sources; anything still being confirmed is marked below.",
    "sections": [
        M("Gift tiers: Loved gifts give the biggest friendship boost, Liked gifts a solid boost, Neutral gifts only a little, and Disliked gifts barely count and can trigger a negative reaction. You can give one gift per character per day."),
        T(["Character", "Loved Gifts", "Liked Gifts", "Disliked Gifts"], GIFT_ROWS_EN, tag="DATA", heading="Complete Gift Table (27 residents)"),
        N("Fast friendship tips", [
            "Flowers are the most versatile gift in the game — many residents love or like them.",
            "Rare flowers (Moonlight Flowers, Black Tulips, Blue Moonlight Flower) are the most valuable for specific characters.",
            "Talk to everyone daily and finish their requests on top of gifting for the fastest heart growth.",
        ]),
        F([
            ["How does the gift system work?", "Each character has four tiers: Loved (largest boost), Liked (solid boost), Neutral (small), Disliked (tiny or negative). One gift per character per day."],
            ["What's the best universal gift?", "Flowers. Luna loves any flower, and most residents at least like them. Rare colored flowers cover even more characters."],
            ["Do disliked gifts hurt the relationship?", "They barely count and can trigger a negative response — avoid the items listed in the Disliked column."],
        ]),
    ],
}

GIFTS_I18N = {
    "zh-CN": {
        "title": "月光小镇 礼物全表",
        "metaTitle": "月光小镇礼物全表：全部角色 喜欢/讨厌 礼物",
        "metaDescription": "《月光小镇》全部角色礼物偏好：23 位可攻略角色与关键 NPC 的 最爱/喜欢/讨厌 礼物，可搜索可筛选。",
        "intro": "送出对方喜爱的礼物是《月光小镇》提升心数最快的方式。每位居民有四档礼物偏好：最爱、喜欢、一般、讨厌。下表为多来源核对后的完整礼物表；仍在核对的会标注。",
        "sections": {
            0: {"body": "礼物分档：最爱礼物 好感加成最大；喜欢礼物 加成可观；一般礼物 只有少量；讨厌礼物 几乎不计且可能引发负面反应。每个角色每天只能送一次礼物。"},
            1: {"heading": "完整礼物表（27 位居民）", "headers": GIFT_I18N_HEADERS["zh-CN"]},
            2: {"heading": "快速提升好感技巧"},
            3: {},
        },
    },
    "ja": {
        "title": "ムーンライトピークス 贈り物ガイド",
        "metaTitle": "全キャラの贈り物：大好物・好物・嫌いな物",
        "metaDescription": "『Moonlight Peaks』全キャラの贈り物：恋愛対象23人と主要NPCの大好物・好物・嫌いな物を一覧に。",
        "intro": "好きな贈り物を渡すのがハートを上げる最短ルート。住民ごとに大好物・好物・普通・嫌いの4段階。複数ソースで検証した完全な表です。",
        "sections": {
            0: {"body": "贈り物の段階：大好物=最大、好物=しっかり、普通=少し、嫌い=ほぼ増えずマイナス反応も。キャラごとに1日1個まで。"},
            1: {"heading": "完全な贈り物表（27人）", "headers": GIFT_I18N_HEADERS["ja"]},
            2: {"heading": "好感度を早く上げるコツ"},
        },
    },
    "ko": {
        "title": "문라이트 피크스 선물 가이드",
        "metaTitle": "전체 캐릭터 선물: 최애·좋아함·싫어함",
        "metaDescription": "『문라이트 피크스』전체 캐릭터 선물: 연애 대상 23명과 주요 NPC의 최애·좋아함·싫어함 선물 목록.",
        "intro": "좋아하는 선물을 주는 것이 하트를 올리는 가장 빠른 길입니다. 주민마다 최애·좋아함·보통·싫어함 4단계가 있으며, 여러 출처로 검증한 완전한 표입니다.",
        "sections": {
            0: {"body": "선물 단계: 최애=최대 상승, 좋아함=확실한 상승, 보통=약간, 싫어함=거의 없음+부정 반응. 캐릭터당 하루 1개."},
            1: {"heading": "전체 선물 표(주민 27명)", "headers": GIFT_I18N_HEADERS["ko"]},
            2: {"heading": "호감도 빨리 올리는 팁"},
        },
    },
    "fr": {
        "title": "Guide des cadeaux de Moonlight Peaks",
        "metaTitle": "Tous les cadeaux : adorés, aimés et détestés pour chaque personnage",
        "metaDescription": "Les préférences de cadeaux de chaque personnage de Moonlight Peaks : adorés, aimés et détestés pour les 23 romances et PNJ clés.",
        "intro": "Offrir des cadeaux adorés est le moyen le plus rapide d'augmenter les cœurs. Chaque habitant a quatre niveaux — adoré, aimé, neutre, détesté. Voici le tableau complet, vérifié sur plusieurs sources.",
        "sections": {
            0: {"body": "Niveaux : adoré = plus gros gain, aimé = gain solide, neutre = petit, détesté = quasi nul et réaction négative possible. Un cadeau par personnage et par jour."},
            1: {"heading": "Tableau complet des cadeaux (27 habitants)", "headers": GIFT_I18N_HEADERS["fr"]},
            2: {"heading": "Astuces pour monter l'amitié vite"},
        },
    },
    "de": {
        "title": "Geschenke-Guide für Moonlight Peaks",
        "metaTitle": "Alle Geschenke: geliebt, gemocht und gehasst für jeden Charakter",
        "metaDescription": "Jeder Charakter in Moonlight Peaks und seine Geschenk-Vorlieben: geliebt, gemocht und gehasst für alle 23 Liebesoptionen und wichtige NPCs.",
        "intro": "Geliebte Geschenke zu geben, erhöht Herzen am schnellsten. Jeder Bewohner hat vier Stufen — geliebt, gemocht, neutral, gehasst. Die komplette, aus mehreren Quellen verifizierte Tabelle.",
        "sections": {
            0: {"body": "Stufen: geliebt = größter Zuwachs, gemocht = solider Zuwachs, neutral = wenig, gehasst = fast nichts plus mögliche negative Reaktion. Ein Geschenk pro Charakter und Tag."},
            1: {"heading": "Komplette Geschenke-Tabelle (27 Bewohner)", "headers": GIFT_I18N_HEADERS["de"]},
            2: {"heading": "Tipps für schnelle Freundschaft"},
        },
    },
}

# =====================================================================
# ROMANCE（23 可攻略角色 · bonus-action L2）
# =====================================================================
ROMANCE_ROWS = [
    ["Fiona", "Witch", "Spring 1 Year 1", "Aloof and uninterested at first; feuds with Orlock but hides a deeper story."],
    ["Noel", "Witch", "Spring 1 Year 1", "Arrogant, self-interested, prefers fishing — his haughty side hides insecurities."],
    ["Sabrina", "Witch", "Spring 1 Year 1", "Dedicated witch, clever, sometimes overwhelmed by her family."],
    ["Luna", "Witch", "Spring 1 Year 1", "Enigmatic, spends time in her garden; knows a lot about magic."],
    ["Orlock", "Vampire", "Spring 1 Year 1", "Haunted vampire with an alcohol problem; a romantic, raw side blooms as he recovers."],
    ["Evan", "Vampire", "Spring 1 Year 1", "Orlock's laid-back child; struggles with how Orlock has spiraled."],
    ["Mina", "Vampire", "Spring 1 Year 1", "Bright, excitable, Orlock's other child and Evan's sister; worries about her family."],
    ["Samael", "Vampire", "Spring 1 Year 1", "Orlock's nephew; dark, mysterious and kind."],
    ["Elvira", "Vampire", "Spring 1 Year 1", "Spirited and motivated; always organizing social gatherings."],
    ["Persephone", "Human", "Summer 24 Year 1", "Curious human who moved in with her niece and nephew."],
    ["Jada", "Human", "With Persephone's quests", "Intense relic collector; unlocks later in the game."],
    ["Winston", "Human", "With Persephone's quests", "Terrified of supernaturals; his arc is about facing fears."],
    ["Saga", "Werewolf", "Spring 1 Year 1", "Trying to ease the feud between Orlock and her father Brook."],
    ["Ridge", "Werewolf", "Spring 1 Year 1", "Brook's laid-back brother; runs the Howling Hammer, father of Ludo."],
    ["Ludo", "Werewolf", "Spring 1 Year 1", "Carefree prankster always in trouble with Brook."],
    ["Dragan", "Seer", "Spring 1 Year 1", "Struggles with visions; perfects his card game (Nokturna)."],
    ["Alina", "Seer", "Spring 1 Year 1", "Intense and passionate; little patience for Dragan."],
    ["Aras", "Seer", "Spring 1 Year 1", "Runs the fashion store Third Eye Threads; kind and soft-spoken."],
    ["Death", "Supernatural", "Story progression", "Tired of the job; caring once you help."],
    ["Llemi", "Supernatural", "Spring before Lovage festival", "A love demon; memorable every interaction."],
    ["Kim", "Mermaid", "Hidden (TBA)", "Secret romance candidate."],
    ["Tae", "Mermaid", "Hidden (TBA)", "Secret romance candidate."],
    ["Rei", "Mermaid", "Hidden (TBA)", "Secret romance candidate."],
]
ROMANCE_EN = {
    "slug": "moonlight-peaks/romance",
    "title": "Moonlight Peaks Romance Guide: All 23 Characters",
    "metaTitle": "All 23 Romanceable Characters in Moonlight Peaks (+ How Dating Works)",
    "metaDescription": "Every romanceable character in Moonlight Peaks: 23 bachelors, bachelorettes and more, with affiliations, when they appear, dating at heart level 4, marriage and vampire conversion.",
    "intro": "Moonlight Peaks lets you date multiple townsfolk at once and marry one of them. There are 23 romanceable characters at launch — witches, vampires, werewolves, seers, humans, mermaids and stranger beings. Here is everyone, who they are, and how dating works.",
    "sections": [
        T(["Character", "Affiliation", "When they appear", "Personality"], ROMANCE_ROWS, heading="All 23 Romanceable Characters"),
        S("How dating works", [
            ["Heart Level 4", "The option to date unlocks at heart level 4. Talk daily and give one liked or loved gift per day."],
            ["Dates", "Invite a character on a date and play dating minigames. Dates can fail — follow the instructions and arrive on time or you lose friendship points."],
            ["Marriage", "You can propose to your partner and marry. You can't marry more than one character."],
            ["Children", "No children mechanic, and none planned. Marrying older characters like Ridge or Orlock can make you a step-parent to their existing kids."],
            ["Vampire conversion", "You can turn your partner into a vampire (mechanic not fully verified — marked 待补)."],
        ]),
        N("Portrait styles (Switch)", [
            "Open the main menu with the '+' button on Nintendo Switch.",
            "Enter Settings → Portrait Style at the bottom of the Gameplay menu.",
            "Choose between style 1 (cartoon with realistic shading) and style 2 (anime-inspired, cute and bubbly).",
        ]),
        F([
            ["Can you date multiple characters?", "Yes — you can date several townsfolk at once, but you can only marry one."],
            ["When can I start dating?", "Dating unlocks at Heart Level 4 with that character."],
            ["Can I have children?", "No — there is no children mechanic and none is planned."],
            ["Who are the secret romance candidates?", "Kim, Tae and Rei (mermaids) appear after hidden requirements; details are marked TBA by sources."],
        ]),
    ],
}

ROMANCE_I18N = {
    "zh-CN": {
        "title": "月光小镇 恋爱指南：23 位可攻略角色",
        "metaTitle": "月光小镇可攻略角色大全：23 位恋爱对象",
        "metaDescription": "《月光小镇》23 位可攻略角色全览：种族、登场时间、性格、心数 4 级约会、结婚与转化为吸血鬼机制。",
        "intro": "《月光小镇》允许你同时与多位居民约会，最终与其中一位结婚。首发共 23 位可攻略角色——女巫、吸血鬼、狼人、先知、人类、人鱼甚至更奇特的种族。这里列出全部角色与恋爱机制。",
        "sections": {
            0: {"heading": "23 位可攻略角色", "headers": ["角色", "种族", "登场时间", "性格"]},
            1: {"heading": "恋爱机制", "items": [
                ["心数 4 级", "心数达到 4 级解锁约会选项。每天交谈并送一件喜欢或最爱的礼物。"],
                ["约会", "邀请角色约会并参与约会小游戏。约会可能失败——按提示操作并准时赴约，否则会损失好感。"],
                ["结婚", "可以向伴侣求婚并结婚，但不能同时与多人结婚。"],
                ["子嗣", "没有子嗣机制，官方暂无计划。与 Ridge 或 Orlock 等较年长角色结婚可成为其现有孩子的继父/母。"],
                ["转化为吸血鬼", "可以把伴侣转化为吸血鬼（该机制尚未完全核实，标注待补）。"],
            ]},
            2: {"heading": "立绘风格（Switch）"},
            3: {},
        },
    },
    "ja": {
        "title": "ムーンライトピークス 恋愛ガイド",
        "metaTitle": "恋愛対象23人とデートの仕組み",
        "metaDescription": "『Moonlight Peaks』の恋愛対象23人：種族・登場時期・性格、ハート4でデート、結婚、吸血鬼化。",
        "intro": "同時に複数の住民とデートでき、最終的に1人と結婚できます。発売時点で恋愛対象は23人。魔女、吸血鬼、狼人、予言者、人間、人魚、そしてもっと不思議な存在まで。",
        "sections": {
            0: {"heading": "恋愛対象23人", "headers": ["キャラクター", "種族", "登場時期", "性格"]},
            1: {"heading": "デートの仕組み", "items": [
                ["ハートレベル4", "ハート4でデート可能に。毎日会話と好物を1つ。"],
                ["デート", "誘ってデートミニゲームを。失敗あり — 指示に従い時間通りに。失敗で好感度減少。"],
                ["結婚", "プロポーズして結婚可能。複数人とは結婚できません。"],
                ["子供", "子供システムはなく、予定もなし。Ridge や Orlock など年長キャラと結婚すると既存の子の継親に。"],
                ["吸血鬼化", "パートナーを吸血鬼にできる（仕組みは未検証 — 待補）。"],
            ]},
            2: {"heading": "ポートレート設定（Switch）"},
        },
    },
    "ko": {
        "title": "문라이트 피크스 연애 가이드",
        "metaTitle": "연애 가능 캐릭터 23명과 데이트 방식",
        "metaDescription": "『문라이트 피크스』연애 대상 23명: 종족·등장 시기·성격, 하트 4레벨 데이트, 결혼, 뱀파이어 전환.",
        "intro": "여러 주민과 동시에 데이트하고, 마지막에는 한 명과 결혼할 수 있습니다. 출시 기준 연애 대상 23명 — 마녀, 뱀파이어, 늑대인간, 예언자, 인간, 인어, 그리고 더 이상한 존재까지.",
        "sections": {
            0: {"heading": "연애 대상 23명", "headers": ["캐릭터", "종족", "등장 시기", "성격"]},
            1: {"heading": "데이트 방식", "items": [
                ["하트 레벨 4", "하트 4에서 데이트 해금. 매일 대화 + 좋아하는 선물 1개."],
                ["데이트", "초대해 데이트 미니게임. 실패 가능 — 지시를 따르고 제시간에 도착해야 함. 실패 시 호감도 감소."],
                ["결혼", "프로포즈로 결혼 가능. 한 번에 한 명만."],
                ["자녀", "자녀 시스템 없음, 계획도 없음. Ridge나 Orlock 같은 연장자와 결혼하면 기존 자녀의 계부모가 됩니다."],
                ["뱀파이어 전환", "파트너를 뱀파이어로 만들 수 있음(미검증 — 대기)."],
            ]},
            2: {"heading": "초상화 설정(Switch)"},
        },
    },
    "fr": {
        "title": "Guide romance de Moonlight Peaks",
        "metaTitle": "Les 23 personnages romantiques et le fonctionnement des rendez-vous",
        "metaDescription": "Tous les personnages romantiques de Moonlight Peaks : 23 options avec affiliations, apparition, rendez-vous au niveau de cœur 4, mariage et conversion en vampire.",
        "intro": "Moonlight Peaks permet de sortir avec plusieurs habitants à la fois et d'en épouser un. 23 personnages romantiques au lancement — sorcières, vampires, loups-garous, voyants, humains, sirènes et bien plus.",
        "sections": {
            0: {"heading": "Les 23 personnages romantiques", "headers": ["Personnage", "Affiliation", "Apparition", "Personnalité"]},
            1: {"heading": "Comment fonctionnent les rendez-vous", "items": [
                ["Niveau de cœur 4", "Le rendez-vous se débloque au niveau de cœur 4. Parlez chaque jour et offrez un cadeau aimé/adoré."],
                ["Rendez-vous", "Invitez et jouez aux mini-jeux. Ils peuvent échouer — suivez les consignes et arrivez à l'heure."],
                ["Mariage", "Vous pouvez proposer et vous marier, mais pas avec plusieurs."],
                ["Enfants", "Aucun mécanisme d'enfants et aucun prévu. Épouser Ridge ou Orlock permet d'être beau-parent."],
                ["Conversion", "Vous pouvez transformer votre partenaire en vampire (non vérifié — à compléter)."],
            ]},
            2: {"heading": "Styles de portrait (Switch)"},
        },
    },
    "de": {
        "title": "Romantik-Guide für Moonlight Peaks",
        "metaTitle": "Alle 23 Liebesoptionen und wie Dating funktioniert",
        "metaDescription": "Alle romantischen Charaktere in Moonlight Peaks: 23 Optionen mit Zugehörigkeit, Auftreten, Dating ab Herz-Stufe 4, Heirat und Vampir-Wandlung.",
        "intro": "In Moonlight Peaks kannst du mit mehreren Bewohnern gleichzeitig ausgehen und einen heiraten. 23 romantische Charaktere zum Start — Hexen, Vampire, Werwölfe, Seher, Menschen, Meerjungfrauen und Seltsameres.",
        "sections": {
            0: {"heading": "Die 23 Liebesoptionen", "headers": ["Charakter", "Zugehörigkeit", "Auftreten", "Persönlichkeit"]},
            1: {"heading": "So funktioniert Dating", "items": [
                ["Herz-Stufe 4", "Dating wird ab Herz-Stufe 4 freigeschaltet. Täglich reden und ein gemochtes/geliebtes Geschenk geben."],
                ["Dates", "Lade ein und spiele Dating-Minispiele. Sie können scheitern — Anweisungen folgen und pünktlich sein."],
                ["Heirat", "Du kannst heiraten, aber nur eine Person."],
                ["Kinder", "Kein Kinder-Mechanik und keine geplant. Heirate Ridge oder Orlock, um Stiefeltern zu werden."],
                ["Wandlung", "Du kannst deinen Partner in einen Vampir verwandeln (nicht verifiziert — offen)."],
            ]},
            2: {"heading": "Porträt-Stile (Switch)"},
        },
    },
}

# =====================================================================
# FISHING（22 鱼 · sportsrant/thegamer/gamewatcher/IGN 合并；4 种待补）
# =====================================================================
FISH_ROWS = [
    ["Whisper", "Common", "Most water (not Silverveil Lake)", "All seasons / any time / any weather", "Any rod", "6", "40"],
    ["Splotch", "Common", "Silverveil Lake", "All seasons / any time", "Any rod", "6", "55"],
    ["Violet", "Uncommon", "Moonlit Pines River", "All seasons / any time", "Any rod", "8", "65"],
    ["Glibby", "Uncommon", "Rivers near Silverveil / your farm", "All seasons / any time", "Any rod", "8", "65"],
    ["Orbis", "Uncommon", "Silverveil Lake", "All seasons / any time", "Any rod", "8", "75"],
    ["Goldy", "Uncommon", "Rivers near Silverveil / farm / Misty Shores", "Spring & Summer only", "Any rod", "8", "50"],
    ["Mouthout", "Uncommon", "Silverveil Lake / Misty Shores", "Rain only", "Any rod", "8", "100"],
    ["Brickle", "Uncommon", "Howling Marshes", "All seasons / any time", "Any rod", "8", "80"],
    ["Leftsee", "Uncommon", "Underground / Cave of Echoes / Crystal Cave", "All seasons / any time", "Any rod", "8", "140"],
    ["Skullfin", "Rare", "Underground / Cave of Echoes / Crystal Cave", "All seasons / any time", "Any rod", "—", "待补"],
    ["Twilight", "Uncommon", "Luna Bay", "Early evening", "Any rod", "—", "待补"],
    ["Moonflutter", "Rare", "Luna Bay", "Full Moon only", "Any rod", "—", "待补"],
    ["Furybud", "Rare", "Luna Bay", "Large fish", "Premium rod", "—", "待补"],
    ["Goliath", "Rare", "Moonlit Pines River", "Large fish", "Premium rod", "—", "待补"],
    ["Amour", "Uncommon", "Pink Grove", "All seasons / any time", "Any rod", "—", "待补"],
    ["Glammer", "Uncommon", "Pink Grove", "All seasons / any time", "Any rod", "—", "待补"],
    ["Armour", "Rare", "Pink Grove", "Large fish", "Premium rod", "8", "280"],
    ["Missing", "Super Rare", "Any fishing spot", "Any", "Any rod", "—", "待补"],
    ["4 more species", "—", "待补", "待补", "待补", "—", "待补"],
]
FISH_EN = {
    "slug": "moonlight-peaks/fishing",
    "title": "Moonlight Peaks Fishing Guide: All Fish & Locations",
    "metaTitle": "All 22 Fish in Moonlight Peaks: Locations, Seasons, Weather & Rods",
    "metaDescription": "Every fish in Moonlight Peaks: locations, seasons, weather and moon-phase conditions, rod requirements, energy and value — plus how to unlock fishing and rod upgrades.",
    "intro": "Moonlight Peaks has 22 fish species. Many only appear in specific locations, seasons, weather or moon phases — a few are full-moon exclusives. This guide lists every fish we've verified, how to unlock fishing, and how to upgrade your rod.",
    "sections": [
        S("How to unlock fishing", [
            ["Second night", "Cross the bridge near your home to the beach and meet Noel."],
            ["The challenge", "He challenges you to catch three different species ('Outfish The Fisherman')."],
            ["Reward", "Complete it to keep the Fishing Rod permanently plus 250 Coins."],
        ]),
        T(["Fish", "Rarity", "Location", "Condition", "Rod", "Energy", "Value"], FISH_ROWS, heading="Moonlight Peaks Fish List (22 total; 4 still 待补)"),
        T(["Rod", "Cost", "What it catches"], [
            ["Fishing Rod", "Free (Noel's quest)", "Small fish only."],
            ["Premium Fishing Rod", "16,000 Coins + 1x Fishing Rod + 3x Gold Bar", "Catches both Large and Small fish."],
            ["Enchanted Fishing Rod", "待补", "Catches every fish and removes the energy cost of fishing (per community reports)."],
        ], heading="Rod Upgrades (bought at Ridge's Howling Hammer)"),
        N("Fishing tips", [
            "Fish in every season and weather — some species are time-specific (Goldy: Spring/Summer; Mouthout: rain only).",
            "Return on Full Moon nights to Luna Bay for Moonflutter.",
            "Upgrade to the Premium Rod early for the large fish (Furybud, Goliath, Armour).",
            "Donate one of every species to the Museum Aquarium Collection.",
            "The Howling Hammer is open Monday–Friday 18:00–00:00.",
        ]),
        F([
            ["When do I get the fishing rod?", "On your second night, complete Noel's fishing challenge by the beach to keep the rod (+250 Coins)."],
            ["Which fish needs a full moon?", "Moonflutter only appears during a Full Moon at Luna Bay."],
            ["Which fish need the Premium rod?", "Furybud, Goliath and Armour are large fish that need the Premium Fishing Rod."],
            ["What is 'Missing'?", "A super-rare fish that can appear at any fishing spot — catching it unlocks the 'Missing? No!' achievement."],
        ]),
    ],
}

FISH_I18N = {
    "zh-CN": {
        "title": "月光小镇 钓鱼图鉴",
        "metaTitle": "月光小镇钓鱼图鉴：22 种鱼位置·季节·满月",
        "metaDescription": "《月光小镇》全部 22 种鱼：钓点、季节、天气与月相条件、鱼竿要求、能量与售价，含解锁钓鱼与鱼竿升级。",
        "intro": "《月光小镇》共有 22 种鱼，许多只在特定地点、季节、天气或月相出现——其中一些是满月专属。本页列出已核实的全部鱼类、钓鱼解锁方式与鱼竿升级。",
        "sections": {
            0: {"heading": "如何解锁钓鱼", "items": [
                ["第二天晚上", "跨过家附近的桥到海滩，找到 Noel。"],
                ["挑战", "他要求你钓上三种不同的鱼（任务“Outfish The Fisherman”）。"],
                ["奖励", "完成后永久保留鱼竿，并获得 250 金币。"],
            ]},
            1: {"heading": "鱼类全表（共 22 种；4 种待补）", "headers": ["鱼", "稀有度", "钓点", "条件", "鱼竿", "体力", "售价"]},
            2: {"heading": "鱼竿升级（Ridge 的 Howling Hammer 购买）", "headers": ["鱼竿", "价格", "可钓"]},
            3: {"heading": "钓鱼技巧"},
            4: {},
        },
    },
    "ja": {
        "title": "ムーンライトピークス 釣りガイド",
        "metaTitle": "全22種の魚：場所・季節・天気・釣り竿",
        "metaDescription": "『Moonlight Peaks』の魚22種：場所、季節、天気、月相条件、竿の必要、体力と売値を解説。釣りの解放と竿強化も。",
        "intro": "魚は22種。多くは特定の場所・季節・天気・月相でのみ出現し、満月限定も。検証済みの全魚、釣りの解放、竿強化をまとめました。",
        "sections": {
            0: {"heading": "釣りの解放方法", "items": [
                ["2日目の夜", "家の近くの橋を渡って浜辺へ、Noel に会う。"],
                ["チャレンジ", "3種の魚を釣るチャレンジ（「Outfish The Fisherman」）。"],
                ["報酬", "クリアで釣り竿を永久入手 +250コイン。"],
            ]},
            1: {"heading": "魚リスト（全22種、4種は待補）", "headers": ["魚", "レア度", "場所", "条件", "竿", "体力", "売値"]},
            2: {"heading": "釣り竿強化（Ridge の Howling Hammer）", "headers": ["竿", "費用", "釣れるもの"]},
            3: {"heading": "釣りのコツ"},
        },
    },
    "ko": {
        "title": "문라이트 피크스 낚시 가이드",
        "metaTitle": "물고기 22종: 위치·계절·날씨·낚싯대",
        "metaDescription": "『문라이트 피크스』물고기 22종: 장소, 계절, 날씨, 달의 조건, 낚싯대 요구, 에너지와 판매가. 낚시 해금과 낚싯대 강화 포함.",
        "intro": "물고기는 총 22종. 많은 종이 특정 장소·계절·날씨·달의 조건에서만 나오며, 보름달 전용도 있습니다. 검증된 전체 어종과 낚시 해금, 낚싯대 강화를 정리했습니다.",
        "sections": {
            0: {"heading": "낚시 해금 방법", "items": [
                ["둘째 날 밤", "집 근처 다리를 건너 해변에서 Noel을 만나세요."],
                ["도전", "물고기 3종을 낚는 도전('Outfish The Fisherman')."],
                ["보상", "클리어하면 낚싯대 영구 획득 +250코인."],
            ]},
            1: {"heading": "어종 목록(총 22종, 4종 대기)", "headers": ["물고기", "희귀도", "장소", "조건", "낚싯대", "에너지", "판매가"]},
            2: {"heading": "낚싯대 강화(Ridge의 Howling Hammer)", "headers": ["낚싯대", "비용", "잡히는 것"]},
            3: {"heading": "낚시 팁"},
        },
    },
    "fr": {
        "title": "Guide de pêche de Moonlight Peaks",
        "metaTitle": "Les 22 poissons : lieux, saisons, météo et cannes",
        "metaDescription": "Tous les poissons de Moonlight Peaks : lieux, saisons, météo et phases de lune, canne requise, énergie et valeur — plus le déblocage et les améliorations.",
        "intro": "Moonlight Peaks compte 22 espèces. Beaucoup n'apparaissent qu'à certains endroits, saisons, météos ou phases lunaires — certaines exclusives à la pleine lune. Voici tous les poissons vérifiés, le déblocage et les cannes.",
        "sections": {
            0: {"heading": "Débloquer la pêche", "items": [
                ["2e nuit", "Traversez le pont près de chez vous vers la plage et trouvez Noel."],
                ["Le défi", "Il vous défie d'attraper trois espèces ('Outfish The Fisherman')."],
                ["Récompense", "Gardez la canne à pêche définitivement +250 pièces."],
            ]},
            1: {"heading": "Liste des poissons (22 au total, 4 à compléter)", "headers": ["Poisson", "Rareté", "Lieu", "Condition", "Canne", "Énergie", "Valeur"]},
            2: {"heading": "Améliorations de canne (Howling Hammer de Ridge)", "headers": ["Canne", "Coût", "Ce qu'elle attrape"]},
            3: {"heading": "Conseils de pêche"},
        },
    },
    "de": {
        "title": "Angel-Guide für Moonlight Peaks",
        "metaTitle": "Alle 22 Fische: Orte, Jahreszeiten, Wetter und Ruten",
        "metaDescription": "Jeder Fisch in Moonlight Peaks: Orte, Jahreszeiten, Wetter und Mondphasen, Ruten-Anforderungen, Energie und Wert — plus Freischalten und Ruten-Upgrades.",
        "intro": "Moonlight Peaks hat 22 Fischarten. Viele erscheinen nur an bestimmten Orten, Jahreszeiten, Wettern oder Mondphasen — einige nur bei Vollmond. Hier sind alle verifizierten Fische, das Freischalten und die Ruten-Upgrades.",
        "sections": {
            0: {"heading": "Angeln freischalten", "items": [
                ["Zweite Nacht", "Überquere die Brücke zum Strand und triff Noel."],
                ["Die Herausforderung", "Er fordert dich heraus, drei Arten zu fangen ('Outfish The Fisherman')."],
                ["Belohnung", "Behalte die Angelrute dauerhaft +250 Münzen."],
            ]},
            1: {"heading": "Fischliste (22 insgesamt, 4 offen)", "headers": ["Fisch", "Seltenheit", "Ort", "Bedingung", "Rute", "Energie", "Wert"]},
            2: {"heading": "Ruten-Upgrades (Ridges Howling Hammer)", "headers": ["Rute", "Kosten", "Was sie fängt"]},
            3: {"heading": "Angeltipps"},
        },
    },
}

# =====================================================================
# FLOWERS（screenhype 全花表 L2）
# =====================================================================
FLOWER_ROWS = [
    ["Black Azalea", "Summer", "Misty Shores, Moonlit Pines", "6", "Death (love), Luna (love)"],
    ["Blue Azalea", "—", "—", "6", "Luna (love), Winston"],
    ["Pink Azalea", "Spring", "Player Farm, Moonlit Pines", "6", "Luna (love), Mina (love)"],
    ["Purple Azalea", "Spring", "Player Farm, Moonlit Pines", "6", "Luna (love), Sabrina (love)"],
    ["Red Azalea", "Spring", "Misty Shores", "6", "Luna (love)"],
    ["Yellow Azalea", "Spring", "Howling Marshes", "6", "Jada (love), Luna (love)"],
    ["Blue Kthonia", "—", "—", "15", "Luna (love)"],
    ["Purple Kthonia", "Spring/Summer", "Moonlit Pines", "15", "Luna (love), Sabrina (love), Saga (love)"],
    ["Purple Lavender", "Spring", "Moonlit Pines", "15", "Luna (love), Persephone (love)"],
    ["Red Lavender", "Spring", "Misty Shores", "15", "Luna (love)"],
    ["Blue Moonlight Flower", "Spring", "Khazan Temple", "—", "Luna (love), Moon Goddess (love)"],
    ["Purple Moonlight Flower", "Summer", "Khazan Temple", "—", "Aras (love), Dragan (love), Luna (love), Moon Goddess (love)"],
    ["Black Plumeria", "—", "—", "6", "Luna (love)"],
    ["Blue Plumeria", "—", "—", "6", "Luna (love)"],
    ["Pink Plumeria", "—", "—", "6", "Luna (love)"],
    ["Purple Plumeria", "Spring/Summer", "Player Farm, Moonlit Pines", "6", "Luna (love), Sabrina (love)"],
    ["Red Plumeria", "—", "—", "6", "Luna (love)"],
    ["Yellow Plumeria", "Spring", "Howling Marshes", "6", "Luna (love), Sun God (love)"],
    ["Poinsettia", "Winter", "Misty Shores", "—", "Luna (love)"],
    ["Black Rose", "Summer", "Khazan Temple", "10", "Alina (love), Luna (love)"],
    ["Blue Rose", "Summer", "Khazan Temple", "10", "Luna (love), Ridge (love)"],
    ["Pink Rose", "—", "—", "10", "Luna (love)"],
    ["Purple Rose", "Spring/Summer", "Moonlit Pines, Player Farm", "10", "Luna (love)"],
    ["Red Rose", "—", "—", "10", "Elvira (love), Luna (love)"],
    ["White Rose", "Spring/Summer", "Khazan Temple, Moonlit Pines", "10", "Brook (love), Luna (love)"],
    ["Yellow Rose", "Spring", "Howling Marshes", "10", "Luna (love)"],
    ["Black Tulips", "Spring", "Misty Shores", "6", "Ludo (love), Luna (love)"],
    ["Blue Tulips", "—", "—", "6", "Luna (love)"],
    ["Pink Tulips", "Spring", "Moonlit Pines", "6", "Luna (love), Mina (love)"],
    ["Purple Tulips", "Spring", "Player Farm, Moonlit Pines", "6", "Luna (love), Sabrina (love)"],
    ["Red Tulips", "Spring", "Misty Shores", "6", "Luna (love)"],
    ["White Tulips", "Spring", "Crest Garden, Town NE", "6", "Fiona (love), Luna (love)"],
    ["Yellow Tulips", "Spring", "Howling Marshes", "6", "Luna (love)"],
]
FLOWERS_EN = {
    "slug": "moonlight-peaks/flowers",
    "title": "Moonlight Peaks Flower Guide: All Flowers",
    "metaTitle": "All Flowers in Moonlight Peaks: Seasons, Locations, Values & Who to Gift",
    "metaDescription": "Every flower in Moonlight Peaks by season, location and value — plus who loves each flower as a gift. Searchable and sortable.",
    "intro": "Flowers are the most versatile gift in Moonlight Peaks: Luna loves any flower, and many other residents love specific colors. This table covers every flower we've verified with its season, location, value and best gift target.",
    "sections": [
        T(["Flower", "Season(s)", "Location(s)", "Value", "Gift to (love)"], FLOWER_ROWS, heading="Complete Flower Table (33 entries)"),
        N("Flower tips", [
            "Luna loves any flower — a safe daily gift.",
            "Moonlight Flowers (Khazan Temple) are the most valuable for Aras, Dragan and Moon Goddess.",
            "Black flowers (Alina) and colored tulips cover many characters — stock them from Misty Shores.",
            "White flowers are a rare spawn; save them for Fiona and Brook.",
            "Plant flowers around beehives to increase honey production and yield (community tip).",
        ]),
        F([
            ["Which flower does everyone like?", "There is no universal favorite, but Luna loves any flower and most residents like most flowers — flowers are the safest gift class."],
            ["Where do Moonlight Flowers spawn?", "Khazan Temple: Blue in Spring, Purple in Summer."],
            ["Do flowers sell well?", "Most sell for 6–15 Coins; rare colored roses and moonlight flowers are the most valuable."],
        ]),
    ],
}

FLOWERS_I18N = {
    "zh-CN": {
        "title": "月光小镇 花卉全表",
        "metaTitle": "月光小镇花卉大全：季节·地点·价格·赠谁",
        "metaDescription": "《月光小镇》全部花卉：季节、地点、价格与赠礼对象（谁最爱哪种花），可搜索可筛选。",
        "intro": "花卉是《月光小镇》最通用的礼物：Luna 喜欢任何花，许多居民则偏爱特定颜色。本表列出已核实的全部花卉的季节、地点、价格与最佳赠礼对象。",
        "sections": {
            0: {"heading": "花卉全表（33 条）", "headers": ["花", "季节", "地点", "价格", "赠给（最爱）"]},
            1: {"heading": "花卉技巧"},
            2: {},
        },
    },
    "ja": {
        "title": "ムーンライトピークス 花ガイド",
        "metaTitle": "全花：季節・場所・価値・贈り先",
        "metaDescription": "『Moonlight Peaks』の全花を季節・場所・価値と贈り先（誰が大好きか）で一覧に。",
        "intro": "花は最も汎用性の高い贈り物。Luna はどんな花でも大好きで、他の住民も特定の色を好みます。検証済みの全花を季節・場所・価値・贈り先でまとめました。",
        "sections": {
            0: {"heading": "完全な花リスト（33種）", "headers": ["花", "季節", "場所", "価値", "贈り先（大好き）"]},
            1: {"heading": "花のコツ"},
        },
    },
    "ko": {
        "title": "문라이트 피크스 꽃 가이드",
        "metaTitle": "전체 꽃: 계절·장소·가치·선물 대상",
        "metaDescription": "『문라이트 피크스』전체 꽃을 계절·장소·가치와 선물 대상(누가 최애인지)으로 정리.",
        "intro": "꽃은 가장 활용도 높은 선물입니다. Luna는 어떤 꽃이든 최애이고, 다른 주민들도 특정 색을 좋아합니다. 검증된 전체 꽃을 계절·장소·가치·선물 대상으로 정리했습니다.",
        "sections": {
            0: {"heading": "전체 꽃 목록(33종)", "headers": ["꽃", "계절", "장소", "가치", "선물 대상(최애)"]},
            1: {"heading": "꽃 팁"},
        },
    },
    "fr": {
        "title": "Guide des fleurs de Moonlight Peaks",
        "metaTitle": "Toutes les fleurs : saisons, lieux, valeurs et destinataires",
        "metaDescription": "Chaque fleur de Moonlight Peaks par saison, lieu et valeur — et qui l'adore en cadeau. Recherchable et triable.",
        "intro": "Les fleurs sont le cadeau le plus polyvalent : Luna adore n'importe quelle fleur et beaucoup d'habitants adorent des couleurs précises. Voici toutes les fleurs vérifiées, saison, lieu, valeur et meilleure cible.",
        "sections": {
            0: {"heading": "Tableau complet des fleurs (33 entrées)", "headers": ["Fleur", "Saison(s)", "Lieu(x)", "Valeur", "Offrir à (adore)"]},
            1: {"heading": "Conseils fleurs"},
        },
    },
    "de": {
        "title": "Blumen-Guide für Moonlight Peaks",
        "metaTitle": "Alle Blumen: Jahreszeiten, Orte, Werte und für wen",
        "metaDescription": "Jede Blume in Moonlight Peaks nach Jahreszeit, Ort und Wert — und wer sie als Geschenk liebt. Durchsuchbar und sortierbar.",
        "intro": "Blumen sind das vielseitigste Geschenk: Luna liebt jede Blume, viele andere Bewohner lieben bestimmte Farben. Diese Tabelle umfasst alle verifizierten Blumen mit Jahreszeit, Ort, Wert und bestem Ziel.",
        "sections": {
            0: {"heading": "Komplette Blumen-Tabelle (33 Einträge)", "headers": ["Blume", "Jahreszeit(en)", "Ort(e)", "Wert", "Schenken an (liebt)"]},
            1: {"heading": "Blumen-Tipps"},
        },
    },
}

# =====================================================================
# TOOLS（screenhype 工具升级 L2）
# =====================================================================
TOOL_ROWS = [
    ["Copper Axe", "1,000", "Rusty Axe + 3x Copper Bar"],
    ["Iron Axe", "4,000", "Copper Axe + 3x Iron Bar"],
    ["Gold Axe", "16,000", "Iron Axe + 3x Gold Bar"],
    ["Copper Pickaxe", "1,000", "Rusty Pickaxe + 3x Copper Bar"],
    ["Iron Pickaxe", "4,000", "Copper Pickaxe + 3x Iron Bar"],
    ["Gold Pickaxe", "16,000", "Iron Pickaxe + 3x Gold Bar"],
    ["Copper Scythe", "1,000", "Rusty Scythe + 3x Copper Bar"],
    ["Iron Scythe", "4,000", "Copper Scythe + 3x Iron Bar"],
    ["Copper Shovel", "1,000", "Rusty Shovel + 3x Copper Bar"],
    ["Iron Shovel", "4,000", "Copper Shovel + 3x Iron Bar"],
    ["Gold Shovel", "16,000", "Iron Shovel + 3x Gold Bar"],
    ["Copper Watering Can", "1,000", "Rusty Watering Can + 3x Copper Bar"],
    ["Iron Watering Can", "4,000", "Copper Watering Can + 3x Iron Bar"],
    ["Gold Watering Can", "16,000", "Iron Watering Can + 3x Gold Bar"],
    ["Premium Fishing Rod", "16,000", "Fishing Rod + 3x Gold Bar"],
]
TOOLS_EN = {
    "slug": "moonlight-peaks/tools",
    "title": "Moonlight Peaks Tool Upgrades: Costs & Materials",
    "metaTitle": "All Tool Upgrades in Moonlight Peaks: Copper, Iron & Gold Costs",
    "metaDescription": "Every tool upgrade in Moonlight Peaks: Copper 1,000 / Iron 4,000 / Gold 16,000 Coins, materials required, and where to upgrade at Ridge's Howling Hammer.",
    "intro": "Tools in Moonlight Peaks start at Rusty and upgrade through Copper, Iron and Gold — each tier needs Coins plus bars of the previous metal. All upgrades are bought at Ridge's shop, the Howling Hammer.",
    "sections": [
        T(["Upgrade", "Coins", "Materials"], TOOL_ROWS, heading="Complete Tool Upgrade Table"),
        N("Where & how to upgrade", [
            "Talk to Ridge inside his shop (the Howling Hammer) during opening hours — 6pm to midnight, Monday–Friday.",
            "The Howling Hammer is the first building after the bridge by the canal in central Moonlight Peaks.",
            "Copper tools unlock after you complete 'A Bridge Too Far' and explore the cave in Misty Shores.",
            "Mine Copper Ore (Cave of Echoes) and Iron Ore (deeper in the cave), then smelt bars in your furnace.",
        ]),
        S("Upgrade order we recommend", [
            ["Pickaxe first", "Better pickaxes break larger rocks and unlock more ore (and Rose Quartz for Mana)."],
            ["Watering can / axe next", "More crops per day and faster wood for kegs, barns and upgrades."],
            ["Scythe & shovel", "The scythe stops at Iron tier; the shovel helps clear land."],
            ["Fishing rod", "The Premium Rod (16,000 + 3 Gold Bars) catches the large fish for the museum and big money."],
        ]),
        F([
            ["How much do tool upgrades cost?", "All Copper tools cost 1,000 Coins, all Iron tools 4,000, all Gold tools 16,000 — plus 3 bars of the previous metal each."],
            ["Where is the tool shop?", "Ridge's Howling Hammer in central Moonlight Peaks, open 6pm–midnight Monday–Friday."],
            ["When can I buy Copper tools?", "After completing 'A Bridge Too Far' and reaching the cave in Misty Shores."],
            ["Does the scythe have a Gold tier?", "No — the scythe stops at Iron (per Screen Hype)."],
        ]),
    ],
}

TOOLS_I18N = {
    "zh-CN": {
        "title": "月光小镇 工具升级",
        "metaTitle": "月光小镇工具升级：铜/铁/金 价格与材料",
        "metaDescription": "《月光小镇》全部工具升级：铜 1000 / 铁 4000 / 金 16000 金币及所需材料，在 Ridge 的 Howling Hammer 购买。",
        "intro": "《月光小镇》工具从 Rusty（生锈）起步，依次升级为 铜、铁、金——每级都需要金币与上一级金属锭。所有升级都在 Ridge 的店铺 Howling Hammer 购买。",
        "sections": {
            0: {"heading": "完整工具升级表", "headers": ["升级", "金币", "材料"]},
            1: {"heading": "在哪里升级", "items": [
                "在营业时间内与 Ridge 店内的他对话——晚上 6 点到午夜，周一至周五。",
                "Howling Hammer 是月光小镇中央运河桥后的第一栋建筑。",
                "完成“A Bridge Too Far”并探索 Misty Shores 的洞穴后解锁铜工具。",
                "在 Cave of Echoes 挖铜矿、洞穴更深处挖铁矿，再用熔炉冶炼成锭。",
            ]},
            2: {"heading": "推荐升级顺序", "items": [
                ["先升镐", "更好的镐能敲碎更大的岩石，解锁更多矿石（以及做魔力萃取器的 Rose Quartz）。"],
                ["再升水壶/斧", "每天种更多作物、更快砍木头做木桶、谷仓与升级。"],
                ["镰刀与铲", "镰刀最高到铁级；铲子帮助清理土地。"],
                ["鱼竿", "Premium 竿（16000 + 3 金条）能钓大鱼，喂博物馆与钱包。"],
            ]},
            3: {},
        },
    },
    "ja": {
        "title": "ムーンライトピークス 道具強化",
        "metaTitle": "全道具強化：銅・鉄・金の費用と素材",
        "metaDescription": "『Moonlight Peaks』の全道具強化：銅1,000/鉄4,000/金16,000コインと必要素材、Ridge の Howling Hammer で購入。",
        "intro": "道具は Rusty から始まり、銅・鉄・金の順に強化。各段階でコインと前段階の金属バーが必要。すべて Ridge の店 Howling Hammer で購入。",
        "sections": {
            0: {"heading": "完全な道具強化表", "headers": ["強化", "コイン", "素材"]},
            1: {"heading": "場所と手順", "items": [
                "営業時間内（18時〜24時、月〜金）に Howling Hammer の Ridge と話す。",
                "中央の運河の橋を渡って最初の建物。",
                "「A Bridge Too Far」完了後、Misty Shores の洞窟で銅道具が解放。",
                "Cave of Echoes で銅鉱、奥で鉄鉱を採掘し、炉でインゴットに。",
            ]},
            2: {"heading": "おすすめ強化順", "items": [
                ["ツルハシ優先", "大きな岩を壊せ、鉱石と Rose Quartz が採れる。"],
                ["次にジョウロ/斧", "毎日多くの作物、木材で樽や納屋。"],
                ["鎌とシャベル", "鎌は鉄止まり。シャベルで土地を開墾。"],
                ["釣り竿", "Premium 竿（16,000+金3）で大型魚が釣れ、博物館と収入に。"],
            ]},
        },
    },
    "ko": {
        "title": "문라이트 피크스 도구 강화",
        "metaTitle": "전체 도구 강화: 구리·철·금 비용과 재료",
        "metaDescription": "『문라이트 피크스』전체 도구 강화: 구리 1,000/철 4,000/금 16,000코인과 필요 재료, Ridge의 Howling Hammer에서 구매.",
        "intro": "도구는 Rusty에서 시작해 구리·철·금 순으로 강화됩니다. 각 단계마다 코인과 이전 단계 금속 주괴가 필요하며, 모두 Ridge의 상점 Howling Hammer에서 구매합니다.",
        "sections": {
            0: {"heading": "전체 도구 강화 표", "headers": ["강화", "코인", "재료"]},
            1: {"heading": "장소와 방법", "items": [
                "영업시간(18시~자정, 월~금)에 Howling Hammer의 Ridge와 대화.",
                "중앙 운하 다리 뒤 첫 번째 건물.",
                "'A Bridge Too Far' 완료 후 Misty Shores 동굴에서 구리 도구 해금.",
                "Cave of Echoes에서 구리 광석, 깊은 곳에서 철 광석을 캐서 용광로로 주괴 제작.",
            ]},
            2: {"heading": "추천 강화 순서", "items": [
                ["곡괭이 우선", "큰 바위를 부수고 광석과 Rose Quartz 확보."],
                ["다음 물뿌리개/도끼", "하루 더 많은 작물, 통·헛간용 목재."],
                ["낫과 삽", "낫은 철까지. 삽은 땅 정리용."],
                ["낚싯대", "Premium 낚싯대(16,000+금괴3)로 대형어 확보."],
            ]},
        },
    },
    "fr": {
        "title": "Améliorations d'outils de Moonlight Peaks",
        "metaTitle": "Toutes les améliorations : coûts cuivre, fer et or",
        "metaDescription": "Chaque amélioration d'outil dans Moonlight Peaks : 1 000 cuivre / 4 000 fer / 16 000 or, matériaux requis, chez Ridge au Howling Hammer.",
        "intro": "Les outils partent de Rusty et passent par Cuivre, Fer et Or — chaque palier demande des pièces plus les barres du métal précédent. Tout s'achète chez Ridge, au Howling Hammer.",
        "sections": {
            0: {"heading": "Tableau complet des améliorations", "headers": ["Amélioration", "Pièces", "Matériaux"]},
            1: {"heading": "Où et comment", "items": [
                "Parlez à Ridge dans sa boutique (le Howling Hammer) — 18h à minuit, lundi–vendredi.",
                "Premier bâtiment après le pont sur le canal, au centre de Moonlight Peaks.",
                "Les outils cuivre se débloquent après 'A Bridge Too Far' et la grotte de Misty Shores.",
                "Minez cuivre (Cave of Echoes) et fer (plus profond), puis fondez les barres au four.",
            ]},
            2: {"heading": "Ordre recommandé", "items": [
                ["Pioche d'abord", "Casse les gros rochers et débloque plus de minerais (et le Rose Quartz)."],
                ["Arrosoir / hache ensuite", "Plus de cultures et de bois pour tonneaux et granges."],
                ["Faux et pelle", "La faux s'arrête au fer ; la pelle déblaie le terrain."],
                ["Canne à pêche", "La Premium (16 000 + 3 or) attrape les gros poissons."],
            ]},
        },
    },
    "de": {
        "title": "Werkzeug-Upgrades in Moonlight Peaks",
        "metaTitle": "Alle Upgrades: Kupfer-, Eisen- und Gold-Kosten",
        "metaDescription": "Jedes Werkzeug-Upgrade in Moonlight Peaks: Kupfer 1.000 / Eisen 4.000 / Gold 16.000 Münzen, benötigte Materialien und wo (Ridges Howling Hammer).",
        "intro": "Werkzeuge starten als Rostig und steigern sich über Kupfer, Eisen und Gold — jede Stufe kostet Münzen plus Barren des vorherigen Metalls. Alles kaufst du bei Ridge im Howling Hammer.",
        "sections": {
            0: {"heading": "Komplette Upgrade-Tabelle", "headers": ["Upgrade", "Münzen", "Materialien"]},
            1: {"heading": "Wo und wie", "items": [
                "Sprich mit Ridge im Laden (Howling Hammer) — 18 bis 24 Uhr, Mo–Fr.",
                "Erstes Gebäude hinter der Brücke am Kanal in der Stadtmitte.",
                "Kupfer-Werkzeuge nach 'A Bridge Too Far' und der Höhle in Misty Shores.",
                "Baue Kupfer (Cave of Echoes) und Eisen (tiefer) ab, schmelze Barren im Ofen.",
            ]},
            2: {"heading": "Empfohlene Reihenfolge", "items": [
                ["Spitzhacke zuerst", "Zerbricht große Felsen und schaltet Erze frei (auch Rose Quartz)."],
                ["Gießkanne / Axt", "Mehr Pflanzen pro Tag, Holz für Fässer und Scheunen."],
                ["Sense und Schaufel", "Die Sense endet bei Eisen; die Schaufel räumt Land."],
                ["Angelrute", "Die Premium (16.000 + 3 Gold) fängt die großen Fische."],
            ]},
        },
    },
}

# =====================================================================
# ACHIEVEMENTS（59 全表 · thegamer L2）
# =====================================================================
ACH_ROWS = [
    ["A Childhood Dream", "Build a treehouse with Ridge."],
    ["A Farming Monopoly", "Earn 1,000,000 coins."],
    ["A Generous Donor", "Give 299 gifts."],
    ["A House for the Hendersons", "Welcome the Henderson family to town."],
    ["A Lively Farm", "Adopt your first farm creature."],
    ["A Magical Cocktail", "Have every potion effect active at the same time."],
    ["A Magical Toolbelt", "Upgrade any tool into its Enchanted version."],
    ["AFKitten", "Pet your Hellkitten for five consecutive minutes."],
    ["Albertus' Helper", "Complete 25 job board requests."],
    ["Archaeo-Logistics", "Open the Museum."],
    ["Awooooo!", "Talk to a werewolf during a full moon."],
    ["Back in Place", "Return every plastic chair."],
    ["Back to the Den", "Return every Vampster to its den."],
    ["Bad Santa!", "Bring charcoal to Pakkeleg."],
    ["Bottomless Chester", "Sell more than 9,000 coins worth of items in one night."],
    ["Buddies for Afterlife", "Become friends with Death."],
    ["By the Shore", "Discover Luna Bay."],
    ["Call of the Current", "Unlock Mermaid form."],
    ["Card Tricks", "Score at least 30 points in a single Nokturna match."],
    ["Cartographer", "Discover every location in Moonlight Peaks."],
    ["Do You Speak Animalese?", "Talk to a creature while in Hellkitten form."],
    ["Dracula Estate", "Fully upgrade your house."],
    ["Fishing Pro", "Catch every fish."],
    ["Fully Energized", "Reach maximum Energy."],
    ["Get Creative", "Craft a flower arrangement, embroidery, or vase."],
    ["Happy New Year!", "Complete your first in-game year."],
    ["Magic at Max Capacity", "Reach maximum Mana."],
    ["Making Mina Proud", "Cook 25 different recipes."],
    ["Master of Witchcraft", "Fully upgrade every spell."],
    ["Missing? No!", "Catch a Missing."],
    ["Moonlit Stretching", "Attend your first yoga session."],
    ["New Beginnings", "Plant your first crop."],
    ["Nokturna Master", "Collect every Nokturna card."],
    ["One Collection to Rule Them All", "Complete the Museum."],
    ["Out of the Mist", "Lift the curse from Misty Shores."],
    ["Out of This World", "Travel to the moon."],
    ["Perpetual Bloom", "Build a greenhouse."],
    ["Purrgatory", "Unlock Hellkitten form."],
    ["Raiders of the Lost Art", "Finish Elvira's treasure hunt."],
    ["Rightful Ritualist", "Activate every Witch's Circle."],
    ["Serial Gifter", "Give 25 loved gifts in the same night."],
    ["Skulls in a Net", "Collect every Soul Blob."],
    ["Social Butterfly", "Reach four hearts with every character."],
    ["Soup-Chef", "Earn the Mastersoup trophy."],
    ["Take a Seat", "Help repair the broken bench."],
    ["The Ambrosias", "Place the Ambrosia Crest in the Crest Garden."],
    ["The Draculas", "Place the Dracula Crest in the Crest Garden."],
    ["The Hendersons", "Place the Henderson Crest in the Crest Garden."],
    ["The Hosus", "Place the Hosu Crest in the Crest Garden."],
    ["The Khazans", "Place the Khazan Crest in the Crest Garden."],
    ["The Logans", "Place the Logan Crest in the Crest Garden."],
    ["The Pumpking", "Meet the mysterious pumpkin."],
    ["The Webbs", "Place the Webb Crest in the Crest Garden."],
    ["Tied the Knot", "Get married."],
    ["To the Depths", "Open the Catacombs."],
    ["Tree Hugger", "Fall in love with a tree."],
    ["Vampire with a Wand", "Cast your first spell."],
    ["Wings of the Night", "Unlock Bat form."],
    ["Witnessing Revolution", "Watch the Draculambs march."],
]
ACH_EN = {
    "slug": "moonlight-peaks/achievements",
    "title": "Moonlight Peaks Achievements: All 59",
    "metaTitle": "All 59 Moonlight Peaks Achievements & How to Unlock Them",
    "metaDescription": "Every Moonlight Peaks achievement with unlock conditions: story, collection, romance, transformation and family crest achievements — the complete 59 list.",
    "intro": "Moonlight Peaks has 59 achievements at launch. Many unlock naturally as you play, but several need planning — family crests, full collections, transformations and romance. This is the complete list with how to unlock each one.",
    "sections": [
        T(["Achievement", "How to unlock"], ACH_ROWS, heading="All 59 Achievements (alphabetical)"),
        N("Tips for 100% completion", [
            "Crest achievements: finish each family storyline (Ambrosia, Dracula, Henderson, Hosu, Khazan, Logan, Webb) to place their crest in the Crest Garden.",
            "Collections: donate every fish, flower and artifact — 'One Collection to Rule Them All' requires the full Museum.",
            "Transformations: Mermaid, Bat and Hellkitten forms unlock through the main story; 'Tree Hugger' comes from a specific romance route.",
            "Gift achievements: plan 25 loved gifts in one night ('Serial Gifter') and 299 total ('A Generous Donor').",
            "Missables to watch: talk to a werewolf on a full moon (Awooooo!), bring charcoal to Pakkeleg (Bad Santa!), catch a Missing (Missing? No!).",
        ]),
        F([
            ["How many achievements are there?", "59 at launch (July 6–7, 2026)."],
            ["What's the hardest achievement?", "Completionists point to 'One Collection to Rule Them All' (full Museum), 'Fishing Pro' (all 22 fish) and 'A Farming Monopoly' (1,000,000 coins)."],
            ["Can I miss achievements?", "Yes — several are tied to events (full moon, Pakkeleg) or late-game story windows; plan ahead."],
        ]),
    ],
}

ACH_I18N = {
    "zh-CN": {
        "title": "月光小镇 成就全表",
        "metaTitle": "月光小镇 59 个成就全表与解锁方法",
        "metaDescription": "《月光小镇》全部 59 个成就与解锁条件：剧情、收集、恋爱、变身与家族纹章成就完整清单。",
        "intro": "《月光小镇》首发共 59 个成就。许多随流程自然解锁，但也有不少需要规划——家族纹章、全收集、变身与恋爱。下面是完整清单与解锁方法。",
        "sections": {
            0: {"heading": "全部 59 个成就（按字母序）", "headers": ["成就", "解锁方法"]},
            1: {"heading": "100% 完成技巧"},
            2: {},
        },
    },
    "ja": {
        "title": "ムーンライトピークス 実績",
        "metaTitle": "実績59個と解除条件",
        "metaDescription": "『Moonlight Peaks』の実績59個と解除条件：ストーリー、収集、恋愛、変身、家紋。完全リスト。",
        "intro": "実績は発売時点で59個。多くは自然に解除されますが、家紋や完全収集、変身、恋愛などは計画が必要。完全リストと解除方法。",
        "sections": {
            0: {"heading": "実績59個（アルファベット順）", "headers": ["実績", "解除方法"]},
            1: {"heading": "コンプリートのコツ"},
        },
    },
    "ko": {
        "title": "문라이트 피크스 업적",
        "metaTitle": "업적 59개와 해금 조건",
        "metaDescription": "『문라이트 피크스』업적 59개와 해금 조건: 스토리, 수집, 연애, 변신, 가문 문장. 전체 목록.",
        "intro": "업적은 출시 기준 59개. 대부분 자연스럽게 해금되지만 가문 문장, 전체 수집, 변신, 연애는 계획이 필요합니다. 전체 목록과 해금 방법.",
        "sections": {
            0: {"heading": "업적 59개(알파벳순)", "headers": ["업적", "해금 방법"]},
            1: {"heading": "100% 달성 팁"},
        },
    },
    "fr": {
        "title": "Succès de Moonlight Peaks",
        "metaTitle": "Les 59 succès et comment les débloquer",
        "metaDescription": "Tous les succès de Moonlight Peaks avec conditions : histoire, collection, romance, transformations et emblèmes familiaux — la liste complète des 59.",
        "intro": "Moonlight Peaks compte 59 succès au lancement. Beaucoup se débloquent naturellement, mais plusieurs demandent de la préparation : emblèmes, collections, transformations, romance. Liste complète.",
        "sections": {
            0: {"heading": "Les 59 succès (ordre alphabétique)", "headers": ["Succès", "Comment débloquer"]},
            1: {"heading": "Conseils pour le 100 %"},
        },
    },
    "de": {
        "title": "Erfolge in Moonlight Peaks",
        "metaTitle": "Alle 59 Erfolge und wie man sie freischaltet",
        "metaDescription": "Jeder Erfolg in Moonlight Peaks mit Bedingungen: Story, Sammlung, Romantik, Verwandlungen und Familienwappen — die komplette Liste der 59.",
        "intro": "Moonlight Peaks hat 59 Erfolge zum Start. Viele schalten sich natürlich frei, einige brauchen Planung: Wappen, komplette Sammlungen, Verwandlungen und Romantik. Die komplette Liste.",
        "sections": {
            0: {"heading": "Alle 59 Erfolge (alphabetisch)", "headers": ["Erfolg", "Freischalten"]},
            1: {"heading": "Tipps für 100 %"},
        },
    },
}

# =====================================================================
# SPELLS（gamerant L2 · Spring Year 1 列表）
# =====================================================================
SPELL_ROWS = [
    ["Aquaflux I", "Free (story)", "Summon a watering can that waters up to 16 crops.", "1 Mana"],
    ["Aquaflux II", "8,000 Coins (needs Witch's Wand)", "Summon 2 watering cans, up to 24 crops each.", "1 Mana"],
    ["Arborascend I", "1,200 Coins", "Magically move 1 tree.", "2 Mana"],
    ["Ethereal Hands I", "1,400 Coins", "Summon helping hands that harvest up to 32 crops.", "1 Mana"],
    ["Metamorphosia I", "1,600 Coins", "Transform 1 crop into another random crop.", "3 Mana"],
    ["Hoisthaven", "2,000 Coins", "Magically move a building.", "3 Mana"],
    ["Maturio I", "2,000 Coins", "Instantly grow crops to maturity in a 1-by-1 area.", "2 Mana"],
    ["Refilliarmus", "2,000 Coins", "Instantly refill your watering can.", "0 Mana"],
    ["Ethereal Shovels I", "2,200 Coins", "Summon a shovel that digs up to 32 spots.", "1 Mana"],
    ["Ethereal Axes I", "2,400 Coins", "Summon an axe that chops up to 16 logs or trees.", "2 Mana"],
    ["Ethereal Pickaxes I", "2,600 Coins", "Summon a pickaxe that crushes up to 16 rocks.", "2 Mana"],
    ["Tomorrow's Tears", "4,000 Coins", "Make it rain the next night.", "3 Mana"],
]
SPELLS_EN = {
    "slug": "moonlight-peaks/spells",
    "title": "Moonlight Peaks Spells: All Spells & Costs",
    "metaTitle": "All Moonlight Peaks Spells: Costs, Mana & Effects",
    "metaDescription": "Every spell in Moonlight Peaks (Spring Year 1): unlock cost, mana cost and effect — from Aquaflux to Tomorrow's Tears, plus how to learn and upgrade magic.",
    "intro": "Magic in Moonlight Peaks comes from your wand and a Grimoire of spells. You learn your first spell (Aquaflux I) from Luna in the 'Magic of Crops' quest, then buy more at Webb of Wonders from Sabrina. Most spells cost Mana to cast.",
    "sections": [
        T(["Spell", "Unlock / cost", "Effect", "Mana cost"], SPELL_ROWS, heading="All Spells (Spring Year 1)"),
        S("How to learn & upgrade magic", [
            ["The Magic of Crops", "Read Luna's letter in Spring, complete the quest, and she teaches you Aquaflux I. Your Fixed Wand gets repaired along the way."],
            ["Buy more spells", "Open the Grimoire (last tab of your menu) → Spells tab to see the wand gestures. Purchase new spells at Webb of Wonders (Sabrina)."],
            ["Witch's Wand", "Some advanced spells (like Aquaflux II) require the Witch's Wand instead of the Fixed Wand."],
            ["Upgrades & mana", "Buy mana upgrades (Arcane Flame) at Webb of Wonders to cast more; the Mana Extractor converts magical crops into mana essence."],
        ]),
        N("Spells worth buying first", [
            "Aquaflux I (free) and Refilliarmus (0 Mana) — the water loop.",
            "Ethereal Hands I (harvest 32 crops) saves hours of clicking.",
            "Ethereal Pickaxes I and Axes I — faster mining and wood.",
            "Maturio I — instant crop growth in a pinch.",
        ]),
        F([
            ["How do I unlock magic?", "Complete 'The Magic of Crops' (letter from Luna in Spring). You learn Aquaflux I and get your Fixed Wand."],
            ["Where do I buy spells?", "Webb of Wonders, Sabrina's magic shop in Moonlight Peaks."],
            ["How do I cast a spell?", "Open the Grimoire → Spells tab to see the wand gesture (the ball of light shows the order to move your wand)."],
            ["How many spells are there?", "The Spring Year 1 list has 12 spells; later-game spells are still being verified (marked 待补)."],
        ]),
    ],
}

SPELLS_I18N = {
    "zh-CN": {
        "title": "月光小镇 咒语大全",
        "metaTitle": "月光小镇咒语大全：价格·魔力·效果",
        "metaDescription": "《月光小镇》全部咒语（第一年春）：解锁价格、魔力消耗与效果，以及学习与升级魔法的完整方法。",
        "intro": "《月光小镇》的魔法来自你的魔杖与咒语书。第一个咒语（Aquaflux I 水涌术）由 Luna 在“魔法作物”任务中教给你，之后可在 Webb of Wonders 找 Sabrina 购买更多咒语。多数咒语需要消耗魔力。",
        "sections": {
            0: {"heading": "全部咒语（第一年春）", "headers": ["咒语", "解锁/价格", "效果", "魔力"]},
            1: {"heading": "如何学习与升级魔法", "items": [
                ["魔法作物任务", "春天读 Luna 的来信完成任务，她会教给你 Aquaflux I，并顺带修好你的固定魔杖。"],
                ["购买更多咒语", "打开菜单最后一栏的咒语书 Grimoire → Spells 标签查看魔杖手势。在 Webb of Wonders（Sabrina）购买新咒语。"],
                ["女巫魔杖", "部分高级咒语（如 Aquaflux II）需要女巫魔杖而非固定魔杖。"],
                ["升级与魔力", "在 Webb of Wonders 购买魔力升级（Arcane Flame）可施更多法术；魔力萃取器把魔法作物转化为魔力精华。"],
            ]},
            2: {"heading": "值得先买的咒语"},
            3: {},
        },
    },
    "ja": {
        "title": "ムーンライトピークス 呪文",
        "metaTitle": "全呪文：費用・マナ・効果",
        "metaDescription": "『Moonlight Peaks』の全呪文（春1年目）：解放コスト、マナ消費、効果。魔法の習得と強化も。",
        "intro": "魔法は杖とグリモワール（呪文書）で使います。最初の呪文 Aquaflux I は「Magic of Crops」で Luna から学び、以降は Webb of Wonders の Sabrina から購入。多くはマナ消費。",
        "sections": {
            0: {"heading": "全呪文（春1年目）", "headers": ["呪文", "解放/費用", "効果", "マナ"]},
            1: {"heading": "習得と強化", "items": [
                ["Magic of Crops", "春に Luna の手紙を読みクエスト完了。Aquaflux I を習得、Fixed Wand も修理。"],
                ["呪文の購入", "メニュー最後のタブ Grimoire → Spells でジェスチャー確認。Webb of Wonders（Sabrina）で購入。"],
                ["Witch's Wand", "Aquaflux II など一部は Witch's Wand が必要。"],
                ["強化とマナ", "Webb of Wonders でマナ強化（Arcane Flame）。Mana Extractor で魔法作物をマナに。"],
            ]},
            2: {"heading": "最初に買うべき呪文"},
        },
    },
    "ko": {
        "title": "문라이트 피크스 주문",
        "metaTitle": "전체 주문: 비용·마나·효과",
        "metaDescription": "『문라이트 피크스』전체 주문(봄 1년차): 해금 비용, 마나 소모, 효과. 마법 학습과 강화도.",
        "intro": "마법은 지팡이와 그리무아르(주문서)로 사용합니다. 첫 주문 Aquaflux I은 'Magic of Crops' 퀘스트로 Luna에게 배우고, 이후 Webb of Wonders의 Sabrina에게 구매합니다. 대부분 마나 소모.",
        "sections": {
            0: {"heading": "전체 주문(봄 1년차)", "headers": ["주문", "해금/비용", "효과", "마나"]},
            1: {"heading": "학습과 강화", "items": [
                ["Magic of Crops", "봄에 Luna의 편지를 읽고 퀘스트 완료. Aquaflux I 습득, Fixed Wand 수리."],
                ["주문 구매", "메뉴 마지막 탭 Grimoire → Spells에서 제스처 확인. Webb of Wonders(Sabrina)에서 구매."],
                ["Witch's Wand", "Aquaflux II 등 일부는 Witch's Wand 필요."],
                ["강화와 마나", "Webb of Wonders에서 마나 강화(Arcane Flame). Mana Extractor로 마법 작물을 마나로."],
            ]},
            2: {"heading": "먼저 사면 좋은 주문"},
        },
    },
    "fr": {
        "title": "Sorts de Moonlight Peaks",
        "metaTitle": "Tous les sorts : coûts, mana et effets",
        "metaDescription": "Chaque sort de Moonlight Peaks (printemps, an 1) : coût, mana et effet — d'Aquaflux à Tomorrow's Tears, plus l'apprentissage et l'amélioration de la magie.",
        "intro": "La magie vient de votre baguette et d'un grimoire. Vous apprenez Aquaflux I auprès de Luna (quête 'Magic of Crops'), puis achetez les autres chez Webb of Wonders (Sabrina). La plupart coûtent du mana.",
        "sections": {
            0: {"heading": "Tous les sorts (printemps, an 1)", "headers": ["Sort", "Déblocage / coût", "Effet", "Mana"]},
            1: {"heading": "Apprendre et améliorer", "items": [
                ["Magic of Crops", "Lisez la lettre de Luna au printemps et terminez la quête pour apprendre Aquaflux I (baguette réparée)."],
                ["Acheter des sorts", "Grimoire (dernier onglet) → Spells pour les gestes. Achetez chez Webb of Wonders (Sabrina)."],
                ["Baguette de sorcière", "Certains sorts (Aquaflux II) exigent la Witch's Wand."],
                ["Améliorations & mana", "Achetez Arcane Flame chez Webb of Wonders ; l'extracteur de mana convertit les cultures magiques."],
            ]},
            2: {"heading": "Sorts à acheter en premier"},
        },
    },
    "de": {
        "title": "Zauber in Moonlight Peaks",
        "metaTitle": "Alle Zauber: Kosten, Mana und Effekte",
        "metaDescription": "Jeder Zauber in Moonlight Peaks (Frühling, Jahr 1): Freischaltkosten, Mana und Effekt — von Aquaflux bis Tomorrow's Tears, plus Lernen und Verbessern.",
        "intro": "Magie kommt aus deinem Zauberstab und einem Grimoire. Den ersten Zauber (Aquaflux I) lernst du von Luna ('Magic of Crops'), weitere kaufst du bei Webb of Wonders (Sabrina). Die meisten kosten Mana.",
        "sections": {
            0: {"heading": "Alle Zauber (Frühling, Jahr 1)", "headers": ["Zauber", "Freischalten / Kosten", "Effekt", "Mana"]},
            1: {"heading": "Lernen & Verbessern", "items": [
                ["Magic of Crops", "Lies Lunas Brief im Frühling, schließe die Quest ab — du lernst Aquaflux I und dein Zauberstab wird repariert."],
                ["Zauber kaufen", "Grimoire (letzter Tab) → Spells für Gesten. Kaufe bei Webb of Wonders (Sabrina)."],
                ["Hexen-Stab", "Manche Zauber (Aquaflux II) brauchen den Witch's Wand."],
                ["Upgrades & Mana", "Kaufe Arcane Flame bei Webb of Wonders; der Mana-Extraktor wandelt magische Pflanzen um."],
            ]},
            2: {"heading": "Zauber zuerst kaufen"},
        },
    },
}

# =====================================================================
# WALKTHROUGH（主线 · intoindiegames 8 部分 L2）
# =====================================================================
WT_ROWS = [
    ["Part 1", "Meeting Townsfolk & Getting Started", "Orlock's Wine Scheme, meet the town, catch fish, first comfort, animal care, A Bridge Too Far."],
    ["Part 2", "Furnace, Magic & Cat Transformation", "Tension in the Crest Garden, A Croak and a Crest, Dinner Party, catch bugs, Magic of Crops."],
    ["Part 3", "Upgrades, Herbs & Mana", "Get Iron, upgrade tools, earn money fast, change clothes, grow herbs, recover Mana."],
    ["Part 4", "Museum, Nokturna & Potion-Making", "A New Beginning, Museum in the Making, how to win Nokturna, Curating the Museum, Mend It With Magic."],
    ["Part 5", "Webb's Crest & Mermaid Transformation", "Webb family storyline and unlocking the Mermaid form."],
    ["Part 6", "Beehives, Saga & Kim Quests", "Beehives, Saga's storyline and Kim's quests."],
    ["Part 7", "Missing, Moon, Bat & Khazan Crest", "The Missing fish, Selene and the moon, Bat transformation, Khazan's Crest, Master of the Night, Pub Quiz."],
    ["Part 8", "Ambrosia, Gold & Dracula", "The Ambrosia Crisis, where to find Gold, Darkness Over Moonlight Peaks, post-game overview."],
]
WT_EN = {
    "slug": "moonlight-peaks/walkthrough",
    "title": "Moonlight Peaks Walkthrough: Main Story Parts 1–8",
    "metaTitle": "Moonlight Peaks Walkthrough: Main Story Step by Step (Parts 1–8)",
    "metaDescription": "The complete Moonlight Peaks main-story walkthrough in 8 parts: wine scheme, crests, museum, Nokturna, transformations, gold and the Dracula storyline.",
    "intro": "The Moonlight Peaks main story is driven by family quests, crests and transformations. This walkthrough follows the main story in 8 parts, from your first Red Wine for Orlock to the post-game.",
    "sections": [
        T(["Part", "Title", "What happens"], WT_ROWS, heading="Walkthrough parts (8)"),
        S("Early story quick path (parts 1–2)", [
            ["Red Wine for Orlock", "Pour water on the man outside your home, meet Viktor, plant Blood Grapes, craft a Keg (20 wood) and make Red Wine."],
            ["Register at Town Hall", "Brook registers you; meet the residents around town (Mina, Ludo, Saga, Noel, Elvira, Dragan, Sabrina, Aras, Samael, Luna)."],
            ["Fishing rod", "Noel's challenge by the coast on night two — keep the rod + 250 Coins."],
            ["Cat transformation", "The Dinner Party at Ambrosia Mansion unlocks your cat form (faster movement)."],
            ["First spells", "Repair your wand at Sabrina's, then Luna teaches Aquaflux I and magical crops."],
        ]),
        S("Mid-to-late story quick path (parts 3–8)", [
            ["Iron & Mana", "Mine Iron in the Cave of Echoes; craft the Mana Extractor with Rose Quartz from the Crystal Cave."],
            ["Museum & Nokturna", "Help Jada set up the Museum (artifacts from four families); win Nokturna for cards."],
            ["Webb's Crest & Mermaid", "Progress the Webb storyline to unlock the Mermaid form."],
            ["Bat & Khazan Crest", "Meet Selene under the moon; Orlock teaches Bat form (bring Red Wine); follow the light trail to the Khazan Crest."],
            ["Gold & Dracula", "Gold ore deep in the Cave of Echoes (silver pickaxe); finish Darkness Over Moonlight Peaks to bring the Dracula family home."],
            ["Post-game", "Complete the Museum and journal, collect Soul Blobs, learn all spells and recipes, unlock the Twilight Catacombs."],
        ]),
        F([
            ["How long is the main story?", "The walkthrough spans 8 parts; completionists add museum, journal, all fish/flowers and every family crest."],
            ["Which family quests matter for crests?", "Ambrosia, Dracula, Henderson, Hosu, Khazan, Logan and Webb each end in a crest for the Crest Garden."],
            ["When can I transform?", "Cat form (Dinner Party, part 2), Mermaid (Webb storyline, part 5), Bat (Orlock, part 7), Hellkitten and others via the story."],
        ]),
    ],
}

WT_I18N = {
    "zh-CN": {
        "title": "月光小镇 主线流程",
        "metaTitle": "月光小镇主线攻略：第 1–8 部分逐步",
        "metaDescription": "《月光小镇》主线流程完整攻略（8 部分）：葡萄酒计划、家族纹章、博物馆、Nokturna、变身、黄金与德古拉线。",
        "intro": "《月光小镇》主线由家族任务、纹章与变身驱动。本攻略按 8 个部分逐步推进，从为 Orlock 酿造第一瓶红酒到通关后内容。",
        "sections": {
            0: {"heading": "攻略分卷（8 部分）", "headers": ["部分", "标题", "内容"]},
            1: {"heading": "前期快速路线（第 1–2 部分）", "items": [
                ["为 Orlock 酿红酒", "给屋外的人浇水，找 Viktor，种血葡萄，做木桶（20 木材）酿红酒。"],
                ["市政厅登记", "Brook 帮你登记，认识小镇居民（Mina、Ludo、Saga、Noel、Elvira、Dragan、Sabrina、Aras、Samael、Luna）。"],
                ["鱼竿", "第二天晚上 Noel 的海边挑战——保留鱼竿 +250 金币。"],
                ["猫形态", "Ambrosia 庄园的晚宴解锁猫形态（移动更快）。"],
                ["第一个咒语", "在 Sabrina 处修好魔杖，Luna 教你 Aquaflux I 与魔法作物。"],
            ]},
            2: {"heading": "中后期快速路线（第 3–8 部分）", "items": [
                ["铁与魔力", "在 Cave of Echoes 挖铁矿；用 Crystal Cave 的 Rose Quartz 制作魔力萃取器。"],
                ["博物馆与 Nokturna", "帮 Jada 建博物馆（四大家族文物）；赢 Nokturna 收集卡牌。"],
                ["Webb 纹章与人鱼", "推进 Webb 家族线解锁人鱼形态。"],
                ["蝙蝠与 Khazan 纹章", "在月下见 Selene；Orlock 教你蝙蝠形态（带红酒）；跟随光点找到 Khazan 纹章。"],
                ["黄金与德古拉", "Cave of Echoes 深处的金矿（银镐）；完成“月光镇的黑暗”让德古拉一家搬来。"],
                ["通关后", "补完博物馆与图鉴、收集灵魂团、学全咒语与菜谱、解锁 Twilight Catacombs。"],
            ]},
            3: {},
        },
    },
    "ja": {
        "title": "ムーンライトピークス ストーリー攻略",
        "metaTitle": "メインストーリーを第1〜8部で解説",
        "metaDescription": "『Moonlight Peaks』メインストーリー完全攻略（8部）：ワイン計画、家紋、博物館、Nokturna、変身、金とドラキュラ編。",
        "intro": "メインストーリーは家族クエストと紋章、変身で進みます。最初の赤ワインからポストゲームまで全8部で解説。",
        "sections": {
            0: {"heading": "攻略パート（全8部）", "headers": ["パート", "タイトル", "内容"]},
            1: {"heading": "序盤の最短ルート（第1〜2部）", "items": [
                ["Orlock の赤ワイン", "家の外の男に水をかけ、Viktor に会い、Blood Grapes を植え、樽（木材20）でワインに。"],
                ["タウンホールで登録", "Brook が登録。住民に会う（Mina、Ludo、Saga、Noel、Elvira、Dragan、Sabrina、Aras、Samael、Luna）。"],
                ["釣り竿", "2日目の夜、Noel のチャレンジで竿+250コイン。"],
                ["猫変身", "Ambrosia Mansion の晩餐会で猫形態（移動が速い）。"],
                ["最初の呪文", "Sabrina で杖を修理し、Luna から Aquaflux I と魔法作物を。"],
            ]},
            2: {"heading": "中盤〜終盤の最短ルート（第3〜8部）", "items": [
                ["鉄とマナ", "Cave of Echoes で鉄鉱。Crystal Cave の Rose Quartz で Mana Extractor を作る。"],
                ["博物館と Nokturna", "Jada の博物館開設（四家族の遺物）。Nokturna でカードを。"],
                ["Webb 紋章と人魚", "Webb ストーリーを進めて人魚形態。"],
                ["蝙蝠と Khazan 紋章", "月下の Selene。Orlock が蝙蝠変身を（赤ワイン持参）。光の跡を追って Khazan 紋章。"],
                ["金とドラキュラ", "Cave of Echoes 奥の金鉱（銀ツルハシ）。「Darkness Over Moonlight Peaks」でドラキュラ一家を。"],
                ["ポストゲーム", "博物館・図鑑、ソウルブロブ、全呪文とレシピ、Twilight Catacombs。"],
            ]},
        },
    },
    "ko": {
        "title": "문라이트 피크스 메인 공략",
        "metaTitle": "메인 스토리 1~8부 단계별 공략",
        "metaDescription": "『문라이트 피크스』메인 스토리 완전 공략(8부): 와인 계획, 가문 문장, 박물관, Nokturna, 변신, 금과 드라큘라 스토리.",
        "intro": "메인 스토리는 가문 퀘스트와 문장, 변신으로 진행됩니다. Orlock을 위한 첫 레드 와인부터 포스트게임까지 8부로 정리했습니다.",
        "sections": {
            0: {"heading": "공략 파트(8부)", "headers": ["파트", "제목", "내용"]},
            1: {"heading": "초반 빠른 루트(1~2부)", "items": [
                ["Orlock의 레드 와인", "집 밖 남자에게 물을 붓고, Viktor를 만나고, Blood Grapes를 심고, 술통(나무20)으로 와인 제작."],
                ["타운홀 등록", "Brook이 등록. 주민들을 만나기(Mina, Ludo, Saga, Noel, Elvira, Dragan, Sabrina, Aras, Samael, Luna)."],
                ["낚싯대", "둘째 날 밤 Noel 도전으로 낚싯대 +250코인."],
                ["고양이 변신", "Ambrosia Mansion 만찬에서 고양이 형태(빠른 이동)."],
                ["첫 주문", "Sabrina에게서 지팡이 수리, Luna에게 Aquaflux I과 마법 작물 학습."],
            ]},
            2: {"heading": "중후반 빠른 루트(3~8부)", "items": [
                ["철과 마나", "Cave of Echoes에서 철광. Crystal Cave의 Rose Quartz로 Mana Extractor 제작."],
                ["박물관과 Nokturna", "Jada의 박물관 개관(네 가문 유물). Nokturna에서 카드 수집."],
                ["Webb 문장과 인어", "Webb 스토리를 진행해 인어 형태 해금."],
                ["박쥐와 Khazan 문장", "달빛 아래 Selene. Orlock이 박쥐 변신을(레드 와인 지참). 빛의 흔적을 따라 Khazan 문장."],
                ["금과 드라큘라", "Cave of Echoes 깊은 곳의 금광(은 곡괭이). 'Darkness Over Moonlight Peaks'로 드라큘라 가족을."],
                ["포스트게임", "박물관·도감, 소울 블롭, 전체 주문과 레시피, Twilight Catacombs."],
            ]},
        },
    },
    "fr": {
        "title": "Soluce de Moonlight Peaks",
        "metaTitle": "La soluce de l'histoire principale en 8 parties",
        "metaDescription": "La soluce complète de Moonlight Peaks en 8 parties : le vin, les emblèmes, le musée, Nokturna, les transformations, l'or et l'histoire de Dracula.",
        "intro": "L'histoire principale avance au fil des quêtes familiales, des emblèmes et des transformations. Cette soluce couvre les 8 parties, du premier vin rouge pour Orlock au post-game.",
        "sections": {
            0: {"heading": "Parties de la soluce (8)", "headers": ["Partie", "Titre", "Contenu"]},
            1: {"heading": "Début rapide (parties 1–2)", "items": [
                ["Le vin rouge d'Orlock", "Versez de l'eau, trouvez Viktor, plantez des Blood Grapes, fabriquez un tonneau (20 bois) et faites du vin."],
                ["Inscription à l'Hôtel de Ville", "Brook vous inscrit ; rencontrez les habitants."],
                ["Canne à pêche", "Le défi de Noel la 2e nuit — gardez la canne +250 pièces."],
                ["Transformation chat", "La soirée à Ambrosia Mansion débloque la forme chat."],
                ["Premiers sorts", "Réparez la baguette chez Sabrina, puis Luna vous apprend Aquaflux I."],
            ]},
            2: {"heading": "Suite rapide (parties 3–8)", "items": [
                ["Fer et mana", "Minez le fer (Cave of Echoes) ; fabriquez l'extracteur de mana (Rose Quartz)."],
                ["Musée & Nokturna", "Aidez Jada pour le musée ; gagnez à Nokturna pour les cartes."],
                ["Emblème Webb & sirène", "Progressez dans l'histoire Webb pour la forme sirène."],
                ["Chauve-souris & emblème Khazan", "Selene sous la lune ; Orlock enseigne la forme chauve-souris ; suivez la traînée lumineuse."],
                ["Or & Dracula", "Or au fond de la Cave of Echoes ; terminez Darkness Over Moonlight Peaks."],
                ["Post-game", "Musée et journal, Soul Blobs, tous sorts et recettes, Twilight Catacombs."],
            ]},
        },
    },
    "de": {
        "title": "Komplettlösung für Moonlight Peaks",
        "metaTitle": "Die Hauptstory Schritt für Schritt (Teile 1–8)",
        "metaDescription": "Die komplette Hauptstory-Lösung in 8 Teilen: Wein, Wappen, Museum, Nokturna, Verwandlungen, Gold und die Dracula-Story.",
        "intro": "Die Hauptstory wird von Familien-Quests, Wappen und Verwandlungen getrieben. Diese Lösung deckt die Story in 8 Teilen ab — vom ersten Rotwein für Orlock bis zum Post-Game.",
        "sections": {
            0: {"heading": "Lösungsteile (8)", "headers": ["Teil", "Titel", "Inhalt"]},
            1: {"heading": "Schneller Start (Teile 1–2)", "items": [
                ["Rotwein für Orlock", "Wasser über den Mann, triff Viktor, pflanze Blood Grapes, baue ein Fass (20 Holz) und mach Rotwein."],
                ["Im Rathaus registrieren", "Brook registriert dich; triff die Bewohner."],
                ["Angelrute", "Noels Herausforderung in Nacht 2 — Rute behalten +250 Münzen."],
                ["Katzenform", "Das Abendessen in Ambrosia Mansion schaltet die Katzenform frei."],
                ["Erste Zauber", "Repariere den Stab bei Sabrina, dann lehrt Luna dich Aquaflux I."],
            ]},
            2: {"heading": "Schneller Verlauf (Teile 3–8)", "items": [
                ["Eisen & Mana", "Baue Eisen (Cave of Echoes) ab; baue den Mana-Extraktor (Rose Quartz)."],
                ["Museum & Nokturna", "Hilf Jada beim Museum; gewinne Nokturna für Karten."],
                ["Webb-Wappen & Meerjungfrau", "Schließe die Webb-Story ab, um die Meerjungfrau-Form zu erhalten."],
                ["Fledermaus & Khazan-Wappen", "Selene unter dem Mond; Orlock lehrt die Fledermausform; folge der Lichtspur."],
                ["Gold & Dracula", "Gold tief in der Cave of Echoes; schließe Darkness Over Moonlight Peaks ab."],
                ["Post-Game", "Museum und Journal, Soul Blobs, alle Zauber und Rezepte, Twilight Catacombs."],
            ]},
        },
    },
}

# =====================================================================
# RELATIONSHIPS（好感机制 · techraptor/bonus-action L2）
# =====================================================================
REL_EN = {
    "slug": "moonlight-peaks/relationships",
    "title": "Moonlight Peaks Relationships: Hearts, Gifts & Dates",
    "metaTitle": "How Relationships Work in Moonlight Peaks: Hearts, Gifts & Dating",
    "metaDescription": "How hearts, gifts and dating work in Moonlight Peaks: one gift per day, liked/loved bonuses, heart level 4 dates, marriage and friendship with non-dateable NPCs.",
    "intro": "Relationships in Moonlight Peaks run on heart levels. Talk to a character and give one gift per day, then grow hearts to unlock hugs, dates and marriage. This page explains the mechanics.",
    "sections": [
        T(["Mechanic", "How it works"], [
            ["Daily routine", "Talk to each character and give one gift per day for a relationship-point boost."],
            ["Gift quality", "Gifts they like or love grant extra points — liked gifts are marked with a star, loved items with a heart in the previously-gifted list."],
            ["Heart levels", "Higher hearts unlock new interactions. Hugs come at heart level 3; dating starts at heart level 4."],
            ["Dates", "Invite a character out and play dating minigames. Dates can fail if you ignore instructions or arrive late — losing friendship points."],
            ["Marriage", "Max out your chosen romance and propose. You can only marry one character."],
            ["Non-dateable NPCs", "A dozen-plus extra NPCs can still be befriended with gifts — useful for quests and the 'Social Butterfly' achievement."],
        ]),
        N("Friendship milestones", [
            "Heart level 3 — hug the character.",
            "Heart level 4 — ask them on a date; kissing unlocks during dates.",
            "Max heart — propose and marry ('Tied the Knot').",
            "Four hearts with every character — 'Social Butterfly' achievement.",
        ]),
        F([
            ["How many gifts can I give per day?", "One gift per character per day."],
            ["How do I know what a character likes?", "Gift a character an item and check the previously-gifted list: stars mark liked items, hearts mark loved items."],
            ["Can I befriend non-romanceable NPCs?", "Yes — over a dozen extra NPCs can be befriended with gifts and dialogue."],
            ["What happens if I fail a date?", "You lose friendship points. Follow the instructions and arrive on time."],
        ]),
    ],
}

REL_I18N = {
    "zh-CN": {
        "title": "月光小镇 关系机制",
        "metaTitle": "月光小镇好感机制：心数·礼物·约会",
        "metaDescription": "《月光小镇》心数、礼物与约会机制：每天一件礼物、喜欢/最爱加成、心数 4 级约会、结婚与普通 NPC 交友。",
        "intro": "《月光小镇》的关系围绕心数展开：每天与角色交谈并送一件礼物，提升心数以解锁拥抱、约会与结婚。本页讲解完整机制。",
        "sections": {
            0: {"headers": ["机制", "说明"], "rows": [
                ["每日互动", "每天与每个角色交谈并赠送一件礼物，获得关系点。"],
                ["礼物质量", "喜欢/最爱的礼物额外加分——已赠列表里，喜欢用星标、最爱用心标。"],
                ["心数等级", "心数越高解锁越多互动：3 级可拥抱，4 级开始约会。"],
                ["约会", "邀请角色外出并玩约会小游戏。若忽略提示或迟到会失败，损失好感。"],
                ["结婚", "把恋爱对象的心数刷满并求婚，一次只能与一人结婚。"],
                ["不可恋爱 NPC", "另有十多位 NPC 可赠送礼物交友——对任务与“Social Butterfly”成就有用。"],
            ]},
            1: {"heading": "友情里程碑"},
            2: {},
        },
    },
    "ja": {
        "title": "ムーンライトピークス 関係の仕組み",
        "metaTitle": "ハート・贈り物・デートの仕組み",
        "metaDescription": "『Moonlight Peaks』のハート、贈り物、デート：毎日1つ、好物/大好物ボーナス、ハート4でデート、結婚、NPC との友情。",
        "intro": "関係はハートレベルで進みます。毎日会話と贈り物1つでハートを上げ、ハグ、デート、結婚を解放。",
        "sections": {
            0: {"headers": ["仕組み", "内容"], "rows": [
                ["毎日の行動", "各キャラに毎日会話と贈り物1つで関係ポイント。"],
                ["贈り物の質", "好物・大好物はボーナス。既に贈ったリストで星=好物、ハート=大好物。"],
                ["ハートレベル", "高くなると新たな行動。3でハグ、4でデート。"],
                ["デート", "ミニゲーム付き。指示を無視したり遅刻すると失敗し好感度減少。"],
                ["結婚", "選んだ相手を最大まで上げプロポーズ。複数とは結婚できません。"],
                ["NPC", "10人以上のNPCとも贈り物で友情を。クエストと「Social Butterfly」実績に。"],
            ]},
            1: {"heading": "友情のマイルストーン"},
        },
    },
    "ko": {
        "title": "문라이트 피크스 관계 시스템",
        "metaTitle": "하트·선물·데이트 방식",
        "metaDescription": "『문라이트 피크스』하트, 선물, 데이트: 하루 1개 선물, 좋아함/최애 보너스, 하트 4레벨 데이트, 결혼, NPC 우정.",
        "intro": "관계는 하트 레벨로 진행됩니다. 매일 대화와 선물 1개로 하트를 올려 포옹, 데이트, 결혼을 해금하세요.",
        "sections": {
            0: {"headers": ["시스템", "방식"], "rows": [
                ["매일 행동", "각 캐릭터에게 매일 대화 + 선물 1개로 관계 포인트."],
                ["선물 품질", "좋아함/최애는 보너스. 기존 선물 목록에서 별=좋아함, 하트=최애."],
                ["하트 레벨", "높을수록 더 많은 행동. 3에서 포옹, 4에서 데이트."],
                ["데이트", "미니게임 포함. 지시 무시나 지각 시 실패, 호감도 감소."],
                ["결혼", "선택한 상대를 최대로 올리고 프로포즈. 한 번에 한 명만."],
                ["NPC", "10명 이상의 NPC도 선물로 우정 가능. 퀘스트와 'Social Butterfly' 업적에 유용."],
            ]},
            1: {"heading": "우정 마일스톤"},
        },
    },
    "fr": {
        "title": "Relations dans Moonlight Peaks",
        "metaTitle": "Cœurs, cadeaux et rendez-vous",
        "metaDescription": "Comment fonctionnent cœurs, cadeaux et rendez-vous : un cadeau par jour, bonus aimé/adoré, rendez-vous au niveau de cœur 4, mariage et amitiés.",
        "intro": "Les relations passent par les niveaux de cœur. Parlez et offrez un cadeau par jour, puis montez les cœurs pour débloquer câlins, rendez-vous et mariage.",
        "sections": {
            0: {"headers": ["Mécanique", "Fonctionnement"], "rows": [
                ["Routine quotidienne", "Parlez et offrez un cadeau par personnage et par jour."],
                ["Qualité du cadeau", "Aimés/adorés donnent des points bonus — étoile = aimé, cœur = adoré."],
                ["Niveaux de cœur", "Câlin au niveau 3, rendez-vous au niveau 4."],
                ["Rendez-vous", "Mini-jeux ; peuvent échouer (retard, consignes ignorées) — perte de points."],
                ["Mariage", "Maxez la romance et proposez. Un seul mariage."],
                ["PNJ", "Plus d'une douzaine de PNJ peuvent être amis via cadeaux."],
            ]},
            1: {"heading": "Étapes d'amitié"},
        },
    },
    "de": {
        "title": "Beziehungen in Moonlight Peaks",
        "metaTitle": "Herzen, Geschenke und Dates",
        "metaDescription": "Wie Herzen, Geschenke und Dates funktionieren: ein Geschenk pro Tag, gemocht/geliebt-Boni, Dates ab Herz-Stufe 4, Heirat und Freundschaften.",
        "intro": "Beziehungen laufen über Herz-Stufen. Rede täglich und gib ein Geschenk, dann steigere Herzen für Umarmungen, Dates und Heirat.",
        "sections": {
            0: {"headers": ["Mechanik", "Funktionsweise"], "rows": [
                ["Tägliche Routine", "Rede mit jedem und gib ein Geschenk pro Tag."],
                ["Geschenkqualität", "Gemocht/geliebt gibt Bonus — Stern = gemocht, Herz = geliebt."],
                ["Herz-Stufen", "Umarmung ab Stufe 3, Dating ab Stufe 4."],
                ["Dates", "Minispiele; können scheitern (Verspätung, Anweisungen) — Verlust an Punkten."],
                ["Heirat", "Maximiere die Romanze und mach einen Heiratsantrag. Nur eine Ehe."],
                ["NPCs", "Über ein Dutzend NPCs sind per Geschenken befreundbar."],
            ]},
            1: {"heading": "Freundschafts-Meilensteine"},
        },
    },
}

# =====================================================================
# VILLAGERS（居民档案 · bonus-action L2 种族+角色；住所/商店部分来源）
# =====================================================================
VILL_ROWS = [
    ["Fiona", "Witch", "Coven circle / Webb of Wonders area", "Aloof witch with a feud with Orlock."],
    ["Noel", "Witch", "Rivers & coast", "Arrogant fisher-witch; haughty on the surface."],
    ["Sabrina", "Witch", "Webb of Wonders (magic shop)", "Sells spells, mana upgrades and inventory slots."],
    ["Luna", "Witch", "Her farm in Moonlit Pines / Town Hall bench", "Sells seeds and animals; loves any flower."],
    ["Orlock", "Vampire", "Ambrosia Mansion / The Broken Lamp", "Haunted vampire recovering from alcohol problems."],
    ["Evan", "Vampire", "Coffee and Coffins", "Laid-back; Orlock's child."],
    ["Mina", "Vampire", "Coffee and Coffins", "Bright and excitable; Orlock's other child."],
    ["Samael", "Vampire", "The Broken Lamp (after 23:00)", "Dark, mysterious, kind."],
    ["Elvira", "Vampire", "Around town / organizes gatherings", "Spirited event organizer."],
    ["Persephone", "Human", "Moves in Summer 24 Year 1", "Curious human with niece and nephew."],
    ["Jada", "Human", "With Persephone's quests", "Relic collector; runs the Museum questline."],
    ["Winston", "Human", "With Persephone's quests", "Afraid of supernaturals."],
    ["Saga", "Werewolf", "Town, Howling Marshes", "Tries to ease the Orlock–Brook feud."],
    ["Ridge", "Werewolf", "The Howling Hammer (tool shop)", "Sells tool upgrades; father of Ludo."],
    ["Ludo", "Werewolf", "Around town", "Prankster werewolf."],
    ["Dragan", "Seer", "Near his house / Nokturna", "Vision-struggling card player."],
    ["Alina", "Seer", "Near Dragan's house", "Intense, passionate seer."],
    ["Aras", "Seer", "Third Eye Threads (fashion)", "Kind, soft-spoken store owner."],
    ["Death", "Supernatural", "Near the Catacombs", "Tired of the job; gives the bug net."],
    ["Llemi", "Supernatural", "Before the Lovage festival", "Love demon; dateable."],
    ["Kim / Tae / Rei", "Mermaid", "Hidden", "Secret romance candidates."],
    ["Viktor", "NPC", "Dome building", "Gives the Red Wine quest; likes cheese."],
    ["Brook", "NPC", "Town Hall / mayor", "Werewolf mayor; registers you."],
    ["Jarvis", "NPC", "Around town (ghost)", "Tells you about the Chalice."],
    ["Chester", "NPC", "Your farm", "Shipping monster."],
]
VILL_EN = {
    "slug": "moonlight-peaks/villagers",
    "title": "Moonlight Peaks Villagers: Resident Directory",
    "metaTitle": "All Moonlight Peaks Villagers: Who, Where & What They Do",
    "metaDescription": "A directory of Moonlight Peaks residents: witches, vampires, werewolves, seers, humans, mermaids and more — where to find them and what they do.",
    "intro": "Moonlight Peaks is home to witches, vampires, werewolves, seers, humans, mermaids and stranger beings. Here's a quick directory of who lives where and what they offer.",
    "sections": [
        T(["Villager", "Affiliation", "Where / role", "Notes"], VILL_ROWS, heading="Resident directory (25 entries)"),
        N("Shops & services", [
            "Webb of Wonders (Sabrina): spells, mana upgrades, inventory slots.",
            "Third Eye Threads (Aras): clothes and fashion.",
            "The Howling Hammer (Ridge): tool upgrades, 18:00–24:00 Mon–Fri.",
            "Coffee and Coffins: drinks and ingredients (Evan & Mina).",
            "The Broken Lamp: bar, Samael after 23:00.",
            "Luna's farm (Moonlit Pines): seeds and animals.",
        ]),
        F([
            ["Who is the mayor?", "Brook, a werewolf, is the town's mayor — he registers you at the Town Hall."],
            ["Where do I buy seeds?", "From Luna's shop in Moonlit Pines."],
            ["Who upgrades my tools?", "Ridge at the Howling Hammer (open 18:00–24:00, Mon–Fri)."],
        ]),
    ],
}

VILL_I18N = {
    "zh-CN": {
        "title": "月光小镇 居民档案",
        "metaTitle": "月光小镇居民大全：谁·在哪·做什么",
        "metaDescription": "《月光小镇》居民目录：女巫、吸血鬼、狼人、先知、人类、人鱼等——在哪里找到他们、他们提供什么。",
        "intro": "月光小镇住着女巫、吸血鬼、狼人、先知、人类、人鱼与更奇特的生物。下面是谁住在哪、能提供什么的快速目录。",
        "sections": {
            0: {"heading": "居民目录（25 条）", "headers": ["居民", "种族", "位置/职能", "备注"]},
            1: {"heading": "商店与服务"},
            2: {},
        },
    },
    "ja": {
        "title": "ムーンライトピークス 住民",
        "metaTitle": "全住民：誰がどこで何を",
        "metaDescription": "『Moonlight Peaks』の住民名鑑：魔女、吸血鬼、狼人、予言者、人間、人魚など、居場所と役割。",
        "intro": "魔女、吸血鬼、狼人、予言者、人間、人魚、そしてもっと不思議な存在が住む町。誰がどこに住み、何を提供するかの名鑑です。",
        "sections": {
            0: {"heading": "住民名鑑（25人）", "headers": ["住民", "種族", "場所/役割", "備考"]},
            1: {"heading": "店とサービス"},
        },
    },
    "ko": {
        "title": "문라이트 피크스 주민",
        "metaTitle": "전체 주민: 누가 어디서 무엇을",
        "metaDescription": "『문라이트 피크스』주민 명부: 마녀, 뱀파이어, 늑대인간, 예언자, 인간, 인어 등 — 위치와 역할.",
        "intro": "마녀, 뱀파이어, 늑대인간, 예언자, 인간, 인어와 더 이상한 존재들이 사는 마을. 누가 어디에 살고 무엇을 제공하는지 정리한 명부입니다.",
        "sections": {
            0: {"heading": "주민 명부(25명)", "headers": ["주민", "종족", "위치/역할", "비고"]},
            1: {"heading": "상점과 서비스"},
        },
    },
    "fr": {
        "title": "Habitants de Moonlight Peaks",
        "metaTitle": "Tous les habitants : qui, où et leur rôle",
        "metaDescription": "Annuaire des habitants de Moonlight Peaks : sorcières, vampires, loups-garous, voyants, humains, sirènes — où les trouver et leur rôle.",
        "intro": "Moonlight Peaks abrite sorcières, vampires, loups-garous, voyants, humains, sirènes et bien plus. Un annuaire rapide de qui vit où et ce qu'ils offrent.",
        "sections": {
            0: {"heading": "Annuaire des habitants (25 entrées)", "headers": ["Habitant", "Affiliation", "Où / rôle", "Notes"]},
            1: {"heading": "Boutiques et services"},
        },
    },
    "de": {
        "title": "Bewohner von Moonlight Peaks",
        "metaTitle": "Alle Bewohner: wer, wo und was sie tun",
        "metaDescription": "Ein Verzeichnis der Bewohner von Moonlight Peaks: Hexen, Vampire, Werwölfe, Seher, Menschen, Meerjungfrauen — wo und welche Rolle.",
        "intro": "Moonlight Peaks ist Heimat von Hexen, Vampiren, Werwölfen, Sehern, Menschen, Meerjungfrauen und Seltsamerem. Ein schnelles Verzeichnis, wer wo lebt und was er bietet.",
        "sections": {
            0: {"heading": "Bewohner-Verzeichnis (25 Einträge)", "headers": ["Bewohner", "Zugehörigkeit", "Wo / Rolle", "Hinweise"]},
            1: {"heading": "Läden & Dienste"},
        },
    },
}

# =====================================================================
# POTIONS（部分数据待补 · 已知：魔力药水/药效叠加成就/药水制作解锁于 Part4）
# =====================================================================
POT_EN = {
    "slug": "moonlight-peaks/potions",
    "title": "Moonlight Peaks Potions: Recipes & Effects",
    "metaTitle": "Moonlight Peaks Potions: All 9 Recipes & Effects",
    "metaDescription": "All Moonlight Peaks potion recipes: effects, ingredients and sell prices for 9 potions, plus how to unlock potion-making and the 'A Magical Cocktail' achievement.",
    "intro": "Potion-making in Moonlight Peaks unlocks through the main story (part 4) and uses the cauldron with foraged and grown ingredients. All 9 recipes below (ingredients and sell prices included) are collected from gamer.org (L2, 2026-08-12).",
    "sections": [
        T(["Potion", "Effect", "Ingredients", "Sell price"], [
            ["Alter Ego Elixir", "Changes your appearance", "Quartz Dust, Nightshade Powder, Honey", "1,000"],
            ["Sunscreen Potion", "Protects you from sunlight", "Fiber, Egg", "45"],
            ["Mindless Miner Tonic", "Removes energy cost while mining", "Gold Ore, Leftsee, Glowglammer, Nightshade Powder", "1,300"],
            ["Frictionless Farming Tonic", "Removes energy cost while farming", "Onion, Honey, Googly Garlic Powder, Heart Stone", "990"],
            ["Fluent Fishing Tonic", "Removes energy cost while fishing", "Splotch, Glow Ginger Powder, Sugar, Volacio Mushroom", "700"],
            ["Fierce Forester Tonic", "Removes energy cost while chopping wood", "Sage Powder, Amanita, Light Wood, Cranberry", "950"],
            ["Rapid Reel Potion", "Fish bite almost instantly", "Angry Mandrake, Wolfsbane Powder, Sugar, Whisper", "700"],
            ["Love Potion", "Slightly increases friendship gained from gifts", "Hold-Me-Close, Muse Nut, Amour, Suffrain Powder, Luck Dust", "2,200"],
            ["Mana Potion", "Restores 8 Mana", "Mana Essence, Drikker, Henbane Powder, Violet, Frosteria", "3,200"],
        ], heading="All 9 known potions & recipes"),
        S("How potion-making works (verified)", [
            ["Unlock", "Potion-making becomes available during the main story (walkthrough part 4: Museum, Nokturna & Potion-Making)."],
            ["Cauldron & ingredients", "Use the cauldron with ingredients you grow or forage (herbs, fruits, magical crops)."],
            ["Effects stack", "Drinking multiple potions lets effects stack — the 'A Magical Cocktail' achievement needs every potion effect active at once."],
        ]),
        F([
            ["When do I unlock potions?", "During the main story — potion-making is covered in walkthrough part 4."],
            ["Which potion restores mana?", "The Mana Potion restores 8 Mana (it's also a loved gift for Noel)."],
            ["Which potion sells for the most?", "The Mana Potion (3,200 Coins) — the priciest recipe found so far."],
            ["Is Red Wine a potion?", "No — it's a keg item (a quest item for Orlock and a loved gift), not brewed in the cauldron."],
            ["How do I get 'A Magical Cocktail'?", "Stockpile potions, then drink each one in quick succession so every effect is active at the same time."],
        ]),
    ],
}

POT_I18N = {
    "zh-CN": {
        "title": "月光小镇 药水配方",
        "metaTitle": "月光小镇药水：全部 9 个配方与效果",
        "metaDescription": "《月光小镇》全部药水配方：9 种药水的效果、材料与售价，以及药水制作解锁方式与“魔法鸡尾酒”成就。",
        "intro": "《月光小镇》的药水制作随主线（第 4 部分）解锁，使用坩埚配合采集与种植的原料。以下为已核实的全部 9 个配方（含材料与售价，来源 gamer.org，2026-08-12 采集）。",
        "sections": {
            0: {"heading": "全部 9 个已知配方", "headers": ["药水", "效果", "材料", "售价"]},
            1: {"heading": "药水制作机制（已核实）", "items": [
                ["解锁", "主线推进到第 4 部分（博物馆、Nokturna 与药水制作）时解锁。"],
                ["坩埚与原料", "用坩埚配合种植或采集的原料（药草、水果、魔法作物）。"],
                ["效果叠加", "同时喝下多种药水可叠加效果——“魔法鸡尾酒”成就需要所有药效同时生效。"],
            ]},
            2: {},
        },
    },
    "ja": {
        "title": "ムーンライトピークス ポーション",
        "metaTitle": "ポーション：全9レシピと効果",
        "metaDescription": "『Moonlight Peaks』全ポーションレシピ：9種の効果・材料・売値と、解放方法と「A Magical Cocktail」実績。",
        "intro": "ポーション作りはメインストーリー（第4部）で解放され、大釜に採取・栽培した材料を入れて作ります。以下は検証済みの全9レシピ（材料・売値込み、出典 gamer.org、2026-08-12 収集）。",
        "sections": {
            0: {"heading": "判明している全9種", "headers": ["ポーション", "効果", "材料", "売値"]},
            1: {"heading": "ポーション作りの仕組み（検証済み）", "items": [
                ["解放", "メインストーリー第4部で利用可能に。"],
                ["大釜と材料", "大釜に採取・栽培した材料（ハーブ、果実、魔法作物）。"],
                ["効果の重複", "複数を飲むと効果が重なる。全効果同時で「A Magical Cocktail」。"],
            ]},
        },
    },
    "ko": {
        "title": "문라이트 피크스 물약",
        "metaTitle": "물약: 전체 9개 레시피와 효과",
        "metaDescription": "『문라이트 피크스』전체 물약 레시피: 9종의 효과·재료·판매가와 해금 방법, 'A Magical Cocktail' 업적.",
        "intro": "물약 제작은 메인 스토리(4부)에서 해금되며, 가마솥에 재배·채집한 재료를 넣어 만듭니다. 아래는 검증된 전체 9개 레시피입니다(재료·판매가 포함, 출처 gamer.org, 2026-08-12 수집).",
        "sections": {
            0: {"heading": "전체 9종 레시피", "headers": ["물약", "효과", "재료", "판매가"]},
            1: {"heading": "물약 제작 방식(검증됨)", "items": [
                ["해금", "메인 스토리 4부에서 사용 가능."],
                ["가마솥과 재료", "재배·채집한 재료(허브, 과일, 마법 작물)를 가마솥에."],
                ["효과 중첩", "여러 물약을 마시면 효과가 중첩. 전부 동시에 켜면 'A Magical Cocktail'."],
            ]},
        },
    },
    "fr": {
        "title": "Potions de Moonlight Peaks",
        "metaTitle": "Potions : les 9 recettes et effets",
        "metaDescription": "Toutes les recettes de potions de Moonlight Peaks : effets, ingrédients et prix de vente pour 9 potions, plus le déblocage et le succès 'A Magical Cocktail'.",
        "intro": "Les potions se débloquent dans l'histoire (partie 4) avec un chaudron et des ingrédients cultivés ou cueillis. Voici les 9 recettes vérifiées (ingrédients et prix inclus, source : gamer.org, collecté le 12/08/2026).",
        "sections": {
            0: {"heading": "Les 9 potions connues", "headers": ["Potion", "Effet", "Ingrédients", "Prix de vente"]},
            1: {"heading": "Fabrication (vérifié)", "items": [
                ["Déblocage", "Disponible pendant l'histoire principale (partie 4)."],
                ["Chaudron & ingrédients", "Chaudron + ingrédients cultivés/cueillis."],
                ["Effets cumulés", "Boire plusieurs potions cumule les effets — 'A Magical Cocktail'."],
            ]},
        },
    },
    "de": {
        "title": "Tränke in Moonlight Peaks",
        "metaTitle": "Tränke: alle 9 Rezepte und Effekte",
        "metaDescription": "Alle Trank-Rezepte in Moonlight Peaks: Effekte, Zutaten und Verkaufspreise für 9 Tränke, plus Freischaltung und der Erfolg 'A Magical Cocktail'.",
        "intro": "Tränke schaltest du in der Hauptstory (Teil 4) frei: Kessel plus angebaute/gesammelte Zutaten. Hier sind alle 9 verifizierten Rezepte (Zutaten und Preise inklusive, Quelle: gamer.org, erfasst am 12.08.2026).",
        "sections": {
            0: {"heading": "Alle 9 bekannten Tränke", "headers": ["Trank", "Effekt", "Zutaten", "Verkaufspreis"]},
            1: {"heading": "Herstellung (verifiziert)", "items": [
                ["Freischalten", "Verfügbar in der Hauptstory (Teil 4)."],
                ["Kessel & Zutaten", "Kessel + angebaute/gesammelte Zutaten."],
                ["Effekte stapeln", "Mehrere Tränke stapeln Effekte — 'A Magical Cocktail'."],
            ]},
        },
    },
}

# =====================================================================
# MUSEUM（成就+主线已知 · 细节待补）
# =====================================================================
MUS_EN = {
    "slug": "moonlight-peaks/museum",
    "title": "Moonlight Peaks Museum: How to Open & Complete It",
    "metaTitle": "Moonlight Peaks Museum: Opening, Donations & Completion",
    "metaDescription": "How to open and complete the Museum in Moonlight Peaks: Jada's questline, the five exhibit rooms (incl. Deity Room artifacts), the aquarium collection and the completion achievement.",
    "intro": "The Museum in Moonlight Peaks is opened through Jada's questline and completed by donating fish, flowers, artifacts and collectibles. It has five exhibit rooms — Critters, Deity, Farming, Supernatural and Aquarium. This page collects what's verified.",
    "sections": [
        S("How to open the Museum", [
            ["Start the questline", "Continue the story and Jada will mention wanting to set up her museum ('Museum in the Making')."],
            ["Gather family artifacts", "She wants artifacts from the four major families — talk to Brook, Orlock, Fiona and Dragan."],
            ["The four requests", "Orlock asks for Red Wine; Dragan needs you to play Nokturna; Fiona wants one Nightshade; Brook asks for Wolfsbane (via Saga)."],
            ["Return & exhibit", "Return the artifacts to Jada and visit her exhibition the next day to open the Museum."],
        ]),
        N("The five exhibit rooms", [
            "Critters Room — small creatures and critters.",
            "Deity Room — divine artifacts from the gods (see the table below).",
            "Farming Room — farming collectibles (including Amanita, grown in summer and autumn).",
            "Supernatural Room — supernatural relics.",
            "Aquarium Room — the fish collection (all 22 fish for 'Fishing Pro').",
        ]),
        T(["Artifact", "How to get it"], [
            ["Death's Tomb", "Reach max friendship with Death."],
            ["Chakra Tuner", "Reach max friendship with the Moon Goddess."],
            ["Sun God's Halo", "Reach max friendship with the Sun God."],
            ["Llemi's Bow", "Reach max friendship with Llemi."],
        ], heading="Deity Room artifacts (4)"),
        N("Completion & achievements", [
            "'Archaeo-Logistics' — open the Museum.",
            "'One Collection to Rule Them All' — complete the Museum (donate everything).",
            "'Skulls in a Net' — collect every Soul Blob.",
            "'Back to the Den' — return every Vampster to its den.",
            "'Back in Place' — return every plastic chair.",
            "'Fishing Pro' — donate/catch all 22 fish for the Aquarium Collection.",
        ]),
        F([
            ["Who runs the Museum questline?", "Jada, the relic collector (unlocks with Persephone's story)."],
            ["What do I donate?", "Fish (Aquarium Collection), flowers, artifacts and collectibles like Soul Blobs."],
            ["Is the Museum required for 100%?", "Yes — completing it is needed for 'One Collection to Rule Them All'."],
        ]),
    ],
}

MUS_I18N = {
    "zh-CN": {
        "title": "月光小镇 博物馆",
        "metaTitle": "月光小镇博物馆：开启·捐赠·完成",
        "metaDescription": "《月光小镇》博物馆怎么开、捐什么、怎么完成：Jada 任务线、四大家族文物、水族馆收集与完成成就。",
        "intro": "《月光小镇》的博物馆通过 Jada 的任务线开启，通过捐赠鱼、花、文物与收藏品完成。本页汇总已核实内容。",
        "sections": {
            0: {"heading": "如何开启博物馆", "items": [
                ["开始任务线", "推进剧情，Jada 会提起想建博物馆（“Museum in the Making”）。"],
                ["收集家族文物", "她需要四大家族的文物——与 Brook、Orlock、Fiona、Dragan 对话。"],
                ["四个请求", "Orlock 要红酒；Dragan 要你玩 Nokturna；Fiona 要一份 Nightshade；Brook（经 Saga）要 Wolfsbane。"],
                ["归还与展览", "把文物交给 Jada，次日参观她的展览即可开启博物馆。"],
            ]},
            1: {"heading": "五个展室"},
            2: {"heading": "神室文物（4 件）", "headers": ["文物", "获取方式"]},
            3: {"heading": "完成与成就"},
            4: {},
        },
    },
    "ja": {
        "title": "ムーンライトピークス 博物館",
        "metaTitle": "博物館：開設・寄贈・完成",
        "metaDescription": "『Moonlight Peaks』博物館の開設、寄贈、完成：Jada のクエスト、四家族の遺物、水族館コレクションと実績。",
        "intro": "博物館は Jada のクエストで開設し、魚や花、遺物、コレクションを寄贈して完成。検証済みをまとめています。",
        "sections": {
            0: {"heading": "博物館の開設", "items": [
                ["クエスト開始", "ストーリーを進めると Jada が博物館を望む（「Museum in the Making」）。"],
                ["家族の遺物", "四家族の遺物が必要 — Brook、Orlock、Fiona、Dragan と話す。"],
                ["4つの依頼", "Orlock=赤ワイン、Dragan=Nokturna、Fiona=Nightshade、Brook（経由 Saga）=Wolfsbane。"],
                ["展示", "遺物を返し、翌日展示を見て開館。"],
            ]},
            1: {"heading": "5つの展示室"},
            2: {"heading": "神の間の遺物（4点）", "headers": ["遺物", "入手方法"]},
            3: {"heading": "完成と実績"},
            4: {},
        },
    },
    "ko": {
        "title": "문라이트 피크스 박물관",
        "metaTitle": "박물관: 개관·기증·완성",
        "metaDescription": "『문라이트 피크스』박물관 개관, 기증, 완성: Jada 퀘스트, 네 가문 유물, 수족관 컬렉션과 업적.",
        "intro": "박물관은 Jada의 퀘스트로 개관하고, 물고기·꽃·유물·수집품을 기증해 완성합니다. 검증된 내용을 정리했습니다.",
        "sections": {
            0: {"heading": "박물관 개관 방법", "items": [
                ["퀘스트 시작", "스토리를 진행하면 Jada가 박물관을 원함('Museum in the Making')."],
                ["가문 유물 수집", "네 가문의 유물 필요 — Brook, Orlock, Fiona, Dragan과 대화."],
                ["네 가지 요청", "Orlock=레드 와인, Dragan=Nokturna, Fiona=Nightshade, Brook(경유 Saga)=Wolfsbane."],
                ["전시", "유물을 돌려주고 다음 날 전시를 보면 개관."],
            ]},
            1: {"heading": "다섯 개의 전시실"},
            2: {"heading": "신의 방 유물(4점)", "headers": ["유물", "획득 방법"]},
            3: {"heading": "완성과 업적"},
            4: {},
        },
    },
    "fr": {
        "title": "Musée de Moonlight Peaks",
        "metaTitle": "Ouvrir et compléter le musée",
        "metaDescription": "Ouvrir et compléter le musée : la quête de Jada, les artefacts des quatre familles, l'aquarium et le succès de complétion.",
        "intro": "Le musée s'ouvre via la quête de Jada et se complète en donnant poissons, fleurs, artefacts et collections. Voici ce qui est vérifié.",
        "sections": {
            0: {"heading": "Ouvrir le musée", "items": [
                ["Lancer la quête", "Avancez dans l'histoire ; Jada veut créer son musée ('Museum in the Making')."],
                ["Artefacts familiaux", "Elle veut des artefacts des quatre grandes familles — parlez à Brook, Orlock, Fiona et Dragan."],
                ["Les quatre demandes", "Orlock : vin rouge ; Dragan : jouer à Nokturna ; Fiona : Nightshade ; Brook : Wolfsbane (via Saga)."],
                ["Exposition", "Rendez les artefacts et visitez l'exposition le lendemain."],
            ]},
            1: {"heading": "Les cinq salles d'exposition"},
            2: {"heading": "Artefacts de la salle divine (4)", "headers": ["Artefact", "Comment l'obtenir"]},
            3: {"heading": "Complétion & succès"},
            4: {},
        },
    },
    "de": {
        "title": "Museum in Moonlight Peaks",
        "metaTitle": "Museum öffnen und vervollständigen",
        "metaDescription": "Museum öffnen und vervollständigen: Jadas Questreihe, Artefakte der vier Familien, Aquariensammlung und der Abschluss-Erfolg.",
        "intro": "Das Museum öffnet sich über Jadas Questreihe und wird durch Spenden von Fischen, Blumen, Artefakten und Sammelstücken vervollständigt.",
        "sections": {
            0: {"heading": "Museum öffnen", "items": [
                ["Quest starten", "Setze die Story fort; Jada will ihr Museum ('Museum in the Making')."],
                ["Familien-Artefakte", "Sie will Artefakte der vier großen Familien — sprich mit Brook, Orlock, Fiona und Dragan."],
                ["Die vier Bitten", "Orlock: Rotwein ; Dragan: Nokturna spielen ; Fiona: Nightshade ; Brook: Wolfsbane (via Saga)."],
                ["Ausstellung", "Gib die Artefakte zurück und besuche die Ausstellung am nächsten Tag."],
            ]},
            1: {"heading": "Die fünf Ausstellungsräume"},
            2: {"heading": "Artefakte des Götterraums (4)", "headers": ["Artefakt", "So erhältst du es"]},
            3: {"heading": "Abschluss & Erfolge"},
            4: {},
        },
    },
}

# =====================================================================
# BREEDING（动物养殖 · walkthrough 已知：cheekens/cowcula）
# =====================================================================
BREED_EN = {
    "slug": "moonlight-peaks/breeding",
    "title": "Moonlight Peaks Animals: Cheekens, Cowcula & More",
    "metaTitle": "Moonlight Peaks Animals: All 7 Farm Creatures & Prices",
    "metaDescription": "All Moonlight Peaks farm animals: Cheeken, Pig Goat, Draculamb, Cowcula, Bumpkin, Stoney and Rabbicula — unlock, purchase price and what each produces.",
    "intro": "Farm animals in Moonlight Peaks unlock after Luna's letter. Build a barn, adopt creatures from Luna's farm, feed them fodder and collect byproducts for cooking, quests and money. All 7 animals with prices below are from sportsrant (L2, 2026-08-12).",
    "sections": [
        S("How to get farm animals", [
            ["Luna's letter", "She writes to you when animals become available — visit her house for the cutscene."],
            ["Build a barn", "A barn costs 4,000 Coins at Ridge's shop. Clear land on your farm before purchasing."],
            ["Adopt creatures", "Go to Luna's farm and purchase creatures (e.g. Cheekens)."],
            ["Feed & collect", "Put fodder in the barn; creatures leave byproducts to collect."],
        ]),
        T(["Animal", "Unlock", "Purchase price", "Produces"], [
            ["Cheeken", "'Farm Animals for Sale' quest", "1,200", "Egg, Golden Egg"],
            ["Pig Goat", "Build a Barn", "3,500", "Piggoat Milk"],
            ["Draculamb", "Build a Barn", "4,500", "Draculamb Milk, Wool"],
            ["Cowcula", "Build a Barn", "6,000", "Cowcula Milk"],
            ["Bumpkin", "Reach Fall (Year 1)", "12,000", "Plops (compost)"],
            ["Stoney", "Reach Winter (Year 1)", "9,000", "Heart Stone"],
            ["Rabbicula", "Reach Spring (Year 2)", "2,800", "待补"],
        ], heading="All 7 known farm animals"),
        F([
            ["When do animals unlock?", "After Luna's letter — early game, around day 3."],
            ["How much is a barn?", "4,000 Coins at Ridge's shop (the Howling Hammer)."],
            ["Which animal pays off fastest?", "Cheeken (1,200) lays eggs daily — the cheapest entry; Bumpkin (Fall, 12,000) is the most expensive so far."],
            ["What can I do with eggs?", "Fried eggs are needed for the Hendersons' housewarming quest; eggs also cook into recipes."],
        ]),
    ],
}

BREED_I18N = {
    "zh-CN": {
        "title": "月光小镇 动物养殖",
        "metaTitle": "月光小镇动物：全部 7 种农场生物与价格",
        "metaDescription": "《月光小镇》全部农场动物：Cheeken、Pig Goat、Draculamb、Cowcula、Bumpkin、Stoney、Rabbicula——解锁方式、购买价与产出。",
        "intro": "收到 Luna 来信后解锁农场动物：建造谷仓、从 Luna 的农场领养生物、投放饲料并收集副产物用于烹饪、任务与赚钱。以下为全部 7 种动物及已核实价格（来源 sportsrant，2026-08-12 采集）。",
        "sections": {
            0: {"heading": "如何获得农场动物", "items": [
                ["Luna 的来信", "动物可用时她会来信——去她家触发过场。"],
                ["建造谷仓", "谷仓在 Ridge 的店铺售价 4,000 金币。购买前先在农场上清出空地。"],
                ["领养生物", "去 Luna 的农场购买生物（如 Cheekens）。"],
                ["喂养与收集", "在谷仓投放饲料；生物会留下副产物供收集。"],
            ]},
            1: {"heading": "全部 7 种已知动物", "headers": ["动物", "解锁", "购买价", "产出"]},
            2: {},
        },
    },
    "ja": {
        "title": "ムーンライトピークス 動物",
        "metaTitle": "動物：全7種の牧場生物と価格",
        "metaDescription": "『Moonlight Peaks』の全牧場動物：Cheeken、Pig Goat、Draculamb、Cowcula、Bumpkin、Stoney、Rabbicula——解放・購入価格・産物。",
        "intro": "Luna の手紙で動物が解放されます。納屋を建て、Luna の農場で動物を迎え、餌を与えて副産物を集めましょう。以下は全7種と確認済みの価格（出典 sportsrant、2026-08-12 収集）。",
        "sections": {
            0: {"heading": "動物の入手方法", "items": [
                ["Luna の手紙", "動物が利用可能になると届く。家を訪ねてカットシーン。"],
                ["納屋を建てる", "Ridge の店で4,000コイン。購入前に農地を空けておく。"],
                ["動物を迎える", "Luna の農場で購入（例：Cheekens）。"],
                ["餌と収穫", "納屋に餌を置くと副産物が。"],
            ]},
            1: {"heading": "判明している全7種", "headers": ["動物", "解放", "購入価格", "産物"]},
        },
    },
    "ko": {
        "title": "문라이트 피크스 동물",
        "metaTitle": "동물: 전체 7종 농장 생물과 가격",
        "metaDescription": "『문라이트 피크스』전체 농장 동물: Cheeken, Pig Goat, Draculamb, Cowcula, Bumpkin, Stoney, Rabbicula — 해금·구매 가격·생산물.",
        "intro": "Luna의 편지로 농장 동물이 해금됩니다. 헛간을 짓고, Luna 농장에서 생물을 입양하고, 사료를 주고 부산물을 모으세요. 아래는 전체 7종과 검증된 가격입니다(출처 sportsrant, 2026-08-12 수집).",
        "sections": {
            0: {"heading": "농장 동물 얻는 법", "items": [
                ["Luna의 편지", "동물이 가능해지면 편지가 옵니다. 집을 방문해 컷신."],
                ["헛간 짓기", "Ridge 상점에서 4,000코인. 구매 전에 농지를 비우세요."],
                ["입양", "Luna 농장에서 생물 구매(예: Cheekens)."],
                ["사료와 수확", "헛간에 사료를 넣으면 부산물이 생깁니다."],
            ]},
            1: {"heading": "전체 7종 확인", "headers": ["동물", "해금", "구매 가격", "생산물"]},
        },
    },
    "fr": {
        "title": "Animaux de Moonlight Peaks",
        "metaTitle": "Animaux : les 7 créatures de ferme et prix",
        "metaDescription": "Tous les animaux de ferme de Moonlight Peaks : Cheeken, Pig Goat, Draculamb, Cowcula, Bumpkin, Stoney et Rabbicula — déblocage, prix et produits.",
        "intro": "Les animaux se débloquent après la lettre de Luna. Construisez une grange, adoptez des créatures, nourrissez-les et collectez les sous-produits. Voici les 7 animaux et leurs prix vérifiés (source : sportsrant, collecté le 12/08/2026).",
        "sections": {
            0: {"heading": "Obtenir des animaux", "items": [
                ["Lettre de Luna", "Elle écrit quand les animaux sont disponibles — visitez sa maison."],
                ["Construire une grange", "4 000 pièces chez Ridge. Dégagez du terrain d'abord."],
                ["Adopter", "Achetez des créatures à la ferme de Luna (ex. Cheekens)."],
                ["Nourrir & collecter", "Du fourrage dans la grange ; sous-produits à collecter."],
            ]},
            1: {"heading": "Les 7 créatures connues", "headers": ["Animal", "Déblocage", "Prix d'achat", "Produits"]},
        },
    },
    "de": {
        "title": "Tiere in Moonlight Peaks",
        "metaTitle": "Tiere: alle 7 Hofkreaturen und Preise",
        "metaDescription": "Alle Hoftiere in Moonlight Peaks: Cheeken, Pig Goat, Draculamb, Cowcula, Bumpkin, Stoney und Rabbicula — Freischaltung, Kaufpreis, Produkte.",
        "intro": "Hoftiere schaltest du nach Lunas Brief frei. Baue eine Scheune, adoptiere Kreaturen, füttere sie und sammle Nebenprodukte. Hier alle 7 Tiere mit verifizierten Preisen (Quelle: sportsrant, erfasst am 12.08.2026).",
        "sections": {
            0: {"heading": "Tiere bekommen", "items": [
                ["Lunas Brief", "Sie schreibt, sobald Tiere verfügbar sind — besuche ihr Haus."],
                ["Scheune bauen", "4.000 Münzen bei Ridge. Räume vorher Land frei."],
                ["Adoptieren", "Kaufe Kreaturen auf Lunas Hof (z. B. Cheekens)."],
                ["Füttern & Sammeln", "Futter in die Scheune; Nebenprodukte sammeln."],
            ]},
            1: {"heading": "Alle 7 bekannten Tiere", "headers": ["Tier", "Freischaltung", "Kaufpreis", "Produkte"]},
        },
    },
}

# =====================================================================
# UPDATES（补丁日志 · vgspoilers L2 + Steam 官方发布）
# =====================================================================
UPD_ROWS = [
    ["1.1.45", "2026-07-21", "Added a photosensitivity warning at startup; fixed Star Gazing signs blocked by black bars on widescreen; fixed the Loveage Gift Exchange soft lock; fixed animals in Luna's shop disappearing after Pumpkin Head's heart event; boosted Weeping Willows respawn in the Howling Marshes; 'Back to the Den' now triggers (retroactive grant one in-game day after all Vampsters returned); fixed escaping the Recover the Moon quest; fixed Bee House / Firefly Sanctuary memory leaks; mouse, Farm Helpers and item-pickup performance; text fixes. More improvements are coming in 1.2."],
    ["1.1.44", "2026-07-16", "Fixed the invisible embroidery table; fixed failing to load after upgrading your house; tree seeds are now plantable in all seasons and show correct seasons; decorations on tables/shelves no longer consume inventory slots; crops no longer grow during rainy nights; fixed a corrupted save from quitting while saving (Steam only)."],
    ["1.1.41", "2026-07-15", "Faster loading; house storage across the whole plot (barns/greenhouses) with Quick Transfer; embroidery unlocks earlier; tree seeds show seasons; 23+ bug fixes (energy on missed net swings, save restoration, crop growth, cutscene triggers, gift responsiveness, house-upgrade inventory losses, Steam Deck controls, gamepad, crafted-item quality)."],
    ["1.1.38", "2026-07-10", "Fixed short freezes every 5–20s; fixed stuck slow-walk animation after exiting doors; fixed Nokturna 'new card' soft lock."],
    ["1.0 (Launch)", "2026-07-06/07", "Released on PC (Steam), Switch, Switch 2 and Google Play Games. Sales passed 200,000 by July 26."],
]
UPD_EN = {
    "slug": "moonlight-peaks/updates",
    "title": "Moonlight Peaks Updates & Patch Notes",
    "metaTitle": "Moonlight Peaks Patch Notes: 1.1.45, 1.1.44 & More",
    "metaDescription": "The latest Moonlight Peaks patch notes: 1.1.45 (photosensitivity warning, Star Gazing fix, 'Back to the Den'), 1.1.44 (embroidery table, tree seeds) and the 1.0 launch — updated as new patches drop.",
    "intro": "Little Chicken keeps Moonlight Peaks updated with regular patches. This page tracks the latest patch notes; it's updated whenever a new update ships.",
    "sections": [
        T(["Version", "Date", "Highlights"], UPD_ROWS, heading="Patch history"),
        N("How to update", [
            "Steam: updates install automatically when you launch the game.",
            "Switch / Switch 2: check for updates in the system menu; console patches follow the Steam release.",
            "Save files remain compatible across patches (1.1.41 fixed a save-restoration bug).",
        ]),
        F([
            ["What did patch 1.1.45 fix?", "A photosensitivity warning at startup, the Star Gazing widescreen black-bar bug, the Loveage Gift Exchange soft lock, animals vanishing from Luna's shop, the 'Back to the Den' achievement trigger (retroactive), Recover the Moon skip, Bee House/Firefly Sanctuary memory leaks, plus mouse/Farm Helpers/item-pickup performance. More is planned for 1.2."],
            ["What did patch 1.1.44 fix?", "The invisible embroidery table, failing to load after a house upgrade, all-season tree planting with correct season display, inventory slots for table/shelf decorations, rainy-night crop growth, and a save-corruption bug (Steam only)."],
            ["What did patch 1.1.41 fix?", "Loading times, house storage across the whole plot (incl. barns/greenhouses), earlier embroidery, season display on tree seeds, and 23+ bug fixes."],
            ["Is there a console version of the patches?", "Yes — console updates follow the Steam release (per NintendoReporters)."],
            ["Where can I see official notes?", "Steam news hub for app 2209900; we summarize verified patch notes here."],
        ]),
    ],
}

UPD_I18N = {
    "zh-CN": {
        "title": "月光小镇 更新日志",
        "metaTitle": "月光小镇补丁说明：1.1.45、1.1.44 等",
        "metaDescription": "《月光小镇》最新补丁说明：1.1.45（光敏警告、观星修复、“Back to the Den”）、1.1.44（刺绣桌、树苗）与 1.0 发布——随新补丁持续更新。",
        "intro": "Little Chicken 持续为《月光小镇》发布补丁。本页追踪最新补丁说明，每次新更新都会更新。",
        "sections": {
            0: {"heading": "补丁历史", "headers": ["版本", "日期", "要点"]},
            1: {"heading": "如何更新"},
            2: {},
        },
    },
    "ja": {
        "title": "ムーンライトピークス アップデート",
        "metaTitle": "パッチノート：1.1.45、1.1.44 ほか",
        "metaDescription": "『Moonlight Peaks』最新パッチ：1.1.45（光過敏警告、スターチェイジング修正、Back to the Den）、1.1.44（刺繍テーブル、苗木）、1.0 発売。",
        "intro": "Little Chicken はパッチを定期的に配信。最新のパッチノートを追跡します。",
        "sections": {
            0: {"heading": "パッチ履歴", "headers": ["バージョン", "日付", "ハイライト"]},
            1: {"heading": "アップデート方法"},
        },
    },
    "ko": {
        "title": "문라이트 피크스 업데이트",
        "metaTitle": "패치 노트: 1.1.45, 1.1.44 등",
        "metaDescription": "『문라이트 피크스』최신 패치: 1.1.45(광과민 경고, 별자리 관측 수정, Back to the Den), 1.1.44(자수 테이블, 묘목), 1.0 출시.",
        "intro": "Little Chicken이 정기적으로 패치를 배포합니다. 최신 패치 노트를 정리합니다.",
        "sections": {
            0: {"heading": "패치 기록", "headers": ["버전", "날짜", "핵심"]},
            1: {"heading": "업데이트 방법"},
        },
    },
    "fr": {
        "title": "Mises à jour de Moonlight Peaks",
        "metaTitle": "Notes de patch : 1.1.45, 1.1.44 et plus",
        "metaDescription": "Les dernières notes de patch : 1.1.45 (avertissement de photosensibilité, Star Gazing, 'Back to the Den'), 1.1.44 (table de broderie, pousses) et la sortie 1.0.",
        "intro": "Little Chicken met régulièrement Moonlight Peaks à jour. Cette page suit les dernières notes de patch.",
        "sections": {
            0: {"heading": "Historique des patchs", "headers": ["Version", "Date", "Points clés"]},
            1: {"heading": "Comment mettre à jour"},
        },
    },
    "de": {
        "title": "Updates für Moonlight Peaks",
        "metaTitle": "Patch-Notizen: 1.1.45, 1.1.44 und mehr",
        "metaDescription": "Die neuesten Patch-Notizen: 1.1.45 (Fotosensibilitäts-Warnung, Star Gazing, 'Back to the Den'), 1.1.44 (Sticktisch, Setzlinge) und der 1.0-Start.",
        "intro": "Little Chicken aktualisiert Moonlight Peaks regelmäßig. Diese Seite verfolgt die neuesten Patch-Notizen.",
        "sections": {
            0: {"heading": "Patch-Verlauf", "headers": ["Version", "Datum", "Highlights"]},
            1: {"heading": "So aktualisierst du"},
        },
    },
}

# =====================================================================
# STEAM DECK
# =====================================================================
SD_EN = {
    "slug": "moonlight-peaks/steam-deck",
    "title": "Moonlight Peaks on Steam Deck: Performance & Controls",
    "metaTitle": "Moonlight Peaks on Steam Deck: Does It Run Well?",
    "metaDescription": "Moonlight Peaks on Steam Deck: what we know about performance and controls, including 1.1.41 Steam Deck control fixes — official Verified status 待补.",
    "intro": "Moonlight Peaks supports controllers, cloud saves and family sharing on Steam. Here's what we know about Steam Deck so far; the official Steam Deck Verified status is still 待补.",
    "sections": [
        T(["Aspect", "What we know"], [
            ["Controller support", "Full controller support + Gamepad Recommended (official Steam categories)."],
            ["Steam Deck controls", "Patch 1.1.41 (2026-07-15) included Steam Deck control fixes."],
            ["Save / Cloud", "Steam Cloud supported."],
            ["Performance on Deck", "Community reports not yet collected — 待补."],
            ["Official Verified status", "待补 (not yet confirmed on the store page)."],
        ], heading="Steam Deck status"),
        N("Steam Deck settings to try", [
            "Cap framerate to 40–60 FPS for a stable handheld experience.",
            "Use the Deck's controller layout; the game recommends a gamepad.",
            "Update to 1.1.41+ for the latest Deck control fixes.",
        ]),
        F([
            ["Is Moonlight Peaks Steam Deck Verified?", "Not confirmed at time of writing (待补). It supports full controller input and cloud saves."],
            ["Does it run on Deck?", "It's a light cozy sim with modest requirements (see System Requirements) — community performance reports are still being collected."],
        ]),
    ],
}

SD_I18N = {
    "zh-CN": {
        "title": "月光小镇 Steam Deck 兼容",
        "metaTitle": "月光小镇 Steam Deck：运行与操作",
        "metaDescription": "《月光小镇》在 Steam Deck 上的表现：已知性能与操作信息，1.1.41 的 Deck 操作修复——官方 Verified 状态待补。",
        "intro": "《月光小镇》支持手柄、云存档与家庭共享。以下为目前已知的 Steam Deck 信息；官方 Verified 状态仍待补。",
        "sections": {
            0: {"heading": "Steam Deck 状态", "headers": ["方面", "已知信息"]},
            1: {"heading": "建议的设置"},
            2: {},
        },
    },
    "ja": {
        "title": "Steam Deck での動作",
        "metaTitle": "Steam Deck：性能と操作",
        "metaDescription": "『Moonlight Peaks』の Steam Deck 情報：既知の性能と操作、1.1.41 のコントロール修正。公式 Verified は待補。",
        "intro": "コントローラー、クラウドセーブ、ファミリーシェア対応。Steam Deck の既知情報をまとめています。",
        "sections": {
            0: {"heading": "Steam Deck の状態", "headers": ["項目", "判明分"]},
            1: {"heading": "おすすめ設定"},
        },
    },
    "ko": {
        "title": "Steam Deck 호환",
        "metaTitle": "Steam Deck: 성능과 조작",
        "metaDescription": "『문라이트 피크스』Steam Deck 정보: 알려진 성능과 조작, 1.1.41 조작 수정. 공식 Verified는 대기.",
        "intro": "컨트롤러, 클라우드 세이브, 패밀리 셰어링 지원. Steam Deck의 알려진 정보를 정리했습니다.",
        "sections": {
            0: {"heading": "Steam Deck 상태", "headers": ["항목", "알려진 정보"]},
            1: {"heading": "권장 설정"},
        },
    },
    "fr": {
        "title": "Moonlight Peaks sur Steam Deck",
        "metaTitle": "Steam Deck : performances et commandes",
        "metaDescription": "Moonlight Peaks sur Steam Deck : performances et commandes connues, correctifs 1.1.41 — statut officiel à confirmer.",
        "intro": "Moonlight Peaks prend en charge manettes, cloud et partage familial. Voici ce qu'on sait sur Steam Deck ; le statut officiel reste à confirmer.",
        "sections": {
            0: {"heading": "État Steam Deck", "headers": ["Aspect", "Ce qu'on sait"]},
            1: {"heading": "Réglages à essayer"},
        },
    },
    "de": {
        "title": "Moonlight Peaks auf Steam Deck",
        "metaTitle": "Steam Deck: Leistung und Steuerung",
        "metaDescription": "Moonlight Peaks auf Steam Deck: bekannte Leistung und Steuerung, 1.1.41-Steuerungsfixes — offizieller Status offen.",
        "intro": "Moonlight Peaks unterstützt Controller, Cloud-Saves und Family Sharing. Das wissen wir über Steam Deck; der offizielle Status ist offen.",
        "sections": {
            0: {"heading": "Steam-Deck-Status", "headers": ["Aspekt", "Was wir wissen"]},
            1: {"heading": "Empfohlene Einstellungen"},
        },
    },
}

# =====================================================================
# CONSOLE（Switch/Switch 2 · gematsu/Marvelous L1-L2）
# =====================================================================
CON_ROWS = [
    ["PC (Steam)", "2026-07-06", "Windows + macOS (no Linux)."],
    ["Nintendo Switch", "2026-07-07", "Published by Marvelous (XSEED)."],
    ["Nintendo Switch 2", "2026-07-07", "Available as 'Moonlight Peaks - Nintendo Switch 2 Edition'."],
    ["Google Play Games (Android)", "2026-07-07", "PC/Android via Google Play Games."],
]
CON_EN = {
    "slug": "moonlight-peaks/console",
    "title": "Moonlight Peaks Platforms: Switch, Switch 2, PC & More",
    "metaTitle": "Moonlight Peaks Platforms & Release Dates (Switch 2, Switch, PC)",
    "metaDescription": "Moonlight Peaks is out on PC (Steam), Nintendo Switch, Switch 2 and Google Play Games: release dates, publishers and console features.",
    "intro": "Moonlight Peaks launched July 6–7, 2026 on PC (Steam), Nintendo Switch, Nintendo Switch 2 and Google Play Games, published by XSEED Games (NA) and Marvelous Europe. Here's the platform breakdown.",
    "sections": [
        T(["Platform", "Release", "Notes"], CON_ROWS, heading="All platforms"),
        N("Console extras", [
            "Portrait styles: on Switch you can switch between two portrait presets (Settings → Portrait Style): cartoon with realistic shading, or anime-inspired.",
            "Switch 2 Edition: listed separately on the eShop (July 7, 2026).",
            "Console patches follow the Steam release (1.1.41 reached consoles after Steam).",
        ]),
        F([
            ["Which platforms is Moonlight Peaks on?", "PC (Steam), Nintendo Switch, Nintendo Switch 2 and Google Play Games (Android) — all launched July 6–7, 2026."],
            ["Who publishes the console versions?", "Marvelous Europe / XSEED Games."],
            ["Is there cross-save?", "Not confirmed — 待补."],
        ]),
    ],
}

CON_I18N = {
    "zh-CN": {
        "title": "月光小镇 平台与发售",
        "metaTitle": "月光小镇平台：Switch 2、Switch、PC",
        "metaDescription": "《月光小镇》已登陆 PC（Steam）、Switch、Switch 2 与 Google Play Games：发售日、发行商与控制台特性。",
        "intro": "《月光小镇》于 2026 年 7 月 6–7 日登陆 PC（Steam）、Switch、Switch 2 与 Google Play Games，由 XSEED Games（北美）与 Marvelous Europe 发行。以下是平台明细。",
        "sections": {
            0: {"heading": "全部平台", "headers": ["平台", "发售日", "备注"]},
            1: {"heading": "主机特色"},
            2: {},
        },
    },
    "ja": {
        "title": "対応プラットフォーム",
        "metaTitle": "対応機種と発売日（Switch 2、Switch、PC）",
        "metaDescription": "『Moonlight Peaks』は PC（Steam）、Switch、Switch 2、Google Play Games で発売中。発売日、発売元、機種別情報。",
        "intro": "2026年7月6〜7日に PC（Steam）、Switch、Switch 2、Google Play Games で発売。XSEED Games（北米）/ Marvelous Europe。",
        "sections": {
            0: {"heading": "全プラットフォーム", "headers": ["機種", "発売日", "備考"]},
            1: {"heading": "機種別の特長"},
        },
    },
    "ko": {
        "title": "플랫폼 안내",
        "metaTitle": "플랫폼과 출시일(Switch 2, Switch, PC)",
        "metaDescription": "『문라이트 피크스』는 PC(Steam), Switch, Switch 2, Google Play Games로 출시. 출시일, 배급사, 기기별 정보.",
        "intro": "2026년 7월 6~7일 PC(Steam), Switch, Switch 2, Google Play Games로 출시. XSEED Games(북미)/Marvelous Europe 배급.",
        "sections": {
            0: {"heading": "전체 플랫폼", "headers": ["플랫폼", "출시일", "비고"]},
            1: {"heading": "콘솔 특징"},
        },
    },
    "fr": {
        "title": "Plateformes de Moonlight Peaks",
        "metaTitle": "Plateformes et dates (Switch 2, Switch, PC)",
        "metaDescription": "Moonlight Peaks est disponible sur PC (Steam), Switch, Switch 2 et Google Play Games : dates, éditeurs et spécificités.",
        "intro": "Sorti les 6–7 juillet 2026 sur PC (Steam), Switch, Switch 2 et Google Play Games, édité par XSEED Games (NA) et Marvelous Europe.",
        "sections": {
            0: {"heading": "Toutes les plateformes", "headers": ["Plateforme", "Sortie", "Notes"]},
            1: {"heading": "Spécificités consoles"},
        },
    },
    "de": {
        "title": "Plattformen von Moonlight Peaks",
        "metaTitle": "Plattformen und Termine (Switch 2, Switch, PC)",
        "metaDescription": "Moonlight Peaks ist auf PC (Steam), Switch, Switch 2 und Google Play Games erschienen: Termine, Publisher und Konsolen-Features.",
        "intro": "Erschienen am 6.–7. Juli 2026 für PC (Steam), Switch, Switch 2 und Google Play Games, veröffentlicht von XSEED Games (NA) und Marvelous Europe.",
        "sections": {
            0: {"heading": "Alle Plattformen", "headers": ["Plattform", "Release", "Hinweise"]},
            1: {"heading": "Konsolen-Extras"},
        },
    },
}

# =====================================================================
# SYSTEM REQUIREMENTS（L1 Steam 官方）
# =====================================================================
SR_EN = {
    "slug": "moonlight-peaks/system-requirements",
    "title": "Moonlight Peaks System Requirements (PC)",
    "metaTitle": "Moonlight Peaks System Requirements: Minimum & Recommended",
    "metaDescription": "Official Moonlight Peaks PC system requirements: minimum and recommended specs (Windows 10, i3/GTX 660 and i7/GTX 960), plus macOS and storage.",
    "intro": "Official Moonlight Peaks system requirements for PC (Steam), straight from the store page. The game runs on Windows and macOS.",
    "sections": [
        T(["", "Minimum", "Recommended"], [
            ["OS", "Windows 10 64-bit", "Windows 10 64-bit"],
            ["Processor", "Intel i3", "Intel i7 / Ryzen 1700+"],
            ["Memory", "6 GB RAM", "16 GB RAM"],
            ["Graphics", "Nvidia GeForce GTX 660 2GB", "Nvidia GeForce GTX 960+"],
            ["DirectX", "Version 10", "Version 10"],
            ["Storage", "8 GB available", "8 GB available"],
        ], heading="PC requirements (official)"),
        N("Other platforms", [
            "macOS: supported (Mac version confirmed on Steam; macOS specs 待补).",
            "Linux: not listed (待补).",
            "Console requirements: N/A (Switch / Switch 2).",
        ]),
        F([
            ["Can I run it on a low-end PC?", "Minimum is modest: Windows 10, Intel i3, 6 GB RAM, GTX 660 2GB, 8 GB storage."],
            ["Is there a Mac version?", "Yes — macOS is listed as supported on Steam."],
        ]),
    ],
}

SR_I18N = {
    "zh-CN": {
        "title": "月光小镇 配置要求",
        "metaTitle": "月光小镇配置要求：最低与推荐",
        "metaDescription": "《月光小镇》官方 PC 配置要求：最低/推荐（Win10、i3/GTX660 与 i7/GTX960），以及 macOS 与存储。",
        "intro": "《月光小镇》官方 PC 配置要求，直接来自 Steam 商店页。游戏支持 Windows 与 macOS。",
        "sections": {
            0: {"heading": "PC 配置（官方）", "headers": ["", "最低", "推荐"]},
            1: {"heading": "其他平台"},
            2: {},
        },
    },
    "ja": {
        "title": "動作環境（PC）",
        "metaTitle": "動作環境：最低・推奨",
        "metaDescription": "『Moonlight Peaks』公式のPC動作環境：最低・推奨（Win10、i3/GTX660、i7/GTX960）、macOSと容量。",
        "intro": "Steam ストアの公式動作環境。Windows と macOS に対応。",
        "sections": {
            0: {"heading": "PC 動作環境（公式）", "headers": ["", "最低", "推奨"]},
            1: {"heading": "他のプラットフォーム"},
        },
    },
    "ko": {
        "title": "시스템 요구 사항(PC)",
        "metaTitle": "시스템 요구 사항: 최소·권장",
        "metaDescription": "『문라이트 피크스』공식 PC 요구 사항: 최소·권장(Win10, i3/GTX660, i7/GTX960), macOS와 용량.",
        "intro": "Steam 상점의 공식 요구 사항. Windows와 macOS 지원.",
        "sections": {
            0: {"heading": "PC 요구 사항(공식)", "headers": ["", "최소", "권장"]},
            1: {"heading": "기타 플랫폼"},
        },
    },
    "fr": {
        "title": "Configuration requise (PC)",
        "metaTitle": "Configuration minimale et recommandée",
        "metaDescription": "Configuration officielle de Moonlight Peaks : minimale et recommandée (Win10, i3/GTX 660, i7/GTX 960), macOS et stockage.",
        "intro": "La configuration officielle, directement depuis la page Steam. Le jeu tourne sur Windows et macOS.",
        "sections": {
            0: {"heading": "Configuration PC (officielle)", "headers": ["", "Minimale", "Recommandée"]},
            1: {"heading": "Autres plateformes"},
        },
    },
    "de": {
        "title": "Systemanforderungen (PC)",
        "metaTitle": "Systemanforderungen: Minimum & empfohlen",
        "metaDescription": "Offizielle Systemanforderungen von Moonlight Peaks: Minimum und empfohlen (Win10, i3/GTX 660, i7/GTX 960), macOS und Speicher.",
        "intro": "Die offiziellen Anforderungen direkt von der Steam-Seite. Das Spiel läuft auf Windows und macOS.",
        "sections": {
            0: {"heading": "PC-Anforderungen (offiziell)", "headers": ["", "Minimum", "Empfohlen"]},
            1: {"heading": "Andere Plattformen"},
        },
    },
}

# =====================================================================
# FAQ
# =====================================================================
FAQ_EN = {
    "slug": "moonlight-peaks/faq",
    "title": "Moonlight Peaks FAQ",
    "metaTitle": "Moonlight Peaks FAQ: Release, Platforms, Romance & More",
    "metaDescription": "Quick answers about Moonlight Peaks: release date, platforms, price, languages, romance count, children, vampire conversion and similar games.",
    "intro": "Quick answers to the most common Moonlight Peaks questions, gathered from the official store page and verified guides.",
    "sections": [
        F([
            ["When was Moonlight Peaks released?", "July 6, 2026 on Steam; July 7, 2026 on Switch, Switch 2 and Google Play Games."],
            ["What platforms is it on?", "PC (Steam), Nintendo Switch, Nintendo Switch 2 and Google Play Games (Android)."],
            ["How much does it cost?", "US$34.99 on Steam (full price at time of writing)."],
            ["Who makes it?", "Developed by Little Chicken; published by XSEED Games (NA) and Marvelous Europe."],
            ["What type of game is it?", "A cozy gothic life-sim: farming, magic, potions, fishing, relationships and romance — RPG + Simulation."],
            ["Which languages are supported?", "English, German, Japanese, Korean, Simplified Chinese and Traditional Chinese."],
            ["How many characters can you romance?", "23 romanceable characters at launch, including secret candidates."],
            ["Can you have children?", "No children mechanic, and none is planned."],
            ["Can you turn your partner into a vampire?", "Yes, per community reports — the mechanic is still being verified."],
            ["Is it like Stardew Valley?", "It shares the farming-sim loop but adds a gothic night-time setting, magic, transformations and supernatural romance."],
        ]),
        N("Still missing an answer?", [
            "Check the Gift Guide, Romance Guide, Fishing Guide and Walkthrough for deeper detail.",
            "Anything not verified is clearly marked 待补 — we update as sources confirm.",
        ]),
    ],
}

FAQ_I18N = {
    "zh-CN": {
        "title": "月光小镇 常见问题",
        "metaTitle": "月光小镇FAQ：发售·平台·恋爱等",
        "metaDescription": "《月光小镇》常见问题速答：发售日、平台、价格、语言、可攻略人数、子嗣、吸血鬼化与同类游戏。",
        "intro": "《月光小镇》最常见问题的快速解答，整理自官方商店页与已核实的攻略。",
        "sections": {
            0: {"heading": "常见问题", "items": [
                ["《月光小镇》什么时候发售？", "Steam 2026 年 7 月 6 日；Switch、Switch 2 与 Google Play Games 7 月 7 日。"],
                ["在哪些平台？", "PC（Steam）、Nintendo Switch、Switch 2 与 Google Play Games（Android）。"],
                ["多少钱？", "Steam 全价 US$34.99（截至撰写时）。"],
                ["谁开发的？", "Little Chicken 开发；XSEED Games（北美）与 Marvelous Europe 发行。"],
                ["是什么类型的游戏？", "哥特田园生活模拟：种田、魔法、药水、钓鱼、社交与恋爱——RPG + Simulation。"],
                ["支持哪些语言？", "英语、德语、日语、韩语、简体中文与繁体中文。"],
                ["能攻略多少人？", "首发 23 位可攻略角色，含隐藏候选。"],
                ["能生孩子吗？", "没有子嗣机制，官方暂无计划。"],
                ["能把伴侣变成吸血鬼吗？", "据社区报告可以——机制仍在核实中。"],
                ["像星露谷物语吗？", "共享农场模拟循环，但加入哥特夜晚场景、魔法、变身与超自然恋爱。"],
            ]},
            1: {"heading": "还有问题？"},
        },
    },
    "ja": {
        "title": "よくある質問",
        "metaTitle": "FAQ：発売・対応機種・恋愛など",
        "metaDescription": "『Moonlight Peaks』のよくある質問：発売日、対応機種、価格、言語、恋愛人数、子供、吸血鬼化など。",
        "intro": "公式ストアと検証済みガイドから集めたよくある質問の簡潔な回答。",
        "sections": {
            0: {"heading": "よくある質問", "items": [
                ["発売日は？", "Steam 2026年7月6日、Switch/Switch 2/Google Play Games は7月7日。"],
                ["対応機種は？", "PC（Steam）、Switch、Switch 2、Google Play Games（Android）。"],
                ["価格は？", "Steam で US$34.99（執筆時点の定価）。"],
                ["開発元は？", "Little Chicken 開発、XSEED Games（北米）/ Marvelous Europe 発売。"],
                ["どんなゲーム？", "ゴシック系スローライフ：農業、魔法、ポーション、釣り、交流、恋愛（RPG+Simulation）。"],
                ["対応言語は？", "英語、ドイツ語、日本語、韓国語、簡体字中国語、繁体字中国語。"],
                ["恋愛対象は何人？", "発売時点で23人（隠し候補含む）。"],
                ["子供は作れる？", "子供システムはなく、予定もありません。"],
                ["パートナーを吸血鬼にできる？", "コミュニティ報告では可能とのこと（検証中）。"],
                ["Stardew Valley みたい？", "農業シミュのループにゴシック夜、魔法、変身、超常恋愛を加えた作品。"],
            ]},
            1: {"heading": "他に質問があれば"},
        },
    },
    "ko": {
        "title": "자주 묻는 질문",
        "metaTitle": "FAQ: 출시·플랫폼·연애 등",
        "metaDescription": "『문라이트 피크스』자주 묻는 질문: 출시일, 플랫폼, 가격, 언어, 연애 인원, 자녀, 뱀파이어 전환 등.",
        "intro": "공식 스토어와 검증된 가이드에서 모은 자주 묻는 질문의 빠른 답변.",
        "sections": {
            0: {"heading": "자주 묻는 질문", "items": [
                ["출시일은?", "Steam 2026년 7월 6일, Switch/Switch 2/Google Play Games 7월 7일."],
                ["플랫폼은?", "PC(Steam), Switch, Switch 2, Google Play Games(Android)."],
                ["가격은?", "Steam 정가 US$34.99(작성 시점)."],
                ["개발사는?", "Little Chicken 개발, XSEED Games(북미)/Marvelous Europe 배급."],
                ["어떤 게임?", "고딕 감성 라이프 시뮬: 농사, 마법, 물약, 낚시, 교류, 연애(RPG+Simulation)."],
                ["지원 언어는?", "영어, 독일어, 일본어, 한국어, 간체 중국어, 번체 중국어."],
                ["연애 대상은 몇 명?", "출시 기준 23명(숨은 후보 포함)."],
                ["자녀는?", "자녀 시스템 없음, 계획도 없음."],
                ["파트너를 뱀파이어로?", "커뮤니티 보고로는 가능(검증 중)."],
                ["스타듀밸리 같은가요?", "농사 시뮬 루프에 고딕 밤, 마법, 변신, 초자연 연애를 더한 게임."],
            ]},
            1: {"heading": "더 궁금한 점이 있다면"},
        },
    },
    "fr": {
        "title": "FAQ Moonlight Peaks",
        "metaTitle": "FAQ : sortie, plateformes, romance et plus",
        "metaDescription": "Réponses rapides : date de sortie, plateformes, prix, langues, nombre de romances, enfants, conversion en vampire.",
        "intro": "Réponses rapides aux questions les plus courantes, issues de la page Steam officielle et de guides vérifiés.",
        "sections": {
            0: {"heading": "Questions fréquentes", "items": [
                ["Date de sortie ?", "6 juillet 2026 sur Steam ; 7 juillet sur Switch, Switch 2 et Google Play Games."],
                ["Plateformes ?", "PC (Steam), Switch, Switch 2 et Google Play Games (Android)."],
                ["Prix ?", "34,99 $ US sur Steam (prix plein au moment de l'écriture)."],
                ["Qui développe ?", "Little Chicken ; édité par XSEED Games (NA) et Marvelous Europe."],
                ["Type de jeu ?", "Life-sim gothique cosy : culture, magie, potions, pêche, relations et romance (RPG + Simulation)."],
                ["Langues ?", "Anglais, allemand, japonais, coréen, chinois simplifié et traditionnel."],
                ["Combien de romances ?", "23 personnages romantiques au lancement, dont des secrets."],
                ["Enfants ?", "Aucun mécanisme d'enfants et aucun prévu."],
                ["Transformer son partenaire en vampire ?", "Oui selon des rapports communautaires — à vérifier."],
                ["Comme Stardew Valley ?", "Même boucle de ferme, mais avec un cadre gothique nocturne, magie et romance surnaturelle."],
            ]},
            1: {"heading": "Toujours une question ?"},
        },
    },
    "de": {
        "title": "FAQ Moonlight Peaks",
        "metaTitle": "FAQ: Release, Plattformen, Romantik und mehr",
        "metaDescription": "Schnelle Antworten: Release, Plattformen, Preis, Sprachen, Anzahl Liebesoptionen, Kinder, Vampir-Wandlung.",
        "intro": "Schnelle Antworten auf die häufigsten Fragen, aus dem offiziellen Steam-Store und verifizierten Guides.",
        "sections": {
            0: {"heading": "Häufige Fragen", "items": [
                ["Wann erschienen?", "6. Juli 2026 auf Steam; 7. Juli auf Switch, Switch 2 und Google Play Games."],
                ["Plattformen?", "PC (Steam), Switch, Switch 2 und Google Play Games (Android)."],
                ["Preis?", "34,99 $ US auf Steam (Vollpreis zum Zeitpunkt der Erstellung)."],
                ["Wer entwickelt?", "Little Chicken; veröffentlicht von XSEED Games (NA) und Marvelous Europe."],
                ["Genre?", "Gemütliches Gothic-Life-Sim: Anbau, Magie, Tränke, Angeln, Beziehungen und Romantik (RPG + Simulation)."],
                ["Sprachen?", "Englisch, Deutsch, Japanisch, Koreanisch, vereinfachtes und traditionelles Chinesisch."],
                ["Wie viele Liebesoptionen?", "23 romantische Charaktere zum Start, inkl. Geheimkandidaten."],
                ["Kinder?", "Keine Kinder-Mechanik und keine geplant."],
                ["Partner zum Vampir machen?", "Ja laut Community-Berichten — noch zu verifizieren."],
                ["Wie Stardew Valley?", "Gleiche Farm-Loop, aber mit gotischer Nacht, Magie und übernatürlicher Romantik."],
            ]},
            1: {"heading": "Noch eine Frage?"},
        },
    },
}

# =====================================================================
# 装配：所有月光页（EN + 5 语 i18n + 补充翻译）
# =====================================================================
try:
    from moonlight_i18n_extra import EXTRA as MOON_EXTRA
except Exception:
    MOON_EXTRA = {}

def build_moon_pages():
    """返回月光页列表，供 build_content.py 追加到 d['pages']。"""
    pages = []
    specs = [
        (HOME_EN, HOME_I18N, True),
        (HTP_EN, HTP_I18N, False),
        (GIFTS_EN, GIFTS_I18N, False),
        (ROMANCE_EN, ROMANCE_I18N, False),
        (FISH_EN, FISH_I18N, False),
        (FLOWERS_EN, FLOWERS_I18N, False),
        (TOOLS_EN, TOOLS_I18N, False),
        (SPELLS_EN, SPELLS_I18N, False),
        (ACH_EN, ACH_I18N, False),
        (WT_EN, WT_I18N, False),
        (REL_EN, REL_I18N, False),
        (VILL_EN, VILL_I18N, False),
        (POT_EN, POT_I18N, False),
        (MUS_EN, MUS_I18N, False),
        (BREED_EN, BREED_I18N, False),
        (UPD_EN, UPD_I18N, False),
        (SD_EN, SD_I18N, False),
        (CON_EN, CON_I18N, False),
        (SR_EN, SR_I18N, False),
        (FAQ_EN, FAQ_I18N, False),
    ]
    for en, i18n, is_home in specs:
        page_i18n = _i18n(i18n, en["sections"])
        # 合并补充翻译（FAQ/笔记 section 覆盖）
        for _lg, _lang_ov in (MOON_EXTRA.get(en["slug"]) or {}).items():
            for _idx, _ov in _lang_ov.items():
                _secs = page_i18n.setdefault(_lg, {}).setdefault("sections", [])
                if 0 <= _idx < len(en["sections"]):
                    _merged = dict(en["sections"][_idx])
                    for _k in ("heading", "headers", "items", "body", "rows"):
                        if _k in _ov:
                            _merged[_k] = _ov[_k]
                    # 保持 sections 顺序：替换或插入
                    if _idx < len(_secs):
                        _secs[_idx] = _merged
                    else:
                        _secs.append(_merged)
        page = {
            "slug": en["slug"],
            "title": en["title"],
            "metaTitle": en["metaTitle"],
            "metaDescription": en["metaDescription"],
            "intro": en["intro"],
            "sections": en["sections"],
            "i18n": page_i18n,
            "priority": "P0",
            "_moon": True,
        }
        pages.append(page)
    return pages
