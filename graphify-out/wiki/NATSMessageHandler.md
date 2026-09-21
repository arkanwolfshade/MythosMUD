# NATSMessageHandler

> 16 nodes

## Key Concepts

- **NATSMessageHandler** (25 connections) — `server/realtime/nats_message_handler.py`
- **.__init__()** (7 connections) — `server/realtime/nats_message_handler.py`
- **._subscribe_to_chat_subjects()** (4 connections) — `server/realtime/nats_message_handler.py`
- **._subscribe_to_standardized_chat_subjects()** (4 connections) — `server/realtime/nats_message_handler.py`
- **.start()** (3 connections) — `server/realtime/nats_message_handler.py`
- **.stop()** (3 connections) — `server/realtime/nats_message_handler.py`
- **._subscribe_to_subject()** (3 connections) — `server/realtime/nats_message_handler.py`
- **._unsubscribe_from_subject()** (3 connections) — `server/realtime/nats_message_handler.py`
- **Start the NATS message handler and subscribe to subjects. Args:…** (1 connections) — `server/realtime/nats_message_handler.py`
- **Stop the NATS message handler and unsubscribe from subjects. Returns: True if…** (1 connections) — `server/realtime/nats_message_handler.py`
- **Subscribe to all chat-related NATS subjects using NATSSubjectManager patterns.…** (1 connections) — `server/realtime/nats_message_handler.py`
- **Subscribe to chat subjects using NATSSubjectManager patterns. This method…** (1 connections) — `server/realtime/nats_message_handler.py`
- **Subscribe to a specific NATS subject. Args: subject: Subject string to…** (1 connections) — `server/realtime/nats_message_handler.py`
- **Unsubscribe from a specific NATS subject. Returns: True if unsubscribed…** (1 connections) — `server/realtime/nats_message_handler.py`
- **Handler for processing NATS messages and broadcasting to WebSocket clients.…** (1 connections) — `server/realtime/nats_message_handler.py`
- **Initialize NATS message handler with error boundaries. Args: nats_service: NATS…** (1 connections) — `server/realtime/nats_message_handler.py`

## Relationships

- [test_container_bundles.py](test_container_bundles.py.md) (3 shared connections)
- [test_message_filtering.py](test_message_filtering.py.md) (3 shared connections)
- [lifespan_protocols.py](lifespan_protocols.py.md) (2 shared connections)
- [PlayerEventHandlerUtils](PlayerEventHandlerUtils.md) (2 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (2 shared connections)
- [DeadLetterQueue](DeadLetterQueue.md) (2 shared connections)
- [CircuitBreaker](CircuitBreaker.md) (2 shared connections)
- [EventHandler](EventHandler.md) (2 shared connections)
- [NATSMessageBroadcastMixin](NATSMessageBroadcastMixin.md) (1 shared connections)
- [nats_message_handler_processing.py](nats_message_handler_processing.py.md) (1 shared connections)
- [NATSMessageSubscriptionMixin](NATSMessageSubscriptionMixin.md) (1 shared connections)
- [GameStateProvider](GameStateProvider.md) (1 shared connections)

## Source Files

- `server/realtime/nats_message_handler.py`

## Audit Trail

- EXTRACTED: 34 (83%)
- INFERRED: 7 (17%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*