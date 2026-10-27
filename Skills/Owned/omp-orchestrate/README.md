# omp-orchestrate

已安裝為使用者層級的 omp skill；不需要 Codex plugin，也沒有更動全域 settings 或內建 agents。

## 使用

安裝後開一個新的 omp session，讓 skill 與 slash command 被載入：

```powershell
omp --model openai-codex/gpt-6.1-sol
```

只規劃：

```text
/skill:omp-orchestrate 規劃這個功能，先定架構、介面、工作包與驗收條件，暫不修改程式。
```

規劃並執行：

```text
/skill:omp-orchestrate 實作這個功能。重大架構交給 Astra、複雜工作包交給 Terra、明確切片交給 Luna；整合後驗證實際行為。
```

自然語言要求這組多模型協作也會符合 skill 的觸發描述。Slash command 需 omp 的 skill commands 功能已啟用；若停用，在提示中直接要求讀取並使用 `omp-orchestrate`。

目前 session 不是 Sol 時，用 `/model` 選擇 Sol；skill 本身不會切換主模型。小任務會跳層，不會為了湊齊角色而建立代理。

## 維護

- 流程權威：本目錄的 `SKILL.md`。
- 三個子角色與模型綁定：`~/.omp/agent/agents/omp-astra.md`、`omp-terra.md`、`omp-luna.md` 的 frontmatter。
- 執行期例外：`runtime.md`，涵蓋 discovery、路由覆寫、深度與真正的 read-only plan mode。

這些是原生檔案式定義，不是強制排程器或安全沙箱。尤其 planning-only 是工作契約；需要工具層級的唯讀保證時，使用 omp 的實際 plan mode 並接受其可用角色限制。

## 已驗證

在 omp 18.13.1 啟動新的 CLI session，實際載入 skill 並執行 planning-only smoke。持久化 assistant-message metadata 確認 Sol 主控、Astra 架構諮詢、Terra 工頭與兩個 Luna 工人均使用指定模型；Terra 在同一批次派出兩個工人，形成兩層子代理鏈。

驗收內容：CSV 空輸入與逗號／引號 escaping 合約、攝氏轉換例子、分鐘拆分的 59／60 分鐘邊界。完整 transcript 的工具呼叫只含 read、task、wait；沒有產品檔案修改或 build/test/formatter 命令。這是編排與規劃驗證，不是產品實作驗證。

證據 session：`01a17dd9-ac45-76d1-8ad5-205a8eca223b`。修改模型後須重新驗證路由，catalog 中存在不代表呼叫一定成功。

依 writing-for-agents 精簡後，另以 session `01a17ddd-a8bd-70af-adae-a9a762a21edb` 驗證小任務跳層：新版 skill 被載入，Sol 直接產出單一 clamp 函式的規劃與邊界例子；工具紀錄只有讀取 skill，沒有啟動子代理或修改產品檔案。
