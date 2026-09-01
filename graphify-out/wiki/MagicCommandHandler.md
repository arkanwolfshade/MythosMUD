# MagicCommandHandler

> 35 nodes

## Key Concepts

- **MagicCommandHandler** (30 connections) — `server/commands/magic_commands.py`
- **Any** (19 connections)
- **.handle_cast_command()** (7 connections) — `server/commands/magic_commands.py`
- **SpellCommandError** (6 connections) — `server/commands/magic_commands.py`
- **._build_cast_response()** (6 connections) — `server/commands/magic_commands.py`
- **.handle_learn_command()** (6 connections) — `server/commands/magic_commands.py`
- **.handle_spell_command()** (6 connections) — `server/commands/magic_commands.py`
- **._interrupt_rest_for_cast()** (6 connections) — `server/commands/magic_commands.py`
- **._resolve_learn_context()** (5 connections) — `server/commands/magic_commands.py`
- **._resolve_spell_context()** (5 connections) — `server/commands/magic_commands.py`
- **._announce_spell_cast()** (4 connections) — `server/commands/magic_commands.py`
- **._build_cast_success_message()** (4 connections) — `server/commands/magic_commands.py`
- **._build_learn_response()** (4 connections) — `server/commands/magic_commands.py`
- **._build_spell_detail_lines()** (4 connections) — `server/commands/magic_commands.py`
- **.handle_spells_command()** (4 connections) — `server/commands/magic_commands.py`
- **.handle_stop_command()** (4 connections) — `server/commands/magic_commands.py`
- **._prepare_cast()** (4 connections) — `server/commands/magic_commands.py`
- **.__init__()** (2 connections) — `server/commands/magic_commands.py`
- **Exception** (1 connections)
- **Resolve player and spell parameters for a cast; returns error message if…** (1 connections) — `server/commands/magic_commands.py`
- **Build the response payload for a cast result and send announcements.** (1 connections) — `server/commands/magic_commands.py`
- **Build the final success message for a cast spell.** (1 connections) — `server/commands/magic_commands.py`
- **If player is resting, cancel rest countdown so they can cast. Swallows errors…** (1 connections) — `server/commands/magic_commands.py`
- **Handle /spells command - list learned spells. Args: command_data: Command data…** (1 connections) — `server/commands/magic_commands.py`
- **Handle /spell command - show spell details.** (1 connections) — `server/commands/magic_commands.py`
- *... and 10 more nodes in this community*

## Relationships

- [command_service.py](command_service.py.md) (12 shared connections)
- [AliasStorage](AliasStorage.md) (6 shared connections)
- [SpellEffects](SpellEffects.md) (4 shared connections)
- [test_magic_commands.py](test_magic_commands.py.md) (2 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (2 shared connections)
- [test_magic_service.py](test_magic_service.py.md) (1 shared connections)
- [SpellLearningService](SpellLearningService.md) (1 shared connections)
- [ChatService](ChatService.md) (1 shared connections)

## Source Files

- `server/commands/magic_commands.py`

## Audit Trail

- EXTRACTED: 79 (92%)
- INFERRED: 7 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*