#!/usr/bin/env python3
"""
Claude Code Stop hook: prompt for test creation when non-test source files were edited.

Reads .claude/hooks/state/edited-files.json for this session_id.
If any non-test files were recorded (by record_edited_file.py), returns
{"decision": "block", "reason": ...} to block the stop and continue the conversation
with a test-creation prompt. Clears state for this session.

Ported from .cursor/hooks/trigger_test_agent.py; adapted to Claude Code's Stop hook
schema: session_id instead of conversation_id, stop_hook_active instead of loop_count
(guards against re-triggering when this hook itself caused the previous stop to be
blocked), and {"decision": "block", "reason": ...} instead of {"followup_message": ...}.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import NoReturn, cast

FOLLOWUP_MESSAGE = (
    "Create or update unit tests for the non-test source files you modified in this "
    "conversation. Follow the mythosmud-test-writing skill: server tests in "
    "server/tests/unit|integration, client tests in __tests__ or *.test.*. Run make test "
    "from project root to verify. If you only edited test files or fixtures, respond "
    "briefly that no action is needed."
)


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


def main() -> None:
    """
    Entry point: read hook payload from stdin, check edited-files state, and optionally
    block the stop with a follow-up test-creation prompt.
    """
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        _exit_empty()

    session_id = payload.get("session_id")
    # stop_hook_active is true if Claude is already continuing because a Stop hook
    # blocked once before in this turn — never block a second time, or this loops forever.
    stop_hook_active = payload.get("stop_hook_active", False)
    cwd = payload.get("cwd", ".")

    if not session_id or stop_hook_active:
        _exit_empty()

    state_dir = Path(cwd or ".") / ".claude" / "hooks" / "state"
    state_file = state_dir / "edited-files.json"
    state = _load_state(state_file)
    if state is None:
        _exit_empty()

    files = state.pop(session_id, [])
    if not files:
        # Write back state (in case we popped nothing but other sessions exist)
        state_file.write_text(json.dumps(state, indent=2), encoding="utf-8")
        _exit_empty()

    # Persist updated state (removed this session)
    state_dir.mkdir(parents=True, exist_ok=True)
    state_file.write_text(json.dumps(state, indent=2), encoding="utf-8")

    print(json.dumps({"decision": "block", "reason": FOLLOWUP_MESSAGE}), end="")
    sys.exit(0)


if __name__ == "__main__":
    main()
