# OpenCode

Install: junction this skill folder to `~/.config/opencode/skills/bounded-delivery`.

OpenCode also reads `~/.agents/skills/` and `~/.claude/skills/`. It does not read `~/.codex/skills/`. Prefer the OpenCode path or `.agents`. One junction is enough.

## Invoke

- Native skill tool, id `bounded-delivery` (from the folder name).
- Frontmatter `name` must stay `bounded-delivery` and match the folder.
- User can also name the skill in chat.

## Extra OpenCode fields

OpenCode recognizes `name`, `description`, `license`, `compatibility`, `metadata`. Unknown keys are ignored. Keep extras in `metadata` if they are ever needed. Do not create `adapters/opencode/SKILL.md`.
