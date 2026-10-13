# Community 41

> 137 nodes

## Key Concepts

- **build_event()** (123 connections) — `server/realtime/envelope.py`
- **message_category.py** (45 connections) — `server/constants/message_category.py`
- **envelope.py** (35 connections) — `server/realtime/envelope.py`
- **test_envelope.py** (33 connections) — `server/tests/unit/realtime/test_envelope.py`
- **websocket_handler_commands.py** (30 connections) — `server/realtime/websocket_handler_commands.py`
- **event_handlers.py** (26 connections) — `server/realtime/event_handlers.py`
- **nats_message_handler_processing.py** (21 connections) — `server/realtime/nats_message_handler_processing.py`
- **npc_event_handlers.py** (17 connections) — `server/realtime/npc_event_handlers.py`
- **NATSMessageProcessingMixin** (13 connections) — `server/realtime/nats_message_handler_processing.py`
- **PlayerBroadcastMixin** (11 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **combat_broadcasts.py** (10 connections) — `server/services/combat_messaging/combat_broadcasts.py`
- **player_broadcasts.py** (10 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **_send_combat_participant_updates()** (9 connections) — `server/realtime/event_handlers.py`
- **integration.py** (9 connections) — `server/services/combat_messaging/integration.py`
- **UUIDEncoder** (8 connections) — `server/realtime/envelope.py`
- **_npc_died_broadcast_and_bridge()** (8 connections) — `server/realtime/event_handlers.py`
- **._process_single_message()** (8 connections) — `server/realtime/nats_message_handler_processing.py`
- **CombatMessagingIntegration** (7 connections) — `server/services/combat_messaging/integration.py`
- **utc_now_z()** (6 connections) — `server/realtime/envelope.py`
- **._validate_chat_message_fields()** (6 connections) — `server/realtime/nats_message_handler_processing.py`
- **.broadcast_player_mortally_wounded()** (6 connections) — `server/services/combat_messaging/player_broadcasts.py`
- **_ChatMessageFields** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **_ValidatedChatFields** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **_refresh_room_after_npc_death()** (5 connections) — `server/realtime/event_handlers.py`
- **._build_chat_event()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- *... and 112 more nodes in this community*

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (42 shared connections)
- [Community 98](Community_98.md) (17 shared connections)
- [Community 144](Community_144.md) (12 shared connections)
- [Community 346](Community_346.md) (12 shared connections)
- [Community 328](Community_328.md) (12 shared connections)
- [Community 106](Community_106.md) (9 shared connections)
- [Community 57](Community_57.md) (8 shared connections)
- [NPC Movement Events](NPC_Movement_Events.md) (7 shared connections)
- [Community 635](Community_635.md) (6 shared connections)
- [WebSocket Message Types](WebSocket_Message_Types.md) (6 shared connections)
- [Community 47](Community_47.md) (5 shared connections)
- [Community 299](Community_299.md) (5 shared connections)

## Source Files

- `server/constants/message_category.py`
- `server/realtime/envelope.py`
- `server/realtime/event_handlers.py`
- `server/realtime/nats_message_handler_processing.py`
- `server/realtime/npc_event_handlers.py`
- `server/realtime/websocket_handler_commands.py`
- `server/services/combat_messaging/__init__.py`
- `server/services/combat_messaging/combat_broadcasts.py`
- `server/services/combat_messaging/integration.py`
- `server/services/combat_messaging/player_broadcasts.py`
- `server/services/combat_messaging_integration.py`
- `server/tests/unit/realtime/test_envelope.py`

## Audit Trail

- EXTRACTED: 452 (97%)
- INFERRED: 14 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*