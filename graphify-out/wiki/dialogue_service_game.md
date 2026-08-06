# dialogue service game

> 90 nodes

## Key Concepts

- **talk_command.py** (27 connections) — `server/commands/talk_command.py`
- **DialogueTree** (19 connections) — `server/schemas/dialogue/dialogue_tree.py`
- **DialogueService** (18 connections) — `server/game/dialogue/dialogue_service.py`
- **dialogue_service.py** (17 connections) — `server/game/dialogue/dialogue_service.py`
- **test_talk_command.py** (14 connections) — `server/tests/unit/commands/test_talk_command.py`
- **DialoguePrompt** (13 connections) — `server/game/dialogue/dialogue_service.py`
- **test_dialogue_service.py** (12 connections) — `server/tests/unit/game/test_dialogue_service.py`
- **handle_talk_command()** (11 connections) — `server/commands/talk_command.py`
- **._present_node()** (10 connections) — `server/game/dialogue/dialogue_service.py`
- **.choose_option()** (9 connections) — `server/game/dialogue/dialogue_service.py`
- **get_dialogue_service()** (9 connections) — `server/game/dialogue/dialogue_service.py`
- **_emit_prompt()** (8 connections) — `server/commands/talk_command.py`
- **_talk_with_npc()** (8 connections) — `server/commands/talk_command.py`
- **UUID** (8 connections)
- **__init__.py** (7 connections) — `server/game/dialogue/__init__.py`
- **format_dialogue_prompt()** (7 connections) — `server/game/dialogue/dialogue_service.py`
- **.clear_cursor()** (7 connections) — `server/game/dialogue/dialogue_service.py`
- **_talk_by_option_index()** (6 connections) — `server/commands/talk_command.py`
- **.get_cursor()** (6 connections) — `server/game/dialogue/dialogue_service.py`
- **.start_with_npc()** (6 connections) — `server/game/dialogue/dialogue_service.py`
- **._load_tree_or_fade()** (6 connections) — `server/game/dialogue/dialogue_service.py`
- **reset_dialogue_service_for_tests()** (6 connections) — `server/game/dialogue/dialogue_service.py`
- **DialogueNode** (6 connections) — `server/schemas/dialogue/dialogue_tree.py`
- **_resolve_player_id()** (5 connections) — `server/commands/talk_command.py`
- **UUID** (5 connections)
- *... and 65 more nodes in this community*

## Relationships

- [commands communication flows](commands_communication_flows.md) (7 shared connections)
- [player preferences services](player_preferences_services.md) (6 shared connections)
- [commands quest rationale](commands_quest_rationale.md) (5 shared connections)
- [message broadcaster realtime](message_broadcaster_realtime.md) (5 shared connections)
- [Error Conversion](Error_Conversion.md) (4 shared connections)
- [add used user](add_used_user.md) (4 shared connections)
- [alias storage rationale](alias_storage_rationale.md) (2 shared connections)
- [realtime real time](realtime_real_time.md) (2 shared connections)
- [game chat moderation](game_chat_moderation.md) (2 shared connections)
- [commands command rationale](commands_command_rationale.md) (2 shared connections)
- [monitoring endpoints rationale](monitoring_endpoints_rationale.md) (1 shared connections)
- [quest chat game](quest_chat_game.md) (1 shared connections)

## Source Files

- `server/commands/talk_command.py`
- `server/game/dialogue/__init__.py`
- `server/game/dialogue/dialogue_service.py`
- `server/schemas/dialogue/__init__.py`
- `server/schemas/dialogue/dialogue_tree.py`
- `server/tests/unit/api/test_dialogue_definitions_api.py`
- `server/tests/unit/commands/test_talk_command.py`
- `server/tests/unit/game/test_dialogue_service.py`

## Audit Trail

- EXTRACTED: 358 (98%)
- INFERRED: 8 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*