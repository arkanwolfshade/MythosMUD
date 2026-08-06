# database config helpers

> 14 nodes

## Key Concepts

- **_validate_app_state_for_status_effects()** (12 connections) — `server/app/game_tick_processing.py`
- **test_validate_app_state_for_status_effects_no_container()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_validate_app_state_for_status_effects_no_async_persistence()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_validate_app_state_for_status_effects_no_connection_manager()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_validate_app_state_for_status_effects_valid()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_validate_app_state_for_status_effects_container_is_none()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_validate_app_state_for_status_effects_connection_manager_is_none()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **Validate app state has required components for status effect processing.      Re** (1 connections) — `server/app/game_tick_processing.py`
- **Test _validate_app_state_for_status_effects returns False when no container.** (1 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **Test _validate_app_state_for_status_effects returns False when no async_persiste** (1 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **Test _validate_app_state_for_status_effects returns False when no connection_man** (1 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **Test _validate_app_state_for_status_effects returns True when all required compo** (1 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **Test _validate_app_state_for_status_effects returns False when container is None** (1 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **Test _validate_app_state_for_status_effects returns False when connection_manage** (1 connections) — `server/tests/unit/app/test_game_tick_processing.py`

## Relationships

- [map RoomMapViewer mapUtils](map_RoomMapViewer_mapUtils.md) (8 shared connections)
- [schemas calendar rationale](schemas_calendar_rationale.md) (2 shared connections)
- [command helpers functions](command_helpers_functions.md) (1 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing.py`

## Audit Trail

- EXTRACTED: 37 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*