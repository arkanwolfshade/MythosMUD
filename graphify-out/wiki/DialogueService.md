# DialogueService

> 46 nodes

## Key Concepts

- **DialogueService** (18 connections) — `server/game/dialogue/dialogue_service.py`
- **dialogue_service.py** (17 connections) — `server/game/dialogue/dialogue_service.py`
- **DialogueTree** (13 connections) — `server/schemas/dialogue/dialogue_tree.py`
- **DialoguePrompt** (12 connections) — `server/game/dialogue/dialogue_service.py`
- **test_dialogue_service.py** (12 connections) — `server/tests/unit/game/test_dialogue_service.py`
- **._present_node()** (10 connections) — `server/game/dialogue/dialogue_service.py`
- **.choose_option()** (9 connections) — `server/game/dialogue/dialogue_service.py`
- **UUID** (8 connections)
- **.clear_cursor()** (7 connections) — `server/game/dialogue/dialogue_service.py`
- **.get_cursor()** (6 connections) — `server/game/dialogue/dialogue_service.py`
- **._load_tree_or_fade()** (6 connections) — `server/game/dialogue/dialogue_service.py`
- **reset_dialogue_service_for_tests()** (6 connections) — `server/game/dialogue/dialogue_service.py`
- **._player_key()** (5 connections) — `server/game/dialogue/dialogue_service.py`
- **.start_with_npc()** (5 connections) — `server/game/dialogue/dialogue_service.py`
- **test_dialogue_service_start_and_choose()** (5 connections) — `server/tests/unit/game/test_dialogue_service.py`
- **DialogueCursor** (4 connections) — `server/game/dialogue/dialogue_service.py`
- **._invalid_option_message()** (4 connections) — `server/game/dialogue/dialogue_service.py`
- **test_dialogue_service_choose_without_cursor()** (4 connections) — `server/tests/unit/game/test_dialogue_service.py`
- **.validate_graph()** (3 connections) — `server/schemas/dialogue/dialogue_tree.py`
- **test_dialogue_tree_graph_validation_still_runs()** (3 connections) — `server/tests/unit/schemas/test_dialogue_tree.py`
- **test_dialogue_tree_rejects_empty_string_next()** (2 connections) — `server/tests/unit/game/test_dialogue_service.py`
- **test_dialogue_tree_rejects_missing_start()** (2 connections) — `server/tests/unit/game/test_dialogue_service.py`
- **test_dialogue_tree_rejects_unknown_next()** (2 connections) — `server/tests/unit/game/test_dialogue_service.py`
- **asyncio** (2 connections)
- **model_validator** (1 connections)
- *... and 21 more nodes in this community*

## Relationships

- [talk_command.py](talk_command.py.md) (16 shared connections)
- [PlayerService](PlayerService.md) (9 shared connections)
- [get_session_maker](get_session_maker.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)

## Source Files

- `server/game/dialogue/dialogue_service.py`
- `server/schemas/dialogue/dialogue_tree.py`
- `server/tests/unit/game/test_dialogue_service.py`
- `server/tests/unit/schemas/test_dialogue_tree.py`

## Audit Trail

- EXTRACTED: 104 (95%)
- INFERRED: 5 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*