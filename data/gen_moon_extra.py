# -*- coding: utf-8 -*-
"""程序化生成 moonlight_i18n_extra.py（FAQ/笔记补充翻译）。
数据用 (slug, lang, idx, {type: data}) 元组，避免手写嵌套括号。
"""
from pathlib import Path

R = []  # (slug, lang, idx, dict)
def A(slug, lang, idx, **kw):
    R.append((slug, lang, idx, kw))

# ---------------- home ----------------
A("moonlight-peaks", "zh-CN", 0, items=["23 位可攻略角色，含 喜欢/最爱/讨厌 礼物与心动事件。","全部 22 种鱼——地点、季节、天气与月相条件，以及鱼竿升级。","每种花：季节、地点、价格与赠礼对象。","工具升级（铜/铁/金）、咒语、药水与完整 59 成就列表。","分章主线流程与最新补丁说明。"])
A("moonlight-peaks", "zh-CN", 2, items=["补丁 1.1.41（2026-07-15）：加载更快、全地块（含谷仓/温室）储物+快速转移、刺绣提前解锁、23+ 项修复。","补丁 1.1.38（2026-07-10）：修复每 5–20 秒卡顿、走路卡住与 Nokturna 软锁。","2026-07-06/07 登陆 PC（Steam）、Switch、Switch 2 与 Google Play Games；7 月 26 日销量破 20 万。"])
A("moonlight-peaks", "zh-CN", 3, items=[["这是官方网站吗？","不是——这是非官方粉丝资源站。《月光小镇》及其资产归 Little Chicken / XSEED Games / Marvelous Europe 所有。"],["游戏支持哪些语言？","官方语言：英语、德语、日语、韩语、简体中文与繁体中文。本站覆盖全部 Hub 语言。"],["能攻略多少角色？","首发（2026-07-07）23 位可攻略角色，含隐藏与秘密候选。"],["《月光小镇》多少钱？","Steam 全价 US$34.99（截至撰写时）。"]])
A("moonlight-peaks", "ja", 0, items=["恋愛対象23人の贈り物（大好物・好物・嫌い）とハートイベント。","魚22種の場所・季節・天気・月相条件と釣り竿強化。","全花の季節・場所・価値・贈り先。","道具強化（銅/鉄/金）、呪文、ポーション、実績59個。","メインストーリーの章別攻略と最新パッチ。"])
A("moonlight-peaks", "ja", 2, items=["パッチ1.1.41（2026-07-15）：ロード高速化、敷地全体の収納+クイック転送、刺繍の早期解放、23以上の修正。","パッチ1.1.38（2026-07-10）：5〜20秒ごとのフリーズ、歩行スタック、Nokturnaのソフトロックを修正。","2026年7月6〜7日にPC・Switch・Switch 2・Google Play Gamesで発売、7月26日までに20万本突破。"])
A("moonlight-peaks", "ja", 3, items=[["公式サイトですか？","いいえ——非公式ファンサイトです。本ゲームと関連アセットは Little Chicken / XSEED Games / Marvelous Europe に帰属します。"],["対応言語は？","公式：英語、ドイツ語、日本語、韓国語、簡体字中国語、繁体字中国語。当サイトは全ハブ言語に対応。"],["恋愛対象は何人？","発売時点で23人（隠し候補含む）。"],["価格は？","Steam で US$34.99（執筆時点の定価）。"]])
A("moonlight-peaks", "ko", 0, items=["연애 대상 23명의 선물(최애·좋아함·싫어함)과 하트 이벤트.","물고기 22종의 장소·계절·날씨·달의 조건과 낚싯대 강화.","전체 꽃의 계절·장소·가치·선물 대상.","도구 강화(구리/철/금), 주문, 물약, 업적 59개.","메인 스토리 파트별 공략과 최신 패치."])
A("moonlight-peaks", "ko", 2, items=["패치 1.1.41(2026-07-15): 로딩 개선, 부지 전체 창고+빠른 전송, 자수 조기 해금, 23개 이상 버그 수정.","패치 1.1.38(2026-07-10): 5~20초마다 프리즈, 걷기 스택, Nokturna 소프트록 수정.","2026년 7월 6~7일 PC·Switch·Switch 2·Google Play Games 출시, 7월 26일 20만 장 돌파."])
A("moonlight-peaks", "ko", 3, items=[["공식 사이트인가요?","아니요 — 비공식 팬 리소스입니다. 게임 및 관련 자산은 Little Chicken / XSEED Games / Marvelous Europe에 귀속됩니다."],["지원 언어는?","공식: 영어, 독일어, 일본어, 한국어, 간체·번체 중국어. 저희는 모든 허브 언어를 제공합니다."],["연애 대상은 몇 명?","출시 기준 23명(숨은 후보 포함)."],["가격은?","Steam 정가 US$34.99(작성 시점)."]])
A("moonlight-peaks", "fr", 0, items=["Les 23 personnages romantiques avec cadeaux adorés/aimés/détestés et événements de cœur.","Les 22 poissons — lieux, saisons, météo et phases de lune, plus les cannes.","Chaque fleur : saison, lieu, valeur et destinataire.","Améliorations d'outils (cuivre/fer/or), sorts, potions et les 59 succès.","La soluce de l'histoire et les dernières notes de patch."])
A("moonlight-peaks", "fr", 2, items=["Patch 1.1.41 (15/07/2026) : chargement plus rapide, stockage sur tout le terrain, broderie plus tôt, 23+ correctifs.","Patch 1.1.38 (10/07/2026) : gels de 5–20 s, animation de marche bloquée et soft lock Nokturna corrigés.","Sorti les 6–7 juillet 2026 sur PC, Switch, Switch 2 et Google Play Games ; plus de 200 000 ventes au 26 juillet."])
A("moonlight-peaks", "fr", 3, items=[["Ce site est-il officiel ?","Non — ressource de fans non officielle. Le jeu et ses ressources appartiennent à Little Chicken / XSEED Games / Marvelous Europe."],["Langues ?","Officielles : anglais, allemand, japonais, coréen, chinois simplifié et traditionnel."],["Combien de romances ?","23 au lancement, secrets inclus."],["Prix ?","34,99 $ US sur Steam (prix plein)."]])
A("moonlight-peaks", "de", 0, items=["Alle 23 Liebesoptionen mit Geschenken (geliebt/gemocht/gehasst) und Herz-Events.","Alle 22 Fische — Orte, Jahreszeiten, Wetter und Mondphasen, plus Ruten.","Jede Blume: Jahreszeit, Ort, Wert und für wen.","Werkzeug-Upgrades (Kupfer/Eisen/Gold), Zauber, Tränke und alle 59 Erfolge.","Die Hauptstory-Lösung und die neuesten Patch-Notizen."])
A("moonlight-peaks", "de", 2, items=["Patch 1.1.41 (15.07.2026): schnelleres Laden, Lager auf dem ganzen Grundstück, Stickerei früher, 23+ Fixes.","Patch 1.1.38 (10.07.2026): Freezes alle 5–20 s, Lauf-Animation und Nokturna-Softlock behoben.","Erschienen am 6.–7. Juli 2026 für PC, Switch, Switch 2 und Google Play Games; über 200.000 Verkäufe bis 26. Juli."])
A("moonlight-peaks", "de", 3, items=[["Offizielle Seite?","Nein — inoffizielle Fan-Ressource. Spiel und Assets gehören Little Chicken / XSEED Games / Marvelous Europe."],["Sprachen?","Offiziell: Englisch, Deutsch, Japanisch, Koreanisch, vereinfachtes und traditionelles Chinesisch."],["Wie viele Liebesoptionen?","23 zum Start, inkl. Geheimkandidaten."],["Preis?","34,99 $ US auf Steam (Vollpreis)."]])

# ---------------- how-to-play ----------------
A("moonlight-peaks/how-to-play", "zh-CN", 3, items=["鱼钩抛得太近——鱼会被吓跑。保持距离抛竿，再轻轻收线。","在解锁谷仓（4000 金币）与第一批工具升级前把钱花光。","忽略任务板：每天都有简单的赚钱与免费物品任务。","错过发光的螺旋地砖——里面藏着配方与实用物品。"])
A("moonlight-peaks/how-to-play", "zh-CN", 4, items=[["什么时候解锁钓鱼？","第二天晚上，Noel 会在海岸附近挑战你（“Outfish The Fisherman”）。完成后保留鱼竿并得 250 金币。"],["什么时候解锁魔法？","完成“魔法作物”任务（春季 Luna 来信）。Luna 教你 Aquaflux I 并修好固定魔杖。"],["怎么快速赚钱？","加工原料（葡萄→酒、牛奶→奶酪）、每天看任务板、卖高价鱼如 Armour（280 金币）。"],["能按自己的节奏玩吗？","可以——没有严格时间限制；剧情通过睡觉与逛小镇推进。"]])
A("moonlight-peaks/how-to-play", "ja", 3, items=["釣り糸を近くに投げすぎると魚が逃げる。距離を取って投げ、軽く巻き取る。","納屋（4,000コイン）と最初の道具強化を解放する前にお金を使い切る。","依頼板を無視する——毎日簡単な報酬と無料アイテムがある。","光る渦巻きタイルをスキップ——レシピと便利アイテムが隠れている。"])
A("moonlight-peaks/how-to-play", "ja", 4, items=[["釣りはいつ解放？","2日目の夜、海岸で Noel のチャレンジ（「Outfish The Fisherman」）。クリアで竿+250コイン。"],["魔法はいつ？","「Magic of Crops」クエスト（春の Luna の手紙）。Aquaflux I を習得し Fixed Wand が修理される。"],["金策は？","素材を加工（葡萄→ワイン、牛乳→チーズ）、依頼板を毎日、Armour（280）など高値の魚を売る。"],["自分のペースで遊べる？","はい——厳密な時間制限はなく、ストーリーは寝る・町を巡ることで進みます。"]])
A("moonlight-peaks/how-to-play", "ko", 3, items=["낚싯바늘을 너무 가까이 던지면 물고기가 도망갑니다. 거리를 두고 던진 뒤 가볍게 감으세요.","헛간(4,000코인)과 첫 도구 강화를 해금하기 전에 돈을 다 써버립니다.","게시판 의뢰를 무시 — 매일 간단한 보상과 무료 아이템이 있습니다.","빛나는 나선 타일을 건너뜀 — 레시피와 유용한 아이템이 숨어 있습니다."])
A("moonlight-peaks/how-to-play", "ko", 4, items=[["낚시는 언제 해금?","둘째 날 밤, 해안에서 Noel의 도전('Outfish The Fisherman'). 클리어 시 낚싯대+250코인."],["마법은 언제?","'Magic of Crops' 퀘스트(봄 Luna의 편지). Aquaflux I 습득, Fixed Wand 수리."],["돈 빨리 버는 법?","원자재 가공(포도→와인, 우유→치즈), 매일 게시판, Armour(280) 등 고가 물고기 판매."],["내 페이스로 할 수 있나요?","네 — 엄격한 시간 제한은 없고, 스토리는 잠과 마을 탐방으로 진행됩니다."]])
A("moonlight-peaks/how-to-play", "fr", 3, items=["Lancer l'hameçon trop près — les poissons fuient. Lancez à distance puis ramenez doucement.","Dépenser tout l'argent avant la grange (4 000) et les premiers outils.","Ignorer le tableau des contrats : tâches simples et objets gratuits chaque jour.","Rater les tuiles spirales brillantes — recettes et objets utiles."])
A("moonlight-peaks/how-to-play", "fr", 4, items=[["Quand débloquer la pêche ?","La 2e nuit, Noel vous défie près de la côte. Réussissez pour garder la canne (+250 pièces)."],["Quand débloquer la magie ?","Quête 'Magic of Crops' (lettre de Luna au printemps). Luna vous apprend Aquaflux I."],["Comment gagner de l'argent vite ?","Transformez (raisins→vin, lait→fromage), le tableau des contrats, vendez Armour (280)."],["Jouer à son rythme ?","Oui — pas de limite stricte ; l'histoire avance en dormant et en visitant la ville."]])
A("moonlight-peaks/how-to-play", "de", 3, items=["Den Haken zu nah werfen — Fische erschrecken. Wirf auf Distanz und kurble sanft.","Geld ausgeben, bevor Scheune (4.000) und erste Upgrades frei sind.","Das Auftragsbrett ignorieren — einfache Aufgaben, kostenlose Items.","Die glühenden Spiral-Fliesen überspringen — Rezepte und nützliche Items."])
A("moonlight-peaks/how-to-play", "de", 4, items=[["Wann Angeln freischalten?","In Nacht 2 fordert Noel dich an der Küste heraus. Erfolg = Rute behalten (+250 Münzen)."],["Wann Magie?","Quest 'Magic of Crops' (Brief von Luna im Frühling). Luna lehrt dich Aquaflux I."],["Schnell Geld?","Verarbeite (Trauben→Wein, Milch→Käse), Auftragsbrett, verkaufe Armour (280)."],["Eigenes Tempo?","Ja — keine strikten Limits; die Story schreitet durch Schlafen und Erkunden voran."]])

