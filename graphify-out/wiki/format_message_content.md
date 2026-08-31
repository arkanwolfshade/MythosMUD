# format_message_content

> 53 nodes

## Key Concepts

- **format_message_content()** (18 connections) — `server/realtime/message_formatters.py`
- **NATSMessageProcessingMixin** (15 connections) — `server/realtime/nats_message_handler_processing.py`
- **CircuitBreakerOpen** (12 connections) — `server/realtime/circuit_breaker.py`
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
- **test_format_message_content_whisper_for_recipient()** (3 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- *... and 28 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (13 shared connections)
- [NATSError](NATSError.md) (12 shared connections)
- [test_nats_message_handler.py](test_nats_message_handler.py.md) (3 shared connections)
- [DeadLetterQueue](DeadLetterQueue.md) (3 shared connections)
- [test_circuit_breaker.py](test_circuit_breaker.py.md) (2 shared connections)
- [.call](call.md) (1 shared connections)
- [asyncio](asyncio.md) (1 shared connections)
- [GameStateProvider](GameStateProvider.md) (1 shared connections)
- [NATSMessageBroadcastMixin](NATSMessageBroadcastMixin.md) (1 shared connections)
- [build_event](build_event.md) (1 shared connections)
- [test_nats_messages.py](test_nats_messages.py.md) (1 shared connections)

## Source Files

- `server/realtime/circuit_breaker.py`
- `server/realtime/message_formatters.py`
- `server/realtime/nats_message_handler_processing.py`
- `server/tests/unit/realtime/test_message_formatters.py`

## Audit Trail

- EXTRACTED: 97 (95%)
- INFERRED: 5 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*