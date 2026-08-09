# Sovereign Tower（君王之塔）攻略站 · 设计方案（G2 · 2026-08-09 v1）

> 主词：Sovereign Tower（Steam 圆桌管理 RPG / 2026-08-06 发售 / Curve Games 发行 / Metacritic 86）
> 验证：docs/20 G1（40/55 ✅ 主推，CEO 批准）→ **本方案待用户批准（G2 ⛔ 关卡点）**
> 方法论：skill `hot-word-game-site`（design.md 模板 + standards.md 四标准 + ui-ux-pro-max / emil-design-eng）
> 页面矩阵：docs/23（62 页 × 7 语；V1 首发 18 页 P0）

---

## 0. 对标结论（对手做到 X / 没做到 Y → 我们做 Z）

| 对手 | 做到 | 没做到 | 我们怎么做 |
|---|---|---|---|
| raiderking.com（最深） | 24 骑士全表、属性/好感/菜谱/XP 全机制 | 一页塞 24 骑士、无筛选排序、无成就/剧情页、单语 | 每骑士一档案卡 + 筛选器 + 菜谱对照表 + 成就/剧情全做 |
| bonus-action.com | 招募条件（Act 容量 6/8/10）、Angelica 浪漫 | 菜谱页标题党（正文无数据）、无成就/剧情 | 完整 6 菜 × 24 骑士对照表（真数据）+ 浪漫线深页 |
| tposegaming.com | 谋杀攻略结构教科书（Quick Answer→表→反例→bug） | 只此一主题 | 按此结构做每个 How-to 事件页 + 决策表 + 跨周目变化 |
| intoindiegames.com | Cycle 1-5 walkthrough 分页 | 单线视角、无分支数值表 | Cycle 决策表（3 选项数值/势力影响/结局）+ 势力追踪 |
| kosguides.com | 单成就深挖（How Cute） | 75 成就全表/roadmap 空白 | 75 全表 + 路线图（难度/时长/missable/glitched，对齐 PowerPyx） |
| powerpyx.com（头部） | 成就路线图 + 专题深页拆分 + 站内搜索 | 只做 3A/主机大作，indie 空白 | 结构照搬，但全 7 语 + 骑士/菜谱数据页（它没有） |
| genshin-builds.com（设计标杆） | 数据卡片质感（角色数据库/卡池倒计时/生日） | 无文字攻略、无 i18n | 数据卡质感 + 完整攻略文字 + 7 语 |
| 18183 / pc6（中文） | 全骑士加入浅文 / 4 骑士零散档案 | 无数值/无成就/无菜谱/无好感 | 中文（zh-CN/zh-TW）全量深表 = 真空补位 |

**差异化五条（全部可指向流量/体验）**：① 7 语 i18n（竞品全单语 0 hreflang）② 查表型数据页（骑士/菜谱/成就 = 长尾）③ 分支决策表（AI 一句话答不完）④ 中文深表真空 ⑤ 数据卡质感 vs WordPress 白底。

---

## 1. 站点主题概念

**「圆桌御书房 · 宫廷敕令」**——这个站扮演「新君登基后的御书房」：每篇攻略是一道**敕令**，每个骑士是一份**廷臣档案**，每道菜是**御膳房菜单**，每个成就是**功勋簿**，每条剧情线是**编年史**。

推导理由：
- 游戏气质 = 你是 Sovereign，坐圆桌、听政、派骑士、回溯时间改写命运 → 玩家需要的是「君主治国的手册」
- 目标玩家情绪 = 想当好君主、怕做错决策、想追全骑士/浪漫/成就 → 「御书房档案」比「攻略列表」更贴合
- 竞品全是 WordPress 白底文章流 → 我们用「羊皮纸 + 深绯红 + 金箔 + 纹章蜡印」做出宫廷感，一眼不像工厂货

---

## 2. 视觉语言（ui-ux-pro-max + emil-design-eng 落地）

### 2.1 风格基准（ui-ux-pro-max 实测结论）
- **Academia（Scholarly）**：mahogany #1C1714 / oak #251E19 / parchment #E8DFD4 / brass #C9A962 / crimson #8B2635，罗马数字标题、首字下沉、拱顶 hero、蜡印、vignette
- 辅以「Brewery/Winery 皇家配色」：深酒红 #7C2D12 + 工艺金（WCAG 3:1 调整后）
- **禁止**：现代科技感（霓虹/玻璃拟态/等宽数据终端——那是第 4 站），纯 sans 正文

### 2.2 配色 Token
| Token | 色值 | 用途 |
|---|---|---|
| --parchment | #E8DFD4 | 背景羊皮纸 |
| --parchment-deep | #D9CDB8 | 卡片/区块底 |
| --ink | #2B2320 | 正文墨色 |
| --mahogany | #1C1714 | 深底（footer/hero 暗区） |
| --oak | #251E19 | 深卡片 |
| --crimson | #8B2635 | 主强调（纹章/蜡印/重点） |
| --gold | #C9A962 | 金箔（饰线/图标/hover） |
| --brass-dim | #9C8B7A | 次级文字/淡化 |
| --border | #4A3F35 | 边界 |