# ---------------- gifts ----------------
A("moonlight-peaks/gifts", "zh-CN", 2, items=["花是全游戏最通用的礼物——许多居民喜欢或最爱花。","稀有花（月光花、黑郁金香、蓝色月光花）对特定角色价值最高。","除送礼外，每天与所有人交谈并完成他们的请求，好感涨得最快。"])
A("moonlight-peaks/gifts", "zh-CN", 3, items=[["礼物系统怎么运作？","每个角色有四档：最爱（加成最大）、喜欢（可观）、一般（少量）、讨厌（几乎不计或负面）。每个角色每天只能送一次。"],["最通用的礼物是什么？","花。Luna 喜欢任何花，多数居民至少喜欢花；稀有彩色花能覆盖更多角色。"],["送讨厌的礼物会掉好感吗？","几乎不计且可能触发负面反应——避开“讨厌”列里的物品。"]])
A("moonlight-peaks/gifts", "ja", 2, items=["花は最も汎用性が高い——多くの住民が好む・大好き。","希少花（Moonlight Flowers、Black Tulips、Blue Moonlight Flower）は特定キャラに最高。","贈り物に加え、毎日全員と話しリクエストをこなすのが最短。"])
A("moonlight-peaks/gifts", "ja", 3, items=[["贈り物の仕組みは？","キャラごとに4段階：大好物（最大）、好物（しっかり）、普通（少し）、嫌い（ほぼ無し・ネガティブ）。1日1個まで。"],["万能な贈り物は？","花。Luna はどんな花も大好き、多くの住民は少なくとも好む。"],["嫌いな物は悪影響？","ほぼ増えずネガティブ反応も——「嫌いな物」列は避けましょう。"]])
A("moonlight-peaks/gifts", "ko", 2, items=["꽃은 가장 활용도 높은 선물 — 많은 주민이 좋아하거나 최애입니다.","희귀 꽃(Moonlight Flowers, Black Tulips, Blue Moonlight Flower)은 특정 캐릭터에게 최고.","선물 외에도 매일 모두와 대화하고 의뢰를 완료하면 호감도가 가장 빠르게 오릅니다."])
A("moonlight-peaks/gifts", "ko", 3, items=[["선물 시스템은?","캐릭터마다 4단계: 최애(최대), 좋아함(확실), 보통(약간), 싫어함(거의 없음·부정). 캐릭터당 하루 1개."],["가장 무난한 선물은?","꽃. Luna는 어떤 꽃이든 최애, 대부분 주민은 최소 좋아합니다."],["싫어하는 선물은?","거의 안 오르고 부정 반응도 — '싫어함' 열은 피하세요."]])
A("moonlight-peaks/gifts", "fr", 2, items=["Les fleurs sont le cadeau le plus polyvalent — beaucoup adorent ou aiment.","Les fleurs rares (Moonlight, tulipes noires, moonlight bleue) valent pour des cibles précises.","En plus des cadeaux, parlez à tous chaque jour et finissez leurs demandes."])
A("moonlight-peaks/gifts", "fr", 3, items=[["Comment fonctionne le système ?","Quatre niveaux : adoré (max), aimé (bon), neutre (petit), détesté (quasi nul/négatif). Un cadeau par jour."],["Cadeau universel ?","Les fleurs. Luna adore toute fleur ; la plupart des habitants les aiment."],["Cadeaux détestés ?","Presque rien et réaction négative possible — évitez la colonne détestés."]])
A("moonlight-peaks/gifts", "de", 2, items=["Blumen sind die vielseitigsten Geschenke — viele lieben oder mögen sie.","Seltene Blumen (Moonlight, schwarze Tulpen, blaue Moonlight) sind für bestimmte Charaktere ideal.","Neben Geschenken: täglich mit allen reden und ihre Bitten erfüllen."])
A("moonlight-peaks/gifts", "de", 3, items=[["Wie funktioniert das System?","Vier Stufen: geliebt (max), gemocht (gut), neutral (wenig), gehasst (fast nichts/negativ). Ein Geschenk pro Tag."],["Universelles Geschenk?","Blumen. Luna liebt jede Blume; die meisten Bewohner mögen sie."],["Gehasste Geschenke?","Fast nichts plus mögliche negative Reaktion — meide die Spalte."]])

# ---------------- romance ----------------
A("moonlight-peaks/romance", "zh-CN", 2, items=["在 Nintendo Switch 上按“+”键打开主菜单。","进入 设置 → Gameplay 菜单底部的 立绘风格（Portrait Style）。","在风格 1（卡通+写实光影）与风格 2（动漫风、可爱圆润）之间选择。"])
A("moonlight-peaks/romance", "zh-CN", 3, items=[["可以同时和多人约会吗？","可以——可以同时约会多位居民，但只能与其中一人结婚。"],["什么时候可以开始约会？","与该角色心数达到 4 级后解锁。"],["能生孩子吗？","不能——没有子嗣机制，官方暂无计划。"],["隐藏恋爱候选是谁？","Kim、Tae、Rei（人鱼）需满足隐藏条件后出现，细节各来源标注 TBA。"]])
A("moonlight-peaks/romance", "ja", 2, items=["Nintendo Switch で「+」ボタンを押してメインメニュー。","設定 → ゲームプレイメニュー下の「Portrait Style」。","スタイル1（写実的な陰影のカートゥーン）かスタイル2（アニメ風で可愛い）を選択。"])
A("moonlight-peaks/romance", "ja", 3, items=[["複数とデートできる？","はい——同時に複数とデート可能ですが、結婚は1人だけ。"],["デートはいつから？","そのキャラのハートレベル4で解放。"],["子供は？","いいえ——子供システムはなく、予定もありません。"],["隠し候補は？","Kim、Tae、Rei（人魚）。条件を満たすと出現。詳細は各ソースでTBA。"]])
A("moonlight-peaks/romance", "ko", 2, items=["Nintendo Switch에서 '+' 버튼으로 메인 메뉴.","설정 → 게임플레이 메뉴 하단의 'Portrait Style'.","스타일 1(카툰+사실적 음영) 또는 스타일 2(애니풍, 귀엽고 통통)."])
A("moonlight-peaks/romance", "ko", 3, items=[["여러 명과 동시에 데이트?","네 — 가능하지만 결혼은 한 명만."],["데이트 시작 시점?","그 캐릭터와 하트 레벨 4에서 해금."],["자녀는?","없음 — 자녀 시스템 없고 계획도 없습니다."],["숨은 후보는?","Kim, Tae, Rei(인어). 조건 충족 시 등장, 세부는 TBA."]])
A("moonlight-peaks/romance", "fr", 2, items=["Ouvrez le menu principal avec '+' sur Switch.","Réglages → Portrait Style en bas du menu Gameplay.","Choisissez style 1 (cartoon, ombrage réaliste) ou 2 (anime, mignon)."])
A("moonlight-peaks/romance", "fr", 3, items=[["Plusieurs romances ?","Oui — vous pouvez sortir avec plusieurs, mais épouser une seule personne."],["Quand dater ?","Au niveau de cœur 4 avec ce personnage."],["Enfants ?","Non — aucun mécanisme et aucun prévu."],["Candidats secrets ?","Kim, Tae et Rei (sirènes) après conditions cachées ; détails TBA."]])
A("moonlight-peaks/romance", "de", 2, items=["Öffne das Hauptmenü mit '+' auf der Switch.","Einstellungen → Portrait Style unten im Gameplay-Menü.","Wähle Stil 1 (Cartoon, realistisch) oder 2 (Anime, niedlich)."])
A("moonlight-peaks/romance", "de", 3, items=[["Mehrere gleichzeitig?","Ja — mit mehreren daten, aber nur eine Person heiraten."],["Wann daten?","Ab Herz-Stufe 4 mit dem Charakter."],["Kinder?","Nein — keine Mechanik, keine geplant."],["Geheime Kandidaten?","Kim, Tae und Rei (Meerjungfrauen) nach versteckten Bedingungen; Details TBA."]])

# ---------------- fishing ----------------
A("moonlight-peaks/fishing", "zh-CN", 3, items=["每个季节和天气都去钓——部分鱼有时令（Goldy 春夏；Mouthout 仅雨天）。","满月夜回 Luna Bay 钓 Moonflutter。","尽早升 Premium 竿，钓大鱼（Furybud、Goliath、Armour）。","每种鱼都捐一条给博物馆水族馆收集。","Howling Hammer 营业时间：周一至周五 18:00–00:00。"])
A("moonlight-peaks/fishing", "zh-CN", 4, items=[["什么时候拿到鱼竿？","第二天晚上完成 Noel 的海边钓鱼挑战即可保留鱼竿（+250 金币）。"],["哪条鱼需要满月？","Moonflutter 只在满月时的 Luna Bay 出现。"],["哪些鱼需要 Premium 竿？","Furybud、Goliath、Armour 是大鱼，需要 Premium 钓鱼竿。"],["“Missing”是什么？","一种超级稀有鱼，可在任意钓点出现——钓到它解锁“Missing? No!”成就。"]])
A("moonlight-peaks/fishing", "ja", 3, items=["季節・天気を変えて釣る——Goldy は春夏のみ、Mouthout は雨のみ。","満月の夜に Luna Bay で Moonflutter。","早めに Premium 竿へ——大型魚（Furybud、Goliath、Armour）。","全種を博物館の水族館コレクションへ寄贈。","Howling Hammer は月〜金 18:00〜24:00。"])
A("moonlight-peaks/fishing", "ja", 4, items=[["竿はいつ？","2日目の夜、Noel の釣りチャレンジをクリアで竿+250コイン。"],["満月の魚は？","Moonflutter。Luna Bay で満月の夜のみ。"],["Premium 竿が必要な魚は？","Furybud、Goliath、Armour（大型魚）。"],["「Missing」とは？","超レアな魚で任意の釣り場に出現。釣ると「Missing? No!」実績。"]])
A("moonlight-peaks/fishing", "ko", 3, items=["모든 계절·날씨에서 낚시 — Goldy는 봄·여름, Mouthout은 비 오는 날만.","보름달 밤에 Luna Bay에서 Moonflutter.","일찍 Premium 낚싯대로 대형어(Furybud, Goliath, Armour).","모든 종을 박물관 수족관에 기증.","Howling Hammer는 월~금 18:00~24:00."])
A("moonlight-peaks/fishing", "ko", 4, items=[["낚싯대는 언제?","둘째 날 밤 Noel 도전 클리어 시 낚싯대+250코인."],["보름달 물고기는?","Moonflutter — Luna Bay에서 보름달 밤만."],["Premium 낚싯대 필요?","Furybud, Goliath, Armour(대형어)."],["'Missing'은?","아무 낚시터에나 나타나는 초희귀 어종. 잡으면 'Missing? No!' 업적."]])
A("moonlight-peaks/fishing", "fr", 3, items=["Pêchez chaque saison et météo — Goldy (printemps/été), Mouthout (pluie).","Revenez les nuits de pleine lune à Luna Bay pour Moonflutter.","Passez tôt à la canne Premium pour les gros poissons.","Donnez une de chaque espèce à l'aquarium du musée.","Le Howling Hammer : lundi–vendredi 18h–00h."])
A("moonlight-peaks/fishing", "fr", 4, items=[["Quand avoir la canne ?","2e nuit, réussissez le défi de Noel pour garder la canne (+250)."],["Poisson de pleine lune ?","Moonflutter, uniquement à Luna Bay en pleine lune."],["Canne Premium ?","Furybud, Goliath et Armour (gros poissons)."],["C'est quoi 'Missing' ?","Poisson super rare à tout spot — succès 'Missing? No!'."]])
A("moonlight-peaks/fishing", "de", 3, items=["In jeder Jahreszeit und jedem Wetter angeln — Goldy (Frühling/Sommer), Mouthout (Regen).","Bei Vollmond nach Luna Bay für Moonflutter.","Früh auf die Premium-Rute für die großen Fische.","Je eine Art ins Museum-Aquarium spenden.","Howling Hammer: Mo–Fr 18–24 Uhr."])
A("moonlight-peaks/fishing", "de", 4, items=[["Wann bekomme ich die Rute?","In Nacht 2: Noels Herausforderung bestehen, Rute behalten (+250)."],["Vollmond-Fisch?","Moonflutter, nur in Luna Bay bei Vollmond."],["Premium-Rute nötig?","Furybud, Goliath und Armour (große Fische)."],["Was ist 'Missing'?","Super-seltener Fisch an jedem Spot — Erfolg 'Missing? No!'."]])

