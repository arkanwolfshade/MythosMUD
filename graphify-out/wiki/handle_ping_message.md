# handle_ping_message

> 6 nodes

## Key Concepts

- **handle_ping_message()** (10 connections) — `server/realtime/message_handlers.py`
- **test_handle_ping_message()** (4 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **test_handle_ping_message_with_data()** (4 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **Handle ping message type.** (1 connections) — `server/realtime/message_handlers.py`
- **Test handle_ping_message() ignores data and sends pong.** (1 connections) — `server/tests/unit/realtime/test_message_handlers.py`
- **Test handle_ping_message() sends pong response.** (1 connections) — `server/tests/unit/realtime/test_message_handlers.py`

## Relationships

- [test_message_handlers.py](test_message_handlers.py.md) (7 shared connections)
- [Any](Any.md) (1 shared connections)
- [build_event](build_event.md) (1 shared connections)
- [message_handler_factory.py](message_handler_factory.py.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/realtime/message_handlers.py`
- `server/tests/unit/realtime/test_message_handlers.py`

## Audit Trail

- EXTRACTED: 16 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*