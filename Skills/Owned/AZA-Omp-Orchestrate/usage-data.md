# 本機用量資料

集中位置：`~/.omp/agent/orchestration-data/`。資料在公開 repository 外；不自動複製提示詞、回答、程式碼、專案路徑或憑證。任務分類、理由、證據是主控輸入的短標籤，請勿貼原始需求、敏感命令或測試輸出。原始 session 永不修改。

## 每項實際工作先建立任務

所有腳本路徑相對於這個 skill。`SESSION` 必須是目前原生 root-session JSONL 的完整路徑；從執行環境的 session ID 或 archive session 資訊取得，不依檔案修改時間猜測。不需要為一般問答建任務，也不額外呼叫模型分析對話。

```powershell
python scripts/tasks.py begin SESSION --task-kind parser --reason tightly-coupled --effort medium
```

記下輸出的 `task_id`。開始邊界預設是當下已持久化紀錄的結尾；若本次需求的 user event ID 可確認，使用 `--start-event EVENT_ID`，從該事件開始計算。不要把舊的整段對話補成一個新任務。派工理由用 `independent-package`、`tightly-coupled` 等短碼；這是決策理由，不是成本節省證明。

任務保存起始邊界、時間、分類、理由、主控宣告的 effort，以及開始時 SKILL、成本政策與收集腳本的內容 hash。每次模型呼叫另存實際模型、來源 session/event ID、時間、用途、輸入／輸出／快取 token、記錄成本及來源中可觀察的 effort。取不到的值維持未知；宣告的 effort 不冒充實際設定。

任務標記存於 `tasks/<task_id>.json`，與整段 session 快照分開。只允許同一 root 同時一個任務；不同任務不重疊。邊界包含來源 prefix hash；若原始紀錄被重寫、壓縮或截斷而無法核對，就拒絕重新歸屬，不猜測成本。

## 子代理與返工

實際派工後，把該代理的原生 transcript 明確掛到任務；有巢狀代理時也逐一掛上，不從時間接近或模型名稱推測關係：

```powershell
python scripts/tasks.py attach SESSION --task-id TASK_ID --child-session CHILD_JSONL
```

只接受該 root 原生 descendant 目錄內的紀錄；同一 worker 不可掛到不同任務。子代理可在同一任務內續作。缺少 transcript 的派工會標警告，不能視為完整測量。

整合與實際驗證完成後：

```powershell
python scripts/tasks.py end SESSION --task-id TASK_ID --outcome accepted --evidence parser-edge:passed
```

`outcome` 可用 accepted、blocked、failed、unknown。accepted 必須附非敏感的驗證參考，但程式不會替你證明測試真的通過；主控仍須實際觀察證據。必要驗收未跑就用 blocked／unknown，不因最後一句「完成」自動改成成功。

返工使用原 task ID，保留前次結果及證據，成本包含前次嘗試：

```powershell
python scripts/tasks.py resume SESSION --task-id TASK_ID
# 修復並驗證後再次 end
```

若中間已開始別的任務，拒絕跨越它的工作範圍 resume。跨 session 的重試仍需人工配對，不能據單次成功低估總成本。關閉時凍結 root 與已掛 worker 的終點；之後其他工作不會算入。結束命令之後的最終回覆等呼叫不在這份快照內，不能稱為整個互動的完整帳單。

## 查看任務與舊 session 資料

```powershell
python scripts/usage.py summary --tasks
python scripts/usage.py collect --scan
python scripts/usage.py summary
```

`--tasks` 只顯示明確記錄的任務，含觀察到的所有模型、主控／子代理估價、版本 hash、嘗試歷程、驗收與完整性警告。不和舊 session 合計，避免重複計費；未關閉的任務成本顯示 null，而不是假裝零成本。smoke 預設排除，加 `--include-smoke` 才納入。測試任務在 begin 使用 `--kind smoke`；混合任務用 `--kind mixed`。

舊 `summary` 仍是整段 session 的用量帳，不是任務效率比較。只要提過／讀過 skill，就可能被列入；inline 只表示沒有 task 子代理，仍可含 auto-thinking 等額外模型呼叫。既有 unknown／unclassified 標籤不會被自動變成 accepted／real。

`collect --scan` 保存 metadata-only 索引；來源大小、mtime、子代理檔案集合及收集器版本未變時跳過解析，來源改動或快照遺失則重建該份 session。索引不保存 transcript 內容或明文來源路徑。需要強制重讀時使用單一 session 命令：

```powershell
python scripts/usage.py collect SESSION
```

重新收集覆寫同一 session 快照、不重複累加，人工標籤保留。沒有來源的舊快照保留；無法恢復已刪除的紀錄。缺少成本維持缺漏，不當作零；fork／匯入 lineage 不作乾淨樣本。全量掃描是補資料工具，不是背景服務。

如需手動標記舊 session，可用 `collect SESSION --kind mixed --task-kind parser --outcome unknown`；無法確認任務邊界及驗收的舊紀錄維持未知。不要批量補成成功。

在所有命令前加 `--data-dir DIR` 可改資料目錄。快照使用 atomic replacement，但不是多寫入者資料庫；同一資料目錄的 begin／attach／end／resume／collect 應順序執行。

## 可以比較到哪裡

只比較同類、相近範圍、相同驗收標準和可核對執行條件的任務；納入失敗與返工，不只看成功樣本。`comparable_candidate` 只是已關閉、real、有結果與呼叫、無已知警告的初篩，還要核對 effort、模型、策略版本與範圍；不等於可直接互比。

成本是 omp 記錄的 API 估價，不是訂閱扣額或帳單保證。不從主控成本猜測交接開銷；沒有相近 Sol-only 對照就不宣稱省下多少。這些工具不執行模型、不產生虛構 baseline，也不自動推薦勝出模型。
