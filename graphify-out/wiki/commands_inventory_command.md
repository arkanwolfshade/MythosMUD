# commands inventory command

> 26 nodes

## Key Concepts

- **inventory_equip_command.py** (45 connections) — `server/commands/inventory_equip_command.py`
- **_equip_build_work()** (13 connections) — `server/commands/inventory_equip_command.py`
- **handle_equip_command()** (11 connections) — `server/commands/inventory_equip_command.py`
- **normalize_inventory_slots()** (8 connections) — `server/commands/equipment_helpers.py`
- **_equip_run_mutation()** (8 connections) — `server/commands/inventory_equip_command.py`
- **resolve_equip_item_index()** (7 connections) — `server/commands/equipment_helpers.py`
- **EquipCommandWork** (7 connections) — `server/commands/inventory_equip_command.py`
- **CommandResponse** (7 connections)
- **_equip_try_inventory_swap()** (7 connections) — `server/commands/inventory_equip_command.py`
- **_equip_success_payload()** (7 connections) — `server/commands/inventory_equip_command.py`
- **_equip_persist_or_rollback()** (5 connections) — `server/commands/inventory_equip_command.py`
- **EquipCommandRuntime** (4 connections) — `server/commands/inventory_equip_command.py`
- **EquipCommandInventoryStep** (4 connections) — `server/commands/inventory_equip_command.py`
- **_equip_target_slot_or_error()** (4 connections) — `server/commands/inventory_equip_command.py`
- **_equip_inventory_rollback_snapshot()** (4 connections) — `server/commands/inventory_equip_command.py`
- **.__init__()** (3 connections) — `server/commands/inventory_equip_command.py`
- **Player** (3 connections)
- **test_handle_equip_command()** (3 connections) — `server/tests/unit/commands/test_inventory_commands.py`
- **Resolve item index from command data for equip command.** (1 connections) — `server/commands/equipment_helpers.py`
- **Normalize slot_type in inventory list in-place.** (1 connections) — `server/commands/equipment_helpers.py`
- **Equip command: move an item from inventory to an equipment slot.** (1 connections) — `server/commands/inventory_equip_command.py`
- **Request-scoped services and player for equip.** (1 connections) — `server/commands/inventory_equip_command.py`
- **Inventory indices, slot choice, and rollback snapshot for equip.** (1 connections) — `server/commands/inventory_equip_command.py`
- **Bundled state for equip mutation (keeps handler and Lizard-friendly).** (1 connections) — `server/commands/inventory_equip_command.py`
- **Equip an item from inventory.** (1 connections) — `server/commands/inventory_equip_command.py`
- *... and 1 more nodes in this community*

## Relationships

- [Inventory Equip](Inventory_Equip.md) (13 shared connections)
- [inventory commands command](inventory_commands_command.md) (12 shared connections)
- [argon2 auth rationale](argon2_auth_rationale.md) (9 shared connections)
- [commands inventory helpers](commands_inventory_helpers.md) (8 shared connections)
- [container helpers endpoints](container_helpers_endpoints.md) (5 shared connections)
- [commands alias rationale](commands_alias_rationale.md) (3 shared connections)
- [NATS Messaging](NATS_Messaging.md) (2 shared connections)
- [commands inventory pickup](commands_inventory_pickup.md) (2 shared connections)
- [world models rationale](world_models_rationale.md) (1 shared connections)
- [Async Query Helpers](Async_Query_Helpers.md) (1 shared connections)

## Source Files

- `server/commands/equipment_helpers.py`
- `server/commands/inventory_equip_command.py`
- `server/tests/unit/commands/test_inventory_commands.py`

## Audit Trail

- EXTRACTED: 150 (95%)
- INFERRED: 8 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*