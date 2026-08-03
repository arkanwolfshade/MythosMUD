# inventory commands command

> 209 nodes

## Key Concepts

- **inventory_command_helpers.py** (48 connections) — `server/commands/inventory_command_helpers.py`
- **inventory_pickup_command.py** (35 connections) — `server/commands/inventory_pickup_command.py`
- **persist_player()** (30 connections) — `server/commands/inventory_command_helpers.py`
- **inventory_get_command.py** (29 connections) — `server/commands/inventory_get_command.py`
- **inventory_commands.py** (28 connections) — `server/commands/inventory_commands.py`
- **test_inventory_helpers_extended.py** (26 connections) — `server/tests/unit/commands/test_inventory_helpers_extended.py`
- **inventory_drop_command.py** (25 connections) — `server/commands/inventory_drop_command.py`
- **test_inventory_commands_more_helpers.py** (23 connections) — `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- **inventory_put_command.py** (21 connections) — `server/commands/inventory_put_command.py`
- **RoomDropManager** (19 connections) — `server/commands/inventory_command_contracts.py`
- **resolve_state_and_player()** (19 connections) — `server/commands/inventory_command_helpers.py`
- **resolve_state()** (18 connections) — `server/commands/inventory_command_helpers.py`
- **resolve_player()** (18 connections) — `server/commands/inventory_command_helpers.py`
- **clone_inventory()** (18 connections) — `server/commands/inventory_command_helpers.py`
- **broadcast_room_event()** (18 connections) — `server/commands/inventory_command_helpers.py`
- **handle_pickup_command()** (17 connections) — `server/commands/inventory_pickup_command.py`
- **handle_drop_command()** (14 connections) — `server/commands/inventory_drop_command.py`
- **build_and_broadcast_inventory_event()** (13 connections) — `server/commands/inventory_command_helpers.py`
- **_handle_get_from_room()** (13 connections) — `server/commands/inventory_get_command.py`
- **handle_get_command()** (13 connections) — `server/commands/inventory_get_command.py`
- **_pickup_commit_inventory_after_floor_extract()** (13 connections) — `server/commands/inventory_pickup_command.py`
- **_drop_resolve_stack_or_error()** (12 connections) — `server/commands/inventory_drop_command.py`
- **_get_from_container_path()** (12 connections) — `server/commands/inventory_get_command.py`
- **handle_put_command()** (12 connections) — `server/commands/inventory_put_command.py`
- **test_inventory_commands_persistence_helpers.py** (12 connections) — `server/tests/unit/commands/test_inventory_commands_persistence_helpers.py`
- *... and 184 more nodes in this community*

## Relationships

- [commands alias rationale](commands_alias_rationale.md) (19 shared connections)
- [commands inventory helpers](commands_inventory_helpers.md) (17 shared connections)
- [commands inventory pickup](commands_inventory_pickup.md) (16 shared connections)
- [Inventory Equip](Inventory_Equip.md) (13 shared connections)
- [commands inventory command](commands_inventory_command.md) (12 shared connections)
- [NATS Messaging](NATS_Messaging.md) (12 shared connections)
- [container helpers endpoints](container_helpers_endpoints.md) (10 shared connections)
- [container inventory helpers](container_inventory_helpers.md) (10 shared connections)
- [models player rationale](models_player_rationale.md) (8 shared connections)
- [Async Query Helpers](Async_Query_Helpers.md) (7 shared connections)
- [npc population stats](npc_population_stats.md) (7 shared connections)
- [world models rationale](world_models_rationale.md) (6 shared connections)

## Source Files

- `server/commands/inventory_command_coercion.py`
- `server/commands/inventory_command_contracts.py`
- `server/commands/inventory_command_helpers.py`
- `server/commands/inventory_commands.py`
- `server/commands/inventory_drop_command.py`
- `server/commands/inventory_get_command.py`
- `server/commands/inventory_pickup_command.py`
- `server/commands/inventory_put_command.py`
- `server/tests/unit/commands/test_inventory_commands.py`
- `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- `server/tests/unit/commands/test_inventory_commands_persistence_helpers.py`
- `server/tests/unit/commands/test_inventory_commands_state_helpers.py`
- `server/tests/unit/commands/test_inventory_helpers_extended.py`

## Audit Trail

- EXTRACTED: 942 (93%)
- INFERRED: 73 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*