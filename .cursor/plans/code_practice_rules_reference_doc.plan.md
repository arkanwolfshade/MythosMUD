---
name: Code Practice Rules Reference Doc
overview: Add a single reference document that lists only code/feature/language best-practice Cursor rules that apply to MythosMUD, derived from the project's actual dependencies (pyproject.toml and client/package.json). No conditional or "if you use" items; every listed rule corresponds to a technology in use in this repo.
todos:
  - id: "1"
    content: Create docs/CURSOR_CODE_PRACTICE_RULES_REFERENCE.md with project-verified rule list
    status: pending
  - id: "2"
    content: Verify doc lists only rules for tech present in repo; run markdown formatter (120-char line length)
    status: pending
isProject: false
---

# Code Practice Rules Reference Document (Project-Verified)

## Goal

Create one markdown reference file that lists **only** code/feature/language best-practice rules from `.cursor/rules` that apply to MythosMUD. The list is derived from the project's actual dependencies and codebase—no "if you use" or optional sections. Every rule listed must correspond to a technology in use in this repository.

## Scope and Exclusions

**Out of scope (excluded from this reference):**

- `e2e-tests/MULTIPLAYER_TEST_RULES.md`
- `.cursor/rules/serverstart.mdc`
- `.cursor/rules/character-tone.mdc`
- `.cursor/rules/mythosmud-skill-triggers.mdc`
- `.cursor/rules/subagent-usage.mdc`
- `.cursor/rules/run-multiplayer-playbook.mdc`
- [.cursor/rules/GAME_BUG_INVESTIGATION_PLAYBOOK.mdc](.cursor/rules/GAME_BUG_INVESTIGATION_PLAYBOOK.mdc)

These are operational, process, persona, or playbook rules—not code-practice rules.

## Source of Truth for "Relevant to This Project"

- **Backend:** [pyproject.toml](pyproject.toml) (dependencies, dev dependencies, tool config)
- **Client:** [client/package.json](client/package.json) (dependencies, devDependencies)
- **Usage in code:** WebSockets, NATS, Click (CLI), etc. are used in server and client code.

## Comprehensive Rule List (Project-Verified)

Only rules that **exist** in `.cursor/rules` and for which the **technology is used** in MythosMUD are listed below.

### 1. Core backend stack

| Rule file                                                    | Evidence in project                                     |
| ------------------------------------------------------------ | ------------------------------------------------------- |
| [.cursor/rules/python.mdc](.cursor/rules/python.mdc)         | Python 3.12, pyproject.toml                             |
| [.cursor/rules/fastapi.mdc](.cursor/rules/fastapi.mdc)       | fastapi in pyproject.toml                               |
| [.cursor/rules/pydantic.mdc](.cursor/rules/pydantic.mdc)     | pydantic, pydantic-settings in pyproject.toml           |
| [.cursor/rules/postgresql.mdc](.cursor/rules/postgresql.mdc) | psycopg2-binary, asyncpg in pyproject.toml              |
| [.cursor/rules/sqlalchemy.mdc](.cursor/rules/sqlalchemy.mdc) | sqlalchemy, fastapi-users[sqlalchemy] in pyproject.toml |
| [.cursor/rules/anyio.mdc](.cursor/rules/anyio.mdc)           | anyio in pyproject.toml                                 |
| [.cursor/rules/structlog.mdc](.cursor/rules/structlog.mdc)   | structlog in pyproject.toml                             |
| [.cursor/rules/uvicorn.mdc](.cursor/rules/uvicorn.mdc)       | uvicorn[standard] in pyproject.toml                     |

### 2. Backend libraries and patterns

| Rule file                                                  | Evidence in project                                                      |
| ---------------------------------------------------------- | ------------------------------------------------------------------------ |
| [.cursor/rules/nats.mdc](.cursor/rules/nats.mdc)           | nats-py in pyproject.toml; server/services/nats_service, realtime        |
| [.cursor/rules/click.mdc](.cursor/rules/click.mdc)         | click in pyproject.toml (CLI parsing/validation)                         |
| [.cursor/rules/websocket.mdc](.cursor/rules/websocket.mdc) | Starlette WebSocket throughout server/realtime (websocket_handler, etc.) |

### 3. Testing

