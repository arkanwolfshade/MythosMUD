# commands magic rationale

> 125 nodes

## Key Concepts

- **test_magic_commands.py** (49 connections) — `server/tests/unit/commands/test_magic_commands.py`
- **MagicCommandHandler** (34 connections) — `server/commands/magic_commands.py`
- **magic_commands.py** (26 connections) — `server/commands/magic_commands.py`
- **Any** (20 connections)
- **handle_cast_command()** (8 connections) — `server/commands/magic_commands.py`
- **handle_spells_command()** (8 connections) — `server/commands/magic_commands.py`
- **handle_spell_command()** (8 connections) — `server/commands/magic_commands.py`
- **handle_learn_command()** (8 connections) — `server/commands/magic_commands.py`
- **handle_stop_command()** (8 connections) — `server/commands/magic_commands.py`
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
- **.handle_stop_command()** (4 connections) — `server/commands/magic_commands.py`
- **MockSchool** (4 connections) — `server/tests/unit/commands/test_magic_commands.py`
- *... and 100 more nodes in this community*

## Relationships

- [commands alias rationale](commands_alias_rationale.md) (20 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (16 shared connections)
- [rest grace period](rest_grace_period.md) (5 shared connections)
- [chat service game](chat_service_game.md) (2 shared connections)
- [NATS Messaging](NATS_Messaging.md) (2 shared connections)
- [chat game message](chat_game_message.md) (1 shared connections)

## Source Files

- `server/commands/magic_commands.py`
- `server/tests/unit/commands/test_magic_commands.py`

## Audit Trail

- EXTRACTED: 383 (96%)
- INFERRED: 15 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*