# inventory_equip_command.py

> 70 nodes

## Key Concepts

- **inventory_equip_command.py** (45 connections) — `server/commands/inventory_equip_command.py`
- **inventory_unequip_command.py** (32 connections) — `server/commands/inventory_unequip_command.py`
- **equipment_helpers.py** (28 connections) — `server/commands/equipment_helpers.py`
- **get_shared_services()** (21 connections) — `server/commands/inventory_service_helpers.py`
- **resolve_state_and_player()** (19 connections) — `server/commands/inventory_command_helpers.py`
- **inventory_service_helpers.py** (16 connections) — `server/commands/inventory_service_helpers.py`
- **handle_unequip_command()** (14 connections) — `server/commands/inventory_unequip_command.py`
- **_equip_build_work()** (13 connections) — `server/commands/inventory_equip_command.py`
- **handle_equip_command()** (11 connections) — `server/commands/inventory_equip_command.py`
- **_unequip_run_mutation()** (9 connections) — `server/commands/inventory_unequip_command.py`
- **normalize_equipped_items()** (8 connections) — `server/commands/equipment_helpers.py`
- **normalize_inventory_slots()** (8 connections) — `server/commands/equipment_helpers.py`
- **resolve_unequip_slot()** (8 connections) — `server/commands/equipment_helpers.py`
- **_equip_run_mutation()** (8 connections) — `server/commands/inventory_equip_command.py`
- **handle_wearable_container_on_equip()** (7 connections) — `server/commands/equipment_helpers.py`
- **handle_wearable_container_on_unequip()** (7 connections) — `server/commands/equipment_helpers.py`
- **resolve_equip_item_index()** (7 connections) — `server/commands/equipment_helpers.py`
- **_equip_success_payload()** (7 connections) — `server/commands/inventory_equip_command.py`
- **_ensure_shared_services_initialized()** (7 connections) — `server/commands/inventory_service_helpers.py`
- **CommandResponse** (7 connections)
- **EquipCommandWork** (6 connections) — `server/commands/inventory_equip_command.py`
- **find_equipped_item_after_equip()** (6 connections) — `server/commands/equipment_helpers.py`
- **_unequip_success_payload()** (6 connections) — `server/commands/inventory_unequip_command.py`
- **test_inventory_service_helpers.py** (6 connections) — `server/tests/unit/commands/test_inventory_service_helpers.py`
- **_equip_persist_or_rollback()** (5 connections) — `server/commands/inventory_equip_command.py`
- *... and 45 more nodes in this community*

## Relationships

- [server/services/__init__.py](server-services-__init__.py.md) (27 shared connections)
- [test_inventory_helpers.py](test_inventory_helpers.py.md) (17 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (15 shared connections)
- [AliasStorage](AliasStorage.md) (14 shared connections)
- [inventory_pickup_command.py](inventory_pickup_command.py.md) (11 shared connections)
- [Player](Player.md) (6 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [test_inventory_commands.py](test_inventory_commands.py.md) (5 shared connections)
- [test_container_helpers_inventory_find.py](test_container_helpers_inventory_find.py.md) (5 shared connections)
- [test_wearable_container_service.py](test_wearable_container_service.py.md) (4 shared connections)
- [container_helpers_inventory_display.py](container_helpers_inventory_display.py.md) (3 shared connections)
- [inventory_put_command.py](inventory_put_command.py.md) (2 shared connections)

## Source Files

- `server/commands/equipment_helpers.py`
- `server/commands/inventory_command_helpers.py`
- `server/commands/inventory_equip_command.py`
- `server/commands/inventory_service_helpers.py`
- `server/commands/inventory_unequip_command.py`
- `server/tests/unit/commands/test_inventory_service_helpers.py`

## Audit Trail

- EXTRACTED: 255 (97%)
- INFERRED: 7 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*