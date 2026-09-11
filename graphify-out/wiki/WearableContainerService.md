# WearableContainerService

> 36 nodes

## Key Concepts

- **WearableContainerService** (28 connections) — `server/services/wearable_container_service.py`
- **Any** (15 connections)
- **UUID** (14 connections)
- **._load_player_wearable_container()** (9 connections) — `server/services/wearable_container_service.py`
- **_filter_container_data()** (8 connections) — `server/services/wearable_container_service.py`
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
- **Return existing equipment container ID for item instance if present.** (1 connections) — `server/services/wearable_container_service.py`
- **Create wearable container in persistence and return container_id payload.** (1 connections) — `server/services/wearable_container_service.py`
- **Handle equipping a wearable container item. Creates a container in PostgreSQL…** (1 connections) — `server/services/wearable_container_service.py`
- **Handle unequipping a wearable container item. Preserves the container and its…** (1 connections) — `server/services/wearable_container_service.py`
- **Get all wearable containers for a player. Args: player_id: UUID of the player…** (1 connections) — `server/services/wearable_container_service.py`
- **Load container and verify it belongs to the player's equipment.** (1 connections) — `server/services/wearable_container_service.py`
- *... and 11 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (10 shared connections)
- [inventory_equip_command.py](inventory_equip_command.py.md) (6 shared connections)
- [test_wearable_container_service.py](test_wearable_container_service.py.md) (4 shared connections)
- [_get_enum_value](_get_enum_value.md) (3 shared connections)
- [look_helpers.py](look_helpers.py.md) (2 shared connections)
- [ContainerComponent](ContainerComponent.md) (2 shared connections)
- [wearable_service](wearable_service.md) (1 shared connections)

## Source Files

- `server/services/wearable_container_service.py`

## Audit Trail

- EXTRACTED: 98 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*