# Community 380

> 46 nodes

## Key Concepts

- **test_game_tick_processing.py** (43 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **asyncio** (21 connections)
- **process_combat_cleanup()** (10 connections) — `server/app/game_tick_processing.py`
- **_cleanup_single_decayed_corpse()** (8 connections) — `server/app/game_tick_corpses.py`
- **get_tick_interval()** (6 connections) — `server/app/game_tick_processing.py`
- **test_process_player_effects_expiration_survives_database_error()** (4 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_single_player_mp_regeneration()** (4 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **_CorpseLike** (3 connections) — `server/app/game_tick_corpses.py`
- **test_cleanup_decayed_corpses_no_persistence()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_cleanup_single_decayed_corpse_success()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_get_tick_interval()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_all_status_effects_empty()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_casting_progress_calls_magic_service()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_combat_cleanup_no_service()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_combat_cleanup_runs_on_interval()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_combat_cleanup_skips_off_interval()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_combat_tick_calls_service()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_damage_over_time_zero_remaining()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_dp_decay_and_death_no_service()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_heal_over_time_effect()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_npc_maintenance_runs_on_interval()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_player_effects_expiration_login_warded()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_single_effect_heal_expires()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_status_effects_no_online_players()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_process_status_effects_with_online_player()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- *... and 21 more nodes in this community*

## Relationships

- [Community 550](Community_550.md) (20 shared connections)
- [Community 893](Community_893.md) (9 shared connections)
- [Community 412](Community_412.md) (5 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (4 shared connections)
- [Community 490](Community_490.md) (4 shared connections)
- [Community 425](Community_425.md) (2 shared connections)
- [Community 1107](Community_1107.md) (2 shared connections)
- [Community 194](Community_194.md) (1 shared connections)
- [Community 176](Community_176.md) (1 shared connections)

## Source Files

- `server/app/game_tick_corpses.py`
- `server/app/game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing.py`

## Audit Trail

- EXTRACTED: 99 (82%)
- INFERRED: 21 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*