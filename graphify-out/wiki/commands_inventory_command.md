# commands inventory command

> 203 nodes

## Key Concepts

- **inventory_equip_command.py** (45 connections) — `server/commands/inventory_equip_command.py`
- **InventoryService** (43 connections) — `server/services/inventory_service.py`
- **inventory_unequip_command.py** (32 connections) — `server/commands/inventory_unequip_command.py`
- **equipment_helpers.py** (28 connections) — `server/commands/equipment_helpers.py`
- **inventory_commands.py** (28 connections) — `server/commands/inventory_commands.py`
- **inventory_drop_command.py** (25 connections) — `server/commands/inventory_drop_command.py`
- **WearableContainerService** (23 connections) — `server/services/wearable_container_service.py`
- **inventory_item_matching.py** (22 connections) — `server/commands/inventory_item_matching.py`
- **SlotValidationError** (22 connections) — `server/services/equipment_service.py`
- **test_equipment_service.py** (22 connections) — `server/tests/unit/services/test_equipment_service.py`
- **equipment_service.py** (21 connections) — `server/services/equipment_service.py`
- **resolve_state_and_player()** (19 connections) — `server/commands/inventory_command_helpers.py`
- **match_room_drop_by_name()** (19 connections) — `server/commands/inventory_item_matching.py`
- **normalize_slot_name()** (19 connections) — `server/commands/inventory_item_matching.py`
- **get_shared_services()** (19 connections) — `server/commands/inventory_service_helpers.py`
- **match_equipped_item_by_name()** (18 connections) — `server/commands/inventory_item_matching.py`
- **EquipmentCapacityError** (17 connections) — `server/services/equipment_service.py`
- **EquipmentService** (17 connections) — `server/services/equipment_service.py`
- **match_inventory_item_by_name()** (16 connections) — `server/commands/inventory_item_matching.py`
- **inventory_service_helpers.py** (16 connections) — `server/commands/inventory_service_helpers.py`
- **handle_drop_command()** (14 connections) — `server/commands/inventory_drop_command.py`
- **build_and_broadcast_inventory_event()** (13 connections) — `server/commands/inventory_command_helpers.py`
- **_equip_build_work()** (13 connections) — `server/commands/inventory_equip_command.py`
- **handle_unequip_command()** (13 connections) — `server/commands/inventory_unequip_command.py`
- **test_inventory_commands_helpers.py** (13 connections) — `server/tests/unit/commands/test_inventory_commands_helpers.py`
- *... and 178 more nodes in this community*

## Relationships

- [container helpers endpoints](container_helpers_endpoints.md) (45 shared connections)
- [inventory commands command](inventory_commands_command.md) (31 shared connections)
- [commands inventory helpers](commands_inventory_helpers.md) (28 shared connections)
- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (18 shared connections)
- [commands inventory pickup](commands_inventory_pickup.md) (16 shared connections)
- [commands admin mute](commands_admin_mute.md) (13 shared connections)
- [command inventory factories](command_inventory_factories.md) (12 shared connections)
- [schedule services service](schedule_services_service.md) (7 shared connections)
- [Exception Containers](Exception_Containers.md) (6 shared connections)
- [persistence rationale player](persistence_rationale_player.md) (5 shared connections)
- [container find inventory](container_find_inventory.md) (5 shared connections)
- [world models rationale](world_models_rationale.md) (4 shared connections)

## Source Files

- `server/commands/equipment_helpers.py`
- `server/commands/inventory_command_contracts.py`
- `server/commands/inventory_command_helpers.py`
- `server/commands/inventory_command_prototype.py`
- `server/commands/inventory_commands.py`
- `server/commands/inventory_drop_command.py`
- `server/commands/inventory_equip_command.py`
- `server/commands/inventory_item_matching.py`
- `server/commands/inventory_service_helpers.py`
- `server/commands/inventory_unequip_command.py`
- `server/services/equipment_service.py`
- `server/services/inventory_service.py`
- `server/services/wearable_container_service.py`
- `server/tests/unit/commands/test_inventory_commands_helpers.py`
- `server/tests/unit/services/test_equipment_service.py`

## Audit Trail

- EXTRACTED: 979 (93%)
- INFERRED: 77 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*