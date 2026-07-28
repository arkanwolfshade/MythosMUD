# Archive Circuit Breaker

> 11 nodes · cohesion 0.18

## Key Concepts

- **Any** (7 connections)
- **_update_player_status_effects()** (7 connections) — `server/app/game_tick_processing.py`
- **_cleanup_single_decayed_corpse()** (6 connections) — `server/app/game_tick_processing.py`
- **_process_single_player_mp_regeneration()** (5 connections) — `server/app/game_tick_processing.py`
- **test_update_player_status_effects_changes()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **test_update_player_status_effects_no_changes()** (3 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **Update and save player status effects if changes occurred.      Returns:** (1 connections) — `server/app/game_tick_processing.py`
- **Process MP regeneration for a single player.      Args:         mp_service: MP r** (1 connections) — `server/app/game_tick_processing.py`
- **Cleanup a single decayed corpse.      Args:         corpse_service: Corpse lifec** (1 connections) — `server/app/game_tick_processing.py`
- **Test _update_player_status_effects() when no changes occurred.** (1 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`
- **Test _update_player_status_effects() when changes occurred.** (1 connections) — `server/tests/unit/app/test_game_tick_processing_async.py`

## Relationships

- [Game Tick Processing](Game_Tick_Processing.md) (7 shared connections)
- [Health Service Tests](Health_Service_Tests.md) (6 shared connections)
- [Container Open Events](Container_Open_Events.md) (1 shared connections)
- [E2E Whisper Fix Report](E2E_Whisper_Fix_Report.md) (1 shared connections)
- [Fresh Session Test Guide](Fresh_Session_Test_Guide.md) (1 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing_async.py`

## Audit Trail

- EXTRACTED: 36 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*