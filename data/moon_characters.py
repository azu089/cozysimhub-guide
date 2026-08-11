# -*- coding: utf-8 -*-
"""Moonlight Peaks 角色单页（P1）：hub + 核心角色档案页（6 语）。
数据源：ROMANCE_ROWS（bonus-action L2 全 23 角色 bio）+ GIFT_ROWS_EN（thegamer L2 礼物表）。
规则：角色名/物品名保留英文；散文/表头/FAQ 全翻译；未核实处标「待补」。
"""
from moonlight_pages import T, S, N, F, lang_page, GIFT_ROWS_EN, ROMANCE_ROWS

# ---------------------------------------------------------------- 基础数据
GIFT_MAP = {r[0]: [r[1], r[2], r[3]] for r in GIFT_ROWS_EN}
ROMANCE_MAP = {r[0]: {"affil": r[1], "appears": r[2], "personality": r[3]} for r in ROMANCE_ROWS}
CORE = ["Fiona", "Noel", "Sabrina", "Luna", "Orlock", "Evan"]
ALL_NAMES = [r[0] for r in ROMANCE_ROWS]

# ---------------------------------------------------------------- 语言模板
L = {
    "zh-CN": {
        "title_tpl": "月光小镇 {name} 角色档案：礼物与恋爱",
        "meta_title_tpl": "{name} 攻略：礼物、心动事件与恋爱指南",
        "meta_desc_tpl": "《月光小镇》{name} 角色档案：最爱/喜欢礼物、性格、登场时间与恋爱攻略。",
        "intro_tpl": "{name} 是《月光小镇》的可攻略角色之一。本页是 TA 的档案：最爱的礼物、性格，以及如何提升好感。",
        "sec_who": "TA 是谁", "sec_gifts": "礼物偏好", "sec_heart": "心动事件与恋爱", "sec_faq": "FAQ",
        "k_affil": "种族", "k_appears": "登场时间", "k_person": "性格",
        "gift_headers": ["最爱礼物", "喜欢礼物", "讨厌礼物"],
        "heart_note": ["{name} 的心动事件细节仍在收集中（待补）。", "恋爱在 TA 的心数达到 4 级后解锁：每天交谈，并送一件喜欢或最爱的礼物。"],
        "faq": [
            ["{name} 最爱什么礼物？", "TA 最爱：{loved}。"],
            ["什么时候可以和 {name} 约会？", "TA 在{appears}登场；心数达到 4 级即可约会。"],
            ["{name} 是隐藏角色吗？", "不是——{name} 是首发即可攻略的角色。"],
        ],
        "hub_title": "月光小镇 角色全览：23 位可攻略角色档案",
        "hub_meta_title": "月光小镇角色大全：23 位可攻略角色",
        "hub_meta_desc": "《月光小镇》23 位可攻略角色索引：种族、登场时间与性格，点击进入各角色礼物与恋爱档案。",
        "hub_intro": "《月光小镇》首发共有 23 位可攻略角色——女巫、吸血鬼、狼人、先知、人类、人鱼与更奇特的种族。点击角色卡进入对应的礼物与恋爱档案。",
        "hub_sec_cards": "全部 23 位角色",
        "hub_sec_note": "角色档案说明",
        "hub_note": ["每个角色卡都会链接到对应的档案页——礼物、性格与恋爱笔记。", "尚未开放单页的角色会链接到完整恋爱指南。"],
        "hub_faq": [
            ["有多少位可攻略角色？", "首发共 23 位（2026-07-07），含隐藏候选。"],
            ["为什么有些角色没有单独档案页？", "单页按优先级逐步补全——没有单页的角色信息都在恋爱指南全表里。"],
        ],
        "affil": {"Witch": "女巫", "Vampire": "吸血鬼", "Werewolf": "狼人", "Seer": "先知", "Human": "人类", "Mermaid": "人鱼", "Supernatural": "超自然存在"},
        "appears": {
            "Spring 1 Year 1": "第 1 年春 1 日", "Summer 24 Year 1": "第 1 年夏 24 日",
            "With Persephone's quests": "随 Persephone 任务线", "Story progression": "随剧情推进",
            "Spring before Lovage festival": "春季、Lovage 节前", "Hidden (TBA)": "隐藏（待补）",
        },
        "personality": {
            "Fiona": "外表疏离、对教团以外的人不感兴趣，与 Orlock 有宿怨，但隐藏着更深的故事。",
            "Noel": "傲慢、只顾自己，最爱钓鱼——高傲只是掩饰不安的面具。",
            "Sabrina": "专注的女巫，痴迷实验，聪明，偶尔被家族事务压得喘不过气。",
            "Luna": "神秘莫测，大部分时间待在花园或照料动物，对魔法造诣很深。",
            "Orlock": "饱受过去阴影折磨、有酗酒问题的吸血鬼；随着康复，浪漫而真挚的一面会绽放。",
            "Evan": "Orlock 的孩子，性格随和放松，享受当下，却为 Orlock 的沉沦而痛苦。",
        },
    },
    "ja": {
        "title_tpl": "ムーンライトピークス {name} キャラクター：贈り物と恋愛",
        "meta_title_tpl": "{name} 攻略：贈り物・ハートイベント・恋愛",
        "meta_desc_tpl": "『Moonlight Peaks』{name} のプロフィール：大好物・好物、性格、登場時期、恋愛のコツ。",
        "intro_tpl": "{name} は『Moonlight Peaks』の恋愛対象の一人。大好物の贈り物、性格、好感度の上げ方をまとめました。",
        "sec_who": "どんなキャラ？", "sec_gifts": "贈り物の好み", "sec_heart": "ハートイベントと恋愛", "sec_faq": "FAQ",
        "k_affil": "種族", "k_appears": "登場", "k_person": "性格",
        "gift_headers": ["大好物", "好物", "嫌いな物"],
        "heart_note": ["{name} のハートイベント詳細は収集中（待補）。", "ハートレベル4でデートが解放：毎日話しかけ、好物か大好物を1日1つ贈りましょう。"],
        "faq": [
            ["{name} の大好物は？", "大好物：{loved}。"],
            ["いつから {name} とデート？", "{appears}に登場。ハートレベル4でデート解放。"],
            ["{name} は隠しキャラ？", "いいえ——{name} は最初から攻略可能です。"],
        ],
        "hub_title": "キャラクター全覧：恋愛対象23人",
        "hub_meta_title": "キャラクター大全：恋愛対象23人",
        "hub_meta_desc": "『Moonlight Peaks』の恋愛対象23人を索引：種族・登場時期・性格。各キャラの贈り物・恋愛ページへ。",
        "hub_intro": "『Moonlight Peaks』発売時点の恋愛対象は23人——魔女、吸血鬼、狼人、予言者、人間、人魚など。カードから各キャラの贈り物・恋愛ページへ。",
        "hub_sec_cards": "全23人",
        "hub_sec_note": "プロフィールについて",
        "hub_note": ["各カードは対応するキャラページへ——贈り物・性格・恋愛ノート。", "単独ページ未作成のキャラは恋愛ガイド全体へリンク。"],
        "hub_faq": [
            ["恋愛対象は何人？", "発売時点で23人（2026-07-07）、隠し候補含む。"],
            ["なぜ単独ページがないキャラも？", "優先度順に順次追加。単独ページがない場合も全情報は恋愛ガイドにあります。"],
        ],
        "affil": {"Witch": "魔女", "Vampire": "吸血鬼", "Werewolf": "狼人", "Seer": "予言者", "Human": "人間", "Mermaid": "人魚", "Supernatural": "超常存在"},
        "appears": {
            "Spring 1 Year 1": "1年目・春1日", "Summer 24 Year 1": "1年目・夏24日",
            "With Persephone's quests": "Persephone のクエストで", "Story progression": "ストーリー進行",
            "Spring before Lovage festival": "春・Lovage 祭前", "Hidden (TBA)": "隠し（TBA）",
        },
        "personality": {
            "Fiona": "よそよそしく教団以外に無関心。Orlock と対立しつつも、深い物語を秘めています。",
            "Noel": "傲慢で自己中心的、釣りが大好き。尊大さは不安を隠す仮面かもしれません。",
            "Sabrina": "実験に夢中な真面目な魔女。賢く、家族のことで時々圧倒されます。",
            "Luna": "謎めいた存在。庭仕事と動物の世話に忙しく、魔法に詳しい。",
            "Orlock": "過去の怪物から逃げ続ける酒に溺れた吸血鬼。回復するにつれ、ロマンチックな素顔が。",
            "Evan": "Orlock の子で穏やかでおおらか。瞬間を楽しむが、父の落ちぶれに悩んでいます。",
        },
    },
    "ko": {
        "title_tpl": "문라이트 피크스 {name} 캐릭터: 선물과 연애",
        "meta_title_tpl": "{name} 공략: 선물·하트 이벤트·연애",
        "meta_desc_tpl": "『문라이트 피크스』{name} 프로필: 최애/좋아하는 선물, 성격, 등장 시기, 연애 공략.",
        "intro_tpl": "{name}은(는) 『문라이트 피크스』의 연애 가능 캐릭터 중 한 명입니다. 최애 선물, 성격, 호감도 올리는 법을 정리했습니다.",
        "sec_who": "누구인가", "sec_gifts": "선물 취향", "sec_heart": "하트 이벤트와 연애", "sec_faq": "FAQ",
        "k_affil": "종족", "k_appears": "등장", "k_person": "성격",
        "gift_headers": ["최애 선물", "좋아하는 선물", "싫어하는 선물"],
        "heart_note": ["{name}의 하트 이벤트 세부 내용은 수집 중(대기).", "하트 레벨 4에서 데이트 해금: 매일 대화하고 좋아하거나 최애인 선물을 하루 1개 주세요."],
        "faq": [
            ["{name}의 최애 선물은?", "최애: {loved}."],
            ["{name}과 언제 데이트?", "{appears}에 등장. 하트 레벨 4에서 데이트 해금."],
            ["{name}은 숨은 캐릭터인가요?", "아니요 — {name}은(는) 처음부터 공략 가능합니다."],
        ],
        "hub_title": "캐릭터 전체보기: 연애 가능 23명",
        "hub_meta_title": "캐릭터 대전: 연애 가능 23명",
        "hub_meta_desc": "『문라이트 피크스』연애 가능 23명 색인: 종족·등장 시기·성격. 각 캐릭터의 선물·연애 페이지로.",
        "hub_intro": "『문라이트 피크스』출시 기준 연애 가능 캐릭터는 23명 — 마녀, 뱀파이어, 늑대인간, 예언자, 인간, 인어 등. 카드에서 각 캐릭터 페이지로 이동하세요.",
        "hub_sec_cards": "전체 23명",
        "hub_sec_note": "프로필 안내",
        "hub_note": ["각 카드는 해당 캐릭터 페이지로 연결됩니다 — 선물, 성격, 연애 노트.", "아직 단독 페이지가 없는 캐릭터는 연애 가이드 전체로 연결됩니다."],
        "hub_faq": [
            ["연애 가능 캐릭터는 몇 명?", "출시 기준 23명(2026-07-07), 숨은 후보 포함."],
            ["단독 페이지가 없는 캐릭터도 있나요?", "우선순위 순으로 추가 중 — 없는 경우도 전체 정보는 연애 가이드에 있습니다."],
        ],
        "affil": {"Witch": "마녀", "Vampire": "뱀파이어", "Werewolf": "늑대인간", "Seer": "예언자", "Human": "인간", "Mermaid": "인어", "Supernatural": "초자연 존재"},
        "appears": {
            "Spring 1 Year 1": "1년차 봄 1일", "Summer 24 Year 1": "1년차 여름 24일",
            "With Persephone's quests": "Persephone 퀘스트", "Story progression": "스토리 진행",
            "Spring before Lovage festival": "봄, Lovage 축제 전", "Hidden (TBA)": "숨김(TBA)",
        },
        "personality": {
            "Fiona": "냉담하고 마녀단 밖에는 관심이 없지만, Orlock과의 갈등 뒤에 더 깊은 이야기를 숨기고 있습니다.",
            "Noel": "거만하고 자기중심적, 낚시를 제일 좋아합니다. 거만함은 불안을 감추는 가면일지도.",
            "Sabrina": "실험에 몰두하는 성실한 마녀. 똑똑하지만 가족 문제에 가끔 압도됩니다.",
            "Luna": "수수께끼 같은 존재. 정원과 동물 돌보기에 바쁘고, 마법에 대해 잘 압니다.",
            "Orlock": "과거의 괴물에게 쫓기며 술에 의존하는 뱀파이어. 회복되면서 낭만적인 본모습이 피어납니다.",
            "Evan": "Orlock의 아이로 느긋하고 편안한 성격. 지금 이 순간을 즐기지만 아버지의 몰락에 괴로워합니다.",
        },
    },
    "fr": {
        "title_tpl": "Moonlight Peaks — {name} : cadeaux et romance",
        "meta_title_tpl": "{name} : cadeaux, événements de cœur et romance",
        "meta_desc_tpl": "Profil de {name} dans Moonlight Peaks : cadeaux adorés/aimés, personnalité, apparition et conseils de romance.",
        "intro_tpl": "{name} est l'un des personnages romantiques de Moonlight Peaks. Voici son profil : cadeaux adorés, personnalité et comment gagner son cœur.",
        "sec_who": "Qui est {name} ?", "sec_gifts": "Cadeaux préférés", "sec_heart": "Événements de cœur & romance", "sec_faq": "FAQ",
        "k_affil": "Affiliation", "k_appears": "Apparition", "k_person": "Personnalité",
        "gift_headers": ["Cadeaux adorés", "Cadeaux aimés", "Cadeaux détestés"],
        "heart_note": ["Les détails des événements de cœur de {name} sont encore en cours de collecte (à compléter).", "Le rendez-vous se débloque au niveau de cœur 4 : parlez-lui chaque jour et offrez un cadeau aimé ou adoré."],
        "faq": [
            ["Quels cadeaux {name} adore-t-il ?", "Il/elle adore : {loved}."],
            ["Quand sortir avec {name} ?", "Apparition : {appears}. Le rendez-vous se débloque au niveau de cœur 4."],
            ["{name} est-il un personnage secret ?", "Non — {name} est disponible dès le lancement."],
        ],
        "hub_title": "Personnages : les 23 candidats romantiques",
        "hub_meta_title": "Tous les personnages romantiques de Moonlight Peaks",
        "hub_meta_desc": "Index des 23 personnages romantiques de Moonlight Peaks : affiliation, apparition, personnalité, et liens vers leurs profils cadeaux/romance.",
        "hub_intro": "Moonlight Peaks compte 23 personnages romantiques au lancement — sorcières, vampires, loups-garous, voyants, humains, sirènes et plus. Cliquez sur une carte pour le profil cadeaux/romance.",
        "hub_sec_cards": "Les 23 personnages",
        "hub_sec_note": "À propos des profils",
        "hub_note": ["Chaque carte mène au profil du personnage — cadeaux, personnalité et notes de romance.", "Les personnages sans page dédiée mènent au guide romance complet."],
        "hub_faq": [
            ["Combien de personnages romantiques ?", "23 au lancement (07/07/2026), candidats cachés inclus."],
            ["Pourquoi certains n'ont pas de page ?", "Les pages arrivent par priorité — sinon, tout est dans le guide romance."],
        ],
        "affil": {"Witch": "Sorcière", "Vampire": "Vampire", "Werewolf": "Loup-garou", "Seer": "Voyant", "Human": "Humain", "Mermaid": "Sirène", "Supernatural": "Surnaturel"},
        "appears": {
            "Spring 1 Year 1": "Printemps 1, année 1", "Summer 24 Year 1": "Été 24, année 1",
            "With Persephone's quests": "Quêtes de Persephone", "Story progression": "Progression de l'histoire",
            "Spring before Lovage festival": "Printemps, avant la fête de Lovage", "Hidden (TBA)": "Caché (TBA)",
        },
        "personality": {
            "Fiona": "Distante et indifférente hors de son coven, en conflit avec Orlock — mais une histoire bien plus profonde se cache.",
            "Noel": "Arrogant et égocentrique, préfère la pêche — son côté hautain masque ses insécurités.",
            "Sabrina": "Sorcière dévouée, passionnée d'expérimentation, intelligente, parfois dépassée par sa famille.",
            "Luna": "Personnage énigmatique, passe son temps au jardin ; sait beaucoup sur la magie.",
            "Orlock": "Vampire hanté par son passé, alcoolique ; un côté romantique et brut éclot en se rétablissant.",
            "Evan": "Enfant d'Orlock, décontracté ; apprécie l'instant présent mais souffre de la chute d'Orlock.",
        },
    },
    "de": {
        "title_tpl": "Moonlight Peaks — {name} : Geschenke und Romantik",
        "meta_title_tpl": "{name} : Geschenke, Herz-Events und Romantik",
        "meta_desc_tpl": "Profil von {name} in Moonlight Peaks : geliebte/gemochte Geschenke, Persönlichkeit, Auftritt und Romantik-Tipps.",
        "intro_tpl": "{name} ist einer der liebbaren Charaktere in Moonlight Peaks. Hier ist das Profil : geliebte Geschenke, Persönlichkeit und wie du die Herzen steigerst.",
        "sec_who": "Wer ist {name} ?", "sec_gifts": "Geschenk-Vorlieben", "sec_heart": "Herz-Events & Romantik", "sec_faq": "FAQ",
        "k_affil": "Zugehörigkeit", "k_appears": "Auftritt", "k_person": "Persönlichkeit",
        "gift_headers": ["Geliebte Geschenke", "Gemochte Geschenke", "Gehasste Geschenke"],
        "heart_note": ["Die Herz-Event-Details von {name} werden noch gesammelt (offen).", "Dating schaltet bei Herz-Level 4 frei : täglich reden und ein gemochtes oder geliebtes Geschenk geben."],
        "faq": [
            ["Welche Geschenke liebt {name}?", "Geliebt : {loved}."],
            ["Wann mit {name} daten?", "Auftritt : {appears}. Dating ab Herz-Level 4."],
            ["Ist {name} ein geheimer Charakter?", "Nein — {name} ist ab dem Start verfügbar."],
        ],
        "hub_title": "Charaktere : alle 23 Liebesoptionen",
        "hub_meta_title": "Alle liebbaren Charaktere in Moonlight Peaks",
        "hub_meta_desc": "Index der 23 liebbaren Charaktere : Zugehörigkeit, Auftritt, Persönlichkeit und Links zu ihren Geschenk-/Romantik-Profilen.",
        "hub_intro": "Moonlight Peaks hat 23 liebbare Charaktere zum Start — Hexen, Vampire, Werwölfe, Seher, Menschen, Meerjungfrauen und mehr. Klicke eine Karte für das Profil.",
        "hub_sec_cards": "Alle 23 Charaktere",
        "hub_sec_note": "Über die Profile",
        "hub_note": ["Jede Karte führt zum Profil — Geschenke, Persönlichkeit und Romantik-Notizen.", "Charaktere ohne eigene Seite führen zum kompletten Romantik-Guide."],
        "hub_faq": [
            ["Wie viele Liebesoptionen?", "23 beim Start (07.07.2026), inkl. versteckter Kandidaten."],
            ["Warum haben nicht alle eine Seite?", "Seiten kommen nach Priorität — sonst steht alles im Romantik-Guide."],
        ],
        "affil": {"Witch": "Hexe", "Vampire": "Vampir", "Werewolf": "Werwolf", "Seer": "Seher", "Human": "Mensch", "Mermaid": "Meerjungfrau", "Supernatural": "Übernatürlich"},
        "appears": {
            "Spring 1 Year 1": "Frühling 1, Jahr 1", "Summer 24 Year 1": "Sommer 24, Jahr 1",
            "With Persephone's quests": "Mit Persephones Quests", "Story progression": "Story-Fortschritt",
            "Spring before Lovage festival": "Frühling, vor dem Lovage-Fest", "Hidden (TBA)": "Versteckt (TBA)",
        },
        "personality": {
            "Fiona": "Distanziert und desinteressiert außerhalb ihres Covens, im Konflikt mit Orlock — doch dahinter steckt mehr.",
            "Noel": "Arrogant und selbstbezogen, angelt am liebsten — sein Hochmut kaschiert Unsicherheiten.",
            "Sabrina": "Hingebungsvolle Hexe, experimentierfreudig, klug, manchmal von ihrer Familie überwältigt.",
            "Luna": "Rätselhafte Figur, meist im Garten; weiß viel über Magie.",
            "Orlock": "Von seiner Vergangenheit verfolgter, alkoholkranker Vampir; beim Genesen blüht eine romantische Seite auf.",
            "Evan": "Orlocks Kind, entspannt; genießt den Moment, leidet aber unter Orlocks Absturz.",
        },
    },
}

