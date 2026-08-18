# test_game_tick_death.py

> 35 nodes

## Key Concepts

- **test_game_tick_death.py** (27 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **game_tick_corpses.py** (21 connections) — `server/app/game_tick_corpses.py`
- **broadcast_tick_event()** (13 connections) — `server/app/game_tick_processing.py`
- **cleanup_decayed_corpses()** (12 connections) — `server/app/game_tick_corpses.py`
- **broadcast_game_event()** (11 connections) — `server/realtime/connection_manager_api.py`
- **asyncio** (11 connections)
- **_cleanup_single_decayed_corpse()** (8 connections) — `server/app/game_tick_corpses.py`
- **_create_corpse_lifecycle_service()** (8 connections) — `server/app/game_tick_corpses.py`
- **_log_cleanup_results()** (7 connections) — `server/app/game_tick_corpses.py`
- **_tick_broadcast_payload()** (4 connections) — `server/app/game_tick_processing.py`
- **_CorpseLike** (3 connections) — `server/app/game_tick_corpses.py`
- **test_broadcast_tick_event()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_broadcast_tick_event_skips_when_no_players()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_cleanup_decayed_corpses_on_interval()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_game_tick_loop_cancelled_on_sleep()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_process_dead_players_moves_to_limbo()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_process_dp_decay_and_death_with_session()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_process_mortally_wounded_death_threshold()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_process_mortally_wounded_skips_active_combat()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_process_passive_lucidity_flux()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_tick_online_players_counts_successes()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **FastAPI** (3 connections)
- **test_create_corpse_lifecycle_service()** (2 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_log_cleanup_results_warning_path()** (2 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_log_cleanup_results()** (2 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- *... and 10 more nodes in this community*

## Relationships

- [game_tick_processing.py](game_tick_processing.py.md) (15 shared connections)
- [test_game_tick_processing.py](test_game_tick_processing.py.md) (12 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [CorpseLifecycleService](CorpseLifecycleService.md) (4 shared connections)
- [MythosChronicle](MythosChronicle.md) (4 shared connections)
- [resolve_lazy_attr](resolve_lazy_attr.md) (3 shared connections)
- [test_container_websocket_events.py](test_container_websocket_events.py.md) (2 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (2 shared connections)
- [build_event](build_event.md) (2 shared connections)
- [CombatParticipant](CombatParticipant.md) (2 shared connections)
- [test_connection_manager_api.py](test_connection_manager_api.py.md) (1 shared connections)
- [MythosTimeEventConsumer](MythosTimeEventConsumer.md) (1 shared connections)

## Source Files

- `server/app/game_tick_corpses.py`
- `server/app/game_tick_processing.py`
- `server/realtime/connection_manager_api.py`
- `server/tests/unit/app/test_game_tick_death.py`
- `server/tests/unit/app/test_game_tick_processing.py`

## Audit Trail

- EXTRACTED: 110 (95%)
- INFERRED: 6 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*