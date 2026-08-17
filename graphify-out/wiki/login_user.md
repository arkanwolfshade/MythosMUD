# login_user

> 60 nodes

## Key Concepts

- **login_user()** (35 connections) — `server/auth/endpoints.py`
- **LoginRequest** (21 connections) — `server/auth/endpoints.py`
- **test_endpoints_login.py** (20 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **test_endpoints_login_profession.py** (11 connections) — `server/tests/unit/auth/test_endpoints_login_profession.py`
- **asyncio** (11 connections)
- **_authenticate_user_credentials()** (8 connections) — `server/auth/endpoints.py`
- **_check_shutdown_status()** (8 connections) — `server/auth/endpoints.py`
- **Request** (8 connections)
- **_find_user_by_username()** (7 connections) — `server/auth/endpoints.py`
- **_get_user_characters()** (7 connections) — `server/auth/endpoints.py`
- **test_login_user_authenticate_raises_exception()** (7 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **test_login_user_authenticate_returns_none()** (7 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **test_login_user_generic_exception()** (7 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **test_login_user_id_mismatch()** (7 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **test_login_user_invalid_credentials()** (7 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **test_login_user_no_email()** (7 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **_check_username_exists()** (6 connections) — `server/auth/endpoints.py`
- **_mark_invite_as_used()** (6 connections) — `server/auth/endpoints.py`
- **test_login_user_player_no_profession_id()** (6 connections) — `server/tests/unit/auth/test_endpoints_login_profession.py`
- **test_login_user_profession_lookup_error()** (6 connections) — `server/tests/unit/auth/test_endpoints_login_profession.py`
- **test_login_user_profession_lookup_none()** (6 connections) — `server/tests/unit/auth/test_endpoints_login_profession.py`
- **test_login_user_profession_lookup_success()** (6 connections) — `server/tests/unit/auth/test_endpoints_login_profession.py`
- **test_login_user_http_exception_re_raised()** (6 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **test_login_user_not_found()** (6 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **test_login_user_shutdown_pending()** (6 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- *... and 35 more nodes in this community*

## Relationships

- [User](User.md) (20 shared connections)
- [get_logger](get_logger.md) (14 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (13 shared connections)
- [register_user](register_user.md) (10 shared connections)
- [test_users.py](test_users.py.md) (2 shared connections)
- [test_endpoints_invites.py](test_endpoints_invites.py.md) (2 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)
- [test_admin_shutdown_command.py](test_admin_shutdown_command.py.md) (1 shared connections)
- [PlayerService](PlayerService.md) (1 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)
- [get_user_manager](get_user_manager.md) (1 shared connections)
- [Invite](Invite.md) (1 shared connections)

## Source Files

- `server/auth/endpoints.py`
- `server/tests/unit/auth/test_endpoints_login.py`
- `server/tests/unit/auth/test_endpoints_login_profession.py`

## Audit Trail

- EXTRACTED: 141 (79%)
- INFERRED: 38 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*