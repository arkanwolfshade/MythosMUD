# Community 644

> 26 nodes

## Key Concepts

- **test_jwt_strategy.py** (9 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **set_auth_epoch()** (8 connections) — `server/auth/token_epoch.py`
- **token_epoch.py** (8 connections) — `server/auth/token_epoch.py`
- **jwt_strategy.py** (7 connections) — `server/auth/jwt_strategy.py`
- **get_auth_epoch()** (6 connections) — `server/auth/token_epoch.py`
- **test_read_token_accepts_matching_epoch()** (6 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **auth/conftest.py** (6 connections) — `server/tests/unit/auth/conftest.py`
- **test_read_token_rejects_missing_epoch()** (5 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **test_read_token_rejects_wrong_epoch()** (5 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **set_auth_epoch_for_tests()** (4 connections) — `server/tests/unit/auth/conftest.py`
- **mock_request()** (3 connections) — `server/tests/unit/auth/conftest.py`
- **mock_session()** (3 connections) — `server/tests/unit/auth/conftest.py`
- **fixture** (3 connections)
- **asyncio** (3 connections)
- **Custom JWT strategy that invalidates tokens after server restart. Tokens must…** (1 connections) — `server/auth/jwt_strategy.py`
- **Auth token epoch for server-restart invalidation. All JWTs issued before the…** (1 connections) — `server/auth/token_epoch.py`
- **Set the current auth epoch (call once at server startup).** (1 connections) — `server/auth/token_epoch.py`
- **Return the current auth epoch. Must be set before any token validation.** (1 connections) — `server/auth/token_epoch.py`
- **Pytest fixtures for auth unit tests.** (1 connections) — `server/tests/unit/auth/conftest.py`
- **Set auth epoch so token generation and validation work in tests (no real server…** (1 connections) — `server/tests/unit/auth/conftest.py`
- **Create a mock request object.** (1 connections) — `server/tests/unit/auth/conftest.py`
- **Create a mock async session.** (1 connections) — `server/tests/unit/auth/conftest.py`
- **Unit tests for restart-invalidating JWT strategy.** (1 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **Tokens with srv claim different from current epoch are rejected.** (1 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **Tokens without srv claim (issued before restart invalidation) are rejected.** (1 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- *... and 1 more nodes in this community*

## Relationships

- [Community 682](Community_682.md) (6 shared connections)
- [Auth Dependencies & Users](Auth_Dependencies_&_Users.md) (2 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (1 shared connections)
- [Community 317](Community_317.md) (1 shared connections)

## Source Files

- `server/auth/jwt_strategy.py`
- `server/auth/token_epoch.py`
- `server/tests/unit/auth/conftest.py`
- `server/tests/unit/auth/test_jwt_strategy.py`

## Audit Trail

- EXTRACTED: 46 (94%)
- INFERRED: 3 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*