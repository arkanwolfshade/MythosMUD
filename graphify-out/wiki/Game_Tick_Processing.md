# Game Tick Processing

> 27 nodes

## Key Concepts

- **game_tick_processing.py** (56 connections) — `server/app/game_tick_processing.py`
- **game_tick_loop()** (17 connections) — `server/app/game_tick_processing.py`
- **broadcast_tick_event()** (13 connections) — `server/app/game_tick_processing.py`
- **_app_container()** (13 connections) — `server/app/game_tick_protocols.py`
- **process_dp_decay_and_death()** (10 connections) — `server/app/game_tick_death.py`
- **process_combat_tick()** (10 connections) — `server/app/game_tick_processing.py`
- **process_npc_maintenance()** (8 connections) — `server/app/game_tick_processing.py`
- **process_casting_progress()** (7 connections) — `server/app/game_tick_processing.py`
- **reset_current_tick()** (6 connections) — `server/app/game_tick_counter.py`
- **get_tick_interval()** (6 connections) — `server/app/game_tick_processing.py`
- **FastAPI** (6 connections)
- **set_current_tick()** (5 connections) — `server/app/game_tick_counter.py`
- **_tick_broadcast_payload()** (4 connections) — `server/app/game_tick_processing.py`
- **test_get_current_tick()** (4 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **Set the current game tick (game tick loop).** (1 connections) — `server/app/game_tick_counter.py`
- **Reset the current tick for testing.** (1 connections) — `server/app/game_tick_counter.py`
- **Process DP decay for mortally wounded players and handle deaths.** (1 connections) — `server/app/game_tick_death.py`
- **Game tick processing functions. This module handles all game tick processing…** (1 connections) — `server/app/game_tick_processing.py`
- **Process NPC lifecycle maintenance (every 60 ticks = 1 minute).** (1 connections) — `server/app/game_tick_processing.py`
- **Build game_tick event payload (Mythos clock + calendar).** (1 connections) — `server/app/game_tick_processing.py`
- **Broadcast game tick event to all connected players.** (1 connections) — `server/app/game_tick_processing.py`
- **Main game tick loop. This function runs continuously and handles periodic game…** (1 connections) — `server/app/game_tick_processing.py`
- **Get the server tick interval from configuration. Returns: float: Tick interval…** (1 connections) — `server/app/game_tick_processing.py`
- **Process combat auto-progression.** (1 connections) — `server/app/game_tick_processing.py`
- **Process casting progress for all active spell castings.** (1 connections) — `server/app/game_tick_processing.py`
- *... and 2 more nodes in this community*

## Relationships

- [Test Game Tick Processing](Test_Game_Tick_Processing.md) (14 shared connections)
- [Game Tick Death](Game_Tick_Death.md) (12 shared connections)
- [Test Game Tick Death](Test_Game_Tick_Death.md) (12 shared connections)
- [Game Tick Status Effects](Game_Tick_Status_Effects.md) (8 shared connections)
- [Test Game Tick Processing Async](Test_Game_Tick_Processing_Async.md) (8 shared connections)
- [Test Magic Service](Test_Magic_Service.md) (5 shared connections)
- [Game State Provider](Game_State_Provider.md) (4 shared connections)
- [Connection Manager Api](Connection_Manager_Api.md) (3 shared connections)
- [Test Envelope](Test_Envelope.md) (3 shared connections)
- [Test Lifespan Startup](Test_Lifespan_Startup.md) (3 shared connections)
- [Game Tick Protocols](Game_Tick_Protocols.md) (3 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (3 shared connections)

## Source Files

- `server/app/game_tick_counter.py`
- `server/app/game_tick_death.py`
- `server/app/game_tick_processing.py`
- `server/app/game_tick_protocols.py`
- `server/tests/unit/app/test_game_tick_processing.py`

## Audit Trail

- EXTRACTED: 128 (96%)
- INFERRED: 5 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*