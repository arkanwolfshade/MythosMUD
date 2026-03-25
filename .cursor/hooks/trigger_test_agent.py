#!/usr/bin/env python3
"""
Cursor stop hook: trigger test-creation agent when non-test source files were edited.

Reads .cursor/hooks/state/edited-files.json for this conversation_id.
If any non-test files were recorded (by record_edited_file.py), returns followup_message
to auto-continue the agent with a test-creation prompt. Clears state for this conversation.
"""

from __future__ import annotations

import json
import os
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
    """Print empty JSON and exit successfully (no followup)."""
    print("{}", end="")
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
    emit a followup_message to trigger the test-creation agent.
    """
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        _exit_empty()

    conversation_id = payload.get("conversation_id")
    loop_count = payload.get("loop_count", 0)
    project_dir = os.environ.get("CURSOR_PROJECT_DIR", ".")

    if not conversation_id:
        _exit_empty()

    # loop_limit: 1 means we only trigger when loop_count is 0
    if loop_count > 0:
        _exit_empty()

    state_dir = Path(project_dir or ".") / ".cursor" / "hooks" / "state"
    state_file = state_dir / "edited-files.json"
    state = _load_state(state_file)
    if state is None:
        _exit_empty()

    files = state.pop(conversation_id, [])
    if not files:
        # Write back state (in case we popped nothing but other convs exist)
        state_file.write_text(json.dumps(state, indent=2), encoding="utf-8")
        _exit_empty()

    # Persist updated state (removed this conversation)
    state_dir.mkdir(parents=True, exist_ok=True)
    state_file.write_text(json.dumps(state, indent=2), encoding="utf-8")

    response = {"followup_message": FOLLOWUP_MESSAGE}
    print(json.dumps(response), end="")
    sys.exit(0)


if __name__ == "__main__":
    main()
