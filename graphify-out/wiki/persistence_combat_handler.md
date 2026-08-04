# persistence combat handler

> 16 nodes

## Key Concepts

- **FastAPI** (16 connections)
- **process_status_effects()** (12 connections) — `server/app/game_tick_processing.py`
- **_process_all_status_effects()** (8 connections) — `server/app/game_tick_processing.py`
- **_validate_and_get_player()** (7 connections) — `server/app/game_tick_processing.py`
- **_process_player_status_effects()** (7 connections) — `server/app/game_tick_processing.py`
- **test_process_status_effects_no_online_players()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_validate_and_get_player_invalid_id()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_validate_and_get_player_success()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_all_status_effects_empty()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_status_effects_no_online_players()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_status_effects_with_online_player()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **Validate container and retrieve player by ID.      Args:         container: Appl** (1 connections) — `server/app/game_tick_processing.py`
- **Process all status effects for a player.      Args:         app: FastAPI applica** (1 connections) — `server/app/game_tick_processing.py`
- **Process status effects for a single player.      Returns:         True if player** (1 connections) — `server/app/game_tick_processing.py`
- **Process status effects for online players.** (1 connections) — `server/app/game_tick_processing.py`
- **Test process_status_effects() when no online players.** (1 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`

## Relationships

- [map RoomMapViewer mapUtils](map_RoomMapViewer_mapUtils.md) (15 shared connections)
- [player persistence repository](player_persistence_repository.md) (7 shared connections)
- [tick game processing](tick_game_processing.md) (6 shared connections)
- [game magic regeneration](game_magic_regeneration.md) (2 shared connections)
- [realtime message nats](realtime_message_nats.md) (2 shared connections)
- [config rationale config()](config_rationale_config%28%29.md) (1 shared connections)
- [npc aggressive mob](npc_aggressive_mob.md) (1 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing_async.py`

## Audit Trail

- EXTRACTED: 68 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*