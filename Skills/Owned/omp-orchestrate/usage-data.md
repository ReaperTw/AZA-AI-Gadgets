# 本機用量資料

集中位置：`~/.omp/agent/orchestration-data/`（本機為 `C:\Users\User\.omp\agent\orchestration-data\`）。資料放在公開 repository 外，不會跟 skill 一起 commit。只存模型／角色名稱、token、omp 紀錄的 API 成本、時間、session ID、標籤與資料完整性警告；不複製提示詞、回答、程式碼、專案路徑或憑證。

## 收集

```powershell
python "$HOME/.omp/agent/skills/omp-orchestrate/scripts/usage.py" collect --scan
```

掃描使用者層級原生 sessions 中有 `omp-orchestrate` 使用痕跡的頂層 session，連同其現存子代理 transcript，將 assistant usage 與 `model_usage` 額外呼叫統整。每個 root session 一份 JSON；重跑更新同一份，不累加重複用量。這是快照而非 daemon，不會即時監控；skill 要求結束或受阻時執行收集，若 host 禁止命令，請手動執行。讀取檔案不需要額外模型呼叫。

原始 transcript 已被清理的子代理無法補回，會回報警告；缺少成本不當作零成本。fork／匯入 lineage 暫不當作乾淨樣本收集，避免繼承歷史誤算。未完成的最後一行會標警告，其餘損壞行拒絕匯入。

## 標記可比較的樣本

以**一個新 session 做一個任務**，避免整段多任務對話混算。接受與否由主控依實際驗收指定，不從最後一句話推測。自動掃描預設 `unknown`／`unclassified`，後續更新不會覆蓋人工標籤。

```powershell
python "$HOME/.omp/agent/skills/omp-orchestrate/scripts/usage.py" collect "完整的 root-session.jsonl 路徑" --kind real --task-kind parser --outcome accepted
```

`--outcome` 可用 accepted、blocked、failed、unknown；`--kind` 可用 real、smoke、mixed、unclassified。`task-kind` 用不敏感的短分類，不放原始需求。手動標籤與自動收集勿同時執行；目前快照更新是 atomic replacement，不是多寫入者資料庫。

既有長對話用 mixed；功能驗證與派工測試用 smoke。不要把這些當作真實工作效率樣本。

## 統計

```powershell
python "$HOME/.omp/agent/skills/omp-orchestrate/scripts/usage.py" summary
```

依樣本種類、任務類型、主模型與 inline／delegated 分組，顯示驗收結果、主控／子代理成本、各類 token 與缺漏。smoke 預設排除，可加 `--include-smoke`。重複 response IDs 全域去重；跨樣本共享呼叫會標 shared_calls，不能據此比較每組效率。沒有成本資料的呼叫另列 missing_cost_calls；數字是已知成本合計，不是帳單保證。

改資料位置時，在 collect／summary 前都加 `--data-dir "資料夾"`。原始 session 不會因收集被修改。

## 如何判斷划算

累積同類、相近範圍及驗收標準的 Sol-inline 與 Sol＋Luna 真實樣本；比較 accepted 比例、整個嘗試群組含失敗的花費，以及主控／子代理成本。不要只比較成功案例、便宜的子代理部分或混合任務。重試 session 必須一併看，必要時人工配對。

資料增加能顯示實際用量與派工開銷，但**樣本多不等於因果證明**：不同任務難度、effort、快取與策略選擇會影響結果。沒有 Sol-only 對照就不能說已省下多少；API 估價也不能當作訂閱扣額。此工具不會執行模型、不產生虛構 baseline，也不自動判定成功或推薦勝出模型。
