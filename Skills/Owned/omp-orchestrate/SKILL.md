---
name: omp-orchestrate
description: Hierarchical planning and execution in omp. Use when the user requests Astra architecture, Sol management, Terra supervision, or Luna workers as a coordinated multi-model workflow.
---

# OMP Orchestrate

One manager owns the result. Architecture is a decision boundary, not a mandatory relay.

## 1. Establish ownership

Use the current Sol session as manager. Check its actual model: this skill supplies instructions, not a model switch. If the manager is not Sol, follow `README.md` to select it before claiming the requested allocation. For discovery failures, routing mismatches or depth restrictions, read `runtime.md`.

Native agent definitions in `~/.omp/agent/agents/` own the model bindings:

| Role | Agent | Authority |
| --- | --- | --- |
| Architect | `omp-astra` | Read-only architecture, interfaces and invariants |
| Manager | Current Sol session | Scope, dispatch, integration and final acceptance |
| Foreman | `omp-terra` | A bounded complex package and its worker outputs |
| Worker | `omp-luna` | A precisely specified slice |

Preserve the requested mode: planning ends with decisions and work packages; implementation continues through runnable behavior. This distinction does not enable omp's read-only plan mode.

**Ready:** the actual manager, requested mode and accountable owner are identified.

## 2. Shape contracts

Inspect enough context inline to find boundaries; use `scout` for genuinely unmapped codebase exploration under the host's delegation rules. Keep small or tightly coupled work inline.

Each useful work package needs a goal, owner, input evidence, writable files, exclusions, dependencies, interface/invariants, acceptance condition and verification scenario. Shared files have one integration owner.

Consult `omp-astra` only for an unresolved architecture or consequential cross-package tradeoff. Supply neutral evidence and require a selected design, its contract, a rejected alternative with a concrete tradeoff, risks and acceptance criteria. Sol adopts one authoritative contract before dependent execution starts; contract conflicts return to Sol.

**Ready:** every package has a bounded owner and checkable acceptance; dependencies form a DAG and required architecture decisions are settled.

## 3. Dispatch the shortest path

- Sol → Luna for independent precisely specified slices.
- Sol → Terra for independent complex packages; Terra implements tightly coupled work itself or delegates useful independent slices to Luna.
- Sol → Astra for architecture consultation, alongside rather than above the execution chain.

Respect the live depth limit. Sol → Terra → Luna uses two child levels; when nesting is unavailable, Terra returns slices for Sol to dispatch.

Batch independent slices in `tasks[]`. Set `agent` inside each item; ordinary task items use agent bindings, not a `model` override. Put shared contracts in `context`, slice requirements in `task`, and actual uncertainty in `solutionSpace`. Include the full relevant contract because children do not inherit the conversation; link large evidence through `local://`.

**Ready:** each started child has non-overlapping write ownership and a complete contract; every layer contributes a distinct responsibility.

## 4. Accept evidence

Work while children run and consume auto-delivered results. Use returned IDs with `write agent://<id>` for steering; `wait` only when otherwise blocked.

Require each child to return status (`complete` or `blocked`), completed scope, changes or none, actual evidence/commands, child IDs and blockers with next actions. Terra inspects worker artifacts against acceptance; Sol integrates across packages.

Follow the host's verification schedule: children skip build/lint/tests/formatters mid-flight; Sol runs relevant checks after integration and exercises the changed user-visible path. Assign child verification separately after editing has stopped.

**Accepted:** every required package meets its contract with observed evidence, or has a precise blocker and owner.

## 5. Deliver the requested artifact

Planning: decisions and dependency-aware work packages with ownership, acceptance checks and unresolved blockers. Execution: completed behavior, exercised verification and remaining blockers.

Include a compact routing record: role, returned agent ID, assignment and observed model, or `unverified` when metadata is unavailable. Model identity comes from task/session metadata, not an agent's self-description. Report only roles that actually ran.

**Complete:** the requested artifact covers every package; implementation claims have runtime evidence.

## Provenance

Adapted from [fdarkaou/agent-skills: orchestrate-models](https://github.com/fdarkaou/agent-skills/blob/main/skills/fdarkaou/orchestrate-models/SKILL.md) for omp-native routing and the user's four-role policy. See `LICENSE`.
