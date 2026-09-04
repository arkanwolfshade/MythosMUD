# Test Teach Command

> 24 nodes

## Key Concepts

- **handle_teach_command()** (18 connections) — `server/commands/teach_command.py`
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

- [Test Target Resolution Service](Test_Target_Resolution_Service.md) (3 shared connections)
- [Test Npc Admin Commands](Test_Npc_Admin_Commands.md) (2 shared connections)
- [Combat Spell Effects (Flee)](Combat_Spell_Effects_Flee.md) (2 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (2 shared connections)
- [Test Rescue Commands](Test_Rescue_Commands.md) (1 shared connections)
- [Test Position Commands](Test_Position_Commands.md) (1 shared connections)
- [Alias Storage](Alias_Storage.md) (1 shared connections)
- [Test Command Parser](Test_Command_Parser.md) (1 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/commands/teach_command.py`
- `server/tests/unit/commands/test_teach_command.py`

## Audit Trail

- EXTRACTED: 62 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*