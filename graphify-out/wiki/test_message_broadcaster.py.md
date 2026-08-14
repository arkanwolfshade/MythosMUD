# test_message_broadcaster.py

> 75 nodes

## Key Concepts

- **test_message_broadcaster.py** (22 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **MessageBroadcaster** (19 connections) — `server/realtime/messaging/message_broadcaster.py`
- **message_broadcaster.py** (15 connections) — `server/realtime/messaging/message_broadcaster.py`
- **asyncio** (15 connections)
- **UUID** (9 connections)
- **.broadcast_global()** (7 connections) — `server/realtime/messaging/message_broadcaster.py`
- **_stats_counter()** (7 connections) — `server/realtime/messaging/message_broadcaster.py`
- **.broadcast_to_room()** (6 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._deliver_room_broadcast()** (6 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._process_batch_delivery_results()** (6 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._process_global_batch_results()** (6 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._build_target_mapping()** (5 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._fallback_global_individual()** (5 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._fallback_individual_send()** (5 connections) — `server/realtime/messaging/message_broadcaster.py`
- **_global_targets_and_stats()** (4 connections) — `server/realtime/messaging/message_broadcaster.py`
- **.broadcast_global_event()** (4 connections) — `server/realtime/messaging/message_broadcaster.py`
- **.broadcast_room_event()** (4 connections) — `server/realtime/messaging/message_broadcaster.py`
- **_narrow_gather_delivery_dict()** (4 connections) — `server/realtime/messaging/message_broadcaster.py`
- **message_broadcaster()** (4 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **._prepare_room_targets()** (3 connections) — `server/realtime/messaging/message_broadcaster.py`
- **mock_room_manager()** (3 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **mock_send_personal_message()** (3 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_broadcast_global()** (3 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_broadcast_global_batch_exception_falls_back()** (3 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **test_broadcast_global_empty()** (3 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- *... and 50 more nodes in this community*

## Relationships

- [connection_manager.py](connection_manager.py.md) (4 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [PersonalMessageSender](PersonalMessageSender.md) (2 shared connections)
- [RoomSubscriptionManager](RoomSubscriptionManager.md) (2 shared connections)

## Source Files

- `server/realtime/messaging/message_broadcaster.py`
- `server/tests/unit/realtime/messaging/test_message_broadcaster.py`

## Audit Trail

- EXTRACTED: 131 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*