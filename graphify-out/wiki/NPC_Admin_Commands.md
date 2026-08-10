# NPC Admin Commands

> 12 nodes

## Key Concepts

- **test_magic_commands.py** (49 connections) — `server/tests/unit/commands/test_magic_commands.py`
- **mock_magic_service()** (2 connections) — `server/tests/unit/commands/test_magic_commands.py`
- **mock_player()** (2 connections) — `server/tests/unit/commands/test_magic_commands.py`
- **mock_chat_service()** (2 connections) — `server/tests/unit/commands/test_magic_commands.py`
- **test_handle_cast_command_success()** (2 connections) — `server/tests/unit/commands/test_magic_commands.py`
- **test_handle_spells_command_no_player()** (2 connections) — `server/tests/unit/commands/test_magic_commands.py`
- **Unit tests for magic commands.  Tests the /cast, /spells, /spell, /learn, and /s** (1 connections) — `server/tests/unit/commands/test_magic_commands.py`
- **Create a mock magic service.** (1 connections) — `server/tests/unit/commands/test_magic_commands.py`
- **Create a mock player (healthy by default for cast/combat checks).** (1 connections) — `server/tests/unit/commands/test_magic_commands.py`
- **Create a mock chat service.** (1 connections) — `server/tests/unit/commands/test_magic_commands.py`
- **Test cast command success.** (1 connections) — `server/tests/unit/commands/test_magic_commands.py`
- **Test spells command when player is not found.** (1 connections) — `server/tests/unit/commands/test_magic_commands.py`

## Relationships

- [Client Event Store](Client_Event_Store.md) (7 shared connections)
- [Upgrade Archive Dependency](Upgrade_Archive_Dependency.md) (5 shared connections)
- [E 2 E Whisper System](E_2_E_Whisper_System.md) (1 shared connections)
- [Game Profession Service](Game_Profession_Service.md) (1 shared connections)
- [Components Map Roommapeditor](Components_Map_Roommapeditor.md) (1 shared connections)
- [E 2 E Scenarios Lucidity](E_2_E_Scenarios_Lucidity.md) (1 shared connections)
- [test_process_combined_rows_with_exits](test_process_combined_rows_with_exits.md) (1 shared connections)
- [test_process_exits_for_room_no_direction](test_process_exits_for_room_no_direction.md) (1 shared connections)
- [test_process_exits_for_room_multiple_exits](test_process_exits_for_room_multiple_exits.md) (1 shared connections)
- [Persistence Item Repositories](Persistence_Item_Repositories.md) (1 shared connections)
- [Cursor Plans First](Cursor_Plans_First.md) (1 shared connections)
- [Lucidity Utc Now](Lucidity_Utc_Now.md) (1 shared connections)

## Source Files

- `server/tests/unit/commands/test_magic_commands.py`

## Audit Trail

- EXTRACTED: 65 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*