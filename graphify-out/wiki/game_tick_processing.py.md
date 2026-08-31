# game_tick_processing.py

> 27 nodes

## Key Concepts

- **game_tick_processing.py** (56 connections) — `server/app/game_tick_processing.py`
- **game_tick_loop()** (17 connections) — `server/app/game_tick_processing.py`
- **broadcast_tick_event()** (13 connections) — `server/app/game_tick_processing.py`
- **_app_container()** (13 connections) — `server/app/game_tick_protocols.py`
- **broadcast_game_event()** (11 connections) — `server/realtime/connection_manager_api.py`
- **process_combat_tick()** (10 connections) — `server/app/game_tick_processing.py`
- **get_tick_interval()** (8 connections) — `server/app/game_tick_processing.py`
- **process_npc_maintenance()** (8 connections) — `server/app/game_tick_processing.py`
- **process_casting_progress()** (7 connections) — `server/app/game_tick_processing.py`
- **reset_current_tick()** (6 connections) — `server/app/game_tick_counter.py`
- **FastAPI** (6 connections)
- **set_current_tick()** (5 connections) — `server/app/game_tick_counter.py`
- **_tick_broadcast_payload()** (4 connections) — `server/app/game_tick_processing.py`
- **.should_run_maintenance()** (3 connections) — `server/config/npc_config.py`
- **Set the current game tick (game tick loop).** (1 connections) — `server/app/game_tick_counter.py`
- **Reset the current tick for testing.** (1 connections) — `server/app/game_tick_counter.py`
- **Game tick processing functions. This module handles all game tick processing…** (1 connections) — `server/app/game_tick_processing.py`
- **Process NPC lifecycle maintenance (every 60 ticks = 1 minute).** (1 connections) — `server/app/game_tick_processing.py`
- **Build game_tick event payload (Mythos clock + calendar).** (1 connections) — `server/app/game_tick_processing.py`
- **Broadcast game tick event to all connected players.** (1 connections) — `server/app/game_tick_processing.py`
- **Main game tick loop. This function runs continuously and handles periodic game…** (1 connections) — `server/app/game_tick_processing.py`
- **Get the server tick interval from configuration. Returns: float: Tick interval…** (1 connections) — `server/app/game_tick_processing.py`
- **Process combat auto-progression.** (1 connections) — `server/app/game_tick_processing.py`
- **Process casting progress for all active spell castings.** (1 connections) — `server/app/game_tick_processing.py`
- **Return the DI container from app.state, or None if missing.** (1 connections) — `server/app/game_tick_protocols.py`
- *... and 2 more nodes in this community*

## Relationships

- [game_tick_status_effects.py](game_tick_status_effects.py.md) (19 shared connections)
- [test_game_tick_processing.py](test_game_tick_processing.py.md) (11 shared connections)
- [game_tick_death.py](game_tick_death.py.md) (11 shared connections)
- [test_game_tick_death.py](test_game_tick_death.py.md) (9 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (5 shared connections)
- [CombatService](CombatService.md) (4 shared connections)
- [build_event](build_event.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [lifespan.py](lifespan.py.md) (3 shared connections)
- [PlayerService](PlayerService.md) (3 shared connections)
- [game_tick_protocols.py](game_tick_protocols.py.md) (3 shared connections)
- [test_lifecycle_periodic.py](test_lifecycle_periodic.py.md) (3 shared connections)

## Source Files

- `server/app/game_tick_counter.py`
- `server/app/game_tick_processing.py`
- `server/app/game_tick_protocols.py`
- `server/config/npc_config.py`
- `server/realtime/connection_manager_api.py`

## Audit Trail

- EXTRACTED: 132 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*