# Inventory Equip

> 80 nodes

## Key Concepts

- **inventory_unequip_command.py** (32 connections) — `server/commands/inventory_unequip_command.py`
- **WearableContainerService** (23 connections) — `server/services/wearable_container_service.py`
- **SlotValidationError** (22 connections) — `server/services/equipment_service.py`
- **test_equipment_service.py** (22 connections) — `server/tests/unit/services/test_equipment_service.py`
- **equipment_service.py** (21 connections) — `server/services/equipment_service.py`
- **wearable_container_service.py** (20 connections) — `server/services/wearable_container_service.py`
- **get_shared_services()** (19 connections) — `server/commands/inventory_service_helpers.py`
- **EquipmentCapacityError** (17 connections) — `server/services/equipment_service.py`
- **EquipmentService** (17 connections) — `server/services/equipment_service.py`
- **inventory_service_helpers.py** (16 connections) — `server/commands/inventory_service_helpers.py`
- **handle_unequip_command()** (13 connections) — `server/commands/inventory_unequip_command.py`
- **_unequip_run_mutation()** (12 connections) — `server/commands/inventory_unequip_command.py`
- **EquipmentServiceError** (10 connections) — `server/services/equipment_service.py`
- **.equip_from_inventory()** (9 connections) — `server/services/equipment_service.py`
- **normalize_equipped_items()** (8 connections) — `server/commands/equipment_helpers.py`
- **.unequip_to_inventory()** (8 connections) — `server/services/equipment_service.py`
- **handle_wearable_container_on_unequip()** (7 connections) — `server/commands/equipment_helpers.py`
- **_ensure_shared_services_initialized()** (7 connections) — `server/commands/inventory_service_helpers.py`
- **_unequip_success_payload()** (6 connections) — `server/commands/inventory_unequip_command.py`
- **_clone_inventory()** (6 connections) — `server/services/equipment_service.py`
- **_clone_equipped()** (6 connections) — `server/services/equipment_service.py`
- **_unequip_persist_or_rollback()** (5 connections) — `server/commands/inventory_unequip_command.py`
- **CommandResponse** (4 connections)
- **Any** (4 connections)
- **InventoryStack** (4 connections)
- *... and 55 more nodes in this community*

## Relationships

- [container helpers endpoints](container_helpers_endpoints.md) (37 shared connections)
- [commands inventory command](commands_inventory_command.md) (13 shared connections)
- [inventory commands command](inventory_commands_command.md) (13 shared connections)
- [argon2 auth rationale](argon2_auth_rationale.md) (10 shared connections)
- [message queue realtime](message_queue_realtime.md) (10 shared connections)
- [NATS Messaging](NATS_Messaging.md) (6 shared connections)
- [wearable container service](wearable_container_service.md) (5 shared connections)
- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (4 shared connections)
- [container inventory display](container_inventory_display.md) (3 shared connections)
- [commands alias rationale](commands_alias_rationale.md) (3 shared connections)
- [look helpers commands](look_helpers_commands.md) (3 shared connections)
- [Loot Generation](Loot_Generation.md) (3 shared connections)

## Source Files

- `server/commands/equipment_helpers.py`
- `server/commands/inventory_service_helpers.py`
- `server/commands/inventory_unequip_command.py`
- `server/services/equipment_service.py`
- `server/services/wearable_container_service.py`
- `server/tests/unit/commands/test_inventory_commands.py`
- `server/tests/unit/services/test_equipment_service.py`

## Audit Trail

- EXTRACTED: 357 (88%)
- INFERRED: 49 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*