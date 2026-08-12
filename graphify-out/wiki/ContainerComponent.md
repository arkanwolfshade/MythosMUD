# ContainerComponent

> 139 nodes

## Key Concepts

- **ContainerComponent** (90 connections) — `server/models/container.py`
- **test_container.py** (38 connections) — `server/tests/unit/models/test_container.py`
- **ContainerFactoryOptions** (6 connections) — `server/models/container.py`
- **.create_corpse()** (5 connections) — `server/models/container.py`
- **.validate_entity_id()** (5 connections) — `server/models/container.py`
- **.validate_lock_state()** (5 connections) — `server/models/container.py`
- **.validate_source_type()** (5 connections) — `server/models/container.py`
- **Any** (5 connections)
- **field_validator** (5 connections)
- **UUID** (5 connections)
- **.create_environment()** (4 connections) — `server/models/container.py`
- **.create_equipment()** (4 connections) — `server/models/container.py`
- **.validate_metadata_no_personal_data()** (4 connections) — `server/models/container.py`
- **.validate_room_id()** (4 connections) — `server/models/container.py`
- **.would_exceed_capacity()** (4 connections) — `server/models/container.py`
- **.has_room_for()** (3 connections) — `server/models/container.py`
- **.is_decayed()** (3 connections) — `server/models/container.py`
- **.to_dict()** (3 connections) — `server/models/container.py`
- **test_container_component_can_hold_exceeds_capacity()** (3 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_can_hold_replacement_items()** (3 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_capacity_slots_valid_range()** (3 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_capacity_slots_validation_max()** (3 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_capacity_slots_validation_min()** (3 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_default_items()** (3 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_default_lock_state()** (3 connections) — `server/tests/unit/models/test_container.py`
- *... and 114 more nodes in this community*

## Relationships

- [LootAllRequest](LootAllRequest.md) (18 shared connections)
- [test_corpse_lifecycle_service.py](test_corpse_lifecycle_service.py.md) (16 shared connections)
- [asyncio](asyncio.md) (8 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (3 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (2 shared connections)
- [server/services/__init__.py](server-services-__init__.py.md) (2 shared connections)
- [Player](Player.md) (1 shared connections)
- [WearableContainerService](WearableContainerService.md) (1 shared connections)
- [api/conftest.py](api-conftest.py.md) (1 shared connections)

## Source Files

- `server/models/container.py`
- `server/tests/unit/models/test_container.py`
- `server/tests/unit/services/test_corpse_lifecycle_service.py`

## Audit Trail

- EXTRACTED: 403 (97%)
- INFERRED: 11 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*