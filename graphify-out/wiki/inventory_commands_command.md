# inventory commands command

> 148 nodes

## Key Concepts

- **inventory_command_helpers.py** (48 connections) — `server/commands/inventory_command_helpers.py`
- **inventory_pickup_command.py** (35 connections) — `server/commands/inventory_pickup_command.py`
- **persist_player()** (30 connections) — `server/commands/inventory_command_helpers.py`
- **test_inventory_helpers_extended.py** (26 connections) — `server/tests/unit/commands/test_inventory_helpers_extended.py`
- **inventory_drop_command.py** (25 connections) — `server/commands/inventory_drop_command.py`
- **test_inventory_commands_more_helpers.py** (23 connections) — `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- **RoomDropManager** (19 connections) — `server/commands/inventory_command_contracts.py`
- **resolve_state_and_player()** (19 connections) — `server/commands/inventory_command_helpers.py`
- **resolve_state()** (18 connections) — `server/commands/inventory_command_helpers.py`
- **resolve_player()** (18 connections) — `server/commands/inventory_command_helpers.py`
- **clone_inventory()** (18 connections) — `server/commands/inventory_command_helpers.py`
- **broadcast_room_event()** (18 connections) — `server/commands/inventory_command_helpers.py`
- **handle_drop_command()** (14 connections) — `server/commands/inventory_drop_command.py`
- **build_and_broadcast_inventory_event()** (13 connections) — `server/commands/inventory_command_helpers.py`
- **_pickup_commit_inventory_after_floor_extract()** (13 connections) — `server/commands/inventory_pickup_command.py`
- **_drop_resolve_stack_or_error()** (12 connections) — `server/commands/inventory_drop_command.py`
- **Player** (11 connections)
- **add_pickup_to_inventory()** (10 connections) — `server/commands/inventory_command_helpers.py`
- **FloorPickupAfterExtract** (10 connections) — `server/commands/inventory_pickup_command.py`
- **_pickup_resolve_floor_stack_or_error()** (10 connections) — `server/commands/inventory_pickup_command.py`
- **complete_pickup_after_floor_extract()** (9 connections) — `server/commands/inventory_pickup_command.py`
- **resolve_pickup_item_index()** (8 connections) — `server/commands/inventory_command_helpers.py`
- **_sync_collect_quests_after_inventory_save()** (7 connections) — `server/commands/inventory_command_helpers.py`
- **ensure_item_instance_for_pickup()** (7 connections) — `server/commands/inventory_command_helpers.py`
- **get_room_manager()** (7 connections) — `server/commands/inventory_command_helpers.py`
- *... and 123 more nodes in this community*

## Relationships

- [container helpers endpoints](container_helpers_endpoints.md) (30 shared connections)
- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (21 shared connections)
- [commands inventory pickup](commands_inventory_pickup.md) (19 shared connections)
- [Loot Generation](Loot_Generation.md) (11 shared connections)
- [combat models rationale](combat_models_rationale.md) (11 shared connections)
- [commands inventory command](commands_inventory_command.md) (9 shared connections)
- [commands inventory put](commands_inventory_put.md) (7 shared connections)
- [models player rationale](models_player_rationale.md) (7 shared connections)
- [npc population stats](npc_population_stats.md) (6 shared connections)
- [commands inventory helpers](commands_inventory_helpers.md) (5 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (3 shared connections)
- [commands party examples](commands_party_examples.md) (3 shared connections)

## Source Files

- `server/commands/inventory_command_contracts.py`
- `server/commands/inventory_command_helpers.py`
- `server/commands/inventory_drop_command.py`
- `server/commands/inventory_pickup_command.py`
- `server/tests/unit/commands/test_inventory_commands_more_helpers.py`
- `server/tests/unit/commands/test_inventory_commands_state_helpers.py`
- `server/tests/unit/commands/test_inventory_helpers_extended.py`

## Audit Trail

- EXTRACTED: 661 (96%)
- INFERRED: 30 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*