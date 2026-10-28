# ._create_grid_map

> 131 nodes · cohesion 0.02

## Key Concepts

- **test_users.py** (53 connections) — `server/tests/unit/auth/test_users.py`
- **UserManager** (41 connections) — `server/auth/users.py`
- **RestartInvalidatingJWTStrategy** (13 connections) — `server/auth/jwt_strategy.py`
- **get_user_manager()** (13 connections) — `server/auth/users.py`
- **get_auth_backend()** (12 connections) — `server/auth/users.py`
- **get_user_db()** (11 connections) — `server/auth/users.py`
- **asyncio** (11 connections)
- **get_username_auth_backend()** (9 connections) — `server/auth/users.py`
- **test_jwt_strategy.py** (9 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **UsernameAuthenticationBackend** (8 connections) — `server/auth/users.py`
- **jwt_strategy.py** (7 connections) — `server/auth/jwt_strategy.py`
- **.read_token()** (7 connections) — `server/auth/jwt_strategy.py`
- **UUID** (7 connections)
- **.__init__()** (6 connections) — `server/auth/users.py`
- **.login()** (6 connections) — `server/auth/users.py`
- **test_read_token_accepts_matching_epoch()** (6 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **test_username_authentication_backend_login()** (6 connections) — `server/tests/unit/auth/test_users.py`
- **test_read_token_rejects_missing_epoch()** (5 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **test_read_token_rejects_wrong_epoch()** (5 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **test_get_user_manager()** (5 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_forgot_password()** (5 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_forgot_password_with_request()** (5 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_register_bogus_email()** (5 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_register_no_email()** (5 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_register_non_bogus_email()** (5 connections) — `server/tests/unit/auth/test_users.py`
- *... and 106 more nodes in this community*

## Relationships

- [useGameConnectionRefactored.ts](useGameConnectionRefactored.ts.md) (29 shared connections)
- [useMythosAppActions.ts](useMythosAppActions.ts.md) (11 shared connections)
- [NPCSpawnRule](NPCSpawnRule.md) (6 shared connections)
- [Room](Room.md) (2 shared connections)
- [test_admin_setlucidity_command.py](test_admin_setlucidity_command.py.md) (2 shared connections)
- [test_connection_session_management.py](test_connection_session_management.py.md) (2 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (2 shared connections)
- [test_db_connectivity_create_and_read_user](test_db_connectivity_create_and_read_user.md) (2 shared connections)
- [properties](properties.md) (1 shared connections)
- [test_lucidity_recovery_commands.py](test_lucidity_recovery_commands.py.md) (1 shared connections)

## Source Files

- `server/auth/jwt_strategy.py`
- `server/auth/users.py`
- `server/tests/unit/auth/test_jwt_strategy.py`
- `server/tests/unit/auth/test_users.py`

## Audit Trail

- EXTRACTED: 230 (88%)
- INFERRED: 31 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*