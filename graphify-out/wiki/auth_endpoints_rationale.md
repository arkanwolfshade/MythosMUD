# auth endpoints rationale

> 37 nodes

## Key Concepts

- **game_tick_processing.py** (68 connections) — `server/app/game_tick_processing.py`
- **FastAPI** (16 connections)
- **game_tick_loop()** (14 connections) — `server/app/game_tick_processing.py`
- **_validate_app_state_for_status_effects()** (12 connections) — `server/app/game_tick_processing.py`
- **process_status_effects()** (9 connections) — `server/app/game_tick_processing.py`
- **broadcast_tick_event()** (9 connections) — `server/app/game_tick_processing.py`
- **_process_player_status_effects()** (7 connections) — `server/app/game_tick_processing.py`
- **process_player_effects_expiration()** (7 connections) — `server/app/game_tick_processing.py`
- **process_combat_tick()** (7 connections) — `server/app/game_tick_processing.py`
- **cleanup_decayed_corpses()** (7 connections) — `server/app/game_tick_processing.py`
- **UUID** (6 connections)
- **_process_all_status_effects()** (6 connections) — `server/app/game_tick_processing.py`
- **process_dp_decay_and_death()** (6 connections) — `server/app/game_tick_processing.py`
- **_create_corpse_lifecycle_service()** (6 connections) — `server/app/game_tick_processing.py`
- **process_npc_maintenance()** (5 connections) — `server/app/game_tick_processing.py`
- **_validate_and_get_player()** (4 connections) — `server/app/game_tick_processing.py`
- **process_casting_progress()** (4 connections) — `server/app/game_tick_processing.py`
- **_log_cleanup_results()** (3 connections) — `server/app/game_tick_processing.py`
- **.should_run_maintenance()** (3 connections) — `server/config/npc_config.py`
- **Game tick processing functions.  This module handles all game tick processing lo** (1 connections) — `server/app/game_tick_processing.py`
- **Validate app state has required components for status effect processing.      Re** (1 connections) — `server/app/game_tick_processing.py`
- **Validate container and retrieve player by ID.      Args:         container: Appl** (1 connections) — `server/app/game_tick_processing.py`
- **Process all status effects for a player.      Args:         app: FastAPI applica** (1 connections) — `server/app/game_tick_processing.py`
- **Process status effects for a single player.      Returns:         True if player** (1 connections) — `server/app/game_tick_processing.py`
- **Expire player_effects for this tick; for LOGIN_WARDED clear in-memory state and** (1 connections) — `server/app/game_tick_processing.py`
- *... and 12 more nodes in this community*

## Relationships

- [tick game processing](tick_game_processing.md) (14 shared connections)
- [app tick game](app_tick_game.md) (11 shared connections)
- [combat services service](combat_services_service.md) (9 shared connections)
- [invite models rationale](invite_models_rationale.md) (7 shared connections)
- [grace period login](grace_period_login.md) (7 shared connections)
- [Item Instances](Item_Instances.md) (6 shared connections)
- [NATS Messaging](NATS_Messaging.md) (4 shared connections)
- [npc lifecycle config](npc_lifecycle_config.md) (3 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (3 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (3 shared connections)
- [connection manager realtime](connection_manager_realtime.md) (3 shared connections)
- [time service rationale](time_service_rationale.md) (3 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/config/npc_config.py`

## Audit Trail

- EXTRACTED: 217 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*