# ---------------- flowers ----------------
A("moonlight-peaks/flowers", "zh-CN", 1, items=["Luna 喜欢任何花——安全的每日礼物。","月光花（Khazan Temple）对 Aras、Dragan 与 Moon Goddess 价值最高。","黑花（Alina）与彩色郁金香覆盖角色多——从 Misty Shores 囤货。","白花稀有——留给 Fiona 与 Brook。","在蜂箱周围种花可提升蜂蜜产量与收成（社区技巧）。"])
A("moonlight-peaks/flowers", "zh-CN", 2, items=[["哪种花所有人都喜欢？","没有全角色通吃的花，但 Luna 喜欢任何花、多数居民喜欢大多数花——花是最安全的礼物类别。"],["月光花在哪里？","Khazan Temple：蓝色春季、紫色夏季。"],["花好卖吗？","多数卖 6–15 金币；稀有彩色玫瑰与月光花价值最高。"]])
A("moonlight-peaks/flowers", "ja", 1, items=["Luna はどんな花も大好き——毎日でも安全。","Moonlight Flowers（Khazan Temple）は Aras、Dragan、Moon Goddess に最高。","黒い花（Alina）と色付きチューリップは多くのキャラをカバー。","白い花は希少——Fiona と Brook に取っておく。","蜂の巣の周りに花を植えるとハチミツ生産が増える（コミュニティ情報）。"])
A("moonlight-peaks/flowers", "ja", 2, items=[["誰にでも効く花は？","全員に効く花はないが、Luna は何でも大好き、多くの住民は大抵の花を好む。"],["Moonlight Flowers はどこ？","Khazan Temple：青=春、紫=夏。"],["花は売れる？","多くは6〜15コイン。希少な色付きバラと月光花が高値。"]])
A("moonlight-peaks/flowers", "ko", 1, items=["Luna는 어떤 꽃이든 최애 — 매일 안전한 선물.","Moonlight Flowers(Khazan Temple)는 Aras, Dragan, Moon Goddess에게 최고.","검은 꽃(Alina)과 색깔 튤립은 많은 캐릭터를 커버.","흰 꽃은 희귀 — Fiona와 Brook에게 아껴두기.","벌통 주변에 꽃을 심으면 꿀 생산이 늘어납니다(커뮤니티 팁)."])
A("moonlight-peaks/flowers", "ko", 2, items=[["모두에게 좋은 꽃?","전원 통하는 꽃은 없지만, Luna는 어떤 꽃이든 최애이고 대부분 주민이 꽃을 좋아합니다."],["Moonlight Flowers 위치?","Khazan Temple: 파랑=봄, 보라=여름."],["꽃이 잘 팔리나요?","대부분 6~15코인. 희귀한 색깔 장미와 문라이트 꽃이 가장 비쌉니다."]])
A("moonlight-peaks/flowers", "fr", 1, items=["Luna adore toute fleur — cadeau sûr.","Les Moonlight Flowers (Khazan Temple) valent pour Aras, Dragan et Moon Goddess.","Fleurs noires (Alina) et tulipes colorées couvrent beaucoup de monde.","Les fleurs blanches sont rares — gardez-les pour Fiona et Brook.","Plantez des fleurs autour des ruches pour plus de miel (conseil communauté)."])
A("moonlight-peaks/flowers", "fr", 2, items=[["Fleur universelle ?","Pas d'universelle, mais Luna adore toute fleur et la plupart des habitants aiment les fleurs."],["Où trouver les Moonlight Flowers ?","Khazan Temple : bleues au printemps, violettes en été."],["Les fleurs se vendent bien ?","6–15 pièces pour la plupart ; roses rares et moonlight plus chères."]])
A("moonlight-peaks/flowers", "de", 1, items=["Luna liebt jede Blume — sicheres Geschenk.","Moonlight Flowers (Khazan Temple) sind ideal für Aras, Dragan und Moon Goddess.","Schwarze Blumen (Alina) und bunte Tulpen decken viele ab.","Weiße Blumen sind selten — für Fiona und Brook aufheben.","Blumen um Bienenstöcke pflanzen erhöht Honig (Community-Tipp)."])
A("moonlight-peaks/flowers", "de", 2, items=[["Universelle Blume?","Keine für alle, aber Luna liebt jede und die meisten mögen Blumen."],["Wo Moonlight Flowers?","Khazan Temple: blau im Frühling, lila im Sommer."],["Verkaufen sich Blumen gut?","Meist 6–15 Münzen; seltene Rosen und Moonlight mehr."]])

# ---------------- tools ----------------
A("moonlight-peaks/tools", "zh-CN", 3, items=[["工具升级多少钱？","所有铜工具 1000 金币、铁工具 4000、金工具 16000——每件再加 3 块上一级金属锭。"],["工具店在哪？","月光小镇中央的 Ridge 的 Howling Hammer，周一至周五 18:00–24:00 营业。"],["什么时候能买铜工具？","完成“A Bridge Too Far”并抵达 Misty Shores 的洞穴之后。"],["镰刀有金级吗？","没有——镰刀最高到铁级（据 Screen Hype）。"]])
A("moonlight-peaks/tools", "ja", 3, items=[["強化費用は？","銅1,000、鉄4,000、金16,000コイン＋前段階の金属バー3本。"],["道具屋はどこ？","中央の Ridge の Howling Hammer。月〜金 18:00〜24:00。"],["銅道具はいつ買える？","「A Bridge Too Far」完了後、Misty Shores の洞窟まで進む。"],["鎌に金はある？","いいえ——鎌は鉄まで（Screen Hype による）。"]])
A("moonlight-peaks/tools", "ko", 3, items=[["강화 비용은?","구리 1,000, 철 4,000, 금 16,000코인 + 이전 단계 금속 주괴 3개."],["도구 상점은?","중앙의 Ridge의 Howling Hammer. 월~금 18:00~24:00."],["구리 도구는 언제?","'A Bridge Too Far' 완료 후 Misty Shores 동굴까지."],["낫에 금 등급?","없음 — 낫은 철까지(Screen Hype 기준)."]])
A("moonlight-peaks/tools", "fr", 3, items=[["Coût des améliorations ?","Cuivre 1 000, fer 4 000, or 16 000 — plus 3 barres du métal précédent."],["Où est la boutique ?","Le Howling Hammer de Ridge, 18h–minuit, lundi–vendredi."],["Quand les outils cuivre ?","Après 'A Bridge Too Far' et la grotte de Misty Shores."],["La faux a-t-elle un palier or ?","Non — elle s'arrête au fer (Screen Hype)."]])
A("moonlight-peaks/tools", "de", 3, items=[["Upgrade-Kosten?","Kupfer 1.000, Eisen 4.000, Gold 16.000 — plus 3 Barren des vorherigen Metalls."],["Wo ist der Laden?","Ridges Howling Hammer, 18–24 Uhr, Mo–Fr."],["Wann Kupfer-Werkzeuge?","Nach 'A Bridge Too Far' und der Höhle in Misty Shores."],["Sense mit Gold-Stufe?","Nein — die Sense endet bei Eisen (Screen Hype)."]])

# ---------------- spells ----------------
A("moonlight-peaks/spells", "zh-CN", 2, items=["Aquaflux I（免费）与 Refilliarmus（0 魔力）——浇水循环。","Ethereal Hands I（收获 32 格）省去大量点击。","Ethereal Pickaxes I 与 Axes I——更快采矿与砍树。","Maturio I——应急瞬间催熟。"])
A("moonlight-peaks/spells", "zh-CN", 3, items=[["怎么解锁魔法？","完成“魔法作物”任务（春季 Luna 来信），学会 Aquaflux I 并拿到固定魔杖。"],["在哪里买咒语？","月光小镇的 Webb of Wonders（Sabrina 的魔法店）。"],["怎么施法？","打开咒语书 Grimoire → Spells 标签查看魔杖手势（光球会显示挥动顺序）。"],["有多少咒语？","第一年春的列表有 12 个咒语；后期咒语仍在核实（标待补）。"]])
A("moonlight-peaks/spells", "ja", 2, items=["Aquaflux I（無料）と Refilliarmus（マナ0）——水やりループ。","Ethereal Hands I（32マス収穫）でクリックを大幅削減。","Ethereal Pickaxes I / Axes I——採掘・伐採が速く。","Maturio I——急ぎの時に瞬間成長。"])
A("moonlight-peaks/spells", "ja", 3, items=[["魔法の解放は？","「Magic of Crops」クエスト（春の Luna の手紙）で Aquaflux I と Fixed Wand を取得。"],["呪文はどこで買う？","Webb of Wonders（Sabrina の魔法店）。"],["呪文の使い方は？","Grimoire → Spells タブで杖のジェスチャーを確認（光の玉が順序を示す）。"],["呪文はいくつ？","春1年目は12個。後半の呪文は検証中（待補）。"]])
A("moonlight-peaks/spells", "ko", 2, items=["Aquaflux I(무료)와 Refilliarmus(마나0) — 물 주기 루프.","Ethereal Hands I(32칸 수확)로 클릭 대폭 절약.","Ethereal Pickaxes I / Axes I — 채광·벌목 속도.","Maturio I — 급할 때 즉시 성장."])
A("moonlight-peaks/spells", "ko", 3, items=[["마법 해금은?","'Magic of Crops' 퀘스트(봄 Luna의 편지)로 Aquaflux I과 Fixed Wand 획득."],["주문 구매처?","Webb of Wonders(Sabrina의 마법 상점)."],["주문 사용법?","Grimoire → Spells 탭에서 지팡이 제스처 확인(빛의 구체가 순서 표시)."],["주문은 몇 개?","봄 1년차 12개. 후반 주문은 검증 중(대기)."]])
A("moonlight-peaks/spells", "fr", 2, items=["Aquaflux I (gratuit) et Refilliarmus (0 mana) — la boucle d'eau.","Ethereal Hands I (32 cultures) économise des heures de clics.","Ethereal Pickaxes I et Axes I — minage et bois plus rapides.","Maturio I — croissance instantanée en cas de besoin."])
A("moonlight-peaks/spells", "fr", 3, items=[["Débloquer la magie ?","Quête 'Magic of Crops' (lettre de Luna) pour Aquaflux I et la baguette."],["Où acheter les sorts ?","Webb of Wonders (boutique de Sabrina)."],["Comment lancer ?","Grimoire → Spells pour les gestes (la boule de lumière montre l'ordre)."],["Combien de sorts ?","12 au printemps, an 1 ; la suite est en cours de vérification."]])
A("moonlight-peaks/spells", "de", 2, items=["Aquaflux I (kostenlos) und Refilliarmus (0 Mana) — der Wasser-Loop.","Ethereal Hands I (32 Pflanzen) spart Stunden an Klicks.","Ethereal Pickaxes I und Axes I — schneller Erz und Holz.","Maturio I — sofortiges Wachstum in der Not."])
A("moonlight-peaks/spells", "de", 3, items=[["Magie freischalten?","Quest 'Magic of Crops' (Brief von Luna) für Aquaflux I und den Stab."],["Zauber kaufen?","Webb of Wonders (Sabrinas Laden)."],["Wie wirken?","Grimoire → Spells für Gesten (die Lichtkugel zeigt die Reihenfolge)."],["Wie viele Zauber?","12 im Frühling, Jahr 1; der Rest wird geprüft."]])


