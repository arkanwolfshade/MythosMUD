# retry nats handler

> 93 nodes

## Key Concepts

- **inventory_unequip_command.py** (33 connections) — `server/commands/inventory_unequip_command.py`
- **InventoryCapacityError** (29 connections) — `server/services/inventory_service.py`
- **SlotValidationError** (27 connections) — `server/services/equipment_service.py`
- **equipment_service.py** (23 connections) — `server/services/equipment_service.py`
- **WearableContainerService** (23 connections) — `server/services/wearable_container_service.py`
- **test_equipment_service.py** (22 connections) — `server/tests/unit/services/test_equipment_service.py`
- **get_shared_services()** (19 connections) — `server/commands/inventory_service_helpers.py`
- **handle_unequip_command()** (18 connections) — `server/commands/inventory_unequip_command.py`
- **EquipmentCapacityError** (17 connections) — `server/services/equipment_service.py`
- **EquipmentService** (17 connections) — `server/services/equipment_service.py`
- **inventory_service_helpers.py** (16 connections) — `server/commands/inventory_service_helpers.py`
- **_unequip_run_mutation()** (12 connections) — `server/commands/inventory_unequip_command.py`
- **test_inventory_unequip_command.py** (12 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- **_equip_try_inventory_swap()** (10 connections) — `server/commands/inventory_equip_command.py`
- **EquipmentServiceError** (10 connections) — `server/services/equipment_service.py`
- **EquipCommandWork** (9 connections) — `server/commands/inventory_equip_command.py`
- **.equip_from_inventory()** (9 connections) — `server/services/equipment_service.py`
- **.unequip_to_inventory()** (8 connections) — `server/services/equipment_service.py`
- **handle_wearable_container_on_unequip()** (7 connections) — `server/commands/equipment_helpers.py`
- **_ensure_shared_services_initialized()** (7 connections) — `server/commands/inventory_service_helpers.py`
- **_unequip_success_payload()** (6 connections) — `server/commands/inventory_unequip_command.py`
- **_clone_inventory()** (6 connections) — `server/services/equipment_service.py`
- **_clone_equipped()** (6 connections) — `server/services/equipment_service.py`
- **test_handle_unequip_command_slot_validation_error()** (6 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- **_unequip_persist_or_rollback()** (5 connections) — `server/commands/inventory_unequip_command.py`
- *... and 68 more nodes in this community*

## Relationships

- [container helpers endpoints](container_helpers_endpoints.md) (39 shared connections)
- [commands inventory command](commands_inventory_command.md) (37 shared connections)
- [inventory commands command](inventory_commands_command.md) (15 shared connections)
- [wearable container service](wearable_container_service.md) (10 shared connections)
- [Exception Containers](Exception_Containers.md) (7 shared connections)
- [container find inventory](container_find_inventory.md) (5 shared connections)
- [models npc rationale](models_npc_rationale.md) (4 shared connections)
- [container inventory display](container_inventory_display.md) (3 shared connections)
- [command inventory factories](command_inventory_factories.md) (3 shared connections)
- [commands inventory pickup](commands_inventory_pickup.md) (3 shared connections)
- [commands npc admin](commands_npc_admin.md) (2 shared connections)
- [world models rationale](world_models_rationale.md) (2 shared connections)

## Source Files

- `server/commands/equipment_helpers.py`
- `server/commands/inventory_equip_command.py`
- `server/commands/inventory_service_helpers.py`
- `server/commands/inventory_unequip_command.py`
- `server/services/equipment_service.py`
- `server/services/inventory_service.py`
- `server/services/wearable_container_service.py`
- `server/tests/unit/commands/test_inventory_equip_command.py`
- `server/tests/unit/commands/test_inventory_unequip_command.py`
- `server/tests/unit/services/test_equipment_service.py`
- `server/tests/unit/services/test_inventory_service.py`

## Audit Trail

- EXTRACTED: 426 (86%)
- INFERRED: 71 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*