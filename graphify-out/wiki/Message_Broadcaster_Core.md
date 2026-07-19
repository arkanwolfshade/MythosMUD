# Message Broadcaster Core

> 31 nodes · cohesion 0.11

## Key Concepts

- **MessageBroadcaster** (20 connections) — `server/realtime/messaging/message_broadcaster.py`
- **UUID** (9 connections) — `server/realtime/messaging/message_broadcaster.py`
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
- **._prepare_room_targets()** (3 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Convert string player IDs to UUIDs for message sending.          Args:** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Process results from batch message delivery.          Args:             delivery** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Fallback to individual message sending if batch fails.          Args:** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Dedupe subscribers and count exclusions.** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Run batch gather (or fallback) for a room broadcast.** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Broadcast a message to all players in a room.          Args:             room_id** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Merge asyncio.gather outcomes into global broadcast stats.** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Narrow asyncio.gather results when return_exceptions=True.** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Send global broadcast recipients one-by-one after batch failure.** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- *... and 6 more nodes in this community*

## Relationships

- [[Combat Player Broadcasts]] (8 shared connections)
- [[Room Occupant Events]] (3 shared connections)
- [[Message Broadcaster Tests]] (2 shared connections)
- [[Realtime Messaging Message]] (1 shared connections)

## Source Files

- `server/realtime/messaging/message_broadcaster.py`

## Audit Trail

- EXTRACTED: 116 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