# ---------------- achievements ----------------
A("moonlight-peaks/achievements", "zh-CN", 1, items=["纹章成就：完成各家族剧情线（Ambrosia、Dracula、Henderson、Hosu、Khazan、Logan、Webb），把纹章放入纹章园。","收集：捐出所有鱼、花与文物——“One Collection to Rule Them All”需要完整博物馆。","变身：人鱼、蝙蝠与 Hellkitten 形态随主线解锁；“Tree Hugger”来自特定恋爱线。","礼物成就：规划一晚送出 25 件最爱礼物（“Serial Gifter”）与累计 299 件（“A Generous Donor”）。","易错项：满月与狼人交谈（Awooooo!）、给 Pakkeleg 带木炭（Bad Santa!）、钓 Missing（Missing? No!）。"])
A("moonlight-peaks/achievements", "zh-CN", 2, items=[["有多少个成就？","首发 59 个（2026-07-06/07）。"],["最难的是哪个？","完成党普遍认为“One Collection to Rule Them All”（完整博物馆）、“Fishing Pro”（22 鱼）与“A Farming Monopoly”（1,000,000 金币）最难。"],["会错过成就吗？","会——部分绑定事件（满月、Pakkeleg）或后期剧情窗口，需要提前规划。"]])
A("moonlight-peaks/achievements", "ja", 1, items=["家紋：各家族のストーリー（Ambrosia、Dracula、Henderson、Hosu、Khazan、Logan、Webb）を終えて紋章園に置く。","収集：魚・花・遺物を全部寄贈。「One Collection to Rule Them All」は博物館コンプ必須。","変身：人魚・蝙蝠・Hellkitten はストーリーで解放。「Tree Hugger」は特定恋愛ルート。","贈り物：一晩で大好物25個（Serial Gifter）と累計299個（A Generous Donor）。","注意：満月に狼人と話す（Awooooo!）、Pakkeleg に炭を持参（Bad Santa!）、Missing を釣る（Missing? No!）。"])
A("moonlight-peaks/achievements", "ja", 2, items=[["実績はいくつ？","発売時点で59個（2026-07-06/07）。"],["難しいのは？","「One Collection to Rule Them All」（博物館コンプ）、「Fishing Pro」（全22種）、「A Farming Monopoly」（1,000,000コイン）。"],["取り逃しはある？","はい——満月や Pakkeleg などイベント連動や終盤の窓が。計画を。"]])
A("moonlight-peaks/achievements", "ko", 1, items=["문장: 각 가문 스토리(Ambrosia, Dracula, Henderson, Hosu, Khazan, Logan, Webb) 완료 후 문장 정원에 배치.","수집: 물고기·꽃·유물 전부 기증. 'One Collection to Rule Them All'은 박물관 완성 필요.","변신: 인어·박쥐·Hellkitten은 스토리로 해금. 'Tree Hugger'는 특정 연애 루트.","선물: 한밤에 최애 선물 25개(Serial Gifter), 누적 299개(A Generous Donor).","주의: 보름달에 늑대인간과 대화(Awooooo!), Pakkeleg에 숯(Bad Santa!), Missing 낚기(Missing? No!)."])
A("moonlight-peaks/achievements", "ko", 2, items=[["업적은 몇 개?", "출시 기준 59개(2026-07-06/07)."],["가장 어려운 건?", "'One Collection to Rule Them All'(박물관 완성), 'Fishing Pro'(물고기 22종), 'A Farming Monopoly'(1,000,000코인)."],["놓칠 수 있나요?", "네 — 보름달, Pakkeleg 등 이벤트 또는 후반 스토리 창. 미리 계획하세요."]])
A("moonlight-peaks/achievements", "fr", 1, items=["Emblèmes : finissez chaque famille (Ambrosia, Dracula, Henderson, Hosu, Khazan, Logan, Webb) pour le Jardin des emblèmes.","Collections : donnez tous les poissons, fleurs et artefacts — 'One Collection to Rule Them All' exige le musée complet.","Transformations : sirène, chauve-souris et Hellkitten via l'histoire ; 'Tree Hugger' vient d'une romance précise.","Cadeaux : 25 adorés en une nuit (Serial Gifter) et 299 au total (A Generous Donor).","Missables : loup-garou à la pleine lune (Awooooo!), charbon à Pakkeleg (Bad Santa!), attraper Missing (Missing? No!)."])
A("moonlight-peaks/achievements", "fr", 2, items=[["Combien de succès ?","59 au lancement (6–7 juillet 2026)."],["Le plus dur ?","'One Collection to Rule Them All' (musée complet), 'Fishing Pro' (22 poissons) et 'A Farming Monopoly' (1 000 000)."],["Des succès manquables ?","Oui — liés à des événements (pleine lune, Pakkeleg) ou à des fenêtres tardives."]])
A("moonlight-peaks/achievements", "de", 1, items=["Wappen: Schließe jede Familie (Ambrosia, Dracula, Henderson, Hosu, Khazan, Logan, Webb) ab und setze das Wappen in den Wappengarten.","Sammlungen: Spende alle Fische, Blumen und Artefakte — 'One Collection to Rule Them All' braucht das volle Museum.","Verwandlungen: Meerjungfrau, Fledermaus, Hellkitten über die Story; 'Tree Hugger' aus einer Romanze.","Geschenke: 25 geliebte in einer Nacht (Serial Gifter) und 299 gesamt (A Generous Donor).","Verpassbar: Werwolf bei Vollmond (Awooooo!), Kohle zu Pakkeleg (Bad Santa!), Missing fangen (Missing? No!)."])
A("moonlight-peaks/achievements", "de", 2, items=[["Wie viele Erfolge?","59 zum Start (6.–7. Juli 2026)."],["Am schwersten?","'One Collection to Rule Them All' (Museum), 'Fishing Pro' (22 Fische) und 'A Farming Monopoly' (1.000.000 Münzen)."],["Verpassbar?","Ja — an Ereignisse (Vollmond, Pakkeleg) oder späte Story-Fenster gebunden."]])

# ---------------- walkthrough ----------------
A("moonlight-peaks/walkthrough", "zh-CN", 3, items=[["主线有多长？","攻略覆盖 8 个部分；完成党还要补博物馆、图鉴、全鱼/全花与全部家族纹章。"],["哪些家族任务产出纹章？","Ambrosia、Dracula、Henderson、Hosu、Khazan、Logan 与 Webb 各以一枚纹章收尾（放入纹章园）。"],["什么时候能变身？","猫形态（晚宴，第 2 部分）、人鱼（Webb 线，第 5 部分）、蝙蝠（Orlock，第 7 部分）、Hellkitten 等随剧情解锁。"]])
A("moonlight-peaks/walkthrough", "ja", 3, items=[["メインはどれくらい？","全8部。コンプには博物館・図鑑・全魚・全花・全家族の紋章も。"],["紋章の家族は？","Ambrosia、Dracula、Henderson、Hosu、Khazan、Logan、Webb が紋章で締め。"],["変身はいつ？","猫（晩餐会・第2部）、人魚（Webb・第5部）、蝙蝠（Orlock・第7部）、Hellkitten など。"]])
A("moonlight-peaks/walkthrough", "ko", 3, items=[["메인 스토리는?", "총 8부. 100%에는 박물관·도감·전어·전화·전 가문 문장도."],["문장 가문은?", "Ambrosia, Dracula, Henderson, Hosu, Khazan, Logan, Webb."],["변신 시점?", "고양이(만찬·2부), 인어(Webb·5부), 박쥐(Orlock·7부), Hellkitten 등."]])
A("moonlight-peaks/walkthrough", "fr", 3, items=[["Combien de temps ?","La soluce couvre 8 parties ; le 100 % ajoute musée, journal, tous poissons/fleurs et emblèmes."],["Quelles familles donnent des emblèmes ?","Ambrosia, Dracula, Henderson, Hosu, Khazan, Logan et Webb."],["Quand se transformer ?","Chat (soirée, partie 2), sirène (Webb, partie 5), chauve-souris (Orlock, partie 7), Hellkitten, etc."]])
A("moonlight-peaks/walkthrough", "de", 3, items=[["Wie lang ist die Story?","8 Teile; für 100 % kommen Museum, Journal, alle Fische/Blumen und Wappen dazu."],["Welche Familien geben Wappen?","Ambrosia, Dracula, Henderson, Hosu, Khazan, Logan und Webb."],["Wann verwandeln?","Katze (Abendessen, Teil 2), Meerjungfrau (Webb, Teil 5), Fledermaus (Orlock, Teil 7), Hellkitten usw."]])

# ---------------- relationships ----------------
A("moonlight-peaks/relationships", "zh-CN", 1, items=["心数 3 级——可以拥抱角色。","心数 4 级——可以约TA出去；约会时解锁接吻。","心数满——求婚并结婚（“Tied the Knot”）。","与每个角色达到 4 心——解锁“Social Butterfly”成就。"])
A("moonlight-peaks/relationships", "zh-CN", 2, items=[["每天能送几件礼物？","每个角色每天一件。"],["怎么知道角色喜欢什么？","送一件后查看已赠列表：星标=喜欢，心标=最爱。"],["能和非恋爱 NPC 交朋友吗？","能——十多位额外 NPC 可通过礼物与对话交好。"],["约会失败会怎样？","损失好感。按提示操作并准时赴约。"]])

# ---------------- villagers ----------------
A("moonlight-peaks/villagers", "zh-CN", 1, items=["Webb of Wonders（Sabrina）：咒语、魔力升级、背包扩容。","Third Eye Threads（Aras）：衣物与时尚。","The Howling Hammer（Ridge）：工具升级，周一至周五 18:00–24:00。","Coffee and Coffins：饮品与食材（Evan 与 Mina）。","The Broken Lamp：酒吧，23:00 后 Samael 出现。","Luna 的农场（Moonlit Pines）：种子与动物。"])

# ---------------- potions ----------------
A("moonlight-peaks/potions", "zh-CN", 2, items=[["什么时候解锁药水？","主线推进到第 4 部分（博物馆、Nokturna 与药水制作）时解锁。"],["哪种药水回复魔力？","魔力药水（也是 Noel 的最爱礼物之一）。"],["怎么拿“魔法鸡尾酒”成就？","囤好药水，然后快速连续喝下，让所有药效同时生效。"]])

# ---------------- museum ----------------
A("moonlight-peaks/museum", "zh-CN", 1, items=["“Archaeo-Logistics”——开启博物馆。","“One Collection to Rule Them All”——完成博物馆（捐出一切）。","“Skulls in a Net”——收集全部灵魂团。","“Back to the Den”——把全部 Vampster 送回巢穴。","“Back in Place”——归还全部塑料椅。","“Fishing Pro”——集齐全部 22 种鱼捐给水族馆收集。"])
A("moonlight-peaks/museum", "zh-CN", 2, items=[["博物馆任务线是谁的？","Jada，文物收藏家（随 Persephone 的剧情解锁）。"],["捐什么？","鱼（水族馆收集）、花、文物与灵魂团等收藏品。"],["100% 需要博物馆吗？","需要——完成它是“One Collection to Rule Them All”的前提。"]])

# ---------------- breeding ----------------
A("moonlight-peaks/breeding", "zh-CN", 2, items=[["什么时候解锁动物？","Luna 来信后——约第三天（早期）。"],["谷仓多少钱？","Ridge 的店铺（Howling Hammer）售价 4,000 金币。"],["鸡蛋能做什么？","煎蛋是 Hendersons 乔迁任务所需；蛋也可用于烹饪。"]])

# ---------------- updates ----------------
A("moonlight-peaks/updates", "zh-CN", 1, items=["Steam：启动游戏时自动更新。","Switch / Switch 2：在系统菜单中检查更新；主机补丁跟随 Steam 版发布。","存档跨补丁兼容（1.1.41 修复了存档恢复 bug）。"])
A("moonlight-peaks/updates", "zh-CN", 2, items=[["1.1.41 修了什么？","加载时间、全地块储物（含谷仓/温室）、刺绣提前、树苗显示结果季节，以及 23+ 项修复。"],["主机版有补丁吗？","有——主机补丁跟随 Steam 版发布（据 NintendoReporters）。"],["官方说明在哪看？","Steam app 2209900 的新闻中心；本站汇总已核实的补丁说明。"]])

# ---------------- steam-deck ----------------
A("moonlight-peaks/steam-deck", "zh-CN", 1, items=["将帧率限制在 40–60 FPS，获得稳定掌机体验。","使用 Deck 的控制器布局——游戏推荐手柄操作。","升级到 1.1.41+ 获取最新 Deck 操作修复。"])
A("moonlight-peaks/steam-deck", "zh-CN", 2, items=[["《月光小镇》是 Steam Deck 已验证吗？","截至撰写时未确认（待补）。游戏支持完整手柄输入与云存档。"],["在 Deck 上能跑吗？","配置要求不高（见配置要求页）——社区性能反馈仍在收集中。"]])

