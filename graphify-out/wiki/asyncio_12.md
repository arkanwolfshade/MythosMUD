# asyncio

> 15 nodes

## Key Concepts

- **asyncio** (7 connections)
- **test_chat_message_handler_handle()** (4 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **test_client_error_report_handler_logs()** (4 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **test_command_message_handler_handle()** (4 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **test_message_handler_factory_handle_message_no_type()** (4 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **test_message_handler_factory_handle_message_success()** (4 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **test_message_handler_factory_handle_message_unknown_type()** (4 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **test_ping_message_handler_handle()** (4 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **Test MessageHandlerFactory.handle_message() successfully handles message.** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **Test MessageHandlerFactory.handle_message() sends error for unknown type.** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **Test MessageHandlerFactory.handle_message() handles message with no type.** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **Test ClientErrorReportMessageHandler logs via logger.error.** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **Test CommandMessageHandler.handle() calls handle_command_message.** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **Test ChatMessageHandler.handle() calls handle_chat_message.** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`
- **Test PingMessageHandler.handle() calls handle_ping_message.** (1 connections) — `server/tests/unit/realtime/test_message_handler_factory.py`

## Relationships

- [message_handler_factory.py](message_handler_factory.py.md) (11 shared connections)
- [MessageHandlerFactory](MessageHandlerFactory.md) (3 shared connections)

## Source Files

- `server/tests/unit/realtime/test_message_handler_factory.py`

## Audit Trail

- EXTRACTED: 21 (75%)
- INFERRED: 7 (25%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*