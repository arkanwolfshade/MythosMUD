# nats_message_handler_processing.py

> 54 nodes

## Key Concepts

- **nats_message_handler_processing.py** (24 connections) — `server/realtime/nats_message_handler_processing.py`
- **format_message_content()** (19 connections) — `server/realtime/message_formatters.py`
- **NATSMessageProcessingMixin** (15 connections) — `server/realtime/nats_message_handler_processing.py`
- **message_formatters.py** (9 connections) — `server/realtime/message_formatters.py`
- **._process_single_message()** (8 connections) — `server/realtime/nats_message_handler_processing.py`
- **_ChatMessageFields** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **_ValidatedChatFields** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._build_chat_event()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._extract_chat_message_fields()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._handle_nats_message()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._process_message_with_retry()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._validate_chat_message_fields()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._broadcast_by_channel_type()** (4 connections) — `server/realtime/nats_message_handler_processing.py`
- **._convert_ids_to_uuids()** (4 connections) — `server/realtime/nats_message_handler_processing.py`
- **_optional_str()** (4 connections) — `server/realtime/nats_message_handler_processing.py`
- **_str_field()** (4 connections) — `server/realtime/nats_message_handler_processing.py`
- **test_format_message_content_admin()** (3 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **test_format_message_content_emote()** (3 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **test_format_message_content_global()** (3 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **test_format_message_content_local()** (3 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **test_format_message_content_pose()** (3 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **test_format_message_content_say()** (3 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **test_format_message_content_system()** (3 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **test_format_message_content_unknown_channel()** (3 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **test_format_message_content_whisper()** (3 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- *... and 29 more nodes in this community*

## Relationships

- [NATSError](NATSError.md) (17 shared connections)
- [test_message_filtering.py](test_message_filtering.py.md) (8 shared connections)
- [DeadLetterQueue](DeadLetterQueue.md) (4 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [CircuitBreaker](CircuitBreaker.md) (3 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [test_nats_messages.py](test_nats_messages.py.md) (2 shared connections)
- [NATSMessageHandler](NATSMessageHandler.md) (1 shared connections)
- [NATSMessageBroadcastMixin](NATSMessageBroadcastMixin.md) (1 shared connections)
- [PlayerGuidFormatter](PlayerGuidFormatter.md) (1 shared connections)
- [test_websocket_handler_core.py](test_websocket_handler_core.py.md) (1 shared connections)

## Source Files

- `server/realtime/message_formatters.py`
- `server/realtime/nats_message_handler_processing.py`
- `server/tests/unit/realtime/test_message_formatters.py`

## Audit Trail

- EXTRACTED: 113 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*