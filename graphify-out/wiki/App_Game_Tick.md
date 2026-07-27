# App Game Tick

> 20 nodes · cohesion 0.16

## Key Concepts

- **test_game_tick_processing.py** (14 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **_validate_app_state_for_status_effects()** (12 connections) — `server/app/game_tick_processing.py`
- **reset_current_tick()** (6 connections) — `server/app/game_tick_processing.py`
- **Test _validate_app_state_for_status_effects returns False when no container.** (4 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_get_current_tick()** (4 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_reset_current_tick()** (4 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_get_tick_interval()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_validate_app_state_for_status_effects_connection_manager_is_none()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_validate_app_state_for_status_effects_container_is_none()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_validate_app_state_for_status_effects_no_async_persistence()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_validate_app_state_for_status_effects_no_connection_manager()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_validate_app_state_for_status_effects_no_container()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_validate_app_state_for_status_effects_valid()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **Reset the current tick for testing.** (1 connections) — `server/app/game_tick_processing.py`
- **Validate app state has required components for status effect processing.      Re** (1 connections) — `server/app/game_tick_processing.py`
- **Test get_current_tick returns the current tick value.** (1 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **Test reset_current_tick resets the tick counter.** (1 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **Test get_tick_interval returns tick interval from config.** (1 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **Test _validate_app_state_for_status_effects returns False when no async_persiste** (1 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **Test _validate_app_state_for_status_effects returns True when all required compo** (1 connections) — `server/tests/unit/app/test_game_tick_processing.py`

## Relationships

- [[Game Tick Processing]] (7 shared connections)
- [[Combat Attack Service]] (3 shared connections)
- [[App Lifespan Management]] (1 shared connections)
- [[Status Effect Tick Tests]] (1 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing.py`

## Audit Trail

- EXTRACTED: 72 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
