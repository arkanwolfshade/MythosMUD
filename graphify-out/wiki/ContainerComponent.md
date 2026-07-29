# ContainerComponent

> 53 nodes

## Key Concepts

- **ContainerComponent** (104 connections) — `server/models/container.py`
- **test_container.py** (38 connections) — `server/tests/unit/models/test_container.py`
- **Test is_locked returns True when lock_state is LOCKED.** (6 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_rejects_extra_fields()** (4 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_capacity_slots_validation_min()** (4 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_capacity_slots_validation_max()** (4 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_is_locked_when_locked()** (3 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_is_locked_when_sealed()** (3 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_is_locked_when_unlocked()** (3 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_is_unlocked_when_unlocked()** (3 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_is_unlocked_when_locked()** (3 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_is_unlocked_when_sealed()** (3 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_has_capacity_when_available()** (3 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_has_capacity_when_full()** (3 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_has_room_for_additional_items()** (3 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_has_room_for_exceeds_capacity()** (3 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_can_hold_replacement_items()** (3 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_would_exceed_capacity()** (3 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_can_hold_exceeds_capacity()** (3 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_get_used_slots()** (3 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_get_used_slots_empty()** (3 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_get_available_slots()** (3 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_get_available_slots_full()** (3 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_is_decayed_when_expired()** (3 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_is_decayed_when_not_expired()** (3 connections) — `server/tests/unit/models/test_container.py`
- *... and 28 more nodes in this community*

## Relationships

- [APIRouter](APIRouter.md) (26 shared connections)
- [test corpse lifecycle service](test_corpse_lifecycle_service.md) (14 shared connections)
- [.create corpse()](create_corpse%28%29.md) (12 shared connections)
- [emit close container event()](emit_close_container_event%28%29.md) (7 shared connections)
- [main()](main%28%29.md) (3 shared connections)
- [. init ()](_init_%28%29.md) (3 shared connections)
- [container websocket events](container_websocket_events.md) (2 shared connections)
- [Test can access corpse() handles](Test_can_access_corpse%28%29_handles.md) (2 shared connections)
- [AbstractContextManager](AbstractContextManager.md) (2 shared connections)
- [Base](Base.md) (1 shared connections)
- [.can hold()](can_hold%28%29.md) (1 shared connections)
- [.get available slots()](get_available_slots%28%29.md) (1 shared connections)

## Source Files

- `server/models/container.py`
- `server/tests/unit/models/test_container.py`

## Audit Trail

- EXTRACTED: 228 (89%)
- INFERRED: 28 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*