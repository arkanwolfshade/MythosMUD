# Admin Summon Command

> 318 nodes · cohesion 0.01

## Key Concepts

- **inventory_equip_command.py** (45 connections) — `server/commands/inventory_equip_command.py`
- **inventory_command_helpers.py** (39 connections) — `server/commands/inventory_command_helpers.py`
- **inventory_pickup_command.py** (35 connections) — `server/commands/inventory_pickup_command.py`
- **admin_summon_command.py** (34 connections) — `server/commands/admin_summon_command.py`
- **inventory_unequip_command.py** (32 connections) — `server/commands/inventory_unequip_command.py`
- **RoomDropManager** (29 connections) — `server/commands/inventory_command_contracts.py`
- **inventory_get_command.py** (29 connections) — `server/commands/inventory_get_command.py`
- **equipment_helpers.py** (28 connections) — `server/commands/equipment_helpers.py`
- **persist_player()** (28 connections) — `server/commands/inventory_command_helpers.py`
- **inventory_commands.py** (26 connections) — `server/commands/inventory_commands.py`
- **inventory_drop_command.py** (25 connections) — `server/commands/inventory_drop_command.py`
- **test_inventory_helpers_extended.py** (25 connections) — `server/tests/unit/commands/test_inventory_helpers_extended.py`
- **test_inventory_commands_more_helpers.py** (22 connections) — `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- **inventory_put_command.py** (21 connections) — `server/commands/inventory_put_command.py`
- **inventory_item_matching.py** (20 connections) — `server/commands/inventory_item_matching.py`
- **get_shared_services()** (20 connections) — `server/commands/inventory_service_helpers.py`
- **resolve_state_and_player()** (19 connections) — `server/commands/inventory_command_helpers.py`
- **normalize_slot_name()** (19 connections) — `server/commands/inventory_item_matching.py`
- **broadcast_room_event()** (18 connections) — `server/commands/inventory_command_helpers.py`
- **clone_inventory()** (18 connections) — `server/commands/inventory_command_helpers.py`
- **resolve_player()** (17 connections) — `server/commands/inventory_command_helpers.py`
- **resolve_state()** (17 connections) — `server/commands/inventory_command_helpers.py`
- **handle_drop_command()** (14 connections) — `server/commands/inventory_drop_command.py`
- **FloorPickupAfterExtract** (14 connections) — `server/commands/inventory_pickup_command.py`
- **build_and_broadcast_inventory_event()** (13 connections) — `server/commands/inventory_command_helpers.py`
- *... and 293 more nodes in this community*

## Relationships

- [[Inventory Service Helpers]] (34 shared connections)
- [[NPC Admin API]] (29 shared connections)
- [[Commands Inventory Item]] (28 shared connections)
- [[Alias Expansion Logic]] (25 shared connections)
- [[Inventory Test Support]] (23 shared connections)
- [[Container Inventory Ops]] (10 shared connections)
- [[Player Domain Model]] (9 shared connections)
- [[SQLAlchemy Model Base]] (8 shared connections)
- [[Container Inventory Finders]] (8 shared connections)
- [[Integer Coercion Utils]] (7 shared connections)
- [[Player Save Preparer]] (7 shared connections)
- [[Commands Container Inventory]] (7 shared connections)

## Source Files

- `server/commands/admin_summon_command.py`
- `server/commands/equipment_helpers.py`
- `server/commands/inventory_command_coercion.py`
- `server/commands/inventory_command_contracts.py`
- `server/commands/inventory_command_helpers.py`
- `server/commands/inventory_command_prototype.py`
- `server/commands/inventory_commands.py`
- `server/commands/inventory_drop_command.py`
- `server/commands/inventory_equip_command.py`
- `server/commands/inventory_get_command.py`
- `server/commands/inventory_item_matching.py`
- `server/commands/inventory_pickup_command.py`
- `server/commands/inventory_put_command.py`
- `server/commands/inventory_service_helpers.py`
- `server/commands/inventory_unequip_command.py`
- `server/tests/unit/commands/test_inventory_commands.py`
- `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- `server/tests/unit/commands/test_inventory_commands_persistence_helpers.py`
- `server/tests/unit/commands/test_inventory_commands_state_helpers.py`
- `server/tests/unit/commands/test_inventory_helpers.py`

## Audit Trail

- EXTRACTED: 1478 (93%)
- INFERRED: 114 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
