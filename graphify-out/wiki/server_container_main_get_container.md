# server container main get container

> 180 nodes

## Key Concepts

- **build_event()** (116 connections) — `server/realtime/envelope.py`
- **envelope.py** (29 connections) — `server/realtime/envelope.py`
- **test_envelope.py** (29 connections) — `server/tests/unit/realtime/test_envelope.py`
- **test_message_handlers.py** (26 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **get_container()** (19 connections) — `server/container/main.py`
- **websocket_handler_connection.py** (18 connections) — `server/realtime/websocket_handler_connection.py`
- **asyncio** (16 connections)
- **CombatBroadcastMixin** (15 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **message_handlers.py** (15 connections) — `server/realtime/message_handlers.py`
- **handle_follow_response_message()** (14 connections) — `server/realtime/message_handlers.py`
- **handle_party_invite_response_message()** (13 connections) — `server/realtime/message_handlers.py`
- **CombatMessagingIntegration** (12 connections) — `server/services/combat_messaging/integration.py`
- **PlayerBroadcastMixin** (11 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **handle_command_message()** (11 connections) — `server/realtime/message_handlers.py`
- **combat_messaging/base.py** (11 connections) — `server/services/combat_messaging/base.py`
- **handle_chat_message()** (10 connections) — `server/realtime/message_handlers.py`
- **handle_ping_message()** (10 connections) — `server/realtime/message_handlers.py`
- **combat_broadcasts.py** (9 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **integration.py** (9 connections) — `server/services/combat_messaging/integration.py`
- **player_broadcasts.py** (9 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **UUIDEncoder** (8 connections) — `server/realtime/envelope.py`
- **handle_client_error_report_message()** (8 connections) — `server/realtime/message_handlers.py`
- **Any** (7 connections)
- **HasConnectionManager** (6 connections) — `server/services/combat_messaging/base.py`
- **utc_now_z()** (6 connections) — `server/realtime/envelope.py`
- *... and 155 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (17 shared connections)
- [server realtime message handler factory](server_realtime_message_handler_factory.md) (12 shared connections)
- [server events event types playerdeliriumrespawnedevent](server_events_event_types_playerdeliriumrespawnedevent.md) (11 shared connections)
- [server app lifespan startup legacy](server_app_lifespan_startup_legacy.md) (9 shared connections)
- [followtargetvalue](followtargetvalue.md) (6 shared connections)
- [server realtime event handlers](server_realtime_event_handlers.md) (6 shared connections)
- [server realtime websocket handler](server_realtime_websocket_handler.md) (6 shared connections)
- [server realtime connection error methods](server_realtime_connection_error_methods.md) (6 shared connections)
- [server realtime websocket handler commands](server_realtime_websocket_handler_commands.md) (5 shared connections)
- [server commands look helpers lookrequest](server_commands_look_helpers_lookrequest.md) (5 shared connections)
- [server game mechanics](server_game_mechanics.md) (4 shared connections)
- [combatmessages](combatmessages.md) (4 shared connections)

## Source Files

- `server/container/main.py`
- `server/realtime/envelope.py`
- `server/realtime/message_handlers.py`
- `server/realtime/websocket_handler_connection.py`
- `server/services/combat_messaging/__init__.py`
- `server/services/combat_messaging/base.py`
- `server/services/combat_messaging/combat_broadcasts.py`
- `server/services/combat_messaging/integration.py`
- `server/services/combat_messaging/player_broadcasts.py`
- `server/services/npc_combat_integration_service.py`
- `server/tests/unit/realtime/test_envelope.py`
- `server/tests/unit/realtime/test_message_handlers.py`

## Audit Trail

- EXTRACTED: 464 (98%)
- INFERRED: 11 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*