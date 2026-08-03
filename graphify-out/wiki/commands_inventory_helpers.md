# commands inventory helpers

> 23 nodes

## Key Concepts

- **admin_summon_command.py** (34 connections) — `server/commands/admin_summon_command.py`
- **_resolve_summon_context()** (11 connections) — `server/commands/admin_summon_command.py`
- **Any** (10 connections)
- **handle_summon_command()** (9 connections) — `server/commands/admin_summon_command.py`
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

- [commands alias rationale](commands_alias_rationale.md) (7 shared connections)
- [inventory commands command](inventory_commands_command.md) (7 shared connections)
- [combat services turn](combat_services_turn.md) (6 shared connections)
- [command inventory factories](command_inventory_factories.md) (3 shared connections)
- [NATS Messaging](NATS_Messaging.md) (3 shared connections)
- [combat services messaging](combat_services_messaging.md) (3 shared connections)
- [npc populate databases](npc_populate_databases.md) (2 shared connections)
- [health models rationale](health_models_rationale.md) (2 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)
- [System Metrics](System_Metrics.md) (1 shared connections)
- [realtime game state](realtime_game_state.md) (1 shared connections)

## Source Files

- `server/commands/admin_summon_command.py`

## Audit Trail

- EXTRACTED: 113 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*