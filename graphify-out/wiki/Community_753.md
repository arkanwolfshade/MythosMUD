# Community 753

> 22 nodes

## Key Concepts

- **handle_teach_command()** (18 connections) — `server/commands/teach_command.py`
- **test_teach_command.py** (13 connections) — `server/tests/unit/commands/test_teach_command.py`
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

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (7 shared connections)
- [Channel Commands](Channel_Commands.md) (1 shared connections)
- [Community 45](Community_45.md) (1 shared connections)

## Source Files

- `server/commands/teach_command.py`
- `server/tests/unit/commands/test_teach_command.py`

## Audit Trail

- EXTRACTED: 51 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*