### 2.3 字体（ui-ux-pro-max Academia 推荐）
- 标题：**Cormorant Garamond**（优雅衬线，宫廷感）
- 正文：**Crimson Pro**（衬线易读，无 UI sans-serif）
- 标签/眉题/罗马数字：**Cinzel**（铭刻感，overlines、章节号、纹章文字）
- 全衬线 = 与四站（像素/无衬线/手写体/等宽）彻底区分

### 2.4 图标语言
- SVG 原生纹章元素：盾徽、剑、狮鹫、王冠、蜡烛、卷轴、酒杯、鹰——**禁 emoji 当图标**（ui-ux-pro-max 硬规则）
- 每类页面配专属纹章：骑士=盾徽、菜谱=酒杯+餐刀、成就=桂冠、剧情=卷轴、FAQ=询问印

### 2.5 组件形态（隐喻命名，≥6 独特组件）
| 组件 | 隐喻名 | 形态 |
|---|---|---|
| 骑士档案卡 | **廷臣档案卡 court-card** | 羊皮纸卡 + 左上蜡印角 + 6 属性徽章横排 + 最爱菜纹章章 + 浪漫线旗标 |
| 按钮 | **敕令蜡印 edict-seal** | 圆形蜡印钮（crimson 底 + gold 纹章字），hover 印章下压 |
| 章节标题 | **纹章横栏 herald-banner** | 中央 crest + 双侧金饰线 + Cinzel 眉题 |
| 目录 | **卷轴目录 scroll-toc** | 左侧细栏羊皮纸 TOC，罗马数字序号，当前章 gold 高亮 |
| 菜谱表 | **御膳对照 feasting-table** | 6 菜 × 24 骑士交叉矩阵，悬停行 gold 高亮 |
| 成就 | **功勋簿 ledger-row** | 成就行 + 已获得=金蜡印/未获得=灰蜡印，隐藏成就=蜡封遮罩 |
| 剧情 | **编年史 chronicle-timeline** | 竖向卷轴时间线 + Cycle 敕令节点 + 决策分支卡（含数值） |
| 首页特色 | **今日廷议 council-card** | 每日一条游戏趣味事实/事件卡（回访驱动） |

### 2.6 动效原则（emil-design-eng）
- 过渡 150-300ms、`ease-out`；按钮 `:active` scale(0.97)；hover = 金箔高亮 + 纹章微动（transform，不 animating width/height）
- Academia 风格 = 缓慢仪式感（Easing.out poly(4)），禁 spring 弹跳（宫廷不是街机）
- 键盘触发不动画；`prefers-reduced-motion` 全关；focus-visible 金环
- **禁装饰性假交互**：筛选/对照/廷议都做真数据切换（JS 改 data-active + 过滤数组），一测就穿帮的 tab 不做

---

## 3. 信息架构

### 3.1 首页骨架「王座厅门廊」
```
[纹章横栏导航] 王冠logo · 骑士名册 · 御膳房 · 功勋簿 · 编年史 · 攻略总纲 · 🌐语言
[拱顶 hero 门廊] 左：游戏名大标题(Cormorant) + 金色饰线 + 一句话
               右：数据铭牌柱（546 评 / 86 分 / 75 成就 / 7 语 / 08-06 发售）—— 王座两侧旗帜式
[今日廷议] 每日一张 council-card（趣味事实/当日事件）
[四道敕令入口] 骑士名册 / 御膳对照 / 功勋簿 / 编年史（2 列横向条卡 + 蜡印序号）
[FAQ 敕令问答] 手风琴（FAQ schema）
```
- hero 形态 = **拱顶门廊**（arch-top，Academia archTopRadius；区别于 Meccha 居中灯牌/KTS 满版墙/Doloc 全景横幅/ApproxUp 控制台）
- 攻略区布局 = **2 列横向条卡**（图标+标题+描述横排+左色条+蜡印序号），非 4 列方块

### 3.2 内页骨架「敕令正文」
```
[纹章横栏导航]
[左卷轴目录 scroll-toc]（细栏，罗马数字章节，当前 gold 高亮，移动端折叠）
[右敕令正文]
  章节眉题 herald-banner → 正文（Crimson Pro，首字下沉 drop cap）
  数据表/决策卡（每页 ≥2 种富组件）
  怎么做/怎么避免块 + Common Mistakes（五段式）
[底部「下一道敕令」递进条]
```
- 内页结构 = 左卷轴目录 + 右敕令正文 + 底部续章递进（区别于四站：Meccha 单栏无侧栏 / KTS 左证据栏 / Doloc 手册+进度 / ApproxUp dossier 双栏）

