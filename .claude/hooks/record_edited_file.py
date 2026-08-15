#!/usr/bin/env python3
"""
Claude Code PostToolUse hook: record non-test source files for test-agent trigger.

Reads JSON from stdin (session_id, cwd, tool_name, tool_input).
If the edited file is NOT a test file, appends it to .claude/hooks/state/edited-files.json.
Test files are excluded so edits to tests never trigger the test-creation follow-up.

Ported from .cursor/hooks/record_edited_file.py; adapted to Claude Code's PostToolUse
stdin schema (session_id instead of conversation_id, tool_input.file_path instead of
a top-level file_path field).
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


def _normalize_path(path: str) -> str:
    """Normalize path to forward slashes for consistent matching."""
    return str(Path(path).as_posix())


def _rel_path(file_path: str, workspace_root: str | None) -> str:
    """Return workspace-relative path for pattern matching."""
    normalized = _normalize_path(file_path)
    root = _normalize_path(workspace_root) if workspace_root else ""
    if root and normalized.startswith(root):
        return normalized[len(root) :].lstrip("/")
    # Path may already be workspace-relative (e.g. server/tests/unit/test_foo.py)
    return normalized


def _is_server_test_path(rel: str) -> bool:
    """True if path is under server/tests/."""
    return "server/tests" in rel or "server\\tests" in rel


def _is_client_test_path(rel: str) -> bool:
    """True if path is in __tests__/ or has client test extension."""
    if "__tests__" in rel:
        return True
    lower_name = Path(rel).name.lower()
    return any(lower_name.endswith(ext) for ext in (".test.ts", ".test.tsx", ".spec.ts", ".spec.tsx"))


def _is_agent_config_path(rel: str) -> bool:
    """True if path is under .claude/ or .cursor/ (agent/skill/rule/hook config, not application code)."""
    return rel.startswith(".claude/") or rel.startswith(".cursor/")


def _is_test_file(file_path: str, workspace_root: str | None) -> bool:
    """
    Return True if the file should NOT trigger the test agent: a test file, or agent
    config (prompts/skills/rules/hooks aren't unit-testable application code).

    Patterns (workspace-relative):
    - server/tests/
    - **/__tests__/
    - *.test.ts, *.test.tsx, *.spec.ts, *.spec.tsx
    - .claude/, .cursor/
    """
    rel = _rel_path(file_path, workspace_root)
    return _is_server_test_path(rel) or _is_client_test_path(rel) or _is_agent_config_path(rel)


def _load_payload() -> dict[str, Any] | None:
    """Load JSON payload from stdin; return None on failure (fail open)."""
    try:
        result: dict[str, Any] = json.load(sys.stdin)
        return result
    except json.JSONDecodeError:
        return None


def _load_state(state_file: Path) -> dict[str, list[str]]:
    """Load state from file; return empty dict on failure."""
    if not state_file.exists():
        return {}
    try:
        data = json.loads(state_file.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except (json.JSONDecodeError, OSError):
        return {}


def _should_skip_recording(payload: dict[str, Any]) -> bool:
    """Return True if we should not record (missing data or test file)."""
    tool_input = payload.get("tool_input") or {}
    file_path = tool_input.get("file_path")
    session_id = payload.get("session_id")
    if not file_path or not session_id:
        return True
    workspace_root = payload.get("cwd", "")
    return _is_test_file(file_path, workspace_root)


def main() -> None:
    """
    Entry point: read hook payload from stdin and record non-test edited files
    to edited-files.json for the test-creation follow-up.
    """
    payload = _load_payload()
    if not payload or _should_skip_recording(payload):
        sys.exit(0)

    tool_input = payload.get("tool_input") or {}
    file_path = tool_input.get("file_path")
    session_id = payload.get("session_id")
    assert file_path is not None and session_id is not None  # ensured by _should_skip_recording
    cwd = payload.get("cwd", "")

    state_dir = Path(cwd or ".") / ".claude" / "hooks" / "state"
    state_file = state_dir / "edited-files.json"
    state_dir.mkdir(parents=True, exist_ok=True)

    state = _load_state(state_file)
    files = state.get(session_id, [])
    if file_path not in files:
        files.append(file_path)
        state[session_id] = files
        state_file.write_text(json.dumps(state, indent=2), encoding="utf-8")

    sys.exit(0)


if __name__ == "__main__":
    main()
