# Test Player Respawn Service

> 105 nodes

## Key Concepts

- **test_player_respawn_service.py** (55 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **player_respawn_service.py** (40 connections) — `server/services/player_respawn_service.py`
- **asyncio** (27 connections)
- **spawn_defaults.py** (9 connections) — `server/constants/spawn_defaults.py`
- **_utc_now()** (7 connections) — `server/services/player_respawn_service.py`
- **fixture** (7 connections)
- **LucidityActionCode** (6 connections) — `server/models/lucidity.py`
- **_PlayerCombatClearing** (5 connections) — `server/services/player_respawn_service.py`
- **_RandomChoiceSource** (5 connections) — `server/services/player_respawn_service.py`
- **_RespawnEventPublisher** (5 connections) — `server/services/player_respawn_service.py`
- **test_respawn_player_from_delirium_combat_clear_error()** (5 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_from_delirium_database_error()** (5 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_from_delirium_success()** (5 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_from_sanitarium_success()** (5 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **.__init__()** (4 connections) — `server/services/player_respawn_service.py`
- **respawn_service()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **respawn_service_no_deps()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **sample_dead_player()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **sample_player()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_get_respawn_room_custom()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_get_respawn_room_database_error()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_get_respawn_room_default()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_get_respawn_room_player_not_found()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_move_player_to_limbo_database_error()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_move_player_to_limbo_player_not_found()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- *... and 80 more nodes in this community*

## Relationships

- [Player Model & Migrations](Player_Model_&_Migrations.md) (16 shared connections)
- [Lucidity Helpers & Catatonia](Lucidity_Helpers_&_Catatonia.md) (15 shared connections)
- [Lucidity & Rescue Service](Lucidity_&_Rescue_Service.md) (12 shared connections)
- [Error Handling & Exceptions](Error_Handling_&_Exceptions.md) (10 shared connections)
- [Test Event Handler](Test_Event_Handler.md) (7 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (3 shared connections)
- [Test Event Bus](Test_Event_Bus.md) (2 shared connections)
- [Test Inventory Command Coercion](Test_Inventory_Command_Coercion.md) (2 shared connections)
- [Dependency Injection (FastAPI)](Dependency_Injection_FastAPI.md) (2 shared connections)
- [Async Persistence & NPC Events](Async_Persistence_&_NPC_Events.md) (2 shared connections)
- [Game](Game.md) (2 shared connections)
- [Test Debrief Command](Test_Debrief_Command.md) (1 shared connections)

## Source Files

- `server/constants/spawn_defaults.py`
- `server/models/lucidity.py`
- `server/services/player_respawn_service.py`
- `server/tests/unit/services/test_player_respawn_service.py`

## Audit Trail

- EXTRACTED: 202 (89%)
- INFERRED: 26 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*