# 英文卡片 sub（hub 默认）：只放种族，保持简短
AFFIL_SUB = {name: ROMANCE_MAP[name]["affil"] for name in ALL_NAMES}

def _slug(name):
    return "moonlight-peaks/romance/" + name.lower().replace(" ", "-")

# ---------------------------------------------------------------- Hub 页
def build_characters_hub():
    en_cards = []
    for name in ALL_NAMES:
        en_cards.append({"name": name, "sub": AFFIL_SUB[name], "slug": _slug(name) if name in CORE else ""})
    en_sections = [
        {"type": "cards", "tag": "CHAR", "heading": "All 23 characters", "body": "", "headers": [], "items": en_cards},
        N("About the profiles", [
            "Each card links to that character's profile page — gifts, personality and romance notes.",
            "Characters without a dedicated page yet link to the full romance guide instead.",
        ]),
        F([
            ["How many characters are romanceable?", "23 at launch (July 7, 2026), including secret and hidden candidates."],
            ["Why don't all characters have their own page?", "Dedicated pages are being added by priority — every character's full info is already in the romance guide."],
        ]),
    ]
    i18n = {}
    for lg, d in L.items():
        cards = [{"name": c["name"], "sub": d["affil"][AFFIL_SUB[c["name"]]], "slug": c["slug"]} for c in en_cards]
        i18n[lg] = lang_page({
            "title": d["hub_title"], "metaTitle": d["hub_meta_title"], "metaDescription": d["hub_meta_desc"], "intro": d["hub_intro"],
            "sections": {
                0: {"heading": d["hub_sec_cards"], "items": cards},
                1: {"heading": d["hub_sec_note"], "items": d["hub_note"]},
                2: {"items": d["hub_faq"]},
            },
        }, en_sections)
    return {
        "slug": "moonlight-peaks/characters",
        "title": "Moonlight Peaks Characters: All 23 Romanceable Profiles",
        "metaTitle": "All 23 Romanceable Characters in Moonlight Peaks (Index)",
        "metaDescription": "All 23 romanceable characters in Moonlight Peaks: affiliation, appearance, personality, and links to each gifts & romance profile.",
        "intro": "Moonlight Peaks has 23 romanceable characters at launch — witches, vampires, werewolves, seers, humans, mermaids and stranger beings. Pick a card to open that character's gifts & romance profile.",
        "sections": en_sections,
        "i18n": i18n,
        "priority": "P0",
        "_moon": True,
    }

