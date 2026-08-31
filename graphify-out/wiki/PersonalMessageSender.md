# PersonalMessageSender

> 70 nodes

## Key Concepts

- **PersonalMessageSender** (22 connections) — `server/realtime/messaging/personal_message_sender.py`
- **PayloadOptimizer** (22 connections) — `server/realtime/payload_optimizer.py`
- **test_payload_optimizer.py** (20 connections) — `server/tests/unit/realtime/test_payload_optimizer.py`
- **test_personal_message_sender.py** (17 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **get_payload_optimizer()** (9 connections) — `server/realtime/payload_optimizer.py`
- **asyncio** (8 connections)
- **.send_message()** (7 connections) — `server/realtime/messaging/personal_message_sender.py`
- **UUID** (7 connections)
- **._prepare_payload()** (6 connections) — `server/realtime/messaging/personal_message_sender.py`
- **._queue_message_if_needed()** (6 connections) — `server/realtime/messaging/personal_message_sender.py`
- **._send_to_websocket()** (6 connections) — `server/realtime/messaging/personal_message_sender.py`
- **Any** (6 connections)
- **payload_optimizer.py** (6 connections) — `server/realtime/payload_optimizer.py`
- **.optimize_payload()** (5 connections) — `server/realtime/payload_optimizer.py`
- **test_send_to_websocket_accept_first_is_debug_not_warning()** (5 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **.get_delivery_stats()** (4 connections) — `server/realtime/messaging/personal_message_sender.py`
- **.__init__()** (4 connections) — `server/realtime/messaging/personal_message_sender.py`
- **.compress_payload()** (4 connections) — `server/realtime/payload_optimizer.py`
- **.get_payload_size()** (4 connections) — `server/realtime/payload_optimizer.py`
- **optimizer()** (4 connections) — `server/tests/unit/realtime/test_payload_optimizer.py`
- **test_send_message_fans_out_to_all_listed_sockets()** (4 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **test_send_message_outer_exception()** (4 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **test_send_to_websocket_empty_runtime_error_is_debug()** (4 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **Any** (4 connections)
- **_CompareExplodes** (3 connections) — `server/tests/unit/realtime/test_payload_optimizer.py`
- *... and 45 more nodes in this community*

## Relationships

- [connection_manager_methods.py](connection_manager_methods.py.md) (8 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [pytest.md](pytest.md.md) (3 shared connections)
- [DatabaseError](DatabaseError.md) (2 shared connections)
- [MessageBroadcaster](MessageBroadcaster.md) (1 shared connections)
- [websocket_handler.py](websocket_handler.py.md) (1 shared connections)
- [test_connection_helpers_impl.py](test_connection_helpers_impl.py.md) (1 shared connections)
- [test_container_helpers_inventory_ops.py](test_container_helpers_inventory_ops.py.md) (1 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (1 shared connections)

## Source Files

- `server/realtime/messaging/personal_message_sender.py`
- `server/realtime/payload_optimizer.py`
- `server/tests/unit/realtime/test_payload_optimizer.py`
- `server/tests/unit/realtime/test_personal_message_sender.py`

## Audit Trail

- EXTRACTED: 121 (84%)
- INFERRED: 23 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*