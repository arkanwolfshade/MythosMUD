# Community 542

> 31 nodes

## Key Concepts

- **test_game_tick_death.py** (29 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **asyncio** (18 connections)
- **_process_mortally_wounded_player()** (12 connections) — `server/app/game_tick_death.py`
- **_process_passive_corruption_flux()** (11 connections) — `server/app/game_tick_death.py`
- **broadcast_tick_event()** (10 connections) — `server/app/game_tick_processing.py`
- **_tick_online_players()** (10 connections) — `server/app/game_tick_protocols.py`
- **_process_single_player_room_flux()** (8 connections) — `server/app/game_tick_death.py`
- **test_game_tick_loop_survives_unanticipated_exception()** (5 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_process_mortally_wounded_publishes_dp_decay_to_nats()** (5 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_broadcast_tick_event()** (4 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_broadcast_tick_event_skips_when_no_players()** (4 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_game_tick_loop_cancelled_on_sleep()** (4 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_process_mortally_wounded_death_threshold()** (4 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_tick_online_players_counts_successes()** (4 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_cleanup_decayed_corpses_on_interval()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_process_mortally_wounded_skips_active_combat()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_process_passive_corruption_flux_no_service_is_noop()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_process_passive_corruption_flux_ticks_online_players()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_process_single_player_room_flux_no_change()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_process_single_player_room_flux_reports_nonzero_delta()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_process_single_player_room_flux_swallows_bad_player_id()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_create_corpse_lifecycle_service()** (2 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_log_cleanup_results_warning_path()** (1 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **Process a single mortally wounded player's DP decay and death check. CRITICAL:…** (1 connections) — `server/app/game_tick_death.py`
- **Process passive room corruption flux for a single online player. Args:…** (1 connections) — `server/app/game_tick_death.py`
- *... and 6 more nodes in this community*

## Relationships

- [Community 370](Community_370.md) (22 shared connections)
- [Community 883](Community_883.md) (13 shared connections)
- [Community 38](Community_38.md) (9 shared connections)
- [Community 831](Community_831.md) (2 shared connections)
- [Community 275](Community_275.md) (2 shared connections)
- [Player Creation Service](Player_Creation_Service.md) (1 shared connections)
- [Community 499](Community_499.md) (1 shared connections)
- [Community 884](Community_884.md) (1 shared connections)
- [Community 268](Community_268.md) (1 shared connections)

## Source Files

- `server/app/game_tick_death.py`
- `server/app/game_tick_processing.py`
- `server/app/game_tick_protocols.py`
- `server/tests/unit/app/test_game_tick_death.py`

## Audit Trail

- EXTRACTED: 89 (84%)
- INFERRED: 17 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*