# User

> 185 nodes

## Key Concepts

- **User** (293 connections) — `server/models/user.py`
- **endpoints.py** (64 connections) — `server/auth/endpoints.py`
- **login_user()** (35 connections) — `server/auth/endpoints.py`
- **register_user()** (32 connections) — `server/auth/endpoints.py`
- **UserCreate** (24 connections) — `server/auth/endpoints.py`
- **test_endpoints_register.py** (22 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **LoginRequest** (21 connections) — `server/auth/endpoints.py`
- **test_endpoints_login.py** (19 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **list_invites()** (14 connections) — `server/auth/endpoints.py`
- **test_endpoints_invites.py** (14 connections) — `server/tests/unit/auth/test_endpoints_invites.py`
- **asyncio** (14 connections)
- **get_shutdown_blocking_message()** (13 connections) — `server/commands/admin_shutdown_command.py`
- **InviteRead** (12 connections) — `server/schemas/auth/invite.py`
- **get_current_superuser()** (12 connections) — `server/auth/dependencies.py`
- **create_invite()** (12 connections) — `server/auth/endpoints.py`
- **asyncio** (11 connections)
- **test_user.py** (11 connections) — `server/tests/unit/models/test_user.py`
- **test_endpoints_login_profession.py** (10 connections) — `server/tests/unit/auth/test_endpoints_login_profession.py`
- **get_current_user_info()** (9 connections) — `server/auth/endpoints.py`
- **_authenticate_user_credentials()** (8 connections) — `server/auth/endpoints.py`
- **_check_shutdown_status()** (8 connections) — `server/auth/endpoints.py`
- **_generate_jwt_token()** (8 connections) — `server/auth/endpoints.py`
- **Request** (8 connections)
- **_find_user_by_username()** (7 connections) — `server/auth/endpoints.py`
- **_get_user_characters()** (7 connections) — `server/auth/endpoints.py`
- *... and 160 more nodes in this community*

## Relationships

- [models/user.py](models-user.py.md) (42 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (39 shared connections)
- [test_users.py](test_users.py.md) (28 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (25 shared connections)
- [maps.py](maps.py.md) (21 shared connections)
- [PlayerService](PlayerService.md) (20 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (18 shared connections)
- [get_admin_auth_service](get_admin_auth_service.md) (14 shared connections)
- [DatabaseError](DatabaseError.md) (13 shared connections)
- [npc_definitions_api.py](npc_definitions_api.py.md) (9 shared connections)
- [Player](Player.md) (8 shared connections)
- [test_users_current_user_logging.py](test_users_current_user_logging.py.md) (8 shared connections)

## Source Files

- `server/auth/dependencies.py`
- `server/auth/endpoints.py`
- `server/commands/admin_shutdown_command.py`
- `server/models/user.py`
- `server/schemas/auth/invite.py`
- `server/tests/unit/auth/test_auth_dependencies.py`
- `server/tests/unit/auth/test_endpoints_invites.py`
- `server/tests/unit/auth/test_endpoints_login.py`
- `server/tests/unit/auth/test_endpoints_login_profession.py`
- `server/tests/unit/auth/test_endpoints_register.py`
- `server/tests/unit/infrastructure/test_async_persistence_core.py`
- `server/tests/unit/models/test_user.py`

## Audit Trail

- EXTRACTED: 593 (80%)
- INFERRED: 146 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*