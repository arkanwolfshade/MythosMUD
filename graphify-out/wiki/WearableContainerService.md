# WearableContainerService

> 39 nodes

## Key Concepts

- **WearableContainerService** (31 connections) — `server/services/wearable_container_service.py`
- **Any** (15 connections)
- **UUID** (14 connections)
- **._load_player_wearable_container()** (9 connections) — `server/services/wearable_container_service.py`
- **_filter_container_data()** (8 connections) — `server/services/wearable_container_service.py`
- **_get_enum_value()** (8 connections) — `server/services/wearable_container_service.py`
- **.handle_container_overflow()** (8 connections) — `server/services/wearable_container_service.py`
- **.handle_equip_wearable_container()** (8 connections) — `server/services/wearable_container_service.py`
- **.add_items_to_wearable_container()** (7 connections) — `server/services/wearable_container_service.py`
- **._update_container_items_or_raise()** (7 connections) — `server/services/wearable_container_service.py`
- **.update_wearable_container_items()** (7 connections) — `server/services/wearable_container_service.py`
- **.handle_unequip_wearable_container()** (6 connections) — `server/services/wearable_container_service.py`
- **._validate_inner_container_capacity()** (6 connections) — `server/services/wearable_container_service.py`
- **._create_equipment_container_record()** (5 connections) — `server/services/wearable_container_service.py`
- **._drop_overflow_to_ground()** (5 connections) — `server/services/wearable_container_service.py`
- **._find_existing_equipment_container()** (5 connections) — `server/services/wearable_container_service.py`
- **.get_wearable_containers_for_player()** (5 connections) — `server/services/wearable_container_service.py`
- **._save_overflow_inventory()** (5 connections) — `server/services/wearable_container_service.py`
- **._split_overflow_items()** (4 connections) — `server/services/wearable_container_service.py`
- **.__init__()** (3 connections) — `server/services/wearable_container_service.py`
- **ContainerComponent** (2 connections)
- **Return existing equipment container ID for item instance if present.** (1 connections) — `server/services/wearable_container_service.py`
- **Create wearable container in persistence and return container_id payload.** (1 connections) — `server/services/wearable_container_service.py`
- **Handle equipping a wearable container item. Creates a container in PostgreSQL…** (1 connections) — `server/services/wearable_container_service.py`
- **Handle unequipping a wearable container item. Preserves the container and its…** (1 connections) — `server/services/wearable_container_service.py`
- *... and 14 more nodes in this community*

## Relationships

- [server/services/__init__.py](server-services-__init__.py.md) (9 shared connections)
- [log_and_raise](log_and_raise.md) (7 shared connections)
- [test_wearable_container_service.py](test_wearable_container_service.py.md) (5 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [test_look_player.py](test_look_player.py.md) (2 shared connections)
- [test_wearable_container_service_init_no_persistence](test_wearable_container_service_init_no_persistence.md) (1 shared connections)
- [wearable_service](wearable_service.md) (1 shared connections)
- [test_get_enum_value_with_enum](test_get_enum_value_with_enum.md) (1 shared connections)

## Source Files

- `server/services/wearable_container_service.py`

## Audit Trail

- EXTRACTED: 104 (96%)
- INFERRED: 4 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*