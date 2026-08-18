# NATSMessageProcessingMixin

> 20 nodes

## Key Concepts

- **NATSMessageProcessingMixin** (15 connections) — `server/realtime/nats_message_handler_processing.py`
- **._process_single_message()** (8 connections) — `server/realtime/nats_message_handler_processing.py`
- **_ChatMessageFields** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **_ValidatedChatFields** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._build_chat_event()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._extract_chat_message_fields()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._validate_chat_message_fields()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._broadcast_by_channel_type()** (4 connections) — `server/realtime/nats_message_handler_processing.py`
- **._convert_ids_to_uuids()** (4 connections) — `server/realtime/nats_message_handler_processing.py`
- **UUID** (3 connections)
- **TypedDict** (2 connections)
- **Process a single NATS message (original logic, can raise exceptions). Args:…** (1 connections) — `server/realtime/nats_message_handler_processing.py`
- **Extract and normalize chat message fields from message data. Args:…** (1 connections) — `server/realtime/nats_message_handler_processing.py`
- **Extracted chat fields before required-field validation.** (1 connections) — `server/realtime/nats_message_handler_processing.py`
- **Validate that all required chat message fields are present. Args: chat_fields:…** (1 connections) — `server/realtime/nats_message_handler_processing.py`
- **Build a WebSocket chat event from chat fields and formatted message. Args:…** (1 connections) — `server/realtime/nats_message_handler_processing.py`
- **Convert string IDs to UUIDs for broadcasting. Args: sender_id: Sender player ID…** (1 connections) — `server/realtime/nats_message_handler_processing.py`
- **Broadcast message based on channel type using strategy pattern. Args: channel:…** (1 connections) — `server/realtime/nats_message_handler_processing.py`
- **Chat fields after required string fields are validated.** (1 connections) — `server/realtime/nats_message_handler_processing.py`
- **Mixin: NATS message ingest, retry, chat field extract/validate, channel…** (1 connections) — `server/realtime/nats_message_handler_processing.py`

## Relationships

- [get_logger](get_logger.md) (6 shared connections)
- [._handle_nats_message](_handle_nats_message.md) (3 shared connections)
- [lifespan_protocols.py](lifespan_protocols.py.md) (1 shared connections)
- [NATSMessageHandlerMixinBase](NATSMessageHandlerMixinBase.md) (1 shared connections)
- [CircuitBreakerOpen](CircuitBreakerOpen.md) (1 shared connections)
- [DeadLetterMessage](DeadLetterMessage.md) (1 shared connections)
- [build_event](build_event.md) (1 shared connections)

## Source Files

- `server/realtime/nats_message_handler_processing.py`

## Audit Trail

- EXTRACTED: 40 (95%)
- INFERRED: 2 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*