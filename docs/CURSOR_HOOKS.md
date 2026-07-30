# Cursor Hooks
**Version 1.0.0** · MythosMUD · 2026-07-30

---

## AI READING INSTRUCTION

Read `[SPEC]` and `[BUG]` blocks for authoritative facts.
Read `[NOTE]` only if additional context is needed.
`[?]` blocks are unverified — treat with lower confidence.

---

## 1. Overview

**[NOTE]**
Cursor Hooks run at specific stages of the agent loop (e.g. after the agent edits a file) and are configured in this project for MythosMUD.

## 2. Configuration

**[SPEC]**
- **Config file:** [`.cursor/hooks.json`](../.cursor/hooks.json)
- **Scripts:** [`.cursor/hooks/`](../.cursor/hooks/) (project hooks run from the project root)
- **UI:** Cursor Settings → Hooks — view configured hooks and the Execution Log

## 3. Configured Hooks

**[SPEC]**
| Event             | Purpose                                                                       | Script                                                                          |
| ----------------- | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| **afterFileEdit** | Record non-test source files for test-agent trigger                           | [`.cursor/hooks/record_edited_file.py`](../.cursor/hooks/record_edited_file.py) |
| **stop**          | Auto-continue agent with test-creation prompt when non-test files were edited | [`.cursor/hooks/trigger_test_agent.py`](../.cursor/hooks/trigger_test_agent.py) |

## 4. Triggered Test Agent

**[SPEC]**
When you accept AI-generated code via Agent (Cmd+K), the agent automatically continues with a prompt to create or update unit tests for the modified source files. Test files are excluded so edits to tests never trigger this flow.

- **Flow:** `afterFileEdit` records edited non-test files; `stop` returns a followup message to auto-continue the agent with a test-creation prompt.
- **Excluded paths:** `server/tests/`, `**/__tests__/`, `*.test.ts`, `*.test.tsx`, `*.spec.ts`, `*.spec.tsx`
- **State:** `.cursor/hooks/state/edited-files.json` (gitignored)
- **Reference:** [mythosmud-test-writing skill](../.cursor/skills/mythosmud-test-writing/SKILL.md)

For manual edits, use "Format Document" or run pre-commit before commit (`uv run pre-commit run --all-files`).

## 5. References

**[SPEC]**
- [Cursor Docs: Hooks](https://cursor.com/docs/agent/hooks)

## 6. Changelog

**[SPEC]**
| Version | Date | Change |
| --- | --- | --- |
| 1.0.0 | 2026-07-30 | Initial HADS structural conversion |
