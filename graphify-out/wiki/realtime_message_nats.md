# realtime message nats

> 11 nodes

## Key Concepts

- **_update_player_status_effects()** (9 connections) — `server/app/game_tick_processing.py`
- **_cleanup_single_decayed_corpse()** (8 connections) — `server/app/game_tick_processing.py`
- **Any** (7 connections)
- **test_update_player_status_effects_no_changes()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_update_player_status_effects_changes()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_update_player_status_effects_saves()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_cleanup_single_decayed_corpse_success()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **Update and save player status effects if changes occurred.      Returns:** (1 connections) — `server/app/game_tick_processing.py`
- **Cleanup a single decayed corpse.      Args:         corpse_service: Corpse lifec** (1 connections) — `server/app/game_tick_processing.py`
- **Test _update_player_status_effects() when no changes occurred.** (1 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **Test _update_player_status_effects() when changes occurred.** (1 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`

## Relationships

- [tick game processing](tick_game_processing.md) (6 shared connections)
- [map RoomMapViewer mapUtils](map_RoomMapViewer_mapUtils.md) (5 shared connections)
- [player persistence repository](player_persistence_repository.md) (3 shared connections)
- [persistence combat handler](persistence_combat_handler.md) (2 shared connections)
- [task registry app](task_registry_app.md) (1 shared connections)
- [nats services service](nats_services_service.md) (1 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing_async.py`

## Audit Trail

- EXTRACTED: 38 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*