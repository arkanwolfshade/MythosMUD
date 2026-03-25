# Cursor Hooks

Cursor Hooks run at specific stages of the agent loop (e.g. after the agent edits a file) and are configured in this project for MythosMUD.

## Configuration

- **Config file:** [`.cursor/hooks.json`](../.cursor/hooks.json)
- **Scripts:** [`.cursor/hooks/`](../.cursor/hooks/) (project hooks run from the project root)
- **UI:** Cursor Settings → Hooks — view configured hooks and the Execution Log

## Configured Hooks

| Event             | Purpose                                                                       | Script                                                                          |
| ----------------- | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| **afterFileEdit** | Record non-test source files for test-agent trigger                           | [`.cursor/hooks/record_edited_file.py`](../.cursor/hooks/record_edited_file.py) |
| **stop**          | Auto-continue agent with test-creation prompt when non-test files were edited | [`.cursor/hooks/trigger_test_agent.py`](../.cursor/hooks/trigger_test_agent.py) |

## Triggered Test Agent

When you accept AI-generated code via Agent (Cmd+K), the agent automatically continues with a prompt to create or update unit tests for the modified source files. Test files are excluded so edits to tests never trigger this flow.

- **Flow:** `afterFileEdit` records edited non-test files; `stop` returns a followup message to auto-continue the agent with a test-creation prompt.
- **Excluded paths:** `server/tests/`, `**/__tests__/`, `*.test.ts`, `*.test.tsx`, `*.spec.ts`, `*.spec.tsx`
- **State:** `.cursor/hooks/state/edited-files.json` (gitignored)
- **Reference:** [mythosmud-test-writing skill](../.cursor/skills/mythosmud-test-writing/SKILL.md)

For manual edits, use "Format Document" or run pre-commit before commit (`uv run pre-commit run --all-files`).

## References

- [Cursor Docs: Hooks](https://cursor.com/docs/agent/hooks)
