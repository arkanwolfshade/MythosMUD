# Test Game Tick Processing Async

> 48 nodes

## Key Concepts

- **test_game_tick_processing_async.py** (23 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **asyncio** (15 connections)
- **_process_single_effect()** (14 connections) — `server/app/game_tick_status_effects.py`
- **_process_damage_over_time_effect()** (13 connections) — `server/app/game_tick_status_effects.py`
- **_process_heal_over_time_effect()** (11 connections) — `server/app/game_tick_status_effects.py`
- **_update_player_status_effects()** (9 connections) — `server/app/game_tick_status_effects.py`
- **Player** (6 connections)
- **test_process_combat_tick_no_service()** (4 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_combat_tick_success()** (4 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_damage_over_time_effect_no_damage()** (4 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_damage_over_time_effect_no_remaining()** (4 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_damage_over_time_effect_success()** (4 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_heal_over_time_effect_no_healing()** (4 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_heal_over_time_effect_no_remaining()** (4 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_heal_over_time_effect_success()** (4 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_single_effect_damage_over_time()** (4 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_single_effect_expired()** (4 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_single_effect_heal_over_time()** (4 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_status_effects_no_container()** (4 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_status_effects_no_online_players()** (4 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_update_player_status_effects_changes()** (4 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_update_player_status_effects_no_changes()** (4 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **mock_app()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **mock_container()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **mock_player()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- *... and 23 more nodes in this community*

## Relationships

- [Game Tick Status Effects](Game_Tick_Status_Effects.md) (12 shared connections)
- [Game Tick Processing](Game_Tick_Processing.md) (8 shared connections)
- [Game Tick Death](Game_Tick_Death.md) (4 shared connections)
- [Test Game Tick Processing](Test_Game_Tick_Processing.md) (4 shared connections)
- [Test Inventory Command Coercion](Test_Inventory_Command_Coercion.md) (3 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (2 shared connections)
- [Game State Provider](Game_State_Provider.md) (1 shared connections)

## Source Files

- `server/app/game_tick_status_effects.py`
- `server/tests/unit/app/test_game_tick_processing_async.py`

## Audit Trail

- EXTRACTED: 93 (85%)
- INFERRED: 17 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*