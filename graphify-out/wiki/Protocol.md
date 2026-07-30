# Protocol

> 24 nodes

## Key Concepts

- **game_tick_processing.py** (68 connections) — `server/app/game_tick_processing.py`
- **FastAPI** (16 connections)
- **game_tick_loop()** (14 connections) — `server/app/game_tick_processing.py`
- **broadcast_tick_event()** (9 connections) — `server/app/game_tick_processing.py`
- **process_player_effects_expiration()** (7 connections) — `server/app/game_tick_processing.py`
- **process_combat_tick()** (7 connections) — `server/app/game_tick_processing.py`
- **cleanup_decayed_corpses()** (7 connections) — `server/app/game_tick_processing.py`
- **process_dp_decay_and_death()** (6 connections) — `server/app/game_tick_processing.py`
- **_create_corpse_lifecycle_service()** (6 connections) — `server/app/game_tick_processing.py`
- **process_npc_maintenance()** (5 connections) — `server/app/game_tick_processing.py`
- **process_casting_progress()** (4 connections) — `server/app/game_tick_processing.py`
- **_log_cleanup_results()** (3 connections) — `server/app/game_tick_processing.py`
- **Game tick processing functions.  This module handles all game tick processing lo** (1 connections) — `server/app/game_tick_processing.py`
- **Expire player_effects for this tick; for LOGIN_WARDED clear in-memory state and** (1 connections) — `server/app/game_tick_processing.py`
- **Process combat auto-progression.** (1 connections) — `server/app/game_tick_processing.py`
- **Process casting progress for all active spell castings.** (1 connections) — `server/app/game_tick_processing.py`
- **Process DP decay for mortally wounded players and handle deaths.** (1 connections) — `server/app/game_tick_processing.py`
- **Process NPC lifecycle maintenance (every 60 ticks = 1 minute).** (1 connections) — `server/app/game_tick_processing.py`
- **Create and initialize CorpseLifecycleService.      Args:         app: FastAPI ap** (1 connections) — `server/app/game_tick_processing.py`
- **Log the results of corpse cleanup.      Args:         tick_count: Current game t** (1 connections) — `server/app/game_tick_processing.py`
- **Cleanup decayed corpse containers (every 60 ticks = 1 minute).** (1 connections) — `server/app/game_tick_processing.py`
- **Broadcast game tick event to all connected players.** (1 connections) — `server/app/game_tick_processing.py`
- **Main game tick loop.      This function runs continuously and handles periodic g** (1 connections) — `server/app/game_tick_processing.py`
- **# NOTE: This remains global for now as it's shared state needed by combat system** (1 connections) — `server/app/game_tick_processing.py`

## Relationships

- [test container persistence sql injection](test_container_persistence_sql_injection.md) (11 shared connections)
- [process all status effects()](process_all_status_effects%28%29.md) (11 shared connections)
- [Calculate max magic points (MP)](Calculate_max_magic_points_%28MP%29.md) (8 shared connections)
- [login grace period](login_grace_period.md) (7 shared connections)
- [calendar](calendar.md) (5 shared connections)
- [Any](Any.md) (5 shared connections)
- [AsyncSessionFactory](AsyncSessionFactory.md) (4 shared connections)
- [append unique valid occupant()](append_unique_valid_occupant%28%29.md) (3 shared connections)
- [rename invites columns](rename_invites_columns.md) (3 shared connections)
- [close db()](close_db%28%29.md) (3 shared connections)
- [.shutdown()](shutdown%28%29.md) (3 shared connections)
- [test combat attack handler](test_combat_attack_handler.md) (2 shared connections)

## Source Files

- `server/app/game_tick_processing.py`

## Audit Trail

- EXTRACTED: 164 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*