# 证据台账

| 证据编号 | 时间/顺序 | 来源类型 | 页面/位置 | 原文或可见对象 | Agent | 操作/状态变化 | 截图 | 支持结论 | 等级 | 冲突/备注 |
|---|---|---|---|---|---|---|---|---|---|---|
| E-J-001 | 2026-08-19 / 01 | 首页表单 | `/` | `Create Games with AI`；1000 字；图片上传；模型选择；Create | 未出现 | 只读观察 | S01 | 用户可从自然语言或图片启动项目 | 已确认 | 未提交首页自由 Prompt |
| E-J-002 | 02 | 模板选择 | 首页 `pick a template` | City Builder、Interactive Story、Voxel World、Vampire Survivors、RPG、Multiplayer Obby；3 个 Coming Soon | 未出现 | 选择 Interactive Story | S03 | 模板提供类型化起点并区分可用/未开放 | 已确认 | 模板真实代码差异未知 |
| E-J-003 | 03 | 生成状态 | 模板 Step 3 | `Preparing your assets...`、0%、4 个 Asset 槽位，随后 `Review your assets` | 资产准备职能 | NEXT 后自动准备资产 | S04、S07 | 资产准备在最终建项前发生；4 个槽位独立呈现 | 已确认 | NEXT 即触发生成，缺少前置额度确认 |
| E-J-004 | 04 | 登录门 | `CREATE GAME` | `Sign in to Rosebud`；Google/Microsoft/Email；条款勾选 | Auth | 未登录点击建项被拦截；登录后出现 Account menu | S06 | 项目创建需要身份；公开 Play 不需要 | 已确认 | Google OAuth 在内置浏览器曾白屏，改用替代登录 |
| E-J-005 | 05 | 项目创建 | 首页模板 Step 3 | `Creating your game`、`Please wait while we set up your project...` | 项目初始化职能 | 创建后跳转稳定 `/edit/{uuid}` | S08 | 项目初始化是独立异步状态 | 已确认 | 进度和可取消性不可见 |
| E-J-006 | 06 | Chat 初始态 | `/edit/{uuid}` | Rosie 欢迎语、3 个建议、自由输入、截图/图片、模型框 | Rosie | 先 disabled/Getting ready，随后可输入 | S09、S12 | Chat 是编辑器主控制面，建议和自由 Prompt 共存 | 已确认 | 欢迎语与模板来源的生成规则未知 |
| E-J-007 | 07 | Preview | 编辑器 PREVIEW | 刷新、调试台、录制、全屏；初次黑屏，约 5 秒后出现可玩 UI | Runtime/Preview | 黑屏→统计/角色/对话/3 个选择 | S10、S10a | 预览有独立加载阶段，聊天完成不等于预览可用 | 已确认 | 黑屏期间无进度和错误原因 |
| E-J-008 | 08 | Assets | 编辑器 ASSETS | `assets`、搜索、上传、Create、4 items；background + failure/neutral/success | 资产管理职能 | 4 个 WebP 可见并有路径复制入口 | S11、S12 | 资产库是项目级稳定引用表面 | 已确认 | 上传、生成、覆盖、删除未执行 |
| E-J-009 | 09 | Code | 编辑器 CODE | Upgrade 锁；文件树 `scenes/Boot.js`、`Game.js`、`systems/DialogueSystem.js`、`agents.md`、`index.html`、`main.js`、`manifest.js` | Rosie/Code workspace | 点击后显示文件树但要求升级 | S13 | 项目由可浏览文件组成；代码访问受方案控制 | 已确认 | 免费层 DOM 可见但实际编辑被锁；不代表已读取全部代码 |
| E-A-001 | 10 | 项目指南 | Code 中 `agents.md` 可见片段 | 不建议替换/再生成视觉资产；建议聚焦玩法、故事、UI/UX、平衡、功能、代码型 polish | Rosie | 未修改 | S13 | 项目级指导文件约束后续建议 | 已确认 | 只见部分内容；不是官方系统 Prompt |
| E-J-010 | 11 | 项目设置 | 项目名下拉 | Name、Description、Preview Image、Remixed From、Remix Enabled、Creator Tips、Save | 项目元数据职能 | 只读打开，未保存 | S14 | Remix 血缘和创作者变现进入项目元数据 | 已确认 | 权限与商业条款未执行 |
| E-J-011 | 12 | 版本历史 | View version history | `Initial import`、Current、Restore disabled | Versioning | 初始建项后存在基线版本 | S15 | 项目支持版本视图和恢复入口 | 已确认 | 恢复语义、冲突与资产回滚未知 |
| E-P-001 | 13 | 用户输入 | Chat Prompt | `Add a small header... Choose your approach... Keep ... unchanged.` | Rosie | 提交 1 次修改 | S16 | 输入契约可包含局部变更与不变约束 | 已确认 | 仅测试一次英文 Prompt |
| E-A-002 | 14 | 工作日志 | Rosie execution | Listed `/`；Read `/index.html`、`/scenes/Game.js`、`/main.js`；Edited `/index.html` 两次 | Rosie | 读→定位→编辑 | S17、S20 | Rosie 具备项目浏览、读取和定点编辑的可观察工具链 | 已确认 | 页面动作名不等于真实底层 API |
| E-A-003 | 15 | 校验结果 | Rosie work log | `Project validation passed` | Rosie/Validator | 编辑后执行校验 | S20 | 修改链路含显式验证门 | 已确认 | 测试项、覆盖率和失败处理未知 |
| E-J-012 | 16 | 完成回复 | Chat | `Added the small “Choose your approach” header...`；4 个 Next moves | Rosie | 工具完成→摘要→下一步建议 | S18、S20 | 完成输出含变更摘要、建议和额度 | 已确认 | 下一步建议未执行 |
| E-J-013 | 17 | 额度 | Chat 完成卡片 | `Credits used: 500` | Billing | 单次小改动显示结算 500 credits | S18、S22 | 额度结果在每次 Agent 回合后可见 | 已确认 | 预估、冻结、余额、退款与计算公式未知 |
| E-J-014 | 18 | 预览验证 | Preview iframe | `Choose your approach` 出现在 3 个选择上方 | Runtime/Preview | Loading latest changes→可见新标题 | S19、S19a | Agent 回复后还需等待预览刷新才能证明资产可用 | 已确认 | 完成回复早于预览稳定完成 |
| E-J-015 | 19 | 状态冲突 | 修改前后 Preview | Stats/DC 在重载后变化；画面和对话保持 | Runtime | 预览重新初始化 | S10a、S19a | “保持 stats 不变”不能仅凭单次运行验证 | 已确认冲突 | 可能是运行时随机值，不能归因于 Rosie 改动 |
| E-J-016 | 20 | 版本历史 | 修改后 History | 新条目 `Turn the Tavern Prototype into a Glam-Fee Showdown` + `Initial import` | Versioning | 修改自动产生当前版本 | S21 | Agent 回合与版本记录关联 | 已确认 | 标题与实际小改动不一致，命名规则未知 |
| E-A-004 | 21 | 模型选择 | Chat model combobox | rosie、claude-sonnet、claude-opus、gemini-pro/flash、gpt-terra/sol、gpt-5.6-luna、grok-4.5 | Model Router | 只展开，不切换 | S25 | 用户可显式选择多个模型/路由档位 | 已确认 | 型号展示不证明后台始终调用对应模型 |
| E-J-017 | 22 | 模型额度提示 | Rosie tooltip | `Usually uses ~6,000 credits (varies by complexity)` | Model Router/Billing | 只读 | S25 | 模型选择同时暴露典型成本预估 | 已确认 | 与本次实际 500 credits 有明显差异，但文案允许按复杂度变化 |
| E-J-018 | 23 | Publish | Publish dialog | `Not published`；预期 URL `/play/interactive-story-barbie-62`；最终 Publish 按钮 | Publishing | 只打开表单，未提交 | S23 | 发布前存在明确确认门和目标 URL | 已确认 | 未验证发布构建、失败、回滚和更新 |
| E-J-019 | 24 | Share | Share dialog | `Publish your project first to get a shareable link.` | Sharing | 只打开，未发布 | S24 | 分享依赖发布完成 | 已确认 | 私密协作分享入口未见 |
| E-J-020 | 25 | Play 广场 | `/play` | New/Featured/Popular；24+ 分类；游戏卡含播放和点赞数字 | Discovery | 只读浏览 | S02 | 产品同时提供内容分发和社区发现面 | 已确认 | 排序算法和指标口径未知 |
| E-J-021 | 26 | 公开成品页 | `/play/attention-passengers...` | iframe、全屏、Like、Comments、Remix、Tip、Share、作者、plays、remixes、标签、推荐 | Runtime/Community | 只读观察 | S05 | 发布结果进入可玩、社交、Remix 和推荐闭环 | 已确认 | 未点击 Remix/Tip/评论/分享 |
| E-O-001 | 官方资料 | 官方界面指南 | `lab.rosebud.ai/blog/rosebud-ai-interface-guide` | Prompt→Publish→Play；Chat/Code/Assets；发布可分享链接 | 官方声明 | 只读 | — | 佐证编辑器功能域 | 已确认（声明） | 当前实测显示 Code 受升级门限制 |
| E-O-002 | 官方资料 | Beginner Guide | `lab.rosebud.ai/blog/beginner-guide` | Rosie 写并应用代码；截图附着；建议下一步；下载代码 Pro+；Publish/Remix/My Projects | 官方声明 | 只读 | — | 补足编辑器与商业边界 | 已确认（声明） | 不自动证明本次任务实际执行 |
| E-O-003 | 官方资料 | 免费游戏制作页 | `rosebud.ai/make-your-own-game-online` | Chat 左侧、游戏右侧、代码自动应用、浏览器运行 | 官方声明 | 只读 | — | 支持双栏即时反馈定位 | 已确认（声明） | 营销描述不等于延迟/成功率保证 |
| E-O-004 | 官方资料 | Pricing FAQ | `rosebud.ai/blog/pricing-subscription-faqs` | 免费周额度；付费商业权；取消后项目和链接保留 | 官方声明 | 只读 | — | 佐证额度/方案/商业化 | 已确认（声明） | 价格和权益可能更新，以产品内为准 |
| E-R-001 | 架构归纳 | 五条流对齐 | Chat→工具日志→文件→Validation→Preview→Version→Publish gate | 语义架构 | 证据归纳 | S12、S20、S21、S23 | Rosebud 是 AI 编码编排器 + 文件工作区 + 浏览器运行时 + 版本/分发系统 | 合理推断 | 不代表官方服务拆分 |
| E-R-002 | To-Be | 状态设计 | 建议统一 Agent run、文件版本、预览 build、validation、credit settlement | — | 设计建议 | — | 降低“回复完成但预览未稳定”冲突 | 建议设计 | 非现有实现声明 |
