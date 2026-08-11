# Character Creation Service

> 108 nodes

## Key Concepts

- **inventory_command_helpers.py** (48 connections) — `server/commands/inventory_command_helpers.py`
- **inventory_equip_command.py** (45 connections) — `server/commands/inventory_equip_command.py`
- **inventory_unequip_command.py** (32 connections) — `server/commands/inventory_unequip_command.py`
- **persist_player()** (30 connections) — `server/commands/inventory_command_helpers.py`
- **equipment_helpers.py** (28 connections) — `server/commands/equipment_helpers.py`
- **test_inventory_commands_more_helpers.py** (23 connections) — `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- **inventory_item_matching.py** (22 connections) — `server/commands/inventory_item_matching.py`
- **normalize_slot_name()** (19 connections) — `server/commands/inventory_item_matching.py`
- **get_shared_services()** (19 connections) — `server/commands/inventory_service_helpers.py`
- **clone_inventory()** (18 connections) — `server/commands/inventory_command_helpers.py`
- **inventory_service_helpers.py** (16 connections) — `server/commands/inventory_service_helpers.py`
- **handle_unequip_command()** (14 connections) — `server/commands/inventory_unequip_command.py`
- **build_and_broadcast_inventory_event()** (13 connections) — `server/commands/inventory_command_helpers.py`
- **_equip_build_work()** (13 connections) — `server/commands/inventory_equip_command.py`
- **handle_equip_command()** (12 connections) — `server/commands/inventory_equip_command.py`
- **_unequip_run_mutation()** (12 connections) — `server/commands/inventory_unequip_command.py`
- **Player** (11 connections)
- **add_pickup_to_inventory()** (10 connections) — `server/commands/inventory_command_helpers.py`
- **normalize_inventory_slots()** (8 connections) — `server/commands/equipment_helpers.py`
- **normalize_equipped_items()** (8 connections) — `server/commands/equipment_helpers.py`
- **resolve_unequip_slot()** (8 connections) — `server/commands/equipment_helpers.py`
- **_equip_run_mutation()** (8 connections) — `server/commands/inventory_equip_command.py`
- **resolve_equip_item_index()** (7 connections) — `server/commands/equipment_helpers.py`
- **handle_wearable_container_on_equip()** (7 connections) — `server/commands/equipment_helpers.py`
- **handle_wearable_container_on_unequip()** (7 connections) — `server/commands/equipment_helpers.py`
- *... and 83 more nodes in this community*

## Relationships

- [Container Component Capacity](Container_Component_Capacity.md) (40 shared connections)
- [Async Task Registry](Async_Task_Registry.md) (30 shared connections)
- [Spell Effect Protocols](Spell_Effect_Protocols.md) (29 shared connections)
- [Container Sync Remediation](Container_Sync_Remediation.md) (27 shared connections)
- [FastAPI Auth Integration](FastAPI_Auth_Integration.md) (17 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (13 shared connections)
- [Client Event Store](Client_Event_Store.md) (10 shared connections)
- [Services Inventory Mutation](Services_Inventory_Mutation.md) (6 shared connections)
- [NPC Definition CRUD](NPC_Definition_CRUD.md) (5 shared connections)
- [Container Inventory Finders](Container_Inventory_Finders.md) (5 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (4 shared connections)
- [Admin NPC Schemas](Admin_NPC_Schemas.md) (4 shared connections)

## Source Files

- `server/commands/equipment_helpers.py`
- `server/commands/inventory_command_helpers.py`
- `server/commands/inventory_equip_command.py`
- `server/commands/inventory_item_matching.py`
- `server/commands/inventory_service_helpers.py`
- `server/commands/inventory_unequip_command.py`
- `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- `server/tests/unit/commands/test_inventory_commands_persistence_helpers.py`

## Audit Trail

- EXTRACTED: 632 (97%)
- INFERRED: 21 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*