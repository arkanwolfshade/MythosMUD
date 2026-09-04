#!/usr/bin/env python3
"""
Claude Code Stop hook: prompt for test creation when non-test source files were edited.

Reads .claude/hooks/state/edited-files.json for this session_id.
If any non-test files were recorded (by record_edited_file.py), blocks the stop and
continues the conversation with a test-creation prompt. Clears state for this session.

Ported from .cursor/hooks/trigger_test_agent.py; adapted to Claude Code's Stop hook
schema: session_id instead of conversation_id.

Blocking mechanism: emits {"decision": "block", "reason": ...} on stdout AND exits
with code 2. `decision: "block"` was empirically confirmed working (live-verified this
repo, single clean block, no double-fire — see git history for the verification note);
exit code 2 is the unambiguously-documented blocking mechanism per
code.claude.com/docs/en/hooks, independent of any JSON `decision` field. Emitting both
is a deliberate belt-and-braces choice since a silent regression here (stops blocking,
or double-fires) would be very hard to notice without dedicated hook tests.

Loop safety is state-derived, not read from hook input: `state.pop(session_id, [])`
below empties this session's entry and writes it back *before* blocking, so a second
Stop in the same turn finds no files recorded and allows the stop on its own. (A real
`stop_hook_active` field IS present on the Stop hook's input payload, confirmed via live
test — but this script doesn't need to read it, since idempotency is already guaranteed
by the pop-then-write above.) Claude Code also force-ends the turn after 8 consecutive
Stop-hook blocks regardless, as a hard backstop.
"""

from __future__ import annotations

import json
import os
import sys
import tempfile
from pathlib import Path
from typing import NoReturn, cast

FOLLOWUP_MESSAGE = (
    "Create or update unit tests for the non-test source files you modified in this "
    "conversation. Follow the mythosmud-test-writing skill: server tests in "
    "server/tests/unit|integration, client tests in __tests__ or *.test.*. Run make test "
    "from project root to verify. If you only edited test files or fixtures, respond "
    "briefly that no action is needed."
)

MAX_TRACKED_SESSIONS = 20


def _exit_empty() -> NoReturn:
    """Exit successfully with no decision (allow the stop)."""
    sys.exit(0)


def _load_state(state_file: Path) -> dict[str, list[str]] | None:
    """Load and validate edited-files state. Returns None if missing or invalid."""
    if not state_file.exists():
        return None
    try:
        state = json.loads(state_file.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None
    return cast(dict[str, list[str]], state) if isinstance(state, dict) else None


def _write_state_atomic(state_dir: Path, state_file: Path, state: dict[str, list[str]]) -> None:
    """Write state via a same-directory temp file + os.replace. See record_edited_file.py
    for the matching helper and rationale (no locking; a lost update just re-prompts later)."""
    if len(state) > MAX_TRACKED_SESSIONS:
        for stale_key in list(state.keys())[: len(state) - MAX_TRACKED_SESSIONS]:
            del state[stale_key]
    try:
        state_dir.mkdir(parents=True, exist_ok=True)
        fd, tmp_path = tempfile.mkstemp(dir=state_dir, prefix=".edited-files-", suffix=".tmp")
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as f:
                json.dump(state, f, indent=2)
            os.replace(tmp_path, state_file)
        except OSError:
            Path(tmp_path).unlink(missing_ok=True)
            raise
    except OSError:
        pass  # fail open


def main() -> None:
    """
    Entry point: read hook payload from stdin, check edited-files state, and optionally
    block the stop with a follow-up test-creation prompt.
    """
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, UnicodeDecodeError, OSError):
        _exit_empty()

    session_id = payload.get("session_id")
    cwd = payload.get("cwd", ".")

    if not session_id:
        _exit_empty()

    state_dir = Path(cwd or ".") / ".claude" / "hooks" / "state"
    state_file = state_dir / "edited-files.json"
    state = _load_state(state_file)
    if state is None:
        _exit_empty()

    files = state.pop(session_id, [])
    if not files:
        # Write back state (in case we popped nothing but other sessions exist)
        _write_state_atomic(state_dir, state_file, state)
        _exit_empty()

    # Persist updated state (removed this session) before blocking
    _write_state_atomic(state_dir, state_file, state)

    print(json.dumps({"decision": "block", "reason": FOLLOWUP_MESSAGE}), end="")
    sys.exit(2)


if __name__ == "__main__":
    main()
