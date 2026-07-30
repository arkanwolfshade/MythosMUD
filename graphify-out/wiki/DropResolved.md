# DropResolved

> 23 nodes

## Key Concepts

- **admin_summon_command.py** (34 connections) — `server/commands/admin_summon_command.py`
- **_resolve_summon_context()** (11 connections) — `server/commands/admin_summon_command.py`
- **Any** (10 connections)
- **handle_summon_command()** (10 connections) — `server/commands/admin_summon_command.py`
- **_broadcast_and_log_summon_success()** (7 connections) — `server/commands/admin_summon_command.py`
- **_complete_summon()** (7 connections) — `server/commands/admin_summon_command.py`
- **_persist_summoned_item()** (6 connections) — `server/commands/admin_summon_command.py`
- **_parse_summon_command_data()** (5 connections) — `server/commands/admin_summon_command.py`
- **_validate_summon_prerequisites()** (4 connections) — `server/commands/admin_summon_command.py`
- **_summon_npc_stub_response()** (4 connections) — `server/commands/admin_summon_command.py`
- **_create_summon_item_instance()** (4 connections) — `server/commands/admin_summon_command.py`
- **_log_summon_success()** (4 connections) — `server/commands/admin_summon_command.py`
- **Administrative summon command implementation.** (1 connections) — `server/commands/admin_summon_command.py`
- **Return an error result dict if item services or room manager are missing; otherw** (1 connections) — `server/commands/admin_summon_command.py`
- **If target_type is 'npc', log and return stub message; otherwise return None.** (1 connections) — `server/commands/admin_summon_command.py`
- **Create item instance via factory. Returns (instance, None) or (None, error_dict)** (1 connections) — `server/commands/admin_summon_command.py`
- **Persist item instance to DB. Logs and continues on failure (room drop still adde** (1 connections) — `server/commands/admin_summon_command.py`
- **Resolve state, player, admin permission, and summon prerequisites.      Returns** (1 connections) — `server/commands/admin_summon_command.py`
- **Parse and validate command_data; optionally record quantity spike; check NPC stu** (1 connections) — `server/commands/admin_summon_command.py`
- **Broadcast admin_summon event to room, then record success logs.** (1 connections) — `server/commands/admin_summon_command.py`
- **Log successful summon in admin logger and structured logs.** (1 connections) — `server/commands/admin_summon_command.py`
- **Create item, persist, add to room, broadcast event, log; return success message.** (1 connections) — `server/commands/admin_summon_command.py`
- **Handle the `/summon` administrative command.** (1 connections) — `server/commands/admin_summon_command.py`

## Relationships

- [Any](Any.md) (10 shared connections)
- [test command factories inventory](test_command_factories_inventory.md) (6 shared connections)
- [real time](real_time.md) (3 shared connections)
- [circuit breaker](circuit_breaker.md) (3 shared connections)
- [Player Position Service](Player_Position_Service.md) (3 shared connections)
- [handle global command()](handle_global_command%28%29.md) (2 shared connections)
- [.initialize()](initialize%28%29.md) (2 shared connections)
- [Player](Player.md) (2 shared connections)
- [init](init.md) (2 shared connections)
- [world](world.md) (2 shared connections)
- [PerformanceStats](PerformanceStats.md) (1 shared connections)
- [.state()](state%28%29.md) (1 shared connections)

## Source Files

- `server/commands/admin_summon_command.py`

## Audit Trail

- EXTRACTED: 113 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*