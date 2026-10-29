# Cursor

Install: do **not** junction to `~/.cursor/skills/` if `~/.agents/skills` or `~/.codex/skills` already point here. Cursor reads those too; a third link duplicates the skill.

Prefer `~/.agents/skills/AZA-Bounded-Delivery` as the Cursor-visible install.

## Invoke

- User names `AZA-Bounded-Delivery`, or asks to bound scope / stop over-testing.
- Model-invoked from the `description` in `SKILL.md`.
- Optional slash: put a one-line command in the project `.cursor/commands/AZA-Bounded-Delivery.md` that says `Follow the AZA-Bounded-Delivery skill.` Do not paste the contract into that command.

## Extra Cursor fields

If a future Cursor-only switch is needed (for example `paths:`), add it to the root `SKILL.md` frontmatter. Cursor ignores unknown keys. Do not create `adapters/cursor/SKILL.md`.
