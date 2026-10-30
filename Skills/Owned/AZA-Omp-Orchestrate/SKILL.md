---
name: AZA-Omp-Orchestrate
description: Use for cost-aware Sol/Luna delegation in omp, with desktop-only Terra and exceptional Astra consultation.
---

# AZA-Omp-Orchestrate

Sol owns decisions, integration and acceptance. Delegate complete work, not repeated reasoning. Preserve planning-only scope; this skill does not switch models.

## 1. Choose once

Small or tightly coupled tasks stay inline. Before nontrivial settled work, identify one complete package and check:

- Concise scope, evidence, interfaces, writable files and independent acceptance.
- Sol can accept the result without repeating its implementation/investigation.
- Conservative added child + Sol handoff/review + rework cost is below avoided Sol work. Read `cost-policy.md` once per session for weights, estimates and explicit-model/high-impact risk exceptions; exceptions are not savings.

Give one sentence naming the work removed and acceptance, or the failed gate. Do not solve the package merely to estimate it, or fragment repetitive work into “tiny edits” to avoid assessing handoff.

For actionable work, read `usage-data.md` and begin an explicit task record before implementation; retain its task ID, decision reason and available execution settings. Attach actual worker transcripts to that task. Ordinary Q&A needs no task record; never invent boundaries for old work.

**Ready:** a gate fails → inline; all pass and host permits → actually call `task`, without asking the user to dispatch. A written assignment is not executed work.

## 2. Hand off

Default: at most one active child; parallelism requires an explicit user request and independent packages. All roles are leaves, not a review ladder:

| Agent | Eligible work / required result |
| --- | --- |
| `omp-luna` | Settled ordinary work → complete artifact and evidence |
| `omp-terra` | Native desktop screenshots/AX/mouse/keyboard only → action plus fresh visual/AX evidence. Child computer capability and task-scoped approval required; no general coding, CLI debugging or DOM/CDP-only browsing |
| `omp-astra` | Unresolved consequential architecture/interface/data-model choice → one read-only decision, invariants and tradeoff |

Roles are contracts, not proven capability rankings. Missing facts require evidence. Desktop eligibility is not permission for consequential actions; retain point-of-risk confirmation.

Set `agent` inside the task item, shared invariants in `context`, bounded output/evidence paths/files/exclusions/acceptance in `task`, actual uncertainty in `solutionSpace`. Children lack conversation history; send relevant evidence, not full histories or repeated plans. One integration owner; Sol does different work, not the child's implementation.

**Handed off:** actual task result/agent ID exists. Reuse that child for bounded follow-up; consume delivered results and wait only when blocked.

## 3. Resolve or stop

Continue a package only with new evidence, a resolved contract question or a testable new hypothesis. An unchanged blocker stops that delegation path: no repeated wakeups or model swaps. Clarify, take work back into Sol, or choose one eligible specialist; no automatic escalation chain.

For discovery, model mismatch, depth/plan-mode restrictions or diagnostic experiments, read `runtime.md`. Check effective role source on first project use or unexpected behavior. Policy-selected work may fall back to Sol; user-explicit roles/models or independent reviews must be blocked rather than silently substituted.

**Resolved:** a usable result or new action; otherwise name the missing prerequisite and stop the affected path.

## 4. Accept and record

Inspect artifacts and changed behavior, not a second implementation. Follow host verification rules; Sol owns integration checks and user-visible smoke. Avoid unchanged duplicate checks. Child completion alone is not acceptance.

**Complete:** every required deliverable/check passed. **Blocked:** name the unaccepted work/check, prerequisite and next action; finish independent reachable work. If coordination/rework erases the benefit, stop spawning.

Return outcome, observed verification and blockers briefly. If delegated, include child ID and meaningful result; observed model comes from runtime metadata or is unverified. No routing report for small inline work.

After observed acceptance or a blocker, close the task with its outcome and a non-sensitive evidence reference using `scripts/tasks.py`; keep rework on the same task ID. Refresh the current session with `scripts/usage.py collect SESSION`; use incremental `collect --scan` for recovery or when the exact source is unavailable. Resolve script paths against this skill directory. Report unavailable collection, never infer acceptance or substitute whole-session totals for task costs. `usage-data.md` owns commands, privacy, boundary and comparison limits.

## Provenance

Adapted from [orchestrate-models](https://github.com/fdarkaou/agent-skills/blob/main/skills/fdarkaou/orchestrate-models/SKILL.md). See `LICENSE`.
