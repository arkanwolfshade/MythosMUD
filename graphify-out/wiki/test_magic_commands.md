# test magic commands

> 168 nodes

## Key Concepts

- **AliasStorage** (229 connections) — `server/alias_storage.py`
- **test_magic_commands.py** (49 connections) — `server/tests/unit/commands/test_magic_commands.py`
- **MagicCommandHandler** (34 connections) — `server/commands/magic_commands.py`
- **magic_commands.py** (26 connections) — `server/commands/magic_commands.py`
- **Any** (20 connections)
- **SpellCommandError** (12 connections) — `server/commands/magic_commands.py`
- **handle_cast_command()** (9 connections) — `server/commands/magic_commands.py`
- **handle_spells_command()** (9 connections) — `server/commands/magic_commands.py`
- **handle_spell_command()** (9 connections) — `server/commands/magic_commands.py`
- **handle_learn_command()** (9 connections) — `server/commands/magic_commands.py`
- **handle_stop_command()** (9 connections) — `server/commands/magic_commands.py`
- **._get_alias_file_path()** (8 connections) — `server/alias_storage.py`
- **.get_player_aliases()** (8 connections) — `server/alias_storage.py`
- **.save_player_aliases()** (7 connections) — `server/alias_storage.py`
- **.create_alias()** (7 connections) — `server/alias_storage.py`
- **._validate_alias_payload()** (7 connections) — `server/alias_storage.py`
- **.handle_cast_command()** (7 connections) — `server/commands/magic_commands.py`
- **._load_alias_data()** (6 connections) — `server/alias_storage.py`
- **._save_alias_data()** (6 connections) — `server/alias_storage.py`
- **.add_alias()** (6 connections) — `server/alias_storage.py`
- **._build_cast_response()** (6 connections) — `server/commands/magic_commands.py`
- **._interrupt_rest_for_cast()** (6 connections) — `server/commands/magic_commands.py`
- **.handle_spell_command()** (6 connections) — `server/commands/magic_commands.py`
- **.handle_learn_command()** (6 connections) — `server/commands/magic_commands.py`
- **._resolve_spell_context()** (5 connections) — `server/commands/magic_commands.py`
- *... and 143 more nodes in this community*

## Relationships

- [Any](Any.md) (27 shared connections)
- [message handler factory](message_handler_factory.md) (17 shared connections)
- [Player Position Service](Player_Position_Service.md) (15 shared connections)
- [CombatService](CombatService.md) (15 shared connections)
- [check alias safety()](check_alias_safety%28%29.md) (14 shared connections)
- [DropResolved](DropResolved.md) (11 shared connections)
- [websocket handler app state](websocket_handler_app_state.md) (10 shared connections)
- [.check and interrupt rest()](check_and_interrupt_rest%28%29.md) (9 shared connections)
- [test command factories inventory](test_command_factories_inventory.md) (7 shared connections)
- [CommandHandler](CommandHandler.md) (7 shared connections)
- [test alias storage](test_alias_storage.md) (6 shared connections)
- [AuthSlice](AuthSlice.md) (5 shared connections)

## Source Files

- `server/alias_storage.py`
- `server/commands/magic_commands.py`
- `server/tests/unit/commands/test_magic_commands.py`

## Audit Trail

- EXTRACTED: 712 (94%)
- INFERRED: 48 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*