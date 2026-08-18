# dropresolved

> 148 nodes

## Key Concepts

- **inventory_command_helpers.py** (50 connections) — `server/commands/inventory_command_helpers.py`
- **inventory_pickup_command.py** (35 connections) — `server/commands/inventory_pickup_command.py`
- **inventory_unequip_command.py** (33 connections) — `server/commands/inventory_unequip_command.py`
- **persist_player()** (30 connections) — `server/commands/inventory_command_helpers.py`
- **inventory_commands.py** (28 connections) — `server/commands/inventory_commands.py`
- **inventory_drop_command.py** (25 connections) — `server/commands/inventory_drop_command.py`
- **test_inventory_commands_more_helpers.py** (24 connections) — `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- **resolve_state()** (19 connections) — `server/commands/inventory_command_helpers.py`
- **resolve_state_and_player()** (19 connections) — `server/commands/inventory_command_helpers.py`
- **clone_inventory()** (18 connections) — `server/commands/inventory_command_helpers.py`
- **handle_unequip_command()** (18 connections) — `server/commands/inventory_unequip_command.py`
- **handle_pickup_command()** (17 connections) — `server/commands/inventory_pickup_command.py`
- **RoomDropManager** (16 connections) — `server/commands/inventory_command_contracts.py`
- **handle_drop_command()** (14 connections) — `server/commands/inventory_drop_command.py`
- **build_and_broadcast_inventory_event()** (13 connections) — `server/commands/inventory_command_helpers.py`
- **_pickup_commit_inventory_after_floor_extract()** (13 connections) — `server/commands/inventory_pickup_command.py`
- **test_inventory_commands_persistence_helpers.py** (13 connections) — `server/tests/unit/commands/test_inventory_commands_persistence_helpers.py`
- **_drop_resolve_stack_or_error()** (12 connections) — `server/commands/inventory_drop_command.py`
- **inventory_command_contracts.py** (11 connections) — `server/commands/inventory_command_contracts.py`
- **Player** (11 connections)
- **asyncio** (11 connections)
- **complete_pickup_after_floor_extract()** (9 connections) — `server/commands/inventory_pickup_command.py`
- **_pickup_resolve_floor_stack_or_error()** (9 connections) — `server/commands/inventory_pickup_command.py`
- **_unequip_run_mutation()** (9 connections) — `server/commands/inventory_unequip_command.py`
- **FloorPickupAfterExtract** (8 connections) — `server/commands/inventory_pickup_command.py`
- *... and 123 more nodes in this community*

## Relationships

- [server commands inventory command helpers](server_commands_inventory_command_helpers.md) (49 shared connections)
- [server commands inventory get command](server_commands_inventory_get_command.md) (20 shared connections)
- [abstractcontextmanager](abstractcontextmanager.md) (17 shared connections)
- [server commands equipment helpers normalize](server_commands_equipment_helpers_normalize.md) (15 shared connections)
- [server async persistence](server_async_persistence.md) (11 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (10 shared connections)
- [server commands equipment helpers](server_commands_equipment_helpers.md) (8 shared connections)
- [server commands inventory item matching](server_commands_inventory_item_matching.md) (8 shared connections)
- [server models player player apply](server_models_player_player_apply.md) (7 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (7 shared connections)
- [server tests unit commands test](server_tests_unit_commands_test.md) (6 shared connections)
- [server schemas shared init](server_schemas_shared_init.md) (6 shared connections)

## Source Files

- `server/commands/equipment_helpers.py`
- `server/commands/inventory_command_coercion.py`
- `server/commands/inventory_command_contracts.py`
- `server/commands/inventory_command_helpers.py`
- `server/commands/inventory_commands.py`
- `server/commands/inventory_drop_command.py`
- `server/commands/inventory_pickup_command.py`
- `server/commands/inventory_unequip_command.py`
- `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- `server/tests/unit/commands/test_inventory_commands_persistence_helpers.py`
- `server/tests/unit/commands/test_inventory_commands_state_helpers.py`

## Audit Trail

- EXTRACTED: 463 (94%)
- INFERRED: 30 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*