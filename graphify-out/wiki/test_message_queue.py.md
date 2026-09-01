# test_message_queue.py

> 73 nodes

## Key Concepts

- **test_message_queue.py** (32 connections) — `server/tests/unit/realtime/test_message_queue.py`
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
- **.cleanup_large_structures()** (3 connections) — `server/realtime/message_queue.py`
- **.get_messages()** (3 connections) — `server/realtime/message_queue.py`
- **.get_stats()** (3 connections) — `server/realtime/message_queue.py`
- **test_message_queue_add_message()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_add_message_error()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_add_message_limit_reached()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_add_message_multiple()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_add_message_with_timestamp()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_large_structures_error()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_old_messages_error()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_get_message_count()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_get_message_count_zero()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- *... and 48 more nodes in this community*

## Relationships

- [connection_manager.py](connection_manager.py.md) (38 shared connections)
- [mythos_mud_mapbuilder.py](mythos_mud_mapbuilder.py.md) (5 shared connections)
- [PersonalMessageSender](PersonalMessageSender.md) (2 shared connections)
- [NATSService](NATSService.md) (1 shared connections)
- [ErrorMonitor](ErrorMonitor.md) (1 shared connections)
- [lifespan.py](lifespan.py.md) (1 shared connections)
- [PerformanceMonitor](PerformanceMonitor.md) (1 shared connections)
- [CombatMonitoringService](CombatMonitoringService.md) (1 shared connections)
- [CoordinateGenerator](CoordinateGenerator.md) (1 shared connections)
- [test_metrics.py](test_metrics.py.md) (1 shared connections)
- [time.py](time.py.md) (1 shared connections)

## Source Files

- `server/realtime/message_queue.py`
- `server/services/nats_metrics.py`
- `server/tests/unit/realtime/test_message_queue.py`

## Audit Trail

- EXTRACTED: 111 (84%)
- INFERRED: 21 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*