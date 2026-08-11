# WebSocket Auth Integration

> 50 nodes

## Key Concepts

- **inventory_unequip_command.py** (32 connections) — `server/commands/inventory_unequip_command.py`
- **equipment_helpers.py** (28 connections) — `server/commands/equipment_helpers.py`
- **handle_unequip_command()** (14 connections) — `server/commands/inventory_unequip_command.py`
- **_equip_build_work()** (13 connections) — `server/commands/inventory_equip_command.py`
- **handle_equip_command()** (12 connections) — `server/commands/inventory_equip_command.py`
- **_unequip_run_mutation()** (12 connections) — `server/commands/inventory_unequip_command.py`
- **normalize_inventory_slots()** (8 connections) — `server/commands/equipment_helpers.py`
- **normalize_equipped_items()** (8 connections) — `server/commands/equipment_helpers.py`
- **resolve_unequip_slot()** (8 connections) — `server/commands/equipment_helpers.py`
- **_equip_run_mutation()** (8 connections) — `server/commands/inventory_equip_command.py`
- **resolve_equip_item_index()** (7 connections) — `server/commands/equipment_helpers.py`
- **handle_wearable_container_on_equip()** (7 connections) — `server/commands/equipment_helpers.py`
- **handle_wearable_container_on_unequip()** (7 connections) — `server/commands/equipment_helpers.py`
- **EquipCommandWork** (7 connections) — `server/commands/inventory_equip_command.py`
- **CommandResponse** (7 connections)
- **_equip_success_payload()** (7 connections) — `server/commands/inventory_equip_command.py`
- **find_equipped_item_after_equip()** (6 connections) — `server/commands/equipment_helpers.py`
- **_unequip_success_payload()** (6 connections) — `server/commands/inventory_unequip_command.py`
- **_equip_persist_or_rollback()** (5 connections) — `server/commands/inventory_equip_command.py`
- **_unequip_persist_or_rollback()** (5 connections) — `server/commands/inventory_unequip_command.py`
- **_equip_stack_from_inventory_index()** (4 connections) — `server/commands/equipment_helpers.py`
- **InventoryStack** (4 connections)
- **EquipCommandRuntime** (4 connections) — `server/commands/inventory_equip_command.py`
- **EquipCommandInventoryStep** (4 connections) — `server/commands/inventory_equip_command.py`
- **_equip_target_slot_or_error()** (4 connections) — `server/commands/inventory_equip_command.py`
- *... and 25 more nodes in this community*

## Relationships

- [Container Component Capacity](Container_Component_Capacity.md) (39 shared connections)
- [Spell Effect Protocols](Spell_Effect_Protocols.md) (16 shared connections)
- [Async Task Registry](Async_Task_Registry.md) (12 shared connections)
- [Container Open Events](Container_Open_Events.md) (6 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (4 shared connections)
- [Admin NPC Schemas](Admin_NPC_Schemas.md) (4 shared connections)
- [Rate Limiter Utilities](Rate_Limiter_Utilities.md) (3 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (2 shared connections)
- [Zone Config Loader](Zone_Config_Loader.md) (2 shared connections)
- [Client Lifecycle Metrics](Client_Lifecycle_Metrics.md) (2 shared connections)

## Source Files

- `server/commands/equipment_helpers.py`
- `server/commands/inventory_equip_command.py`
- `server/commands/inventory_unequip_command.py`

## Audit Trail

- EXTRACTED: 261 (96%)
- INFERRED: 11 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*