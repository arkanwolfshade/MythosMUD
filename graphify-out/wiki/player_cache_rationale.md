# player cache rationale

> 214 nodes

## Key Concepts

- **inventory_equip_command.py** (46 connections) — `server/commands/inventory_equip_command.py`
- **test_inventory_equip_command.py** (36 connections) — `server/tests/unit/commands/test_inventory_equip_command.py`
- **equipment_helpers.py** (29 connections) — `server/commands/equipment_helpers.py`
- **SlotValidationError** (27 connections) — `server/services/equipment_service.py`
- **test_equipment_helpers.py** (25 connections) — `server/tests/unit/commands/test_equipment_helpers.py`
- **equipment_service.py** (23 connections) — `server/services/equipment_service.py`
- **WearableContainerService** (23 connections) — `server/services/wearable_container_service.py`
- **inventory_item_matching.py** (22 connections) — `server/commands/inventory_item_matching.py`
- **test_equipment_service.py** (22 connections) — `server/tests/unit/services/test_equipment_service.py`
- **wearable_container_service.py** (20 connections) — `server/services/wearable_container_service.py`
- **match_room_drop_by_name()** (19 connections) — `server/commands/inventory_item_matching.py`
- **normalize_slot_name()** (19 connections) — `server/commands/inventory_item_matching.py`
- **get_shared_services()** (19 connections) — `server/commands/inventory_service_helpers.py`
- **match_equipped_item_by_name()** (18 connections) — `server/commands/inventory_item_matching.py`
- **handle_unequip_command()** (18 connections) — `server/commands/inventory_unequip_command.py`
- **EquipmentCapacityError** (17 connections) — `server/services/equipment_service.py`
- **EquipmentService** (17 connections) — `server/services/equipment_service.py`
- **handle_equip_command()** (16 connections) — `server/commands/inventory_equip_command.py`
- **match_inventory_item_by_name()** (16 connections) — `server/commands/inventory_item_matching.py`
- **inventory_service_helpers.py** (16 connections) — `server/commands/inventory_service_helpers.py`
- **resolve_unequip_slot()** (14 connections) — `server/commands/equipment_helpers.py`
- **resolve_equip_item_index()** (13 connections) — `server/commands/equipment_helpers.py`
- **_equip_build_work()** (13 connections) — `server/commands/inventory_equip_command.py`
- **test_inventory_commands_helpers.py** (13 connections) — `server/tests/unit/commands/test_inventory_commands_helpers.py`
- **_sample_work()** (13 connections) — `server/tests/unit/commands/test_inventory_equip_command.py`
- *... and 189 more nodes in this community*

## Relationships

- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (54 shared connections)
- [task registry app](task_registry_app.md) (37 shared connections)
- [commands inventory command](commands_inventory_command.md) (24 shared connections)
- [Error Conversion](Error_Conversion.md) (15 shared connections)
- [npc combat service](npc_combat_service.md) (10 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (8 shared connections)
- [stats game generator](stats_game_generator.md) (6 shared connections)
- [container find inventory](container_find_inventory.md) (5 shared connections)
- [wearable container service](wearable_container_service.md) (4 shared connections)
- [player room realtime](player_room_realtime.md) (3 shared connections)
- [alias storage rationale](alias_storage_rationale.md) (3 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (3 shared connections)

## Source Files

- `server/commands/equipment_helpers.py`
- `server/commands/inventory_equip_command.py`
- `server/commands/inventory_item_matching.py`
- `server/commands/inventory_service_helpers.py`
- `server/commands/inventory_unequip_command.py`
- `server/services/equipment_service.py`
- `server/services/wearable_container_service.py`
- `server/tests/unit/commands/test_equipment_helpers.py`
- `server/tests/unit/commands/test_inventory_commands.py`
- `server/tests/unit/commands/test_inventory_commands_helpers.py`
- `server/tests/unit/commands/test_inventory_equip_command.py`
- `server/tests/unit/commands/test_inventory_unequip_command.py`
- `server/tests/unit/services/test_equipment_service.py`

## Audit Trail

- EXTRACTED: 1029 (94%)
- INFERRED: 61 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*