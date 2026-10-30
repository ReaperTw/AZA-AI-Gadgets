# Runtime exceptions

Consult this reference when discovery, routing or nesting differs from the requested workflow. The live schema and observed results outrank these notes.

## Discovery

Skills are discovered at startup. Restart omp after installing this skill so its metadata and `/skill:AZA-Omp-Orchestrate` command are available. Task execution rediscovers agent files, so a newly installed agent can resolve before the tool description lists it. An unknown agent error is a discovery failure, not permission to substitute another model.

Same-named project `.omp/agents/*.md` definitions take precedence over user `~/.omp/agent/agents/*.md`. On first use in a project or when routing/behavior is unexpected, check the effective definition/source, including `agentSource` in task metadata when available. Matching model identity alone does not prove the updated role contract was loaded. If source evidence is unavailable, report it as unverified rather than declaring the new contract active.

## Routing

Native agent frontmatter holds requested models. `task.agentModelOverrides` and extension routing hooks can supersede it. Ordinary task items select `agent`; the task schema's `model` field is seance-only. Avoid repurposing seance or launching a nested CLI for worker selection.

Use task result metadata or persisted assistant-message `provider`/`model` fields to check the actual route; `history://<id>` can locate the transcript. A catalog entry is not an authentication or execution check. If a route fails or differs, preserve evidence and report the mismatch. Policy-selected delegation may fall back inline to the current Sol session; user-explicit models/roles or independent evaluations must be marked blocked instead of silently replaced. Changing an explicit requested allocation requires user approval. Finish unrelated reachable work.

Do not rewrite global settings to repair a skill invocation. The user can inspect `/agents` model overrides or choose an available selector; changing an agent's model is a frontmatter edit, not a skill-body edit.

## Depth and plan mode

The documented default recursion depth is two child levels, but this policy needs only direct Sol → worker/specialist dispatch. All supplied child roles are leaves. A shallower live limit means inline fallback only for policy-selected work; explicit-role requests remain blocked, not substituted. Do not launch nested CLIs or change settings to bypass the restriction.

OMP's actual read-only plan mode may restrict tools and agent spawn policy beyond this skill's planning-only contract. Respect the active schema; hidden custom agents mean inline planning for policy-selected work, or blocked for user-explicit role requests. Mark unexercised routes accurately. Do not change depth or plan-mode settings to bypass a restriction.

## Diagnostic experiments

Children skip mid-flight build/lint/tests/formatters unless assigned verification-only work. A diagnostic experiment additionally requires host permission and Sol's explicit command, scope and purpose; authorization is not blanket test permission or final acceptance. Never rerun a user-reported failure just to confirm it. If the host forbids an essential experiment, supply its evidence before handoff or bound the assignment to static diagnosis. Sol owns final integration checks and user-visible smoke.

## Sources

- `omp://task-agent-discovery.md`: discovery, precedence and agent frontmatter.
- `omp://tools/task.md`: task schema, depth and session artifacts.
- `omp://skills.md`: skill discovery and invocation.
