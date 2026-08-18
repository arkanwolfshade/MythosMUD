# server commands inventory command helpers

> 39 nodes

## Key Concepts

- **test_inventory_helpers_extended.py** (27 connections) — `server/tests/unit/commands/test_inventory_helpers_extended.py`
- **broadcast_room_event()** (19 connections) — `server/commands/inventory_command_helpers.py`
- **resolve_player()** (17 connections) — `server/commands/inventory_command_helpers.py`
- **asyncio** (15 connections)
- **ensure_item_instance_for_pickup()** (7 connections) — `server/commands/inventory_command_helpers.py`
- **test_resolve_player_username_error()** (6 connections) — `server/tests/unit/commands/test_inventory_helpers_extended.py`
- **test_persist_player_validation_error()** (5 connections) — `server/tests/unit/commands/test_inventory_helpers_extended.py`
- **test_broadcast_room_event_async()** (4 connections) — `server/tests/unit/commands/test_inventory_helpers_extended.py`
- **test_broadcast_room_event_error()** (4 connections) — `server/tests/unit/commands/test_inventory_helpers_extended.py`
- **test_broadcast_room_event_no_broadcast_method()** (4 connections) — `server/tests/unit/commands/test_inventory_helpers_extended.py`
- **test_broadcast_room_event_no_connection_manager()** (4 connections) — `server/tests/unit/commands/test_inventory_helpers_extended.py`
- **test_broadcast_room_event_success()** (4 connections) — `server/tests/unit/commands/test_inventory_helpers_extended.py`
- **test_broadcast_room_event_with_exclude()** (4 connections) — `server/tests/unit/commands/test_inventory_helpers_extended.py`
- **test_persist_player_general_error()** (4 connections) — `server/tests/unit/commands/test_inventory_helpers_extended.py`
- **test_persist_player_success()** (4 connections) — `server/tests/unit/commands/test_inventory_helpers_extended.py`
- **test_resolve_player_no_persistence()** (4 connections) — `server/tests/unit/commands/test_inventory_helpers_extended.py`
- **test_resolve_player_not_found()** (4 connections) — `server/tests/unit/commands/test_inventory_helpers_extended.py`
- **test_resolve_player_persistence_error()** (4 connections) — `server/tests/unit/commands/test_inventory_helpers_extended.py`
- **test_resolve_player_success()** (4 connections) — `server/tests/unit/commands/test_inventory_helpers_extended.py`
- **test_clone_inventory()** (3 connections) — `server/tests/unit/commands/test_inventory_helpers_extended.py`
- **test_ensure_item_instance_for_pickup_awaits_async_ensure()** (3 connections) — `server/tests/unit/commands/test_inventory_helpers_extended.py`
- **Test _broadcast_room_event when connection_manager is None.** (2 connections) — `server/tests/unit/commands/test_inventory_helpers_extended.py`
- **Ensure item instance exists in database for picked up item.** (1 connections) — `server/commands/inventory_command_helpers.py`
- **Resolve player from persistence and current user.** (1 connections) — `server/commands/inventory_command_helpers.py`
- **Broadcast event to room, excluding optional player.** (1 connections) — `server/commands/inventory_command_helpers.py`
- *... and 14 more nodes in this community*

## Relationships

- [dropresolved](dropresolved.md) (26 shared connections)
- [server commands admin summon command](server_commands_admin_summon_command.md) (4 shared connections)
- [mythosvalidationerror](mythosvalidationerror.md) (3 shared connections)
- [server schemas shared init](server_schemas_shared_init.md) (2 shared connections)
- [server commands position commands](server_commands_position_commands.md) (1 shared connections)
- [server commands admin commands](server_commands_admin_commands.md) (1 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (1 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (1 shared connections)

## Source Files

- `server/commands/inventory_command_helpers.py`
- `server/tests/unit/commands/test_inventory_helpers_extended.py`

## Audit Trail

- EXTRACTED: 100 (96%)
- INFERRED: 4 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*