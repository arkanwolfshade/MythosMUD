# Cursor Skills Harden

> 16 nodes

## Key Concepts

- **teach_command.py** (15 connections) — `server/commands/teach_command.py`
- **handle_teach_command()** (14 connections) — `server/commands/teach_command.py`
- **test_teach_command.py** (6 connections) — `server/tests/unit/commands/test_teach_command.py`
- **Any** (5 connections)
- **_get_teach_services()** (4 connections) — `server/commands/teach_command.py`
- **_resolve_npc_teacher()** (4 connections) — `server/commands/teach_command.py`
- **_format_teach_result()** (3 connections) — `server/commands/teach_command.py`
- **test_handle_teach_command()** (3 connections) — `server/tests/unit/commands/test_teach_command.py`
- **test_handle_teach_command_no_target()** (3 connections) — `server/tests/unit/commands/test_teach_command.py`
- **test_handle_teach_command_no_persistence()** (3 connections) — `server/tests/unit/commands/test_teach_command.py`
- **Teach command handler for learning spells from NPC teachers.  This module handle** (1 connections) — `server/commands/teach_command.py`
- **Handle /teach command for learning spells from NPCs.      Usage: /teach <npc_nam** (1 connections) — `server/commands/teach_command.py`
- **Unit tests for teach command handlers.  Tests the teach command functionality.** (1 connections) — `server/tests/unit/commands/test_teach_command.py`
- **Test handle_teach_command() teaches spell to player.** (1 connections) — `server/tests/unit/commands/test_teach_command.py`
- **Test handle_teach_command() handles missing target.** (1 connections) — `server/tests/unit/commands/test_teach_command.py`
- **Test handle_teach_command() handles missing persistence.** (1 connections) — `server/tests/unit/commands/test_teach_command.py`

## Relationships

- [Player Schema Converter](Player_Schema_Converter.md) (4 shared connections)
- [Container Open Events](Container_Open_Events.md) (3 shared connections)
- [Client Event Store](Client_Event_Store.md) (3 shared connections)
- [Look Command Helpers](Look_Command_Helpers.md) (2 shared connections)
- [Inventory Command Models](Inventory_Command_Models.md) (1 shared connections)
- [NPC Death Lifecycle](NPC_Death_Lifecycle.md) (1 shared connections)
- [Character Info Panel Fix](Character_Info_Panel_Fix.md) (1 shared connections)
- [Rate Limiter Utilities](Rate_Limiter_Utilities.md) (1 shared connections)

## Source Files

- `server/commands/teach_command.py`
- `server/tests/unit/commands/test_teach_command.py`

## Audit Trail

- EXTRACTED: 62 (94%)
- INFERRED: 4 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*