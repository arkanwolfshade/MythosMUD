# game tick processing

> 37 nodes

## Key Concepts

- **game_tick_processing.py** (68 connections) — `server/app/game_tick_processing.py`
- **FastAPI** (16 connections)
- **game_tick_loop()** (14 connections) — `server/app/game_tick_processing.py`
- **process_status_effects()** (9 connections) — `server/app/game_tick_processing.py`
- **broadcast_tick_event()** (9 connections) — `server/app/game_tick_processing.py`
- **get_tick_interval()** (8 connections) — `server/app/game_tick_processing.py`
- **_process_player_status_effects()** (7 connections) — `server/app/game_tick_processing.py`
- **process_player_effects_expiration()** (7 connections) — `server/app/game_tick_processing.py`
- **process_combat_tick()** (7 connections) — `server/app/game_tick_processing.py`
- **cleanup_decayed_corpses()** (7 connections) — `server/app/game_tick_processing.py`
- **UUID** (6 connections)
- **process_dp_decay_and_death()** (6 connections) — `server/app/game_tick_processing.py`
- **_create_corpse_lifecycle_service()** (6 connections) — `server/app/game_tick_processing.py`
- **_cleanup_single_decayed_corpse()** (6 connections) — `server/app/game_tick_processing.py`
- **process_npc_maintenance()** (5 connections) — `server/app/game_tick_processing.py`
- **_validate_and_get_player()** (4 connections) — `server/app/game_tick_processing.py`
- **process_casting_progress()** (4 connections) — `server/app/game_tick_processing.py`
- **_log_cleanup_results()** (3 connections) — `server/app/game_tick_processing.py`
- **.should_run_maintenance()** (3 connections) — `server/config/npc_config.py`
- **Game tick processing functions.  This module handles all game tick processing lo** (1 connections) — `server/app/game_tick_processing.py`
- **Get the server tick interval from configuration.      Returns:         float: Ti** (1 connections) — `server/app/game_tick_processing.py`
- **Validate container and retrieve player by ID.      Args:         container: Appl** (1 connections) — `server/app/game_tick_processing.py`
- **Process status effects for a single player.      Returns:         True if player** (1 connections) — `server/app/game_tick_processing.py`
- **Expire player_effects for this tick; for LOGIN_WARDED clear in-memory state and** (1 connections) — `server/app/game_tick_processing.py`
- **Process status effects for online players.** (1 connections) — `server/app/game_tick_processing.py`
- *... and 12 more nodes in this community*

## Relationships

- [process all status effects()](process_all_status_effects%28%29.md) (19 shared connections)
- [process dead players()](process_dead_players%28%29.md) (11 shared connections)
- [Reset the current tick for](Reset_the_current_tick_for.md) (8 shared connections)
- [main()](main%28%29.md) (7 shared connections)
- [login grace period](login_grace_period.md) (7 shared connections)
- [initialize nats and combat services()](initialize_nats_and_combat_services%28%29.md) (5 shared connections)
- [Any](Any.md) (4 shared connections)
- [. init ()](_init_%28%29.md) (4 shared connections)
- [Connection Manager](Connection_Manager.md) (3 shared connections)
- [connection manager api](connection_manager_api.md) (3 shared connections)
- [container websocket events](container_websocket_events.md) (3 shared connections)
- [time commands](time_commands.md) (3 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/config/npc_config.py`

## Audit Trail

- EXTRACTED: 212 (100%)
- INFERRED: 1 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*