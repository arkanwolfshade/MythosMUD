# inventory_equip_command.py

> 94 nodes

## Key Concepts

- **inventory_equip_command.py** (46 connections) — `server/commands/inventory_equip_command.py`
- **test_inventory_equip_command.py** (37 connections) — `server/tests/unit/commands/test_inventory_equip_command.py`
- **equipment_service.py** (23 connections) — `server/services/equipment_service.py`
- **test_equipment_service.py** (23 connections) — `server/tests/unit/services/test_equipment_service.py`
- **SlotValidationError** (21 connections) — `server/services/equipment_service.py`
- **handle_equip_command()** (15 connections) — `server/commands/inventory_equip_command.py`
- **_equip_build_work()** (13 connections) — `server/commands/inventory_equip_command.py`
- **_sample_work()** (13 connections) — `server/tests/unit/commands/test_inventory_equip_command.py`
- **_equip_run_mutation()** (12 connections) — `server/commands/inventory_equip_command.py`
- **EquipmentCapacityError** (11 connections) — `server/services/equipment_service.py`
- **.equip_from_inventory()** (10 connections) — `server/services/equipment_service.py`
- **asyncio** (10 connections)
- **_equip_success_payload()** (9 connections) — `server/commands/inventory_equip_command.py`
- **_equip_target_slot_or_error()** (9 connections) — `server/commands/inventory_equip_command.py`
- **EquipCommandWork** (8 connections) — `server/commands/inventory_equip_command.py`
- **_equip_persist_or_rollback()** (8 connections) — `server/commands/inventory_equip_command.py`
- **.unequip_to_inventory()** (8 connections) — `server/services/equipment_service.py`
- **_equip_try_inventory_swap()** (7 connections) — `server/commands/inventory_equip_command.py`
- **CommandResponse** (7 connections)
- **EquipCommandInventoryStep** (6 connections) — `server/commands/inventory_equip_command.py`
- **EquipCommandRuntime** (6 connections) — `server/commands/inventory_equip_command.py`
- **EquipmentServiceError** (6 connections) — `server/services/equipment_service.py`
- **_equip_inventory_rollback_snapshot()** (6 connections) — `server/commands/inventory_equip_command.py`
- **_clone_equipped()** (6 connections) — `server/services/equipment_service.py`
- **_clone_inventory()** (6 connections) — `server/services/equipment_service.py`
- *... and 69 more nodes in this community*

## Relationships

- [command_result_text](command_result_text.md) (18 shared connections)
- [inventory_unequip_command.py](inventory_unequip_command.py.md) (17 shared connections)
- [test_inventory_helpers.py](test_inventory_helpers.py.md) (15 shared connections)
- [InventoryService](InventoryService.md) (9 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (7 shared connections)
- [Player](Player.md) (7 shared connections)
- [server/services/__init__.py](server-services-__init__.py.md) (4 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [test_inventory_command_prototype.py](test_inventory_command_prototype.py.md) (3 shared connections)
- [AliasStorage](AliasStorage.md) (3 shared connections)
- [sqlalchemy.md](sqlalchemy.md.md) (2 shared connections)

## Source Files

- `server/commands/inventory_equip_command.py`
- `server/services/equipment_service.py`
- `server/tests/unit/commands/test_inventory_equip_command.py`
- `server/tests/unit/services/test_equipment_service.py`

## Audit Trail

- EXTRACTED: 272 (93%)
- INFERRED: 21 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*