# task registry app

> 155 nodes

## Key Concepts

- **inventory_equip_command.py** (46 connections) — `server/commands/inventory_equip_command.py`
- **__init__.py** (42 connections) — `server/services/__init__.py`
- **InventoryService** (40 connections) — `server/services/inventory_service.py`
- **InventoryMutationGuard** (39 connections) — `server/services/inventory_mutation_guard.py`
- **InventoryStack** (38 connections) — `server/services/inventory_service.py`
- **inventory_unequip_command.py** (33 connections) — `server/commands/inventory_unequip_command.py`
- **inventory_service.py** (33 connections) — `server/services/inventory_service.py`
- **SlotValidationError** (27 connections) — `server/services/equipment_service.py`
- **InventoryCapacityError** (26 connections) — `server/services/inventory_service.py`
- **equipment_service.py** (23 connections) — `server/services/equipment_service.py`
- **WearableContainerService** (23 connections) — `server/services/wearable_container_service.py`
- **test_equipment_service.py** (22 connections) — `server/tests/unit/services/test_equipment_service.py`
- **wearable_container_service.py** (20 connections) — `server/services/wearable_container_service.py`
- **test_inventory_service.py** (20 connections) — `server/tests/unit/services/test_inventory_service.py`
- **get_shared_services()** (19 connections) — `server/commands/inventory_service_helpers.py`
- **MutationDecision** (19 connections) — `server/services/inventory_mutation_guard.py`
- **EquipmentCapacityError** (17 connections) — `server/services/equipment_service.py`
- **EquipmentService** (17 connections) — `server/services/equipment_service.py`
- **inventory_service_helpers.py** (16 connections) — `server/commands/inventory_service_helpers.py`
- **InventoryValidationError** (13 connections) — `server/services/inventory_service.py`
- **InventorySplitError** (13 connections) — `server/services/inventory_service.py`
- **_unequip_run_mutation()** (12 connections) — `server/commands/inventory_unequip_command.py`
- **_equip_try_inventory_swap()** (10 connections) — `server/commands/inventory_equip_command.py`
- **EquipmentServiceError** (10 connections) — `server/services/equipment_service.py`
- **EquipCommandWork** (9 connections) — `server/commands/inventory_equip_command.py`
- *... and 130 more nodes in this community*

## Relationships

- [player cache rationale](player_cache_rationale.md) (48 shared connections)
- [player effects endpoints](player_effects_endpoints.md) (20 shared connections)
- [container find inventory](container_find_inventory.md) (16 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (15 shared connections)
- [database helpers infrastructure](database_helpers_infrastructure.md) (14 shared connections)
- [room cache services](room_cache_services.md) (13 shared connections)
- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (12 shared connections)
- [models profession rationale](models_profession_rationale.md) (9 shared connections)
- [alias storage commands](alias_storage_commands.md) (7 shared connections)
- [player event handlers](player_event_handlers.md) (7 shared connections)
- [container inventory display](container_inventory_display.md) (6 shared connections)
- [emote game service](emote_game_service.md) (6 shared connections)

## Source Files

- `server/commands/inventory_equip_command.py`
- `server/commands/inventory_service_helpers.py`
- `server/commands/inventory_unequip_command.py`
- `server/services/__init__.py`
- `server/services/equipment_service.py`
- `server/services/inventory_mutation_guard.py`
- `server/services/inventory_service.py`
- `server/services/wearable_container_service.py`
- `server/tests/unit/commands/test_inventory_equip_command.py`
- `server/tests/unit/services/test_equipment_service.py`
- `server/tests/unit/services/test_inventory_mutation_guard_internal.py`
- `server/tests/unit/services/test_inventory_mutation_guard_sync.py`
- `server/tests/unit/services/test_inventory_service.py`

## Audit Trail

- EXTRACTED: 768 (85%)
- INFERRED: 133 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*