# auth users rationale

> 246 nodes

## Key Concepts

- **endpoints.py** (61 connections) — `server/auth/endpoints.py`
- **test_users.py** (50 connections) — `server/tests/unit/auth/test_users.py`
- **users.py** (49 connections) — `server/auth/users.py`
- **UserManager** (46 connections) — `server/auth/users.py`
- **login_user()** (33 connections) — `server/auth/endpoints.py`
- **register_user()** (31 connections) — `server/auth/endpoints.py`
- **UserCreate** (27 connections) — `server/auth/endpoints.py`
- **InviteManager** (25 connections) — `server/auth/invites.py`
- **test_endpoints_register.py** (22 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **dependencies.py** (18 connections) — `server/auth/dependencies.py`
- **invites.py** (16 connections) — `server/auth/invites.py`
- **list_invites()** (13 connections) — `server/auth/endpoints.py`
- **get_user_manager()** (13 connections) — `server/auth/users.py`
- **get_current_superuser()** (12 connections) — `server/auth/dependencies.py`
- **RestartInvalidatingJWTStrategy** (12 connections) — `server/auth/jwt_strategy.py`
- **get_auth_backend()** (12 connections) — `server/auth/users.py`
- **create_invite()** (11 connections) — `server/auth/endpoints.py`
- **get_user_db()** (11 connections) — `server/auth/users.py`
- **invite.py** (11 connections) — `server/models/invite.py`
- **set_auth_epoch()** (10 connections) — `server/auth/token_epoch.py`
- **get_invite_manager()** (9 connections) — `server/auth/invites.py`
- **UsernameAuthenticationBackend** (9 connections) — `server/auth/users.py`
- **get_username_auth_backend()** (9 connections) — `server/auth/users.py`
- **test_jwt_strategy.py** (9 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **_check_shutdown_status()** (8 connections) — `server/auth/endpoints.py`
- *... and 221 more nodes in this community*

## Relationships

- [ascii map renderer](ascii_map_renderer.md) (62 shared connections)
- [command inventory factories](command_inventory_factories.md) (18 shared connections)
- [Exception Containers](Exception_Containers.md) (18 shared connections)
- [player requests schemas](player_requests_schemas.md) (16 shared connections)
- [command factories moderation](command_factories_moderation.md) (14 shared connections)
- [player preferences service](player_preferences_service.md) (11 shared connections)
- [useWebSocketConnectionTestFixtures useWe](useWebSocketConnectionTestFixtures_useWe.md) (9 shared connections)
- [logging file setup](logging_file_setup.md) (9 shared connections)
- [Database Config](Database_Config.md) (7 shared connections)
- [auth users rationale](auth_users_rationale.md) (6 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (6 shared connections)
- [admin auth service](admin_auth_service.md) (6 shared connections)

## Source Files

- `server/app/factory.py`
- `server/auth/__init__.py`
- `server/auth/dependencies.py`
- `server/auth/endpoints.py`
- `server/auth/invites.py`
- `server/auth/jwt_strategy.py`
- `server/auth/token_epoch.py`
- `server/auth/users.py`
- `server/models/invite.py`
- `server/tests/unit/auth/conftest.py`
- `server/tests/unit/auth/test_endpoints_register.py`
- `server/tests/unit/auth/test_jwt_strategy.py`
- `server/tests/unit/auth/test_users.py`

## Audit Trail

- EXTRACTED: 1015 (94%)
- INFERRED: 68 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*