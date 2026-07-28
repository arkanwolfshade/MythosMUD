# Server Auth (2)

> 103 nodes

## Key Concepts

- **Result** (52 connections) — `scripts/run_test_ci.py`
- **test_endpoints.py** (51 connections) — `server/tests/unit/auth/test_endpoints.py`
- **register_user()** (28 connections) — `server/auth/endpoints.py`
- **login_user()** (28 connections) — `server/auth/endpoints.py`
- **UserCreate** (27 connections) — `server/auth/endpoints.py`
- **LoginRequest** (22 connections) — `server/auth/endpoints.py`
- **_check_shutdown_status()** (8 connections) — `server/auth/endpoints.py`
- **Request** (8 connections)
- **LoginResponse** (7 connections) — `server/auth/endpoints.py`
- **_validate_invite_code()** (7 connections) — `server/auth/endpoints.py`
- **_check_username_exists()** (7 connections) — `server/auth/endpoints.py`
- **_find_user_by_username()** (7 connections) — `server/auth/endpoints.py`
- **_authenticate_user_credentials()** (7 connections) — `server/auth/endpoints.py`
- **test_register_user_duplicate_username()** (7 connections) — `server/tests/unit/auth/test_endpoints.py`
- **test_register_user_integrity_error()** (7 connections) — `server/tests/unit/auth/test_endpoints.py`
- **test_login_user_no_email()** (7 connections) — `server/tests/unit/auth/test_endpoints.py`
- **test_login_user_id_mismatch()** (7 connections) — `server/tests/unit/auth/test_endpoints.py`
- **test_login_user_generic_exception()** (7 connections) — `server/tests/unit/auth/test_endpoints.py`
- **test_register_user_email_constraint_violation()** (7 connections) — `server/tests/unit/auth/test_endpoints.py`
- **test_register_user_username_constraint_violation()** (7 connections) — `server/tests/unit/auth/test_endpoints.py`
- **test_register_user_generic_constraint_violation()** (7 connections) — `server/tests/unit/auth/test_endpoints.py`
- **test_login_user_authenticate_returns_none()** (7 connections) — `server/tests/unit/auth/test_endpoints.py`
- **test_login_user_authenticate_raises_exception()** (7 connections) — `server/tests/unit/auth/test_endpoints.py`
- **_create_user_object()** (6 connections) — `server/auth/endpoints.py`
- **_mark_invite_as_used()** (6 connections) — `server/auth/endpoints.py`
- *... and 78 more nodes in this community*

## Relationships

- [Server Admin](Server_Admin.md) (58 shared connections)
- [Server Services (16)](Server_Services_%2816%29.md) (25 shared connections)
- [Server Api](Server_Api.md) (21 shared connections)
- [Server Auth](Server_Auth.md) (3 shared connections)
- [Server Middleware](Server_Middleware.md) (2 shared connections)
- [Server Api (4)](Server_Api_%284%29.md) (2 shared connections)
- [Server Utils](Server_Utils.md) (2 shared connections)
- [Docs Examples](Docs_Examples.md) (1 shared connections)
- [Docs Examples (2)](Docs_Examples_%282%29.md) (1 shared connections)
- [Scripts Utils (2)](Scripts_Utils_%282%29.md) (1 shared connections)
- [Server Auth (4)](Server_Auth_%284%29.md) (1 shared connections)

## Source Files

- `scripts/run_test_ci.py`
- `server/auth/endpoints.py`
- `server/tests/unit/auth/test_endpoints.py`
- `server/tests/unit/services/test_player_preferences_service.py`

## Audit Trail

- EXTRACTED: 422 (80%)
- INFERRED: 107 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*