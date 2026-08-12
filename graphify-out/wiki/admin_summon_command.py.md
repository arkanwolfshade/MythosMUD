# admin_summon_command.py

> 23 nodes

## Key Concepts

- **admin_summon_command.py** (34 connections) — `server/commands/admin_summon_command.py`
- **_resolve_summon_context()** (11 connections) — `server/commands/admin_summon_command.py`
- **handle_summon_command()** (10 connections) — `server/commands/admin_summon_command.py`
- **Any** (10 connections)
- **_broadcast_and_log_summon_success()** (7 connections) — `server/commands/admin_summon_command.py`
- **_complete_summon()** (7 connections) — `server/commands/admin_summon_command.py`
- **_parse_summon_command_data()** (5 connections) — `server/commands/admin_summon_command.py`
- **_create_summon_item_instance()** (4 connections) — `server/commands/admin_summon_command.py`
- **_log_summon_success()** (4 connections) — `server/commands/admin_summon_command.py`
- **_persist_summoned_item()** (4 connections) — `server/commands/admin_summon_command.py`
- **_summon_npc_stub_response()** (4 connections) — `server/commands/admin_summon_command.py`
- **_validate_summon_prerequisites()** (4 connections) — `server/commands/admin_summon_command.py`
- **Administrative summon command implementation.** (1 connections) — `server/commands/admin_summon_command.py`
- **Persist item instance to DB. Logs and continues on failure (room drop still…** (1 connections) — `server/commands/admin_summon_command.py`
- **Resolve state, player, admin permission, and summon prerequisites. Returns…** (1 connections) — `server/commands/admin_summon_command.py`
- **Parse and validate command_data; optionally record quantity spike; check NPC…** (1 connections) — `server/commands/admin_summon_command.py`
- **Broadcast admin_summon event to room, then record success logs.** (1 connections) — `server/commands/admin_summon_command.py`
- **Return an error result dict if item services or room manager are missing;…** (1 connections) — `server/commands/admin_summon_command.py`
- **Log successful summon in admin logger and structured logs.** (1 connections) — `server/commands/admin_summon_command.py`
- **Create item, persist, add to room, broadcast event, log; return success message.** (1 connections) — `server/commands/admin_summon_command.py`
- **Handle the `/summon` administrative command.** (1 connections) — `server/commands/admin_summon_command.py`
- **If target_type is 'npc', log and return stub message; otherwise return None.** (1 connections) — `server/commands/admin_summon_command.py`
- **Create item instance via factory. Returns (instance, None) or (None,…** (1 connections) — `server/commands/admin_summon_command.py`

## Relationships

- [admin_teleport_commands.py](admin_teleport_commands.py.md) (6 shared connections)
- [inventory_command_helpers.py](inventory_command_helpers.py.md) (5 shared connections)
- [AliasStorage](AliasStorage.md) (5 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [lifespan.py](lifespan.py.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [test_alias_commands.py](test_alias_commands.py.md) (2 shared connections)
- [resolve_state](resolve_state.md) (2 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (2 shared connections)
- [item_factory.py](item_factory.py.md) (2 shared connections)
- [.state](state.md) (1 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)

## Source Files

- `server/commands/admin_summon_command.py`

## Audit Trail

- EXTRACTED: 113 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*