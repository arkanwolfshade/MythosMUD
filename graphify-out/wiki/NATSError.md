# NATSError

> 91 nodes

## Key Concepts

- **NATSError** (70 connections) — `server/services/nats_exceptions.py`
- **nats_exceptions.py** (37 connections) — `server/services/nats_exceptions.py`
- **nats_message_handler.py** (35 connections) — `server/realtime/nats_message_handler.py`
- **nats_message_handler_processing.py** (24 connections) — `server/realtime/nats_message_handler_processing.py`
- **nats_message_handler_base.py** (20 connections) — `server/realtime/nats_message_handler_base.py`
- **format_message_content()** (18 connections) — `server/realtime/message_formatters.py`
- **NATSMessageHandlerMixinBase** (17 connections) — `server/realtime/nats_message_handler_base.py`
- **nats_message_handler_broadcast.py** (16 connections) — `server/realtime/nats_message_handler_broadcast.py`
- **test_message_formatters.py** (16 connections) — `server/tests/unit/realtime/test_message_formatters.py`
- **NATSMessageProcessingMixin** (15 connections) — `server/realtime/nats_message_handler_processing.py`
- **message_filtering.py** (12 connections) — `server/realtime/message_filtering.py`
- **_Handler** (11 connections) — `server/tests/unit/realtime/test_nats_message_handler_base.py`
- **dead_letter_queue.py** (11 connections) — `server/realtime/dead_letter_queue.py`
- **nats_message_handler_subscriptions.py** (10 connections) — `server/realtime/nats_message_handler_subscriptions.py`
- **message_formatters.py** (9 connections) — `server/realtime/message_formatters.py`
- **._process_single_message()** (8 connections) — `server/realtime/nats_message_handler_processing.py`
- **test_nats_message_handler_base.py** (7 connections) — `server/tests/unit/realtime/test_nats_message_handler_base.py`
- **_ChatMessageFields** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **_ValidatedChatFields** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **TestNATSError** (5 connections) — `server/tests/unit/services/test_nats_exceptions.py`
- **._build_chat_event()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._extract_chat_message_fields()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._handle_nats_message()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._process_message_with_retry()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._validate_chat_message_fields()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- *... and 66 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (29 shared connections)
- [NATSPublishError](NATSPublishError.md) (18 shared connections)
- [DeadLetterQueue](DeadLetterQueue.md) (10 shared connections)
- [test_nats_message_handler.py](test_nats_message_handler.py.md) (10 shared connections)
- [CircuitBreaker](CircuitBreaker.md) (8 shared connections)
- [test_nats_message_handler_subzone_events.py](test_nats_message_handler_subzone_events.py.md) (8 shared connections)
- [EventHandler](EventHandler.md) (7 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (7 shared connections)
- [MessageFilteringHelper](MessageFilteringHelper.md) (5 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (5 shared connections)
- [CombatService](CombatService.md) (5 shared connections)
- [logging_file_setup.py](logging_file_setup.py.md) (5 shared connections)

## Source Files

- `server/realtime/dead_letter_queue.py`
- `server/realtime/message_filtering.py`
- `server/realtime/message_formatters.py`
- `server/realtime/nats_message_handler.py`
- `server/realtime/nats_message_handler_base.py`
- `server/realtime/nats_message_handler_broadcast.py`
- `server/realtime/nats_message_handler_processing.py`
- `server/realtime/nats_message_handler_subscriptions.py`
- `server/services/nats_exceptions.py`
- `server/tests/unit/realtime/test_message_formatters.py`
- `server/tests/unit/realtime/test_nats_message_handler_base.py`
- `server/tests/unit/services/test_nats_exceptions.py`

## Audit Trail

- EXTRACTED: 288 (86%)
- INFERRED: 48 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*