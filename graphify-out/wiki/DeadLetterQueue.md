# DeadLetterQueue

> 134 nodes

## Key Concepts

- **DeadLetterQueue** (37 connections) — `server/realtime/dead_letter_queue.py`
- **DeadLetterMessage** (28 connections) — `server/realtime/dead_letter_queue.py`
- **test_dead_letter_queue.py** (28 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **format_message_content()** (18 connections) — `server/realtime/message_formatters.py`
- **test_message_formatters.py** (16 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **NATSMessageProcessingMixin** (15 connections) — `server/realtime/nats_message_handler_processing.py`
- **._process_single_message()** (8 connections) — `server/realtime/nats_message_handler_processing.py`
- **Any** (7 connections)
- **.from_dict()** (6 connections) — `server/realtime/dead_letter_queue.py`
- **_ChatMessageFields** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **_ValidatedChatFields** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._build_chat_event()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._extract_chat_message_fields()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._handle_nats_message()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._process_message_with_retry()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._validate_chat_message_fields()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **Path** (5 connections)
- **.enqueue()** (4 connections) — `server/realtime/dead_letter_queue.py`
- **.enqueue_async()** (4 connections) — `server/realtime/dead_letter_queue.py`
- **.__init__()** (4 connections) — `server/realtime/dead_letter_queue.py`
- **.replay_message()** (4 connections) — `server/realtime/dead_letter_queue.py`
- **._broadcast_by_channel_type()** (4 connections) — `server/realtime/nats_message_handler_processing.py`
- **._convert_ids_to_uuids()** (4 connections) — `server/realtime/nats_message_handler_processing.py`
- **_optional_str()** (4 connections) — `server/realtime/nats_message_handler_processing.py`
- **_str_field()** (4 connections) — `server/realtime/nats_message_handler_processing.py`
- *... and 109 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (17 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (4 shared connections)
- [PlayerEventHandlerUtils](PlayerEventHandlerUtils.md) (2 shared connections)
- [NATSError](NATSError.md) (2 shared connections)
- [CircuitBreakerOpen](CircuitBreakerOpen.md) (1 shared connections)
- [get_config](get_config.md) (1 shared connections)
- [build_event](build_event.md) (1 shared connections)
- [test_nats_messages.py](test_nats_messages.py.md) (1 shared connections)
- [nats_exceptions.py](nats_exceptions.py.md) (1 shared connections)

## Source Files

- `server/realtime/dead_letter_queue.py`
- `server/realtime/message_formatters.py`
- `server/realtime/nats_message_handler_processing.py`
- `server/tests/unit/realtime/test_dead_letter_queue.py`
- `server/tests/unit/realtime/test_message_formatters.py`

## Audit Trail

- EXTRACTED: 195 (82%)
- INFERRED: 43 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*