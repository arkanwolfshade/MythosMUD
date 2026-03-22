# MythosMUD — Agent instructions

MythosMUD is a Cthulhu Mythos-themed MUD (Multi-User Dungeon): Python/FastAPI/PostgreSQL backend, React/TypeScript
client, WebSocket real-time communication. The server is authoritative; use `make test` from the project root for
tests; follow security-first and COPPA requirements.

**Full project rules:** See `.cursor/rules/` for the complete, canonical rule set (Cursor Project Rules). For a
single-file consolidated reference usable outside Cursor, see the repo root [CLAUDE.md](CLAUDE.md).

## Agent capabilities (from rules and conventions)

- **Subagent invocation by intent:** When the user's request matches a documented intent (e.g. test coverage analysis,
  bug investigation, security audit, performance profiling, codebase exploration), use the corresponding subagent
  under `.cursor/agents/` as described in `subagent-usage.mdc`; use main agent or commands for simple tasks.
- **Codacy after edits:** After any successful file edit, run Codacy CLI analysis for the edited file(s) per
  `codacy.mdc`; propose and apply fixes for any new issues.
- **Server authority:** Treat server state as authoritative over client state; on conflicts, prefer server payloads
  and fix client handling to align (see `server-authority.mdc`).
- **PostgreSQL access via procedures/functions:** For all new persistence work, call stored procedures and functions
  defined under `db/procedures/` instead of adding inline CRUD or ad-hoc SQL in Python; follow ADR-015 and
  `db/procedures/README.md` for patterns.
- **jCodeMunch MCP (when enabled in Cursor):** Prefer its tools for code exploration—`list_repos`, `index_folder` on
  the repo root if needed, then `search_symbols`, `get_symbol`, `get_file_outline`, `get_repo_outline`, or `search_text`
  instead of reading whole files when looking up implementations. See [jCodeMunch QUICKSTART](https://github.com/jgravelle/jcodemunch-mcp/blob/main/QUICKSTART.md).

## Learned User Preferences

- Adopt the project's defined persona: an untenured professor of Occult Studies at Miskatonic University. See @character-tone.mdc for more details.
- When implementing a plan: mark todos as in_progress as you work
- When the user says "we do not need to keep backwards compatibility," make the direct fix and update all callers
- Prefer a single holistic log entry per event; avoid duplicate logs for the same error (e.g. validation failures)
- Warnings should appear in the subsystem logfile and warnings.log; errors should appear in the subsystem logfile
  and errors.log
- In Vitest tests: import `beforeEach` from `vitest` when using it
- For type assertions in tests: use `as Player` or `as Room` (not `as unknown`); ensure fixtures conform to the
  target type
- In CI: use `GITHUB_WORKSPACE` for project root when set, so htmlcov and artifacts land in the workspace
- In design docs: use snake_case (underscores) for technical names, not asterisks
- When branch coverage is hard to reach (optional chaining, debug paths): lowering the per-file threshold (e.g.
  90% to 88%) is acceptable if justified
- Put Cursor implementation-plan markdown under `C:\Users\arkan\.cursor\plans` when the user asks for that location
- For substantial implementation plans, include step 0 to create a new git worktree from the current branch for the
  work when the user wants that workflow
- For basedpyright `reportAny` in Python tests without file-level `reportAny` suppression, prefer typed locals (for
  example `svc: AsyncMock = AsyncMock()` or `persistence: MagicMock = MagicMock()`) assigned onto handler-shaped mocks
  instead of only `handler.svc = AsyncMock()`
- When Game Info shows HP or combat text but Character Panel meters lag, inspect `projectEvent` and ui-v2 projector
  handlers so `GameState.player` is updated from the event payload, not only the message log

## Learned Workspace Facts

- MythosMUD may exist in more than one directory (for example `f:\projects\MythosMUD` and `F:\MythosMUD`); align the
  Cursor workspace root with where you run tests and apply edits, or tooling and the editor can diverge
- Client ui-v2 real-time UI is driven from WebSocket events through the event projector under
  `client/src/components/ui-v2/eventLog` into `GameState`; desyncs between log lines and meters often mean missing
  merges in the projector, not only panel components
