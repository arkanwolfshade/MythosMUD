# useGameConnectionRefactored.ts

> 254 nodes · cohesion 0.02

## Key Concepts

- **User** (331 connections) — `server/models/user.py`
- **endpoints.py** (66 connections) — `server/auth/endpoints.py`
- **login_user()** (35 connections) — `server/auth/endpoints.py`
- **register_user()** (31 connections) — `server/auth/endpoints.py`
- **UserCreate** (31 connections) — `server/auth/endpoints.py`
- **test_endpoints_register.py** (30 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **LoginRequest** (22 connections) — `server/auth/endpoints.py`
- **test_endpoints_login.py** (20 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **asyncio** (18 connections)
- **test_invite_schemas.py** (15 connections) — `server/tests/unit/schemas/test_invite_schemas.py`
- **list_invites()** (14 connections) — `server/auth/endpoints.py`
- **test_endpoints_invites.py** (14 connections) — `server/tests/unit/auth/test_endpoints_invites.py`
- **schemas/auth/__init__.py** (13 connections) — `server/schemas/auth/__init__.py`
- **create_invite()** (12 connections) — `server/auth/endpoints.py`
- **_persist_new_user()** (12 connections) — `server/auth/endpoints.py`
- **InviteRead** (12 connections) — `server/schemas/auth/invite.py`
- **test_users_current_user_logging.py** (12 connections) — `server/tests/unit/auth/test_users_current_user_logging.py`
- **get_current_user_with_logging()** (11 connections) — `server/auth/users.py`
- **asyncio** (11 connections)
- **test_user.py** (11 connections) — `server/tests/unit/models/test_user.py`
- **InviteBase** (10 connections) — `server/schemas/auth/invite.py`
- **test_endpoints_login_profession.py** (10 connections) — `server/tests/unit/auth/test_endpoints_login_profession.py`
- **_mock_invite_manager()** (10 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **get_current_user_info()** (9 connections) — `server/auth/endpoints.py`
- **InviteUpdate** (9 connections) — `server/schemas/auth/invite.py`
- *... and 229 more nodes in this community*

## Relationships

- [test_security_validator.py](test_security_validator.py.md) (60 shared connections)
- [useMythosAppActions.ts](useMythosAppActions.ts.md) (52 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (35 shared connections)
- [._create_grid_map](_create_grid_map.md) (29 shared connections)
- [active_lucidity_service.py](active_lucidity_service.py.md) (24 shared connections)
- [schema.sql](schema.sql.md) (20 shared connections)
- [test_admin_setlucidity_command.py](test_admin_setlucidity_command.py.md) (16 shared connections)
- [test_look_player.py](test_look_player.py.md) (16 shared connections)
- [test_npc_startup_service.py](test_npc_startup_service.py.md) (14 shared connections)
- [test_websocket_handler_helpers_extended.py](test_websocket_handler_helpers_extended.py.md) (14 shared connections)
- [get_logger](get_logger.md) (11 shared connections)
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (10 shared connections)

## Source Files

- `server/auth/endpoints.py`
- `server/auth/invites.py`
- `server/auth/token_epoch.py`
- `server/auth/users.py`
- `server/models/user.py`
- `server/schemas/auth/__init__.py`
- `server/schemas/auth/invite.py`
- `server/tests/integration/test_db_connectivity.py`
- `server/tests/integration/test_integration_cleanup.py`
- `server/tests/unit/auth/test_endpoints_invites.py`
- `server/tests/unit/auth/test_endpoints_login.py`
- `server/tests/unit/auth/test_endpoints_login_profession.py`
- `server/tests/unit/auth/test_endpoints_register.py`
- `server/tests/unit/auth/test_users_current_user_logging.py`
- `server/tests/unit/models/test_user.py`
- `server/tests/unit/schemas/test_invite_schemas.py`

## Audit Trail

- EXTRACTED: 765 (83%)
- INFERRED: 153 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*