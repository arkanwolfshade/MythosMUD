# inventory_equip_command.py

> 51 nodes

## Key Concepts

- **inventory_equip_command.py** (45 connections) — `server/commands/inventory_equip_command.py`
- **handle_unequip_command()** (14 connections) — `server/commands/inventory_unequip_command.py`
- **_equip_build_work()** (13 connections) — `server/commands/inventory_equip_command.py`
- **inventory_command_prototype.py** (12 connections) — `server/commands/inventory_command_prototype.py`
- **handle_equip_command()** (11 connections) — `server/commands/inventory_equip_command.py`
- **infer_equip_slot_from_prototype()** (9 connections) — `server/commands/inventory_command_prototype.py`
- **_unequip_run_mutation()** (9 connections) — `server/commands/inventory_unequip_command.py`
- **normalize_equipped_items()** (8 connections) — `server/commands/equipment_helpers.py`
- **normalize_inventory_slots()** (8 connections) — `server/commands/equipment_helpers.py`
- **_equip_run_mutation()** (8 connections) — `server/commands/inventory_equip_command.py`
- **handle_wearable_container_on_equip()** (7 connections) — `server/commands/equipment_helpers.py`
- **handle_wearable_container_on_unequip()** (7 connections) — `server/commands/equipment_helpers.py`
- **_equip_success_payload()** (7 connections) — `server/commands/inventory_equip_command.py`
- **CommandResponse** (7 connections)
- **EquipCommandWork** (6 connections) — `server/commands/inventory_equip_command.py`
- **find_equipped_item_after_equip()** (6 connections) — `server/commands/equipment_helpers.py`
- **_unequip_success_payload()** (6 connections) — `server/commands/inventory_unequip_command.py`
- **_equip_persist_or_rollback()** (5 connections) — `server/commands/inventory_equip_command.py`
- **_unequip_persist_or_rollback()** (5 connections) — `server/commands/inventory_unequip_command.py`
- **EquipCommandInventoryStep** (4 connections) — `server/commands/inventory_equip_command.py`
- **EquipCommandRuntime** (4 connections) — `server/commands/inventory_equip_command.py`
- **prototype_from_registry()** (4 connections) — `server/commands/inventory_command_prototype.py`
- **prototype_registry_from_request()** (4 connections) — `server/commands/inventory_command_prototype.py`
- **_equip_inventory_rollback_snapshot()** (4 connections) — `server/commands/inventory_equip_command.py`
- **_equip_target_slot_or_error()** (4 connections) — `server/commands/inventory_equip_command.py`
- *... and 26 more nodes in this community*

## Relationships

- [server/services/__init__.py](server-services-__init__.py.md) (23 shared connections)
- [test_inventory_helpers.py](test_inventory_helpers.py.md) (19 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (18 shared connections)
- [AliasStorage](AliasStorage.md) (6 shared connections)
- [test_inventory_commands.py](test_inventory_commands.py.md) (4 shared connections)
- [prototype_registry.py](prototype_registry.py.md) (3 shared connections)
- [log_and_raise](log_and_raise.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [.state](state.md) (1 shared connections)

## Source Files

- `server/commands/equipment_helpers.py`
- `server/commands/inventory_command_prototype.py`
- `server/commands/inventory_equip_command.py`
- `server/commands/inventory_unequip_command.py`

## Audit Trail

- EXTRACTED: 164 (95%)
- INFERRED: 8 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*