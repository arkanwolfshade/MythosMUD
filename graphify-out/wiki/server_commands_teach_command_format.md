# server commands teach command format

> 22 nodes

## Key Concepts

- **handle_teach_command()** (19 connections) — `server/commands/teach_command.py`
- **test_teach_command.py** (14 connections) — `server/tests/unit/commands/test_teach_command.py`
- **asyncio** (9 connections)
- **_resolve_npc_teacher()** (4 connections) — `server/commands/teach_command.py`
- **test_handle_teach_command()** (4 connections) — `server/tests/unit/commands/test_teach_command.py`
- **test_handle_teach_command_learn_failure()** (4 connections) — `server/tests/unit/commands/test_teach_command.py`
- **test_handle_teach_command_no_persistence()** (4 connections) — `server/tests/unit/commands/test_teach_command.py`
- **test_handle_teach_command_no_target()** (4 connections) — `server/tests/unit/commands/test_teach_command.py`
- **test_handle_teach_command_not_npc_target()** (4 connections) — `server/tests/unit/commands/test_teach_command.py`
- **test_handle_teach_command_success_with_corruption()** (4 connections) — `server/tests/unit/commands/test_teach_command.py`
- **test_handle_teach_command_target_resolution_failure()** (4 connections) — `server/tests/unit/commands/test_teach_command.py`
- **Any** (4 connections)
- **patch** (4 connections)
- **_format_teach_result()** (3 connections) — `server/commands/teach_command.py`
- **_get_teach_services()** (3 connections) — `server/commands/teach_command.py`
- **test_handle_teach_command_no_spell_learning_service()** (3 connections) — `server/tests/unit/commands/test_teach_command.py`
- **test_handle_teach_command_player_not_found()** (3 connections) — `server/tests/unit/commands/test_teach_command.py`
- **Handle /teach command for learning spells from NPCs. Usage: /teach <npc_name>…** (1 connections) — `server/commands/teach_command.py`
- **Unit tests for teach command handlers. Tests the teach command functionality.** (1 connections) — `server/tests/unit/commands/test_teach_command.py`
- **Test handle_teach_command() teaches spell to player.** (1 connections) — `server/tests/unit/commands/test_teach_command.py`
- **Test handle_teach_command() handles missing target.** (1 connections) — `server/tests/unit/commands/test_teach_command.py`
- **Test handle_teach_command() handles missing persistence.** (1 connections) — `server/tests/unit/commands/test_teach_command.py`

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (5 shared connections)
- [server commands admin commands](server_commands_admin_commands.md) (2 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (1 shared connections)
- [server schemas shared target metadata](server_schemas_shared_target_metadata.md) (1 shared connections)
- [server commands combat app protocols](server_commands_combat_app_protocols.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/commands/teach_command.py`
- `server/tests/unit/commands/test_teach_command.py`

## Audit Trail

- EXTRACTED: 51 (93%)
- INFERRED: 4 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*