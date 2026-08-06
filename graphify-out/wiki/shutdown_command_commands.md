# shutdown command commands

> 23 nodes

## Key Concepts

- **admin_summon_command.py** (35 connections) — `server/commands/admin_summon_command.py`
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

- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (7 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (5 shared connections)
- [character creation service](character_creation_service.md) (4 shared connections)
- [admin structured logging](admin_structured_logging.md) (4 shared connections)
- [commands npc admin](commands_npc_admin.md) (3 shared connections)
- [room cache services](room_cache_services.md) (3 shared connections)
- [security sessionManager SessionManager](security_sessionManager_SessionManager.md) (2 shared connections)
- [endpoints auth rationale](endpoints_auth_rationale.md) (2 shared connections)
- [command inventory models](command_inventory_models.md) (2 shared connections)
- [schedule service services](schedule_service_services.md) (2 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (1 shared connections)
- [npc behavior engine](npc_behavior_engine.md) (1 shared connections)

## Source Files

- `server/commands/admin_summon_command.py`

## Audit Trail

- EXTRACTED: 114 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*