| Rule file                                                                                    | Evidence in project                                                                |
| -------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| [.cursor/rules/pytest.mdc](.cursor/rules/pytest.mdc)                                         | pytest, pytest-cov, pytest-asyncio, pytest-timeout, pytest-xdist in pyproject.toml |
| [.cursor/rules/test_coverage_requirements.mdc](.cursor/rules/test_coverage_requirements.mdc) | Project rule; .coveragerc, pytest-cov config                                       |
| [.cursor/rules/testwriting.mdc](.cursor/rules/testwriting.mdc)                               | Project rule; server/tests layout                                                  |
| [.cursor/rules/playwright.mdc](.cursor/rules/playwright.mdc)                                 | playwright in pyproject.toml; @playwright/test in client/package.json              |
| [.cursor/rules/vitest.mdc](.cursor/rules/vitest.mdc)                                         | vitest in client/package.json (unit tests)                                         |
| [.cursor/rules/unittest.mdc](.cursor/rules/unittest.mdc)                                     | Python stdlib; test patterns in server/tests                                       |

### 4. Code quality and tooling

| Rule file                                                    | Evidence in project                                                     |
| ------------------------------------------------------------ | ----------------------------------------------------------------------- |
| [.cursor/rules/codacy.mdc](.cursor/rules/codacy.mdc)         | Project rule; Codacy CLI/config                                         |
| [.cursor/rules/eslint.mdc](.cursor/rules/eslint.mdc)         | eslint in client/package.json                                           |
| [.cursor/rules/pre-commit.mdc](.cursor/rules/pre-commit.mdc) | pre-commit in pyproject.toml                                            |
| [.cursor/rules/mypy.mdc](.cursor/rules/mypy.mdc)             | mypy in pyproject.toml dev; [tool.mypy] config                          |
| [.cursor/rules/pylint.mdc](.cursor/rules/pylint.mdc)         | pylint in pyproject.toml dev                                            |
| [.cursor/rules/flake8.mdc](.cursor/rules/flake8.mdc)         | Ruff config in pyproject.toml (E, W, F, B, C4, C90, UP); style concepts |

### 5. Design and security

| Rule file                                                                      | Evidence in project                              |
| ------------------------------------------------------------------------------ | ------------------------------------------------ |
| [.cursor/rules/server-authority.mdc](.cursor/rules/server-authority.mdc)       | Project rule (server authoritative over client)  |
| [.cursor/rules/security.mdc](.cursor/rules/security.mdc)                       | Security-first project; COPPA, env-based secrets |
| [.cursor/rules/architecture-review.mdc](.cursor/rules/architecture-review.mdc) | Project rule; docs/architecture, ADRs            |

### 6. Front-end stack

| Rule file                                                    | Evidence in project                                       |
| ------------------------------------------------------------ | --------------------------------------------------------- |
| [.cursor/rules/react.mdc](.cursor/rules/react.mdc)           | react, react-dom, react-router-dom in client/package.json |
| [.cursor/rules/typescript.mdc](.cursor/rules/typescript.mdc) | typescript in client/package.json                         |
| [.cursor/rules/vite.mdc](.cursor/rules/vite.mdc)             | vite, @vitejs/plugin-react in client/package.json         |
| [.cursor/rules/tailwind.mdc](.cursor/rules/tailwind.mdc)     | tailwindcss, @tailwindcss/postcss in client/package.json  |
| [.cursor/rules/zustand.mdc](.cursor/rules/zustand.mdc)       | zustand in client/package.json                            |

### 7. CI and workflow (code-adjacent)

| Rule file                                                            | Evidence in project                |
| -------------------------------------------------------------------- | ---------------------------------- |
| [.cursor/rules/git.mdc](.cursor/rules/git.mdc)                       | Git workflow; commit message rules |
| [.cursor/rules/github-actions.mdc](.cursor/rules/github-actions.mdc) | CI runs tests, lint, etc.          |

## Explicitly not included (not in project)

- [.cursor/rules/redis.mdc](.cursor/rules/redis.mdc) — Redis is not a dependency in pyproject.toml or client.
- [.cursor/rules/react-query.mdc](.cursor/rules/react-query.mdc) — Not in client/package.json.
- [.cursor/rules/hypothesis.mdc](.cursor/rules/hypothesis.mdc) — Hypothesis is not in pyproject.toml (only string "hypothesisId" in tests).
- [.cursor/rules/httpx.mdc](.cursor/rules/httpx.mdc) — Not in main or dev dependencies in pyproject.toml.

## Deliverable

- **Path:** [docs/CURSOR_CODE_PRACTICE_RULES_REFERENCE.md](docs/CURSOR_CODE_PRACTICE_RULES_REFERENCE.md)
- **Content:** Same structure as above: title, purpose, excluded rules, then the seven categories with one line per rule (path + brief description). No conditional or optional sections.
- **Formatting:** Markdown line length 120 characters max per project preference; run formatter on the file.

## Verification

- Every rule in the doc exists under `.cursor/rules/` and corresponds to a dependency or pattern in this repo.
- Excluded list matches the seven items above.
- No "if you use" or "optional" wording in the reference doc.
