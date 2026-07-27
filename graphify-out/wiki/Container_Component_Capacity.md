# Container Component Capacity

> 199 nodes · cohesion 0.01

## Key Concepts

- **ContainerComponent** (90 connections) — `server/models/container.py`
- **test_corpse_lifecycle_service.py** (53 connections) — `server/tests/unit/services/test_corpse_lifecycle_service.py`
- **test_container.py** (36 connections) — `server/tests/unit/models/test_container.py`
- **Any** (8 connections) — `server/models/container.py`
- **_get_enum_value()** (8 connections) — `server/services/corpse_lifecycle_service.py`
- **.create_corpse()** (7 connections) — `server/models/container.py`
- **.create_environment()** (6 connections) — `server/models/container.py`
- **.create_equipment()** (6 connections) — `server/models/container.py`
- **Test is_locked returns True when lock_state is LOCKED.** (6 connections) — `server/tests/unit/models/test_container.py`
- **CorpseServiceError** (6 connections) — `server/services/corpse_lifecycle_service.py`
- **UUID** (5 connections) — `server/models/container.py`
- **CorpseNotFoundError** (5 connections) — `server/services/corpse_lifecycle_service.py`
- **WearableContainerServiceError** (5 connections) — `server/services/wearable_container_service.py`
- **.validate_entity_id()** (4 connections) — `server/models/container.py`
- **.validate_lock_state()** (4 connections) — `server/models/container.py`
- **.validate_source_type()** (4 connections) — `server/models/container.py`
- **.would_exceed_capacity()** (4 connections) — `server/models/container.py`
- **.has_room_for()** (3 connections) — `server/models/container.py`
- **.is_decayed()** (3 connections) — `server/models/container.py`
- **.to_dict()** (3 connections) — `server/models/container.py`
- **.validate_metadata_no_personal_data()** (3 connections) — `server/models/container.py`
- **.validate_room_id()** (3 connections) — `server/models/container.py`
- **test_container_component_can_hold_exceeds_capacity()** (3 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_can_hold_replacement_items()** (3 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_capacity_slots_valid_range()** (3 connections) — `server/tests/unit/models/test_container.py`
- *... and 174 more nodes in this community*

## Relationships

- [[Inventory Service Helpers]] (17 shared connections)
- [[Container API Endpoints]] (6 shared connections)
- [[Combat Death Handling]] (6 shared connections)
- [[Container Exception Handlers]] (5 shared connections)
- [[Loot All Endpoint]] (5 shared connections)
- [[NPC Admin API]] (5 shared connections)
- [[Container Open Events]] (4 shared connections)
- [[Container Loot Helpers]] (2 shared connections)
- [[Admin NPC Schemas]] (1 shared connections)
- [[SQLAlchemy Model Base]] (1 shared connections)
- [[API Test Fixtures]] (1 shared connections)
- [[Combat Player Broadcasts]] (1 shared connections)

## Source Files

- `server/models/container.py`
- `server/services/container_service.py`
- `server/services/corpse_lifecycle_service.py`
- `server/services/wearable_container_service.py`
- `server/tests/unit/models/test_container.py`
- `server/tests/unit/services/test_corpse_lifecycle_service.py`

## Audit Trail

- EXTRACTED: 580 (98%)
- INFERRED: 11 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
