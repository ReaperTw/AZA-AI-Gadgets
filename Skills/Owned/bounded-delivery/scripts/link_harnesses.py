"""Junction bounded-delivery into local Agent Skills roots. No copies."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

CANON = Path(__file__).resolve().parents[1]
NAME = "bounded-delivery"
HOME = Path.home()
LOCAL = Path(os.environ.get("LOCALAPPDATA", HOME / "AppData" / "Local"))
HERMES_HOME = Path(os.environ.get("HERMES_HOME", LOCAL / "hermes"))


def targets() -> list[tuple[str, Path]]:
    return [
        ("agents-shared", HOME / ".agents" / "skills" / NAME),
        ("codex", HOME / ".codex" / "skills" / NAME),
        ("cursor", HOME / ".cursor" / "skills" / NAME),
        ("opencode", HOME / ".config" / "opencode" / "skills" / NAME),
        ("command-code", HOME / ".commandcode" / "skills" / NAME),
        ("claude-code", HOME / ".claude" / "skills" / NAME),
        ("gemini", HOME / ".gemini" / "skills" / NAME),
        ("grok", HOME / ".grok" / "skills" / NAME),
        ("copilot", HOME / ".copilot" / "skills" / NAME),
        ("hermes", HERMES_HOME / "skills" / NAME),
    ]


def same(a: Path, b: Path) -> bool:
    try:
        return a.exists() and b.exists() and os.path.samefile(a, b)
    except OSError:
        return False


def is_reparse(path: Path) -> bool:
    if path.is_symlink():
        return True
    try:
        return bool(path.stat().st_file_attributes & stat_reparse())  # type: ignore[attr-defined]
    except (AttributeError, OSError):
        return False


def stat_reparse() -> int:
    return getattr(os.stat_result, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400)


def mklink_junction(dest: Path, src: Path) -> int:
    dest.parent.mkdir(parents=True, exist_ok=True)
    completed = subprocess.run(
        ["cmd", "/c", "mklink", "/J", str(dest), str(src)],
        capture_output=True,
        check=False,
    )
    return completed.returncode


def link_one(label: str, dest: Path) -> str:
    if dest.exists() or dest.is_symlink():
        if same(dest, CANON):
            return f"{label}: already linked"
        return f"{label}: skipped (exists, not this source) -> {dest}"
    code = mklink_junction(dest, CANON)
    if dest.exists() and same(dest, CANON):
        return f"{label}: linked -> {dest}"
    return f"{label}: FAILED rc={code} dest={dest}"


def main() -> int:
    skill = CANON / "SKILL.md"
    if not skill.is_file():
        print(f"missing {skill}", file=sys.stderr)
        return 1
    text = skill.read_text(encoding="utf-8")
    if "name: bounded-delivery" not in text:
        print("SKILL.md missing name: bounded-delivery", file=sys.stderr)
        return 1
    print(f"canonical: {CANON}")
    failed = 0
    for label, dest in targets():
        line = link_one(label, dest)
        print(line)
        if line.startswith(f"{label}: FAILED"):
            failed += 1
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
