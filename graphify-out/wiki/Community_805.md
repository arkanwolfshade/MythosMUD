# Community 805

> 20 nodes

## Key Concepts

- **NATSMessageHandler** (29 connections) — `server/realtime/nats_message_handler.py`
- **.__init__()** (5 connections) — `server/realtime/nats_message_handler.py`
- **._subscribe_to_chat_subjects()** (4 connections) — `server/realtime/nats_message_handler.py`
- **._subscribe_to_standardized_chat_subjects()** (4 connections) — `server/realtime/nats_message_handler.py`
- **_chat_driver()** (4 connections) — `server/tests/unit/realtime/test_message_category_invariants.py`
- **.start()** (3 connections) — `server/realtime/nats_message_handler.py`
- **.stop()** (3 connections) — `server/realtime/nats_message_handler.py`
- **._subscribe_to_subject()** (3 connections) — `server/realtime/nats_message_handler.py`
- **._unsubscribe_from_subject()** (3 connections) — `server/realtime/nats_message_handler.py`
- **DeadLetterQueue** (2 connections)
- **Driver** (1 connections)
- **NATSMessageSubscriptionMixin** (1 connections)
- **Start the NATS message handler and subscribe to subjects. Args:…** (1 connections) — `server/realtime/nats_message_handler.py`
- **Stop the NATS message handler and unsubscribe from subjects. Returns: True if…** (1 connections) — `server/realtime/nats_message_handler.py`
- **Subscribe to all chat-related NATS subjects using NATSSubjectManager patterns.…** (1 connections) — `server/realtime/nats_message_handler.py`
- **Subscribe to chat subjects using NATSSubjectManager patterns. This method…** (1 connections) — `server/realtime/nats_message_handler.py`
- **Subscribe to a specific NATS subject. Args: subject: Subject string to…** (1 connections) — `server/realtime/nats_message_handler.py`
- **Unsubscribe from a specific NATS subject. Returns: True if unsubscribed…** (1 connections) — `server/realtime/nats_message_handler.py`
- **Handler for processing NATS messages and broadcasting to WebSocket clients.…** (1 connections) — `server/realtime/nats_message_handler.py`
- **Initialize NATS message handler with error boundaries. Args: nats_service: NATS…** (1 connections) — `server/realtime/nats_message_handler.py`

## Relationships

- [Community 794](Community_794.md) (5 shared connections)
- [Community 47](Community_47.md) (3 shared connections)
- [Community 500](Community_500.md) (2 shared connections)
- [Community 563](Community_563.md) (2 shared connections)
- [Community 75](Community_75.md) (2 shared connections)
- [NPC Movement Events](NPC_Movement_Events.md) (2 shared connections)
- [Community 328](Community_328.md) (2 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (1 shared connections)
- [Community 417](Community_417.md) (1 shared connections)
- [Community 41](Community_41.md) (1 shared connections)
- [Community 220](Community_220.md) (1 shared connections)
- [Community 106](Community_106.md) (1 shared connections)

## Source Files

- `server/realtime/nats_message_handler.py`
- `server/tests/unit/realtime/test_message_category_invariants.py`

## Audit Trail

- EXTRACTED: 37 (79%)
- INFERRED: 10 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*