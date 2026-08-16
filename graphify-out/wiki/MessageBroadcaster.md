# MessageBroadcaster

> 25 nodes

## Key Concepts

- **MessageBroadcaster** (19 connections) — `server/realtime/messaging/message_broadcaster.py`
- **UUID** (9 connections)
- **.broadcast_global()** (7 connections) — `server/realtime/messaging/message_broadcaster.py`
- **_stats_counter()** (7 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._deliver_room_broadcast()** (6 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._process_batch_delivery_results()** (6 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._process_global_batch_results()** (6 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._build_target_mapping()** (5 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._fallback_global_individual()** (5 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._fallback_individual_send()** (5 connections) — `server/realtime/messaging/message_broadcaster.py`
- **_global_targets_and_stats()** (4 connections) — `server/realtime/messaging/message_broadcaster.py`
- **.broadcast_global_event()** (4 connections) — `server/realtime/messaging/message_broadcaster.py`
- **_narrow_gather_delivery_dict()** (4 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Convert string player IDs to UUIDs for message sending. Args: target_list: List…** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Process results from batch message delivery. Args: delivery_results: Results…** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Fallback to individual message sending if batch fails. Args: target_mapping:…** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Run batch gather (or fallback) for a room broadcast.** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Merge asyncio.gather outcomes into global broadcast stats.** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Narrow asyncio.gather results when return_exceptions=True.** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Send global broadcast recipients one-by-one after batch failure.** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Broadcast a message to all connected players. Args: event: The event data to…** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Read an integer delivery counter from stats dicts typed as dict[str, object].** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Broadcast a global event to all connected players.** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Compute recipient list and initial stats for broadcast_global.** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Broadcasts messages to rooms and globally. This class provides: - Room-scoped…** (1 connections) — `server/realtime/messaging/message_broadcaster.py`

## Relationships

- [build_event](build_event.md) (6 shared connections)
- [.broadcast_to_room](broadcast_to_room.md) (5 shared connections)
- [RoomSubscriptionManager](RoomSubscriptionManager.md) (2 shared connections)
- [PersonalMessageSender](PersonalMessageSender.md) (1 shared connections)
- [test_message_broadcaster.py](test_message_broadcaster.py.md) (1 shared connections)
- [.__init__](__init__.md) (1 shared connections)
- [message_broadcaster](message_broadcaster.md) (1 shared connections)

## Source Files

- `server/realtime/messaging/message_broadcaster.py`

## Audit Trail

- EXTRACTED: 57 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*