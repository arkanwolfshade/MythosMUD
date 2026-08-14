# PersonalMessageSender

> 35 nodes

## Key Concepts

- **PersonalMessageSender** (21 connections) — `server/realtime/messaging/personal_message_sender.py`
- **personal_message_sender.py** (15 connections) — `server/realtime/messaging/personal_message_sender.py`
- **test_personal_message_sender.py** (14 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **.send_message()** (7 connections) — `server/realtime/messaging/personal_message_sender.py`
- **UUID** (7 connections)
- **asyncio** (7 connections)
- **._prepare_payload()** (6 connections) — `server/realtime/messaging/personal_message_sender.py`
- **._queue_message_if_needed()** (6 connections) — `server/realtime/messaging/personal_message_sender.py`
- **._send_to_websocket()** (6 connections) — `server/realtime/messaging/personal_message_sender.py`
- **Any** (6 connections)
- **test_send_to_websocket_accept_first_is_debug_not_warning()** (5 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **server/realtime/messaging/__init__.py** (5 connections) — `server/realtime/messaging/__init__.py`
- **.get_delivery_stats()** (4 connections) — `server/realtime/messaging/personal_message_sender.py`
- **.__init__()** (4 connections) — `server/realtime/messaging/personal_message_sender.py`
- **test_send_message_outer_exception()** (4 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **test_send_to_websocket_empty_runtime_error_is_debug()** (4 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **sender()** (3 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **test_get_delivery_stats()** (3 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **test_prepare_payload_too_large()** (3 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **test_send_message_delivers_via_websocket()** (3 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **test_send_message_queues_when_offline()** (3 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **test_send_to_websocket_disconnect()** (3 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **LogCaptureFixture** (2 connections)
- **fixture** (1 connections)
- **Messaging components for connection management. This package provides modular…** (1 connections) — `server/realtime/messaging/__init__.py`
- *... and 10 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (7 shared connections)
- [connection_manager.py](connection_manager.py.md) (4 shared connections)
- [PayloadOptimizer](PayloadOptimizer.md) (2 shared connections)
- [deque](deque.md) (2 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (2 shared connections)
- [test_message_broadcaster.py](test_message_broadcaster.py.md) (2 shared connections)
- [MessageQueue](MessageQueue.md) (1 shared connections)
- [websocket_helpers.py](websocket_helpers.py.md) (1 shared connections)

## Source Files

- `server/realtime/messaging/__init__.py`
- `server/realtime/messaging/personal_message_sender.py`
- `server/tests/unit/realtime/test_personal_message_sender.py`

## Audit Trail

- EXTRACTED: 85 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*