# test resolve state no app()

> 128 nodes

## Key Concepts

- **inventory_equip_command.py** (45 connections) — `server/commands/inventory_equip_command.py`
- **inventory_unequip_command.py** (32 connections) — `server/commands/inventory_unequip_command.py`
- **equipment_helpers.py** (28 connections) — `server/commands/equipment_helpers.py`
- **inventory_commands.py** (28 connections) — `server/commands/inventory_commands.py`
- **inventory_item_matching.py** (22 connections) — `server/commands/inventory_item_matching.py`
- **resolve_state_and_player()** (19 connections) — `server/commands/inventory_command_helpers.py`
- **match_room_drop_by_name()** (19 connections) — `server/commands/inventory_item_matching.py`
- **normalize_slot_name()** (19 connections) — `server/commands/inventory_item_matching.py`
- **get_shared_services()** (19 connections) — `server/commands/inventory_service_helpers.py`
- **match_equipped_item_by_name()** (18 connections) — `server/commands/inventory_item_matching.py`
- **EquipmentService** (17 connections) — `server/services/equipment_service.py`
- **match_inventory_item_by_name()** (16 connections) — `server/commands/inventory_item_matching.py`
- **inventory_service_helpers.py** (16 connections) — `server/commands/inventory_service_helpers.py`
- **handle_unequip_command()** (14 connections) — `server/commands/inventory_unequip_command.py`
- **_equip_build_work()** (13 connections) — `server/commands/inventory_equip_command.py`
- **test_inventory_commands_helpers.py** (13 connections) — `server/tests/unit/commands/test_inventory_commands_helpers.py`
- **inventory_command_prototype.py** (12 connections) — `server/commands/inventory_command_prototype.py`
- **handle_equip_command()** (12 connections) — `server/commands/inventory_equip_command.py`
- **_unequip_run_mutation()** (12 connections) — `server/commands/inventory_unequip_command.py`
- **inventory_command_contracts.py** (9 connections) — `server/commands/inventory_command_contracts.py`
- **infer_equip_slot_from_prototype()** (9 connections) — `server/commands/inventory_command_prototype.py`
- **normalize_inventory_slots()** (8 connections) — `server/commands/equipment_helpers.py`
- **normalize_equipped_items()** (8 connections) — `server/commands/equipment_helpers.py`
- **resolve_unequip_slot()** (8 connections) — `server/commands/equipment_helpers.py`
- **_equip_run_mutation()** (8 connections) — `server/commands/inventory_equip_command.py`
- *... and 103 more nodes in this community*

## Relationships

- [Any](Any.md) (36 shared connections)
- [test format metadata empty()](test_format_metadata_empty%28%29.md) (28 shared connections)
- [.validate message()](validate_message%28%29.md) (21 shared connections)
- [Lock](Lock.md) (20 shared connections)
- [handle pickup command()](handle_pickup_command%28%29.md) (10 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (8 shared connections)
- [. init ()](_init_%28%29.md) (6 shared connections)
- [maps](maps.md) (5 shared connections)
- [test magic commands](test_magic_commands.md) (5 shared connections)
- [container helpers inventory find](container_helpers_inventory_find.md) (5 shared connections)
- [DropResolved](DropResolved.md) (3 shared connections)
- [emit close container event()](emit_close_container_event%28%29.md) (3 shared connections)

## Source Files

- `server/commands/equipment_helpers.py`
- `server/commands/inventory_command_contracts.py`
- `server/commands/inventory_command_helpers.py`
- `server/commands/inventory_command_prototype.py`
- `server/commands/inventory_commands.py`
- `server/commands/inventory_equip_command.py`
- `server/commands/inventory_item_matching.py`
- `server/commands/inventory_service_helpers.py`
- `server/commands/inventory_unequip_command.py`
- `server/services/equipment_service.py`
- `server/tests/unit/commands/test_inventory_commands_helpers.py`

## Audit Trail

- EXTRACTED: 662 (97%)
- INFERRED: 21 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*