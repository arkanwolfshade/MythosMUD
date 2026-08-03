# combat services messaging

> 206 nodes

## Key Concepts

- **build_event()** (116 connections) — `server/realtime/envelope.py`
- **send_game_event()** (30 connections) — `server/realtime/connection_manager_api.py`
- **test_envelope.py** (28 connections) — `server/tests/unit/realtime/test_envelope.py`
- **envelope.py** (27 connections) — `server/realtime/envelope.py`
- **follow_service.py** (25 connections) — `server/game/follow_service.py`
- **player_connection_setup.py** (25 connections) — `server/realtime/player_connection_setup.py`
- **test_message_handlers.py** (24 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **message_handler_factory.py** (23 connections) — `server/realtime/message_handler_factory.py`
- **connection_manager_api.py** (21 connections) — `server/realtime/connection_manager_api.py`
- **handle_new_connection_setup()** (17 connections) — `server/realtime/player_connection_setup.py`
- **message_handlers.py** (14 connections) — `server/realtime/message_handlers.py`
- **handle_follow_response_message()** (14 connections) — `server/realtime/message_handlers.py`
- **handle_party_invite_response_message()** (13 connections) — `server/realtime/message_handlers.py`
- **broadcast_game_event()** (12 connections) — `server/realtime/connection_manager_api.py`
- **handle_command_message()** (11 connections) — `server/realtime/message_handlers.py`
- **resolve_connection_manager()** (10 connections) — `server/realtime/connection_manager_utils.py`
- **handle_chat_message()** (10 connections) — `server/realtime/message_handlers.py`
- **handle_ping_message()** (10 connections) — `server/realtime/message_handlers.py`
- **__getattr__()** (9 connections) — `server/realtime/connection_manager.py`
- **_broadcast_player_entered_game()** (9 connections) — `server/realtime/player_connection_setup.py`
- **send_room_event()** (8 connections) — `server/realtime/connection_manager_api.py`
- **connection_manager_utils.py** (8 connections) — `server/realtime/connection_manager_utils.py`
- **UUIDEncoder** (8 connections) — `server/realtime/envelope.py`
- **handle_client_error_report_message()** (8 connections) — `server/realtime/message_handlers.py`
- **_trigger_quests_for_room_on_spawn()** (8 connections) — `server/realtime/player_connection_setup.py`
- *... and 181 more nodes in this community*

## Relationships

- [models npc rationale](models_npc_rationale.md) (38 shared connections)
- [Room Broadcast](Room_Broadcast.md) (22 shared connections)
- [Database Config](Database_Config.md) (11 shared connections)
- [NATS Messaging](NATS_Messaging.md) (10 shared connections)
- [look helpers commands](look_helpers_commands.md) (8 shared connections)
- [command utility models](command_utility_models.md) (8 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (7 shared connections)
- [follow game service](follow_game_service.md) (7 shared connections)
- [circuit breaker realtime](circuit_breaker_realtime.md) (7 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (6 shared connections)
- [room look commands](room_look_commands.md) (6 shared connections)
- [game chat moderation](game_chat_moderation.md) (6 shared connections)

## Source Files

- `server/game/follow_service.py`
- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_api.py`
- `server/realtime/connection_manager_utils.py`
- `server/realtime/envelope.py`
- `server/realtime/message_handler_factory.py`
- `server/realtime/message_handlers.py`
- `server/realtime/player_connection_setup.py`
- `server/realtime/websocket_handler_commands.py`
- `server/services/combat_messaging/combat_broadcasts.py`
- `server/services/combat_messaging/player_broadcasts.py`
- `server/tests/unit/realtime/test_envelope.py`
- `server/tests/unit/realtime/test_message_handlers.py`
- `server/tests/unit/realtime/test_player_connection_setup_grace_period.py`

## Audit Trail

- EXTRACTED: 878 (96%)
- INFERRED: 33 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*