# ._handle_nats_message

> 8 nodes

## Key Concepts

- **._handle_nats_message()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **._process_message_with_retry()** (5 connections) — `server/realtime/nats_message_handler_processing.py`
- **_optional_str()** (4 connections) — `server/realtime/nats_message_handler_processing.py`
- **_str_field()** (4 connections) — `server/realtime/nats_message_handler_processing.py`
- **Process message with retry logic. Attempts message processing with exponential…** (1 connections) — `server/realtime/nats_message_handler_processing.py`
- **Narrow a message field to str | None.** (1 connections) — `server/realtime/nats_message_handler_processing.py`
- **Narrow a message field to str with a default.** (1 connections) — `server/realtime/nats_message_handler_processing.py`
- **Handle incoming NATS message with error boundaries. Wraps message processing…** (1 connections) — `server/realtime/nats_message_handler_processing.py`

## Relationships

- [NATSMessageProcessingMixin](NATSMessageProcessingMixin.md) (3 shared connections)
- [DeadLetterMessage](DeadLetterMessage.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [test_nats_messages.py](test_nats_messages.py.md) (1 shared connections)

## Source Files

- `server/realtime/nats_message_handler_processing.py`

## Audit Trail

- EXTRACTED: 15 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*