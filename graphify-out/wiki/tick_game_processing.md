# tick game processing

> 37 nodes

## Key Concepts

- **test_game_tick_processing_async.py** (26 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **_process_damage_over_time_effect()** (13 connections) — `server/app/game_tick_processing.py`
- **_process_single_effect()** (13 connections) — `server/app/game_tick_processing.py`
- **_process_heal_over_time_effect()** (10 connections) — `server/app/game_tick_processing.py`
- **test_process_damage_over_time_effect_no_damage()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_damage_over_time_effect_no_remaining()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_damage_over_time_effect_success()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_heal_over_time_effect_no_healing()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_heal_over_time_effect_no_remaining()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_heal_over_time_effect_success()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_single_effect_damage_over_time()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_single_effect_heal_over_time()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_single_effect_expired()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_status_effects_no_container()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_heal_over_time_effect()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_damage_over_time_zero_remaining()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_single_effect_heal_expires()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **mock_app()** (2 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **mock_container()** (2 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **mock_player()** (2 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **Process a damage over time effect.      Returns:         True if effect was appl** (1 connections) — `server/app/game_tick_processing.py`
- **Process a heal over time effect.      Returns:         True if effect was applie** (1 connections) — `server/app/game_tick_processing.py`
- **Process a single status effect.      Returns:         Tuple of (updated_effect_d** (1 connections) — `server/app/game_tick_processing.py`
- **Unit tests for game tick processing async functions.  Tests the async game tick** (1 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **Create a mock FastAPI app.** (1 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- *... and 12 more nodes in this community*

## Relationships

- [persistence combat handler](persistence_combat_handler.md) (6 shared connections)
- [realtime message nats](realtime_message_nats.md) (6 shared connections)
- [map RoomMapViewer mapUtils](map_RoomMapViewer_mapUtils.md) (6 shared connections)
- [player persistence repository](player_persistence_repository.md) (5 shared connections)
- [config rationale config()](config_rationale_config%28%29.md) (3 shared connections)
- [command utility models](command_utility_models.md) (1 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing_async.py`

## Audit Trail

- EXTRACTED: 121 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*