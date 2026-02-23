# MythosMUD — AI PR Reviewer Instructions

## Purpose

MythosMUD is a Cthulhu Mythos-themed MUD (Multi-User Dungeon): Python/FastAPI/PostgreSQL backend,
React/TypeScript client, WebSocket real-time communication. The server is authoritative. Security-first
and COPPA compliance are mandatory.

## Architecture

- **Monorepo**: `server/` (Python), `client/` (React), shared config at root
- **Server authority**: Server state is always correct; client must sync to server payloads
- **Patterns**: FastAPI REST + WebSocket, Pydantic validation, thread-safe singleton for persistence
- **Async**: AnyIO for backend-agnostic async; use `anyio.run()` at entry points, never `asyncio.run()`
  in `server/`

## Folder Structure

- `server/` — FastAPI backend, game logic, persistence, WebSocket handlers
- `server/tests/` — Unit (`unit`), integration (`integration`), fixtures in `fixtures/`
- `client/` — React/TypeScript SPA, Vite build
- `data/players/`, `data/npcs/` — Production DB paths (PostgreSQL; no SQLite)
- `scripts/` — PowerShell and Python tooling (lint, format, server start/stop)
- `docs/` — Documentation, OpenAPI spec

## Stack

- **Backend**: Python 3.12+, FastAPI, Pydantic, SQLAlchemy, asyncpg, AnyIO
- **Frontend**: React, TypeScript, Vite
- **Database**: PostgreSQL only (`mythos_unit`, `mythos_e2e` for tests; `mythos_dev` protected)
- **Tooling**: uv (Python), ruff (lint/format), mypy, pre-commit, ESLint, Prettier

## Testing

- **Framework**: pytest (server), Vitest (client), Playwright (E2E)
- **Execution**: Run `make test` or `make test-coverage` from project root only; never from `server/`
- **Never**: `python -m pytest` directly
- **Coverage**: 70% minimum; 90% for security, core features, user-facing code
- **Test placement**: `server/tests/unit/`, `server/tests/integration/`; fixtures in `fixtures/` only
- **Markers**: `unit`, `integration`, `e2e`, `slow`, `serial`, etc. (see `server/pytest.ini`)

## Code Style & Conventions

- **Linting**: ruff (sole Python linter/formatter); 120-char line length
- **Logging**: `from server.logging.enhanced_logging_config import get_logger` — never `logging.getLogger()`
- **Logging format**: Structured key-value `logger.info("msg", key=value)`; never f-strings or
  `context={}`
- **Terminology**: Use "controller"/"coordinator" not "master"; "agent" not "slave"
- **Suppressions**: Add a comment justifying any mypy/ruff/pylint suppression
- **File size**: Refactor files over ~500 lines into smaller modules
- **Unicode**: No unicode characters in Python files

## PR-Specific Rules

- **Branch strategy**: Never switch branches without explicit user permission
- **Commits**: Concise, technical; link issues with `#issue-number`; no corporate boilerplate
- **Task tracking**: GitHub Issues; PRs should reference issues
- **Definition of done**: Formatting, linting, and tests must pass
- **API changes**: Update OpenAPI spec (`make openapi-spec`) when routes/schemas change

## Common Pitfalls (Flag These)

Things reviewers should flag: anti-patterns, known gotchas, and areas that break easily.

- **Database placement**: DB files outside `/data/players/`, `/data/npcs/` (prod) or
  `server/tests/data/players/`, `server/tests/data/npcs/` (tests)
- **player_id**: Must be UUID type, not string
- **SQLite**: Do not use; PostgreSQL only
- **mythos_dev**: Never truncate or delete; tests must not use it for cleanup
- **Logging**: `import logging` or `logging.getLogger()` instead of enhanced logger
- **asyncio.run()**: Forbidden in `server/`; use `anyio.run()` at entry points
- **Security**: Hardcoded secrets; missing input validation; missing COPPA checks for user data
- **Client vs server**: Client treating local state as source of truth when it conflicts with server
- **Tests**: Tests that exercise test infrastructure or Python built-ins instead of server code

## Out of Scope

- Mythos flavor in variable/function names (flavor belongs in comments)
- Exact line-length debates beyond 120-char limit
- Codacy complexity metrics as blockers (focus on complexity issues, not raw metrics)
- Coverage metric changes from duplicated or boilerplate code
