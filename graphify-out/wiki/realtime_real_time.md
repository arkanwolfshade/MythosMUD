# realtime real time

> 8 nodes

## Key Concepts

- **._subscribe_to_standardized_chat_subjects()** (5 connections) — `server/realtime/nats_message_handler.py`
- **.start()** (4 connections) — `server/realtime/nats_message_handler.py`
- **._subscribe_to_chat_subjects()** (4 connections) — `server/realtime/nats_message_handler.py`
- **._subscribe_to_subject()** (4 connections) — `server/realtime/nats_message_handler.py`
- **Start the NATS message handler and subscribe to subjects.          Args:** (1 connections) — `server/realtime/nats_message_handler.py`
- **Subscribe to all chat-related NATS subjects using NATSSubjectManager patterns.** (1 connections) — `server/realtime/nats_message_handler.py`
- **Subscribe to chat subjects using NATSSubjectManager patterns.          This meth** (1 connections) — `server/realtime/nats_message_handler.py`
- **Subscribe to a specific NATS subject.          Args:             subject: Subjec** (1 connections) — `server/realtime/nats_message_handler.py`

## Relationships

- [circuit breaker realtime](circuit_breaker_realtime.md) (4 shared connections)
- [nats exceptions services](nats_exceptions_services.md) (3 shared connections)

## Source Files

- `server/realtime/nats_message_handler.py`

## Audit Trail

- EXTRACTED: 18 (86%)
- INFERRED: 3 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*