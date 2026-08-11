# NPC Admin Commands

> 129 nodes

## Key Concepts

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
- *... and 104 more nodes in this community*

## Relationships

- [Combat Attack Service](Combat_Attack_Service.md) (15 shared connections)
- [Player Schema Converter](Player_Schema_Converter.md) (14 shared connections)
- [Chat NATS Publisher](Chat_NATS_Publisher.md) (11 shared connections)
- [Client Event Store](Client_Event_Store.md) (5 shared connections)
- [Player State Factories](Player_State_Factories.md) (5 shared connections)
- [Chat Mute Admin API](Chat_Mute_Admin_API.md) (3 shared connections)
- [Who Command Tests](Who_Command_Tests.md) (1 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (1 shared connections)

## Source Files

- `server/commands/magic_commands.py`
- `server/tests/unit/commands/test_magic_commands.py`

## Audit Trail

- EXTRACTED: 393 (94%)
- INFERRED: 26 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*