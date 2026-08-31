# equipment_service.py

> 68 nodes

## Key Concepts

- **equipment_service.py** (23 connections) — `server/services/equipment_service.py`
- **test_equipment_service.py** (23 connections) — `server/tests/unit/services/test_equipment_service.py`
- **get_shared_services()** (21 connections) — `server/commands/inventory_service_helpers.py`
- **EquipmentService** (18 connections) — `server/services/equipment_service.py`
- **inventory_service_helpers.py** (16 connections) — `server/commands/inventory_service_helpers.py`
- **EquipmentCapacityError** (11 connections) — `server/services/equipment_service.py`
- **.equip_from_inventory()** (10 connections) — `server/services/equipment_service.py`
- **.unequip_to_inventory()** (8 connections) — `server/services/equipment_service.py`
- **_ensure_shared_services_initialized()** (7 connections) — `server/commands/inventory_service_helpers.py`
- **test_inventory_service_helpers.py** (7 connections) — `server/tests/unit/commands/test_inventory_service_helpers.py`
- **EquipmentServiceError** (6 connections) — `server/services/equipment_service.py`
- **_clone_equipped()** (6 connections) — `server/services/equipment_service.py`
- **_clone_inventory()** (6 connections) — `server/services/equipment_service.py`
- **InventoryStack** (5 connections)
- **_resolve_effective_equip_slot()** (4 connections) — `server/services/equipment_service.py`
- **equipment_service()** (4 connections) — `server/tests/unit/services/test_equipment_service.py`
- **inventory_service()** (4 connections) — `server/tests/unit/services/test_equipment_service.py`
- **Any** (4 connections)
- **reset_shared_inventory_services_for_tests()** (3 connections) — `server/commands/inventory_service_helpers.py`
- **._maybe_log_wearable_container_failure()** (3 connections) — `server/services/equipment_service.py`
- **_request_with_persistence()** (3 connections) — `server/tests/unit/commands/test_inventory_service_helpers.py`
- **reset_shared_inventory_services_autouse()** (3 connections) — `server/tests/unit/commands/test_inventory_service_helpers.py`
- **test_get_shared_services_initializes_and_reuses_singletons()** (3 connections) — `server/tests/unit/commands/test_inventory_service_helpers.py`
- **test_get_shared_services_raises_without_async_persistence()** (3 connections) — `server/tests/unit/commands/test_inventory_service_helpers.py`
- **test_equip_from_inventory_capacity_error()** (3 connections) — `server/tests/unit/services/test_equipment_service.py`
- *... and 43 more nodes in this community*

## Relationships

- [server/services/__init__.py](server-services-__init__.py.md) (20 shared connections)
- [inventory_equip_command.py](inventory_equip_command.py.md) (19 shared connections)
- [inventory_unequip_command.py](inventory_unequip_command.py.md) (9 shared connections)
- [test_wearable_container_service.py](test_wearable_container_service.py.md) (7 shared connections)
- [test_container_helpers_inventory_find.py](test_container_helpers_inventory_find.py.md) (5 shared connections)
- [test_container_helpers_inventory_display.py](test_container_helpers_inventory_display.py.md) (3 shared connections)
- [test_inventory_helpers.py](test_inventory_helpers.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)
- [.state](state.md) (1 shared connections)
- [test_equipment_helpers.py](test_equipment_helpers.py.md) (1 shared connections)

## Source Files

- `server/commands/inventory_service_helpers.py`
- `server/services/equipment_service.py`
- `server/tests/unit/commands/test_inventory_service_helpers.py`
- `server/tests/unit/services/test_equipment_service.py`

## Audit Trail

- EXTRACTED: 152 (90%)
- INFERRED: 17 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*