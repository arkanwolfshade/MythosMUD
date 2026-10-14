# asyncio

> 17 nodes

## Key Concepts

- **asyncio** (29 connections)
- **test_handle_cast_command_wrapper_no_magic_service()** (4 connections) — `server/tests/unit/commands/test_magic_commands.py`
- **test_handle_spells_command_wrapper_no_spell_registry()** (4 connections) — `server/tests/unit/commands/test_magic_commands.py`
- **test_announce_spell_cast_no_chat_service()** (3 connections) — `server/tests/unit/commands/test_magic_commands.py`
- **test_handle_cast_command_blocked_when_incapacitated()** (3 connections) — `server/tests/unit/commands/test_magic_commands.py`
- **test_handle_cast_command_cast_failure()** (3 connections) — `server/tests/unit/commands/test_magic_commands.py`
- **test_handle_cast_command_no_player()** (3 connections) — `server/tests/unit/commands/test_magic_commands.py`
- **test_handle_learn_command_no_service()** (3 connections) — `server/tests/unit/commands/test_magic_commands.py`
- **test_handle_learn_command_no_spell_name()** (3 connections) — `server/tests/unit/commands/test_magic_commands.py`
- **Test cast command when player is not found.** (1 connections) — `server/tests/unit/commands/test_magic_commands.py`
- **Cast command returns incapacitated message when player has 0 to -9 DP (prone,…** (1 connections) — `server/tests/unit/commands/test_magic_commands.py`
- **Test cast command when casting fails.** (1 connections) — `server/tests/unit/commands/test_magic_commands.py`
- **Test learn command when spell learning service is not available.** (1 connections) — `server/tests/unit/commands/test_magic_commands.py`
- **Test learn command when no spell name is provided.** (1 connections) — `server/tests/unit/commands/test_magic_commands.py`
- **Test announce spell cast when chat service is not available.** (1 connections) — `server/tests/unit/commands/test_magic_commands.py`
- **Test handle_cast_command wrapper when magic service is not available.** (1 connections) — `server/tests/unit/commands/test_magic_commands.py`
- **Test handle_spells_command wrapper when spell registry is not available.** (1 connections) — `server/tests/unit/commands/test_magic_commands.py`

## Relationships

- [test_magic_commands.py](test_magic_commands.py.md) (13 shared connections)
- [MagicCommandHandler](MagicCommandHandler.md) (2 shared connections)
- [test_announce_spell_cast_no_player_id](test_announce_spell_cast_no_player_id.md) (1 shared connections)
- [test_handle_cast_command_success](test_handle_cast_command_success.md) (1 shared connections)
- [test_handle_cast_command_with_target](test_handle_cast_command_with_target.md) (1 shared connections)
- [test_handle_learn_command_no_player](test_handle_learn_command_no_player.md) (1 shared connections)
- [test_handle_learn_command_success](test_handle_learn_command_success.md) (1 shared connections)
- [test_handle_learn_command_with_corruption](test_handle_learn_command_with_corruption.md) (1 shared connections)
- [test_handle_learn_command_wrapper_success](test_handle_learn_command_wrapper_success.md) (1 shared connections)
- [test_handle_spell_command_no_player](test_handle_spell_command_no_player.md) (1 shared connections)
- [test_handle_spell_command_spell_not_found](test_handle_spell_command_spell_not_found.md) (1 shared connections)
- [test_handle_spell_command_success](test_handle_spell_command_success.md) (1 shared connections)

## Source Files

- `server/tests/unit/commands/test_magic_commands.py`

## Audit Trail

- EXTRACTED: 47 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*