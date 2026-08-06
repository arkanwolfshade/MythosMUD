# dialogue service game

> 63 nodes

## Key Concepts

- **DialogueService** (18 connections) — `server/game/dialogue/dialogue_service.py`
- **dialogue_service.py** (17 connections) — `server/game/dialogue/dialogue_service.py`
- **test_talk_command.py** (14 connections) — `server/tests/unit/commands/test_talk_command.py`
- **DialoguePrompt** (13 connections) — `server/game/dialogue/dialogue_service.py`
- **test_dialogue_service.py** (12 connections) — `server/tests/unit/game/test_dialogue_service.py`
- **._present_node()** (10 connections) — `server/game/dialogue/dialogue_service.py`
- **.choose_option()** (9 connections) — `server/game/dialogue/dialogue_service.py`
- **get_dialogue_service()** (9 connections) — `server/game/dialogue/dialogue_service.py`
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
- **test_dialogue_tree_rejects_unknown_next()** (4 connections) — `server/tests/unit/game/test_dialogue_service.py`
- **test_dialogue_tree_rejects_empty_string_next()** (4 connections) — `server/tests/unit/game/test_dialogue_service.py`
- **test_dialogue_tree_rejects_missing_start()** (4 connections) — `server/tests/unit/game/test_dialogue_service.py`
- *... and 38 more nodes in this community*

## Relationships

- [persistence container rationale](persistence_container_rationale.md) (11 shared connections)
- [occupants npc commands](occupants_npc_commands.md) (10 shared connections)
- [message broadcaster realtime](message_broadcaster_realtime.md) (6 shared connections)
- [command inventory models](command_inventory_models.md) (3 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (2 shared connections)
- [commands command rationale](commands_command_rationale.md) (2 shared connections)

## Source Files

- `server/game/dialogue/__init__.py`
- `server/game/dialogue/dialogue_service.py`
- `server/schemas/dialogue/__init__.py`
- `server/schemas/dialogue/dialogue_tree.py`
- `server/tests/unit/commands/test_talk_command.py`
- `server/tests/unit/game/test_dialogue_service.py`

## Audit Trail

- EXTRACTED: 236 (98%)
- INFERRED: 6 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*