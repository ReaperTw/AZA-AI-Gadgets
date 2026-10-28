---
name: omp-orchestrate
description: Cost-aware work sharing in omp. Use when Sol should retain judgment while delegating complete, bounded work to Luna without agent fan-out or duplicate work.
---

# OMP Orchestrate

Sol steers; Luna executes work that can genuinely leave Sol's workload. Optimize completed-task cost and correctness against Sol working alone, not worker count or raw speed.

## 1. Choose whether to delegate

Use the current Sol main session for scope, decisions, integration and acceptance. This skill cannot switch models; report the actual model and follow `README.md` to select Sol if needed. Preserve planning-only versus implementation scope.

Default to no child. Sol handles small or tightly coupled tasks inline. Delegate to `omp-luna` only when all hold:

- A substantial package can produce a complete, independently checkable result.
- Scope, evidence, interfaces and file ownership can be handed over concisely.
- Sol can accept the result without redoing the same investigation or implementation.
- Avoided Sol work plausibly exceeds handoff, child context, extra review and rework.

Sol specifies enough to bound the result, not a full solution followed by a worker copying it. Task size alone does not justify delegation. Read `cost-policy.md` when the economic choice is unclear; choose inline execution when no advantage is identifiable. Once all four gates hold and host policy permits delegation, actually invoke `task` without asking the user to dispatch it. Writing a worker assignment in a plan is not execution. A planning-only request may legitimately stop with the requested plan.

**Ready:** for nontrivial settled work, identify a complete remaining package once before implementation. In one sentence, say what leaves Sol and how it is accepted, or which handoff gate fails if kept inline. Small tasks need no report; do not disguise a substantial repetitive package as unrelated tiny edits.

## 2. Hand off once

Default to at most one active child in total and obey the host's delegation gates. Use parallel children only when the user explicitly requests parallelism and independent packages justify it. A specialist is an alternative to the worker, not another mandatory layer.

Route by the work's remaining uncertainty:

| Agent | Input condition | Owned output | Outside its role |
| --- | --- | --- | --- |
| `omp-luna` | Requirements and interface are settled; ordinary implementation/planning remains | Complete bounded artifact, changes and acceptance evidence | Architecture decisions and broad unresolved technical exploration |
| `omp-terra` | Implementation has a named technical uncertainty, such as a reproducible race, failed algorithm or contained technical integration; the package still meets the economic handoff gate | Implemented technical package or root-cause evidence and a targeted next experiment | Team supervision and redoing Sol's whole plan |
| `omp-astra` | Existing contracts do not settle a consequential cross-module interface, data-model or irreversible architecture choice | One selected decision with interfaces, invariants, tradeoff and acceptance | Implementation, routine code review and general status reporting |

These roles express work contracts, not benchmark-proven model rankings. Choose one appropriate child, not all three. If its required facts are missing, gather them rather than assuming a more expensive model can infer them.

Select `agent` inside a task item; shared `context` carries only relevant invariants, while `task` states the result, evidence paths, writable files, exclusions and acceptance. `solutionSpace` describes uncertainty. Children do not inherit the conversation; pass concise evidence, not repeated plans or the entire history.

Use the same child for bounded follow-up rather than spawning a replacement for each small edit. Sol works on genuinely different decisions or integration needs while the child runs; it does not implement the child's package in parallel. Consume auto-delivered results and wait only when blocked.

**Ready:** the child owns a complete package with one integration owner; Sol's work does not duplicate it.

## 3. Resolve blockers without building a ladder

When a worker is blocked, inspect the evidence and choose one action: clarify the contract for that worker, take the package back into Sol, or consult one necessary specialist. A failed attempt is not an automatic Luna → Terra → Sol → Astra pipeline.

Before any follow-up on the same package, identify new evidence, a resolved contract question or a testable new hypothesis. If the same blocker has no information gain, stop that delegation path; do not wake the child or swap models to repeat it. Sol may take back work it can finish; missing external prerequisites mean blocked.

Select any specialist using the same economic gate and role contracts above. Sol may route an uncertain technical package directly to Terra or a high-impact architecture decision directly to Astra; requiring a failed Luna run first would pay for an unnecessary attempt.

Specialists return directly to Sol and do not dispatch more agents. Avoid routine specialist review, recurring status reports and repeated plans. Missing facts require evidence, not merely a more expensive model.

For model/discovery failures or depth restrictions, read `runtime.md`. Native definitions in `~/.omp/agent/agents/` own bindings; requested identities are not proof of the resolved model.

**Resolved:** control returns to Sol with an accepted result, a targeted next action or an explicit blocker.

## 4. Accept once and finish

Inspect the returned artifact and relevant behavior, not a second independent implementation. Follow the host's verification schedule: children skip mid-flight build/lint/tests/formatters unless assigned verification-only work. A technical package may include a named diagnostic experiment only when host policy permits it and Sol explicitly authorizes its command, scope and purpose; this is not blanket test permission or final acceptance. Do not rerun a user-reported failure merely to confirm it. If host policy forbids the necessary experiment, supply its evidence before handoff or explicitly limit the package to static diagnosis. Sol owns post-integration checks and user-visible smoke; avoid unchanged duplicate checks.

Return completed behavior or requested planning decisions, observed verification and blockers. If a child ran, give its returned ID, meaningful outcome and observed model from runtime metadata, or mark the model unverified. A claimed handoff requires an actual task result/agent ID. Policy-selected delegation may fall back to Sol when blocked; a user-explicit role/model or independent evaluation may not be silently substituted. Mark that requested part blocked and finish independent reachable work. Small inline tasks need no routing report.

**Complete:** all required deliverables and acceptance checks have passed. Child completion alone is not final acceptance.

**Blocked:** a required deliverable or check cannot be completed; name what remains unaccepted, the missing prerequisite and next action. This stops the affected path, not successful completion. If delegation adds coordination or rework without removing Sol work, stop spawning and finish reachable work in Sol.

## Provenance

Adapted from [fdarkaou/agent-skills: orchestrate-models](https://github.com/fdarkaou/agent-skills/blob/main/skills/fdarkaou/orchestrate-models/SKILL.md) for omp-native routing and the user's four-role policy. See `LICENSE`.
