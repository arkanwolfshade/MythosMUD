# SendPersonalMessage

> 38 nodes

## Key Concepts

- **MessageBroadcaster** (17 connections) — `server/realtime/messaging/message_broadcaster.py`
- **message_broadcaster.py** (14 connections) — `server/realtime/messaging/message_broadcaster.py`
- **UUID** (9 connections)
- **_stats_counter()** (7 connections) — `server/realtime/messaging/message_broadcaster.py`
- **.broadcast_global()** (7 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._process_batch_delivery_results()** (6 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._deliver_room_broadcast()** (6 connections) — `server/realtime/messaging/message_broadcaster.py`
- **.broadcast_to_room()** (6 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._process_global_batch_results()** (6 connections) — `server/realtime/messaging/message_broadcaster.py`
- **__init__.py** (5 connections) — `server/realtime/messaging/__init__.py`
- **._build_target_mapping()** (5 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._fallback_individual_send()** (5 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._fallback_global_individual()** (5 connections) — `server/realtime/messaging/message_broadcaster.py`
- **_narrow_gather_delivery_dict()** (4 connections) — `server/realtime/messaging/message_broadcaster.py`
- **_global_targets_and_stats()** (4 connections) — `server/realtime/messaging/message_broadcaster.py`
- **.__init__()** (4 connections) — `server/realtime/messaging/message_broadcaster.py`
- **.broadcast_room_event()** (4 connections) — `server/realtime/messaging/message_broadcaster.py`
- **.broadcast_global_event()** (4 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._prepare_room_targets()** (3 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Messaging components for connection management.  This package provides modular m** (1 connections) — `server/realtime/messaging/__init__.py`
- **SendPersonalMessage** (1 connections)
- **Message broadcasting for connection management.  This module provides room and g** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Narrow asyncio.gather results when return_exceptions=True.** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Read an integer delivery counter from stats dicts typed as dict[str, object].** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Compute recipient list and initial stats for broadcast_global.** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- *... and 13 more nodes in this community*

## Relationships

- [main()](main%28%29.md) (4 shared connections)
- [UUID](UUID.md) (4 shared connections)
- [test message broadcaster](test_message_broadcaster.md) (3 shared connections)
- [Any](Any.md) (2 shared connections)
- [PersonalMessageSender](PersonalMessageSender.md) (1 shared connections)

## Source Files

- `server/realtime/messaging/__init__.py`
- `server/realtime/messaging/message_broadcaster.py`

## Audit Trail

- EXTRACTED: 140 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*