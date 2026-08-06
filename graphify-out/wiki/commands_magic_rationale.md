# commands magic rationale

> 127 nodes

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
- *... and 102 more nodes in this community*

## Relationships

- [commands npc admin](commands_npc_admin.md) (15 shared connections)
- [player respawn event](player_respawn_event.md) (7 shared connections)
- [character creation service](character_creation_service.md) (6 shared connections)
- [rest grace period](rest_grace_period.md) (6 shared connections)
- [persistence core infrastructure](persistence_core_infrastructure.md) (6 shared connections)
- [npc combat player](npc_combat_player.md) (5 shared connections)
- [chat service game](chat_service_game.md) (3 shared connections)
- [container persistence rationale](container_persistence_rationale.md) (3 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (2 shared connections)
- [panels domPurifyClient chat](panels_domPurifyClient_chat.md) (2 shared connections)
- [chat game message](chat_game_message.md) (1 shared connections)
- [lucidity active service](lucidity_active_service.md) (1 shared connections)

## Source Files

- `server/commands/magic_commands.py`
- `server/tests/unit/commands/test_magic_commands.py`
- `server/tests/unit/game/magic/test_magic_service.py`

## Audit Trail

- EXTRACTED: 389 (92%)
- INFERRED: 34 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*