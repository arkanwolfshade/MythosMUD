# MythosMUD — Agent instructions

MythosMUD is a Cthulhu Mythos-themed MUD (Multi-User Dungeon): Python/FastAPI/PostgreSQL backend, React/TypeScript
client, WebSocket real-time communication. The server is authoritative; use `make test` from the project root for
tests; follow security-first and COPPA requirements.

**Full project rules:** See `.cursor/rules/` for the complete, canonical rule set (Cursor Project Rules). For a
single-file consolidated reference usable outside Cursor, see the repo root [CLAUDE.md](CLAUDE.md).

## Learned preferences (from chat history)

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
