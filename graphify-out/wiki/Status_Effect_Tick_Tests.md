# Status Effect Tick Tests

> 39 nodes · cohesion 0.06

## Key Concepts

- **test_game_tick_processing_async.py** (25 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **_update_player_status_effects()** (7 connections) — `server/app/game_tick_processing.py`
- **test_process_combat_tick_no_service()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_combat_tick_success()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_damage_over_time_effect_no_damage()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_damage_over_time_effect_no_remaining()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_damage_over_time_effect_success()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_heal_over_time_effect_no_healing()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_heal_over_time_effect_no_remaining()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_heal_over_time_effect_success()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_single_effect_damage_over_time()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_single_effect_expired()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_single_effect_heal_over_time()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_status_effects_no_container()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_status_effects_no_online_players()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_update_player_status_effects_changes()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_update_player_status_effects_no_changes()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **mock_container()** (2 connections) — `server/tests/unit/api/test_game.py`
- **Create a mock application container.** (2 connections) — `server/tests/unit/api/test_game.py`
- **mock_app()** (2 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **mock_container()** (2 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **mock_player()** (2 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **Test _update_player_status_effects() when no changes occurred.** (2 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **Test _process_damage_over_time_effect() successful application.** (2 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **Unit tests for game tick processing functions.  Tests the game tick processing l** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- *... and 14 more nodes in this community*

## Relationships

- [[Game Tick Processing]] (21 shared connections)
- [[Game Status API]] (1 shared connections)
- [[App Game Tick]] (1 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/tests/unit/api/test_game.py`
- `server/tests/unit/app/test_game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing_async.py`

## Audit Trail

- EXTRACTED: 107 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
