# tick game processing

> 50 nodes

## Key Concepts

- **test_game_tick_processing_async.py** (26 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **_process_damage_over_time_effect()** (13 connections) — `server/app/game_tick_processing.py`
- **_process_single_effect()** (13 connections) — `server/app/game_tick_processing.py`
- **_process_heal_over_time_effect()** (10 connections) — `server/app/game_tick_processing.py`
- **_update_player_status_effects()** (9 connections) — `server/app/game_tick_processing.py`
- **test_process_damage_over_time_effect_no_damage()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_damage_over_time_effect_no_remaining()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_damage_over_time_effect_success()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_heal_over_time_effect_no_healing()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_heal_over_time_effect_no_remaining()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_heal_over_time_effect_success()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_single_effect_damage_over_time()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_single_effect_heal_over_time()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_single_effect_expired()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_update_player_status_effects_no_changes()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_update_player_status_effects_changes()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_status_effects_no_container()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_status_effects_no_online_players()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_combat_tick_no_service()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_combat_tick_success()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_heal_over_time_effect()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_damage_over_time_zero_remaining()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_single_effect_heal_expires()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_update_player_status_effects_saves()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **mock_app()** (2 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- *... and 25 more nodes in this community*

## Relationships

- [map RoomMapViewer mapUtils](map_RoomMapViewer_mapUtils.md) (24 shared connections)
- [realtime message nats](realtime_message_nats.md) (4 shared connections)
- [command utility models](command_utility_models.md) (1 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing_async.py`

## Audit Trail

- EXTRACTED: 153 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*