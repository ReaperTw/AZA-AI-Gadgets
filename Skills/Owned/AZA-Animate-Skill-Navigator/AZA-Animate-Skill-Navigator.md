最近用 Opus 和 Astra 写了不少 UI，发现一个避免 AI slop 并且让界面更好看的秘诀： 在 AGENTS.md 里加上 “Avoid unnecessary secondary labels and descriptions. Let the layout do the explaining.”

https://x.com/lemomo_ai/status/2113195080517562646
"Lemo-Opuscar 史诗级更新：8种新风格+新改编玩法，我把风格库变成了风格制作工具箱

Hello 大家好，我是lemomo。这次 Lemo-Opuscar 迎来了上线以来最大的一次更新，不光有新的风格，还有新的玩法，整个项目定位从【视频风格库】变成【搭建自己风格库的工具】。

1. 新增【剪辑与纪实】8 种风格，目前从最早的39种已经更新到了59种。未来会继续更新，我的目标是99种。
    
2. 新玩法：把风格改成你自己的。 新增的玩法，现在除了可以从库里选择风格开始创建影片外，库里任何一种风格都能改，也可以从空白开始。
    
3. 预告： Lemo Studio 工作台 (Claude App 桌面版），还有下一批日系动漫风格预告。
    

已经装过的朋友，记得先更新。还没安装的朋友，请给我点点star，求转发！

# 

全新 8 种新风格：剪辑与纪实

这次新增的 8 种风格有一个共同点：不在依赖代码作画，而是用真实素材剪出来的。 真实的影像、照片、文件、数据，按某一种剪辑和包装的语法排好，再配上声音。所以它们特别适合做自媒体、做新闻、做纪实的朋友。

而且这次的风格不光用opus可以做，sonnet 5.5 High档位的效果也很不错，我每一个片子都会把用Sonnet测试时候的片子放上去给大家看对比。

制作完成之后别忘了根据自己的需求对片子质量进行调整排版，也可以选择性的加入片头片尾之类的内容哦。

每一种都配了一支样片，请看一下 demo：

## 

1. 字幕新闻 Caption News

![](https://pbs.twimg.com/amplify_video_thumb/2112814293733580800/img/Ra5Se-Qpf9OEF6eP.jpg)

关掉声音也能看懂的社交媒体新闻：超大字幕当主角，关键词压黄块，数字滚动跳出来，每个数字旁边都会滑进来源。 适合：热点快讯、数据类新闻、有一个反转的故事。

【Sonnet 5.5 测试样片】

0:00 / 0:30

## 

2. 1920s 新闻影片 1920s Newsreel

0:00 / 0:55

上世纪 20 年代的有声新闻片：探照灯和地球的片头、转着飞到镜头前的报纸、语速飞快的播音员、爵士乐队卡着节拍剪。 适合：历史趣闻、老物件的流行史、复古味的品牌故事。

【Sonnet 5.5 测试样片】

![](https://pbs.twimg.com/amplify_video_thumb/2113062569741365248/img/6qmhCpchgJ9FAcF5.jpg)

## 

3. 实时倒计时分屏 Live Countdown Split-screen

0:00 / 1:00

一件有明确【零点】的事，按真实时间播放，一秒都不剪。离零点越近，分屏越多；到零点，所有分屏合成一个画面。 适合：发射、开奖、终场哨、开售、跨年倒数。

【Sonnet 5.5 测试样片】

0:00 / 0:30

由 Sonnet 5.5制作

## 

4. 延时交响 Time-lapse Symphony

![](https://pbs.twimg.com/amplify_video_thumb/2112816750903607296/img/8rL-YRRbMN5t2yQ1.jpg)

没有旁白，音乐就是剧本。延时摄影把车流、人潮、云变成光的河流，剪辑越来越密，最后卡在一个重拍上硬切黑。 适合：城市宣传片、品牌形象片、地方纪录。

【Sonnet 5.5 测试样片】

0:00 / 0:30

## 

5. 视觉调查 Visual Investigation

![](https://pbs.twimg.com/amplify_video_thumb/2112817231319171072/img/Pdt3eIy9cypX1w5m.jpg)

把同一件事的视频、照片、文件、声音、地图放在同一条时间线上互相对照：定格、画圈、放大、在原文件上划重点。 适合：事件复盘、调查报道、事故还原、辟谣。

【Sonnet 5.5 测试样片】

![](https://pbs.twimg.com/amplify_video_thumb/2113063965521772545/img/mYGPjjX_qnlRLiIA.jpg)

## 

6. 构成主义蒙太奇 Constructivist Montage

0:00 / 1:00

所有档案素材统一成黑、红、纸三色的海报印刷感，文字压在斜向色带上，跟着机器般的节拍切，两张图一撞，撞出第三层意思。 适合：工业和工程史、群像故事、有态度的历史评论。

【Sonnet 5.5 测试样片】

![](https://pbs.twimg.com/amplify_video_thumb/2113064361522864128/img/sFLWyRGEIZpBAL7J.jpg)

## 

7. 体育战术板 Sports Telestrator

0:00 / 0:54

电视足球分析那一套：先正常速度看一遍，倒回去、定格，在真实转播画面上画圈、画箭头、标出没人防的空当，最后把球场压平成战术板。 适合：比赛复盘、战术解说，任何【一段录像拆解】的内容。

【Sonnet 5.5 测试样片】

![](https://pbs.twimg.com/amplify_video_thumb/2113063064023257088/img/QbBe88nNKy6a83wN.jpg)

## 

8. 电视新闻包装 Broadcast News Package

0:00 / 0:54

一整套电视台新闻包装，全部用代码做：片头变成台标、开场的【今日要闻】目录、一直在画面底部的标题条、全屏的数据图表和地图。 适合：周报、行业快讯、公司内部播报、自媒体的固定栏目。

【Sonnet 5.5 测试样片】

![](https://pbs.twimg.com/amplify_video_thumb/2113063330621632512/img/NJ911t4Xmo9rn4I3.jpg)

加上上次更新的【实证影像】8 种，Lemo-Opuscar 已经从最早的 39 种长到了 59 种。接下来还会继续更新。

到现在为止的全部 59 种

- 剪辑与纪实（8，这次新增）：字幕新闻、1920s 新闻影片、实时倒计时分屏、延时交响、视觉调查、构成主义蒙太奇、体育战术板、电视新闻包装
    
- 实证影像（8，上次新增）：卫星简报、工程简报板、点云测绘、白模投影、数据实物化、产品拆解、显微叙事、档案灯台
    
- 手绘与绘画（7）：蜡笔儿童绘本、水彩笔刷、中国水墨、油画厚涂、一笔画、白板讲解、钢笔淡彩
    
- 东方传统（4）：皮影戏、浮世绘、红色窗花剪纸、纸雕灯影
    
- 印刷与版画（5）：Risograph 孔版印刷、复古半调案卷、木刻版画、铜版画、丝印旅行海报
    
- 图形与排版（7）：瑞士动态排版、60s 间谍片头、装饰艺术、蓝图 / 工程制图、彩色玻璃窗、象形运动图形、ASCII / CRT 终端
    
- 信息与发布（5）：数据叙事、等距信息图、暗色科技发布、活体实机录屏、科幻全息界面
    
- 卡通与动画（4）：1930s 橡皮管卡通、80 年代赛璐璐动画、科幻情景喜剧卡通、50s 扁平卡通
    
- 游戏（4）：16-bit 像素 RPG、HD-2D、微游戏快闪、综艺节奏扁平
    
- 电影与时代（2）：1920s 默片、后室 / 新怪谈
    
- 材质与 3D（5）：积木玩具、纸片立体书、移轴微缩、低多边形等距、玻璃质感产品
    

另外还有Opuscar98 长篇的98种风格提示词，也全部公开啦！

所有风格的样片都在这里，可以随心所欲的挑选自己喜欢的风

[https://lemomo-ai.github.io/lemo-opuscar/](https://lemomo-ai.github.io/lemo-opuscar/)

# 

新玩法：改成你自己的风格

先说说我做这个库的初衷。

Lemo-Opuscar 主要是给 Claude 用的，靠 Opus、Sonnet 这些模型自己的能力，用代码做出 2D、3D 的视频。跟很多动效模板类的项目不一样，我没有把东西都写成参数，而是把导演、镜头、风格这些东西用提示词讲清楚。

原因有两个：

1. 给灵感。 我希望大家翻这个库的时候，能打开思路。没灵感的时候翻一翻，会发现【原来我还可以做这种风格】。
    
2. 少设限制。 模型一直在进化。把所有东西写死成参数，在某些场景里确实好用，但也把模型自己的能力锁住了。未来Fable5.5会发布，其他模型能力也会追上来，我觉得要有一种【向前开发】的思路，比起告诉模型你“应该严格按照规矩动”，我更希望告诉模型“我想什么样的效果”。
    

这就是为什么我叫它风格库：提示词不是规定你用什么技术、调到什么数值，而是告诉模型【你可以做什么】和【我想要什么】。以后所有的开发都会围绕这一点，跟着模型一起升级。当然这样的弊端是，其他模型比如codex之类的效果可能不会太好（非常抱歉）。

现在 Opus 用起来非常顺。名字虽然是给 Opus 起的，但 Sonnet 用起来也很好，换成更新的模型只会更好。就算换成便宜一点的模型，有这套风格打底，照样能做出风格很完整的片子。

但每个人想要的都不一样：有自己的品牌色、logo、IP，有自己的账号调性。这次我把自己入库一个新风格时走的流程整理出来，每个人都能用它，把库里的风格改成只属于自己的。

## 

第 0 步：先更新

已经装过 skill 的，在终端里跑：

> claude plugin marketplace update lemolab claude plugin update lemo-opuscar@lemolab

然后重启 Claude Code。风格库本身（~/lemo-opuscar）会在下一次做片时自动更新。

用 clone 仓库方式的，在仓库里 git pull 就行。

还没装过的：

> claude plugin marketplace add lemomo-ai/lemo-opuscar claude plugin install lemo-opuscar@lemolab

## 

第 1 步：选一个入口

最简单的办法，什么都不说，直接启动 skill：输入 /lemo-opuscar:lemo-opuscar。

它会先问你用什么语言：中文、English，或者选 Other 自己写（日语、韩语都行）。之后的提问、汇报都用这个语言，片子的配音和字幕默认也一样。

[

](https://x.com/lemomo_ai/article/2113195080517562646/media/2113112507498082304)

然后问你这次想做什么：

- 用库里的风格做一支片 （原本只有这一项）
    
- 改一个库里的风格，存成自己的
    
- 从空白开始，做一个自己的风格
    
- 用你自己的风格做片（已经存过风格才会出现）
    

[

](https://x.com/lemomo_ai/article/2113195080517562646/media/2113112740130897921)

也可以一句话直接说：

- 【我想把浮世绘改成我自己的风格】
    
- 【从空白开始，做一个黑板粉笔画的风格，暖一点、慢一点】
    

改库里的风格，它会把 59 种全部列出来，附上画廊链接，你直接打字说要改哪一个。

[

](https://x.com/lemomo_ai/article/2113195080517562646/media/2113113108785004544)

从空白开始，你用自己的话描述想要的样子，也可以给一张喜欢的图或者一支片。Claude 会从库里挑一个最接近的风格当【技法底子】，说清楚为什么选它，你点头或者换一个。

## 

第 2 步：一个问题一个问题定方案

这是整个玩法的核心。Claude 一次只问一个问题，每个问题都给几个选项，它推荐的排第一，附上理由。一共十个左右，嫌多随时说【你定】，剩下的它按推荐填好，列给你看。

[

](https://x.com/lemomo_ai/article/2113195080517562646/media/2113113400423469056)

如果你嫌一题一题问太慢，每一题的最后一个选项都是【自由对话】。

选了它，就不再一个个问，改成聊天：Claude 列一张清单，哪些定了、哪些还没定，没定的每项都附上推荐。你想先说哪项就说哪项，一次说好几项也行，也可以反过来问它；拿不准的，它给你两三个方向挑。

[

](https://x.com/lemomo_ai/article/2113195080517562646/media/2113113604115599360)

它大概会按这个顺序问：

拿来做什么。 做什么片、给谁看、发在哪个平台。发竖屏信息流就要 1080×1920 或 1080×1440。有没有品牌色、logo、字体、固定角色，文件后面再给。

想改哪里。 改库里风格时，它会先把这个风格的各个部分分成三组讲给你听，用的都是这个风格自己的例子：

- 放心改：配色（在原来的逻辑里换颜色）、字体、动作快慢、声音和乐器、加或换一个标志镜头。改了风格还是它自己。
    
- 一改就变味：材质和画法、配色的逻辑本身、镜头语法。能改，但它会告诉你会丢掉什么。
    
- 不能改：风格的本质和底层引擎。改了就是另一个风格了，它会建议你换一个更接近的底子。
    

一项一项细问。 只问你要动的部分：材质、配色、字体、动态、镜头、声音、标志镜头，每项给两三个具体方向。

起名字。 中文名、英文名，或者都要。

## 

第 3 步：看汇总，点头

问完以后，它会把方案汇总给你：每一项改前是什么、改后是什么、代价是什么。你点头了，它才写下来。

[

](https://x.com/lemomo_ai/article/2113195080517562646/media/2113113878699900928)

## 

第 4 步：先看一张风格图

它用真实的绘制代码出一张风格图。改库里风格的，会把同一个画面用原风格再出一张，并排放：左边原版，右边你的，一眼看出改了什么。

如果修改特别大，像我这次的修改算是完全打破了平面设计的限制，他建议你从新的风格开始，然后给你重新画一张风格图。

[

](https://x.com/lemomo_ai/article/2113195080517562646/media/2113114660560072704)

不满意就说哪里不对，它改了再出。两轮还不对，它会直说，并建议换一个更接近的底子。

## 

第 5 步：一支 15 到 30 秒的 demo 片

风格图点头之后，它做一支短片，专门用来证明这个风格成立：

- 每一处改动都会在画面里出现至少一次，标志镜头也会出现。
    
- 有音乐和音效，默认不配音、不加字幕。
    
- 做完自己检查一轮、修一轮，再交给你，告诉你每一处改动在第几秒能看到。
    

0:00 / 0:31

## 

第 6 步：满意了，再固化成你自己的风格

demo 片交给你的时候，它会问你：固化成我的风格、再改一轮，还是先不固化。你去人之后，它才会根据固化流程进行固化。 在这之前，所有东西都只放在这次的项目文件夹里，不会出现在【我的风格】里。

固化以后，它会存在你电脑的 ~/lemo-my-styles/<名字>/ 里，和库里的风格是同一个结构：风格说明、改了什么、demo 片和它的源码。以后做片能接着用这一套技法。

库更新、重装 skill 都不会动它。底子风格以后有更新，它会提一句，问你要不要把有用的修复同步过来，不会自己改。

以后：直接点名用

> 用我的【夜浮世绘】风格做一支 30 秒的片子，讲……

再启动 skill 时，你自己的风格会排在最前面。

从空白开始也是这个流程。如果你做出了好的风格，可以把它提交到 GitHub，申请加入 Lemo-Opuscar 的风格库，我看过后会整理入库。现在开始欢迎更多风格贡献者啦。

关于档位的选择，新创建风格最好用 opus high，也可以xhigh。之后制作片子的时候可以根据需求选择sonnet high。实测中这三个档位效果是最稳定的。

最后说一句我很想说的：风格只是载体，内容才是最重要的。 编排得再花哨，没有好内容也撑不起来。

所以我的建议是，先想清楚自己想做什么。库里的样片覆盖了很多场景：讲故事、做新闻、做剪辑、讲历史、做知识讲解，都能找到参考。然后再根据自己的内容，去改出属于自己的风格。

## 

更新预告

## 

Lemo Movie Studio

一个 Claude MCP App 做片工作台。在 Claude 桌面版的对话里说一句，工作台就出现在对话里。四种开拍方式：从库里选、改一个风格、用我的风格、从空白开始。从选风格、看分镜、看样张，一直到出片、审片、交付，整条流程都在一个界面里，不用再在终端里或者App来回沟通。

现在还在打磨，未来会免费使用，这样这个库的搭配工具做好了之后，claude 做视频就是可以自己创建风格，自己固化风格，整个流水线打通。做好了我会单独写一篇。

0:00 / 1:00

  

## 

下一批风格：日系动漫

这是我自己的一点私心，已经在做了。主打一个可玩度极高。

不过先打个预防针：这一批要用到生图，所以对环境的要求会比之前苛刻不少，不是装上就能跑。具体需要什么，发布的时候我会写清楚。

库的目标是做到 99 种风格。

# 

最后

谢谢大家一直以来的支持，谢谢你们。

Lemo-Opuscar 上过 Trendshift JavaScript 日榜第 1，GitHub 上也拿到了 Starstruck 金色成就（4096 星以上）。这是我前两天审计项目的时候才知道的。

如果觉得有用，欢迎帮忙转发、推广，也欢迎去 GitHub 点个 Star！

- GitHub：
    
    [https://github.com/lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar)
    
- 样片画廊：
    
    [https://lemomo-ai.github.io/lemo-opuscar/](https://lemomo-ai.github.io/lemo-opuscar/)
    
- Opuscar98 长篇观看以及提示词：
    
    [https://lemomo-ai.github.io/lemo-opuscar/opuscar98/#styles](https://lemomo-ai.github.io/lemo-opuscar/opuscar98/#styles)""

https://x.com/chasen_liao/status/2113138389172224237
"挖槽？！花叔这个 huashu-motion skills 是真的绝  我之前也用过不少 motion skill，没一个能做到这个效果 这次真的就一句话：“给我的项目做个产品宣传片 它直接给 Pi Agent Desktop 出了一整支 30 秒的片子” 最离谱的是模型用的是 MiniMax M3.1 Flash，现在在 OpenRouter 上免费爽用 搭配 Claude Code 开 Ultra Code，模型这块一分钱没花 花叔用的是 Opus 5.5，我用免费模型跑出来的片子也一点不虚  装上只要一行： npx skills add alchaincyf/huashu-motion"""

https://x.com/KinGao476942/status/2112729924943634602
"卧槽！兄弟姐妹们，想用 Opus 5.5 做视频，一定要收藏这 8 个 GitHub 仓库。 1. awesome-opus5-5-videos（约 7100 star） 目前最大的爆款视频合集，每条都附上了背后的提示词。 [https://github.com/yihui-dev/awesome-opus5-5-videos](https://t.co/VWhSZgNz6C) 2. lemo-opuscar（约 4400 star） 一个 Claude Code skill，装上之后挑一种风格，就能做出纯代码短片，51 种风格随便选。 [https://github.com/lemomo-ai/lemo-opuscar](https://t.co/CSj7tyu8ie) 3. pdoom-video（约 3000 star） 一支歌词卡拉 OK MV 的完整工程，本地就能渲出 4K60。 [https://github.com/mexicat/pdoom-video](https://t.co/3WbzuFefAL) 4. PDoomVideo（约 2300 star） 同一首歌的另一支 MV 源码，和第 3 个对照着拆，很有意思。 [https://github.com/JohnHeibel/PDoomVideo](https://t.co/xnriTUB8nQ) 5. mg-styles-15（约 1400 star） 15 种 MG 动效风格，成片、提示词、源码全都给。 [https://github.com/Vincentwei1021/mg-styles-15](https://t.co/LkRmgFXx7b) 6. ClaudeAnimationBase（约 1300 star） 手绘卡通角色动画的起步包，自带 31 种表情。 [https://github.com/JohnHeibel/ClaudeAnimationBase](https://t.co/wkXHp8xffq) 7. awesome-claude-5-5-videos（约 560 star） 视频工作流合集，每个案例都标了出处，Opus 的就有 301 个。 [https://github.com/athemeroy/awesome-claude-5-5-videos](https://t.co/uOw55tL0CQ) 8. opus-video-prompts（约 510 star） 中文案例，配上能直接复制的提示词。 [https://github.com/joeseesun/opus-video-prompts](https://t.co/1WH40CnNub)

[

](https://t.co/7EJX8L0ndN)""

https://x.com/czzzzzzJ_/status/2112085934267346976
"我看谁不会用 Claude Opus 5.5 做视频？ 完整地看一下这四个开源仓。 从跟做到拆工程都够用： 1. lemo-opuscar — 多风格提示词 + 纯代码样片，填故事让 AI 导演短片 [https://github.com/lemomo-ai/lemo-opuscar](https://t.co/Ea3zYO6f2H) 2. awesome-opus5-5-videos — Opus 5.5 成片合集，附创作者 Prompt（HTML/Canvas/SVG/Three.js） [https://github.com/yihui-dev/awesome-opus5-5-videos](https://t.co/unZ1MIkySx) 3. PDoomVideo — 完整 MV 工程（源码/分镜/渲染），适合研究复杂动画 [https://github.com/JohnHeibel/PDoomVideo](https://t.co/QZFBjqwmIE) 4. opus-video-prompts — 约 54 个可复制案例，中文友好，新手先从这个啃 [https://github.com/joeseesun/opus-video-prompts](https://t.co/WybUYeNO2a)

[

](https://x.com/czzzzzzJ_/status/2112085934267346976/photo/1)"


https://x.com/Cryptoxorz/status/2110044544494600619
"我把电脑里 8 个 Claude 做视频的 skills，做成了一支 100 秒的视频。片子本身也是 Claude 写代码做出来的，用的是其中第一个。 下面挨个说说它们各自适合干什么。 1. xilo-opus-video 最通用。给它一个想法、一篇文章或一支参考视频，它先出三套方案和预览，你选一套，它再做成片。 [https://github.com/Kianzzz/xilo-opus-video](https://t.co/dBiKCQM9E3) 2. lemo-opuscar 一本风格图册。43 种影片风格，油画厚涂、中国水墨、浮世绘、白板讲解……报出风格名，它照着做。每种风格都配了一支纯代码样片。 [https://github.com/lemomo-ai/lemo-opuscar](https://t.co/a2soExxRDQ) 3. mg-styles-15 专做 MG 动态设计。15 种风格，每支 10 秒，附完整提示词和源码，连配乐都是用代码编的。 [https://github.com/Vincentwei1021/mg-styles-15](https://t.co/KYzQBZQWxZ) 4. dashi-animationstyle 给口播配画面。15 到 60 秒的中文口播，自带 7 套画风（手绘笔记、复古报刊、黑底科技等），成片带字幕，能直接拖进剪映。 [https://github.com/chuspeeism/dashi-animationstyle](https://t.co/DssouHRLXC) 5. huashu-art-motion 把美术史搬了进来。从洞穴壁画到像素游戏，35 种艺术风格都能动，另外还有 9 种解说动画的讲法。 [https://github.com/alchaincyf/huashu-art-motion](https://t.co/0oZ7VTeVMR) 6. wtt-code-animation-studio 从编剧开始。一个想法进去，剧本、分镜、可改的源码、带声音的成片一次交齐，沙画、粉笔、水彩这类画法也能做。 [https://github.com/WaterDJiang/Wattter_openSkills/tree/main/wattter_skills/wtt-code-animation-studio](https://t.co/pn6BdVaDE2) 7. video-shotcraft 专拍产品。把你的网页或前端项目做成带 2.5D 运镜的宣传片，自带 124 张镜头配方卡。 [https://github.com/Vincentwei1021/video-shotcraft](https://t.co/KzPD7xbCBA) 8. archival-doc（我自己做的） 这一个不画画。它去找公有领域和 CC 授权的真实历史影像，核对素材许可，再剪成纪录片。 感谢各位开源作者！"


https://x.com/minchoi/status/2111306174259691669
"This Opus 5.5 prompt is literally a $400/hr motion graphics designer: <role> You are a motion director and creative technologist. You design, animate, score and QA a finished film entirely in code. Judge every choice against the best work in the genre and any references in the brief. A film with no bugs is not finished; it's finished when it holds up next to that work. These instructions are the floor, not the ceiling. If anything conflicts, the brief wins, then any kit it names, then these defaults. </role> <brief> Leave any line blank and decide it yourself, noting the choice and a one-line reason in brief.md. mode: [showreel | product | launch-story | explainer] subject: [product URL, topic, or "the craft itself"] viewer: [who's watching and what they care about] end state: [what they should feel, know or do in the last second] length: [e.g. 15 s 16:9; 30 s 16:9 + 9:16] frame rate: [blank = 60 for UI/product, 30 for character, 24 for handmade looks] brand: [logo, colours, fonts, or "derive from the product"] facts: [URL or file. The only source for any claim on screen or in voice.] assets: [files, or "capture from the live product"] style: [direction or reference videos, or blank] sound: [music + sfx | voice + music + sfx | silent] autonomy: [unattended: never stop | gated: stop at each ◆] toolchain: [Remotion | HTML + GSAP renderer | a kit repo to follow | blank] sign-off: [end mark and call to action] </brief> <modes> - showreel: the craft is the subject. Build it around one idea that keeps transforming, not a sampler of effects. Show range: type, shape, UI, 3D or simulation, an organic moment, and one transition worth rewinding. A new composition every 1–2.5 s, with one or two held breaths. No fake clients, logos or metrics. - product: the product is the hero. Real logo, real UI rebuilt as live components, every action with a visible result, ending on the name and URL. A new composition every 1.4–3.5 s. - launch-story: characters carry the release. Write 2–3 treatments and pick one. Characters act: readable poses, holds on faces, funny timing. One or two facts at most, woven into the world. - explainer: one cause and effect. Hook, familiar world, disruption, mechanism, discovery, consequence, recap. Narration at 125–145 wpm, and labels never repeat it. </modes> <assets> - Capture the real product at 2×, take the logo as SVG from the source, and sample the real colours and fonts. Never redraw a logo. - Never show a raw screenshot as a static slab. Rebuild its panels, icons and text as live HTML/SVG so each part can move. - Generated images are references (style frames, character sheets, key poses) that you rebuild in code. They go on screen only if the brief allows, labelled as concept. - References are for study. Find their cuts and fast moments with a frame-difference pass and dense contact sheets, and extract the principles. Never copy footage, layouts or music. </assets> <craft> 1. Frame one is a finished picture that works as a still on a busy feed. The hook lands in the first second. 2. One object, shape or word carries the film, and it lands on the same pixels on both sides of every handoff. 3. Transitions are made of content: the thing in front moves to camera, wipes or unfolds into the next scene. Hard cuts only when size, direction and subject match, and only on a beat. 4. One lead movement with overlapping secondary ones. Nothing starts or stops all at once. 5. Speed always changes: arrive slowly enough to read, leave fast. No linear easing. Use anticipation, follow-through, squash and stretch, springs and arcs. 6. Every action has a visible result. 7. Type is motion, not captions: it enters, masks and reveals. Keep it readable for ~0.3 s per word (0.7 s minimum), and never over busy picture without a plate. If the picture says it, cut the word. 8. Vary scale and layout: macro, wide, overhead, full-frame type. The subject fills the frame. Never repeat a layout. 9. Holds breathe with micro-motion, and nothing freezes. Camera moves are motivated, with motion blur on the fast ones. 10. 3D only where it explains something spatial. Use product-shoot lighting, a camera at 35–55°, real materials, and labels as HTML tracked from the scene. 11. Every effect earns its place. No decorative particles, generic gradients or stock glitches. </craft> <audio> Audio comes first, and the picture is cut to it. - Music matches the energy and sits low. Never name a brand or artist in a music prompt. Trim or offset a track rather than bend the picture. - Detect beats and write timing.json: beats, the drop, voice in/out frames, and key actions snapped to beats. All animation timing reads from it. - Effects only for real on-screen events: one soft whoosh per scene change, and clicks and impacts on real actions, each in its own frequency range just above the music. - Voices: audition two per character and two takes per line. Mouths follow loudness and stay still in silence. Duck the music under dialogue. - Mix to about −14 LUFS with true peak ≤ −1 dBTP. Export a music-only version. </audio> <build> - Everything is code on one timeline, with pinned local fonts and assets, rendered frame by frame and encoded with ffmpeg. API keys stay in environment variables. - Render a 3–5 s test end to end before real work. - Every value is a function of the frame number. No timers, no unseeded randomness. - Write shared tokens, eases and handoff positions first, build each scene as its own component, and run builders in parallel. - Recompose each format rather than cropping, and keep 9:16 content out of the platform UI zones. </build> <workflow> 1. Lock facts: facts.json with every claim, its exact source sentence and its URL. Collect the real assets. 2. Study the references and, for public work, how this audience talks about the subject now. 3. Concept: 2–3 directions, pick one, and name three signature moments without using effect names. 4. Storyboard table: time, on screen, purpose, audio cue, exit, and what carries over. It must read with the sound off. ◆ 5. Style bible (≤6 colours, local fonts, textures, motion vocabulary) and three style frames rendered in code, plus character sheets and key poses if needed. ◆ 6. Audio and timing map. Play the audio-only mix. ◆ 7. Build, assemble, and run the critic loop until the quality bar passes. 8. Deliver. ◆ If asked, save the pipeline as a reusable skill. </workflow> <critic_loop> The builder never judges its own work. After the storyboard, each scene and each full render, a fresh critic subagent that has seen none of the building pulls its own frames (every 0.2 s, dense around transitions), measures, and returns ranked problems with timestamps, ending in "ship" or "one more pass". Every full render also gets: - Sound-off read: a critic sees only a silent 2 fps contact sheet and retells the story. - Sync: every hit and line within 1 frame of timing.json. - Fact check: every word traced to facts.json. - Director's review: a brutal critique of what feels assembled, slow or generic. Fix the biggest problem first, re-render, and have a new critic recheck every earlier item. Log each round in ledger.md with before and after numbers. </critic_loop> <quality_bar> Measured: - Exact duration, size and frame rate. - Frame one finished. - ≤1 s frozen per 30 s, and no still stretch over 0.5 s. - Text contrast ≥4.5:1, no collisions, inside safe margins. - Brand colours match in the render. - Cuts and hits within 1 frame of the beat. - Loudness ~−14 LUFS, no clipping, effects below music and voice. - Understood with the sound off. - Every claim in facts.json, and nothing invented (testimonials, ratings, prices, results, real people). Anything generated is labelled. Judged: a critic would put it beside the references without it looking weaker. </quality_bar> <deliverables> The final MP4 per format, a music-only version, a 10–20 frame contact sheet, brief.md, facts.json, the style bible, timing.json, ledger.md, the quality-bar results, and a note on what a human should still check by eye and ear. </deliverables>"

https://x.com/Khazix0918/status/2110587546271191166
"[https://github.com/wheresryan22/anatomy/tree/main](https://github.com/wheresryan22/anatomy/tree/main)"

https://x.com/laobaishare/status/2108533494725103926
"Netflix工程师放出20个GitHub仓库，直接把Claude Opus 5.5改造成视频生成机器 视频都能生成了，那67个Skills还能解锁什么玩法？ [https://mp.weixin.qq.com/s/GtBZZAmxjJc_qjvpw47pCw](https://t.co/juE4O3Zht7) 【Opus 5.5专用工具】 1. claude-motion：自动检查每一帧，音频也写进代码 [http://github.com/whaleyxbt/claude-motion](https://t.co/gm8pHPbTjM) 2. claude-motion-design：HTML+Playwright+ffmpeg，不用Remotion [http://github.com/howseen-ai/claude-motion-design](https://t.co/5Q05MZWj0A) 3. motion-graphics-skills：13个启动视频技能 [http://github.com/charlie947/motion-graphics-skills](https://t.co/Y3iy8S7F2r) 4. claude-remotion-skill：一句话生成Remotion编辑器，带字幕和背景音乐 [http://github.com/haidrrrry/claude-remotion-skill](https://t.co/GGI7wSljgQ) 5. klik-anim-skill-creation：动画和摄像机原理库 [http://github.com/t3knobox/klik-anim-skill-creation](https://t.co/hQlQeurqVa) 6. hyperframes-motion-reel-skill：120BPM节奏感宣传片 [http://github.com/Sunwood-ai-labs/hyperframes-motion-reel-skill](https://t.co/Pujssm8tHW) 7. product-launch-motion：完整产品发布片，含旁白和调色 [http://github.com/AbubakrChan/product-launch-motion](https://t.co/tHolNd7RAD) 8. animate：单文件生成短视频，边做边分镜 [http://github.com/cth9191/animate](https://t.co/ncBekH1eOW) 9. motion-design-skills：时间、配色、排版、Logo、Remotion [http://github.com/iart-ai/motion-design-skills](https://t.co/iVf7Yv6LVa) 10. hyperframes-student-kit：14个技能+406张动画素材卡 [http://github.com/nateherkai/hyperframes-student-kit](https://t.co/psPWKWzaZ6) 【渲染引擎】 11. hyperframes：HTML直接转MP4，最常装的那个 [http://github.com/heygen-com/hyperframes](https://t.co/emV6qnhzTe) 12. remotion：用React写视频 [http://github.com/remotion-dev/remotion](https://t.co/RHqZD5eqZT) 13. remotion skills：Remotion官方技能库 [http://github.com/remotion-dev/skills](https://t.co/de89xP4YKS) 14. GSAP：驱动HyperFrames的时间轴 [http://github.com/greensock/GSAP](https://t.co/Z3KQec6YoX) 【配套生态】 15. motion-design-skill：通用动画原理 [http://github.com/LottieFiles/motion-design-skill](https://t.co/a3QoQFziNI) 16. awesome-motion-design-agent-skills：GSAP、Remotion、Lottie、Rive技能地图 [http://github.com/frankxai/awesome-motion-design-agent-skills](https://t.co/izIdhDDA4V) 17. motion-graphics：直接从文案生成动画素材 [http://github.com/Barty-Bart/motion-graphics](https://t.co/G3I4PQ9Hme) 18. motion-dev-animations-skill：[http://Motion.dev](https://t.co/zloZJjjSjT)网页动画 [http://github.com/199-biotechnologies/motion-dev-animations-skill](https://t.co/bwxDPk99Xt) 19. motion：Framer Motion的新版本 [http://github.com/motiondivision/motion](https://t.co/aDmG6OLaeG) 20. lottie-web：需要Lottie格式而不是MP4时 [http://github.com/airbnb/lottie-web](https://t.co/V1s0w8MI5g) 工作流就这么简单：Opus写代码→技能库设置节奏摄像机→引擎输出MP4 每个仓库安装前都看一眼，收藏备用"

https://x.com/yupi996/status/2107735426769551691
"生怕你不知道 > 网页上那些滚动动画，其实都有专门的名字，直接报给 AI 比费力写提示词更好使！  Scroll-triggered，滚进屏幕就自己播完，比如卡片淡入  Scroll-linked，滚多少动多少，比如顶部的阅读进度条  Parallax，背景比前景滚得慢  Sticky，滚到顶就钉住，比如通讯录的字母标题  Scroll Snap，一次停一屏  Horizontal Scroll，往下滚，卡片横着走 下次跟 AI 说「导航栏用 Sticky，首屏背景做成 Parallax」就行！"

https://x.com/majidmanzarpour/status/2102476258948927543
"  Create a single self-contained HTML file that renders an animated pixel art wizard casting a spell, using vanilla JavaScript and Canvas 2D. No external assets, libraries, or network requests. RENDERING - Draw everything to an offscreen canvas at a fixed logical resolution of 128x96, then blit to a fullscreen display canvas scaled by the largest integer factor that fits the window, centered, with imageSmoothingEnabled = false and CSS image-rendering: pixelated. - All drawing snaps to integer coordinates on the logical canvas. No sub-pixel positions, anti-aliasing, gradients, or shadowBlur. - Fixed palette of ~24 hex colors: deep blues/purples for night sky, warm robe tones, 3-4 bright magic colors. Every pixel comes from this palette. CHARACTER - Build the wizard procedurally from filled rects and pixel runs, ~24x32 logical pixels: pointed hat with a bend, long beard, two-shade robe with darker outline, staff with a gem at the tip. - Parameterize the pose (staff angle, arm raise, head tilt, robe sway). Animate parameters smoothly, then quantize to the pixel grid each frame so motion reads at an 8-12 fps pixel animation feel even though the loop runs at 60fps. ANIMATION - Looping state machine: IDLE (2-frame bob, beard sway) -> CHARGE (staff raises, gem flickers, sparks spiral inward) -> CAST (bright burst, projectile fires across the scene, 1-2 pixel screen shake) -> RECOVER (settle back). Ease pose parameters between keyframes. - Pooled allocation-free particle system: preallocate and reuse. Sparks orbit the gem during CHARGE, explode outward on CAST, each particle stepping its palette index from white to magic color to dark before despawn. Snap particle positions to the grid when drawing. - Fixed 60hz timestep update with rAF rendering. Zero object allocation inside the loop. SCENE - Minimal background: dark sky, a few twinkling 1px stars, moon, stone floor line. Character silhouette must read clearly. - Subtle 1px rim light on the wizard from the gem, brightening during CHARGE and CAST. QUALITY BAR - Crisp pixels at any window size, seamless loop, stable 60fps, readable silhouette. Should look like a polished 16-bit sprite animation, not vector shapes scaled down."

這個比較不一樣, 是寫作的, 整理但不要放進去skill:
https://x.com/cnyzgkc/status/2107498419099209806
"分享我常用的7个skill，从选题到排版，全部分享给大家~ 你只需照着装就能拼出一条自己的写作流水线，建议收藏~ 1｜选题：dbskill（

[@dontbesilent](https://x.com/dontbesilent)

） 动笔前先拿它过一遍，问它「这个选题谁会看、凭什么点开」。答不上来的选题，直接放回选题库。 [http://github.com/dontbesilent2025/dbskill](https://t.co/joAWxfCJwa) 2｜写稿：khazix-skills（

[@Khazix0918](https://x.com/Khazix0918)

） 我不让它代写，主要学它的长文推进：开头怎么抓人，每隔几段怎么把人拉回来。 [http://github.com/KKKKhazix/khazix-skills](https://t.co/parqnADZOH) 3｜自查：dbs-ai-check（

[@dontbesilent](https://x.com/dontbesilent)

） dbskill 里自带的。写完先让它出一份 AI 痕迹报告，默认只标问题不改原文，哪句要改自己定。 [http://github.com/dontbesilent2025/dbskill](https://t.co/joAWxfCJwa) 4｜润色：Humanizer-zh（

[@op7418](https://x.com/op7418)

） 报告里确认要改的句子，再交给它处理。整篇丢进去，它容易把正常的过渡也一起删掉。 [http://github.com/op7418/Humanizer-zh](https://t.co/0SBo44RXSz) 5｜配图：baoyu-skills（

[@dotey](https://x.com/dotey)

） 封面、信息图、文中插图都靠它，一个仓库装完基本够用。 [http://github.com/jimliu/baoyu-skills](https://t.co/75EP24sbfD) 6｜排版：gzh-design（

[@jiamu_future](https://x.com/jiamu_future)

、

[@li_mo60607](https://x.com/li_mo60607)

） Markdown 直接转成能粘进公众号后台的 HTML，章节编号、代码块都排好了。 [http://github.com/isjiamu/gzh-design-skill](https://t.co/XQWtZ84e2g) 7｜二次分发：guizang-ppt-skill（

[@op7418](https://x.com/op7418)

） 把文章的核心观点做成一份网页 PPT，杂志风和瑞士风二选一，拿去做分享很省事。 [http://github.com/op7418/guizang-ppt-skill](https://t.co/YNnoJ0X4V4)

[

](https://x.com/cnyzgkc/status/2107498419099209806/photo/1)"