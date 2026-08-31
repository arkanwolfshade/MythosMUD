# inventory_unequip_command.py

> 39 nodes

## Key Concepts

- **inventory_unequip_command.py** (33 connections) — `server/commands/inventory_unequip_command.py`
- **get_shared_services()** (21 connections) — `server/commands/inventory_service_helpers.py`
- **EquipmentService** (18 connections) — `server/services/equipment_service.py`
- **handle_unequip_command()** (18 connections) — `server/commands/inventory_unequip_command.py`
- **inventory_service_helpers.py** (16 connections) — `server/commands/inventory_service_helpers.py`
- **test_inventory_unequip_command.py** (13 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- **_unequip_run_mutation()** (9 connections) — `server/commands/inventory_unequip_command.py`
- **handle_wearable_container_on_unequip()** (7 connections) — `server/commands/equipment_helpers.py`
- **_ensure_shared_services_initialized()** (7 connections) — `server/commands/inventory_service_helpers.py`
- **test_handle_unequip_command_slot_validation_error()** (7 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- **test_inventory_service_helpers.py** (7 connections) — `server/tests/unit/commands/test_inventory_service_helpers.py`
- **_unequip_success_payload()** (6 connections) — `server/commands/inventory_unequip_command.py`
- **test_handle_unequip_command_mutation_suppressed()** (6 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- **test_handle_unequip_command_persist_rollback()** (6 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- **test_handle_unequip_command_success()** (6 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- **_unequip_persist_or_rollback()** (5 connections) — `server/commands/inventory_unequip_command.py`
- **_mutation_cm()** (5 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- **_player_with_equipped()** (5 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- **_request_wiring()** (5 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- **CommandResponse** (4 connections)
- **asyncio** (4 connections)
- **reset_shared_inventory_services_for_tests()** (3 connections) — `server/commands/inventory_service_helpers.py`
- **_request_with_persistence()** (3 connections) — `server/tests/unit/commands/test_inventory_service_helpers.py`
- **reset_shared_inventory_services_autouse()** (3 connections) — `server/tests/unit/commands/test_inventory_service_helpers.py`
- **test_get_shared_services_initializes_and_reuses_singletons()** (3 connections) — `server/tests/unit/commands/test_inventory_service_helpers.py`
- *... and 14 more nodes in this community*

## Relationships

- [inventory_equip_command.py](inventory_equip_command.py.md) (17 shared connections)
- [test_inventory_helpers.py](test_inventory_helpers.py.md) (13 shared connections)
- [InventoryService](InventoryService.md) (10 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (8 shared connections)
- [command_result_text](command_result_text.md) (7 shared connections)
- [test_wearable_container_service.py](test_wearable_container_service.py.md) (5 shared connections)
- [test_container_helpers_inventory_find.py](test_container_helpers_inventory_find.py.md) (5 shared connections)
- [test_container_helpers_inventory_display.py](test_container_helpers_inventory_display.py.md) (3 shared connections)
- [AliasStorage](AliasStorage.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)
- [server/services/__init__.py](server-services-__init__.py.md) (1 shared connections)

## Source Files

- `server/commands/equipment_helpers.py`
- `server/commands/inventory_service_helpers.py`
- `server/commands/inventory_unequip_command.py`
- `server/services/equipment_service.py`
- `server/tests/unit/commands/test_inventory_service_helpers.py`
- `server/tests/unit/commands/test_inventory_unequip_command.py`

## Audit Trail

- EXTRACTED: 151 (94%)
- INFERRED: 9 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*