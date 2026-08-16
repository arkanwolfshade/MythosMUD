# ContainerComponent

> 187 nodes

## Key Concepts

- **ContainerComponent** (100 connections) — `server/models/container.py`
- **ContainerSourceType** (89 connections) — `server/models/container.py`
- **ContainerLockState** (42 connections) — `server/models/container.py`
- **test_container.py** (40 connections) — `server/tests/unit/models/test_container.py`
- **InventoryStack** (36 connections) — `server/services/inventory_service.py`
- **models/container.py** (34 connections) — `server/models/container.py`
- **EnvironmentalContainerLoader** (18 connections) — `server/services/environmental_container_loader.py`
- **test_environmental_container_loader.py** (17 connections) — `server/tests/unit/services/test_environmental_container_loader.py`
- **_container()** (16 connections) — `server/tests/unit/services/test_container_service.py`
- **environmental_container_loader.py** (14 connections) — `server/services/environmental_container_loader.py`
- **.load_container_from_room_json()** (7 connections) — `server/services/environmental_container_loader.py`
- **ContainerFactoryOptions** (6 connections) — `server/models/container.py`
- **.migrate_room_container_to_postgresql()** (6 connections) — `server/services/environmental_container_loader.py`
- **.create_corpse()** (5 connections) — `server/models/container.py`
- **.validate_entity_id()** (5 connections) — `server/models/container.py`
- **.validate_lock_state()** (5 connections) — `server/models/container.py`
- **.validate_source_type()** (5 connections) — `server/models/container.py`
- **test_container_component_default_lock_state()** (5 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_get_available_slots()** (5 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_get_available_slots_full()** (5 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_get_used_slots()** (5 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_has_capacity_when_full()** (5 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_has_room_for_additional_items()** (5 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_has_room_for_exceeds_capacity()** (5 connections) — `server/tests/unit/models/test_container.py`
- **test_container_component_is_locked_when_locked()** (5 connections) — `server/tests/unit/models/test_container.py`
- *... and 162 more nodes in this community*

## Relationships

- [ContainerService](ContainerService.md) (33 shared connections)
- [test_corpse_lifecycle_service.py](test_corpse_lifecycle_service.py.md) (31 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (22 shared connections)
- [LootAllRequest](LootAllRequest.md) (20 shared connections)
- [ConnectionManager](ConnectionManager.md) (19 shared connections)
- [server/services/__init__.py](server-services-__init__.py.md) (15 shared connections)
- [test_wearable_container_service.py](test_wearable_container_service.py.md) (6 shared connections)
- [log_and_raise](log_and_raise.md) (5 shared connections)
- [Player](Player.md) (4 shared connections)
- [TestEmitLootAllEvent](TestEmitLootAllEvent.md) (4 shared connections)
- [ValidationError](ValidationError.md) (4 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (3 shared connections)

## Source Files

- `server/models/container.py`
- `server/services/environmental_container_loader.py`
- `server/services/inventory_service.py`
- `server/tests/unit/models/test_container.py`
- `server/tests/unit/services/test_container_service.py`
- `server/tests/unit/services/test_corpse_lifecycle_service.py`
- `server/tests/unit/services/test_environmental_container_loader.py`

## Audit Trail

- EXTRACTED: 336 (64%)
- INFERRED: 187 (36%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*