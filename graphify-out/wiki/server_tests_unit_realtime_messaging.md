# server tests unit realtime messaging

> 41 nodes

## Key Concepts

- **test_message_broadcaster.py** (23 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **asyncio** (15 connections)
- **message_broadcaster()** (4 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **mock_room_manager()** (3 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **mock_send_personal_message()** (3 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_broadcast_global()** (3 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_broadcast_global_batch_exception_falls_back()** (3 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_broadcast_global_empty()** (3 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_broadcast_global_event()** (3 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_broadcast_global_event_error()** (3 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_broadcast_global_exclude_player()** (3 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_broadcast_room_event()** (3 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_broadcast_room_event_error()** (3 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_broadcast_to_room()** (3 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_broadcast_to_room_batch_exception_falls_back()** (3 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_broadcast_to_room_delivery_failure()** (3 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_broadcast_to_room_empty()** (3 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_broadcast_to_room_exclude_player()** (3 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_broadcast_to_room_invalid_player_id()** (3 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_broadcast_to_room_with_uuid_exclude()** (3 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **fixture** (3 connections)
- **test_message_broadcaster_init()** (2 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **Test broadcast_to_room() falls back when batch gather fails.** (2 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **Unit tests for message broadcaster. Tests the MessageBroadcaster class.** (1 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **Test broadcast_global() excludes specified player.** (1 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- *... and 16 more nodes in this community*

## Relationships

- [sendpersonalmessage](sendpersonalmessage.md) (3 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/messaging/test_message_broadcaster.py`

## Audit Trail

- EXTRACTED: 60 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*