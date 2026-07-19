# Game Tick Processing

> 48 nodes · cohesion 0.08

## Key Concepts

- **game_tick_processing.py** (65 connections) — `server/app/game_tick_processing.py`
- **get_mythos_chronicle()** (24 connections) — `server/time/time_service.py`
- **FastAPI** (16 connections) — `server/app/game_tick_processing.py`
- **game_tick_loop()** (14 connections) — `server/app/game_tick_processing.py`
- **_process_damage_over_time_effect()** (11 connections) — `server/app/game_tick_processing.py`
- **_process_single_effect()** (11 connections) — `server/app/game_tick_processing.py`
- **broadcast_tick_event()** (9 connections) — `server/app/game_tick_processing.py`
- **process_status_effects()** (9 connections) — `server/app/game_tick_processing.py`
- **_process_heal_over_time_effect()** (8 connections) — `server/app/game_tick_processing.py`
- **cleanup_decayed_corpses()** (7 connections) — `server/app/game_tick_processing.py`
- **_create_corpse_lifecycle_service()** (7 connections) — `server/app/game_tick_processing.py`
- **get_tick_interval()** (7 connections) — `server/app/game_tick_processing.py`
- **process_combat_tick()** (7 connections) — `server/app/game_tick_processing.py`
- **process_player_effects_expiration()** (7 connections) — `server/app/game_tick_processing.py`
- **_process_player_status_effects()** (7 connections) — `server/app/game_tick_processing.py`
- **Any** (7 connections) — `server/app/game_tick_processing.py`
- **_cleanup_single_decayed_corpse()** (6 connections) — `server/app/game_tick_processing.py`
- **_process_all_status_effects()** (6 connections) — `server/app/game_tick_processing.py`
- **process_dp_decay_and_death()** (6 connections) — `server/app/game_tick_processing.py`
- **UUID** (6 connections) — `server/app/game_tick_processing.py`
- **_process_single_player_mp_regeneration()** (5 connections) — `server/app/game_tick_processing.py`
- **process_casting_progress()** (4 connections) — `server/app/game_tick_processing.py`
- **process_npc_maintenance()** (4 connections) — `server/app/game_tick_processing.py`
- **_validate_and_get_player()** (4 connections) — `server/app/game_tick_processing.py`
- **_log_cleanup_results()** (3 connections) — `server/app/game_tick_processing.py`
- *... and 23 more nodes in this community*

## Relationships

- [[Status Effect Tick Tests]] (21 shared connections)
- [[App Game Tick]] (17 shared connections)
- [[NPC Admin API]] (12 shared connections)
- [[Look Command Helpers]] (8 shared connections)
- [[Combat Player Broadcasts]] (6 shared connections)
- [[App Lifespan Management]] (4 shared connections)
- [[Lifespan Startup Hooks]] (3 shared connections)
- [[Async Task Registry]] (3 shared connections)
- [[Players API Endpoints]] (2 shared connections)
- [[Config Npc]] (2 shared connections)
- [[Application DI Bundles]] (2 shared connections)
- [[Combat Taunt Tests]] (2 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/time/time_service.py`

## Audit Trail

- EXTRACTED: 285 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
