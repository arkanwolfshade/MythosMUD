# game_tick_processing.py

> 37 nodes

## Key Concepts

- **game_tick_processing.py** (79 connections) — `server/app/game_tick_processing.py`
- **FastAPI** (16 connections)
- **game_tick_loop()** (14 connections) — `server/app/game_tick_processing.py`
- **broadcast_tick_event()** (9 connections) — `server/app/game_tick_processing.py`
- **process_status_effects()** (9 connections) — `server/app/game_tick_processing.py`
- **cleanup_decayed_corpses()** (7 connections) — `server/app/game_tick_processing.py`
- **process_combat_tick()** (7 connections) — `server/app/game_tick_processing.py`
- **_process_player_status_effects()** (7 connections) — `server/app/game_tick_processing.py`
- **_create_corpse_lifecycle_service()** (6 connections) — `server/app/game_tick_processing.py`
- **_process_all_status_effects()** (6 connections) — `server/app/game_tick_processing.py`
- **process_dp_decay_and_death()** (6 connections) — `server/app/game_tick_processing.py`
- **process_player_effects_expiration()** (6 connections) — `server/app/game_tick_processing.py`
- **process_npc_maintenance()** (5 connections) — `server/app/game_tick_processing.py`
- **passive_lucidity_flux_service.py** (5 connections) — `server/services/passive_lucidity_flux_service.py`
- **process_casting_progress()** (4 connections) — `server/app/game_tick_processing.py`
- **_validate_and_get_player()** (4 connections) — `server/app/game_tick_processing.py`
- **_log_cleanup_results()** (3 connections) — `server/app/game_tick_processing.py`
- **.should_run_maintenance()** (3 connections) — `server/config/npc_config.py`
- **UUID** (2 connections)
- **Game tick processing functions. This module handles all game tick processing…** (1 connections) — `server/app/game_tick_processing.py`
- **Validate container and retrieve player by ID. Args: container: Application…** (1 connections) — `server/app/game_tick_processing.py`
- **Process all status effects for a player. Args: app: FastAPI application…** (1 connections) — `server/app/game_tick_processing.py`
- **Process status effects for a single player. Returns: True if player was…** (1 connections) — `server/app/game_tick_processing.py`
- **Expire player_effects for this tick; for LOGIN_WARDED clear in-memory state and…** (1 connections) — `server/app/game_tick_processing.py`
- **Process status effects for online players.** (1 connections) — `server/app/game_tick_processing.py`
- *... and 12 more nodes in this community*

## Relationships

- [test_game_tick_processing_async.py](test_game_tick_processing_async.py.md) (13 shared connections)
- [_process_session_dp_decay_and_death](_process_session_dp_decay_and_death.md) (10 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [get_current_tick](get_current_tick.md) (9 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (7 shared connections)
- [Any](Any.md) (6 shared connections)
- [CombatService](CombatService.md) (4 shared connections)
- [send_game_event](send_game_event.md) (3 shared connections)
- [test_corpse_lifecycle_service.py](test_corpse_lifecycle_service.py.md) (3 shared connections)
- [lifespan.py](lifespan.py.md) (3 shared connections)
- [database.py](database.py.md) (3 shared connections)
- [lifecycle_periodic.py](lifecycle_periodic.py.md) (3 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/config/npc_config.py`
- `server/services/passive_lucidity_flux_service.py`

## Audit Trail

- EXTRACTED: 216 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*