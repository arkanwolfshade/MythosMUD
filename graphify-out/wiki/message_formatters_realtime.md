# message formatters realtime

> 21 nodes

## Key Concepts

- **handle_teach_command()** (18 connections) — `server/commands/teach_command.py`
- **teach_command.py** (14 connections) — `server/commands/teach_command.py`
- **test_teach_command.py** (13 connections) — `server/tests/unit/commands/test_teach_command.py`
- **test_handle_teach_command()** (3 connections) — `server/tests/unit/commands/test_teach_command.py`
- **test_handle_teach_command_no_target()** (3 connections) — `server/tests/unit/commands/test_teach_command.py`
- **test_handle_teach_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_teach_command.py`
- **Any** (2 connections)
- **test_handle_teach_command_no_spell_learning_service()** (2 connections) — `server/tests/unit/commands/test_teach_command.py`
- **test_handle_teach_command_player_not_found()** (2 connections) — `server/tests/unit/commands/test_teach_command.py`
- **test_handle_teach_command_target_resolution_failure()** (2 connections) — `server/tests/unit/commands/test_teach_command.py`
- **test_handle_teach_command_not_npc_target()** (2 connections) — `server/tests/unit/commands/test_teach_command.py`
- **test_handle_teach_command_learn_failure()** (2 connections) — `server/tests/unit/commands/test_teach_command.py`
- **test_handle_teach_command_success_with_corruption()** (2 connections) — `server/tests/unit/commands/test_teach_command.py`
- **Teach command handler for learning spells from NPC teachers.  This module handle** (1 connections) — `server/commands/teach_command.py`
- **Handle /teach command for learning spells from NPCs.      Usage: /teach <npc_nam** (1 connections) — `server/commands/teach_command.py`
- **# TODO: Check if NPC is a teacher and can teach this spell  # pylint: disable=fi** (1 connections) — `server/commands/teach_command.py`
- **# TODO: Send message to room about NPC teaching  # pylint: disable=fixme  # Reas** (1 connections) — `server/commands/teach_command.py`
- **Unit tests for teach command handlers.  Tests the teach command functionality.** (1 connections) — `server/tests/unit/commands/test_teach_command.py`
- **Test handle_teach_command() teaches spell to player.** (1 connections) — `server/tests/unit/commands/test_teach_command.py`
- **Test handle_teach_command() handles missing target.** (1 connections) — `server/tests/unit/commands/test_teach_command.py`
- **Test handle_teach_command() handles missing persistence.** (1 connections) — `server/tests/unit/commands/test_teach_command.py`

## Relationships

- [NPC Services Bootstrap](NPC_Services_Bootstrap.md) (5 shared connections)
- [commands npc admin](commands_npc_admin.md) (4 shared connections)
- [character creation service](character_creation_service.md) (2 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (2 shared connections)
- [command inventory factories](command_inventory_factories.md) (1 shared connections)
- [middleware correlation rationale](middleware_correlation_rationale.md) (1 shared connections)
- [connection realtime manager](connection_realtime_manager.md) (1 shared connections)

## Source Files

- `server/commands/teach_command.py`
- `server/tests/unit/commands/test_teach_command.py`

## Audit Trail

- EXTRACTED: 73 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*