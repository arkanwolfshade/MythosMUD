# Security Issues And Fixes

> 18 nodes

## Key Concepts

- **._subscribe_to_subject()** (7 connections) — `server/realtime/nats_message_handler.py`
- **.handle_player_movement()** (6 connections) — `server/realtime/nats_message_handler.py`
- **.start()** (5 connections) — `server/realtime/nats_message_handler.py`
- **._subscribe_to_standardized_chat_subjects()** (5 connections) — `server/realtime/nats_message_handler.py`
- **._subscribe_to_chat_subjects()** (4 connections) — `server/realtime/nats_message_handler.py`
- **.subscribe_to_subzone()** (4 connections) — `server/realtime/nats_message_handler.py`
- **.subscribe_to_event_subjects()** (4 connections) — `server/realtime/nats_message_handler.py`
- **.subscribe_to_room()** (3 connections) — `server/realtime/nats_message_handler.py`
- **.track_player_subzone_subscription()** (3 connections) — `server/realtime/nats_message_handler.py`
- **Start the NATS message handler and subscribe to subjects.          Args:** (1 connections) — `server/realtime/nats_message_handler.py`
- **Subscribe to all chat-related NATS subjects using NATSSubjectManager patterns.** (1 connections) — `server/realtime/nats_message_handler.py`
- **Subscribe to chat subjects using NATSSubjectManager patterns.          This meth** (1 connections) — `server/realtime/nats_message_handler.py`
- **Subscribe to a specific NATS subject.          Args:             subject: Subjec** (1 connections) — `server/realtime/nats_message_handler.py`
- **Subscribe to chat messages for a specific room.          Args:             room_** (1 connections) — `server/realtime/nats_message_handler.py`
- **Subscribe to local channel messages for a specific sub-zone.          Args:** (1 connections) — `server/realtime/nats_message_handler.py`
- **Track a player's sub-zone subscription for local channels.          Args:** (1 connections) — `server/realtime/nats_message_handler.py`
- **Handle player movement between rooms and update sub-zone subscriptions.** (1 connections) — `server/realtime/nats_message_handler.py`
- **Subscribe to all event-related NATS subjects using standardized patterns.** (1 connections) — `server/realtime/nats_message_handler.py`

## Relationships

- [NATS Chat Broadcasting](NATS_Chat_Broadcasting.md) (10 shared connections)
- [Inventory Command Models](Inventory_Command_Models.md) (3 shared connections)
- [Monitoring API Endpoints](Monitoring_API_Endpoints.md) (1 shared connections)

## Source Files

- `server/realtime/nats_message_handler.py`

## Audit Trail

- EXTRACTED: 47 (94%)
- INFERRED: 3 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*