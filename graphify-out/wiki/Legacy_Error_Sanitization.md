# Legacy Error Sanitization

> 39 nodes

## Key Concepts

- **game_tick_processing.py** (77 connections) — `server/app/game_tick_processing.py`
- **FastAPI** (16 connections)
- **game_tick_loop()** (14 connections) — `server/app/game_tick_processing.py`
- **_validate_app_state_for_status_effects()** (12 connections) — `server/app/game_tick_processing.py`
- **_process_single_effect()** (11 connections) — `server/app/game_tick_processing.py`
- **process_status_effects()** (9 connections) — `server/app/game_tick_processing.py`
- **broadcast_tick_event()** (9 connections) — `server/app/game_tick_processing.py`
- **Any** (8 connections)
- **_process_player_status_effects()** (7 connections) — `server/app/game_tick_processing.py`
- **process_player_effects_expiration()** (7 connections) — `server/app/game_tick_processing.py`
- **process_combat_tick()** (7 connections) — `server/app/game_tick_processing.py`
- **cleanup_decayed_corpses()** (7 connections) — `server/app/game_tick_processing.py`
- **_process_all_status_effects()** (6 connections) — `server/app/game_tick_processing.py`
- **process_dp_decay_and_death()** (6 connections) — `server/app/game_tick_processing.py`
- **_create_corpse_lifecycle_service()** (6 connections) — `server/app/game_tick_processing.py`
- **_cleanup_single_decayed_corpse()** (6 connections) — `server/app/game_tick_processing.py`
- **process_npc_maintenance()** (5 connections) — `server/app/game_tick_processing.py`
- **_validate_and_get_player()** (4 connections) — `server/app/game_tick_processing.py`
- **process_casting_progress()** (4 connections) — `server/app/game_tick_processing.py`
- **_log_cleanup_results()** (3 connections) — `server/app/game_tick_processing.py`
- **Game tick processing functions.  This module handles all game tick processing lo** (1 connections) — `server/app/game_tick_processing.py`
- **Validate app state has required components for status effect processing.      Re** (1 connections) — `server/app/game_tick_processing.py`
- **Process a single status effect.      Returns:         Tuple of (updated_effect_d** (1 connections) — `server/app/game_tick_processing.py`
- **Validate container and retrieve player by ID.      Args:         container: Appl** (1 connections) — `server/app/game_tick_processing.py`
- **Process all status effects for a player.      Args:         app: FastAPI applica** (1 connections) — `server/app/game_tick_processing.py`
- *... and 14 more nodes in this community*

## Relationships

- [Command Alias Handling](Command_Alias_Handling.md) (21 shared connections)
- [Multiplayer Browser Helpers](Multiplayer_Browser_Helpers.md) (16 shared connections)
- [Combat DP Persistence Tests](Combat_DP_Persistence_Tests.md) (11 shared connections)
- [Player Respawn Events](Player_Respawn_Events.md) (7 shared connections)
- [Skill Service Tests](Skill_Service_Tests.md) (4 shared connections)
- [Test Modernization Plan](Test_Modernization_Plan.md) (4 shared connections)
- [E 2 E Di Migration](E_2_E_Di_Migration.md) (3 shared connections)
- [Spell Registry Costs](Spell_Registry_Costs.md) (3 shared connections)
- [Zone Config Loader](Zone_Config_Loader.md) (3 shared connections)
- [Connection Health Monitor](Connection_Health_Monitor.md) (3 shared connections)
- [Magic Command Handlers](Magic_Command_Handlers.md) (3 shared connections)
- [Docker PostgreSQL Typo Bug](Docker_PostgreSQL_Typo_Bug.md) (3 shared connections)

## Source Files

- `server/app/game_tick_processing.py`

## Audit Trail

- EXTRACTED: 243 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*