# ---------------- console ----------------
A("moonlight-peaks/console", "zh-CN", 1, items=["立绘风格：在 Switch 上可切换两套立绘预设（设置 → 立绘风格）：卡通+写实光影，或动漫风。","Switch 2 版：eShop 上单独列出的“Moonlight Peaks - Nintendo Switch 2 Edition”（2026-07-07）。","主机补丁跟随 Steam 版发布（1.1.41 已在 Steam 之后到达主机）。"])
A("moonlight-peaks/console", "zh-CN", 2, items=[["《月光小镇》在哪些平台？","PC（Steam）、Nintendo Switch、Switch 2 与 Google Play Games（Android）——均于 2026-07-06/07 发售。"],["主机版谁发行？","Marvelous Europe / XSEED Games。"],["有跨平台存档吗？","未确认——待补。"]])

# ---------------- system-requirements ----------------
A("moonlight-peaks/system-requirements", "zh-CN", 1, items=["macOS：支持（Steam 已确认 Mac 版；具体配置待补）。","Linux：未列出（待补）。","主机：不适用（Switch / Switch 2）。"])
A("moonlight-peaks/system-requirements", "zh-CN", 2, items=[["低配电脑能玩吗？","最低配置要求不高：Windows 10、Intel i3、6 GB 内存、GTX 660 2GB、8 GB 存储。"],["有 Mac 版吗？","有——Steam 上已列明支持 macOS。"]])

# ---------------- faq ----------------
A("moonlight-peaks/faq", "zh-CN", 1, items=["查礼物全表、恋爱指南、钓鱼图鉴与主线流程获取更深细节。","任何未核实内容都会明确标注“待补”——来源确认后我们会更新。"])

# 补充 ja/ko/fr/de 的 walkthrough/relationships/villagers/potions/museum/breeding/updates/steam-deck/console/sysreq/faq
A("moonlight-peaks/walkthrough", "ja", 3, items=[["メインはどれくらい？","全8部。コンプには博物館・図鑑・全魚・全花・全家族の紋章も。"],["紋章の家族は？","Ambrosia、Dracula、Henderson、Hosu、Khazan、Logan、Webb が紋章で締め。"],["変身はいつ？","猫（晩餐会・第2部）、人魚（Webb・第5部）、蝙蝠（Orlock・第7部）、Hellkitten など。"]])
A("moonlight-peaks/walkthrough", "ko", 3, items=[["메인 스토리는?","총 8부. 100%에는 박물관·도감·전어·전화·전 가문 문장도."],["문장 가문은?","Ambrosia, Dracula, Henderson, Hosu, Khazan, Logan, Webb."],["변신 시점?","고양이(만찬·2부), 인어(Webb·5부), 박쥐(Orlock·7부), Hellkitten 등."]])
A("moonlight-peaks/walkthrough", "fr", 3, items=[["Combien de temps ?","La soluce couvre 8 parties ; le 100 % ajoute musée, journal, tous poissons/fleurs et emblèmes."],["Quelles familles donnent des emblèmes ?","Ambrosia, Dracula, Henderson, Hosu, Khazan, Logan et Webb."],["Quand se transformer ?","Chat (soirée, partie 2), sirène (Webb, partie 5), chauve-souris (Orlock, partie 7), Hellkitten, etc."]])
A("moonlight-peaks/walkthrough", "de", 3, items=[["Wie lang ist die Story?","8 Teile; für 100 % kommen Museum, Journal, alle Fische/Blumen und Wappen dazu."],["Welche Familien geben Wappen?","Ambrosia, Dracula, Henderson, Hosu, Khazan, Logan und Webb."],["Wann verwandeln?","Katze (Abendessen, Teil 2), Meerjungfrau (Webb, Teil 5), Fledermaus (Orlock, Teil 7), Hellkitten usw."]])
A("moonlight-peaks/relationships", "ja", 1, items=["ハート3——ハグ可能。","ハート4——デート可能に。デート中にキスも。","ハート最大——プロポーズして結婚（「Tied the Knot」）。","全キャラ4ハート——「Social Butterfly」実績。"])


# relationships 其余语言
A("moonlight-peaks/relationships", "ja", 2, items=[["贈り物は1日いくつ？","キャラごとに1日1個。"],["好みはどう分かる？","贈った後のリストで星=好物、ハート=大好物。"],["NPC と友達になれる？","はい——10人以上のNPCが贈り物と会話で友好に。"],["デート失敗の影響？","好感度が減ります。指示に従い時間通りに。"]])
A("moonlight-peaks/relationships", "ko", 1, items=["하트 3 — 포옹 가능.","하트 4 — 데이트 가능. 데이트 중 키스도.","하트 최대 — 프로포즈·결혼('Tied the Knot').","모든 캐릭터 4하트 — 'Social Butterfly' 업적."])
A("moonlight-peaks/relationships", "ko", 2, items=[["선물은 하루 몇 개?", "캐릭터당 하루 1개."],["호감도 파악법?", "선물 후 목록에서 별=좋아함, 하트=최애."],["NPC와 친구 가능?", "네 — 10명 이상 NPC가 선물·대화로 친구가 됩니다."],["데이트 실패 영향?", "호감도 감소. 지시를 따르고 제시간에 도착하세요."]])
A("moonlight-peaks/relationships", "fr", 1, items=["Niveau de cœur 3 — câlin.","Niveau 4 — rendez-vous ; baiser pendant les dates.","Cœur max — proposer et se marier ('Tied the Knot').","4 cœurs avec tout le monde — succès 'Social Butterfly'."])
A("moonlight-peaks/relationships", "fr", 2, items=[["Combien de cadeaux par jour ?","Un par personnage et par jour."],["Comment savoir ?","Dans la liste des cadeaux : étoile = aimé, cœur = adoré."],["Amis avec les PNJ ?","Oui — plus d'une douzaine de PNJ via cadeaux et dialogues."],["Échec d'un date ?","Perte de points ; suivez les consignes et arrivez à l'heure."]])
A("moonlight-peaks/relationships", "de", 1, items=["Herz-Stufe 3 — Umarmung.","Stufe 4 — Dates; Kuss während der Dates.","Max. Herz — Antrag und Heirat ('Tied the Knot').","4 Herzen mit allen — Erfolg 'Social Butterfly'."])
A("moonlight-peaks/relationships", "de", 2, items=[["Wie viele Geschenke pro Tag?","Eins pro Charakter und Tag."],["Wie erkennen?", "In der Geschenkliste: Stern = gemocht, Herz = geliebt."],["NPC-Freunde?", "Ja — über ein Dutzend NPCs per Geschenken und Dialog."],["Date scheitert?", "Punkteverlust; Anweisungen folgen und pünktlich sein."]])

# villagers 其余语言
A("moonlight-peaks/villagers", "ja", 1, items=["Webb of Wonders（Sabrina）：呪文、マナ強化、バックパック拡張。","Third Eye Threads（Aras）：服とファッション。","The Howling Hammer（Ridge）：道具強化、月〜金18:00〜24:00。","Coffee and Coffins：飲み物と材料（Evan と Mina）。","The Broken Lamp：バー。23:00以降 Samael。","Luna の農場（Moonlit Pines）：種と動物。"])

# potions 其余语言
A("moonlight-peaks/potions", "ja", 2, items=[["ポーションはいつ？","メインストーリー第4部で解放。"],["マナ回復のポーションは？","マナポーション（Noel の大好物でもある）。"],["「A Magical Cocktail」は？","ポーションを溜めて素早く飲み、全効果を同時に。"]])
A("moonlight-peaks/potions", "ko", 2, items=[["물약은 언제?", "메인 스토리 4부에서 해금."],["마나 회복 물약?", "마나 물약(Noel의 최애 선물이기도)."],["'A Magical Cocktail'?", "물약을 모아 빠르게 마셔 모든 효과 동시 활성."]])
A("moonlight-peaks/potions", "fr", 2, items=[["Quand les potions ?","Pendant l'histoire (partie 4)."],["Potion de mana ?","La potion de mana (aussi un cadeau adoré de Noel)."],["'A Magical Cocktail' ?","Buvez plusieurs potions à la suite pour cumuler les effets."]])
A("moonlight-peaks/potions", "de", 2, items=[["Wann Tränke?","In der Hauptstory (Teil 4)."],["Mana-Trank?", "Der Mana-Trank (auch ein geliebtes Geschenk von Noel)."],["'A Magical Cocktail'?", "Mehrere Tränke schnell trinken, um alle Effekte zu stapeln."]])

# museum 其余语言
A("moonlight-peaks/museum", "ja", 1, items=["「Archaeo-Logistics」——博物館を開く。","「One Collection to Rule Them All」——博物館をコンプ。","「Skulls in a Net」——全ソウルブロブ。","「Back to the Den」——全 Vampster を巣へ。","「Back in Place」——全プラスチック椅子を戻す。","「Fishing Pro」——全22種の魚で水族館コレクション。"])

# breeding 其余语言
A("moonlight-peaks/breeding", "ja", 2, items=[["動物はいつ？","Luna の手紙後（3日目頃、序盤）。"],["納屋の値段は？","Ridge の店（Howling Hammer）で4,000コイン。"],["卵の使い道？","目玉焼きは Hendersons の引っ越しクエストに必要。料理にも。"]])
A("moonlight-peaks/breeding", "ko", 2, items=[["동물은 언제?", "Luna의 편지 후(3일차쯤, 초반)."],["헛간 가격?", "Ridge 상점(Howling Hammer)에서 4,000코인."],["달걀 용도?", "프라이드에그는 Hendersons 이사 퀘스트 필요. 요리에도."]])
A("moonlight-peaks/breeding", "fr", 2, items=[["Quand les animaux ?","Après la lettre de Luna (jour 3, tôt)."],["Prix de la grange ?","4 000 pièces chez Ridge (Howling Hammer)."],["Œufs ?","Œufs au plat pour la quête des Hendersons ; cuisine aussi."]])
A("moonlight-peaks/breeding", "de", 2, items=[["Wann Tiere?","Nach Lunas Brief (ca. Tag 3, früh)."],["Scheunenpreis?", "4.000 Münzen bei Ridge (Howling Hammer)."],["Eier?", "Spiegeleier für die Henderson-Quest; auch Kochen."]])

# updates 其余语言
A("moonlight-peaks/updates", "ja", 1, items=["Steam：起動時に自動更新。","Switch / Switch 2：システムメニューで更新確認。コンソール版は Steam 版に追随。","セーブはパッチ間で互換（1.1.41 で復元バグを修正）。"])
A("moonlight-peaks/updates", "ja", 2, items=[["1.1.41 の修正は？","ロード時間、敷地全体の収納（納屋・温室含む）、刺繍の早期解放、季節表示、23以上のバグ。"],["コンソール版のパッチは？","あります——Steam 版に追随（NintendoReporters より）。"],["公式ノートは？","Steam の app 2209900 ニュース。ここに検証済みを要約。"]])
A("moonlight-peaks/updates", "ko", 1, items=["Steam: 실행 시 자동 업데이트.","Switch/Switch 2: 시스템 메뉴에서 업데이트 확인. 콘솔 패치는 Steam에 이어 제공.","세이브는 패치 간 호환(1.1.41에서 복원 버그 수정)."])
A("moonlight-peaks/updates", "ko", 2, items=[["1.1.41 수정?", "로딩 시간, 부지 전체 창고(헛간·온실), 자수 조기 해금, 계절 표시, 23개 이상 버그."],["콘솔 패치?", "네 — Steam 버전에 이어 제공(NintendoReporters)."],["공식 노트?", "Steam app 2209900 뉴스. 여기에 검증된 내용을 요약."]])
A("moonlight-peaks/updates", "fr", 1, items=["Steam : mise à jour auto au lancement.","Switch / Switch 2 : vérifiez dans le menu système ; les patchs consoles suivent Steam.","Sauvegardes compatibles (1.1.41 a corrigé la restauration)."])
A("moonlight-peaks/updates", "fr", 2, items=[["Que corrige 1.1.41 ?","Chargement, stockage sur tout le terrain (granges/serres), broderie plus tôt, saisons, 23+ correctifs."],["Patchs consoles ?","Oui — ils suivent Steam (NintendoReporters)."],["Notes officielles ?","Hub Steam app 2209900 ; résumé vérifié ici."]])
A("moonlight-peaks/updates", "de", 1, items=["Steam: automatisch beim Start.","Switch/Switch 2: im Systemmenü prüfen; Konsolen-Patches folgen Steam.","Saves bleiben kompatibel (1.1.41 fixte die Wiederherstellung)."])
A("moonlight-peaks/updates", "de", 2, items=[["Was fixte 1.1.41?","Ladezeiten, Lager auf dem Grundstück (Scheunen/Gewächshäuser), Stickerei früher, Jahreszeiten, 23+ Fixes."],["Konsolen-Patches?", "Ja — sie folgen Steam (NintendoReporters)."],["Offizielle Notizen?", "Steam-Hub app 2209900; hier zusammengefasst."]])