### 3.3 页面矩阵（完整见 docs/23，62 页 × 7 语；V1 首发 P0 = 18 页）
V1 P0：首页 + 5 导航页（knights/guides/achievements/romance/cooking）+ all-knights + favorite-meals + how-to-recruit + romance-guide + affinity + achievements-list + how-to-play + quests + murder + cycle-1 + system-requirements + faq
P1 分批：24 骑士单页、achievements/roadmap、dragon-knight、endings、各 cycle、dishes、tier-list、console-release、multiplayer、how-long-to-beat、controls、steam-deck

---

## 4. 语言集

- Steam 官方 6 语：en / fr / de / ja / ko / zh-CN → **全量 6 语** + **zh-TW（OpenCC 转换）** = **7 语**
- 每页 `sources[].labels[lang]` 输出对应语言来源名；zh-TW 走 OpenCC，禁止 generator 回退英文混排（P0 坑，grep `lang==="zh"` 校验）
- 竞品全单语（0 hreflang）→ 7 语 hreflang = Google 多语言索引直接增量
- 优先级：en 核心 + zh-CN/zh-TW（中文深表真空）+ ja/ko + fr/de

---

## 5. 内容策略

- **唯一事实来源**：docs/sovereign-tower-research.md（8 大块，全 L0-L4 标注）；未核实标「待补」（完整 75 成就表/骑士余项/DLC/社区讨论）
- **每页结构（头部站逻辑五段式）**：机制怎么运作 → 步骤级流程 → 决策/影响 → 常见错误 → 进阶技巧；答案页（系统需求/controls/faq）150-220 词 + 数据表 + FAQ schema 即合格，不注水
- **硬数据页**：system-requirements / controls / round-table / faq —— 数据表 + FAQ schema
- **深表页**：favorite-meals（6 菜 × 24 骑士真数据）/ all-knights（24 档案卡 + 筛选）/ achievements-list（75 全表）
- **标题 ≤60 字符**（CJK 按宽字符截断）；FAQ schema 全站答案页
- **每页 1-2 个 L0 来源**；引用 raiderking 数据时二次核验（本知识库已逐条摘录）

---

## 6. 配图清单（Seedream 统一风格）

- **统一风格 prompt 模板**：`Medieval illuminated manuscript illustration, deep crimson and gold leaf on aged parchment, heraldic crest, wax seal, soft candlelight, ornate gold filigree border, no text, 16:9`
- 比例：hero 16:9 三档 srcset（1920/1280/640）；卡片 4:3 或 1:1
- 清单：hero 王座厅 ×1；每 P0 页主题图（骑士名册/御膳/功勋/编年史/谋杀/龙骑士/好感/招募）× 14；今日廷议占位纹章 ×1
- 禁：现代霓虹/玻璃拟态/写实照片人物脸

---

## 7. 执行顺序

1. G3 建站：site-kit 脚手架换主题 → 全量重写 style.css（宫廷羊皮纸）+ generate.js（纹章导航/廷臣卡/御膳表/功勋簿组件）→ 数据驱动 18 P0 页 × 7 语 → 7 语纯净校验（grep + curl 原始 HTML）
2. G4 双视角全维审计：用户视角（宫廷感/导航/移动端 375px/语言切换/交互实测）+ 开发者视角（schema/sitemap/hreflang/LCP/死链/合规）
3. G5 部署：GitHub 建仓 → Cloudflare Pages + 域名 `sovereign-towerguides.com`（L0 可用）→ GSC + GA4 独立资源
4. G6 数据复盘：D3/D7/D14 GSC 查询 + GA4 organic；有词上榜→补 P1 深页；无数据→换词
5. 周更保鲜：update-log / 今日廷议 每日真实内容变更

---

## 8. 流量判断（为什么能拿流量）

1. **差异化长尾**：骑士档案/菜谱对照/成就全表/分支决策 = 竞品 4 小站全没做深（raiderking 一页塞、bonus-action 无数据、kosguides 单成就）
2. **行为信号**：75 成就 + 谋杀分支（72.3% 达成率 = 大量玩家卡在这）+ 24 骑士查表需求 = AI 一句话答不完的页面
3. **语言覆盖**：7 语（竞品单语）→ Google 多语言索引增量，尤其中文深表真空（18183/pc6 只有浅文）
4. **设计质感**：数据卡 + 宫廷卷宗 vs WordPress 白底 = 停留/复访（今日廷议每日卡）
5. **风险护栏**：主词不硬碰（已有 4 小站），靠长尾 + 多语言；域名新站信任期 3-9 个月，止损线 D14 无展示则换词（docs/09）

---

## 批准记录（⛔ G2 关卡点 · 待用户批准）
> 本方案（站点概念/视觉/骨架/页面矩阵/语言集/内容策略/配图/执行序/流量判断）已完整落盘。
> **批准 → 进 G3 建站；否 → 改方案不改代码。**
