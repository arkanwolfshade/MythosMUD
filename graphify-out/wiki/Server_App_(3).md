# Server App (3)

> 83 nodes

## Key Concepts

- **game_tick_processing.py** (68 connections) — `server/app/game_tick_processing.py`
- **test_game_tick_processing_async.py** (26 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **FastAPI** (16 connections)
- **game_tick_loop()** (14 connections) — `server/app/game_tick_processing.py`
- **_process_damage_over_time_effect()** (11 connections) — `server/app/game_tick_processing.py`
- **_process_single_effect()** (11 connections) — `server/app/game_tick_processing.py`
- **process_status_effects()** (9 connections) — `server/app/game_tick_processing.py`
- **broadcast_tick_event()** (9 connections) — `server/app/game_tick_processing.py`
- **_process_heal_over_time_effect()** (8 connections) — `server/app/game_tick_processing.py`
- **Any** (7 connections)
- **_update_player_status_effects()** (7 connections) — `server/app/game_tick_processing.py`
- **_process_player_status_effects()** (7 connections) — `server/app/game_tick_processing.py`
- **process_player_effects_expiration()** (7 connections) — `server/app/game_tick_processing.py`
- **process_combat_tick()** (7 connections) — `server/app/game_tick_processing.py`
- **cleanup_decayed_corpses()** (7 connections) — `server/app/game_tick_processing.py`
- **UUID** (6 connections)
- **_process_all_status_effects()** (6 connections) — `server/app/game_tick_processing.py`
- **process_dp_decay_and_death()** (6 connections) — `server/app/game_tick_processing.py`
- **_create_corpse_lifecycle_service()** (6 connections) — `server/app/game_tick_processing.py`
- **_cleanup_single_decayed_corpse()** (6 connections) — `server/app/game_tick_processing.py`
- **_process_single_player_mp_regeneration()** (5 connections) — `server/app/game_tick_processing.py`
- **process_npc_maintenance()** (5 connections) — `server/app/game_tick_processing.py`
- **_validate_and_get_player()** (4 connections) — `server/app/game_tick_processing.py`
- **process_casting_progress()** (4 connections) — `server/app/game_tick_processing.py`
- **_log_cleanup_results()** (3 connections) — `server/app/game_tick_processing.py`
- *... and 58 more nodes in this community*

## Relationships

- [Server App (7)](Server_App_%287%29.md) (10 shared connections)
- [Server Realtime (8)](Server_Realtime_%288%29.md) (8 shared connections)
- [Server App (4)](Server_App_%284%29.md) (6 shared connections)
- [Server Commands](Server_Commands.md) (6 shared connections)
- [Server Api (3)](Server_Api_%283%29.md) (4 shared connections)
- [Server Services](Server_Services.md) (4 shared connections)
- [Server Services (46)](Server_Services_%2846%29.md) (4 shared connections)
- [Server Npc (2)](Server_Npc_%282%29.md) (3 shared connections)
- [Server Admin](Server_Admin.md) (3 shared connections)
- [Server Realtime (48)](Server_Realtime_%2848%29.md) (3 shared connections)
- [Server Services (43)](Server_Services_%2843%29.md) (3 shared connections)
- [Server Monitoring](Server_Monitoring.md) (3 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/config/npc_config.py`
- `server/tests/unit/app/test_game_tick_processing_async.py`

## Audit Trail

- EXTRACTED: 361 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*