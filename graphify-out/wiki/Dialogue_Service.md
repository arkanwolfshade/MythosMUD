# Dialogue Service

> 48 nodes

## Key Concepts

- **DialogueService** (18 connections) — `server/game/dialogue/dialogue_service.py`
- **dialogue_service.py** (17 connections) — `server/game/dialogue/dialogue_service.py`
- **test_dialogue_service.py** (14 connections) — `server/tests/unit/game/test_dialogue_service.py`
- **DialoguePrompt** (12 connections) — `server/game/dialogue/dialogue_service.py`
- **DialogueTree** (12 connections) — `server/schemas/dialogue/dialogue_tree.py`
- **._present_node()** (10 connections) — `server/game/dialogue/dialogue_service.py`
- **.choose_option()** (9 connections) — `server/game/dialogue/dialogue_service.py`
- **UUID** (8 connections)
- **DialogueNode** (7 connections) — `server/schemas/dialogue/dialogue_tree.py`
- **.clear_cursor()** (7 connections) — `server/game/dialogue/dialogue_service.py`
- **.get_cursor()** (6 connections) — `server/game/dialogue/dialogue_service.py`
- **._load_tree_or_fade()** (6 connections) — `server/game/dialogue/dialogue_service.py`
- **reset_dialogue_service_for_tests()** (6 connections) — `server/game/dialogue/dialogue_service.py`
- **schemas/dialogue/__init__.py** (6 connections) — `server/schemas/dialogue/__init__.py`
- **._player_key()** (5 connections) — `server/game/dialogue/dialogue_service.py`
- **.start_with_npc()** (5 connections) — `server/game/dialogue/dialogue_service.py`
- **test_dialogue_service_start_and_choose()** (5 connections) — `server/tests/unit/game/test_dialogue_service.py`
- **DialogueCursor** (4 connections) — `server/game/dialogue/dialogue_service.py`
- **._invalid_option_message()** (4 connections) — `server/game/dialogue/dialogue_service.py`
- **test_dialogue_service_choose_without_cursor()** (4 connections) — `server/tests/unit/game/test_dialogue_service.py`
- **.validate_graph()** (3 connections) — `server/schemas/dialogue/dialogue_tree.py`
- **test_dialogue_tree_rejects_empty_string_next()** (2 connections) — `server/tests/unit/game/test_dialogue_service.py`
- **test_dialogue_tree_rejects_missing_start()** (2 connections) — `server/tests/unit/game/test_dialogue_service.py`
- **test_dialogue_tree_rejects_unknown_next()** (2 connections) — `server/tests/unit/game/test_dialogue_service.py`
- **asyncio** (2 connections)
- *... and 23 more nodes in this community*

## Relationships

- [Talk Command](Talk_Command.md) (16 shared connections)
- [NPC Definitions API](NPC_Definitions_API.md) (9 shared connections)
- [Dialogue Definition Repository](Dialogue_Definition_Repository.md) (4 shared connections)
- [Npc Admin](Npc_Admin.md) (2 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (2 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)
- [Command Aliases](Command_Aliases.md) (1 shared connections)

## Source Files

- `server/game/dialogue/dialogue_service.py`
- `server/schemas/dialogue/__init__.py`
- `server/schemas/dialogue/dialogue_tree.py`
- `server/tests/unit/game/test_dialogue_service.py`

## Audit Trail

- EXTRACTED: 112 (96%)
- INFERRED: 5 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*