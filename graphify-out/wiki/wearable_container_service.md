# wearable container service

> 133 nodes

## Key Concepts

- **test_wearable_container_service.py** (62 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **_get_enum_value()** (9 connections) — `server/services/wearable_container_service.py`
- **_filter_container_data()** (9 connections) — `server/services/wearable_container_service.py`
- **Any** (8 connections)
- **.add_items_to_wearable_container()** (8 connections) — `server/services/wearable_container_service.py`
- **.update_wearable_container_items()** (8 connections) — `server/services/wearable_container_service.py`
- **UUID** (7 connections)
- **.handle_equip_wearable_container()** (6 connections) — `server/services/wearable_container_service.py`
- **.handle_unequip_wearable_container()** (6 connections) — `server/services/wearable_container_service.py`
- **.handle_container_overflow()** (6 connections) — `server/services/wearable_container_service.py`
- **.get_wearable_containers_for_player()** (5 connections) — `server/services/wearable_container_service.py`
- **.__init__()** (3 connections) — `server/services/wearable_container_service.py`
- **wearable_service()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_wearable_container_service_init_no_persistence()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_handle_equip_wearable_container_capacity_exceeded()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_add_items_to_wearable_container_not_found()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_add_items_to_wearable_container_capacity_exceeded()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_handle_container_overflow_player_not_found()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_handle_equip_wearable_container_creation_error()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_add_items_to_wearable_container_wrong_player()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_add_items_to_wearable_container_wrong_source_type()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_add_items_to_wearable_container_update_fails()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_update_wearable_container_items_not_found()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_update_wearable_container_items_capacity_exceeded()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- **test_update_wearable_container_items_update_fails()** (3 connections) — `server/tests/unit/services/test_wearable_container_service.py`
- *... and 108 more nodes in this community*

## Relationships

- [command inventory factories](command_inventory_factories.md) (22 shared connections)
- [retry nats handler](retry_nats_handler.md) (10 shared connections)
- [Database Config](Database_Config.md) (4 shared connections)
- [Exception Containers](Exception_Containers.md) (1 shared connections)

## Source Files

- `server/services/wearable_container_service.py`
- `server/tests/unit/services/test_wearable_container_service.py`

## Audit Trail

- EXTRACTED: 314 (95%)
- INFERRED: 17 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*