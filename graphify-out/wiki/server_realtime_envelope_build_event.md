# server realtime envelope build event

> 201 nodes

## Key Concepts

- **build_event()** (105 connections) — `server/realtime/envelope.py`
- **test_websocket_handler_core.py** (43 connections) — `server/tests/unit/realtime/test_websocket_handler_core.py`
- **websocket_handler_commands.py** (33 connections) — `server/realtime/websocket_handler_commands.py`
- **handle_game_command()** (29 connections) — `server/realtime/websocket_handler_commands.py`
- **test_websocket_handler_commands.py** (29 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **asyncio** (28 connections)
- **process_websocket_command()** (19 connections) — `server/realtime/websocket_handler_commands.py`
- **handle_chat_message()** (17 connections) — `server/realtime/websocket_handler.py`
- **send_system_message()** (13 connections) — `server/realtime/websocket_handler.py`
- **resolve_websocket_connection_manager()** (12 connections) — `server/realtime/websocket_handler_commands.py`
- **handle_websocket_message()** (11 connections) — `server/realtime/websocket_handler.py`
- **asyncio** (11 connections)
- **validate_player_and_persistence()** (9 connections) — `server/realtime/websocket_handler_commands.py`
- **test_websocket_handler_system_message.py** (9 connections) — `server/tests/unit/realtime/test_websocket_handler_system_message.py`
- **_attach_room_state_to_result()** (8 connections) — `server/realtime/websocket_handler_commands.py`
- **parse_game_command_tokens()** (8 connections) — `server/realtime/websocket_handler_commands.py`
- **Any** (7 connections)
- **_resolve_get_room_state_callable()** (6 connections) — `server/realtime/websocket_handler_commands.py`
- **.broadcast_combat_attack()** (6 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **.broadcast_player_mortally_wounded()** (6 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **test_process_websocket_command_attaches_room_state()** (6 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **test_process_websocket_command_room_state_get_room_fails_softly()** (6 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **._build_combat_attack_event()** (5 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **test_process_websocket_command_room_changed_no_player_handler_skips_room_state()** (5 connections) — `server/tests/unit/realtime/test_websocket_handler_commands.py`
- **Any** (5 connections)
- *... and 176 more nodes in this community*

## Relationships

- [combatmessages](combatmessages.md) (18 shared connections)
- [server realtime envelope rationale 33](server_realtime_envelope_rationale_33.md) (17 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (16 shared connections)
- [server realtime websocket handler](server_realtime_websocket_handler.md) (16 shared connections)
- [server realtime message validator](server_realtime_message_validator.md) (13 shared connections)
- [docs examples logging fastapi integration](docs_examples_logging_fastapi_integration.md) (12 shared connections)
- [server realtime websocket handler app](server_realtime_websocket_handler_app.md) (11 shared connections)
- [server container main get container](server_container_main_get_container.md) (7 shared connections)
- [server commands container helpers inventory](server_commands_container_helpers_inventory.md) (6 shared connections)
- [server events event types playerdpupdated](server_events_event_types_playerdpupdated.md) (5 shared connections)
- [server commands admin teleport utils](server_commands_admin_teleport_utils.md) (3 shared connections)
- [server commands rest countdown task](server_commands_rest_countdown_task.md) (3 shared connections)

## Source Files

- `server/realtime/envelope.py`
- `server/realtime/websocket_handler.py`
- `server/realtime/websocket_handler_commands.py`
- `server/services/combat_messaging/combat_broadcasts.py`
- `server/services/combat_messaging/player_broadcasts.py`
- `server/tests/unit/realtime/test_envelope.py`
- `server/tests/unit/realtime/test_websocket_handler_commands.py`
- `server/tests/unit/realtime/test_websocket_handler_core.py`
- `server/tests/unit/realtime/test_websocket_handler_system_message.py`

## Audit Trail

- EXTRACTED: 472 (93%)
- INFERRED: 34 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*