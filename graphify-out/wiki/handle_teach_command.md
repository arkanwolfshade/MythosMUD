# handle_teach_command

> 24 nodes

## Key Concepts

- **handle_teach_command()** (19 connections) — `server/commands/teach_command.py`
- **teach_command.py** (15 connections) — `server/commands/teach_command.py`
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
- **Teach command handler for learning spells from NPC teachers. This module…** (1 connections) — `server/commands/teach_command.py`
- **Handle /teach command for learning spells from NPCs. Usage: /teach <npc_name>…** (1 connections) — `server/commands/teach_command.py`
- **Unit tests for teach command handlers. Tests the teach command functionality.** (1 connections) — `server/tests/unit/commands/test_teach_command.py`
- **Test handle_teach_command() teaches spell to player.** (1 connections) — `server/tests/unit/commands/test_teach_command.py`
- **Test handle_teach_command() handles missing target.** (1 connections) — `server/tests/unit/commands/test_teach_command.py`
- **Test handle_teach_command() handles missing persistence.** (1 connections) — `server/tests/unit/commands/test_teach_command.py`

## Relationships

- [TargetResolutionService](TargetResolutionService.md) (5 shared connections)
- [AliasStorage](AliasStorage.md) (2 shared connections)
- [command_service.py](command_service.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [get_username_from_user](get_username_from_user.md) (1 shared connections)
- [alias_storage.py](alias_storage.py.md) (1 shared connections)
- [CommandFactory](CommandFactory.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/commands/teach_command.py`
- `server/tests/unit/commands/test_teach_command.py`

## Audit Trail

- EXTRACTED: 61 (94%)
- INFERRED: 4 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*