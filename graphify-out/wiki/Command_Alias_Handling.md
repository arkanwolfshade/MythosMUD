# Command Alias Handling

> 34 nodes

## Key Concepts

- **game_tick_processing.py** (77 connections) — `server/app/game_tick_processing.py`
- **FastAPI** (16 connections)
- **game_tick_loop()** (14 connections) — `server/app/game_tick_processing.py`
- **_validate_app_state_for_status_effects()** (12 connections) — `server/app/game_tick_processing.py`
- **process_status_effects()** (9 connections) — `server/app/game_tick_processing.py`
- **broadcast_tick_event()** (9 connections) — `server/app/game_tick_processing.py`
- **_process_player_status_effects()** (7 connections) — `server/app/game_tick_processing.py`
- **process_player_effects_expiration()** (7 connections) — `server/app/game_tick_processing.py`
- **process_combat_tick()** (7 connections) — `server/app/game_tick_processing.py`
- **cleanup_decayed_corpses()** (7 connections) — `server/app/game_tick_processing.py`
- **_process_all_status_effects()** (6 connections) — `server/app/game_tick_processing.py`
- **process_dp_decay_and_death()** (6 connections) — `server/app/game_tick_processing.py`
- **_create_corpse_lifecycle_service()** (6 connections) — `server/app/game_tick_processing.py`
- **process_npc_maintenance()** (5 connections) — `server/app/game_tick_processing.py`
- **_validate_and_get_player()** (4 connections) — `server/app/game_tick_processing.py`
- **process_casting_progress()** (4 connections) — `server/app/game_tick_processing.py`
- **_log_cleanup_results()** (3 connections) — `server/app/game_tick_processing.py`
- **Game tick processing functions.  This module handles all game tick processing lo** (1 connections) — `server/app/game_tick_processing.py`
- **Validate app state has required components for status effect processing.      Re** (1 connections) — `server/app/game_tick_processing.py`
- **Validate container and retrieve player by ID.      Args:         container: Appl** (1 connections) — `server/app/game_tick_processing.py`
- **Process all status effects for a player.      Args:         app: FastAPI applica** (1 connections) — `server/app/game_tick_processing.py`
- **Process status effects for a single player.      Returns:         True if player** (1 connections) — `server/app/game_tick_processing.py`
- **Expire player_effects for this tick; for LOGIN_WARDED clear in-memory state and** (1 connections) — `server/app/game_tick_processing.py`
- **Process status effects for online players.** (1 connections) — `server/app/game_tick_processing.py`
- **Process combat auto-progression.** (1 connections) — `server/app/game_tick_processing.py`
- *... and 9 more nodes in this community*

## Relationships

- [Invite and User Schemas](Invite_and_User_Schemas.md) (18 shared connections)
- [E2E Suite Spec Helpers](E2E_Suite_Spec_Helpers.md) (11 shared connections)
- [Client Event Store](Client_Event_Store.md) (9 shared connections)
- [Investigations Sessions Xx](Investigations_Sessions_Xx.md) (8 shared connections)
- [Connection Room Presence Utils](Connection_Room_Presence_Utils.md) (7 shared connections)
- [Player Respawn Events](Player_Respawn_Events.md) (7 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (5 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (4 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (3 shared connections)
- [E 2 E Di Migration](E_2_E_Di_Migration.md) (3 shared connections)
- [Combat Turn Processor](Combat_Turn_Processor.md) (3 shared connections)
- [Skill Service Tests](Skill_Service_Tests.md) (3 shared connections)

## Source Files

- `server/app/game_tick_processing.py`

## Audit Trail

- EXTRACTED: 216 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*