# ---------------------------------------------------------------- 角色单页
def _char_page(name):
    affil = ROMANCE_MAP[name]["affil"]
    appears = ROMANCE_MAP[name]["appears"]
    loved, liked, disliked = GIFT_MAP[name]
    bio_en = ROMANCE_MAP[name]["personality"]

    en_sections = [
        S("Who they are", [
            ["Affiliation", affil],
            ["Appears", appears],
            ["Personality", bio_en],
        ]),
        T(["Loved Gifts", "Liked Gifts", "Disliked Gifts"], [[loved, liked, disliked]], heading="Gift preferences"),
        N("Heart events & romance", [
            f"{name}'s heart-event details are still being collected (待补).",
            "Dating unlocks at Heart Level 4: talk daily and give one liked or loved gift per day.",
        ]),
        F([
            [f"What gifts does {name} love?", f"They love: {loved}."],
            [f"When can I romance {name}?", f"{name} appears {appears}; dating unlocks at Heart Level 4."],
            [f"Is {name} a secret character?", f"No — {name} is dateable from the start."],
        ]),
    ]
    i18n = {}
    for lg, d in L.items():
        secs = {
            0: {"heading": d["sec_who"].replace("{name}", name), "items": [
                [d["k_affil"], d["affil"][affil]],
                [d["k_appears"], d["appears"][appears]],
                [d["k_person"], d["personality"][name]],
            ]},
            1: {"heading": d["sec_gifts"], "headers": d["gift_headers"]},
            2: {"heading": d["sec_heart"], "items": [s.replace("{name}", name) for s in d["heart_note"]]},
            3: {"heading": d["sec_faq"], "items": [[q.replace("{name}", name).replace("{loved}", loved).replace("{appears}", d["appears"][appears]), a.replace("{name}", name).replace("{loved}", loved).replace("{appears}", d["appears"][appears])] for q, a in d["faq"]]},
        }
        i18n[lg] = lang_page({
            "title": d["title_tpl"].replace("{name}", name),
            "metaTitle": d["meta_title_tpl"].replace("{name}", name),
            "metaDescription": d["meta_desc_tpl"].replace("{name}", name),
            "intro": d["intro_tpl"].replace("{name}", name),
            "sections": secs,
        }, en_sections)
    return {
        "slug": _slug(name),
        "title": f"Moonlight Peaks {name}: Gifts, Romance & Profile",
        "metaTitle": f"{name} (Moonlight Peaks): Gifts, Heart Events & How to Romance",
        "metaDescription": f"Moonlight Peaks {name} profile: loved gifts, liked gifts, personality, when they appear and how to romance them.",
        "intro": f"{name} is one of the romanceable characters in Moonlight Peaks. Here is their profile: the gifts they love, what they're like, and how to raise hearts.",
        "sections": en_sections,
        "i18n": i18n,
        "priority": "P0",
        "_moon": True,
    }

def build_character_pages():
    return [build_characters_hub()] + [_char_page(n) for n in CORE]
