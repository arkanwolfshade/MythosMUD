# test_game_tick_death.py

> 33 nodes

## Key Concepts

- **test_game_tick_death.py** (28 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **game_tick_corpses.py** (21 connections) — `server/app/game_tick_corpses.py`
- **cleanup_decayed_corpses()** (12 connections) — `server/app/game_tick_corpses.py`
- **asyncio** (12 connections)
- **_tick_online_players()** (9 connections) — `server/app/game_tick_protocols.py`
- **_cleanup_single_decayed_corpse()** (8 connections) — `server/app/game_tick_corpses.py`
- **_create_corpse_lifecycle_service()** (8 connections) — `server/app/game_tick_corpses.py`
- **_log_cleanup_results()** (7 connections) — `server/app/game_tick_corpses.py`
- **test_process_mortally_wounded_publishes_dp_decay_to_nats()** (4 connections) — `server/tests/unit/app/test_game_tick_death.py`
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
- **Protocol** (1 connections)
- *... and 8 more nodes in this community*

## Relationships

- [game_tick_processing.py](game_tick_processing.py.md) (9 shared connections)
- [game_tick_death.py](game_tick_death.py.md) (8 shared connections)
- [test_game_tick_processing.py](test_game_tick_processing.py.md) (7 shared connections)
- [ContainerComponent](ContainerComponent.md) (4 shared connections)
- [game_tick_protocols.py](game_tick_protocols.py.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [test_container_websocket_events.py](test_container_websocket_events.py.md) (2 shared connections)
- [get_username_from_user](get_username_from_user.md) (2 shared connections)
- [game_tick_status_effects.py](game_tick_status_effects.py.md) (2 shared connections)
- [models/combat.py](models-combat.py.md) (2 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)

## Source Files

- `server/app/game_tick_corpses.py`
- `server/app/game_tick_protocols.py`
- `server/tests/unit/app/test_game_tick_death.py`
- `server/tests/unit/app/test_game_tick_processing.py`

## Audit Trail

- EXTRACTED: 98 (94%)
- INFERRED: 6 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*