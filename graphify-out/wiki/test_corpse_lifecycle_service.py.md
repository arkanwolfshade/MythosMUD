# test_corpse_lifecycle_service.py

> 74 nodes

## Key Concepts

- **test_corpse_lifecycle_service.py** (56 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **asyncio** (23 connections)
- **corpse_lifecycle_service.py** (19 connections) — `server/services/corpse_lifecycle_service.py`
- **CorpseServiceError** (11 connections) — `server/services/corpse_lifecycle_service.py`
- **_get_enum_value()** (8 connections) — `server/services/corpse_lifecycle_service.py`
- **CorpseNotFoundError** (6 connections) — `server/services/corpse_lifecycle_service.py`
- **test_cleanup_decayed_corpse_not_corpse()** (5 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_create_corpse_on_death_success()** (5 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **corpse_service()** (4 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_cleanup_decayed_corpse_delete_error()** (4 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_cleanup_decayed_corpse_not_found()** (4 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_corpse_not_found_error()** (4 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_create_corpse_on_death_custom_grace_period()** (4 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_create_corpse_on_death_persistence_error()** (4 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_create_corpse_on_death_player_no_name()** (4 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_create_corpse_on_death_player_not_found()** (4 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_get_all_decayed_corpses()** (4 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_get_all_decayed_corpses_non_corpse()** (4 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_get_decayed_corpses_in_room_non_corpse()** (4 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_get_decayed_corpses_in_room_with_decayed()** (4 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **mock_persistence()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_cleanup_all_decayed_corpses()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_cleanup_all_decayed_corpses_handles_errors()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_cleanup_decayed_corpse_success()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_cleanup_decayed_corpses_in_room()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- *... and 49 more nodes in this community*

## Relationships

- [ContainerComponent](ContainerComponent.md) (36 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (3 shared connections)
- [ContainerLockState](ContainerLockState.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [TransferContainerRequest](TransferContainerRequest.md) (2 shared connections)
- [log_and_raise](log_and_raise.md) (1 shared connections)
- [test_game_tick_death.py](test_game_tick_death.py.md) (1 shared connections)
- [error_logging.py](error_logging.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/services/corpse_lifecycle_service.py`
- `server/tests/unit/services/test_corpse_lifecycle_service.py`

## Audit Trail

- EXTRACTED: 143 (90%)
- INFERRED: 16 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*