# Community 893

> 17 nodes

## Key Concepts

- **game_tick_loop()** (15 connections) — `server/app/game_tick_processing.py`
- **broadcast_game_event()** (11 connections) — `server/realtime/connection_manager_api.py`
- **broadcast_tick_event()** (10 connections) — `server/app/game_tick_processing.py`
- **_app_container()** (10 connections) — `server/app/game_tick_protocols.py`
- **process_npc_maintenance()** (8 connections) — `server/app/game_tick_processing.py`
- **process_casting_progress()** (7 connections) — `server/app/game_tick_processing.py`
- **FastAPI** (7 connections)
- **_tick_broadcast_payload()** (4 connections) — `server/app/game_tick_processing.py`
- **.should_run_maintenance()** (4 connections) — `server/config/npc_config.py`
- **Process casting progress for all active spell castings.** (1 connections) — `server/app/game_tick_processing.py`
- **Process NPC lifecycle maintenance (every 60 ticks = 1 minute).** (1 connections) — `server/app/game_tick_processing.py`
- **Build game_tick event payload (Mythos clock + calendar).** (1 connections) — `server/app/game_tick_processing.py`
- **Broadcast game tick event to all connected players.** (1 connections) — `server/app/game_tick_processing.py`
- **Main game tick loop. This function runs continuously and handles periodic game…** (1 connections) — `server/app/game_tick_processing.py`
- **Return the DI container from app.state, or None if missing.** (1 connections) — `server/app/game_tick_protocols.py`
- **Check if NPC maintenance should run on this tick. Args: tick_count: Current…** (1 connections) — `server/config/npc_config.py`
- **Broadcast a game event to all connected players. Args: event_type: The type of…** (1 connections) — `server/realtime/connection_manager_api.py`

## Relationships

- [Community 550](Community_550.md) (10 shared connections)
- [Community 380](Community_380.md) (9 shared connections)
- [Community 233](Community_233.md) (5 shared connections)
- [Community 425](Community_425.md) (3 shared connections)
- [Community 491](Community_491.md) (3 shared connections)
- [Community 46](Community_46.md) (2 shared connections)
- [Community 41](Community_41.md) (2 shared connections)
- [Community 247](Community_247.md) (2 shared connections)
- [Community 1107](Community_1107.md) (1 shared connections)
- [Community 490](Community_490.md) (1 shared connections)
- [Community 412](Community_412.md) (1 shared connections)
- [Community 95](Community_95.md) (1 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/app/game_tick_protocols.py`
- `server/config/npc_config.py`
- `server/realtime/connection_manager_api.py`

## Audit Trail

- EXTRACTED: 62 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*