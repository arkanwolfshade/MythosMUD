# Game Chat Whisper

> 9 nodes

## Key Concepts

- **pytest_asyncio_loop_factories()** (6 connections) — `server/tests/conftest.py`
- **_create_test_event_loop()** (4 connections) — `server/tests/conftest.py`
- **eslint.config.js** (3 connections) — `client/eslint.config.js`
- **Config** (3 connections)
- **AbstractEventLoop** (2 connections)
- **jsxA11yRecommendedWarnRules** (1 connections) — `client/eslint.config.js`
- **jsxA11yRulesOff** (1 connections) — `client/eslint.config.js`
- **Create an event loop suitable for MythosMUD tests.      CRITICAL: On Windows, Se** (1 connections) — `server/tests/conftest.py`
- **Register platform-appropriate loop factories for pytest-asyncio (Python 3.14+ sa** (1 connections) — `server/tests/conftest.py`

## Relationships

- [ESLint Conftest Fixtures](ESLint_Conftest_Fixtures.md) (4 shared connections)

## Source Files

- `client/eslint.config.js`
- `server/tests/conftest.py`

## Audit Trail

- EXTRACTED: 20 (91%)
- INFERRED: 2 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*