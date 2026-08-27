# PersonalMessageSender

> 21 nodes

## Key Concepts

- **PersonalMessageSender** (22 connections) — `server/realtime/messaging/personal_message_sender.py`
- **test_personal_message_sender.py** (17 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **personal_message_sender.py** (16 connections) — `server/realtime/messaging/personal_message_sender.py`
- **asyncio** (8 connections)
- **test_send_to_websocket_accept_first_is_debug_not_warning()** (5 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **test_send_message_fans_out_to_all_listed_sockets()** (4 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
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
- **Personal message delivery for connection management. This module provides…** (1 connections) — `server/realtime/messaging/personal_message_sender.py`
- **Sends personal messages to individual players. This class provides: - Personal…** (1 connections) — `server/realtime/messaging/personal_message_sender.py`
- **Unit tests for PersonalMessageSender.** (1 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **E2E teardown: send after client drop must not warn.** (1 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **Occupancy/who/chat ride the full player_websockets list (#610).** (1 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`

## Relationships

- [.send_message](send_message.md) (7 shared connections)
- [connection_manager.py](connection_manager.py.md) (6 shared connections)
- [DatabaseError](DatabaseError.md) (5 shared connections)
- [MessageBroadcaster](MessageBroadcaster.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (2 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (1 shared connections)
- [PayloadOptimizer](PayloadOptimizer.md) (1 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/realtime/messaging/personal_message_sender.py`
- `server/tests/unit/realtime/test_personal_message_sender.py`

## Audit Trail

- EXTRACTED: 56 (84%)
- INFERRED: 11 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*