# steam-deck 其余语言
A("moonlight-peaks/steam-deck", "ja", 1, items=["フレームレートを40〜60FPSに制限して安定させる。","Deck のコントローラーレイアウトを利用（ゲームはパッド推奨）。","1.1.41+ で最新の Deck コントロール修正を。"])

# console 其余语言
A("moonlight-peaks/console", "ja", 1, items=["ポートレート：Switch で2つのプリセットを切替（設定→Portrait Style）。カートゥーン or アニメ風。","Switch 2 版：eShop で「Moonlight Peaks - Nintendo Switch 2 Edition」（2026-07-07）。","コンソール版のパッチは Steam 版に追随（1.1.41 も）。"])

# system-requirements 其余语言
A("moonlight-peaks/system-requirements", "ja", 1, items=["macOS：対応（Steam で Mac 版確認済み。詳細スペックは待補）。","Linux：未掲載（待補）。","コンソール：対象外（Switch / Switch 2）。"])

# faq 其余语言
A("moonlight-peaks/faq", "ja", 1, items=["贈り物ガイド、恋愛ガイド、釣りガイド、ストーリー攻略でさらに詳しく。","未検証の内容は「待補」と明記——ソース確認後に更新します。"])
A("moonlight-peaks/faq", "ko", 1, items=["선물 가이드, 연애 가이드, 낚시 가이드, 메인 공략에서 더 자세히.", "검증되지 않은 내용은 '대기'로 표시 — 출처 확인 후 업데이트합니다."])
A("moonlight-peaks/faq", "fr", 1, items=["Consultez les guides cadeaux, romance, pêche et la soluce pour plus de détails.","Tout ce qui n'est pas vérifié est marqué 'à compléter' — mis à jour dès confirmation."])
A("moonlight-peaks/faq", "de", 1, items=["Mehr Details in Geschenke-, Romantik-, Angel-Guide und Komplettlösung.","Alles Unverifizierte ist mit 'offen' markiert — wird nach Bestätigung aktualisiert."])


# villagers ko/fr/de
A("moonlight-peaks/villagers", "ko", 1, items=["Webb of Wonders(Sabrina): 주문, 마나 강화, 가방 확장.", "Third Eye Threads(Aras): 옷과 패션.", "The Howling Hammer(Ridge): 도구 강화, 월~금 18:00~24:00.", "Coffee and Coffins: 음료와 재료(Evan과 Mina).", "The Broken Lamp: 바. 23:00 이후 Samael.", "Luna 농장(Moonlit Pines): 씨앗과 동물."])
A("moonlight-peaks/villagers", "fr", 1, items=["Webb of Wonders (Sabrina) : sorts, mana, emplacements de sac.", "Third Eye Threads (Aras) : vêtements.", "The Howling Hammer (Ridge) : outils, 18h–minuit lundi–vendredi.", "Coffee and Coffins : boissons et ingrédients (Evan & Mina).", "The Broken Lamp : bar, Samael après 23h.", "Ferme de Luna (Moonlit Pines) : graines et animaux."])
A("moonlight-peaks/villagers", "de", 1, items=["Webb of Wonders (Sabrina): Zauber, Mana, Inventarplätze.", "Third Eye Threads (Aras): Kleidung.", "The Howling Hammer (Ridge): Werkzeuge, 18–24 Uhr Mo–Fr.", "Coffee and Coffins: Getränke und Zutaten (Evan & Mina).", "The Broken Lamp: Bar, Samael nach 23 Uhr.", "Lunas Hof (Moonlit Pines): Samen und Tiere."])

# museum ko/fr/de
A("moonlight-peaks/museum", "ko", 1, items=["'Archaeo-Logistics' — 박물관 개관.", "'One Collection to Rule Them All' — 박물관 완성.", "'Skulls in a Net' — 소울 블롭 전체 수집.", "'Back to the Den' — 뱀프스터 전원 보금자리로.", "'Back in Place' — 플라스틱 의자 전부 반납.", "'Fishing Pro' — 물고기 22종 수족관 컬렉션."])
A("moonlight-peaks/museum", "fr", 1, items=["'Archaeo-Logistics' — ouvrir le musée.", "'One Collection to Rule Them All' — compléter le musée.", "'Skulls in a Net' — tous les Soul Blobs.", "'Back to the Den' — tous les Vampsters.", "'Back in Place' — toutes les chaises en plastique.", "'Fishing Pro' — les 22 poissons pour l'aquarium."])
A("moonlight-peaks/museum", "de", 1, items=["'Archaeo-Logistics' — Museum öffnen.", "'One Collection to Rule Them All' — Museum vervollständigen.", "'Skulls in a Net' — alle Soul Blobs.", "'Back to the Den' — alle Vampster.", "'Back in Place' — alle Plastikstühle.", "'Fishing Pro' — alle 22 Fische für das Aquarium."])

# steam-deck ko/fr/de
A("moonlight-peaks/steam-deck", "ko", 1, items=["프레임 40~60FPS로 제한해 안정적으로.", "Deck 컨트롤러 레이아웃 사용(패드 권장).", "1.1.41+로 최신 Deck 조작 수정 적용."])
A("moonlight-peaks/steam-deck", "fr", 1, items=["Limitez à 40–60 FPS pour une expérience stable.", "Utilisez la disposition manette du Deck (manette recommandée).", "Mettez à jour en 1.1.41+ pour les correctifs Deck."])
A("moonlight-peaks/steam-deck", "de", 1, items=["Frame auf 40–60 FPS begrenzen.", "Deck-Controller-Layout nutzen (Gamepad empfohlen).", "Auf 1.1.41+ für die neuesten Deck-Fixes updaten."])

# console ko/fr/de
A("moonlight-peaks/console", "ko", 1, items=["초상화: Switch에서 프리셋 2개 전환(설정→Portrait Style). 카툰 or 애니풍.", "Switch 2판: eShop에 'Moonlight Peaks - Nintendo Switch 2 Edition'(2026-07-07).", "콘솔 패치는 Steam에 이어 제공(1.1.41도)."])
A("moonlight-peaks/console", "fr", 1, items=["Portraits : deux préréglages sur Switch (Réglages → Portrait Style) : cartoon ou anime.", "Switch 2 : 'Moonlight Peaks - Nintendo Switch 2 Edition' sur l'eShop (07/07/2026).", "Les patchs consoles suivent Steam (1.1.41 aussi)."])
A("moonlight-peaks/console", "de", 1, items=["Porträts: zwei Presets auf Switch (Einstellungen → Portrait Style): Cartoon oder Anime.", "Switch 2: 'Moonlight Peaks - Nintendo Switch 2 Edition' im eShop (07.07.2026).", "Konsolen-Patches folgen Steam (auch 1.1.41)."])

# system-requirements ko/fr/de
A("moonlight-peaks/system-requirements", "ko", 1, items=["macOS: 지원(Steam에서 Mac 버전 확인. 세부 사양은 대기).", "Linux: 미기재(대기).", "콘솔: 해당 없음(Switch/Switch 2)."])
A("moonlight-peaks/system-requirements", "fr", 1, items=["macOS : pris en charge (version Mac confirmée sur Steam ; specs à compléter).", "Linux : non listé (à compléter).", "Consoles : N/A (Switch / Switch 2)."])
A("moonlight-peaks/system-requirements", "de", 1, items=["macOS: unterstützt (Mac-Version auf Steam bestätigt; Specs offen).", "Linux: nicht gelistet (offen).", "Konsolen: N/A (Switch / Switch 2)."])

# console FAQ 其余语言
A("moonlight-peaks/console", "ja", 2, items=[["対応機種は？","PC（Steam）、Switch、Switch 2、Google Play Games（Android）——2026年7月6〜7日発売。"],["コンソール版の発売元は？","Marvelous Europe / XSEED Games。"],["クロスセーブは？","未確認——待補。"]])
A("moonlight-peaks/console", "ko", 2, items=[["플랫폼은?","PC(Steam), Switch, Switch 2, Google Play Games(Android) — 2026년 7월 6~7일 출시."],["콘솔 배급사?", "Marvelous Europe / XSEED Games."],["크로스 세이브?", "미확인 — 대기."]])
A("moonlight-peaks/console", "fr", 2, items=[["Plateformes ?","PC (Steam), Switch, Switch 2 et Google Play Games — sorties les 6–7 juillet 2026."],["Éditeur consoles ?","Marvelous Europe / XSEED Games."],["Cross-save ?","Non confirmé — à compléter."]])
A("moonlight-peaks/console", "de", 2, items=[["Plattformen?","PC (Steam), Switch, Switch 2 und Google Play Games — erschienen am 6.–7. Juli 2026."],["Konsolen-Publisher?", "Marvelous Europe / XSEED Games."],["Cross-Save?", "Nicht bestätigt — offen."]])

# steam-deck FAQ 其余语言
A("moonlight-peaks/steam-deck", "ja", 2, items=[["Steam Deck 公式対応？","執筆時点で未確認（待補）。フルコントローラー入力とクラウドセーブ対応。"],["Deck で動く？","軽量なcozy simで要求は控えめ（動作環境参照）——コミュニティの性能報告を収集中。"]])
A("moonlight-peaks/steam-deck", "ko", 2, items=[["Steam Deck 공식 지원?", "작성 시점 미확인(대기). 전체 컨트롤러 입력과 클라우드 세이브 지원."],["Deck에서 돌아가나요?", "가벼운 코지 심, 요구 사양 낮음(시스템 요구 사항 참고) — 커뮤니티 성능 보고 수집 중."]])
A("moonlight-peaks/steam-deck", "fr", 2, items=[["Steam Deck Verified ?","Non confirmé (à compléter). Il prend en charge manettes et cloud."],["Tourne sur Deck ?","Life-sim léger aux specs modestes (voir configuration) — retours communautaires en cours."]])
A("moonlight-peaks/steam-deck", "de", 2, items=[["Steam Deck Verified?", "Nicht bestätigt (offen). Unterstützt Controller und Cloud."],["Läuft es auf dem Deck?", "Leichtes Life-Sim, moderate Anforderungen (siehe Systemanforderungen) — Community-Berichte folgen."]])

# system-requirements FAQ 其余语言
A("moonlight-peaks/system-requirements", "ja", 2, items=[["低スペックPCで動く？","最低構成は控えめ：Windows 10、Intel i3、6GB RAM、GTX 660 2GB、8GB。"],["Mac版は？","はい——Steam で macOS 対応と明記。"]])
A("moonlight-peaks/system-requirements", "ko", 2, items=[["저사양 PC에서?", "최소 사양은 낮음: Windows 10, Intel i3, 6GB RAM, GTX 660 2GB, 8GB."],["Mac 버전?", "네 — Steam에 macOS 지원 명시."]])
A("moonlight-peaks/system-requirements", "fr", 2, items=[["Sur un PC modeste ?","Le minimum est léger : Win10, i3, 6 Go RAM, GTX 660 2 Go, 8 Go."],["Version Mac ?","Oui — macOS listé sur Steam."]])
A("moonlight-peaks/system-requirements", "de", 2, items=[["Auf schwachem PC?", "Das Minimum ist moderat: Win10, i3, 6 GB RAM, GTX 660 2 GB, 8 GB."],["Mac-Version?", "Ja — macOS wird auf Steam gelistet."]])

# villagers FAQ 全部语言
A("moonlight-peaks/villagers", "zh-CN", 2, items=[["镇长是谁？","Brook，一位狼人——他在市政厅为你登记。"],["在哪里买种子？","Moonlit Pines 的 Luna 商店。"],["谁帮我升级工具？","Howling Hammer 的 Ridge（营业 18:00–24:00，周一至周五）。"]])
A("moonlight-peaks/villagers", "ja", 2, items=[["町長は？","Brook（狼人）。タウンホールで登録してくれます。"],["種はどこで？","Moonlit Pines の Luna の店。"],["道具は誰が？","Howling Hammer の Ridge（18:00〜24:00、月〜金）。"]])
A("moonlight-peaks/villagers", "ko", 2, items=[["시장은?", "Brook(늑대인간). 타운홀에서 등록해 줍니다."],["씨앗은 어디서?", "Moonlit Pines의 Luna 상점."],["도구 강화는?", "Howling Hammer의 Ridge(18:00~24:00, 월~금)."]])
A("moonlight-peaks/villagers", "fr", 2, items=[["Qui est le maire ?","Brook, un loup-garou — il vous inscrit à l'Hôtel de Ville."],["Où acheter des graines ?","La boutique de Luna à Moonlit Pines."],["Qui améliore les outils ?","Ridge au Howling Hammer (18h–minuit, lundi–vendredi)."]])
A("moonlight-peaks/villagers", "de", 2, items=[["Wer ist der Bürgermeister?", "Brook, ein Werwolf — er registriert dich im Rathaus."],["Wo Samen kaufen?", "Lunas Laden in Moonlit Pines."],["Wer upgradet Werkzeuge?", "Ridge im Howling Hammer (18–24 Uhr, Mo–Fr)."]])

