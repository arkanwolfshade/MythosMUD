# server game dialogue dialogue service

> 61 nodes

## Key Concepts

- **DialogueService** (18 connections) — `server/game/dialogue/dialogue_service.py`
- **dialogue_service.py** (17 connections) — `server/game/dialogue/dialogue_service.py`
- **test_dialogue_service.py** (14 connections) — `server/tests/unit/game/test_dialogue_service.py`
- **DialoguePrompt** (12 connections) — `server/game/dialogue/dialogue_service.py`
- **DialogueTree** (11 connections) — `server/schemas/dialogue/dialogue_tree.py`
- **._present_node()** (10 connections) — `server/game/dialogue/dialogue_service.py`
- **.choose_option()** (9 connections) — `server/game/dialogue/dialogue_service.py`
- **get_dialogue_service()** (9 connections) — `server/game/dialogue/dialogue_service.py`
- **game/dialogue/__init__.py** (9 connections) — `server/game/dialogue/__init__.py`
- **UUID** (8 connections)
- **.clear_cursor()** (7 connections) — `server/game/dialogue/dialogue_service.py`
- **format_dialogue_prompt()** (7 connections) — `server/game/dialogue/dialogue_service.py`
- **DialogueNode** (6 connections) — `server/schemas/dialogue/dialogue_tree.py`
- **.get_cursor()** (6 connections) — `server/game/dialogue/dialogue_service.py`
- **._load_tree_or_fade()** (6 connections) — `server/game/dialogue/dialogue_service.py`
- **reset_dialogue_service_for_tests()** (6 connections) — `server/game/dialogue/dialogue_service.py`
- **dialogue_tree.py** (6 connections) — `server/schemas/dialogue/dialogue_tree.py`
- **schemas/dialogue/__init__.py** (6 connections) — `server/schemas/dialogue/__init__.py`
- **._player_key()** (5 connections) — `server/game/dialogue/dialogue_service.py`
- **.start_with_npc()** (5 connections) — `server/game/dialogue/dialogue_service.py`
- **test_dialogue_service_start_and_choose()** (5 connections) — `server/tests/unit/game/test_dialogue_service.py`
- **DialogueCursor** (4 connections) — `server/game/dialogue/dialogue_service.py`
- **DialogueOption** (4 connections) — `server/schemas/dialogue/dialogue_tree.py`
- **._invalid_option_message()** (4 connections) — `server/game/dialogue/dialogue_service.py`
- **test_dialogue_service_choose_without_cursor()** (4 connections) — `server/tests/unit/game/test_dialogue_service.py`
- *... and 36 more nodes in this community*

## Relationships

- [server commands quest commands npc](server_commands_quest_commands_npc.md) (13 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (5 shared connections)
- [server game dialogue dialogue service](server_game_dialogue_dialogue_service.md) (3 shared connections)
- [server commands go command](server_commands_go_command.md) (3 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (3 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/game/dialogue/__init__.py`
- `server/game/dialogue/dialogue_service.py`
- `server/schemas/dialogue/__init__.py`
- `server/schemas/dialogue/dialogue_tree.py`
- `server/tests/unit/game/test_dialogue_service.py`

## Audit Trail

- EXTRACTED: 130 (96%)
- INFERRED: 6 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*