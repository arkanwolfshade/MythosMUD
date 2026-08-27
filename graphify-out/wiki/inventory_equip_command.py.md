# inventory_equip_command.py

> 57 nodes

## Key Concepts

- **inventory_equip_command.py** (46 connections) — `server/commands/inventory_equip_command.py`
- **test_inventory_equip_command.py** (37 connections) — `server/tests/unit/commands/test_inventory_equip_command.py`
- **normalize_slot_name()** (19 connections) — `server/commands/inventory_item_matching.py`
- **handle_equip_command()** (15 connections) — `server/commands/inventory_equip_command.py`
- **_equip_build_work()** (13 connections) — `server/commands/inventory_equip_command.py`
- **_sample_work()** (13 connections) — `server/tests/unit/commands/test_inventory_equip_command.py`
- **_equip_run_mutation()** (12 connections) — `server/commands/inventory_equip_command.py`
- **normalize_equipped_items()** (10 connections) — `server/commands/equipment_helpers.py`
- **normalize_inventory_slots()** (10 connections) — `server/commands/equipment_helpers.py`
- **asyncio** (10 connections)
- **_equip_success_payload()** (9 connections) — `server/commands/inventory_equip_command.py`
- **_equip_target_slot_or_error()** (9 connections) — `server/commands/inventory_equip_command.py`
- **EquipCommandWork** (8 connections) — `server/commands/inventory_equip_command.py`
- **_equip_persist_or_rollback()** (8 connections) — `server/commands/inventory_equip_command.py`
- **_equip_try_inventory_swap()** (7 connections) — `server/commands/inventory_equip_command.py`
- **CommandResponse** (7 connections)
- **EquipCommandInventoryStep** (6 connections) — `server/commands/inventory_equip_command.py`
- **EquipCommandRuntime** (6 connections) — `server/commands/inventory_equip_command.py`
- **_equip_inventory_rollback_snapshot()** (6 connections) — `server/commands/inventory_equip_command.py`
- **test_equip_run_mutation_swap_error()** (6 connections) — `server/tests/unit/commands/test_inventory_equip_command.py`
- **test_equip_run_mutation_suppressed()** (5 connections) — `server/tests/unit/commands/test_inventory_equip_command.py`
- **test_equip_success_payload()** (5 connections) — `server/tests/unit/commands/test_inventory_equip_command.py`
- **test_equip_try_inventory_swap_rejected()** (5 connections) — `server/tests/unit/commands/test_inventory_equip_command.py`
- **test_handle_equip_command_invalid_selected_stack()** (5 connections) — `server/tests/unit/commands/test_inventory_equip_command.py`
- **test_handle_equip_command_mutation_error()** (5 connections) — `server/tests/unit/commands/test_inventory_equip_command.py`
- *... and 32 more nodes in this community*

## Relationships

- [equipment_helpers.py](equipment_helpers.py.md) (17 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (15 shared connections)
- [server/services/__init__.py](server-services-__init__.py.md) (14 shared connections)
- [command_result_text](command_result_text.md) (11 shared connections)
- [AliasStorage](AliasStorage.md) (7 shared connections)
- [Player](Player.md) (7 shared connections)
- [inventory_pickup_command.py](inventory_pickup_command.py.md) (5 shared connections)
- [test_inventory_command_prototype.py](test_inventory_command_prototype.py.md) (5 shared connections)
- [handle_unequip_command](handle_unequip_command.md) (2 shared connections)
- [test_container_helpers_inventory_find.py](test_container_helpers_inventory_find.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [models/player.py](models-player.py.md) (2 shared connections)

## Source Files

- `server/commands/equipment_helpers.py`
- `server/commands/inventory_equip_command.py`
- `server/commands/inventory_item_matching.py`
- `server/tests/unit/commands/test_inventory_commands_helpers.py`
- `server/tests/unit/commands/test_inventory_equip_command.py`
- `server/tests/unit/commands/test_inventory_helpers.py`

## Audit Trail

- EXTRACTED: 214 (96%)
- INFERRED: 8 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*