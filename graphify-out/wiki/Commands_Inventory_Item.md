# Commands Inventory Item

> 207 nodes · cohesion 0.02

## Key Concepts

- **__init__.py** (47 connections) — `server/services/__init__.py`
- **inventory_equip_command.py** (45 connections) — `server/commands/inventory_equip_command.py`
- **InventoryService** (43 connections) — `server/services/inventory_service.py`
- **inventory_unequip_command.py** (32 connections) — `server/commands/inventory_unequip_command.py`
- **inventory_service.py** (29 connections) — `server/services/inventory_service.py`
- **InventoryCapacityError** (29 connections) — `server/services/inventory_service.py`
- **equipment_helpers.py** (28 connections) — `server/commands/equipment_helpers.py`
- **WearableContainerService** (23 connections) — `server/services/wearable_container_service.py`
- **inventory_item_matching.py** (22 connections) — `server/commands/inventory_item_matching.py`
- **SlotValidationError** (22 connections) — `server/services/equipment_service.py`
- **test_equipment_service.py** (22 connections) — `server/tests/unit/services/test_equipment_service.py`
- **equipment_service.py** (21 connections) — `server/services/equipment_service.py`
- **wearable_container_service.py** (20 connections) — `server/services/wearable_container_service.py`
- **test_inventory_service.py** (20 connections) — `server/tests/unit/services/test_inventory_service.py`
- **match_room_drop_by_name()** (19 connections) — `server/commands/inventory_item_matching.py`
- **normalize_slot_name()** (19 connections) — `server/commands/inventory_item_matching.py`
- **get_shared_services()** (19 connections) — `server/commands/inventory_service_helpers.py`
- **match_equipped_item_by_name()** (18 connections) — `server/commands/inventory_item_matching.py`
- **EquipmentCapacityError** (17 connections) — `server/services/equipment_service.py`
- **EquipmentService** (17 connections) — `server/services/equipment_service.py`
- **match_inventory_item_by_name()** (16 connections) — `server/commands/inventory_item_matching.py`
- **inventory_service_helpers.py** (16 connections) — `server/commands/inventory_service_helpers.py`
- **handle_unequip_command()** (14 connections) — `server/commands/inventory_unequip_command.py`
- **_equip_build_work()** (13 connections) — `server/commands/inventory_equip_command.py`
- **test_inventory_commands_helpers.py** (13 connections) — `server/tests/unit/commands/test_inventory_commands_helpers.py`
- *... and 182 more nodes in this community*

## Relationships

- [Services Inventory Mutation](Services_Inventory_Mutation.md) (48 shared connections)
- [Rest Command Flow](Rest_Command_Flow.md) (27 shared connections)
- [Commands Inventory Display](Commands_Inventory_Display.md) (26 shared connections)
- [Container API Endpoints](Container_API_Endpoints.md) (20 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (16 shared connections)
- [Chat Panel Components](Chat_Panel_Components.md) (16 shared connections)
- [Admin Set Lucidity Command](Admin_Set_Lucidity_Command.md) (12 shared connections)
- [Combat Messaging Integration](Combat_Messaging_Integration.md) (8 shared connections)
- [Event Bus Serialization](Event_Bus_Serialization.md) (6 shared connections)
- [Admin Summon Command](Admin_Summon_Command.md) (6 shared connections)
- [Container Inventory Finders](Container_Inventory_Finders.md) (5 shared connections)
- [Container Component Capacity](Container_Component_Capacity.md) (5 shared connections)

## Source Files

- `server/commands/equipment_helpers.py`
- `server/commands/inventory_command_prototype.py`
- `server/commands/inventory_equip_command.py`
- `server/commands/inventory_item_matching.py`
- `server/commands/inventory_service_helpers.py`
- `server/commands/inventory_unequip_command.py`
- `server/services/__init__.py`
- `server/services/equipment_service.py`
- `server/services/inventory_service.py`
- `server/services/wearable_container_service.py`
- `server/tests/unit/commands/test_inventory_commands_helpers.py`
- `server/tests/unit/services/test_equipment_service.py`
- `server/tests/unit/services/test_inventory_service.py`

## Audit Trail

- EXTRACTED: 985 (92%)
- INFERRED: 90 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*