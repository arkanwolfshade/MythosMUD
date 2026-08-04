# container helpers endpoints

> 291 nodes

## Key Concepts

- **__init__.py** (47 connections) — `server/services/__init__.py`
- **inventory_equip_command.py** (46 connections) — `server/commands/inventory_equip_command.py`
- **InventoryService** (43 connections) — `server/services/inventory_service.py`
- **InventoryMutationGuard** (42 connections) — `server/services/inventory_mutation_guard.py`
- **test_inventory_equip_command.py** (36 connections) — `server/tests/unit/commands/test_inventory_equip_command.py`
- **InventoryStack** (34 connections) — `server/services/inventory_service.py`
- **inventory_unequip_command.py** (33 connections) — `server/commands/inventory_unequip_command.py`
- **inventory_service.py** (29 connections) — `server/services/inventory_service.py`
- **InventoryCapacityError** (29 connections) — `server/services/inventory_service.py`
- **SlotValidationError** (27 connections) — `server/services/equipment_service.py`
- **equipment_service.py** (23 connections) — `server/services/equipment_service.py`
- **WearableContainerService** (23 connections) — `server/services/wearable_container_service.py`
- **test_equipment_service.py** (22 connections) — `server/tests/unit/services/test_equipment_service.py`
- **inventory_mutation_guard.py** (20 connections) — `server/services/inventory_mutation_guard.py`
- **test_inventory_service.py** (20 connections) — `server/tests/unit/services/test_inventory_service.py`
- **get_shared_services()** (19 connections) — `server/commands/inventory_service_helpers.py`
- **MutationDecision** (19 connections) — `server/services/inventory_mutation_guard.py`
- **EquipmentCapacityError** (17 connections) — `server/services/equipment_service.py`
- **EquipmentService** (17 connections) — `server/services/equipment_service.py`
- **test_inventory_mutation_guard.py** (17 connections) — `server/tests/unit/services/test_inventory_mutation_guard.py`
- **handle_equip_command()** (16 connections) — `server/commands/inventory_equip_command.py`
- **inventory_service_helpers.py** (16 connections) — `server/commands/inventory_service_helpers.py`
- **test_inventory_mutation_guard_internal.py** (15 connections) — `server/tests/unit/services/test_inventory_mutation_guard_internal.py`
- **_equip_build_work()** (13 connections) — `server/commands/inventory_equip_command.py`
- **InventoryValidationError** (13 connections) — `server/services/inventory_service.py`
- *... and 266 more nodes in this community*

## Relationships

- [Exception Containers](Exception_Containers.md) (41 shared connections)
- [inventory commands command](inventory_commands_command.md) (30 shared connections)
- [commands inventory command](commands_inventory_command.md) (28 shared connections)
- [commands inventory pickup](commands_inventory_pickup.md) (27 shared connections)
- [Loot Generation](Loot_Generation.md) (15 shared connections)
- [combat models rationale](combat_models_rationale.md) (11 shared connections)
- [command admin setlucidity](command_admin_setlucidity.md) (7 shared connections)
- [container inventory display](container_inventory_display.md) (6 shared connections)
- [combat services persistence](combat_services_persistence.md) (6 shared connections)
- [container find inventory](container_find_inventory.md) (5 shared connections)
- [commands inventory helpers](commands_inventory_helpers.md) (4 shared connections)
- [task registry app](task_registry_app.md) (4 shared connections)

## Source Files

- `server/commands/equipment_helpers.py`
- `server/commands/inventory_command_contracts.py`
- `server/commands/inventory_equip_command.py`
- `server/commands/inventory_service_helpers.py`
- `server/commands/inventory_unequip_command.py`
- `server/npc/threading.py`
- `server/services/__init__.py`
- `server/services/equipment_service.py`
- `server/services/inventory_mutation_guard.py`
- `server/services/inventory_service.py`
- `server/services/wearable_container_service.py`
- `server/tests/unit/commands/test_inventory_equip_command.py`
- `server/tests/unit/services/test_equipment_service.py`
- `server/tests/unit/services/test_inventory_mutation_guard.py`
- `server/tests/unit/services/test_inventory_mutation_guard_async.py`
- `server/tests/unit/services/test_inventory_mutation_guard_internal.py`
- `server/tests/unit/services/test_inventory_service.py`

## Audit Trail

- EXTRACTED: 1225 (88%)
- INFERRED: 161 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*