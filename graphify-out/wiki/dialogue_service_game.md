# dialogue service game

> 62 nodes

## Key Concepts

- **talk_command.py** (26 connections) — `server/commands/talk_command.py`
- **DialogueTree** (17 connections) — `server/schemas/dialogue/dialogue_tree.py`
- **DialogueService** (16 connections) — `server/game/dialogue/dialogue_service.py`
- **dialogue_service.py** (15 connections) — `server/game/dialogue/dialogue_service.py`
- **handle_talk_command()** (11 connections) — `server/commands/talk_command.py`
- **test_dialogue_service.py** (11 connections) — `server/tests/unit/game/test_dialogue_service.py`
- **._present_node()** (10 connections) — `server/game/dialogue/dialogue_service.py`
- **DialoguePrompt** (9 connections) — `server/game/dialogue/dialogue_service.py`
- **get_dialogue_service()** (9 connections) — `server/game/dialogue/dialogue_service.py`
- **_emit_prompt()** (8 connections) — `server/commands/talk_command.py`
- **_talk_with_npc()** (8 connections) — `server/commands/talk_command.py`
- **.choose_option()** (8 connections) — `server/game/dialogue/dialogue_service.py`
- **__init__.py** (7 connections) — `server/game/dialogue/__init__.py`
- **format_dialogue_prompt()** (7 connections) — `server/game/dialogue/dialogue_service.py`
- **UUID** (7 connections)
- **_talk_by_option_index()** (6 connections) — `server/commands/talk_command.py`
- **.clear_cursor()** (6 connections) — `server/game/dialogue/dialogue_service.py`
- **.get_cursor()** (6 connections) — `server/game/dialogue/dialogue_service.py`
- **.start_with_npc()** (6 connections) — `server/game/dialogue/dialogue_service.py`
- **reset_dialogue_service_for_tests()** (6 connections) — `server/game/dialogue/dialogue_service.py`
- **_resolve_player_id()** (5 connections) — `server/commands/talk_command.py`
- **UUID** (5 connections)
- **DialogueCursor** (5 connections) — `server/game/dialogue/dialogue_service.py`
- **._player_key()** (5 connections) — `server/game/dialogue/dialogue_service.py`
- **test_dialogue_tree_rejects_unknown_next()** (4 connections) — `server/tests/unit/game/test_dialogue_service.py`
- *... and 37 more nodes in this community*

## Relationships

- [commands alias rationale](commands_alias_rationale.md) (6 shared connections)
- [dialogue definition persistence](dialogue_definition_persistence.md) (6 shared connections)
- [commands communication say](commands_communication_say.md) (5 shared connections)
- [commands quest rationale](commands_quest_rationale.md) (5 shared connections)
- [admin auth service](admin_auth_service.md) (5 shared connections)
- [NATS Messaging](NATS_Messaging.md) (4 shared connections)
- [dialogue schemas tree](dialogue_schemas_tree.md) (3 shared connections)
- [commands communication flows](commands_communication_flows.md) (2 shared connections)
- [quest chat game](quest_chat_game.md) (2 shared connections)
- [commands command rationale](commands_command_rationale.md) (2 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [chat game message](chat_game_message.md) (1 shared connections)

## Source Files

- `server/commands/talk_command.py`
- `server/game/dialogue/__init__.py`
- `server/game/dialogue/dialogue_service.py`
- `server/schemas/dialogue/dialogue_tree.py`
- `server/tests/unit/api/test_dialogue_definitions_api.py`
- `server/tests/unit/game/test_dialogue_service.py`

## Audit Trail

- EXTRACTED: 270 (98%)
- INFERRED: 6 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*