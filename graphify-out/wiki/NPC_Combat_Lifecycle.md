# NPC Combat Lifecycle

> 171 nodes

## Key Concepts

- **Result** (52 connections) — `scripts/run_test_ci.py`
- **endpoints.py** (52 connections) — `server/auth/endpoints.py`
- **test_endpoints.py** (51 connections) — `server/tests/unit/auth/test_endpoints.py`
- **register_user()** (28 connections) — `server/auth/endpoints.py`
- **login_user()** (28 connections) — `server/auth/endpoints.py`
- **UserCreate** (27 connections) — `server/auth/endpoints.py`
- **InviteManager** (24 connections) — `server/auth/invites.py`
- **LoginRequest** (22 connections) — `server/auth/endpoints.py`
- **invites.py** (16 connections) — `server/auth/invites.py`
- **is_shutdown_pending()** (14 connections) — `server/commands/admin_shutdown_command.py`
- **get_shutdown_blocking_message()** (13 connections) — `server/commands/admin_shutdown_command.py`
- **list_invites()** (10 connections) — `server/auth/endpoints.py`
- **InviteRead** (10 connections) — `server/schemas/auth/invite.py`
- **create_invite()** (9 connections) — `server/auth/endpoints.py`
- **_check_shutdown_status()** (8 connections) — `server/auth/endpoints.py`
- **Request** (8 connections)
- **get_auth_epoch()** (8 connections) — `server/auth/token_epoch.py`
- **get_user_manager()** (8 connections) — `server/auth/users.py`
- **__init__.py** (7 connections) — `server/auth/__init__.py`
- **LoginResponse** (7 connections) — `server/auth/endpoints.py`
- **_validate_invite_code()** (7 connections) — `server/auth/endpoints.py`
- **_check_username_exists()** (7 connections) — `server/auth/endpoints.py`
- **_find_user_by_username()** (7 connections) — `server/auth/endpoints.py`
- **_authenticate_user_credentials()** (7 connections) — `server/auth/endpoints.py`
- **test_register_user_duplicate_username()** (7 connections) — `server/tests/unit/auth/test_endpoints.py`
- *... and 146 more nodes in this community*

## Relationships

- [Room Occupancy Class](Room_Occupancy_Class.md) (46 shared connections)
- [Async Persistence Delegates](Async_Persistence_Delegates.md) (25 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (24 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (15 shared connections)
- [Room Drop Renderer](Room_Drop_Renderer.md) (11 shared connections)
- [E 2 E Scenarios Scenario](E_2_E_Scenarios_Scenario.md) (9 shared connections)
- [Plan Cursor Plans](Plan_Cursor_Plans.md) (7 shared connections)
- [Client Event Store](Client_Event_Store.md) (6 shared connections)
- [Game Mechanics Service](Game_Mechanics_Service.md) (6 shared connections)
- [Combat Flee Command](Combat_Flee_Command.md) (6 shared connections)
- [Realtime Conftest Mocks](Realtime_Conftest_Mocks.md) (4 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (3 shared connections)

## Source Files

- `scripts/run_test_ci.py`
- `server/auth/__init__.py`
- `server/auth/endpoints.py`
- `server/auth/invites.py`
- `server/auth/token_epoch.py`
- `server/auth/users.py`
- `server/commands/admin_shutdown_command.py`
- `server/schemas/auth/invite.py`
- `server/tests/unit/auth/test_endpoints.py`
- `server/tests/unit/commands/test_admin_shutdown_command.py`
- `server/tests/unit/services/test_player_preferences_service.py`

## Audit Trail

- EXTRACTED: 720 (86%)
- INFERRED: 118 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*