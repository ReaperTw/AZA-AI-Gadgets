# Compare against Sol alone

Read when deciding whether a complete package should leave the Sol main session, or whether a specialist adds value. Delegation is optional.

## Price evidence

Snapshot from `omp models find gpt-6 --json`, provider `openai-codex`, 2026-10-28. USD per million tokens; omp catalog estimates, not an account invoice. Re-query if models/prices change; do not fetch prices for every routine task.

| Model | Uncached input | Output | Cached input |
| --- | ---: | ---: | ---: |
| GPT-6 Luna | 0.10 | 0.50 | 0.01 |
| GPT-6.1 Terra | 1.00 | 5.00 | 0.05 |
| GPT-6.1 Sol | 2.00 | 10.00 | 0.10 |
| GPT-6 Astra | 10.00 | 50.00 | 1.00 |

Sol is twice Terra on each listed token category. Terra is ten times Luna on fresh input/output, but five times on cached input; Sol is twenty times/fresh and ten times/cached. Account for the actual mix, not just input price.

## Completed-task economics

Count the main session, every child startup/context, uncached and cached input, output (including billable reasoning where applicable), handoff summaries, rework and final verification. Compare the same accepted outcome with Sol doing the task alone.

Delegate only when the Sol work removed is plausibly worth more than the child's work plus additional handoff, review and rework. Sol fully solving the package and then asking Luna to repeat it creates cost rather than savings. Many cheap workers can still cost more and fail to deliver the result.

Luna is much cheaper per token, so complete execution packages are the useful target. This does not imply tiny edits need a worker, that more parallel workers are better, or that Sol should transfer every difficult decision away.

Sol is twice Terra for the same token mix. That price difference alone does not justify a Terra management layer: Sol is already the main session, so adding Terra pays for another context and handoff. Use Terra only for a specific technical package or blocker that genuinely removes Sol work; Astra only for a consequential architecture decision worth its additional cost.

For an isolated choice between Terra and Sol at identical token mix and success quality, Sol would need less than half Terra's tokens to be cheaper. This is a break-even condition, not evidence that either model is more capable. There is no same-task benchmark here proving a specialist improves success enough to pay for itself.

Default to one active child, reuse it for bounded follow-up, and stop the delegation path if repeated clarification or duplicated work erases the advantage. Keep the finish criterion unchanged. No fixed savings percentage or automated spending cap is enforced by this prompt-only policy.
