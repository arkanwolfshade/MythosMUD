# admin summon command

> 25 nodes

## Key Concepts

- **admin_summon_command.py** (34 connections) — `server/commands/admin_summon_command.py`
- **resolve_player()** (18 connections) — `server/commands/inventory_command_helpers.py`
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
- **Resolve player from persistence and current user.** (1 connections) — `server/commands/inventory_command_helpers.py`

## Relationships

- [Any](Any.md) (14 shared connections)
- [test resolve state no app()](test_resolve_state_no_app%28%29.md) (13 shared connections)
- [main()](main%28%29.md) (10 shared connections)
- [DropResolved](DropResolved.md) (4 shared connections)
- [UUID](UUID.md) (3 shared connections)
- [. init ()](_init_%28%29.md) (2 shared connections)
- [.state()](state%28%29.md) (1 shared connections)
- [communication commands support](communication_commands_support.md) (1 shared connections)
- [. get persistence from app()](_get_persistence_from_app%28%29.md) (1 shared connections)
- [MythosValidationError](MythosValidationError.md) (1 shared connections)

## Source Files

- `server/commands/admin_summon_command.py`
- `server/commands/inventory_command_helpers.py`

## Audit Trail

- EXTRACTED: 130 (96%)
- INFERRED: 6 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*