# museum FAQ 其余语言
A("moonlight-peaks/museum", "ja", 2, items=[["博物館のクエストは誰？","Jada（遺物コレクター）。Persephone のストーリーで解放。"],["何を寄贈？","魚（水族館）、花、遺物、ソウルブロブなどのコレクション。"],["100% に必要？","はい——「One Collection to Rule Them All」に必須。"]])
A("moonlight-peaks/museum", "ko", 2, items=[["박물관 퀘스트는?", "Jada(유물 수집가). Persephone 스토리로 해금."],["뭘 기증?", "물고기(수족관), 꽃, 유물, 소울 블롭 등."],["100%에 필수?", "네 — 'One Collection to Rule Them All'에 필수."]])
A("moonlight-peaks/museum", "fr", 2, items=[["Qui dirige la quête ?","Jada, la collectionneuse (avec l'histoire de Persephone)."],["Quoi donner ?","Poissons (aquarium), fleurs, artefacts, Soul Blobs."],["Nécessaire pour 100 % ?","Oui — requis pour 'One Collection to Rule Them All'."]])
A("moonlight-peaks/museum", "de", 2, items=[["Wer führt die Quest?", "Jada, die Sammlerin (mit Persephones Story)."],["Was spenden?", "Fische (Aquarium), Blumen, Artefakte, Soul Blobs."],["Für 100 % nötig?", "Ja — für 'One Collection to Rule Them All'."]])
# 2026-08-12 数据深化追加：1.1.45/1.1.44 补丁、药水9配方、动物7种、博物馆5展室
# （后写覆盖先写；museum 索引随 MUS_EN 新结构重排：0开馆/1五展室/2神室/3完成/4FAQ）
# =====================================================================
# home: 最新更新（1.1.45 / 1.1.44 / 发布）
A("moonlight-peaks", "zh-CN", 2, items=["补丁 1.1.45（2026-07-21）：起播光敏警告、观星宽屏黑条修复、“Back to the Den”补发解锁——更多改进计划在 1.2。","补丁 1.1.44（2026-07-16）：刺绣桌可见、树苗全年可种、雨天晚上作物修复、存档损坏修复。","2026-07-06/07 登陆 PC（Steam）、Switch、Switch 2 与 Google Play Games；7 月 26 日销量破 20 万。"])
A("moonlight-peaks", "ja", 2, items=["パッチ1.1.45（2026-07-21）：起動時の光過敏警告、Star Gazing のワイド画面黒帯修正、「Back to the Den」の遡及解除。1.2 でさらなる改善予定。","パッチ1.1.44（2026-07-16）：刺繍テーブルの表示、苗木の全季節植え付け、雨の夜の作物修正、セーブ破損修正。","2026年7月6〜7日にPC・Switch・Switch 2・Google Play Gamesで発売、7月26日までに20万本突破。"])
A("moonlight-peaks", "ko", 2, items=["패치 1.1.45(2026-07-21): 시작 시 광과민 경고, 별자리 관측 와이드 화면 수정, 'Back to the Den' 소급 해금. 1.2에서 추가 개선 예정.","패치 1.1.44(2026-07-16): 자수 테이블 표시, 묘목 전 계절 심기, 비 오는 밤 작물 수정, 세이브 손상 수정.","2026년 7월 6~7일 PC·Switch·Switch 2·Google Play Games 출시, 7월 26일 20만 장 돌파."])
A("moonlight-peaks", "fr", 2, items=["Patch 1.1.45 (21/07/2026) : avertissement de photosensibilité, correctif Star Gazing écran large, déblocage rétroactif 'Back to the Den'. D'autres améliorations en 1.2.","Patch 1.1.44 (16/07/2026) : table de broderie visible, pousses plantables toute l'année, correctif cultures les nuits de pluie, correctif de sauvegarde.","Sorti les 6–7 juillet 2026 sur PC, Switch, Switch 2 et Google Play Games ; plus de 200 000 ventes au 26 juillet."])
A("moonlight-peaks", "de", 2, items=["Patch 1.1.45 (21.07.2026): Fotosensibilitäts-Warnung, Star-Gazing-Breitbild-Fix, 'Back to the Den' nachträglich. Mehr in 1.2.","Patch 1.1.44 (16.07.2026): Sticktisch sichtbar, Setzlinge ganzjährig, Pflanzenfix an Regennächten, Speicherfehler-Fix.","Release 6.–7. Juli 2026 auf PC, Switch, Switch 2 und Google Play Games; über 200.000 Verkäufe bis 26. Juli."])

# potions: FAQ（9配方版）
A("moonlight-peaks/potions", "zh-CN", 2, items=[["什么时候解锁药水？","主线推进到第 4 部分（博物馆、Nokturna 与药水制作）时解锁。"],["哪种药水恢复魔力？","魔力药水恢复 8 点魔力（也是 Noel 的最爱礼物）。"],["哪种药水最赚钱？","魔力药水（3,200 金币）是目前发现的最贵配方。"],["红酒是药水吗？","不是——红酒是酒桶产物（Orlock 的任务物品，也是最爱礼物），不用坩埚酿。"],["怎么拿“魔法鸡尾酒”成就？","囤好药水，然后快速连续喝下，让所有药效同时生效。"]])
A("moonlight-peaks/potions", "ja", 2, items=[["ポーションはいつ解放？","メインストーリー第4部で解放。"],["マナ回復は？","Mana Potion がマナを8回復（Noel の大好物でもある）。"],["一番売れるのは？","Mana Potion（3,200コイン）が現時点で最高値。"],["赤ワインはポーション？","いいえ——たるで作るアイテム（Orlock のクエスト品で大好物）。大釜では作りません。"],["「A Magical Cocktail」は？","全ポーションを確保し、続けて飲んで全効果を同時に。"]])
A("moonlight-peaks/potions", "ko", 2, items=[["물약은 언제 해금?","메인 스토리 4부에서 해금."],["마나 회복 물약은?","Mana Potion이 마나 8 회복(Noel의 최애 선물이기도)."],["가장 비싼 물약은?","Mana Potion(3,200코인)이 현재 최고가."],["레드 와인은 물약인가요?","아니요 — 술통 아이템(Orlock 퀘스트용, 최애 선물). 가마솥으로 만들지 않습니다."],["'A Magical Cocktail'은?","물약을 모아 두고 연속으로 마셔 모든 효과를 동시에. "]])
A("moonlight-peaks/potions", "fr", 2, items=[["Quand débloquer les potions ?","Pendant l'histoire principale (partie 4)."],["Quelle potion restaure le mana ?","La Mana Potion restaure 8 de mana (cadeau adoré de Noel aussi)."],["La plus chère ?","Mana Potion (3 200 pièces) — la plus chère trouvée."],["Le vin rouge est-il une potion ?","Non — un produit du tonneau (objet de quête pour Orlock, cadeau adoré), pas un brassin de chaudron."],["Comment avoir 'A Magical Cocktail' ?","Stockez les potions puis buvez-les à la suite pour cumuler les effets."]])
A("moonlight-peaks/potions", "de", 2, items=[["Wann Tränke freischalten?","In der Hauptstory (Teil 4)."],["Welcher Trank stellt Mana wieder her?","Mana Potion stellt 8 Mana wieder her (auch ein Lieblingsgeschenk von Noel)."],["Der teuerste?","Mana Potion (3.200 Münzen) — der bisher teuerste."],["Ist Rotwein ein Trank?","Nein — ein Fassprodukt (Quest-Item für Orlock, geliebtes Geschenk), nicht im Kessel."],["Wie bekomme ich 'A Magical Cocktail'?","Tränke horten und nacheinander trinken, damit alle Effekte gleichzeitig aktiv sind."]])

# breeding: FAQ（7动物版）
A("moonlight-peaks/breeding", "zh-CN", 2, items=[["什么时候解锁动物？","Luna 来信后——约第三天（早期）。"],["谷仓多少钱？","Ridge 的店铺（Howling Hammer）售价 4,000 金币。"],["哪种动物回本最快？","Cheeken（1,200）每天产蛋，是最便宜入门；Bumpkin（秋季 12,000）目前最贵。"],["鸡蛋能做什么？","煎蛋是 Hendersons 乔迁任务所需；蛋也可用于烹饪。"]])
A("moonlight-peaks/breeding", "ja", 2, items=[["動物はいつ解放？","Luna の手紙後（3日目頃、序盤）。"],["納屋の値段は？","Ridge の店（Howling Hammer）で4,000コイン。"],["回収が早い動物は？","Cheekens（1,200）は毎日卵を産み最も手軽。Bumpkin（秋・12,000）が今のところ最高額。"],["卵の使い道は？","Hendersons の引っ越しクエストに目玉焼き、料理にも。"]])
A("moonlight-peaks/breeding", "ko", 2, items=[["동물은 언제 해금?","Luna의 편지 후(3일차쯤, 초반)."],["헛간 가격은?","Ridge 상점(Howling Hammer)에서 4,000코인."],["회수 빠른 동물은?","Cheeken(1,200)이 매일 알을 낳아 가장 가볍고, Bumpkin(가을·12,000)이 현재 최고가."],["달걀 용도는?","프라이드에그는 Hendersons 이사 퀘스트 필요. 요리에도."]])
A("moonlight-peaks/breeding", "fr", 2, items=[["Quand débloquer les animaux ?","Après la lettre de Luna (jour 3, tôt)."],["Prix de la grange ?","4 000 pièces chez Ridge (Howling Hammer)."],["Le plus rentable ?","Cheeken (1 200) pond chaque jour ; Bumpkin (automne, 12 000) est le plus cher."],["Œufs ?","Œufs au plat pour la quête des Hendersons ; cuisine aussi."]])
A("moonlight-peaks/breeding", "de", 2, items=[["Wann Tiere freischalten?","Nach Lunas Brief (ca. Tag 3, früh)."],["Scheunenpreis?","4.000 Münzen bei Ridge (Howling Hammer)."],["Am schnellsten rentabel?","Cheeken (1.200) legt täglich Eier; Bumpkin (Herbst, 12.000) ist das teuerste."],["Wofür Eier?","Spiegeleier für die Henderson-Quest; auch Kochen."]])

