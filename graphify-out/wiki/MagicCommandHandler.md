# MagicCommandHandler

> 45 nodes

## Key Concepts

- **MagicCommandHandler** (30 connections) — `server/commands/magic_commands.py`
- **magic_commands.py** (28 connections) — `server/commands/magic_commands.py`
- **Any** (19 connections)
- **magic_service()** (13 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **handle_cast_command()** (9 connections) — `server/commands/magic_commands.py`
- **handle_learn_command()** (9 connections) — `server/commands/magic_commands.py`
- **handle_spell_command()** (9 connections) — `server/commands/magic_commands.py`
- **handle_spells_command()** (9 connections) — `server/commands/magic_commands.py`
- **handle_stop_command()** (9 connections) — `server/commands/magic_commands.py`
- **.handle_cast_command()** (7 connections) — `server/commands/magic_commands.py`
- **SpellCommandError** (6 connections) — `server/commands/magic_commands.py`
- **._build_cast_response()** (6 connections) — `server/commands/magic_commands.py`
- **.handle_learn_command()** (6 connections) — `server/commands/magic_commands.py`
- **.handle_spell_command()** (6 connections) — `server/commands/magic_commands.py`
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
- *... and 20 more nodes in this community*

## Relationships

- [AliasStorage](AliasStorage.md) (12 shared connections)
- [test_magic_commands.py](test_magic_commands.py.md) (7 shared connections)
- [test_magic_service.py](test_magic_service.py.md) (7 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (6 shared connections)
- [command_service.py](command_service.py.md) (6 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [SpellLearningService](SpellLearningService.md) (4 shared connections)
- [lifespan_magic.py](lifespan_magic.py.md) (2 shared connections)
- [SpellEffects](SpellEffects.md) (2 shared connections)
- [ChatService](ChatService.md) (2 shared connections)
- [asyncio](asyncio.md) (2 shared connections)
- [TargetMatch](TargetMatch.md) (2 shared connections)

## Source Files

- `server/commands/magic_commands.py`
- `server/tests/unit/game/magic/test_magic_service.py`

## Audit Trail

- EXTRACTED: 121 (82%)
- INFERRED: 26 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*