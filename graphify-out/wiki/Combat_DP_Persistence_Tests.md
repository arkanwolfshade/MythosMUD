# Combat DP Persistence Tests

> 26 nodes

## Key Concepts

- **test_game_tick_processing.py** (15 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **_validate_app_state_for_status_effects()** (12 connections) — `server/app/game_tick_processing.py`
- **get_tick_interval()** (8 connections) — `server/app/game_tick_processing.py`
- **reset_current_tick()** (6 connections) — `server/app/game_tick_processing.py`
- **test_get_current_tick()** (4 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_reset_current_tick()** (4 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_get_tick_interval()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_validate_app_state_for_status_effects_no_container()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_validate_app_state_for_status_effects_no_async_persistence()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_validate_app_state_for_status_effects_no_connection_manager()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_validate_app_state_for_status_effects_valid()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_validate_app_state_for_status_effects_container_is_none()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_validate_app_state_for_status_effects_connection_manager_is_none()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **Reset the current tick for testing.** (1 connections) — `server/app/game_tick_processing.py`
- **Get the server tick interval from configuration.      Returns:         float: Ti** (1 connections) — `server/app/game_tick_processing.py`
- **Validate app state has required components for status effect processing.      Re** (1 connections) — `server/app/game_tick_processing.py`
- **Unit tests for game tick processing functions.  Tests the game tick processing l** (1 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **Test get_current_tick returns the current tick value.** (1 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **Test reset_current_tick resets the tick counter.** (1 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **Test get_tick_interval returns tick interval from config.** (1 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **Test _validate_app_state_for_status_effects returns False when no container.** (1 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **Test _validate_app_state_for_status_effects returns False when no async_persiste** (1 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **Test _validate_app_state_for_status_effects returns False when no connection_man** (1 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **Test _validate_app_state_for_status_effects returns True when all required compo** (1 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **Test _validate_app_state_for_status_effects returns False when container is None** (1 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- *... and 1 more nodes in this community*

## Relationships

- [Legacy Error Sanitization](Legacy_Error_Sanitization.md) (8 shared connections)
- [Rest Command Flow](Rest_Command_Flow.md) (4 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (2 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (1 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing.py`

## Audit Trail

- EXTRACTED: 82 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*