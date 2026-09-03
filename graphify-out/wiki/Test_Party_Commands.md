# Test Party Commands

> 54 nodes

## Key Concepts

- **test_party_commands.py** (23 connections) — `server/tests/unit/commands/test_party_commands.py`
- **party_commands.py** (21 connections) — `server/commands/party_commands.py`
- **handle_party_command()** (20 connections) — `server/commands/party_commands.py`
- **asyncio** (13 connections)
- **_party_request()** (11 connections) — `server/tests/unit/commands/test_party_commands.py`
- **Any** (9 connections)
- **schemas/shared/__init__.py** (9 connections) — `server/schemas/shared/__init__.py`
- **_handle_party_chat()** (7 connections) — `server/commands/party_commands.py`
- **_get_member_display()** (6 connections) — `server/commands/party_commands.py`
- **_get_party_command_context()** (6 connections) — `server/commands/party_commands.py`
- **_handle_party_invite()** (5 connections) — `server/commands/party_commands.py`
- **_handle_party_kick()** (5 connections) — `server/commands/party_commands.py`
- **_handle_party_leave()** (5 connections) — `server/commands/party_commands.py`
- **_handle_party_list()** (5 connections) — `server/commands/party_commands.py`
- **test_handle_party_command_invite_no_target()** (5 connections) — `server/tests/unit/commands/test_party_commands.py`
- **test_handle_party_command_invite_success()** (5 connections) — `server/tests/unit/commands/test_party_commands.py`
- **test_handle_party_command_kick_not_leader()** (5 connections) — `server/tests/unit/commands/test_party_commands.py`
- **test_handle_party_command_leave()** (5 connections) — `server/tests/unit/commands/test_party_commands.py`
- **test_handle_party_command_list_not_in_party()** (5 connections) — `server/tests/unit/commands/test_party_commands.py`
- **test_handle_party_command_list_with_members()** (5 connections) — `server/tests/unit/commands/test_party_commands.py`
- **test_handle_party_command_player_not_in_game()** (5 connections) — `server/tests/unit/commands/test_party_commands.py`
- **test_handle_party_command_unknown_subcommand()** (5 connections) — `server/tests/unit/commands/test_party_commands.py`
- **_get_container()** (4 connections) — `server/commands/party_commands.py`
- **test_get_member_display_invalid_uuid()** (4 connections) — `server/tests/unit/commands/test_party_commands.py`
- **test_handle_party_chat_no_party()** (4 connections) — `server/tests/unit/commands/test_party_commands.py`
- *... and 29 more nodes in this community*

## Relationships

- [Test Target Resolution Service](Test_Target_Resolution_Service.md) (5 shared connections)
- [Test Npc Admin Commands](Test_Npc_Admin_Commands.md) (2 shared connections)
- [Combat Spell Effects (Flee)](Combat_Spell_Effects_Flee.md) (2 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (2 shared connections)
- [NPC Definitions API](NPC_Definitions_API.md) (2 shared connections)
- [Test Rescue Commands](Test_Rescue_Commands.md) (1 shared connections)
- [Test Position Commands](Test_Position_Commands.md) (1 shared connections)
- [Alias Storage](Alias_Storage.md) (1 shared connections)
- [Test Command Parser](Test_Command_Parser.md) (1 shared connections)
- [Test Combat Handler](Test_Combat_Handler.md) (1 shared connections)
- [Test Inventory Helpers Extended](Test_Inventory_Helpers_Extended.md) (1 shared connections)
- [Test Follow Commands](Test_Follow_Commands.md) (1 shared connections)

## Source Files

- `server/commands/party_commands.py`
- `server/schemas/shared/__init__.py`
- `server/tests/unit/commands/test_party_commands.py`

## Audit Trail

- EXTRACTED: 128 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*