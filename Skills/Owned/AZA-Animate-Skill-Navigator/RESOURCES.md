# 動畫資源選型索引

依據同目錄 `AZA-Animate-Skill-Navigator.md` 的蒐集內容整理；原稿保留作為來源，不是執行指令。以下能力均為蒐集來源的描述，未逐一檢查上游或實測。推薦是依用途的初選，不代表品質排名或相容性保證。安裝前須查上游 README、授權、依賴、費用與當前調用方式。

## 先分清楚資源類型

- **工作流／skill 候選**：引導 AI 規劃、製作或檢查；是否為可直接安裝的 skill，仍以倉庫為準。
- **風格／案例庫**：提供外觀、提示詞或範例，不等於具備端到端製作能力。
- **完整工程**：適合拆解、改作；不是通用生成器。
- **引擎／函式庫**：負責動畫或渲染，不會自動補齊腳本、配音與導演流程。

## 1. 製作工作流與風格入口

| 資源 | 來源描述的定位 | 優先考慮的需求 |
|---|---|---|
| [xilo-opus-video](https://github.com/Kianzzz/xilo-opus-video) | 從想法、文章或參考影片提出方案與預覽，再製作 | 尚無明確方向，希望先比較提案 |
| [lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar) | 多風格代碼短片；可改風格、從空白建立並保存個人風格 | 想先選視覺風格，或建立可重用風格 |
| [huashu-motion](https://github.com/alchaincyf/huashu-motion) | 貼文展示產品宣傳片製作 | 產品影片候選；與下一項分開查證，不假定同一工具 |
| [huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion) | 藝術史風格與解說動畫表達 | 美術風格強烈、敘事或知識解說 |
| [dashi-animationstyle](https://github.com/chuspeeism/dashi-animationstyle) | 中文口播配畫面、字幕、可接後續剪輯 | 已有口播稿的短影音 |
| [wtt-code-animation-studio](https://github.com/WaterDJiang/Wattter_openSkills/tree/main/wattter_skills/wtt-code-animation-studio) | 劇本、分鏡、可改源碼與有聲影片 | 希望從故事開始，並取得可修改工程 |
| [video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | 網頁／前端產品的 2.5D 運鏡與鏡頭配方 | 真實 UI、網站與產品展示 |
| [claude-motion](https://github.com/whaleyxbt/claude-motion) | 代碼影片、音訊與逐幀檢查 | 重視製作檢查流程；具體覆蓋範圍需查證 |
| [claude-motion-design](https://github.com/howseen-ai/claude-motion-design) | HTML、Playwright、ffmpeg 路線 | 偏好網頁技術、不想用 Remotion |
| [claude-remotion-skill](https://github.com/haidrrrry/claude-remotion-skill) | Remotion 編輯器、字幕與背景音樂 | 已決定採用 React／Remotion |
| [hyperframes-motion-reel-skill](https://github.com/Sunwood-ai-labs/hyperframes-motion-reel-skill) | 節拍驅動的宣傳片 | 強節奏 motion reel |
| [product-launch-motion](https://github.com/AbubakrChan/product-launch-motion) | 產品發布片、旁白與調色 | 產品發布敘事 |
| [animate](https://github.com/cth9191/animate) | 單檔短影片與分鏡 | 想走精簡、單檔製作路線 |
| [motion-graphics](https://github.com/Barty-Bart/motion-graphics) | 文案轉動畫素材 | 已有文案，想產生動態圖像 |
| archival-doc | 貼文描述：尋找公有領域／CC 歷史影像、核對許可並剪輯 | 真實史料紀錄片；原稿沒有倉庫網址，先確認取得方式與授權 |

## 2. 動態設計技能與原理

| 資源 | 用途 |
|---|---|
| [mg-styles-15](https://github.com/Vincentwei1021/mg-styles-15) | MG 動態設計風格、成片、提示詞與源碼；適合先挑視覺語言 |
| [motion-graphics-skills](https://github.com/charlie947/motion-graphics-skills) | 啟動／宣傳影片技能集合 |
| [klik-anim-skill-creation](https://github.com/t3knobox/klik-anim-skill-creation) | 動畫與攝影機原理 |
| [motion-design-skills](https://github.com/iart-ai/motion-design-skills) | 時間、配色、排版、Logo 與 Remotion |
| [hyperframes-student-kit](https://github.com/nateherkai/hyperframes-student-kit) | 技能與動畫素材卡；偏學習／組裝入口 |
| [motion-design-skill](https://github.com/LottieFiles/motion-design-skill) | 通用動畫設計原理 |
| [motion-dev-animations-skill](https://github.com/199-biotechnologies/motion-dev-animations-skill) | Motion 網頁動畫；不是 MP4 成片工作流 |
| [awesome-motion-design-agent-skills](https://github.com/frankxai/awesome-motion-design-agent-skills) | GSAP、Remotion、Lottie、Rive 等資源地圖 |

## 3. 案例、提示詞與可拆解工程

| 資源 | 類型與用途 |
|---|---|
| [awesome-opus5-5-videos](https://github.com/yihui-dev/awesome-opus5-5-videos) | 成片與提示詞合集；找靈感或參考案例 |
| [awesome-claude-5-5-videos](https://github.com/athemeroy/awesome-claude-5-5-videos) | 有出處的影片工作流合集 |
| [opus-video-prompts](https://github.com/joeseesun/opus-video-prompts) | 中文友善案例與可複用提示詞 |
| [pdoom-video](https://github.com/mexicat/pdoom-video) | 歌詞／卡拉 OK MV 工程，研究時間軸與渲染 |
| [PDoomVideo](https://github.com/JohnHeibel/PDoomVideo) | 另一份 MV 工程，可與上一項對照；保留不同擁有者與大小寫 |
| [ClaudeAnimationBase](https://github.com/JohnHeibel/ClaudeAnimationBase) | 手繪卡通角色動畫起步包與表情素材 |
| [anatomy](https://github.com/wheresryan22/anatomy/tree/main) | 原稿只有連結，未說明功能；確認內容後再推薦 |

## 4. 引擎與輸出格式

| 資源 | 定位 | 選型提醒 |
|---|---|---|
| [HyperFrames](https://github.com/heygen-com/hyperframes) | HTML 轉影片 | 查證目前渲染介面與依賴 |
| [Remotion](https://github.com/remotion-dev/remotion) | React 程式化影片 | 留意版本、渲染環境與授權 |
| [Remotion skills](https://github.com/remotion-dev/skills) | Remotion 技能庫 | 配合 Remotion，不是另一個引擎 |
| [GSAP](https://github.com/greensock/GSAP) | 網頁動畫與時間軸 | 匯出 MP4 仍需渲染／編碼流程 |
| [Motion](https://github.com/motiondivision/motion) | 網頁互動動畫 | 網站動效不等於影片輸出 |
| [lottie-web](https://github.com/airbnb/lottie-web) | 播放 Lottie 動畫 | 適合 Lottie 交付需求；播放器不等於製作／匯出工具 |

## 5. Lemo-Opuscar 風格導覽

原稿不同貼文出現 43、51、59 種，代表來源快照不同；不把數量當成當前規格。

- [樣片畫廊](https://lemomo-ai.github.io/lemo-opuscar/)
- [Opuscar98 長篇與風格提示詞](https://lemomo-ai.github.io/lemo-opuscar/opuscar98/#styles)

| 風格族群 | 原稿收錄的方向 |
|---|---|
| 剪輯與紀實 | 字幕新聞、1920s 新聞影片、即時倒數分屏、縮時交響、視覺調查、構成主義蒙太奇、體育戰術板、電視新聞包裝 |
| 實證影像 | 衛星簡報、工程簡報板、點雲測繪、白模投影、數據實物化、產品拆解、顯微敘事、檔案燈台 |
| 手繪與繪畫 | 蠟筆繪本、水彩、中國水墨、厚塗油畫、一筆畫、白板講解、鋼筆淡彩 |
| 東方傳統 | 皮影戲、浮世繪、紅色窗花剪紙、紙雕燈影 |
| 印刷與版畫 | Risograph、復古半調、木刻、銅版畫、絲印旅行海報 |
| 圖形與排版 | 瑞士動態排版、60s 間諜片頭、裝飾藝術、藍圖、彩色玻璃、象形運動圖形、ASCII／CRT |
| 資訊與發布 | 數據敘事、等距資訊圖、暗色科技發布、實機錄屏、科幻全息介面 |
| 卡通與動畫 | 橡皮管卡通、80 年代賽璐璐、科幻情境喜劇、50s 扁平卡通 |
| 遊戲 | 16-bit 像素 RPG、HD-2D、微遊戲快閃、綜藝節奏扁平 |
| 電影與時代 | 1920s 默片、後室／新怪談 |
| 材質與 3D | 積木、紙片立體書、移軸微縮、低多邊形等距、玻璃產品 |

來源描述的自訂流程：選現有風格或空白起步 → 討論材質、配色、字體、動態、鏡頭與聲音 → 確認方案 → 風格圖 → 短 demo → 經同意保存為個人風格。這是該工具的來源介紹，不要求其他工具照辦。尚在預告的 Studio 與日系動漫不列為已可用能力。

## 6. 非 skill 的提示詞與術語

### 導演式製作提示詞

[原貼文](https://x.com/minchoi/status/2111306174259691669) 提供完整 prompt，不是已確認可安裝的 skill。可借用的需求欄位：模式（showreel／product／launch-story／explainer）、主題、觀眾、結尾目的、片長與比例、品牌、事實來源、素材、風格、聲音、工具鏈與 CTA。

製作要點：先鎖定事實與真實產品素材；比較創意方向；分鏡與風格圖；音訊時間圖；先做短段端到端渲染；逐幀檢查轉場、可讀性、音畫同步；交付影片與可修改工程。原 prompt 的節奏、音量與品質數值是特定配方，不當成所有專案的硬性標準。

### 像素巫師 Canvas 範例

[原貼文](https://x.com/majidmanzarpour/status/2102476258948927543)：單一 HTML、原生 JS／Canvas 2D、128×96 邏輯畫布、整數倍縮放、關閉平滑、有限色盤；以 IDLE → CHARGE → CAST → RECOVER 狀態機與預配置粒子產生循環。適合像素互動 demo；不是現成 skill，也不自帶影片匯出。

### 網頁捲動動畫詞彙

[原貼文](https://x.com/yupi996/status/2107735426769551691)

| 術語 | 意思 |
|---|---|
| Scroll-triggered | 捲到指定位置觸發播放 |
| Scroll-linked | 動畫進度跟隨捲動進度 |
| Parallax | 前景與背景以不同速度移動 |
| Sticky | 元素到達指定位置後黏住 |
| Scroll Snap | 捲動停靠在指定區塊 |
| Horizontal Scroll | 橫向內容移動，可由垂直捲動驅動 |

原稿開頭的 UI 建議「避免不必要的次要標籤與說明，讓版面自己解釋」作為設計備註保留，不是動畫工具。

## 7. 來源與維護

主要蒐集貼文：[Lemo 更新](https://x.com/lemomo_ai/status/2113195080517562646)、[huashu-motion](https://x.com/chasen_liao/status/2113138389172224237)、[八個倉庫](https://x.com/KinGao476942/status/2112729924943634602)、[四個開源倉庫](https://x.com/czzzzzzJ_/status/2112085934267346976)、[八種製作工具](https://x.com/Cryptoxorz/status/2110044544494600619)、[工具與引擎整理](https://x.com/laobaishare/status/2108533494725103926)、[anatomy 線索](https://x.com/Khazix0918/status/2110587546271191166)。

- 去除星數、免費額度與模型優劣宣傳；這些不是可靠的長期選型依據。
- 原稿的安裝指令有多行黏合情形；本索引不重用，實際安裝查上游。
- huashu-motion 的 GitHub 位置由原稿 `npx skills add alchaincyf/huashu-motion` 推得，尚未線上確認。
- archival-doc 沒有倉庫連結；anatomy 沒有功能說明；兩者不作無條件首選。
- 寫作流水線另存上層 `AZA-Writing-Resources.md`，不是本導航的候選資源。
