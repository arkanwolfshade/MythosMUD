# test_corpse_lifecycle_service.py

> 64 nodes

## Key Concepts

- **test_corpse_lifecycle_service.py** (56 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **asyncio** (23 connections)
- **CorpseServiceError** (11 connections) — `server/services/corpse_lifecycle_service.py`
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
- **test_cleanup_decayed_corpses_in_room_handles_errors()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_corpse_service_error()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- *... and 39 more nodes in this community*

## Relationships

- [ContainerComponent](ContainerComponent.md) (25 shared connections)
- [CorpseLifecycleService](CorpseLifecycleService.md) (9 shared connections)
- [ContainerLockState](ContainerLockState.md) (2 shared connections)
- [MythosMUDError](MythosMUDError.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/services/corpse_lifecycle_service.py`
- `server/tests/unit/services/test_corpse_lifecycle_service.py`

## Audit Trail

- EXTRACTED: 117 (88%)
- INFERRED: 16 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*