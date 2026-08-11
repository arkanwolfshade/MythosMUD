# NPC Combat Lifecycle

> 207 nodes

## Key Concepts

- **User** (314 connections) — `server/models/user.py`
- **Result** (52 connections) — `scripts/run_test_ci.py`
- **endpoints.py** (52 connections) — `server/auth/endpoints.py`
- **test_endpoints.py** (51 connections) — `server/tests/unit/auth/test_endpoints.py`
- **register_user()** (28 connections) — `server/auth/endpoints.py`
- **login_user()** (28 connections) — `server/auth/endpoints.py`
- **UserCreate** (27 connections) — `server/auth/endpoints.py`
- **InviteManager** (24 connections) — `server/auth/invites.py`
- **LoginRequest** (22 connections) — `server/auth/endpoints.py`
- **invites.py** (16 connections) — `server/auth/invites.py`
- **get_shutdown_blocking_message()** (13 connections) — `server/commands/admin_shutdown_command.py`
- **RestartInvalidatingJWTStrategy** (12 connections) — `server/auth/jwt_strategy.py`
- **test_user.py** (11 connections) — `server/tests/unit/models/test_user.py`
- **list_invites()** (10 connections) — `server/auth/endpoints.py`
- **InviteRead** (10 connections) — `server/schemas/auth/invite.py`
- **create_invite()** (9 connections) — `server/auth/endpoints.py`
- **test_jwt_strategy.py** (9 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **_check_shutdown_status()** (8 connections) — `server/auth/endpoints.py`
- **Request** (8 connections)
- **token_epoch.py** (8 connections) — `server/auth/token_epoch.py`
- **get_auth_epoch()** (8 connections) — `server/auth/token_epoch.py`
- **LoginResponse** (7 connections) — `server/auth/endpoints.py`
- **_validate_invite_code()** (7 connections) — `server/auth/endpoints.py`
- **_check_username_exists()** (7 connections) — `server/auth/endpoints.py`
- **_find_user_by_username()** (7 connections) — `server/auth/endpoints.py`
- *... and 182 more nodes in this community*

## Relationships

- [Combat Command Handler](Combat_Command_Handler.md) (72 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (48 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (27 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (27 shared connections)
- [Async Persistence Delegates](Async_Persistence_Delegates.md) (25 shared connections)
- [Game Mechanics Service](Game_Mechanics_Service.md) (21 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (18 shared connections)
- [NATS Metrics API](NATS_Metrics_API.md) (14 shared connections)
- [Container Persistence Ops](Container_Persistence_Ops.md) (12 shared connections)
- [E 2 E Scenarios Scenario](E_2_E_Scenarios_Scenario.md) (11 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (10 shared connections)
- [Client Event Store](Client_Event_Store.md) (9 shared connections)

## Source Files

- `scripts/run_test_ci.py`
- `server/auth/endpoints.py`
- `server/auth/invites.py`
- `server/auth/jwt_strategy.py`
- `server/auth/token_epoch.py`
- `server/commands/admin_shutdown_command.py`
- `server/models/user.py`
- `server/schemas/auth/invite.py`
- `server/tests/integration/test_db_connectivity.py`
- `server/tests/unit/api/conftest.py`
- `server/tests/unit/api/test_container_exception_handlers.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_container_helpers_loot.py`
- `server/tests/unit/api/test_containers.py`
- `server/tests/unit/auth/test_endpoints.py`
- `server/tests/unit/auth/test_jwt_strategy.py`
- `server/tests/unit/models/test_user.py`
- `server/tests/unit/services/test_player_preferences_service.py`

## Audit Trail

- EXTRACTED: 1036 (84%)
- INFERRED: 193 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*