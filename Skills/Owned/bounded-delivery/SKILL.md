---
name: bounded-delivery
description: Bound coding work to a minimum sufficient scope contract and proof budget. Use when the user requests an implementation, bug fix, refactor, or code change without explicit acceptance boundaries; leaves testing unspecified; or reports over-testing, scope creep, overbuilding, or work that never stops.
license: MIT
compatibility: Any Agent Skills client (Hermes, Codex, Cursor, OpenCode, Command Code, Claude Code, Gemini CLI, Grok, Copilot, and others).
metadata:
  author: Azazel
  version: "1.1.0"
  standard: agentskills.io
---

# Bounded Delivery

Deliver the requested outcome, prove it once, then stop.

This skill owns the **scope contract** and **proof budget**. If Ponytail is also loaded, Ponytail chooses the smallest implementation; this skill still decides Outcome, Surface, Proof, and Stop.

Install paths: [references/harnesses.md](references/harnesses.md). Cursor / OpenCode notes: [adapters/cursor.md](adapters/cursor.md), [adapters/opencode.md](adapters/opencode.md). Load those only when installing or debugging discovery.

## When not to use

- The user, repo, or an active workflow already requires TDD or a full suite: honor that proof, then apply this skill's stop rule.
- Planning, spec, or interview work with no code change.
- Diagnosis-only work (root cause, hang, deploy): stop on the cause, not on a delivery contract.
- Large migration, multi-session, or multi-agent work: use a hard allowlist and file budget. This skill alone is not that governor.

## 1. Form the scope contract

Before changing files, reduce the request to four items:

- **Outcome:** the observable result the user asked for.
- **Surface:** the smallest files or components reasonably needed.
- **Proof:** the cheapest reliable evidence that the outcome works.
- **Stop:** the condition after which control returns to the user.

Preserve every explicit requirement. When the user leaves a boundary unstated:

- Choose the smallest useful interpretation consistent with the request.
- Include only direct prerequisites needed for the outcome.
- Place adjacent cleanup, generalization, documentation, hardening, and unrelated defects outside the current contract.
- Ask one focused question only when competing interpretations would materially change behavior, data, security, external state, or effort. Otherwise state the inferred boundary in one sentence and proceed.

Complete this step when the outcome and stop condition are checkable.

## 2. Set the proof budget

Treat tests as evidence, not an automatic deliverable.

- Honor tests or TDD when the user, repository rules, or an active workflow requires them.
- Otherwise prefer one existing directly relevant test, reproduction, smoke check, build check, or static check.
- Add a new test only when it is required, protects a high-risk invariant, or no cheaper deterministic proof can establish a materially regression-prone change.
- Default to one strongest check. After that check, expand at most twice, and only after a failure, unstable result, broad or high-risk impact, or an explicit requirement.
- If two expansions add no new failure and no new signal, stop. Report the last evidence. Do not keep checking to be sure.
- Keep proof commands confined to the outcome and surface. Treat files absent from the edit set as preserved unless the editing tool reports collateral changes.
- Run the planned decisive check first. When it passes, verification is complete; proceed directly to the report.

Complete this step when one decisive check passes, or when the exact reason verification is `NOT RUN` is known.

## 3. Execute inside the contract

- Inspect only enough context to make the scoped change safely.
- Make the smallest coherent change that delivers the outcome.
- If removing a diff still delivers the outcome, do not make it.
- Include a newly discovered direct prerequisite when it remains local and necessary.
- Request authorization before a material expansion of files, behavior, dependencies, architecture, or deliverables. A fourth production file that is not the proof itself is a material expansion.
- Preserve unrelated user changes and existing failures outside the contract.

Complete this step when every edit maps directly to the outcome or its proof.

## 4. Stop at done

Stop when all are true:

1. The requested observable outcome exists.
2. The proof budget is satisfied or precisely reported as `NOT RUN`.
3. No explicit requirement remains inside the scope contract.

After the proof passes, additional tests, refactors, cleanup, documentation, and hardening require a new observed failure or explicit scope. Return control immediately. Mention an unexecuted follow-up only when it exposes a material risk or blocker.

Report only:

- **Done:** the delivered outcome.
- **Evidence:** the command or observation and result.
- **Outside contract:** a material unresolved item, only when one exists.

## Pitfalls

- Prompt discipline, not a runtime kill switch. If this skill is not loaded, it does nothing.
- `high-risk` and `cheapest reliable` are model judgements. When security, data, or external state is involved, expand the proof.
- One check can miss cross-module damage. If the edit set spans a shared interface, the decisive check must exercise that interface.
