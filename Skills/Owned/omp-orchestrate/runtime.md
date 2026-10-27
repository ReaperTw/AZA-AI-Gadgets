# Runtime exceptions

Consult this reference when discovery, routing or nesting differs from the requested workflow. The live schema and observed results outrank these notes.

## Discovery

Skills are discovered at startup. Restart omp after installing this skill so its metadata and `/skill:omp-orchestrate` command are available. Task execution rediscovers agent files, so a newly installed agent can resolve before the tool description lists it. An unknown agent error is a discovery failure, not permission to substitute another model.

## Routing

Native agent frontmatter holds requested models. `task.agentModelOverrides` and extension routing hooks can supersede it. Ordinary task items select `agent`; the task schema's `model` field is seance-only. Avoid repurposing seance or launching a nested CLI for worker selection.

Use task result metadata or persisted assistant-message `provider`/`model` fields to check the actual route; `history://<id>` can locate the transcript. A catalog entry is not an authentication or execution check. If a role fails or resolves to another model, preserve its evidence, finish independent reachable work and report the exact mismatch. Changing the requested allocation requires user approval.

Do not rewrite global settings to repair a skill invocation. The user can inspect `/agents` model overrides or choose an available selector; changing an agent's model is a frontmatter edit, not a skill-body edit.

## Depth and plan mode

The documented default recursion depth is two child levels, enough for Sol → Terra → Luna. A lower live limit requires flattened dispatch through Sol. A foreman without child tools returns a decomposition, not imaginary worker results.

OMP's actual read-only plan mode may restrict tools and agent spawn policy beyond this skill's planning-only contract. Respect the active schema; if it hides custom agents, plan inline and explicitly mark those routes as unexercised. Do not change depth or plan-mode settings to bypass a restriction.

## Sources

- `omp://task-agent-discovery.md`: discovery, precedence and agent frontmatter.
- `omp://tools/task.md`: task schema, depth and session artifacts.
- `omp://skills.md`: skill discovery and invocation.
