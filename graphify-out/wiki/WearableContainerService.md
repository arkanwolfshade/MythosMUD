# WearableContainerService

> 40 nodes

## Key Concepts

- **WearableContainerService** (37 connections) — `server/services/wearable_container_service.py`
- **UUID** (18 connections)
- **Any** (11 connections)
- **._load_player_wearable_container()** (9 connections) — `server/services/wearable_container_service.py`
- **_filter_container_data()** (8 connections) — `server/services/wearable_container_service.py`
- **_get_enum_value()** (8 connections) — `server/services/wearable_container_service.py`
- **.handle_container_overflow()** (8 connections) — `server/services/wearable_container_service.py`
- **.handle_equip_wearable_container()** (8 connections) — `server/services/wearable_container_service.py`
- **.add_items_to_wearable_container()** (7 connections) — `server/services/wearable_container_service.py`
- **.handle_unequip_wearable_container()** (7 connections) — `server/services/wearable_container_service.py`
- **._update_container_items_or_raise()** (7 connections) — `server/services/wearable_container_service.py`
- **.update_wearable_container_items()** (7 connections) — `server/services/wearable_container_service.py`
- **._create_equipment_container_record()** (6 connections) — `server/services/wearable_container_service.py`
- **._drop_overflow_to_ground()** (6 connections) — `server/services/wearable_container_service.py`
- **._find_existing_equipment_container()** (6 connections) — `server/services/wearable_container_service.py`
- **._validate_inner_container_capacity()** (6 connections) — `server/services/wearable_container_service.py`
- **_row_metadata()** (5 connections) — `server/services/wearable_container_service.py`
- **.get_wearable_containers_for_player()** (5 connections) — `server/services/wearable_container_service.py`
- **._save_overflow_inventory()** (5 connections) — `server/services/wearable_container_service.py`
- **._split_overflow_items()** (4 connections) — `server/services/wearable_container_service.py`
- **.__init__()** (3 connections) — `server/services/wearable_container_service.py`
- **A container row's metadata, whichever key it arrived under (metadata_json from…** (1 connections) — `server/services/wearable_container_service.py`
- **Service for managing wearable container operations. Handles container creation…** (1 connections) — `server/services/wearable_container_service.py`
- **Initialize the wearable container service. Args: persistence: Persistence layer…** (1 connections) — `server/services/wearable_container_service.py`
- **Validate inner container item count against capacity.** (1 connections) — `server/services/wearable_container_service.py`
- *... and 15 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (13 shared connections)
- [test_wearable_container_service.py](test_wearable_container_service.py.md) (11 shared connections)
- [_WearablePersistence](_WearablePersistence.md) (6 shared connections)
- [alias_storage.py](alias_storage.py.md) (3 shared connections)
- [equipment_service.py](equipment_service.py.md) (2 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (2 shared connections)
- [ContainerCreateParams](ContainerCreateParams.md) (2 shared connections)
- [ContainerComponent](ContainerComponent.md) (2 shared connections)
- [look_container.py](look_container.py.md) (1 shared connections)
- [wearable_service](wearable_service.md) (1 shared connections)
- [look_helpers.py](look_helpers.py.md) (1 shared connections)
- [asyncio](asyncio.md) (1 shared connections)

## Source Files

- `server/services/wearable_container_service.py`

## Audit Trail

- EXTRACTED: 114 (92%)
- INFERRED: 10 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*