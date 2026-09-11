# game_tick_processing.py

> 35 nodes

## Key Concepts

- **game_tick_processing.py** (55 connections) — `server/app/game_tick_processing.py`
- **game_tick_loop()** (17 connections) — `server/app/game_tick_processing.py`
- **get_current_tick()** (16 connections) — `server/app/game_tick_counter.py`
- **broadcast_tick_event()** (13 connections) — `server/app/game_tick_processing.py`
- **_app_container()** (13 connections) — `server/app/game_tick_protocols.py`
- **broadcast_game_event()** (11 connections) — `server/realtime/connection_manager_api.py`
- **process_dp_decay_and_death()** (10 connections) — `server/app/game_tick_death.py`
- **process_combat_tick()** (10 connections) — `server/app/game_tick_processing.py`
- **game_tick_counter.py** (9 connections) — `server/app/game_tick_counter.py`
- **get_tick_interval()** (8 connections) — `server/app/game_tick_processing.py`
- **process_npc_maintenance()** (8 connections) — `server/app/game_tick_processing.py`
- **process_casting_progress()** (7 connections) — `server/app/game_tick_processing.py`
- **reset_current_tick()** (6 connections) — `server/app/game_tick_counter.py`
- **FastAPI** (6 connections)
- **set_current_tick()** (5 connections) — `server/app/game_tick_counter.py`
- **_tick_broadcast_payload()** (4 connections) — `server/app/game_tick_processing.py`
- **test_get_current_tick()** (4 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_reset_current_tick()** (4 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **Shared game tick counter. Kept in a leaf module so combat services can read the…** (1 connections) — `server/app/game_tick_counter.py`
- **Get the current game tick.** (1 connections) — `server/app/game_tick_counter.py`
- **Set the current game tick (game tick loop).** (1 connections) — `server/app/game_tick_counter.py`
- **Reset the current tick for testing.** (1 connections) — `server/app/game_tick_counter.py`
- **Process DP decay for mortally wounded players and handle deaths.** (1 connections) — `server/app/game_tick_death.py`
- **Game tick processing functions. This module handles all game tick processing…** (1 connections) — `server/app/game_tick_processing.py`
- **Process NPC lifecycle maintenance (every 60 ticks = 1 minute).** (1 connections) — `server/app/game_tick_processing.py`
- *... and 10 more nodes in this community*

## Relationships

- [game_tick_status_effects.py](game_tick_status_effects.py.md) (15 shared connections)
- [test_game_tick_processing.py](test_game_tick_processing.py.md) (12 shared connections)
- [game_tick_death.py](game_tick_death.py.md) (11 shared connections)
- [test_game_tick_death.py](test_game_tick_death.py.md) (9 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (6 shared connections)
- [NPCCombatDataProvider](NPCCombatDataProvider.md) (4 shared connections)
- [PlayerService](PlayerService.md) (4 shared connections)
- [build_event](build_event.md) (4 shared connections)
- [test_game_tick_processing_async.py](test_game_tick_processing_async.py.md) (4 shared connections)
- [MythosTickScheduler](MythosTickScheduler.md) (4 shared connections)
- [resolve_lazy_attr](resolve_lazy_attr.md) (4 shared connections)

## Source Files

- `server/app/game_tick_counter.py`
- `server/app/game_tick_death.py`
- `server/app/game_tick_processing.py`
- `server/app/game_tick_protocols.py`
- `server/realtime/connection_manager_api.py`
- `server/tests/unit/app/test_game_tick_processing.py`

## Audit Trail

- EXTRACTED: 154 (94%)
- INFERRED: 10 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*