# combat configuration service

> 40 nodes

## Key Concepts

- **test_message_broadcaster.py** (22 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **message_broadcaster()** (3 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **mock_room_manager()** (2 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **mock_send_personal_message()** (2 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_message_broadcaster_init()** (2 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_broadcast_to_room()** (2 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_broadcast_to_room_exclude_player()** (2 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_broadcast_to_room_empty()** (2 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_broadcast_global()** (2 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_broadcast_to_room_with_uuid_exclude()** (2 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_broadcast_to_room_delivery_failure()** (2 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_broadcast_global_exclude_player()** (2 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_broadcast_global_empty()** (2 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_broadcast_room_event()** (2 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_broadcast_to_room_invalid_player_id()** (2 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_broadcast_to_room_batch_exception_falls_back()** (2 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_broadcast_global_batch_exception_falls_back()** (2 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_broadcast_room_event_error()** (2 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_broadcast_global_event()** (2 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_broadcast_global_event_error()** (2 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **Unit tests for message broadcaster.  Tests the MessageBroadcaster class.** (1 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **Create a mock room manager.** (1 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **Create a mock send_personal_message callback.** (1 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **Create a MessageBroadcaster instance.** (1 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **Test MessageBroadcaster initialization.** (1 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- *... and 15 more nodes in this community*

## Relationships

- [realtime messaging message](realtime_messaging_message.md) (3 shared connections)

## Source Files

- `server/tests/unit/realtime/messaging/test_message_broadcaster.py`

## Audit Trail

- EXTRACTED: 81 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*