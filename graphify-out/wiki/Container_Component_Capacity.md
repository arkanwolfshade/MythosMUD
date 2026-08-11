# Container Component Capacity

> 112 nodes

## Key Concepts

- **__init__.py** (47 connections) — `server/services/__init__.py`
- **inventory_equip_command.py** (45 connections) — `server/commands/inventory_equip_command.py`
- **InventoryService** (43 connections) — `server/services/inventory_service.py`
- **InventoryStack** (34 connections) — `server/services/inventory_service.py`
- **InventoryCapacityError** (29 connections) — `server/services/inventory_service.py`
- **SlotValidationError** (22 connections) — `server/services/equipment_service.py`
- **test_equipment_service.py** (22 connections) — `server/tests/unit/services/test_equipment_service.py`
- **equipment_service.py** (21 connections) — `server/services/equipment_service.py`
- **test_inventory_service.py** (20 connections) — `server/tests/unit/services/test_inventory_service.py`
- **get_shared_services()** (19 connections) — `server/commands/inventory_service_helpers.py`
- **EquipmentService** (18 connections) — `server/services/equipment_service.py`
- **EquipmentCapacityError** (17 connections) — `server/services/equipment_service.py`
- **inventory_service_helpers.py** (16 connections) — `server/commands/inventory_service_helpers.py`
- **InventoryValidationError** (13 connections) — `server/services/inventory_service.py`
- **EquipmentServiceError** (10 connections) — `server/services/equipment_service.py`
- **.equip_from_inventory()** (10 connections) — `server/services/equipment_service.py`
- **._clone_stack()** (9 connections) — `server/services/inventory_service.py`
- **.unequip_to_inventory()** (8 connections) — `server/services/equipment_service.py`
- **.add_stack()** (8 connections) — `server/services/inventory_service.py`
- **.split_stack()** (8 connections) — `server/services/inventory_service.py`
- **_equip_try_inventory_swap()** (7 connections) — `server/commands/inventory_equip_command.py`
- **_ensure_shared_services_initialized()** (7 connections) — `server/commands/inventory_service_helpers.py`
- **Any** (7 connections)
- **._validate_and_clone_optional_fields()** (7 connections) — `server/services/inventory_service.py`
- **._clone_with_quantity()** (7 connections) — `server/services/inventory_service.py`
- *... and 87 more nodes in this community*

## Relationships

- [WebSocket Auth Integration](WebSocket_Auth_Integration.md) (39 shared connections)
- [Client Lifecycle Metrics](Client_Lifecycle_Metrics.md) (35 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (24 shared connections)
- [Exploration Command Factories](Exploration_Command_Factories.md) (13 shared connections)
- [Spell Effect Protocols](Spell_Effect_Protocols.md) (12 shared connections)
- [Async Task Registry](Async_Task_Registry.md) (9 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (9 shared connections)
- [Container Open Events](Container_Open_Events.md) (5 shared connections)
- [Container Inventory Finders](Container_Inventory_Finders.md) (5 shared connections)
- [Player Effects API](Player_Effects_API.md) (4 shared connections)
- [Enhanced Logging Exceptions](Enhanced_Logging_Exceptions.md) (3 shared connections)
- [Client Event Store](Client_Event_Store.md) (3 shared connections)

## Source Files

- `server/commands/inventory_equip_command.py`
- `server/commands/inventory_service_helpers.py`
- `server/services/__init__.py`
- `server/services/equipment_service.py`
- `server/services/inventory_service.py`
- `server/services/passive_lucidity_flux_service.py`
- `server/tests/unit/services/test_equipment_service.py`
- `server/tests/unit/services/test_inventory_service.py`

## Audit Trail

- EXTRACTED: 517 (84%)
- INFERRED: 97 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*