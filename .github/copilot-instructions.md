# GitHub Copilot instructions (MythosMUD)

**Authoritative guidance for AI agents (including Copilot):** see the repository root
[`AGENTS.md`](../AGENTS.md). This file stays small so GitHub’s Copilot integration can point at one maintained document.

- **Cursor IDE:** `.cursor/rules/` is the granular rule set for Cursor.
- **Sync:** When `.cursor/rules/` or agent skills change meaningfully, update [`AGENTS.md`](../AGENTS.md). Keep this file a
  router, not a second copy of the rules.

Optional quick reminders (details live in `AGENTS.md`):

- Tests from repo root: `make test` / `make test-comprehensive` (do not run raw `pytest` against `server/` alone).
- One MythosMUD server at a time; use `scripts/stop_server.ps1` before `scripts/start_local.ps1`.
- Server is authoritative over client; prefer server payloads on conflicts.
