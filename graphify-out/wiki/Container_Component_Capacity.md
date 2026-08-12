# Container Component Capacity

> 196 nodes

## Key Concepts

- **__init__.py** (47 connections) — `server/services/__init__.py`
- **inventory_equip_command.py** (45 connections) — `server/commands/inventory_equip_command.py`
- **InventoryService** (43 connections) — `server/services/inventory_service.py`
- **InventoryStack** (34 connections) — `server/services/inventory_service.py`
- **inventory_unequip_command.py** (32 connections) — `server/commands/inventory_unequip_command.py`
- **persist_player()** (30 connections) — `server/commands/inventory_command_helpers.py`
- **inventory_service.py** (29 connections) — `server/services/inventory_service.py`
- **InventoryCapacityError** (29 connections) — `server/services/inventory_service.py`
- **equipment_helpers.py** (28 connections) — `server/commands/equipment_helpers.py`
- **SlotValidationError** (22 connections) — `server/services/equipment_service.py`
- **test_equipment_service.py** (22 connections) — `server/tests/unit/services/test_equipment_service.py`
- **equipment_service.py** (21 connections) — `server/services/equipment_service.py`
- **test_inventory_service.py** (20 connections) — `server/tests/unit/services/test_inventory_service.py`
- **normalize_slot_name()** (19 connections) — `server/commands/inventory_item_matching.py`
- **get_shared_services()** (19 connections) — `server/commands/inventory_service_helpers.py`
- **EquipmentService** (18 connections) — `server/services/equipment_service.py`
- **MutationDecision** (18 connections) — `server/services/inventory_mutation_guard.py`
- **EquipmentCapacityError** (17 connections) — `server/services/equipment_service.py`
- **inventory_service_helpers.py** (16 connections) — `server/commands/inventory_service_helpers.py`
- **handle_unequip_command()** (14 connections) — `server/commands/inventory_unequip_command.py`
- **build_and_broadcast_inventory_event()** (13 connections) — `server/commands/inventory_command_helpers.py`
- **_equip_build_work()** (13 connections) — `server/commands/inventory_equip_command.py`
- **InventoryValidationError** (13 connections) — `server/services/inventory_service.py`
- **InventorySplitError** (13 connections) — `server/services/inventory_service.py`
- **handle_equip_command()** (12 connections) — `server/commands/inventory_equip_command.py`
- *... and 171 more nodes in this community*

## Relationships

- [Async Task Registry](Async_Task_Registry.md) (32 shared connections)
- [Container Sync Remediation](Container_Sync_Remediation.md) (28 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (25 shared connections)
- [Client Lifecycle Metrics](Client_Lifecycle_Metrics.md) (18 shared connections)
- [Client Event Store](Client_Event_Store.md) (13 shared connections)
- [Exploration Command Factories](Exploration_Command_Factories.md) (13 shared connections)
- [Spell Effect Protocols](Spell_Effect_Protocols.md) (9 shared connections)
- [Zone Config Loader](Zone_Config_Loader.md) (6 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (6 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (5 shared connections)
- [Admin NPC Schemas](Admin_NPC_Schemas.md) (5 shared connections)
- [Container Inventory Finders](Container_Inventory_Finders.md) (5 shared connections)

## Source Files

- `server/commands/equipment_helpers.py`
- `server/commands/inventory_command_helpers.py`
- `server/commands/inventory_equip_command.py`
- `server/commands/inventory_item_matching.py`
- `server/commands/inventory_service_helpers.py`
- `server/commands/inventory_unequip_command.py`
- `server/services/__init__.py`
- `server/services/equipment_service.py`
- `server/services/inventory_mutation_guard.py`
- `server/services/inventory_service.py`
- `server/services/passive_lucidity_flux_service.py`
- `server/tests/unit/commands/test_inventory_commands.py`
- `server/tests/unit/services/test_equipment_service.py`
- `server/tests/unit/services/test_inventory_service.py`

## Audit Trail

- EXTRACTED: 935 (87%)
- INFERRED: 135 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*