# Server Services (19)

> 86 nodes

## Key Concepts

- **test_corpse_lifecycle_service.py** (55 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **CorpseServiceError** (13 connections) — `server/services/corpse_lifecycle_service.py`
- **CorpseNotFoundError** (7 connections) — `server/services/corpse_lifecycle_service.py`
- **test_corpse_not_found_error()** (4 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_corpse_service_error()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_create_corpse_on_death_success()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_create_corpse_on_death_player_not_found()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_create_corpse_on_death_persistence_error()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_can_access_corpse_admin()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_can_access_corpse_owner()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_can_access_corpse_no_owner()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_can_access_corpse_grace_period_active()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_can_access_corpse_grace_period_expired()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_can_access_corpse_invalid_grace_period()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_is_corpse_decayed_not_decayed()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_is_corpse_decayed_decayed()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_is_corpse_decayed_no_decay_time()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_is_corpse_decayed_uses_real_time_not_mythos_time()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_cleanup_decayed_corpse_not_found()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_cleanup_decayed_corpse_not_corpse()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_can_access_corpse_no_grace_period_start()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_can_access_corpse_grace_period_type_error()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_cleanup_decayed_corpse_delete_error()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_create_corpse_on_death_player_no_name()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_create_corpse_on_death_custom_grace_period()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- *... and 61 more nodes in this community*

## Relationships

- [Server Models (9)](Server_Models_%289%29.md) (18 shared connections)
- [Server Services (46)](Server_Services_%2846%29.md) (12 shared connections)
- [Server Api (2)](Server_Api_%282%29.md) (3 shared connections)
- [Server Error Handlers](Server_Error_Handlers.md) (1 shared connections)

## Source Files

- `server/services/corpse_lifecycle_service.py`
- `server/tests/unit/services/test_corpse_lifecycle_service.py`

## Audit Trail

- EXTRACTED: 208 (92%)
- INFERRED: 18 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*