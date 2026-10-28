# omp-orchestrate

Sol 主控、Luna 選擇性執行的 omp skill。目的是把完整工作真正移出 Sol，而非開越多代理越好；若交接與重工不划算，就由 Sol 直接完成。不更動全域 settings 或內建 agents。

## 使用

安裝後開一個新的 omp session，讓 skill 與 slash command 被載入：

```powershell
omp --model openai-codex/gpt-6.1-sol --thinking medium
```

只規劃：

```text
/skill:omp-orchestrate 規劃這個功能，先給必要決策與驗收條件，暫不修改程式。
```

規劃並執行：

```text
/skill:omp-orchestrate 實作這個功能。Sol 掌舵；可完整交付、且交接划算的工作交給 Luna，其他直接完成。不要重複實作，整合後驗證。
```

自然語言要求這組多模型協作也會符合 skill 的觸發描述。Slash command 需 omp 的 skill commands 功能已啟用；若停用，在提示中直接要求讀取並使用 `omp-orchestrate`。

主 session 用 Sol；skill 不會自動切換主模型。預設不開子代理，需要時同時最多一個；只有你明確要求平行、且工作互不干涉時才放寬。小任務或緊密耦合工作由 Sol 完成。Luna 保持 medium effort；Sol 的 effort 沿用你啟動時的選擇，並非 skill 強制設定。

## 維護

- 流程權威：本目錄的 `SKILL.md`。
- 子角色與模型綁定：可攜副本 `agents/` 下的原生定義；實際啟用時放到 `~/.omp/agent/agents/`。Luna 是一般工人；Terra／Astra 都是必要時的單一技術／架構支援，不再加入多層工頭鏈。
- 執行期例外：`runtime.md`，涵蓋 discovery、路由覆寫、深度與真正的 read-only plan mode。
- 成本判斷：`cost-policy.md`。比較的是相同驗收結果下的整體完成成本，包含 Sol、子代理上下文、交接、重工與驗證；不保證開 Luna 一定比較省。

安裝／更新對照：本目錄的 `SKILL.md`、`README.md`、`runtime.md`、`cost-policy.md`、`LICENSE` 放到 `~/.omp/agent/skills/omp-orchestrate/`；`agents/omp-luna.md`、`omp-terra.md`、`omp-astra.md` 放到 `~/.omp/agent/agents/`。更新後重開 session。專案 `.omp/agents/` 中同名定義優先，不能只更新使用者副本就假設該專案也生效；首次使用或異常時確認有效來源。

審查修正：非瑣碎已定案工作需評估一次完整工作包；不派工指出未滿足的條件。續派必須有資訊增量；使用者明確指定角色不可靜默替換。診斷實驗須 host 允許且明確授權，最終驗收仍由 Sol 執行。必要驗收受阻應列 blocked，不算 complete。

這些是原生檔案式定義，不是強制排程器或安全沙箱。尤其 planning-only 是工作契約；需要工具層級的唯讀保證時，使用 omp 的實際 plan mode 並接受其可用角色限制。

這是提示詞式派工，不是會強制排程的程式。規則要求：規格、範圍、可驗收結果與成本條件成立，且 host 允許時，Sol 自行呼叫 `task`，不需要你手動派工。只有實際 task 結果與 agent ID 才算已派工；列出分工計畫不算。角色條件與各自輸出以 `SKILL.md` 的路由表為權威；Terra 不再負責管理其他工人。

## 驗證範圍

既有階層 smoke（session `01a17dd9-ac45-76d1-8ad5-205a8eca223b`）確認過各模型路由；不代表現行策略會啟動整組角色，也不是節省成本的證明。

現行稀疏派工 smoke（session `01a17fe6-143d-76d2-9953-62b64cfa66e0`）預先給定已成立的派工條件，確認 Sol 實際呼叫一次 `task`，建立唯一的 `omp-luna` 子代理 `RangeCases`，收到完整的範例資料後完成驗收；持久化 metadata 確認主控為 GPT-6.1 Sol、工人為 GPT-6 Luna，沒有 Terra、Astra 或巢狀派工。這證明該條件下的工具路徑，不保證所有任務都會正確判斷是否值得派工，也不是比 Sol 單獨完成更省錢的基準測試。

審查修正後的決策 smoke（session `01a17ff4-0d83-760e-8f5f-a2a805a4ac49`）由 Sol 載入安裝版與 runtime 參考，逐一評估六個假設情境：先辨識完整工作包再比較交接成本、無資訊增量停止續派、host 禁止時不跑診斷實驗、確認同名專案角色來源、明確指定角色失敗不替換、必要驗收未執行則 blocked。六項回答符合修正後契約；工具紀錄僅讀取文件。這是情境決策驗證，不是實際注入路由故障、測試專案覆蓋或證明自然派工更省錢。
