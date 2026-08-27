# models/container.py

> 146 nodes

## Key Concepts

- **test_users.py** (55 connections) — `server/tests/unit/auth/test_users.py`
- **users.py** (48 connections) — `server/auth/users.py`
- **UserManager** (38 connections) — `server/auth/users.py`
- **RestartInvalidatingJWTStrategy** (13 connections) — `server/auth/jwt_strategy.py`
- **get_auth_backend()** (12 connections) — `server/auth/users.py`
- **get_user_db()** (11 connections) — `server/auth/users.py`
- **get_user_manager()** (11 connections) — `server/auth/users.py`
- **asyncio** (11 connections)
- **test_jwt_strategy.py** (10 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **get_username_auth_backend()** (9 connections) — `server/auth/users.py`
- **UsernameAuthenticationBackend** (8 connections) — `server/auth/users.py`
- **token_epoch.py** (8 connections) — `server/auth/token_epoch.py`
- **.read_token()** (7 connections) — `server/auth/jwt_strategy.py`
- **server/auth/__init__.py** (7 connections) — `server/auth/__init__.py`
- **jwt_strategy.py** (7 connections) — `server/auth/jwt_strategy.py`
- **UUID** (7 connections)
- **get_auth_epoch()** (6 connections) — `server/auth/token_epoch.py`
- **set_auth_epoch()** (6 connections) — `server/auth/token_epoch.py`
- **.login()** (6 connections) — `server/auth/users.py`
- **test_read_token_accepts_matching_epoch()** (6 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **test_username_authentication_backend_login()** (6 connections) — `server/tests/unit/auth/test_users.py`
- **.__init__()** (5 connections) — `server/auth/users.py`
- **.on_after_register()** (5 connections) — `server/auth/users.py`
- **test_read_token_rejects_missing_epoch()** (5 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **test_read_token_rejects_wrong_epoch()** (5 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- *... and 121 more nodes in this community*

## Relationships

- [NATSServicePoolMixin](NATSServicePoolMixin.md) (21 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (9 shared connections)
- [maps.py](maps.py.md) (6 shared connections)
- [UserManager](UserManager.md) (4 shared connections)
- [auth_rate_limit.py](auth_rate_limit.py.md) (3 shared connections)
- [NPC Combat Start Race Condition](NPC_Combat_Start_Race_Condition.md) (2 shared connections)
- [test_player_position_service.py](test_player_position_service.py.md) (2 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (2 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (2 shared connections)
- [useRespawnHandlers.ts](useRespawnHandlers.ts.md) (2 shared connections)
- [Gladiator Ring (Arena) Implementation Plan](Gladiator_Ring_Arena_Implementation_Plan.md) (2 shared connections)
- [ContainerComponent](ContainerComponent.md) (2 shared connections)

## Source Files

- `server/auth/__init__.py`
- `server/auth/jwt_strategy.py`
- `server/auth/token_epoch.py`
- `server/auth/users.py`
- `server/tests/unit/auth/test_jwt_strategy.py`
- `server/tests/unit/auth/test_users.py`

## Audit Trail

- EXTRACTED: 285 (91%)
- INFERRED: 28 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*