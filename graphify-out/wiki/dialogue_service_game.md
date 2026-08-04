# dialogue service game

> 69 nodes

## Key Concepts

- **DialogueTree** (19 connections) — `server/schemas/dialogue/dialogue_tree.py`
- **DialogueService** (18 connections) — `server/game/dialogue/dialogue_service.py`
- **dialogue_service.py** (17 connections) — `server/game/dialogue/dialogue_service.py`
- **test_talk_command.py** (14 connections) — `server/tests/unit/commands/test_talk_command.py`
- **DialoguePrompt** (13 connections) — `server/game/dialogue/dialogue_service.py`
- **test_dialogue_service.py** (12 connections) — `server/tests/unit/game/test_dialogue_service.py`
- **._present_node()** (10 connections) — `server/game/dialogue/dialogue_service.py`
- **.choose_option()** (9 connections) — `server/game/dialogue/dialogue_service.py`
- **UUID** (8 connections)
- **__init__.py** (7 connections) — `server/game/dialogue/__init__.py`
- **.clear_cursor()** (7 connections) — `server/game/dialogue/dialogue_service.py`
- **.get_cursor()** (6 connections) — `server/game/dialogue/dialogue_service.py`
- **.start_with_npc()** (6 connections) — `server/game/dialogue/dialogue_service.py`
- **._load_tree_or_fade()** (6 connections) — `server/game/dialogue/dialogue_service.py`
- **reset_dialogue_service_for_tests()** (6 connections) — `server/game/dialogue/dialogue_service.py`
- **DialogueNode** (6 connections) — `server/schemas/dialogue/dialogue_tree.py`
- **DialogueCursor** (5 connections) — `server/game/dialogue/dialogue_service.py`
- **._player_key()** (5 connections) — `server/game/dialogue/dialogue_service.py`
- **__init__.py** (5 connections) — `server/schemas/dialogue/__init__.py`
- **dialogue_tree.py** (5 connections) — `server/schemas/dialogue/dialogue_tree.py`
- **._invalid_option_message()** (4 connections) — `server/game/dialogue/dialogue_service.py`
- **DialogueOption** (4 connections) — `server/schemas/dialogue/dialogue_tree.py`
- **test_dialogue_tree_schema_rejects_bad_start()** (4 connections) — `server/tests/unit/api/test_dialogue_definitions_api.py`
- **test_dialogue_tree_rejects_unknown_next()** (4 connections) — `server/tests/unit/game/test_dialogue_service.py`
- **test_dialogue_tree_rejects_empty_string_next()** (4 connections) — `server/tests/unit/game/test_dialogue_service.py`
- *... and 44 more nodes in this community*

## Relationships

- [player cache rationale](player_cache_rationale.md) (10 shared connections)
- [Database Config](Database_Config.md) (6 shared connections)
- [player preferences services](player_preferences_services.md) (6 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (4 shared connections)
- [Loot Generation](Loot_Generation.md) (2 shared connections)

## Source Files

- `server/game/dialogue/__init__.py`
- `server/game/dialogue/dialogue_service.py`
- `server/schemas/dialogue/__init__.py`
- `server/schemas/dialogue/dialogue_tree.py`
- `server/tests/unit/api/test_dialogue_definitions_api.py`
- `server/tests/unit/commands/test_talk_command.py`
- `server/tests/unit/game/test_dialogue_service.py`

## Audit Trail

- EXTRACTED: 257 (97%)
- INFERRED: 7 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*