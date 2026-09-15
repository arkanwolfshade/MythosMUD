# test_game_tick_death.py

> 38 nodes

## Key Concepts

- **test_game_tick_death.py** (31 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **get_mythos_chronicle()** (26 connections) — `server/time/time_service.py`
- **game_tick_corpses.py** (21 connections) — `server/app/game_tick_corpses.py`
- **asyncio** (17 connections)
- **cleanup_decayed_corpses()** (12 connections) — `server/app/game_tick_corpses.py`
- **_process_single_player_room_flux()** (9 connections) — `server/app/game_tick_death.py`
- **_cleanup_single_decayed_corpse()** (8 connections) — `server/app/game_tick_corpses.py`
- **_create_corpse_lifecycle_service()** (8 connections) — `server/app/game_tick_corpses.py`
- **_log_cleanup_results()** (7 connections) — `server/app/game_tick_corpses.py`
- **_CorpseLike** (3 connections) — `server/app/game_tick_corpses.py`
- **test_broadcast_tick_event()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_broadcast_tick_event_skips_when_no_players()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_cleanup_decayed_corpses_on_interval()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_game_tick_loop_cancelled_on_sleep()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_process_dead_players_moves_to_limbo()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_process_dp_decay_and_death_with_session()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_process_mortally_wounded_death_threshold()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_process_mortally_wounded_skips_active_combat()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_process_passive_corruption_flux_no_service_is_noop()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_process_passive_corruption_flux_ticks_online_players()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_process_passive_lucidity_flux()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_process_single_player_room_flux_no_change()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_process_single_player_room_flux_reports_nonzero_delta()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_process_single_player_room_flux_swallows_bad_player_id()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_tick_online_players_counts_successes()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- *... and 13 more nodes in this community*

## Relationships

- [game_tick_processing.py](game_tick_processing.py.md) (34 shared connections)
- [ContainerComponent](ContainerComponent.md) (4 shared connections)
- [HolidayService](HolidayService.md) (4 shared connections)
- [MythosTickScheduler](MythosTickScheduler.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [container_events.py](container_events.py.md) (2 shared connections)
- [api/game.py](api-game.py.md) (2 shared connections)
- [lifespan.py](lifespan.py.md) (2 shared connections)
- [lifespan_protocols.py](lifespan_protocols.py.md) (2 shared connections)
- [test_admin_commands.py](test_admin_commands.py.md) (2 shared connections)
- [handle_time_command](handle_time_command.md) (2 shared connections)
- [test_time_bundle.py](test_time_bundle.py.md) (2 shared connections)

## Source Files

- `server/app/game_tick_corpses.py`
- `server/app/game_tick_death.py`
- `server/tests/unit/app/test_game_tick_death.py`
- `server/tests/unit/app/test_game_tick_processing.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 128 (93%)
- INFERRED: 10 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*