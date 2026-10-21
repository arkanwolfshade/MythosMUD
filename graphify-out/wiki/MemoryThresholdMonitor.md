# MemoryThresholdMonitor

> 62 nodes · cohesion 0.07

## Key Concepts

- **party_commands.py** (26 connections) — `server/commands/party_commands.py`
- **handle_party_command()** (25 connections) — `server/commands/party_commands.py`
- **test_party_commands.py** (25 connections) — `server/tests/unit/commands/test_party_commands.py`
- **asyncio** (16 connections)
- **_party_request()** (14 connections) — `server/tests/unit/commands/test_party_commands.py`
- **Any** (11 connections)
- **_get_party_command_context()** (7 connections) — `server/commands/party_commands.py`
- **_handle_party_chat()** (7 connections) — `server/commands/party_commands.py`
- **_resolve_target_for_party_action()** (7 connections) — `server/commands/party_commands.py`
- **_get_member_display()** (6 connections) — `server/commands/party_commands.py`
- **_handle_party_invite()** (6 connections) — `server/commands/party_commands.py`
- **_handle_party_kick()** (6 connections) — `server/commands/party_commands.py`
- **_handle_party_leave()** (5 connections) — `server/commands/party_commands.py`
- **test_handle_party_command_invite_no_player_service()** (5 connections) — `server/tests/unit/commands/test_party_commands.py`
- **test_handle_party_command_invite_no_target()** (5 connections) — `server/tests/unit/commands/test_party_commands.py`
- **test_handle_party_command_invite_success()** (5 connections) — `server/tests/unit/commands/test_party_commands.py`
- **test_handle_party_command_kick_not_leader()** (5 connections) — `server/tests/unit/commands/test_party_commands.py`
- **test_handle_party_command_kick_success()** (5 connections) — `server/tests/unit/commands/test_party_commands.py`
- **test_handle_party_command_kick_target_resolve_failed()** (5 connections) — `server/tests/unit/commands/test_party_commands.py`
- **test_handle_party_command_leave()** (5 connections) — `server/tests/unit/commands/test_party_commands.py`
- **test_handle_party_command_list_not_in_party()** (5 connections) — `server/tests/unit/commands/test_party_commands.py`
- **test_handle_party_command_list_with_members()** (5 connections) — `server/tests/unit/commands/test_party_commands.py`
- **test_handle_party_command_player_not_in_game()** (5 connections) — `server/tests/unit/commands/test_party_commands.py`
- **test_handle_party_command_unknown_subcommand()** (5 connections) — `server/tests/unit/commands/test_party_commands.py`
- **_get_container()** (4 connections) — `server/commands/party_commands.py`
- *... and 37 more nodes in this community*

## Relationships

- [command_parser.py](command_parser.py.md) (10 shared connections)
- [NPCCombatLucidity](NPCCombatLucidity.md) (3 shared connections)
- [InventorySchemaValidationError](InventorySchemaValidationError.md) (2 shared connections)
- [test_user_manager.py](test_user_manager.py.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)
- [ADR-026: Item Catalog Metadata Contracts](ADR-026-_Item_Catalog_Metadata_Contracts.md) (1 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (1 shared connections)
- [CommandFactory](CommandFactory.md) (1 shared connections)
- [.load_room_data](load_room_data.md) (1 shared connections)

## Source Files

- `server/commands/party_commands.py`
- `server/tests/unit/commands/test_party_commands.py`

## Audit Trail

- EXTRACTED: 148 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*