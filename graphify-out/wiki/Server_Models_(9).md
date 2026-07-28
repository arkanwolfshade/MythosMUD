# Server Models (9)

> 75 nodes

## Key Concepts

- **ContainerComponent** (104 connections) — `server/models/container.py`
- **test_container.py** (38 connections) — `server/tests/unit/models/test_container.py`
- **Test is_locked returns True when lock_state is LOCKED.** (6 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_rejects_extra_fields()** (4 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_capacity_slots_validation_min()** (4 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_capacity_slots_validation_max()** (4 connections) — `server/tests/unit/models/test_container.py`
- **mock_container()** (3 connections) — `server/tests/unit/api/conftest.py`
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
- *... and 50 more nodes in this community*

## Relationships

- [Server Api (2)](Server_Api_%282%29.md) (29 shared connections)
- [Server Services (19)](Server_Services_%2819%29.md) (18 shared connections)
- [Server Models (22)](Server_Models_%2822%29.md) (12 shared connections)
- [Server Api](Server_Api.md) (7 shared connections)
- [Server Utils](Server_Utils.md) (3 shared connections)
- [Server Services (43)](Server_Services_%2843%29.md) (2 shared connections)
- [Server Api (14)](Server_Api_%2814%29.md) (2 shared connections)
- [Server Models (14)](Server_Models_%2814%29.md) (1 shared connections)
- [Server Services (46)](Server_Services_%2846%29.md) (1 shared connections)
- [Server Services (66)](Server_Services_%2866%29.md) (1 shared connections)

## Source Files

- `server/models/container.py`
- `server/tests/unit/api/conftest.py`
- `server/tests/unit/models/test_container.py`

## Audit Trail

- EXTRACTED: 261 (90%)
- INFERRED: 29 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*