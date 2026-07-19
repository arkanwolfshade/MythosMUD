# Message Queue Cleanup

> 84 nodes · cohesion 0.04

## Key Concepts

- **MessageQueue** (56 connections) — `server/realtime/message_queue.py`
- **test_message_queue.py** (30 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **deque** (24 connections) — `data/local/mythos_mud_mapbuilder.py`
- **.add_message()** (4 connections) — `server/realtime/message_queue.py`
- **.cleanup_old_messages()** (4 connections) — `server/realtime/message_queue.py`
- **._is_message_recent()** (4 connections) — `server/realtime/message_queue.py`
- **test_message_queue_cleanup_large_structures()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_old_messages()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_old_messages_invalid_timestamp()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_old_messages_removes_empty()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_old_messages_string_timestamp()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_get_messages_error()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_has_messages_empty_list()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **Any** (4 connections) — `server/realtime/message_queue.py`
- **.__init__()** (3 connections) — `server/monitoring/memory_leak_metrics.py`
- **.__init__()** (3 connections) — `server/monitoring/performance_monitor.py`
- **.__init__()** (3 connections) — `server/services/nats_subject_manager/metrics.py`
- **.cleanup_large_structures()** (3 connections) — `server/realtime/message_queue.py`
- **.get_messages()** (3 connections) — `server/realtime/message_queue.py`
- **.get_stats()** (3 connections) — `server/realtime/message_queue.py`
- **Test MessageQueue.get_messages() handles errors.** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **Test MessageQueue.remove_player_messages() removes all messages.** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_add_message()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_add_message_error()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_add_message_limit_reached()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- *... and 59 more nodes in this community*

## Relationships

- [[Room Occupant Events]] (11 shared connections)
- [[Mythos Map Builder]] (5 shared connections)
- [[Connection Disconnection Cleanup]] (5 shared connections)
- [[NPC Admin API]] (2 shared connections)
- [[Error Monitor Service]] (1 shared connections)
- [[Services Combat Service]] (1 shared connections)
- [[Zone Coordinate Generator]] (1 shared connections)
- [[Memory Leak Metrics]] (1 shared connections)
- [[Performance Monitor Metrics]] (1 shared connections)
- [[Manager Services Nats]] (1 shared connections)
- [[Combat Domain Events]] (1 shared connections)

## Source Files

- `data/local/mythos_mud_mapbuilder.py`
- `server/monitoring/memory_leak_metrics.py`
- `server/monitoring/performance_monitor.py`
- `server/realtime/message_queue.py`
- `server/services/nats_metrics.py`
- `server/services/nats_subject_manager/metrics.py`
- `server/tests/unit/realtime/test_message_queue.py`

## Audit Trail

- EXTRACTED: 248 (86%)
- INFERRED: 40 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
