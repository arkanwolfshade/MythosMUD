# Invite and User Schemas

> 49 nodes

## Key Concepts

- **test_game_tick_processing_async.py** (26 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **_process_damage_over_time_effect()** (11 connections) — `server/app/game_tick_processing.py`
- **_process_single_effect()** (11 connections) — `server/app/game_tick_processing.py`
- **Any** (8 connections)
- **_process_heal_over_time_effect()** (8 connections) — `server/app/game_tick_processing.py`
- **_update_player_status_effects()** (7 connections) — `server/app/game_tick_processing.py`
- **_cleanup_single_decayed_corpse()** (6 connections) — `server/app/game_tick_processing.py`
- **test_process_damage_over_time_effect_no_damage()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_damage_over_time_effect_no_remaining()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_damage_over_time_effect_success()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_heal_over_time_effect_no_healing()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_heal_over_time_effect_no_remaining()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_heal_over_time_effect_success()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_single_effect_damage_over_time()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_single_effect_heal_over_time()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_single_effect_expired()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_update_player_status_effects_no_changes()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_update_player_status_effects_changes()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_status_effects_no_container()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_status_effects_no_online_players()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_combat_tick_no_service()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_process_combat_tick_success()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **mock_app()** (2 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **mock_container()** (2 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **mock_player()** (2 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- *... and 24 more nodes in this community*

## Relationships

- [Command Alias Handling](Command_Alias_Handling.md) (18 shared connections)
- [Connection Room Presence Utils](Connection_Room_Presence_Utils.md) (2 shared connections)
- [Player Respawn Events](Player_Respawn_Events.md) (1 shared connections)
- [Investigations Sessions Xx](Investigations_Sessions_Xx.md) (1 shared connections)
- [Database Manager Tests](Database_Manager_Tests.md) (1 shared connections)
- [Skill Service Tests](Skill_Service_Tests.md) (1 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing_async.py`

## Audit Trail

- EXTRACTED: 152 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*