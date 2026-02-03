# Cursor Hooks

Cursor Hooks run at specific stages of the agent loop (e.g. after the agent edits a file) and are configured in this project for MythosMUD.

## Configuration

- **Config file:** [`.cursor/hooks.json`](../.cursor/hooks.json)
- **Scripts:** [`.cursor/hooks/`](../.cursor/hooks/) (project hooks run from the project root)
- **UI:** Cursor Settings → Hooks — view configured hooks and the Execution Log

## Configured Hooks

| Event | Purpose | Script |
|-------|---------|--------|
| **afterFileEdit** | Format agent-edited files so output matches pre-commit (ruff for server Python, prettier for client TS/JSON/MD) | [`.cursor/hooks/format-after-edit.ps1`](../.cursor/hooks/format-after-edit.ps1) |

## Formatting After Agent Edit

Formatting of files edited by the Cursor agent is handled by the **afterFileEdit** hook only (no VS Code format-on-save for the same behavior). For manual edits, use "Format Document" in the editor or run pre-commit before commit (`uv run pre-commit run --all-files`).

## References

- [Cursor Docs: Hooks](https://cursor.com/docs/agent/hooks)
