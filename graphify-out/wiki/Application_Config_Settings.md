# Application Config Settings

> 150 nodes

## Key Concepts

- **test_player_respawn_service.py** (48 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **player_respawn_service.py** (41 connections) — `server/services/player_respawn_service.py`
- **test_event_handler.py** (41 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **PlayerDPUpdated** (39 connections) — `server/events/event_types.py`
- **game.py** (32 connections) — `server/models/game.py`
- **test_player_schemas.py** (21 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- **PositionState** (20 connections) — `server/models/game.py`
- **PlayerRespawnedEvent** (19 connections) — `server/events/event_types.py`
- **PlayerDeliriumRespawnedEvent** (15 connections) — `server/events/event_types.py`
- **._subscribe_to_events()** (13 connections) — `server/realtime/event_handler.py`
- **test_game_enums.py** (11 connections) — `server/tests/unit/models/test_game_enums.py`
- **AttributeType** (8 connections) — `server/models/game.py`
- **LucidityActionCode** (8 connections) — `server/models/lucidity.py`
- **_utc_now()** (7 connections) — `server/services/player_respawn_service.py`
- **test_respawn_player_from_delirium_success()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_from_delirium_database_error()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **test_respawn_player_from_delirium_combat_clear_error()** (4 connections) — `server/tests/unit/services/test_player_respawn_service.py`
- **StrEnum** (3 connections)
- **test_event_handler_handle_npc_left()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_handle_player_dp_updated()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_handle_player_died()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_handle_player_dp_decay()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_handle_player_respawned()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_event_handler_handle_player_delirium_respawned()** (3 connections) — `server/tests/unit/realtime/test_event_handler.py`
- **test_player_base()** (3 connections) — `server/tests/unit/schemas/test_player_schemas.py`
- *... and 125 more nodes in this community*

## Relationships

- [Zone Config Loader](Zone_Config_Loader.md) (30 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (15 shared connections)
- [Enhanced Logging Exceptions](Enhanced_Logging_Exceptions.md) (15 shared connections)
- [Tailwind UI Migration Plan](Tailwind_UI_Migration_Plan.md) (14 shared connections)
- [Panel Layout Libraries Spec](Panel_Layout_Libraries_Spec.md) (14 shared connections)
- [Character Creation E2E](Character_Creation_E2E.md) (10 shared connections)
- [NPC Database Sessions](NPC_Database_Sessions.md) (10 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (10 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (9 shared connections)
- [Combat NPC Lookup](Combat_NPC_Lookup.md) (9 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (8 shared connections)
- [Look Command Helpers](Look_Command_Helpers.md) (6 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/models/game.py`
- `server/models/lucidity.py`
- `server/realtime/event_handler.py`
- `server/services/player_respawn_service.py`
- `server/tests/unit/models/test_game_enums.py`
- `server/tests/unit/realtime/test_event_handler.py`
- `server/tests/unit/schemas/test_player_schemas.py`
- `server/tests/unit/services/test_player_respawn_service.py`

## Audit Trail

- EXTRACTED: 507 (92%)
- INFERRED: 47 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*