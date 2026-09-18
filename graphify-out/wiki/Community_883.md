# Community 883

> 17 nodes

## Key Concepts

- **game_tick_processing.py** (49 connections) — `server/app/game_tick_processing.py`
- **game_tick_loop()** (17 connections) — `server/app/game_tick_processing.py`
- **process_dp_decay_and_death()** (10 connections) — `server/app/game_tick_death.py`
- **process_combat_tick()** (10 connections) — `server/app/game_tick_processing.py`
- **process_casting_progress()** (7 connections) — `server/app/game_tick_processing.py`
- **process_npc_maintenance()** (7 connections) — `server/app/game_tick_processing.py`
- **FastAPI** (7 connections)
- **test_process_dp_decay_and_death_with_session()** (4 connections) — `server/tests/unit/app/test_game_tick_death.py`
- **_tick_broadcast_payload()** (3 connections) — `server/app/game_tick_processing.py`
- **FastAPI** (2 connections)
- **Process DP decay for mortally wounded players and handle deaths.** (1 connections) — `server/app/game_tick_death.py`
- **Game tick processing functions. This module handles all game tick processing…** (1 connections) — `server/app/game_tick_processing.py`
- **Process casting progress for all active spell castings.** (1 connections) — `server/app/game_tick_processing.py`
- **Process NPC lifecycle maintenance (every 60 ticks = 1 minute).** (1 connections) — `server/app/game_tick_processing.py`
- **Build game_tick event payload (Mythos clock + calendar).** (1 connections) — `server/app/game_tick_processing.py`
- **Main game tick loop. This function runs continuously and handles periodic game…** (1 connections) — `server/app/game_tick_processing.py`
- **Process combat auto-progression.** (1 connections) — `server/app/game_tick_processing.py`

## Relationships

- [Community 370](Community_370.md) (15 shared connections)
- [Community 542](Community_542.md) (13 shared connections)
- [Community 385](Community_385.md) (12 shared connections)
- [Community 831](Community_831.md) (8 shared connections)
- [Community 386](Community_386.md) (7 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (4 shared connections)
- [DI Containers & API Bootstrap](DI_Containers_&_API_Bootstrap.md) (3 shared connections)
- [Character Creation & Auth Dependencies](Character_Creation_&_Auth_Dependencies.md) (3 shared connections)
- [Community 161](Community_161.md) (1 shared connections)
- [Community 312](Community_312.md) (1 shared connections)
- [Community 38](Community_38.md) (1 shared connections)
- [Community 499](Community_499.md) (1 shared connections)

## Source Files

- `server/app/game_tick_death.py`
- `server/app/game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_death.py`

## Audit Trail

- EXTRACTED: 95 (96%)
- INFERRED: 4 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*