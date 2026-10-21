# schema.sql

> 120 nodes · cohesion 0.03

## Key Concepts

- **api/game.py** (32 connections) — `server/api/game.py`
- **test_auth_dependencies.py** (24 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_game.py** (20 connections) — `server/tests/unit/api/test_game.py`
- **broadcast_message()** (18 connections) — `server/api/game.py`
- **auth/dependencies.py** (18 connections) — `server/auth/dependencies.py`
- **get_mythos_time()** (15 connections) — `server/api/game.py`
- **asyncio** (14 connections)
- **get_current_superuser()** (12 connections) — `server/auth/dependencies.py`
- **require_invite_code()** (11 connections) — `server/auth/dependencies.py`
- **TestGetMythosTime** (11 connections) — `server/tests/unit/api/test_game.py`
- **get_game_status()** (8 connections) — `server/api/game.py`
- **get_current_verified_user()** (8 connections) — `server/auth/dependencies.py`
- **BroadcastMessageResponse** (8 connections) — `server/schemas/game/game.py`
- **GameStatusResponse** (8 connections) — `server/schemas/game/game.py`
- **MythosTimeResponse** (8 connections) — `server/schemas/game/game.py`
- **schemas/game/__init__.py** (8 connections) — `server/schemas/game/__init__.py`
- **game/game.py** (7 connections) — `server/schemas/game/game.py`
- **asyncio** (7 connections)
- **get_optional_current_user()** (6 connections) — `server/auth/dependencies.py`
- **BroadcastStats** (6 connections) — `server/schemas/game/game.py`
- **test_get_current_superuser_failure()** (6 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_get_current_superuser_with_none_user()** (6 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_get_current_verified_user_failure()** (6 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_get_current_verified_user_with_none_user()** (6 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_require_invite_code_invalid()** (6 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- *... and 95 more nodes in this community*

## Relationships

- [useGameConnectionRefactored.ts](useGameConnectionRefactored.ts.md) (20 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (13 shared connections)
- [useMythosAppActions.ts](useMythosAppActions.ts.md) (6 shared connections)
- [NPCCombatDataProvider](NPCCombatDataProvider.md) (5 shared connections)
- [test_admin_setlucidity_command.py](test_admin_setlucidity_command.py.md) (5 shared connections)
- [look_container.py](look_container.py.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [Room](Room.md) (3 shared connections)
- [WearableContainerServiceError](WearableContainerServiceError.md) (3 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (2 shared connections)
- [command_parser.py](command_parser.py.md) (2 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (2 shared connections)

## Source Files

- `server/api/game.py`
- `server/auth/dependencies.py`
- `server/schemas/game/__init__.py`
- `server/schemas/game/game.py`
- `server/tests/unit/api/test_game.py`
- `server/tests/unit/auth/test_auth_dependencies.py`

## Audit Trail

- EXTRACTED: 262 (93%)
- INFERRED: 19 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*