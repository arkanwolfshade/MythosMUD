# deque

> 31 nodes

## Key Concepts

- **deque** (26 connections)
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
- **Any** (4 connections)
- **.__init__()** (3 connections) — `server/monitoring/memory_leak_metrics.py`
- **.cleanup_large_structures()** (3 connections) — `server/realtime/message_queue.py`
- **.get_messages()** (3 connections) — `server/realtime/message_queue.py`
- **.get_stats()** (3 connections) — `server/realtime/message_queue.py`
- **.__init__()** (2 connections) — `server/services/nats_metrics.py`
- **Initialize the memory leak metrics collector.** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Clean up old messages to prevent memory bloat. Args: max_age_seconds: Maximum…** (1 connections) — `server/realtime/message_queue.py`
- **Clean up large data structures to prevent memory bloat. Args: max_entries:…** (1 connections) — `server/realtime/message_queue.py`
- **Check if a message is recent (within the specified age limit). Args: msg:…** (1 connections) — `server/realtime/message_queue.py`
- **Get message queue statistics. Returns: Dict[str, Any]: Statistics about the…** (1 connections) — `server/realtime/message_queue.py`
- **Add a message to a player's pending message queue. Args: player_id: The…** (1 connections) — `server/realtime/message_queue.py`
- **Get all pending messages for a player and clear the queue. Args: player_id: The…** (1 connections) — `server/realtime/message_queue.py`
- **Test MessageQueue.get_messages() handles errors.** (1 connections) — `server/tests/unit/realtime/test_message_queue.py`
- *... and 6 more nodes in this community*

## Relationships

- [MessageQueue](MessageQueue.md) (15 shared connections)
- [test_message_queue.py](test_message_queue.py.md) (7 shared connections)
- [mythos_mud_mapbuilder.py](mythos_mud_mapbuilder.py.md) (5 shared connections)
- [MemoryLeakMetricsCollector](MemoryLeakMetricsCollector.md) (1 shared connections)
- [NATSMetrics](NATSMetrics.md) (1 shared connections)
- [ErrorMonitor](ErrorMonitor.md) (1 shared connections)
- [PerformanceMonitor](PerformanceMonitor.md) (1 shared connections)
- [.send_message](send_message.md) (1 shared connections)
- [CombatMonitoringService](CombatMonitoringService.md) (1 shared connections)
- [CoordinateGenerator](CoordinateGenerator.md) (1 shared connections)
- [SubjectManagerMetrics](SubjectManagerMetrics.md) (1 shared connections)
- [PersonalMessageSender](PersonalMessageSender.md) (1 shared connections)

## Source Files

- `server/monitoring/memory_leak_metrics.py`
- `server/realtime/message_queue.py`
- `server/services/nats_metrics.py`
- `server/tests/unit/realtime/test_message_queue.py`

## Audit Trail

- EXTRACTED: 39 (58%)
- INFERRED: 28 (42%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*