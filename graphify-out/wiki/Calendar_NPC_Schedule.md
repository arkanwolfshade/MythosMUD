# Calendar NPC Schedule

> 9 nodes

## Key Concepts

- **Any** (8 connections)
- **_update_player_status_effects()** (7 connections) — `server/app/game_tick_processing.py`
- **_cleanup_single_decayed_corpse()** (6 connections) — `server/app/game_tick_processing.py`
- **test_update_player_status_effects_no_changes()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_update_player_status_effects_changes()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **Update and save player status effects if changes occurred.      Returns:** (1 connections) — `server/app/game_tick_processing.py`
- **Cleanup a single decayed corpse.      Args:         corpse_service: Corpse lifec** (1 connections) — `server/app/game_tick_processing.py`
- **Test _update_player_status_effects() when no changes occurred.** (1 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **Test _update_player_status_effects() when changes occurred.** (1 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`

## Relationships

- [Command Alias Handling](Command_Alias_Handling.md) (6 shared connections)
- [Legacy Error Sanitization](Legacy_Error_Sanitization.md) (5 shared connections)
- [Multiplayer Browser Helpers](Multiplayer_Browser_Helpers.md) (2 shared connections)
- [Magic Command Handlers](Magic_Command_Handlers.md) (1 shared connections)
- [Skill Service Tests](Skill_Service_Tests.md) (1 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing_async.py`

## Audit Trail

- EXTRACTED: 31 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*