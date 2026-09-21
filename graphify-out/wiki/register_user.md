# register_user

> 75 nodes

## Key Concepts

- **UserCreate** (31 connections) — `server/auth/endpoints.py`
- **register_user()** (31 connections) — `server/auth/endpoints.py`
- **test_endpoints_register.py** (30 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **asyncio** (18 connections)
- **_persist_new_user()** (12 connections) — `server/auth/endpoints.py`
- **_mock_invite_manager()** (10 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **_check_shutdown_status()** (8 connections) — `server/auth/endpoints.py`
- **test_register_user_duplicate_username()** (8 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_register_user_email_constraint_violation()** (8 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_register_user_generic_constraint_violation()** (8 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_register_user_integrity_error()** (8 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_register_user_username_constraint_violation()** (8 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **IntegrityError** (8 connections)
- **Request** (8 connections)
- **_handle_integrity_error()** (7 connections) — `server/auth/endpoints.py`
- **test_register_user_reserve_rejected()** (7 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **UserUpdate** (6 connections) — `server/auth/endpoints.py`
- **_check_username_exists()** (6 connections) — `server/auth/endpoints.py`
- **_create_user_object()** (6 connections) — `server/auth/endpoints.py`
- **test_register_user_capture_rejected_rolls_back()** (6 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_register_user_invite_validation_failure()** (6 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_register_user_no_email()** (6 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_register_user_shutdown_pending()** (6 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_register_user_success()** (6 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_register_user_unexpected_exception()** (6 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- *... and 50 more nodes in this community*

## Relationships

- [User](User.md) (28 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (13 shared connections)
- [Invite](Invite.md) (3 shared connections)
- [factory.py](factory.py.md) (2 shared connections)
- [SecureBaseModel](SecureBaseModel.md) (2 shared connections)
- [is_shutdown_pending](is_shutdown_pending.md) (1 shared connections)
- [get_shutdown_blocking_message](get_shutdown_blocking_message.md) (1 shared connections)
- [test_auth_utils.py](test_auth_utils.py.md) (1 shared connections)
- [RoomService](RoomService.md) (1 shared connections)
- [passive_lucidity_flux/service.py](passive_lucidity_flux-service.py.md) (1 shared connections)
- [test_player_preferences_service.py](test_player_preferences_service.py.md) (1 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (1 shared connections)

## Source Files

- `server/auth/endpoints.py`
- `server/tests/unit/auth/test_endpoints_register.py`

## Audit Trail

- EXTRACTED: 166 (81%)
- INFERRED: 39 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*