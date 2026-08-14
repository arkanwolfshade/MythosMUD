# NATSMessageHandlerMixinBase

> 32 nodes

## Key Concepts

- **NATSMessageHandlerMixinBase** (19 connections) — `server/realtime/nats_message_handler_base.py`
- **NATSMessageProcessingMixin** (15 connections) — `server/realtime/nats_message_handler_processing.py`
- **_ChatMessageFields** (8 connections) — `server/realtime/nats_message_handler_processing.py`
- **_ValidatedChatFields** (8 connections) — `server/realtime/nats_message_handler_processing.py`
- **._process_single_message()** (8 connections) — `server/realtime/nats_message_handler_processing.py`
- **._build_chat_event()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._extract_chat_message_fields()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._handle_nats_message()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._process_message_with_retry()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._validate_chat_message_fields()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._broadcast_by_channel_type()** (4 connections) — `server/realtime/nats_message_handler_processing.py`
- **._convert_ids_to_uuids()** (4 connections) — `server/realtime/nats_message_handler_processing.py`
- **_optional_str()** (4 connections) — `server/realtime/nats_message_handler_processing.py`
- **_str_field()** (4 connections) — `server/realtime/nats_message_handler_processing.py`
- **UUID** (3 connections)
- **TypedDict** (2 connections)
- **._subscribe_to_subject()** (1 connections) — `server/realtime/nats_message_handler_base.py`
- **._unsubscribe_from_subject()** (1 connections) — `server/realtime/nats_message_handler_base.py`
- **Attrs/methods provided by NATSMessageHandler when mixed in.** (1 connections) — `server/realtime/nats_message_handler_base.py`
- **Process message with retry logic. Attempts message processing with exponential…** (1 connections) — `server/realtime/nats_message_handler_processing.py`
- **Process a single NATS message (original logic, can raise exceptions). Args:…** (1 connections) — `server/realtime/nats_message_handler_processing.py`
- **Extract and normalize chat message fields from message data. Args:…** (1 connections) — `server/realtime/nats_message_handler_processing.py`
- **Extracted chat fields before required-field validation.** (1 connections) — `server/realtime/nats_message_handler_processing.py`
- **Validate that all required chat message fields are present. Args: chat_fields:…** (1 connections) — `server/realtime/nats_message_handler_processing.py`
- **Build a WebSocket chat event from chat fields and formatted message. Args:…** (1 connections) — `server/realtime/nats_message_handler_processing.py`
- *... and 7 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (11 shared connections)
- [DeadLetterQueue](DeadLetterQueue.md) (6 shared connections)
- [test_nats_message_handler.py](test_nats_message_handler.py.md) (3 shared connections)
- [logging_file_setup.py](logging_file_setup.py.md) (2 shared connections)
- [test_room_utils.py](test_room_utils.py.md) (1 shared connections)
- [CircuitBreaker](CircuitBreaker.md) (1 shared connections)
- [EventHandler](EventHandler.md) (1 shared connections)
- [MessageFilteringHelper](MessageFilteringHelper.md) (1 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (1 shared connections)
- [NATSMessageBroadcastMixin](NATSMessageBroadcastMixin.md) (1 shared connections)
- [NATSMessageSubscriptionMixin](NATSMessageSubscriptionMixin.md) (1 shared connections)
- [PlayerEventHandlerUtils](PlayerEventHandlerUtils.md) (1 shared connections)

## Source Files

- `server/realtime/nats_message_handler_base.py`
- `server/realtime/nats_message_handler_processing.py`

## Audit Trail

- EXTRACTED: 58 (76%)
- INFERRED: 18 (24%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*