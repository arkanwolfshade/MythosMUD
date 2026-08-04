# commands magic rationale

> 129 nodes

## Key Concepts

- **test_magic_commands.py** (49 connections) — `server/tests/unit/commands/test_magic_commands.py`
- **MagicCommandHandler** (34 connections) — `server/commands/magic_commands.py`
- **magic_commands.py** (26 connections) — `server/commands/magic_commands.py`
- **Any** (20 connections)
- **magic_service()** (13 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **SpellCommandError** (12 connections) — `server/commands/magic_commands.py`
- **handle_cast_command()** (9 connections) — `server/commands/magic_commands.py`
- **handle_spells_command()** (9 connections) — `server/commands/magic_commands.py`
- **handle_spell_command()** (9 connections) — `server/commands/magic_commands.py`
- **handle_learn_command()** (9 connections) — `server/commands/magic_commands.py`
- **handle_stop_command()** (9 connections) — `server/commands/magic_commands.py`
- **.handle_cast_command()** (7 connections) — `server/commands/magic_commands.py`
- **._build_cast_response()** (6 connections) — `server/commands/magic_commands.py`
- **._interrupt_rest_for_cast()** (6 connections) — `server/commands/magic_commands.py`
- **.handle_spell_command()** (6 connections) — `server/commands/magic_commands.py`
- **.handle_learn_command()** (6 connections) — `server/commands/magic_commands.py`
- **._resolve_spell_context()** (5 connections) — `server/commands/magic_commands.py`
- **._resolve_learn_context()** (5 connections) — `server/commands/magic_commands.py`
- **Enum** (5 connections)
- **._prepare_cast()** (4 connections) — `server/commands/magic_commands.py`
- **._build_cast_success_message()** (4 connections) — `server/commands/magic_commands.py`
- **.handle_spells_command()** (4 connections) — `server/commands/magic_commands.py`
- **._build_spell_detail_lines()** (4 connections) — `server/commands/magic_commands.py`
- **._announce_spell_cast()** (4 connections) — `server/commands/magic_commands.py`
- **._build_learn_response()** (4 connections) — `server/commands/magic_commands.py`
- *... and 104 more nodes in this community*

## Relationships

- [commands party examples](commands_party_examples.md) (14 shared connections)
- [coercion int inventory](coercion_int_inventory.md) (11 shared connections)
- [player respawn event](player_respawn_event.md) (7 shared connections)
- [commands admin mute](commands_admin_mute.md) (6 shared connections)
- [rest grace period](rest_grace_period.md) (5 shared connections)
- [Loot Generation](Loot_Generation.md) (3 shared connections)
- [chat service game](chat_service_game.md) (3 shared connections)
- [admin auth service](admin_auth_service.md) (3 shared connections)
- [spell game magic](spell_game_magic.md) (2 shared connections)
- [chat game message](chat_game_message.md) (1 shared connections)
- [Database Config](Database_Config.md) (1 shared connections)
- [command commands handler](command_commands_handler.md) (1 shared connections)

## Source Files

- `server/commands/magic_commands.py`
- `server/tests/unit/commands/test_magic_commands.py`
- `server/tests/unit/game/magic/test_magic_service.py`

## Audit Trail

- EXTRACTED: 396 (92%)
- INFERRED: 34 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*