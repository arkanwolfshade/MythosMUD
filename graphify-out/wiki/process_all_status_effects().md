# process all status effects()

> 127 nodes

## Key Concepts

- **game_tick_processing.py** (68 connections) — `server/app/game_tick_processing.py`
- **test_game_tick_processing_async.py** (26 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **FastAPI** (16 connections)
- **get_current_tick()** (15 connections) — `server/app/game_tick_processing.py`
- **test_game_tick_processing.py** (15 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **game_tick_loop()** (14 connections) — `server/app/game_tick_processing.py`
- **_validate_app_state_for_status_effects()** (12 connections) — `server/app/game_tick_processing.py`
- **_process_damage_over_time_effect()** (11 connections) — `server/app/game_tick_processing.py`
- **_process_single_effect()** (11 connections) — `server/app/game_tick_processing.py`
- **process_status_effects()** (9 connections) — `server/app/game_tick_processing.py`
- **broadcast_tick_event()** (9 connections) — `server/app/game_tick_processing.py`
- **get_tick_interval()** (8 connections) — `server/app/game_tick_processing.py`
- **_process_heal_over_time_effect()** (8 connections) — `server/app/game_tick_processing.py`
- **_process_session_dp_decay_and_death()** (8 connections) — `server/app/game_tick_processing.py`
- **Any** (7 connections)
- **_update_player_status_effects()** (7 connections) — `server/app/game_tick_processing.py`
- **_process_player_status_effects()** (7 connections) — `server/app/game_tick_processing.py`
- **process_player_effects_expiration()** (7 connections) — `server/app/game_tick_processing.py`
- **process_combat_tick()** (7 connections) — `server/app/game_tick_processing.py`
- **_process_mortally_wounded_player()** (7 connections) — `server/app/game_tick_processing.py`
- **cleanup_decayed_corpses()** (7 connections) — `server/app/game_tick_processing.py`
- **reset_current_tick()** (6 connections) — `server/app/game_tick_processing.py`
- **UUID** (6 connections)
- **_process_all_status_effects()** (6 connections) — `server/app/game_tick_processing.py`
- **AsyncSession** (6 connections)
- *... and 102 more nodes in this community*

## Relationships

- [Any](Any.md) (11 shared connections)
- [login grace period](login_grace_period.md) (9 shared connections)
- [append unique valid occupant()](append_unique_valid_occupant%28%29.md) (5 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (5 shared connections)
- [.shutdown()](shutdown%28%29.md) (5 shared connections)
- [get health status()](get_health_status%28%29.md) (4 shared connections)
- [movement monitor](movement_monitor.md) (3 shared connections)
- [.get population stats()](get_population_stats%28%29.md) (3 shared connections)
- [process dead players()](process_dead_players%28%29.md) (2 shared connections)
- [test player preferences service](test_player_preferences_service.md) (2 shared connections)
- [. init ()](_init_%28%29.md) (2 shared connections)
- [clean command input()](clean_command_input%28%29.md) (2 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing_async.py`

## Audit Trail

- EXTRACTED: 501 (99%)
- INFERRED: 5 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*