# dialogue service game

> 49 nodes

## Key Concepts

- **DialogueTree** (17 connections) — `server/schemas/dialogue/dialogue_tree.py`
- **DialogueService** (16 connections) — `server/game/dialogue/dialogue_service.py`
- **dialogue_service.py** (15 connections) — `server/game/dialogue/dialogue_service.py`
- **test_dialogue_service.py** (11 connections) — `server/tests/unit/game/test_dialogue_service.py`
- **._present_node()** (10 connections) — `server/game/dialogue/dialogue_service.py`
- **DialoguePrompt** (9 connections) — `server/game/dialogue/dialogue_service.py`
- **get_dialogue_service()** (9 connections) — `server/game/dialogue/dialogue_service.py`
- **.choose_option()** (8 connections) — `server/game/dialogue/dialogue_service.py`
- **__init__.py** (7 connections) — `server/game/dialogue/__init__.py`
- **format_dialogue_prompt()** (7 connections) — `server/game/dialogue/dialogue_service.py`
- **UUID** (7 connections)
- **.clear_cursor()** (6 connections) — `server/game/dialogue/dialogue_service.py`
- **.get_cursor()** (6 connections) — `server/game/dialogue/dialogue_service.py`
- **.start_with_npc()** (6 connections) — `server/game/dialogue/dialogue_service.py`
- **reset_dialogue_service_for_tests()** (6 connections) — `server/game/dialogue/dialogue_service.py`
- **DialogueCursor** (5 connections) — `server/game/dialogue/dialogue_service.py`
- **._player_key()** (5 connections) — `server/game/dialogue/dialogue_service.py`
- **test_dialogue_tree_schema_rejects_bad_start()** (4 connections) — `server/tests/unit/api/test_dialogue_definitions_api.py`
- **test_dialogue_tree_rejects_unknown_next()** (4 connections) — `server/tests/unit/game/test_dialogue_service.py`
- **test_dialogue_tree_rejects_missing_start()** (4 connections) — `server/tests/unit/game/test_dialogue_service.py`
- **test_dialogue_service_start_and_choose()** (4 connections) — `server/tests/unit/game/test_dialogue_service.py`
- **test_dialogue_tree_schema_accepts_nav_only()** (3 connections) — `server/tests/unit/api/test_dialogue_definitions_api.py`
- **test_format_dialogue_prompt_numbers_options()** (3 connections) — `server/tests/unit/game/test_dialogue_service.py`
- **test_dialogue_service_choose_without_cursor()** (3 connections) — `server/tests/unit/game/test_dialogue_service.py`
- **.__init__()** (2 connections) — `server/game/dialogue/dialogue_service.py`
- *... and 24 more nodes in this community*

## Relationships

- [message broadcaster realtime](message_broadcaster_realtime.md) (7 shared connections)
- [Database Config](Database_Config.md) (6 shared connections)
- [admin auth service](admin_auth_service.md) (5 shared connections)
- [world loader room](world_loader_room.md) (3 shared connections)
- [command inventory models](command_inventory_models.md) (3 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [commands command rationale](commands_command_rationale.md) (2 shared connections)

## Source Files

- `server/game/dialogue/__init__.py`
- `server/game/dialogue/dialogue_service.py`
- `server/schemas/dialogue/dialogue_tree.py`
- `server/tests/unit/api/test_dialogue_definitions_api.py`
- `server/tests/unit/game/test_dialogue_service.py`

## Audit Trail

- EXTRACTED: 196 (97%)
- INFERRED: 6 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*