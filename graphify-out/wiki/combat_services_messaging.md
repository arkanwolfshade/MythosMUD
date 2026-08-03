# combat services messaging

> 163 nodes

## Key Concepts

- **build_event()** (116 connections) — `server/realtime/envelope.py`
- **test_envelope.py** (28 connections) — `server/tests/unit/realtime/test_envelope.py`
- **envelope.py** (27 connections) — `server/realtime/envelope.py`
- **CombatMessagingService** (18 connections) — `server/services/combat_messaging_service.py`
- **CombatBroadcastMixin** (15 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **CombatMessagingIntegration** (12 connections) — `server/services/combat_messaging/integration.py`
- **test_message_handlers.py** (12 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **handle_command_message()** (11 connections) — `server/realtime/message_handlers.py`
- **base.py** (11 connections) — `server/services/combat_messaging/base.py`
- **PlayerBroadcastMixin** (11 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **handle_chat_message()** (10 connections) — `server/realtime/message_handlers.py`
- **handle_ping_message()** (10 connections) — `server/realtime/message_handlers.py`
- **handle_follow_response_message()** (9 connections) — `server/realtime/message_handlers.py`
- **combat_broadcasts.py** (9 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **integration.py** (9 connections) — `server/services/combat_messaging/integration.py`
- **player_broadcasts.py** (9 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **combat_messaging_service.py** (9 connections) — `server/services/combat_messaging_service.py`
- **UUIDEncoder** (8 connections) — `server/realtime/envelope.py`
- **handle_party_invite_response_message()** (8 connections) — `server/realtime/message_handlers.py`
- **CombatMessagingBase** (8 connections) — `server/services/combat_messaging/base.py`
- **HasConnectionManager** (7 connections) — `server/services/combat_messaging/base.py`
- **Any** (7 connections)
- **utc_now_z()** (6 connections) — `server/realtime/envelope.py`
- **handle_client_error_report_message()** (6 connections) — `server/realtime/message_handlers.py`
- **WebSocket** (6 connections)
- *... and 138 more nodes in this community*

## Relationships

- [command inventory factories](command_inventory_factories.md) (16 shared connections)
- [Room Broadcast](Room_Broadcast.md) (15 shared connections)
- [commands admin mute](commands_admin_mute.md) (13 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (11 shared connections)
- [item models rationale](item_models_rationale.md) (6 shared connections)
- [NATS Messaging](NATS_Messaging.md) (6 shared connections)
- [circuit breaker realtime](circuit_breaker_realtime.md) (5 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (5 shared connections)
- [realtime websocket initial](realtime_websocket_initial.md) (5 shared connections)
- [connection manager realtime](connection_manager_realtime.md) (5 shared connections)
- [game chat moderation](game_chat_moderation.md) (5 shared connections)
- [combat npc services](combat_npc_services.md) (4 shared connections)

## Source Files

- `server/realtime/envelope.py`
- `server/realtime/message_handlers.py`
- `server/services/combat_messaging/__init__.py`
- `server/services/combat_messaging/base.py`
- `server/services/combat_messaging/combat_broadcasts.py`
- `server/services/combat_messaging/integration.py`
- `server/services/combat_messaging/player_broadcasts.py`
- `server/services/combat_messaging_integration.py`
- `server/services/combat_messaging_service.py`
- `server/tests/unit/realtime/test_envelope.py`
- `server/tests/unit/realtime/test_message_handlers.py`
- `server/tests/unit/services/test_combat_messaging_service.py`

## Audit Trail

- EXTRACTED: 645 (97%)
- INFERRED: 20 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*