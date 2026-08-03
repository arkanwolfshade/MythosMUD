# realtime message nats

> 12 nodes

## Key Concepts

- **_process_mp_regeneration()** (8 connections) — `server/app/game_tick_processing.py`
- **_cleanup_single_decayed_corpse()** (8 connections) — `server/app/game_tick_processing.py`
- **Any** (7 connections)
- **_process_single_player_mp_regeneration()** (7 connections) — `server/app/game_tick_processing.py`
- **_validate_mp_regeneration_services()** (5 connections) — `server/app/game_tick_processing.py`
- **test_process_single_player_mp_regeneration()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_validate_mp_regeneration_services()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_cleanup_single_decayed_corpse_success()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **Validate that required services exist for MP regeneration.      Args:         co** (1 connections) — `server/app/game_tick_processing.py`
- **Process MP regeneration for a single player.      Args:         mp_service: MP r** (1 connections) — `server/app/game_tick_processing.py`
- **Process MP regeneration for online players.** (1 connections) — `server/app/game_tick_processing.py`
- **Cleanup a single decayed corpse.      Args:         corpse_service: Corpse lifec** (1 connections) — `server/app/game_tick_processing.py`

## Relationships

- [map RoomMapViewer mapUtils](map_RoomMapViewer_mapUtils.md) (14 shared connections)
- [tick game processing](tick_game_processing.md) (4 shared connections)
- [player persistence repository](player_persistence_repository.md) (2 shared connections)
- [commands follow rationale](commands_follow_rationale.md) (1 shared connections)
- [rate limiter services](rate_limiter_services.md) (1 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing.py`

## Audit Trail

- EXTRACTED: 46 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*