# Price-weighted handoff

Read once when assessing a nontrivial package or specialist; reuse these rates within the session. This is an API-cost proxy, not a capability score, subscription quota conversion or enforced spending limit.

## Price evidence

Snapshot from `omp models find gpt-6 --json`, provider `openai-codex`, 2026-10-28. USD per million tokens; omp catalog estimates, not an account invoice. Re-query if models/prices change; do not fetch prices for every routine task.

| Model | Uncached input | Output | Cached input |
| --- | ---: | ---: | ---: |
| GPT-6 Luna | 0.10 | 0.50 | 0.01 |
| GPT-6.1 Terra | 1.00 | 5.00 | 0.05 |
| GPT-6.1 Sol | 2.00 | 10.00 | 0.10 |
| GPT-6 Astra | 10.00 | 50.00 | 1.00 |

## Weights relative to Sol

| Model | Fresh input weight | Output weight | Cache-read weight |
| --- | ---: | ---: | ---: |
| Luna | 0.05 | 0.05 | 0.10 |
| Terra | 0.50 | 0.50 | 0.50 |
| Sol | 1.00 | 1.00 | 1.00 |
| Astra | 5.00 | 5.00 | 10.00 |

Each column is relative to Sol's price for that category, not interchangeable token units. Use the price table to combine categories:

`cost(model, U, C, O) = (input_price * U + cache_price * C + output_price * O) / 1_000_000`

`U` is uncached input, `C` cache-read input, `O` billable output including reasoning when the provider reports it that way. U and C are disjoint. Include every request, tool-result/context replay and child startup; use the effective tier/long-context rates if they differ from this standard-rate snapshot. Refresh rates when routing, pricing or tier changes, not on each tiny edit.

## Numeric dispatch gate

For the same required accepted result, estimate only the marginal work:

- `S`: Sol cost actually avoided by handing off this package. Exclude sunk analysis, retained management work and prefix reads that still occur.
- `D`: all child request costs, including startup and rereads.
- `H`: additional Sol handoff, returned-artifact review, repeated context and any extra verification caused by delegation. Exclude unchanged checks required on both paths.
- `R`: additional retry/repair costs. State the bounded repair assumption or use observed comparable work; price alone supplies no failure probability.

`ratio = (D + H + R) / S`

Use a brief token estimate or range from available context size, artifact size and comparable work; label it estimated. Do not solve the package to estimate it or invent precise success probabilities. If cache reuse is uncertain, price child input as fresh and retained Sol context at its known rate; missing cache evidence is not proof of a hit.

Dispatch only when all scope/acceptance gates hold and the conservative ratio is below 1: `(D_high + H_high + R_high) < S_low`. Equality, `S <= 0`, or overlapping ranges do not establish savings: keep it inline and identify that failed gate. No arbitrary model priority may override the comparison. A new full plan or review chain must be included in H, not treated as free.

For a nontrivial settled package, give one short estimate such as `Luna: D+H+R=$0.0168 vs avoided Sol=$0.0400; ratio=0.42 (estimated)`, or the gate that failed. Small inline work needs no calculation/report. These are routing estimates, not actual bill reductions.

## Worked example and limits

Illustrative standard-rate counts, not measured productivity: avoiding Sol's 10k fresh input + 2k output saves $0.0400. Luna using 16k fresh input + 2.4k output costs $0.0028. Extra Sol handoff/review using 2k fresh + 20k cached input + 300 output costs $0.0090. Reserving one additional Sol repair of 1k fresh + 300 output adds $0.0050. Total is $0.0168, ratio 0.42, if these upper estimates and the avoided-work lower estimate are credible.

Luna is not always cheaper: extra Sol work can consume the entire saving. Terra must pass the same gate despite being half Sol's per-token price. Astra's higher price needs sufficiently less total work or a separately stated high-impact quality/risk reason; neither model name nor price proves that advantage.

A user-explicit model request takes priority over cost optimization. A consequential risk may justify a consultation that is not cheaper; name that reason and do not label it cost-saving. Never trade away required acceptance to pass the price gate. Keep the one-active-child and information-gain stop rules; no automatic retry ladder.

Subscription limits are a separate metric. Use documented model-specific quota charges or account usage deltas only if available; do not convert API dollar weights into Plus/Pro quota multipliers. No such verified conversion is configured here. These weights and estimates are prompt guidance, not runtime metering or a benchmark proving superiority over Sol alone.
