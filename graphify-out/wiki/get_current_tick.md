# get_current_tick

> 28 nodes

## Key Concepts

- **get_current_tick()** (15 connections) — `server/app/game_tick_processing.py`
- **test_game_tick_processing.py** (15 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **_validate_app_state_for_status_effects()** (12 connections) — `server/app/game_tick_processing.py`
- **get_tick_interval()** (8 connections) — `server/app/game_tick_processing.py`
- **reset_current_tick()** (6 connections) — `server/app/game_tick_processing.py`
- **test_get_current_tick()** (4 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_reset_current_tick()** (4 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_get_tick_interval()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_validate_app_state_for_status_effects_connection_manager_is_none()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_validate_app_state_for_status_effects_container_is_none()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_validate_app_state_for_status_effects_no_async_persistence()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_validate_app_state_for_status_effects_no_connection_manager()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_validate_app_state_for_status_effects_no_container()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **test_validate_app_state_for_status_effects_valid()** (3 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **Get the current game tick.** (1 connections) — `server/app/game_tick_processing.py`
- **Reset the current tick for testing.** (1 connections) — `server/app/game_tick_processing.py`
- **Get the server tick interval from configuration. Returns: float: Tick interval…** (1 connections) — `server/app/game_tick_processing.py`
- **Validate app state has required components for status effect processing.…** (1 connections) — `server/app/game_tick_processing.py`
- **Unit tests for game tick processing functions. Tests the game tick processing…** (1 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **Test _validate_app_state_for_status_effects returns False when container is…** (1 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **Test _validate_app_state_for_status_effects returns False when…** (1 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **Test get_current_tick returns the current tick value.** (1 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **Test reset_current_tick resets the tick counter.** (1 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **Test get_tick_interval returns tick interval from config.** (1 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- **Test _validate_app_state_for_status_effects returns False when no container.** (1 connections) — `server/tests/unit/app/test_game_tick_processing.py`
- *... and 3 more nodes in this community*

## Relationships

- [game_tick_processing.py](game_tick_processing.py.md) (9 shared connections)
- [PlayerService](PlayerService.md) (4 shared connections)
- [CombatService](CombatService.md) (2 shared connections)
- [lifespan.py](lifespan.py.md) (2 shared connections)
- [_NPCCombatIntegrationDeps](_NPCCombatIntegrationDeps.md) (2 shared connections)
- [_MagicServiceCore](_MagicServiceCore.md) (1 shared connections)
- [magic_service.py](magic_service.py.md) (1 shared connections)
- [is_player_in_login_grace_period](is_player_in_login_grace_period.md) (1 shared connections)
- [get_config](get_config.md) (1 shared connections)

## Source Files

- `server/app/game_tick_processing.py`
- `server/tests/unit/app/test_game_tick_processing.py`

## Audit Trail

- EXTRACTED: 94 (95%)
- INFERRED: 5 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*