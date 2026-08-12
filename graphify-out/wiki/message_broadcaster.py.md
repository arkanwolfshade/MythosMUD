# message_broadcaster.py

> 17 nodes

## Key Concepts

- **message_broadcaster.py** (15 connections) — `server/realtime/messaging/message_broadcaster.py`
- **UUID** (9 connections)
- **.broadcast_global()** (7 connections) — `server/realtime/messaging/message_broadcaster.py`
- **_stats_counter()** (7 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._process_batch_delivery_results()** (6 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._process_global_batch_results()** (6 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._fallback_global_individual()** (5 connections) — `server/realtime/messaging/message_broadcaster.py`
- **_global_targets_and_stats()** (4 connections) — `server/realtime/messaging/message_broadcaster.py`
- **_narrow_gather_delivery_dict()** (4 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Message broadcasting for connection management. This module provides room and…** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Process results from batch message delivery. Args: delivery_results: Results…** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Merge asyncio.gather outcomes into global broadcast stats.** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Narrow asyncio.gather results when return_exceptions=True.** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Send global broadcast recipients one-by-one after batch failure.** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Broadcast a message to all connected players. Args: event: The event data to…** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Read an integer delivery counter from stats dicts typed as dict[str, object].** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Compute recipient list and initial stats for broadcast_global.** (1 connections) — `server/realtime/messaging/message_broadcaster.py`

## Relationships

- [MessageBroadcaster](MessageBroadcaster.md) (8 shared connections)
- [._deliver_room_broadcast](_deliver_room_broadcast.md) (5 shared connections)
- [RateLimiter](RateLimiter.md) (3 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [build_event](build_event.md) (2 shared connections)
- [test_message_broadcaster.py](test_message_broadcaster.py.md) (1 shared connections)

## Source Files

- `server/realtime/messaging/message_broadcaster.py`

## Audit Trail

- EXTRACTED: 71 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*