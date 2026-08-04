# container helpers endpoints

> 89 nodes

## Key Concepts

- **InventoryService** (43 connections) — `server/services/inventory_service.py`
- **inventory_unequip_command.py** (33 connections) — `server/commands/inventory_unequip_command.py`
- **SlotValidationError** (27 connections) — `server/services/equipment_service.py`
- **equipment_service.py** (23 connections) — `server/services/equipment_service.py`
- **test_equipment_service.py** (22 connections) — `server/tests/unit/services/test_equipment_service.py`
- **get_shared_services()** (19 connections) — `server/commands/inventory_service_helpers.py`
- **handle_unequip_command()** (18 connections) — `server/commands/inventory_unequip_command.py`
- **EquipmentCapacityError** (17 connections) — `server/services/equipment_service.py`
- **EquipmentService** (17 connections) — `server/services/equipment_service.py`
- **inventory_service_helpers.py** (16 connections) — `server/commands/inventory_service_helpers.py`
- **_unequip_run_mutation()** (12 connections) — `server/commands/inventory_unequip_command.py`
- **test_inventory_unequip_command.py** (12 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- **EquipmentServiceError** (10 connections) — `server/services/equipment_service.py`
- **.equip_from_inventory()** (9 connections) — `server/services/equipment_service.py`
- **.unequip_to_inventory()** (8 connections) — `server/services/equipment_service.py`
- **handle_wearable_container_on_unequip()** (7 connections) — `server/commands/equipment_helpers.py`
- **_ensure_shared_services_initialized()** (7 connections) — `server/commands/inventory_service_helpers.py`
- **_unequip_success_payload()** (6 connections) — `server/commands/inventory_unequip_command.py`
- **_clone_inventory()** (6 connections) — `server/services/equipment_service.py`
- **_clone_equipped()** (6 connections) — `server/services/equipment_service.py`
- **test_inventory_service_helpers.py** (6 connections) — `server/tests/unit/commands/test_inventory_service_helpers.py`
- **test_handle_unequip_command_slot_validation_error()** (6 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- **_unequip_persist_or_rollback()** (5 connections) — `server/commands/inventory_unequip_command.py`
- **_mutation_cm()** (5 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- **_player_with_equipped()** (5 connections) — `server/tests/unit/commands/test_inventory_unequip_command.py`
- *... and 64 more nodes in this community*

## Relationships

- [commands inventory command](commands_inventory_command.md) (40 shared connections)
- [Exception Containers](Exception_Containers.md) (37 shared connections)
- [wearable container service](wearable_container_service.md) (8 shared connections)
- [payload realtime optimizer](payload_realtime_optimizer.md) (8 shared connections)
- [commands inventory pickup](commands_inventory_pickup.md) (5 shared connections)
- [logout command commands](logout_command_commands.md) (4 shared connections)
- [NPC Combat](NPC_Combat.md) (4 shared connections)
- [container inventory display](container_inventory_display.md) (3 shared connections)
- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (3 shared connections)
- [commands npc admin](commands_npc_admin.md) (2 shared connections)
- [combat models rationale](combat_models_rationale.md) (2 shared connections)
- [player cache rationale](player_cache_rationale.md) (2 shared connections)

## Source Files

- `server/commands/equipment_helpers.py`
- `server/commands/inventory_service_helpers.py`
- `server/commands/inventory_unequip_command.py`
- `server/services/equipment_service.py`
- `server/services/inventory_service.py`
- `server/tests/unit/commands/test_inventory_service_helpers.py`
- `server/tests/unit/commands/test_inventory_unequip_command.py`
- `server/tests/unit/services/test_equipment_service.py`

## Audit Trail

- EXTRACTED: 413 (88%)
- INFERRED: 56 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*