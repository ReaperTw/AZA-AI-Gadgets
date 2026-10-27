# Harness adapters

Canonical source: this skill directory (`SKILL.md` + `agents/` + `scripts/`). Do not copy the tree. Junction or install the folder.

The body is harness-agnostic. Product files only add discovery UI, not a second workflow.

## Local install (this machine)

From the skill directory:

```bash
python scripts/link_harnesses.py
```

The script junctions the canonical folder into each detected user skill root. It never overwrites a real (non-link) directory. Re-run after adding a harness.

Hermes skill index is frozen for the current session. Start a new chat to see `bounded-delivery` in the prompt; `skill_view(name="bounded-delivery")` works immediately.

One scanner, one junction. Cursor also reads `~/.agents/skills` and `~/.codex/skills`. Do not also junction `~/.cursor/skills` or Cursor loads the same skill twice. Hermes native path is `$HERMES_HOME/skills/bounded-delivery`; do not also put it in `codex-imports/`.

## Shared root (broadest coverage)

| Path | Who reads it |
|---|---|
| `~/.agents/skills/bounded-delivery/` | Codex, Cursor, Copilot, Amp, Gemini CLI, OpenCode (fallback), Command Code (compat), Devin Desktop, many others |

Prefer this path when a tool documents Agent Skills / `.agents/skills` support.

## Native skill roots

| Harness | User-level path | Invoke |
|---|---|---|
| Hermes Agent | `%LOCALAPPDATA%/hermes/skills/bounded-delivery/` (or `$HERMES_HOME/skills/`) | `skill_view` / `/bounded-delivery` |
| Codex | `~/.codex/skills/bounded-delivery/` | `$bounded-delivery` |
| Cursor | `~/.cursor/skills/bounded-delivery/` | `/bounded-delivery` (also reads `.agents`, `.claude`, `.codex`) |
| OpenCode | `~/.config/opencode/skills/bounded-delivery/` | native `skill` tool (also reads `.agents`, `.claude`) |
| Command Code | `~/.commandcode/skills/bounded-delivery/` | `/bounded-delivery` (`cmd skills add …`) |
| Claude Code | `~/.claude/skills/bounded-delivery/` | `/bounded-delivery` |
| Gemini CLI | `~/.gemini/skills/bounded-delivery/` | `activate_skill` (`.agents/skills` also native) |
| Grok Build | `~/.grok/skills/bounded-delivery/` | skill name / slash, per Grok UI |
| GitHub Copilot | `~/.copilot/skills/bounded-delivery/` or project `.github/skills/` | Copilot skills discovery |

Project-level equivalents (same folder name) when the team wants the skill in-repo:

- `.agents/skills/bounded-delivery/`
- `.cursor/skills/bounded-delivery/`
- `.opencode/skills/bounded-delivery/`
- `.commandcode/skills/bounded-delivery/`
- `.claude/skills/bounded-delivery/`
- `.hermes/skills/bounded-delivery/`
- `.codex/skills/bounded-delivery/`
- `.gemini/skills/bounded-delivery/`

## Product extras in this folder

| File | Harness |
|---|---|
| `agents/openai.yaml` | Codex / OpenAI skill UI (`display_name`, default `$bounded-delivery` prompt, implicit invocation) |
| `adapters/cursor.md` | Cursor discovery and invoke notes. Not a second `SKILL.md`. |
| `adapters/opencode.md` | OpenCode discovery and invoke notes. Not a second `SKILL.md`. |

No second instruction body. Every harness loads root `SKILL.md`.

## Other harnesses

If a client implements [Agent Skills](https://agentskills.io/specification):

1. Put this directory where that client scans for `*/SKILL.md`.
2. Keep `name: bounded-delivery` matching the folder name.
3. Do not rewrite the four-step contract for that product.

If it only accepts a rule / system prompt (Aider, some IDEs): point it at `SKILL.md` or paste the body. The contract is the file.

## Do not

- Copy files into each harness. Junction or one shared `.agents/skills` install.
- Point Hermes `skills.external_dirs` at `~/.codex/skills` (loads Codex `.system`).
- Duplicate the workflow into `.cursorrules`, `CLAUDE.md`, or `AGENTS.md`. Those stay pointers, not forks.
