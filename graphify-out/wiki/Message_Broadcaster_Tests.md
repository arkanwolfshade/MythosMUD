# Message Broadcaster Tests

> 32 nodes · cohesion 0.06

## Key Concepts

- **test_message_broadcaster.py** (16 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **message_broadcaster()** (3 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_broadcast_global_exclude_player()** (3 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_broadcast_global_event_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_broadcast_room_event_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **mock_room_manager()** (2 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **mock_send_personal_message()** (2 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **Test broadcast_global() when no players online.** (2 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **Test broadcast_room_event() broadcasts room event.** (2 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **Test broadcast_global_event() broadcasts global event.** (2 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_broadcast_global()** (2 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_broadcast_global_empty()** (2 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_broadcast_global_event()** (2 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_broadcast_room_event()** (2 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_broadcast_to_room()** (2 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_broadcast_to_room_delivery_failure()** (2 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_broadcast_to_room_empty()** (2 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_broadcast_to_room_exclude_player()** (2 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_broadcast_to_room_with_uuid_exclude()** (2 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_message_broadcaster_init()** (2 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **Unit tests for message broadcaster.  Tests the MessageBroadcaster class.** (1 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **Test broadcast_global() excludes specified player.** (1 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **Create a mock room manager.** (1 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **Create a mock send_personal_message callback.** (1 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **Create a MessageBroadcaster instance.** (1 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- *... and 7 more nodes in this community*

## Relationships

- [[Realtime Connection Impl]] (4 shared connections)
- [[Message Broadcaster Core]] (2 shared connections)

## Source Files

- `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- `server/tests/unit/realtime/test_connection_helpers_impl.py`

## Audit Trail

- EXTRACTED: 70 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
