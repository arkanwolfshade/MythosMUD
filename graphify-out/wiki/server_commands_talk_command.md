# server commands talk command

> 89 nodes

## Key Concepts

- **talk_command.py** (28 connections) — `server/commands/talk_command.py`
- **DialogueService** (18 connections) — `server/game/dialogue/dialogue_service.py`
- **dialogue_service.py** (17 connections) — `server/game/dialogue/dialogue_service.py`
- **test_talk_command.py** (15 connections) — `server/tests/unit/commands/test_talk_command.py`
- **test_dialogue_service.py** (14 connections) — `server/tests/unit/game/test_dialogue_service.py`
- **handle_talk_command()** (13 connections) — `server/commands/talk_command.py`
- **DialoguePrompt** (12 connections) — `server/game/dialogue/dialogue_service.py`
- **DialogueTree** (11 connections) — `server/schemas/dialogue/dialogue_tree.py`
- **_emit_prompt()** (10 connections) — `server/commands/talk_command.py`
- **._present_node()** (10 connections) — `server/game/dialogue/dialogue_service.py`
- **_talk_with_npc()** (9 connections) — `server/commands/talk_command.py`
- **.choose_option()** (9 connections) — `server/game/dialogue/dialogue_service.py`
- **get_dialogue_service()** (9 connections) — `server/game/dialogue/dialogue_service.py`
- **game/dialogue/__init__.py** (9 connections) — `server/game/dialogue/__init__.py`
- **UUID** (8 connections)
- **_resolve_player_id()** (7 connections) — `server/commands/talk_command.py`
- **_talk_by_option_index()** (7 connections) — `server/commands/talk_command.py`
- **.clear_cursor()** (7 connections) — `server/game/dialogue/dialogue_service.py`
- **format_dialogue_prompt()** (7 connections) — `server/game/dialogue/dialogue_service.py`
- **DialogueNode** (6 connections) — `server/schemas/dialogue/dialogue_tree.py`
- **.get_cursor()** (6 connections) — `server/game/dialogue/dialogue_service.py`
- **._load_tree_or_fade()** (6 connections) — `server/game/dialogue/dialogue_service.py`
- **reset_dialogue_service_for_tests()** (6 connections) — `server/game/dialogue/dialogue_service.py`
- **dialogue_tree.py** (6 connections) — `server/schemas/dialogue/dialogue_tree.py`
- **schemas/dialogue/__init__.py** (6 connections) — `server/schemas/dialogue/__init__.py`
- *... and 64 more nodes in this community*

## Relationships

- [server commands communication commands](server_commands_communication_commands.md) (7 shared connections)
- [exitstack](exitstack.md) (5 shared connections)
- [server commands admin commands](server_commands_admin_commands.md) (4 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (4 shared connections)
- [server game dialogue dialogue service](server_game_dialogue_dialogue_service.md) (3 shared connections)
- [server api admin dialogue definitions](server_api_admin_dialogue_definitions.md) (3 shared connections)
- [server container bundles chat chatbundle](server_container_bundles_chat_chatbundle.md) (3 shared connections)
- [server commands exploration commands](server_commands_exploration_commands.md) (3 shared connections)
- [server alias storage aliasstorage](server_alias_storage_aliasstorage.md) (2 shared connections)
- [claude rules pydantic](claude_rules_pydantic.md) (2 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (2 shared connections)
- [aliaspayload](aliaspayload.md) (1 shared connections)

## Source Files

- `server/commands/talk_command.py`
- `server/game/dialogue/__init__.py`
- `server/game/dialogue/dialogue_service.py`
- `server/schemas/dialogue/__init__.py`
- `server/schemas/dialogue/dialogue_tree.py`
- `server/tests/unit/commands/test_talk_command.py`
- `server/tests/unit/game/test_dialogue_service.py`

## Audit Trail

- EXTRACTED: 205 (97%)
- INFERRED: 6 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*