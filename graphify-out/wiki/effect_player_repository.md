# effect player repository

> 20 nodes

## Key Concepts

- **set_auth_epoch()** (10 connections) — `server/auth/token_epoch.py`
- **test_jwt_strategy.py** (9 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **token_epoch.py** (8 connections) — `server/auth/token_epoch.py`
- **conftest.py** (6 connections) — `server/tests/unit/auth/conftest.py`
- **test_read_token_accepts_matching_epoch()** (5 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **test_read_token_rejects_wrong_epoch()** (4 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **test_read_token_rejects_missing_epoch()** (4 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **set_auth_epoch_for_tests()** (3 connections) — `server/tests/unit/auth/conftest.py`
- **mock_request()** (2 connections) — `server/tests/unit/auth/conftest.py`
- **mock_session()** (2 connections) — `server/tests/unit/auth/conftest.py`
- **Auth token epoch for server-restart invalidation.  All JWTs issued before the cu** (1 connections) — `server/auth/token_epoch.py`
- **Set the current auth epoch (call once at server startup).** (1 connections) — `server/auth/token_epoch.py`
- **Pytest fixtures for auth unit tests.** (1 connections) — `server/tests/unit/auth/conftest.py`
- **Set auth epoch so token generation and validation work in tests (no real server** (1 connections) — `server/tests/unit/auth/conftest.py`
- **Create a mock request object.** (1 connections) — `server/tests/unit/auth/conftest.py`
- **Create a mock async session.** (1 connections) — `server/tests/unit/auth/conftest.py`
- **Unit tests for restart-invalidating JWT strategy.** (1 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **Tokens with srv claim different from current epoch are rejected.** (1 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **Tokens without srv claim (issued before restart invalidation) are rejected.** (1 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **Tokens with srv matching current epoch are accepted (user lookup proceeds).** (1 connections) — `server/tests/unit/auth/test_jwt_strategy.py`

## Relationships

- [auth users rationale](auth_users_rationale.md) (6 shared connections)
- [player requests schemas](player_requests_schemas.md) (4 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (2 shared connections)
- [aggro threat services](aggro_threat_services.md) (1 shared connections)

## Source Files

- `server/auth/token_epoch.py`
- `server/tests/unit/auth/conftest.py`
- `server/tests/unit/auth/test_jwt_strategy.py`

## Audit Trail

- EXTRACTED: 63 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*