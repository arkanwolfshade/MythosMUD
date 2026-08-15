# asyncio

> 32 nodes

## Key Concepts

- **asyncio** (25 connections)
- **game_tick_loop()** (16 connections) — `server/app/game_tick_processing.py`
- **FastAPI** (16 connections)
- **process_status_effects()** (12 connections) — `server/app/game_tick_processing.py`
- **broadcast_tick_event()** (11 connections) — `server/app/game_tick_processing.py`
- **process_dp_decay_and_death()** (9 connections) — `server/app/game_tick_processing.py`
- **_process_all_status_effects()** (8 connections) — `server/app/game_tick_processing.py`
- **process_player_effects_expiration()** (8 connections) — `server/app/game_tick_processing.py`
- **_process_player_status_effects()** (7 connections) — `server/app/game_tick_processing.py`
- **_validate_and_get_player()** (7 connections) — `server/app/game_tick_processing.py`
- **process_casting_progress()** (6 connections) — `server/app/game_tick_processing.py`
- **test_broadcast_tick_event()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_game_tick_loop_cancelled_on_sleep()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_all_status_effects_empty()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_casting_progress_calls_magic_service()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_dp_decay_and_death_no_service()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_dp_decay_and_death_with_session()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_player_effects_expiration_login_warded()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_status_effects_no_online_players()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_status_effects_with_online_player()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_validate_and_get_player_invalid_id()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_validate_and_get_player_success()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **UUID** (2 connections)
- **Validate container and retrieve player by ID. Args: container: Application…** (1 connections) — `server/app/game_tick_processing.py`
- **Process all status effects for a player. Args: app: FastAPI application…** (1 connections) — `server/app/game_tick_processing.py`
- *... and 7 more nodes in this community*

## Relationships

- [test_game_tick_processing.py](test_game_tick_processing.py.md) (25 shared connections)
- [test_game_tick_processing_async.py](test_game_tick_processing_async.py.md) (12 shared connections)
- [get_logger](get_logger.md) (11 shared connections)
- [_process_mortally_wounded_player](_process_mortally_wounded_player.md) (7 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (3 shared connections)
- [process_npc_maintenance](process_npc_maintenance.md) (3 shared connections)
- [_validate_app_state_for_status_effects](_validate_app_state_for_status_effects.md) (3 shared connections)
- [lifespan.py](lifespan.py.md) (2 shared connections)
- [_update_player_status_effects](_update_player_status_effects.md) (2 shared connections)
- [MythosChronicle](MythosChronicle.md) (1 shared connections)
- [send_game_event](send_game_event.md) (1 shared connections)
- [build_event](build_event.md) (1 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing.py`

## Audit Trail

- EXTRACTED: 121 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*