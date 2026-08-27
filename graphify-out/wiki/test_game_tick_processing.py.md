# test_game_tick_processing.py

> 81 nodes

## Key Concepts

- **test_game_tick_processing.py** (40 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_game_tick_death.py** (28 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **game_tick_loop()** (17 connections) — `server/app/game_tick_processing.py`
- **asyncio** (17 connections)
- **broadcast_tick_event()** (13 connections) — `server/app/game_tick_processing.py`
- **cleanup_decayed_corpses()** (12 connections) — `server/app/game_tick_corpses.py`
- **asyncio** (12 connections)
- **broadcast_game_event()** (11 connections) — `server/realtime/connection_manager_api.py`
- **process_combat_tick()** (10 connections) — `server/app/game_tick_processing.py`
- **_cleanup_single_decayed_corpse()** (8 connections) — `server/app/game_tick_corpses.py`
- **_create_corpse_lifecycle_service()** (8 connections) — `server/app/game_tick_corpses.py`
- **get_tick_interval()** (8 connections) — `server/app/game_tick_processing.py`
- **process_npc_maintenance()** (8 connections) — `server/app/game_tick_processing.py`
- **_log_cleanup_results()** (7 connections) — `server/app/game_tick_corpses.py`
- **process_casting_progress()** (7 connections) — `server/app/game_tick_processing.py`
- **FastAPI** (6 connections)
- **_tick_broadcast_payload()** (4 connections) — `server/app/game_tick_processing.py`
- **test_process_mortally_wounded_publishes_dp_decay_to_nats()** (4 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_process_single_player_mp_regeneration()** (4 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **_CorpseLike** (3 connections) — `server/app/game_tick_corpses.py`
- **test_broadcast_tick_event()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_broadcast_tick_event_skips_when_no_players()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_cleanup_decayed_corpses_on_interval()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_game_tick_loop_cancelled_on_sleep()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **test_process_dead_players_moves_to_limbo()** (3 connections) — `server/tests/unit/app/test_game_tick_death.py`
- *... and 56 more nodes in this community*

## Relationships

- [game_tick_processing.py](game_tick_processing.py.md) (48 shared connections)
- [AliasStorage](AliasStorage.md) (10 shared connections)
- [resolve_lazy_attr](resolve_lazy_attr.md) (4 shared connections)
- [get_current_tick](get_current_tick.md) (3 shared connections)
- [test_game_tick_processing_async.py](test_game_tick_processing_async.py.md) (3 shared connections)
- [ContainerComponent](ContainerComponent.md) (2 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (2 shared connections)
- [build_event](build_event.md) (2 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (2 shared connections)
- [players.py](players.py.md) (2 shared connections)
- [time_event_consumer.py](time_event_consumer.py.md) (2 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)

## Source Files

- `server/app/game_tick_corpses.py`
- `server/app/game_tick_processing.py`
- `server/realtime/connection_manager_api.py`
- `server/tests/unit/app/test_game_tick_death.py`
- `server/tests/unit/app/test_game_tick_processing.py`

## Audit Trail

- EXTRACTED: 197 (88%)
- INFERRED: 28 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*