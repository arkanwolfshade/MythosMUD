# Test Auth Dependencies

> 91 nodes

## Key Concepts

- **LoggedHTTPException** (235 connections) — `server/exceptions.py`
- **api/player_respawn.py** (29 connections) — `server/api/player_respawn.py`
- **test_auth_dependencies.py** (26 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **auth/dependencies.py** (19 connections) — `server/auth/dependencies.py`
- **test_player_respawn_api.py** (18 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **TestMonitoringEndpoints** (16 connections) — `server/tests/unit/test_main.py`
- **test_player_respawn_handlers.py** (16 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **respawn_player()** (15 connections) — `server/api/player_respawn.py`
- **asyncio** (14 connections)
- **respawn_player_from_delirium()** (13 connections) — `server/api/player_respawn.py`
- **_handle_delirium_respawn_validation_error()** (12 connections) — `server/api/player_respawn.py`
- **_handle_respawn_validation_error()** (11 connections) — `server/api/player_respawn.py`
- **require_invite_code()** (11 connections) — `server/auth/dependencies.py`
- **_run_player_respawn()** (10 connections) — `server/api/player_respawn.py`
- **RespawnResponse** (9 connections) — `server/schemas/players/player_respawn.py`
- **get_current_superuser()** (9 connections) — `server/auth/dependencies.py`
- **_user()** (9 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **get_current_verified_user()** (8 connections) — `server/auth/dependencies.py`
- **_user()** (8 connections) — `server/tests/unit/api/test_player_respawn_handlers.py`
- **asyncio** (8 connections)
- **get_optional_current_user()** (6 connections) — `server/auth/dependencies.py`
- **test_respawn_player_from_delirium_not_found()** (6 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **test_respawn_player_not_found()** (6 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **test_respawn_player_validation_error()** (6 connections) — `server/tests/unit/api/test_player_respawn_api.py`
- **test_get_current_superuser_failure()** (6 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- *... and 66 more nodes in this community*

## Relationships

- [Container Exception Handling](Container_Exception_Handling.md) (51 shared connections)
- [Container/Inventory Helpers](Container-Inventory_Helpers.md) (42 shared connections)
- [Npc Admin](Npc_Admin.md) (33 shared connections)
- [Character Creation API](Character_Creation_API.md) (27 shared connections)
- [Monitoring](Monitoring.md) (19 shared connections)
- [Error Handling & Exceptions](Error_Handling_&_Exceptions.md) (19 shared connections)
- [Monitoring Models](Monitoring_Models.md) (17 shared connections)
- [Metrics](Metrics.md) (15 shared connections)
- [Test Command Factories Inventory](Test_Command_Factories_Inventory.md) (13 shared connections)
- [Test Rooms Write Api](Test_Rooms_Write_Api.md) (8 shared connections)
- [NPC Definitions API](NPC_Definitions_API.md) (6 shared connections)
- [Maps](Maps.md) (6 shared connections)

## Source Files

- `server/api/player_respawn.py`
- `server/auth/dependencies.py`
- `server/exceptions.py`
- `server/schemas/players/player_respawn.py`
- `server/tests/unit/api/test_player_respawn_api.py`
- `server/tests/unit/api/test_player_respawn_handlers.py`
- `server/tests/unit/auth/test_auth_dependencies.py`
- `server/tests/unit/test_exceptions.py`
- `server/tests/unit/test_exceptions_comprehensive.py`
- `server/tests/unit/test_main.py`

## Audit Trail

- EXTRACTED: 402 (80%)
- INFERRED: 99 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*