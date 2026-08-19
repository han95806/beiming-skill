# 证据台账

| 证据编号 | 时间/顺序 | 来源类型 | 页面/位置 | 原文或可见对象 | Agent | 操作/状态变化 | 截图 | 支持结论 | 等级 | 冲突/备注 |
|---|---|---|---|---|---|---|---|---|---|---|
| E-J-001 | 2026-08-19 / 01 | 营销首页 | https://www.seetarot.com/ | Ask → Shuffle → Reveal | 未命名解读职能 | 无状态修改 | S09 | 公开描述的核心体验为提问、洗牌、揭示三步 | 已确认 | 尚未在应用内复核 |
| E-J-002 | 2026-08-19 / 02 | 样例解读 | 首页 The Star 样例弹窗 | 牌名与正逆位、意象描述、情境化解读、反思问题 | 未命名解读职能 | 打开预置样例 | — | 可见输出结构至少包含四类内容 | 已确认 | 样例不等于实时生成结果 |
| E-J-003 | 2026-08-19 / 03 | FAQ | 首页 FAQ | 免费层可实际使用；付费层包含复杂牌阵、每日抽牌和跨解读记忆 | — | 无状态修改 | — | 公开商业模式与付费能力边界 | 已确认 | 属官方声明，真实价格和付费门未知 |
| E-J-004 | 2026-08-19 / 04 | FAQ/首页 | 首页 FAQ 与 Why AI tarot | 问题和解读不用于训练；重复用户的解读会记忆 | — | 无状态修改 | — | 隐私与长期记忆是核心价值主张 | 已确认 | 声明未由账户内行为复核 |
| E-J-005 | 2026-08-19 / 05 | 应用入口 | https://app.seetarot.com/ | Begin the practice / Enter the chamber | — | 无状态修改 | — | 使用核心产品前需注册或登录 | 已确认 | 未发现游客模式 |
| E-J-006 | 2026-08-19 / 06 | 注册页 | https://app.seetarot.com/sign-up | Querent、email、8 位以上密码 | — | 无状态修改 | — | 注册输入为昵称、邮箱、密码 | 已确认 | 未提交账户数据 |
| E-O-001 | 2026-08-19 / 07 | About | https://www.seetarot.com/about | AI tarot companion；不是预测或建议；仅面向美国居民 | — | 无状态修改 | — | 产品定位、非专业建议与地域范围 | 已确认 | 官方自述 |
| E-O-002 | 2026-08-19 / 08 | 营销站隐私政策 | https://www.seetarot.com/privacy | Vercel、GA4、Meta Pixel；应用有独立隐私政策 | — | 无状态修改 | — | 营销站技术供应商和数据收集范围 | 已确认 | 不代表应用内部技术栈；应用隐私政策尚未看到 |
| E-O-003 | 2026-08-19 / 09 | 营销站条款 | https://www.seetarot.com/terms | 营销站与应用是独立服务；样例不构成专业建议 | — | 无状态修改 | — | 站点与应用的法律边界 | 已确认 | 应用条款尚未看到 |
| E-J-007 | 2026-08-19 / 10 | Oracle 步骤 1 | https://app.seetarot.com/oracle | General、Love、Career、Finances、As Feeling、As Action、Yes & No | 编排职能 | 选择 General | S02 | 第一步将问题分类为七种意图 | 已确认 | 未验证其他意图的差异 |
| E-J-008 | 2026-08-19 / 11 | Oracle 步骤 2 | 同上 | Single、Three、Celtic Cross（Coming Soon） | 编排职能 | 选择 Three | S03 | 第二步选择牌阵；三牌语义为 Past / Present / Possible | 已确认 | 未出现价格或锁标识 |
| E-J-009 | 2026-08-19 / 12 | Oracle 步骤 3 | 同上 | 问题最多 500 字；至少 10 字；鼓励开放问题 | 编排职能 | 提交非敏感测试问题 | S04 | 问题输入存在长度和表达引导 | 已确认 | 未测试错误分支 |
| E-J-010 | 2026-08-19 / 13 | 抽牌页面 | 同上 | 19 张牌背；Choose 3；用户主动选牌 | 抽牌/编排职能 | 选择第 4、9、15 张 | — | 系统保留用户选择仪式，不自动代抽 | 已确认 | 随机化算法未知 |
| E-J-011 | 2026-08-19 / 14 | 揭示页面 | 同上 | Past / Present / Possible 逐张翻开 | 解读职能 | 依次揭示三张牌 | S06 | 第三张揭示后出现完整解读 | 已确认 | 生成是在选牌后还是揭示时开始未知 |
| E-A-001 | 2026-08-19 / 15 | AI 解读结果 | 同上 | Direct word、三位置解读、反思问题 | 解读职能 Agent | 生成完成 | S07 | 可观察输出契约及统一叙事语气 | 已确认 | 模型、Prompt 与工具名未知 |
| E-A-002 | 2026-08-19 / 16 | AI 解读结果 | 同上 | 结果引用账户画像中的星座信息 | 解读职能 Agent | 读取个人资料上下文 | S07 | 解读会融合可选出生日期推导的星座上下文 | 合理推断 | 不在报告保留用户具体资料值 |
| E-J-012 | 2026-08-19 / 17 | 阅读详情 | `/reading/<id>` | 独立 URL、Share、Reflections、0/2000、Inscribe | 阅读/日志服务 | 未分享、未写反思 | S06/S07 | 解读自动持久化，支持分享与反思日志 | 已确认 | 分享和写入未执行 |
| E-J-013 | 2026-08-19 / 18 | History | https://app.seetarot.com/history | Oracle 与 Daily 两条记录，含牌阵、意图、摘要、时间 | 历史服务 | 读取历史 | S05 | Oracle 结果已自动写入历史 | 已确认 | 未见筛选、搜索或单条删除 |
| E-J-014 | 2026-08-19 / 19 | Daily 与 History | `/daily`、`/history` | Daily 持续显示 deck is turning；History 已有 Daily 结果 | Daily/历史服务 | 两页面交叉核对 | S01/S05 | 页面状态与持久化结果冲突 | 已确认 | 可能是前端状态恢复或时区问题，原因未知 |
| E-J-015 | 2026-08-19 / 20 | 日期显示 | `/daily`、阅读详情、History | Daily 显示本地 8 月 19 日；详情/历史显示 8 月 18 日 | 日期/时区服务 | 同一会话交叉核对 | S01/S05/S06 | 同一批结果存在日期口径差异 | 已确认 | 可能使用本地时区与 UTC，后台实现未知 |
| E-A-003 | 2026-08-19 / 21 | Daily 阅读详情 | `/reading/<id>` | The card today、A reflection、A grounding practice | Daily 解读职能 | 读取已保存结果 | — | Daily 与 Oracle 使用不同输出模板 | 已确认 | Daily 创建触发点未知 |
| E-J-016 | 2026-08-19 / 22 | Profile | https://app.seetarot.com/profile | Display name、Timezone、Preferred intent、Birth date；账户永久删除入口 | 画像/账户服务 | 只读查看标签 | — | 画像字段服务于称呼、每日时间、默认语境与星座织入 | 已确认 | 未修改、未删除 |
| E-R-001 | 2026-08-19 / 23 | App 页脚与营销政策 | app footer → seetarot.com/privacy | 应用链接到营销站政策；政策声明只覆盖营销站、应用另有政策 | 治理层 | 交叉核对 | — | 当前可见隐私入口存在覆盖范围缺口 | 已确认 | 是否有未暴露的应用政策未知 |
| E-J-017 | 2026-08-19 / 24 | Profile/账户菜单 | https://app.seetarot.com/profile | “The full deck is yours. Draw as often as the moment asks.”；无 Upgrade/Billing/Plan/Price 入口 | 账户/商业化 | 只读查看 | — | 当前账户界面未呈现商业化门 | 已确认 | 不证明产品永远免费；FAQ 描述未来付费层 |
