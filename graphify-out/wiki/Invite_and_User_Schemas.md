# Invite and User Schemas

> 135 nodes

## Key Concepts

- **game_tick_processing.py** (77 connections) — `server/app/game_tick_processing.py`
- **test_game_tick_processing_async.py** (26 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **_stats_int()** (17 connections) — `server/models/player.py`
- **FastAPI** (16 connections)
- **get_current_tick()** (15 connections) — `server/app/game_tick_processing.py`
- **test_game_tick_processing.py** (15 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **game_tick_loop()** (14 connections) — `server/app/game_tick_processing.py`
- **_validate_app_state_for_status_effects()** (12 connections) — `server/app/game_tick_processing.py`
- **_process_damage_over_time_effect()** (11 connections) — `server/app/game_tick_processing.py`
- **_process_single_effect()** (11 connections) — `server/app/game_tick_processing.py`
- **UUID** (9 connections)
- **process_status_effects()** (9 connections) — `server/app/game_tick_processing.py`
- **broadcast_tick_event()** (9 connections) — `server/app/game_tick_processing.py`
- **get_tick_interval()** (8 connections) — `server/app/game_tick_processing.py`
- **Any** (8 connections)
- **_process_heal_over_time_effect()** (8 connections) — `server/app/game_tick_processing.py`
- **_handle_player_death_threshold()** (8 connections) — `server/app/game_tick_processing.py`
- **_process_mortally_wounded_player()** (8 connections) — `server/app/game_tick_processing.py`
- **_process_session_dp_decay_and_death()** (8 connections) — `server/app/game_tick_processing.py`
- **_update_player_status_effects()** (7 connections) — `server/app/game_tick_processing.py`
- **_process_player_status_effects()** (7 connections) — `server/app/game_tick_processing.py`
- **process_player_effects_expiration()** (7 connections) — `server/app/game_tick_processing.py`
- **process_combat_tick()** (7 connections) — `server/app/game_tick_processing.py`
- **AsyncSession** (7 connections)
- **cleanup_decayed_corpses()** (7 connections) — `server/app/game_tick_processing.py`
- *... and 110 more nodes in this community*

## Relationships

- [Player Creation Service](Player_Creation_Service.md) (12 shared connections)
- [Player Respawn Events](Player_Respawn_Events.md) (9 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (8 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (5 shared connections)
- [Test Optimization Insights](Test_Optimization_Insights.md) (5 shared connections)
- [Test Modernization Plan](Test_Modernization_Plan.md) (4 shared connections)
- [NPCMaintenanceConfig](NPCMaintenanceConfig.md) (3 shared connections)
- [E 2 E Testing Guide](E_2_E_Testing_Guide.md) (3 shared connections)
- [Player State Factories](Player_State_Factories.md) (3 shared connections)
- [Restart Invalidating JWT](Restart_Invalidating_JWT.md) (3 shared connections)
- [Archive Frd Random](Archive_Frd_Random.md) (2 shared connections)
- [Communication Command Flows](Communication_Command_Flows.md) (2 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/models/player.py`
- `server/tests/unit/app/test_game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing_async.py`
- `server/tests/unit/commands/test_inventory_command_coercion.py`

## Audit Trail

- EXTRACTED: 553 (99%)
- INFERRED: 5 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*