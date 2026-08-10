# Combat Client Crash Report

> 19 nodes

## Key Concepts

- **MovementService** (45 connections) — `server/game/movement_service.py`
- **Any** (7 connections)
- **._resolve_player_for_movement()** (6 connections) — `server/game/movement_service.py`
- **.__init__()** (5 connections) — `server/game/movement_service.py`
- **._persist_player_location()** (4 connections) — `server/game/movement_service.py`
- **._handle_tutorial_exit_if_applicable()** (4 connections) — `server/game/movement_service.py`
- **._record_move_validation_failure()** (4 connections) — `server/game/movement_service.py`
- **movement_service()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **test_movement_service_init_no_persistence()** (3 connections) — `server/tests/unit/game/test_movement_service.py`
- **.set_player_combat_service()** (2 connections) — `server/game/movement_service.py`
- **Service for handling atomic player movement operations.      This class provides** (1 connections) — `server/game/movement_service.py`
- **Initialize the movement service.          Args:             event_bus: Optional** (1 connections) — `server/game/movement_service.py`
- **Set the player combat service after initialization.          This allows the com** (1 connections) — `server/game/movement_service.py`
- **Resolve player by ID or name and return player object and resolved ID.** (1 connections) — `server/game/movement_service.py`
- **Update player location in database.** (1 connections) — `server/game/movement_service.py`
- **If player exited tutorial instance (moved to fixed exit room), clear and destroy** (1 connections) — `server/game/movement_service.py`
- **Record timing and monitor stats when movement validation fails.** (1 connections) — `server/game/movement_service.py`
- **Create a MovementService instance.** (1 connections) — `server/tests/unit/game/test_movement_service.py`
- **Test MovementService initialization without persistence raises error.** (1 connections) — `server/tests/unit/game/test_movement_service.py`

## Relationships

- [Room Map Viewer UI](Room_Map_Viewer_UI.md) (14 shared connections)
- [Command Request App State](Command_Request_App_State.md) (4 shared connections)
- [NPC Utility Functions](NPC_Utility_Functions.md) (3 shared connections)
- [NPC Service Tests](NPC_Service_Tests.md) (3 shared connections)
- [Game Magic Spell](Game_Magic_Spell.md) (3 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (3 shared connections)
- [Level and XP Curve](Level_and_XP_Curve.md) (3 shared connections)
- [Calendar Holiday Schemas](Calendar_Holiday_Schemas.md) (3 shared connections)
- [Error Logging Implementation](Error_Logging_Implementation.md) (2 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (2 shared connections)
- [Claude Agents Deps](Claude_Agents_Deps.md) (2 shared connections)
- [Cache and NPC Cache](Cache_and_NPC_Cache.md) (1 shared connections)

## Source Files

- `server/game/movement_service.py`
- `server/tests/unit/game/test_movement_service.py`

## Audit Trail

- EXTRACTED: 88 (96%)
- INFERRED: 4 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*