# register_user

> 72 nodes

## Key Concepts

- **register_user()** (31 connections) — `server/auth/endpoints.py`
- **UserCreate** (30 connections) — `server/auth/endpoints.py`
- **test_endpoints_register.py** (28 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **asyncio** (18 connections)
- **_persist_new_user()** (12 connections) — `server/auth/endpoints.py`
- **_mock_invite_manager()** (10 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **_check_shutdown_status()** (8 connections) — `server/auth/endpoints.py`
- **test_register_user_duplicate_username()** (8 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_register_user_email_constraint_violation()** (8 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_register_user_generic_constraint_violation()** (8 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_register_user_integrity_error()** (8 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_register_user_username_constraint_violation()** (8 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **Request** (8 connections)
- **_find_user_by_username()** (7 connections) — `server/auth/endpoints.py`
- **_handle_integrity_error()** (7 connections) — `server/auth/endpoints.py`
- **test_register_user_reserve_rejected()** (7 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **IntegrityError** (7 connections)
- **_check_username_exists()** (6 connections) — `server/auth/endpoints.py`
- **test_register_user_capture_rejected_rolls_back()** (6 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_register_user_invite_validation_failure()** (6 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_register_user_no_email()** (6 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_register_user_shutdown_pending()** (6 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_register_user_success()** (6 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_register_user_unexpected_exception()** (6 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **LoginResponse** (5 connections) — `server/auth/endpoints.py`
- *... and 47 more nodes in this community*

## Relationships

- [User](User.md) (34 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (14 shared connections)
- [factory.py](factory.py.md) (1 shared connections)
- [is_shutdown_pending](is_shutdown_pending.md) (1 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (1 shared connections)
- [pydantic.md](pydantic.md.md) (1 shared connections)
- [test_player_preferences_service.py](test_player_preferences_service.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/auth/endpoints.py`
- `server/tests/unit/auth/test_endpoints_register.py`

## Audit Trail

- EXTRACTED: 164 (82%)
- INFERRED: 36 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*