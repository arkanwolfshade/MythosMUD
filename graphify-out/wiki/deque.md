# deque

> 20 nodes

## Key Concepts

- **deque** (24 connections)
- **.add_message()** (4 connections) — `server/realtime/message_queue.py`
- **.cleanup_old_messages()** (4 connections) — `server/realtime/message_queue.py`
- **._is_message_recent()** (4 connections) — `server/realtime/message_queue.py`
- **Any** (4 connections)
- **.__init__()** (3 connections) — `server/monitoring/memory_leak_metrics.py`
- **.__init__()** (3 connections) — `server/monitoring/performance_monitor.py`
- **.cleanup_large_structures()** (3 connections) — `server/realtime/message_queue.py`
- **.get_messages()** (3 connections) — `server/realtime/message_queue.py`
- **.get_stats()** (3 connections) — `server/realtime/message_queue.py`
- **.__init__()** (3 connections) — `server/services/nats_subject_manager/metrics.py`
- **Initialize the memory leak metrics collector.** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Initialize the performance monitor. Args: max_metrics: Maximum number of…** (1 connections) — `server/monitoring/performance_monitor.py`
- **Clean up old messages to prevent memory bloat. Args: max_age_seconds: Maximum…** (1 connections) — `server/realtime/message_queue.py`
- **Clean up large data structures to prevent memory bloat. Args: max_entries:…** (1 connections) — `server/realtime/message_queue.py`
- **Check if a message is recent (within the specified age limit). Args: msg:…** (1 connections) — `server/realtime/message_queue.py`
- **Get message queue statistics. Returns: Dict[str, Any]: Statistics about the…** (1 connections) — `server/realtime/message_queue.py`
- **Add a message to a player's pending message queue. Args: player_id: The…** (1 connections) — `server/realtime/message_queue.py`
- **Get all pending messages for a player and clear the queue. Args: player_id: The…** (1 connections) — `server/realtime/message_queue.py`
- **Initialize metrics collection.** (1 connections) — `server/services/nats_subject_manager/metrics.py`

## Relationships

- [MessageQueue](MessageQueue.md) (13 shared connections)
- [mythos_mud_mapbuilder.py](mythos_mud_mapbuilder.py.md) (5 shared connections)
- [lifespan.py](lifespan.py.md) (1 shared connections)
- [LucidityFluxService](LucidityFluxService.md) (1 shared connections)
- [test_metrics.py](test_metrics.py.md) (1 shared connections)
- [ErrorMonitor](ErrorMonitor.md) (1 shared connections)
- [test_connection_initialization.py](test_connection_initialization.py.md) (1 shared connections)
- [PersonalMessageSender](PersonalMessageSender.md) (1 shared connections)
- [CombatMonitoringService](CombatMonitoringService.md) (1 shared connections)
- [CoordinateGenerator](CoordinateGenerator.md) (1 shared connections)
- [NATSMetrics](NATSMetrics.md) (1 shared connections)

## Source Files

- `server/monitoring/memory_leak_metrics.py`
- `server/monitoring/performance_monitor.py`
- `server/realtime/message_queue.py`
- `server/services/nats_subject_manager/metrics.py`

## Audit Trail

- EXTRACTED: 28 (60%)
- INFERRED: 19 (40%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*