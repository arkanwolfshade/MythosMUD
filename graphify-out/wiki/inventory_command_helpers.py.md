# inventory_command_helpers.py

> 37 nodes

## Key Concepts

- **inventory_command_helpers.py** (48 connections) — `server/commands/inventory_command_helpers.py`
- **admin_summon_command.py** (34 connections) — `server/commands/admin_summon_command.py`
- **broadcast_room_event()** (18 connections) — `server/commands/inventory_command_helpers.py`
- **resolve_state()** (18 connections) — `server/commands/inventory_command_helpers.py`
- **build_and_broadcast_inventory_event()** (13 connections) — `server/commands/inventory_command_helpers.py`
- **_resolve_summon_context()** (11 connections) — `server/commands/admin_summon_command.py`
- **Any** (10 connections)
- **_broadcast_and_log_summon_success()** (7 connections) — `server/commands/admin_summon_command.py`
- **_complete_summon()** (7 connections) — `server/commands/admin_summon_command.py`
- **test_inventory_commands_state_helpers.py** (6 connections) — `server/tests/unit/commands/test_inventory_commands_state_helpers.py`
- **_parse_summon_command_data()** (5 connections) — `server/commands/admin_summon_command.py`
- **_create_summon_item_instance()** (4 connections) — `server/commands/admin_summon_command.py`
- **_log_summon_success()** (4 connections) — `server/commands/admin_summon_command.py`
- **_persist_summoned_item()** (4 connections) — `server/commands/admin_summon_command.py`
- **_summon_npc_stub_response()** (4 connections) — `server/commands/admin_summon_command.py`
- **_validate_summon_prerequisites()** (4 connections) — `server/commands/admin_summon_command.py`
- **test_resolve_state_no_app()** (3 connections) — `server/tests/unit/commands/test_inventory_commands_state_helpers.py`
- **test_resolve_state_no_state()** (3 connections) — `server/tests/unit/commands/test_inventory_commands_state_helpers.py`
- **test_resolve_state_success()** (3 connections) — `server/tests/unit/commands/test_inventory_commands_state_helpers.py`
- **Administrative summon command implementation.** (1 connections) — `server/commands/admin_summon_command.py`
- **Persist item instance to DB. Logs and continues on failure (room drop still…** (1 connections) — `server/commands/admin_summon_command.py`
- **Resolve state, player, admin permission, and summon prerequisites. Returns…** (1 connections) — `server/commands/admin_summon_command.py`
- **Parse and validate command_data; optionally record quantity spike; check NPC…** (1 connections) — `server/commands/admin_summon_command.py`
- **Broadcast admin_summon event to room, then record success logs.** (1 connections) — `server/commands/admin_summon_command.py`
- **Return an error result dict if item services or room manager are missing;…** (1 connections) — `server/commands/admin_summon_command.py`
- *... and 12 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (15 shared connections)
- [persist_player](persist_player.md) (14 shared connections)
- [test_inventory_helpers_extended.py](test_inventory_helpers_extended.py.md) (12 shared connections)
- [test_inventory_commands_more_helpers.py](test_inventory_commands_more_helpers.py.md) (11 shared connections)
- [AliasStorage](AliasStorage.md) (8 shared connections)
- [inventory_pickup_command.py](inventory_pickup_command.py.md) (7 shared connections)
- [test_inventory_helpers.py](test_inventory_helpers.py.md) (7 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (6 shared connections)
- [inventory_equip_command.py](inventory_equip_command.py.md) (3 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (3 shared connections)
- [Player](Player.md) (3 shared connections)
- [lifespan.py](lifespan.py.md) (2 shared connections)

## Source Files

- `server/commands/admin_summon_command.py`
- `server/commands/inventory_command_helpers.py`
- `server/tests/unit/commands/test_inventory_commands_state_helpers.py`

## Audit Trail

- EXTRACTED: 222 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*