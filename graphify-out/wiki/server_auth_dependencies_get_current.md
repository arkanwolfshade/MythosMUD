# server auth dependencies get current

> 36 nodes

## Key Concepts

- **test_auth_dependencies.py** (26 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **asyncio** (14 connections)
- **get_current_superuser()** (12 connections) — `server/auth/dependencies.py`
- **require_invite_code()** (11 connections) — `server/auth/dependencies.py`
- **get_current_verified_user()** (8 connections) — `server/auth/dependencies.py`
- **get_optional_current_user()** (6 connections) — `server/auth/dependencies.py`
- **test_get_current_superuser_failure()** (6 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_get_current_superuser_with_none_user()** (6 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_get_current_verified_user_failure()** (6 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_get_current_verified_user_with_none_user()** (6 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_get_current_superuser_success()** (5 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_get_current_verified_user_success()** (5 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_get_optional_current_user_with_user()** (5 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_require_invite_code_generic_exception()** (5 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_require_invite_code_invalid()** (5 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_require_invite_code_logged_http_exception()** (5 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_require_invite_code_none()** (5 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_get_optional_current_user_none()** (4 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_require_invite_code_success()** (4 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_require_invite_code_with_request()** (4 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **Test requiring invite code when validate_invite raises LoggedHTTPException.** (2 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **Test getting current superuser when user is superuser.** (2 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **Test getting current verified user when user is verified.** (2 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **Get current superuser or raise 403.** (1 connections) — `server/auth/dependencies.py`
- **Get current verified user or raise 403.** (1 connections) — `server/auth/dependencies.py`
- *... and 11 more nodes in this community*

## Relationships

- [server api players](server_api_players.md) (12 shared connections)
- [dependsparam](dependsparam.md) (11 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (8 shared connections)
- [baseusermanager](baseusermanager.md) (3 shared connections)
- [server auth invites](server_auth_invites.md) (1 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (1 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (1 shared connections)

## Source Files

- `server/auth/dependencies.py`
- `server/tests/unit/auth/test_auth_dependencies.py`

## Audit Trail

- EXTRACTED: 86 (84%)
- INFERRED: 16 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*