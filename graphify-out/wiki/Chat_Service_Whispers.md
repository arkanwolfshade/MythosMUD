# Chat Service Whispers

> 86 nodes

## Key Concepts

- **InventoryService** (43 connections) — `server/services/inventory_service.py`
- **InventoryStack** (34 connections) — `server/services/inventory_service.py`
- **inventory_service.py** (29 connections) — `server/services/inventory_service.py`
- **test_inventory_service.py** (20 connections) — `server/tests/unit/services/test_inventory_service.py`
- **EquipmentService** (18 connections) — `server/services/equipment_service.py`
- **MutationDecision** (18 connections) — `server/services/inventory_mutation_guard.py`
- **inventory_service_helpers.py** (16 connections) — `server/commands/inventory_service_helpers.py`
- **InventoryValidationError** (13 connections) — `server/services/inventory_service.py`
- **InventorySplitError** (13 connections) — `server/services/inventory_service.py`
- **.equip_from_inventory()** (10 connections) — `server/services/equipment_service.py`
- **InventoryServiceError** (9 connections) — `server/services/inventory_service.py`
- **._clone_stack()** (9 connections) — `server/services/inventory_service.py`
- **.unequip_to_inventory()** (8 connections) — `server/services/equipment_service.py`
- **.add_stack()** (8 connections) — `server/services/inventory_service.py`
- **.split_stack()** (8 connections) — `server/services/inventory_service.py`
- **_ensure_shared_services_initialized()** (7 connections) — `server/commands/inventory_service_helpers.py`
- **Any** (7 connections)
- **._validate_and_clone_optional_fields()** (7 connections) — `server/services/inventory_service.py`
- **._clone_with_quantity()** (7 connections) — `server/services/inventory_service.py`
- **_clone_inventory()** (6 connections) — `server/services/equipment_service.py`
- **_clone_equipped()** (6 connections) — `server/services/equipment_service.py`
- **InventoryStackRequired** (6 connections) — `server/services/inventory_service.py`
- **InnerContainer** (6 connections) — `server/services/inventory_service.py`
- **InventoryStack** (5 connections)
- **.begin_mutation()** (5 connections) — `server/services/inventory_service.py`
- *... and 61 more nodes in this community*

## Relationships

- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (35 shared connections)
- [Game Client Container](Game_Client_Container.md) (23 shared connections)
- [Character Creation Service](Character_Creation_Service.md) (15 shared connections)
- [Magic Command Handlers](Magic_Command_Handlers.md) (12 shared connections)
- [Whisper Remediation Plan](Whisper_Remediation_Plan.md) (8 shared connections)
- [Async Task Registry](Async_Task_Registry.md) (7 shared connections)
- [Admin NPC Schemas](Admin_NPC_Schemas.md) (4 shared connections)
- [NATS Subject Patterns](NATS_Subject_Patterns.md) (3 shared connections)
- [Combat Persistence Events](Combat_Persistence_Events.md) (3 shared connections)
- [Combat Player Broadcasts](Combat_Player_Broadcasts.md) (2 shared connections)
- [Container Inventory Finders](Container_Inventory_Finders.md) (1 shared connections)
- [Application Container Analysis](Application_Container_Analysis.md) (1 shared connections)

## Source Files

- `server/commands/inventory_service_helpers.py`
- `server/services/equipment_service.py`
- `server/services/inventory_mutation_guard.py`
- `server/services/inventory_service.py`
- `server/tests/unit/services/test_equipment_service.py`
- `server/tests/unit/services/test_inventory_service.py`

## Audit Trail

- EXTRACTED: 351 (83%)
- INFERRED: 70 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*