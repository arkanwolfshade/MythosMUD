# CombatService

> 254 nodes · cohesion 0.02

## Key Concepts

- **game_tick_processing.py** (60 connections) — `server/app/game_tick_processing.py`
- **game_tick_death.py** (48 connections) — `server/app/game_tick_death.py`
- **test_game_tick_processing.py** (43 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_game_tick_death.py** (40 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **game_tick_status_effects.py** (32 connections) — `server/app/game_tick_status_effects.py`
- **game_tick_protocols.py** (31 connections) — `server/app/game_tick_protocols.py`
- **_TickContainer** (25 connections) — `server/app/game_tick_protocols.py`
- **game_tick_corpses.py** (24 connections) — `server/app/game_tick_corpses.py`
- **asyncio** (21 connections)
- **test_game_tick_processing_async.py** (21 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **asyncio** (21 connections)
- **game_tick_loop()** (20 connections) — `server/app/game_tick_processing.py`
- **_process_mortally_wounded_player()** (16 connections) — `server/app/game_tick_death.py`
- **asyncio** (15 connections)
- **_app_container()** (14 connections) — `server/app/game_tick_protocols.py`
- **_process_single_effect()** (14 connections) — `server/app/game_tick_status_effects.py`
- **_validate_app_state_for_status_effects()** (14 connections) — `server/app/game_tick_status_effects.py`
- **broadcast_tick_event()** (13 connections) — `server/app/game_tick_processing.py`
- **_process_damage_over_time_effect()** (13 connections) — `server/app/game_tick_status_effects.py`
- **process_status_effects()** (13 connections) — `server/app/game_tick_status_effects.py`
- **cleanup_decayed_corpses()** (12 connections) — `server/app/game_tick_corpses.py`
- **_process_mp_regeneration()** (11 connections) — `server/app/game_tick_death.py`
- **_process_passive_corruption_flux()** (11 connections) — `server/app/game_tick_death.py`
- **_process_heal_over_time_effect()** (11 connections) — `server/app/game_tick_status_effects.py`
- **process_dp_decay_and_death()** (10 connections) — `server/app/game_tick_death.py`
- *... and 229 more nodes in this community*

## Relationships

- [Room](Room.md) (16 shared connections)
- [InventorySchemaValidationError](InventorySchemaValidationError.md) (11 shared connections)
- [FollowService](FollowService.md) (11 shared connections)
- [ChatLogger](ChatLogger.md) (10 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (8 shared connections)
- [test_player_combat_service.py](test_player_combat_service.py.md) (6 shared connections)
- [ConnectionManager](ConnectionManager.md) (6 shared connections)
- [command_parser.py](command_parser.py.md) (4 shared connections)
- [RoomNodeData](RoomNodeData.md) (4 shared connections)
- [manual_dependency_analysis.py](manual_dependency_analysis.py.md) (4 shared connections)
- [connection_manager_methods.py](connection_manager_methods.py.md) (3 shared connections)
- [fixtures/auth.ts](fixtures-auth.ts.md) (3 shared connections)

## Source Files

- `server/app/game_tick_corpses.py`
- `server/app/game_tick_counter.py`
- `server/app/game_tick_death.py`
- `server/app/game_tick_processing.py`
- `server/app/game_tick_protocols.py`
- `server/app/game_tick_status_effects.py`
- `server/config/npc_config.py`
- `server/services/combat_messaging_integration.py`
- `server/tests/unit/app/test_game_tick_death.py`
- `server/tests/unit/app/test_game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing_async.py`

## Audit Trail

- EXTRACTED: 655 (94%)
- INFERRED: 40 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*