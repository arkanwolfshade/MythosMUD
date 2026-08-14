# SpellLearningService

> 87 nodes

## Key Concepts

- **SpellLearningService** (50 connections) — `server/game/magic/spell_learning_service.py`
- **MagicCommandHandler** (34 connections) — `server/commands/magic_commands.py`
- **magic_commands.py** (26 connections) — `server/commands/magic_commands.py`
- **Any** (19 connections)
- **test_spell_learning_service.py** (15 connections) — `server/tests/unit/game/magic/test_spell_learning_service.py`
- **magic_service()** (13 connections) — `server/tests/unit/game/magic/test_magic_service.py`
- **SpellCommandError** (12 connections) — `server/commands/magic_commands.py`
- **.learn_spell()** (12 connections) — `server/game/magic/spell_learning_service.py`
- **Any** (12 connections)
- **asyncio** (11 connections)
- **UUID** (10 connections)
- **handle_cast_command()** (9 connections) — `server/commands/magic_commands.py`
- **handle_learn_command()** (9 connections) — `server/commands/magic_commands.py`
- **handle_spell_command()** (9 connections) — `server/commands/magic_commands.py`
- **handle_spells_command()** (9 connections) — `server/commands/magic_commands.py`
- **handle_stop_command()** (9 connections) — `server/commands/magic_commands.py`
- **._validate_prerequisites()** (9 connections) — `server/game/magic/spell_learning_service.py`
- **.__init__()** (8 connections) — `server/commands/magic_commands.py`
- **.handle_cast_command()** (7 connections) — `server/commands/magic_commands.py`
- **._build_cast_response()** (6 connections) — `server/commands/magic_commands.py`
- **.handle_learn_command()** (6 connections) — `server/commands/magic_commands.py`
- **.handle_spell_command()** (6 connections) — `server/commands/magic_commands.py`
- **._load_spell_learn_context()** (6 connections) — `server/game/magic/spell_learning_service.py`
- **._resolve_learn_context()** (5 connections) — `server/commands/magic_commands.py`
- **._resolve_spell_context()** (5 connections) — `server/commands/magic_commands.py`
- *... and 62 more nodes in this community*

## Relationships

- [PlayerService](PlayerService.md) (27 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (22 shared connections)
- [AliasStorage](AliasStorage.md) (19 shared connections)
- [test_magic_commands.py](test_magic_commands.py.md) (8 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (6 shared connections)
- [ChatService](ChatService.md) (4 shared connections)
- [Enum](Enum.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [fixture](fixture.md) (1 shared connections)
- [asyncio](asyncio.md) (1 shared connections)
- [test_handle_learn_command_wrapper_success](test_handle_learn_command_wrapper_success.md) (1 shared connections)
- [test_handle_spell_command_wrapper_success](test_handle_spell_command_wrapper_success.md) (1 shared connections)

## Source Files

- `server/commands/magic_commands.py`
- `server/game/magic/spell_learning_service.py`
- `server/tests/unit/game/magic/test_magic_service.py`
- `server/tests/unit/game/magic/test_spell_learning_service.py`

## Audit Trail

- EXTRACTED: 245 (87%)
- INFERRED: 37 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*