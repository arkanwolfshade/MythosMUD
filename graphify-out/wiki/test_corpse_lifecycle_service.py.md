# test_corpse_lifecycle_service.py

> 69 nodes

## Key Concepts

- **test_corpse_lifecycle_service.py** (56 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **asyncio** (23 connections)
- **CorpseServiceError** (11 connections) — `server/services/corpse_lifecycle_service.py`
- **CorpseNotFoundError** (6 connections) — `server/services/corpse_lifecycle_service.py`
- **test_can_access_corpse_admin()** (5 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_can_access_corpse_invalid_grace_period()** (5 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_cleanup_decayed_corpse_not_corpse()** (5 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_create_corpse_on_death_success()** (5 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_is_corpse_decayed_timezone_aware()** (5 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_is_corpse_decayed_timezone_naive_vs_aware()** (5 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
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
- **test_cleanup_all_decayed_corpses()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_cleanup_all_decayed_corpses_handles_errors()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_cleanup_decayed_corpse_success()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_cleanup_decayed_corpses_in_room()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- *... and 44 more nodes in this community*

## Relationships

- [ContainerLockState](ContainerLockState.md) (15 shared connections)
- [ContainerSourceType](ContainerSourceType.md) (11 shared connections)
- [CorpseLifecycleService](CorpseLifecycleService.md) (10 shared connections)
- [ContainerComponent](ContainerComponent.md) (8 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/services/corpse_lifecycle_service.py`
- `server/tests/unit/services/test_corpse_lifecycle_service.py`

## Audit Trail

- EXTRACTED: 116 (79%)
- INFERRED: 30 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*