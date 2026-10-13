# Community 412

> 42 nodes

## Key Concepts

- **test_game_tick_death.py** (37 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **asyncio** (21 connections)
- **cleanup_decayed_corpses()** (12 connections) — `server/app/game_tick_corpses.py`
- **_process_single_player_room_flux()** (9 connections) — `server/app/game_tick_death.py`
- **_create_corpse_lifecycle_service()** (7 connections) — `server/app/game_tick_corpses.py`
- **_log_cleanup_results()** (7 connections) — `server/app/game_tick_corpses.py`
- **_bleed_out_setup()** (5 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_bleed_out_corpse_failure_does_not_abort_the_death_sequence()** (5 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_mortally_wounded_decay_runs_once_per_second()** (5 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_bleed_out_without_persistence_skips_corpse_but_still_moves_to_limbo()** (4 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_process_mortally_wounded_death_threshold()** (4 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_process_mortally_wounded_publishes_dp_decay_to_nats()** (4 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_cleanup_decayed_corpses_on_interval()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_game_tick_loop_survives_unanticipated_exception()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_process_dead_players_moves_to_limbo()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_process_dp_decay_and_death_with_session()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_process_mortally_wounded_skips_active_combat()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_process_passive_corruption_flux_no_service_is_noop()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_process_passive_corruption_flux_ticks_online_players()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_process_passive_lucidity_flux()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_process_single_player_room_flux_no_change()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_process_single_player_room_flux_reports_nonzero_delta()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_process_single_player_room_flux_swallows_bad_player_id()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **FastAPI** (3 connections)
- **test_broadcast_tick_event()** (2 connections) — `server/tests/unit/app/test_game_tick_death.py`
- *... and 17 more nodes in this community*

## Relationships

- [Community 490](Community_490.md) (15 shared connections)
- [Community 380](Community_380.md) (5 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (5 shared connections)
- [Community 550](Community_550.md) (3 shared connections)
- [Community 176](Community_176.md) (3 shared connections)
- [Combat Attack Execution](Combat_Attack_Execution.md) (2 shared connections)
- [Community 893](Community_893.md) (1 shared connections)
- [Community 441](Community_441.md) (1 shared connections)
- [Community 491](Community_491.md) (1 shared connections)
- [Argon2 Password Hashing](Argon2_Password_Hashing.md) (1 shared connections)

## Source Files

- `server/app/game_tick_corpses.py`
- `server/app/game_tick_death.py`
- `server/tests/unit/app/test_game_tick_death.py`
- `server/tests/unit/app/test_game_tick_processing.py`

## Audit Trail

- EXTRACTED: 108 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*