# NATSMessageHandlerMixinBase

> 14 nodes

## Key Concepts

- **NATSMessageHandlerMixinBase** (17 connections) — `server/realtime/nats_message_handler_base.py`
- **_Handler** (11 connections) — `server/tests/unit/realtime/test_nats_message_handler_base.py`
- **test_nats_message_handler_base.py** (7 connections) — `server/tests/unit/realtime/test_nats_message_handler_base.py`
- **_setup_async_logging_queue()** (5 connections) — `server/structured_logging/logging_file_setup.py`
- **test_subscribe_stub_returns_false()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler_base.py`
- **test_unsubscribe_stub_returns_false()** (3 connections) — `server/tests/unit/realtime/test_nats_message_handler_base.py`
- **QueueListener** (2 connections)
- **asyncio** (2 connections)
- **._subscribe_to_subject()** (1 connections) — `server/realtime/nats_message_handler_base.py`
- **._unsubscribe_from_subject()** (1 connections) — `server/realtime/nats_message_handler_base.py`
- **Attrs/methods provided by NATSMessageHandler when mixed in.** (1 connections) — `server/realtime/nats_message_handler_base.py`
- **Set up async logging queue listener for non-blocking file I/O. Uses…** (1 connections) — `server/structured_logging/logging_file_setup.py`
- **Unit tests for NATSMessageHandlerMixinBase stubs.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_base.py`
- **Concrete subclass for testing mixin stubs.** (1 connections) — `server/tests/unit/realtime/test_nats_message_handler_base.py`

## Relationships

- [logging_file_setup.py](logging_file_setup.py.md) (7 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [CircuitBreaker](CircuitBreaker.md) (2 shared connections)
- [EventHandler](EventHandler.md) (1 shared connections)
- [MessageFilteringHelper](MessageFilteringHelper.md) (1 shared connections)
- [DeadLetterQueue](DeadLetterQueue.md) (1 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (1 shared connections)
- [NATSMessageBroadcastMixin](NATSMessageBroadcastMixin.md) (1 shared connections)
- [NATSMessageProcessingMixin](NATSMessageProcessingMixin.md) (1 shared connections)
- [NATSMessageSubscriptionMixin](NATSMessageSubscriptionMixin.md) (1 shared connections)
- [test_logging_file_setup.py](test_logging_file_setup.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/realtime/nats_message_handler_base.py`
- `server/structured_logging/logging_file_setup.py`
- `server/tests/unit/realtime/test_nats_message_handler_base.py`

## Audit Trail

- EXTRACTED: 30 (77%)
- INFERRED: 9 (23%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*