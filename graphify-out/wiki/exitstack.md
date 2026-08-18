# exitstack

> 77 nodes

## Key Concepts

- **quest_commands.py** (40 connections) — `server/commands/quest_commands.py`
- **test_quest_commands.py** (21 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **handle_quest_command()** (20 connections) — `server/commands/quest_commands.py`
- **Any** (18 connections)
- **handle_journal_command()** (14 connections) — `server/commands/quest_commands.py`
- **asyncio** (13 connections)
- **_handle_quest_npc_sub()** (11 connections) — `server/commands/quest_commands.py`
- **_resolve_quest_command_context()** (10 connections) — `server/commands/quest_commands.py`
- **resolve_npc_in_player_room()** (9 connections) — `server/commands/quest_commands.py`
- **_get_quest_service()** (7 connections) — `server/commands/quest_commands.py`
- **npc_definition_id()** (7 connections) — `server/commands/quest_commands.py`
- **_enter_quest_command_patches()** (7 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **_active_npc_ids_in_room()** (6 connections) — `server/commands/quest_commands.py`
- **_emit_npc_lines_for_results()** (6 connections) — `server/commands/quest_commands.py`
- **_quest_command_ready()** (6 connections) — `server/commands/quest_commands.py`
- **_resolve_player_id()** (6 connections) — `server/commands/quest_commands.py`
- **test_quest_ask_npc_not_in_room()** (6 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **test_quest_ask_success()** (6 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **test_quest_turnin_npc_not_in_room()** (6 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **test_quest_turnin_success()** (6 connections) — `server/tests/unit/commands/test_quest_commands.py`
- **UUID** (6 connections)
- **_format_one_quest_entry()** (5 connections) — `server/commands/quest_commands.py`
- **_format_quest_log()** (5 connections) — `server/commands/quest_commands.py`
- **_get_container_and_persistence()** (5 connections) — `server/commands/quest_commands.py`
- **_handle_quest_abandon()** (5 connections) — `server/commands/quest_commands.py`
- *... and 52 more nodes in this community*

## Relationships

- [server commands look npc](server_commands_look_npc.md) (9 shared connections)
- [server container bundles chat chatbundle](server_container_bundles_chat_chatbundle.md) (9 shared connections)
- [server commands admin commands](server_commands_admin_commands.md) (6 shared connections)
- [server commands talk command](server_commands_talk_command.md) (5 shared connections)
- [server game quest quest service](server_game_quest_quest_service.md) (3 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (3 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [server tests unit game test](server_tests_unit_game_test.md) (1 shared connections)
- [server api admin dialogue definitions](server_api_admin_dialogue_definitions.md) (1 shared connections)
- [aliaspayload](aliaspayload.md) (1 shared connections)
- [server game quest collect inventory](server_game_quest_collect_inventory.md) (1 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (1 shared connections)

## Source Files

- `server/commands/quest_commands.py`
- `server/tests/unit/commands/test_quest_commands.py`

## Audit Trail

- EXTRACTED: 187 (96%)
- INFERRED: 8 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*