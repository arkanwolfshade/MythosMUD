# test corpse lifecycle service

> 65 nodes

## Key Concepts

- **test_corpse_lifecycle_service.py** (55 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **corpse_service()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_corpse_lifecycle_service_init_no_persistence()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_create_corpse_on_death_success()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_can_access_corpse_admin()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_can_access_corpse_owner()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_can_access_corpse_grace_period_active()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_can_access_corpse_grace_period_expired()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_is_corpse_decayed_not_decayed()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_is_corpse_decayed_decayed()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_is_corpse_decayed_no_decay_time()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_is_corpse_decayed_uses_real_time_not_mythos_time()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_can_access_corpse_no_grace_period_start()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_create_corpse_on_death_player_no_name()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_create_corpse_on_death_custom_grace_period()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_is_corpse_decayed_timezone_aware()** (3 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **mock_persistence()** (2 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_corpse_lifecycle_service_init()** (2 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_get_decayed_corpses_in_room_empty()** (2 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_get_decayed_corpses_in_room_with_decayed()** (2 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_cleanup_decayed_corpse_success()** (2 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_cleanup_decayed_corpses_in_room()** (2 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_get_all_decayed_corpses()** (2 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_cleanup_all_decayed_corpses()** (2 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_get_decayed_corpses_in_room_validation_error()** (2 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- *... and 40 more nodes in this community*

## Relationships

- [ContainerComponent](ContainerComponent.md) (14 shared connections)
- [CorpseNotFoundError](CorpseNotFoundError.md) (9 shared connections)
- [APIRouter](APIRouter.md) (3 shared connections)
- [.can access corpse()](can_access_corpse%28%29.md) (3 shared connections)
- [initialize nats and combat services()](initialize_nats_and_combat_services%28%29.md) (3 shared connections)
- [Test can access corpse() handles](Test_can_access_corpse%28%29_handles.md) (2 shared connections)
- [main()](main%28%29.md) (1 shared connections)
- [Test can access corpse() allows](Test_can_access_corpse%28%29_allows.md) (1 shared connections)
- [Test is corpse decayed() handles](Test_is_corpse_decayed%28%29_handles.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_corpse_lifecycle_service.py`

## Audit Trail

- EXTRACTED: 164 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*