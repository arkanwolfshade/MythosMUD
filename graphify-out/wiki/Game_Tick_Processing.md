# Game Tick Processing

> 33 nodes · cohesion 0.11

## Key Concepts

- **game_tick_processing.py** (68 connections) — `server/app/game_tick_processing.py`
- **FastAPI** (16 connections)
- **game_tick_loop()** (14 connections) — `server/app/game_tick_processing.py`
- **broadcast_tick_event()** (9 connections) — `server/app/game_tick_processing.py`
- **process_status_effects()** (9 connections) — `server/app/game_tick_processing.py`
- **cleanup_decayed_corpses()** (7 connections) — `server/app/game_tick_processing.py`
- **process_combat_tick()** (7 connections) — `server/app/game_tick_processing.py`
- **process_player_effects_expiration()** (7 connections) — `server/app/game_tick_processing.py`
- **_process_player_status_effects()** (7 connections) — `server/app/game_tick_processing.py`
- **_create_corpse_lifecycle_service()** (6 connections) — `server/app/game_tick_processing.py`
- **_process_all_status_effects()** (6 connections) — `server/app/game_tick_processing.py`
- **process_dp_decay_and_death()** (6 connections) — `server/app/game_tick_processing.py`
- **UUID** (6 connections)
- **process_npc_maintenance()** (5 connections) — `server/app/game_tick_processing.py`
- **process_casting_progress()** (4 connections) — `server/app/game_tick_processing.py`
- **_validate_and_get_player()** (4 connections) — `server/app/game_tick_processing.py`
- **_log_cleanup_results()** (3 connections) — `server/app/game_tick_processing.py`
- **Game tick processing functions.  This module handles all game tick processing lo** (1 connections) — `server/app/game_tick_processing.py`
- **Validate container and retrieve player by ID.      Args:         container: Appl** (1 connections) — `server/app/game_tick_processing.py`
- **Process all status effects for a player.      Args:         app: FastAPI applica** (1 connections) — `server/app/game_tick_processing.py`
- **Process status effects for a single player.      Returns:         True if player** (1 connections) — `server/app/game_tick_processing.py`
- **Expire player_effects for this tick; for LOGIN_WARDED clear in-memory state and** (1 connections) — `server/app/game_tick_processing.py`
- **Process status effects for online players.** (1 connections) — `server/app/game_tick_processing.py`
- **Process combat auto-progression.** (1 connections) — `server/app/game_tick_processing.py`
- **Process casting progress for all active spell castings.** (1 connections) — `server/app/game_tick_processing.py`
- *... and 8 more nodes in this community*

## Relationships

- [Health Service Tests](Health_Service_Tests.md) (14 shared connections)
- [Fresh Session Test Guide](Fresh_Session_Test_Guide.md) (9 shared connections)
- [PostgreSQL Audit Report](PostgreSQL_Audit_Report.md) (8 shared connections)
- [Archive Circuit Breaker](Archive_Circuit_Breaker.md) (7 shared connections)
- [Moderation Command Models](Moderation_Command_Models.md) (7 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (4 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (4 shared connections)
- [Archive Effects System](Archive_Effects_System.md) (3 shared connections)
- [Event Bus Serialization](Event_Bus_Serialization.md) (3 shared connections)
- [NPC Combat Handler Tests](NPC_Combat_Handler_Tests.md) (3 shared connections)
- [Weapon Resolution Helpers](Weapon_Resolution_Helpers.md) (3 shared connections)
- [Memory Leak Metrics](Memory_Leak_Metrics.md) (3 shared connections)

## Source Files

- `server/app/game_tick_processing.py`

## Audit Trail

- EXTRACTED: 200 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*