# museum: 新结构 1=五展室 / 2=神室表头 / 3=完成成就(原1) / 4=FAQ(原2)
A("moonlight-peaks/museum", "zh-CN", 1, heading='五个展室', items=["生物室（Critters Room）——小型生物与萌宠。","神室（Deity Room）——诸神的圣物（见下方表格）。","农业室（Farming Room）——农耕收藏（含 Amanita，夏秋两季种植）。","超自然室（Supernatural Room）——超自然遗物。","水族馆室（Aquarium Room）——鱼类收藏（集齐 22 种鱼得“Fishing Pro”）。"])
A("moonlight-peaks/museum", "zh-CN", 2, heading='神室文物（4 件）', headers=["文物", "获取方式"])
A("moonlight-peaks/museum", "zh-CN", 3, heading='完成与成就', items=["“Archaeo-Logistics”——开启博物馆。","“One Collection to Rule Them All”——完成博物馆（捐出一切）。","“Skulls in a Net”——收集全部灵魂团。","“Back to the Den”——把全部 Vampster 送回巢穴。","“Back in Place”——归还全部塑料椅。","“Fishing Pro”——集齐全部 22 种鱼捐给水族馆收集。"])
A("moonlight-peaks/museum", "zh-CN", 4, items=[["博物馆任务线是谁的？","Jada，文物收藏家（随 Persephone 的剧情解锁）。"],["博物馆有几个展室？","5 个：生物室、神室、农业室、超自然室与水族馆室。"],["神室有什么？","4 件圣物：Death 满好感的 Death's Tomb、月神/太阳神/Llemi 满好感的 Chakra Tuner、Sun God's Halo、Llemi's Bow。"],["捐什么？","鱼（水族馆收集）、花、文物与灵魂团等收藏品。"],["100% 需要博物馆吗？","需要——完成它是“One Collection to Rule Them All”的前提。"]])
A("moonlight-peaks/museum", "ja", 1, heading='5つの展示室', items=["クリッター室（Critters Room）——小さな生き物。","神の間（Deity Room）——神々の聖物（下表参照）。","農業室（Farming Room）——農耕コレクション（Amanita は夏・秋に栽培）。","超自然室（Supernatural Room）——超自然の遺物。","水族館室（Aquarium Room）——魚コレクション（全22種で「Fishing Pro」）。"])
A("moonlight-peaks/museum", "ja", 2, heading='神の間の遺物（4点）', headers=["遺物", "入手方法"])
A("moonlight-peaks/museum", "ja", 3, heading='完成と実績', items=["「Archaeo-Logistics」——博物館を開く。","「One Collection to Rule Them All」——博物館をコンプ。","「Skulls in a Net」——全ソウルブロブ。","「Back to the Den」——全 Vampster を巣へ。","「Back in Place」——全プラスチック椅子を戻す。","「Fishing Pro」——全22種の魚で水族館コレクション。"])
A("moonlight-peaks/museum", "ja", 4, items=[["博物館のクエストは誰？","Jada（遺物コレクター）。Persephone のストーリーで解放。"],["展示室はいくつ？","5つ：クリッター、神、農業、超自然、水族館。"],["神の間には？","4点：Death 好感度MAXの Death's Tomb、月神・太陽神・Llemi 好感度MAXの Chakra Tuner / Sun God's Halo / Llemi's Bow。"],["何を寄贈？","魚（水族館）、花、遺物、ソウルブロブなどのコレクション。"],["100% に必要？","はい——「One Collection to Rule Them All」に必須。"]])
A("moonlight-peaks/museum", "ko", 1, heading='다섯 개의 전시실', items=["크리터즈 룸(Critters Room) — 작은 생물들.","신의 방(Deity Room) — 신들의 성물(아래 표 참조).","파밍 룸(Farming Room) — 농업 컬렉션(Amanita, 여름·가을 재배).","초자연의 방(Supernatural Room) — 초자연 유물.","아쿠아리움 룸(Aquarium Room) — 물고기 컬렉션(22종 완성 시 'Fishing Pro')."])
A("moonlight-peaks/museum", "ko", 2, heading='신의 방 유물(4점)', headers=["유물", "획득 방법"])
A("moonlight-peaks/museum", "ko", 3, heading='완성과 업적', items=["'Archaeo-Logistics' — 박물관 개관.", "'One Collection to Rule Them All' — 박물관 완성.", "'Skulls in a Net' — 소울 블롭 전체 수집.", "'Back to the Den' — 뱀프스터 전원 보금자리로.", "'Back in Place' — 플라스틱 의자 전부 반납.", "'Fishing Pro' — 물고기 22종 수족관 컬렉션."])
A("moonlight-peaks/museum", "ko", 4, items=[["박물관 퀘스트는?", "Jada(유물 수집가). Persephone 스토리로 해금."],["전시실은 몇 개?", "5개: 크리터즈, 신, 파밍, 초자연, 아쿠아리움."],["신의 방에는?", "4점: Death 호감도 MAX Death's Tomb, 달의 여신·태양신·Llemi 호감도 MAX Chakra Tuner / Sun God's Halo / Llemi's Bow."],["뭘 기증?", "물고기(수족관), 꽃, 유물, 소울 블롭 등."],["100%에 필수?", "네 — 'One Collection to Rule Them All'에 필수."]])
A("moonlight-peaks/museum", "fr", 1, heading="Les cinq salles d'exposition", items=["Salle des créatures (Critters) — petites créatures.","Salle divine (Deity) — artefacts des dieux (voir tableau).","Salle agricole (Farming) — collection agricole (Amanita, été/automne).","Salle du surnaturel (Supernatural) — reliques surnaturelles.","Salle de l'aquarium (Aquarium) — poissons (les 22 pour 'Fishing Pro')."])
A("moonlight-peaks/museum", "fr", 2, heading='Artefacts de la salle divine (4)', headers=["Artefact", "Comment l'obtenir"])
A("moonlight-peaks/museum", "fr", 3, heading='Complétion & succès', items=["'Archaeo-Logistics' — ouvrir le musée.", "'One Collection to Rule Them All' — compléter le musée.", "'Skulls in a Net' — tous les Soul Blobs.", "'Back to the Den' — tous les Vampsters.", "'Back in Place' — toutes les chaises en plastique.", "'Fishing Pro' — les 22 poissons pour l'aquarium."])
A("moonlight-peaks/museum", "fr", 4, items=[["Qui dirige la quête ?","Jada, la collectionneuse (avec l'histoire de Persephone)."],["Combien de salles ?","5 : créatures, divine, agricole, surnaturel et aquarium."],["Salle divine ?","4 artefacts : Death's Tomb (amitié max avec Death), Chakra Tuner (déesse lunaire), Sun God's Halo (dieu soleil), Llemi's Bow (Llemi)."],["Quoi donner ?","Poissons (aquarium), fleurs, artefacts, Soul Blobs."],["Nécessaire pour 100 % ?","Oui — requis pour 'One Collection to Rule Them All'."]])
A("moonlight-peaks/museum", "de", 1, heading='Die fünf Ausstellungsräume', items=["Kreaturen-Raum (Critters) — kleine Kreaturen.","Götterraum (Deity) — göttliche Artefakte (siehe Tabelle).","Landwirtschaftsraum (Farming) — Farm-Sammelstücke (Amanita, Sommer/Herbst).","Übernatürlicher Raum (Supernatural) — Relikte.","Aquarienraum (Aquarium) — Fischsammlung (alle 22 für 'Fishing Pro')."])
A("moonlight-peaks/museum", "de", 2, heading='Artefakte des Götterraums (4)', headers=["Artefakt", "So erhältst du es"])
A("moonlight-peaks/museum", "de", 3, heading='Abschluss & Erfolge', items=["'Archaeo-Logistics' — Museum öffnen.", "'One Collection to Rule Them All' — Museum vervollständigen.", "'Skulls in a Net' — alle Soul Blobs.", "'Back to the Den' — alle Vampster.", "'Back in Place' — alle Plastikstühle.", "'Fishing Pro' — alle 22 Fische für das Aquarium."])
A("moonlight-peaks/museum", "de", 4, items=[["Wer führt die Quest?", "Jada, die Sammlerin (mit Persephones Story)."],["Wie viele Räume?", "5: Kreaturen, Götter, Landwirtschaft, Übernatürliches, Aquarium."],["Götterraum?", "4 Artefakte: Death's Tomb (max. Freundschaft mit Death), Chakra Tuner (Mondgöttin), Sun God's Halo (Sonnengott), Llemi's Bow (Llemi)."],["Was spenden?", "Fische (Aquarium), Blumen, Artefakte, Soul Blobs."],["Für 100 % nötig?", "Ja — für 'One Collection to Rule Them All'."]])

# updates: FAQ（1.1.45 / 1.1.44 版本）
A("moonlight-peaks/updates", "zh-CN", 2, items=[["1.1.45 修了什么？","起播光敏警告、观星宽屏黑条、Loveage 礼物交换软锁、Luna 商店动物消失（南瓜头心事件后）、“Back to the Den”成就补发、Recover the Moon 逃课、蜜蜂屋/萤火虫圣所内存泄漏，以及鼠标/农场助手/捡拾性能——1.2 还有更多改进。"],["1.1.44 修了什么？","刺绣桌不可见、升级房屋后无法加载、树苗全年可种且季节显示正确、桌面/架装饰不占库存、雨天晚上作物不生长、保存时退出损坏存档（仅 Steam）。"],["1.1.41 修了什么？","加载时间、全地块储物（含谷仓/温室）、刺绣提前、树苗显示结果季节，以及 23+ 项修复。"],["主机版有补丁吗？","有——主机补丁跟随 Steam 版发布（据 NintendoReporters）。"],["官方说明在哪看？","Steam app 2209900 的新闻中心；本站汇总已核实的补丁说明。"]])
A("moonlight-peaks/updates", "ja", 2, items=[["1.1.45 の修正は？","起動時の光過敏警告、Star Gazing の黒帯、Loveage Gift Exchange のソフトロック、Pumpkin Head のハートイベント後の動物消失、「Back to the Den」の遡及解除、Recover the Moon の逃げ道、Bee House/Firefly Sanctuary のメモリリーク、マウス・ファームヘルパー・拾い性能。1.2 でさらなる改善予定。"],["1.1.44 の修正は？","刺繍テーブル非表示、家のアップグレード後のロード不能、苗木の全季節植え付けと季節表示、テーブル・棚の装飾がインベントリを消費しない、雨の夜の作物成長、保存中の終了によるセーブ破損（Steamのみ）。"],["1.1.41 の修正は？","ロード時間、敷地全体の収納（納屋・温室含む）、刺繍の早期解放、季節表示、23以上のバグ。"],["コンソール版のパッチは？","あります——Steam 版に追随（NintendoReporters より）。"],["公式ノートは？","Steam の app 2209900 ニュース。ここに検証済みを要約。"]])
A("moonlight-peaks/updates", "ko", 2, items=[["1.1.45 수정?", "시작 시 광과민 경고, 별자리 관측 검은띠, Loveage 선물 교환 소프트록, Pumpkin Head 하트 이벤트 후 동물 소멸, 'Back to the Den' 소급 해금, Recover the Moon 탈출, Bee House/Firefly Sanctuary 메모리 누수, 마우스·농장 헬퍼·줍기 성능. 1.2에서 추가 개선."],["1.1.44 수정?", "자수 테이블 비표시, 집 업그레이드 후 로드 불가, 묘목 전 계절 심기·계절 표시, 테이블·선반 장식이 인벤토리 차지 안 함, 비 오는 밤 작물 성장, 저장 중 종료로 세이브 손상(Steam 전용)."],["1.1.41 수정?", "로딩 시간, 부지 전체 창고(헛간·온실), 자수 조기 해금, 계절 표시, 23개 이상 버그."],["콘솔 패치?", "네 — Steam 버전에 이어 제공(NintendoReporters)."],["공식 노트?", "Steam app 2209900 뉴스. 여기에 검증된 내용을 요약."]])
A("moonlight-peaks/updates", "fr", 2, items=[["Que corrige 1.1.45 ?","Avertissement de photosensibilité, Star Gazing en écran large, soft lock Loveage, animaux disparus chez Luna, 'Back to the Den' rétroactif, Recover the Moon, fuites mémoire Bee House/Firefly Sanctuary, performances souris/ferme/ramassage. Plus en 1.2."],["Que corrige 1.1.44 ?","Table de broderie invisible, chargement après upgrade de maison, pousses plantables toute l'année, décorations sans slot d'inventaire, cultures les nuits de pluie, sauvegarde corrompue (Steam uniquement)."],["Que corrige 1.1.41 ?","Chargement, stockage sur tout le terrain, broderie plus tôt, saisons, 23+ correctifs."],["Patchs consoles ?","Oui — ils suivent Steam (NintendoReporters)."],["Notes officielles ?","Hub Steam app 2209900 ; résumé vérifié ici."]])
A("moonlight-peaks/updates", "de", 2, items=[["Was fixte 1.1.45?","Fotosensibilitäts-Warnung, Star-Gazing-Balken, Loveage-Softlock, verschwundene Tiere, 'Back to the Den' nachträglich, Recover the Moon, Speicherlecks, Maus/Farmhelfer/Aufsammeln-Performance. Mehr in 1.2."],["Was fixte 1.1.44?","Unsichtbarer Sticktisch, Laden nach Haus-Upgrade, Setzlinge ganzjährig, Dekoration ohne Inventarslots, Pflanzenfix an Regennächten, Speicherfehler (nur Steam)."],["Was fixte 1.1.41?","Ladezeiten, Lager auf dem Grundstück, Stickerei früher, Jahreszeiten, 23+ Fixes."],["Konsolen-Patches?", "Ja — sie folgen Steam (NintendoReporters)."],["Offizielle Notizen?", "Steam-Hub app 2209900; hier zusammengefasst."]])

# 写出 EXTRA
EXTRA = {}
for slug, lang, idx, kw in R:
    EXTRA.setdefault(slug, {}).setdefault(lang, {})[idx] = kw

out = "# -*- coding: utf-8 -*-\n\"\"\"Moonlight Peaks 补充翻译：FAQ / 笔记 section（程序生成，勿手改）。\"\"\"\nEXTRA = "
out += repr(EXTRA)
out += "\n"
Path(__file__).parent.joinpath("moonlight_i18n_extra.py").write_text(out, encoding="utf8")
print("generated moonlight_i18n_extra.py with", len(EXTRA), "pages")


# =====================================================================
