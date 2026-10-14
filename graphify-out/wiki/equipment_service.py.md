# equipment_service.py

> 69 nodes

## Key Concepts

- **equipment_service.py** (23 connections) — `server/services/equipment_service.py`
- **test_equipment_service.py** (22 connections) — `server/tests/unit/services/test_equipment_service.py`
- **SlotValidationError** (21 connections) — `server/services/equipment_service.py`
- **handle_unequip_command()** (20 connections) — `server/commands/inventory_unequip_command.py`
- **EquipmentService** (18 connections) — `server/services/equipment_service.py`
- **test_inventory_unequip_command.py** (13 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- **EquipmentCapacityError** (11 connections) — `server/services/equipment_service.py`
- **.equip_from_inventory()** (10 connections) — `server/services/equipment_service.py`
- **.unequip_to_inventory()** (8 connections) — `server/services/equipment_service.py`
- **test_handle_unequip_command_emits_inventory_updated()** (7 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- **test_handle_unequip_command_slot_validation_error()** (7 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- **EquipmentServiceError** (6 connections) — `server/services/equipment_service.py`
- **_clone_equipped()** (6 connections) — `server/services/equipment_service.py`
- **_clone_inventory()** (6 connections) — `server/services/equipment_service.py`
- **_mutation_cm()** (6 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- **_player_with_equipped()** (6 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- **_request_wiring()** (6 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- **test_handle_unequip_command_mutation_suppressed()** (6 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- **test_handle_unequip_command_persist_rollback()** (6 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- **test_handle_unequip_command_success()** (6 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- **InventoryStack** (5 connections)
- **asyncio** (5 connections)
- **_resolve_effective_equip_slot()** (4 connections) — `server/services/equipment_service.py`
- **equipment_service()** (4 connections) — `server/tests/unit/services/test_equipment_service.py`
- **inventory_service()** (4 connections) — `server/tests/unit/services/test_equipment_service.py`
- *... and 44 more nodes in this community*

## Relationships

- [alias_storage.py](alias_storage.py.md) (31 shared connections)
- [get_logger](get_logger.md) (8 shared connections)
- [InventoryService](InventoryService.md) (4 shared connections)
- [ContainerComponent](ContainerComponent.md) (4 shared connections)
- [WearableContainerService](WearableContainerService.md) (2 shared connections)
- [command_result_text](command_result_text.md) (2 shared connections)
- [command_error](command_error.md) (1 shared connections)
- [AliasStorage](AliasStorage.md) (1 shared connections)

## Source Files

- `server/commands/inventory_unequip_command.py`
- `server/services/equipment_service.py`
- `server/tests/unit/commands/test_inventory_unequip_command.py`
- `server/tests/unit/services/test_equipment_service.py`

## Audit Trail

- EXTRACTED: 160 (89%)
- INFERRED: 20 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*