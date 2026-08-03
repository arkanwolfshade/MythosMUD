# message nats handler

> 63 nodes

## Key Concepts

- **DeadLetterMessage** (27 connections) — `server/realtime/dead_letter_queue.py`
- **format_message_content()** (18 connections) — `server/realtime/message_formatters.py`
- **NATSMessageHandlerMixinBase** (17 connections) — `server/realtime/nats_message_handler_base.py`
- **test_message_formatters.py** (16 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **NATSMessageProcessingMixin** (15 connections) — `server/realtime/nats_message_handler_processing.py`
- **CircuitBreakerOpen** (14 connections) — `server/realtime/circuit_breaker.py`
- **_ChatMessageFields** (8 connections) — `server/realtime/nats_message_handler_processing.py`
- **_ValidatedChatFields** (8 connections) — `server/realtime/nats_message_handler_processing.py`
- **._process_single_message()** (8 connections) — `server/realtime/nats_message_handler_processing.py`
- **._handle_nats_message()** (6 connections) — `server/realtime/nats_message_handler_processing.py`
- **._process_message_with_retry()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._extract_chat_message_fields()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._validate_chat_message_fields()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._build_chat_event()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._broadcast_by_channel_type()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **_optional_str()** (4 connections) — `server/realtime/nats_message_handler_processing.py`
- **_str_field()** (4 connections) — `server/realtime/nats_message_handler_processing.py`
- **._convert_ids_to_uuids()** (4 connections) — `server/realtime/nats_message_handler_processing.py`
- **test_format_message_content_nats_error()** (4 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **UUID** (3 connections)
- **test_format_message_content_say()** (3 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **test_format_message_content_local()** (3 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **test_format_message_content_global()** (3 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **test_format_message_content_emote()** (3 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **test_format_message_content_pose()** (3 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- *... and 38 more nodes in this community*

## Relationships

- [NATS Messaging](NATS_Messaging.md) (19 shared connections)
- [realtime dead letter](realtime_dead_letter.md) (9 shared connections)
- [dead letter queue](dead_letter_queue.md) (6 shared connections)
- [Item Instances](Item_Instances.md) (5 shared connections)
- [dead letter realtime](dead_letter_realtime.md) (4 shared connections)
- [circuit breaker realtime](circuit_breaker_realtime.md) (3 shared connections)
- [nats message handler](nats_message_handler.md) (2 shared connections)
- [message broadcast realtime](message_broadcast_realtime.md) (2 shared connections)
- [realtime message filtering](realtime_message_filtering.md) (2 shared connections)
- [realtime circuit breaker](realtime_circuit_breaker.md) (1 shared connections)
- [realtime message nats](realtime_message_nats.md) (1 shared connections)
- [game room service](game_room_service.md) (1 shared connections)

## Source Files

- `server/realtime/circuit_breaker.py`
- `server/realtime/dead_letter_queue.py`
- `server/realtime/message_formatters.py`
- `server/realtime/nats_message_handler_base.py`
- `server/realtime/nats_message_handler_processing.py`
- `server/tests/unit/realtime/test_message_formatters.py`

## Audit Trail

- EXTRACTED: 216 (88%)
- INFERRED: 29 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*