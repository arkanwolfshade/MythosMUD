# useWebSocketConnectionTestFixtures useWe

> 34 nodes

## Key Concepts

- **test_auth_dependencies.py** (24 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **get_current_verified_user()** (8 connections) — `server/auth/dependencies.py`
- **get_optional_current_user()** (6 connections) — `server/auth/dependencies.py`
- **test_get_current_superuser_failure()** (5 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_get_current_verified_user_failure()** (5 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_get_current_superuser_with_none_user()** (5 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_get_current_verified_user_with_none_user()** (5 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_get_current_superuser_success()** (4 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_get_current_verified_user_success()** (4 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_require_invite_code_invalid()** (4 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_require_invite_code_logged_http_exception()** (4 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_require_invite_code_generic_exception()** (4 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_get_optional_current_user_with_user()** (4 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_require_invite_code_none()** (4 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_require_invite_code_success()** (3 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_get_optional_current_user_none()** (3 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_require_invite_code_with_request()** (3 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **Get current verified user or raise 403.** (1 connections) — `server/auth/dependencies.py`
- **Get current user if authenticated, otherwise None.** (1 connections) — `server/auth/dependencies.py`
- **Unit tests for authentication dependencies.** (1 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **Test getting current superuser when user is superuser.** (1 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **Test getting current superuser when user is not superuser.** (1 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **Test getting current verified user when user is verified.** (1 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **Test getting current verified user when user is not verified.** (1 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **Test requiring invite code with valid code.** (1 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- *... and 9 more nodes in this community*

## Relationships

- [Exception Containers](Exception_Containers.md) (20 shared connections)
- [player requests schemas](player_requests_schemas.md) (14 shared connections)
- [command inventory factories](command_inventory_factories.md) (1 shared connections)
- [admin auth service](admin_auth_service.md) (1 shared connections)

## Source Files

- `server/auth/dependencies.py`
- `server/tests/unit/auth/test_auth_dependencies.py`

## Audit Trail

- EXTRACTED: 104 (93%)
- INFERRED: 8 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*