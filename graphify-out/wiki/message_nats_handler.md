# message nats handler

> 22 nodes

## Key Concepts

- **deque** (25 connections)
- **test_message_queue_get_messages_error()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_has_messages_empty_list()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_old_messages()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_old_messages_removes_empty()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_old_messages_string_timestamp()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_old_messages_invalid_timestamp()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_large_structures()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **.__init__()** (3 connections) — `server/monitoring/memory_leak_metrics.py`
- **.cleanup_large_structures()** (3 connections) — `server/realtime/message_queue.py`
- **.__init__()** (3 connections) — `server/services/nats_subject_manager/metrics.py`
- **.__init__()** (2 connections) — `server/services/nats_metrics.py`
- **Initialize the memory leak metrics collector.** (1 connections) — `server/monitoring/memory_leak_metrics.py`
- **Clean up large data structures to prevent memory bloat.          Args:** (1 connections) — `server/realtime/message_queue.py`
- **Initialize metrics collection.** (1 connections) — `server/services/nats_subject_manager/metrics.py`
- **Test MessageQueue.get_messages() handles errors.** (1 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **Test MessageQueue.has_messages() returns False for empty list.** (1 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **Test MessageQueue.cleanup_old_messages() removes old messages.** (1 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **Test MessageQueue.cleanup_old_messages() removes empty queues.** (1 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **Test MessageQueue.cleanup_old_messages() handles ISO string timestamps.** (1 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **Test MessageQueue.cleanup_old_messages() handles invalid timestamps.** (1 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **Test MessageQueue.cleanup_large_structures() trims large queues.** (1 connections) — `server/tests/unit/realtime/test_message_queue.py`

## Relationships

- [Room Broadcast](Room_Broadcast.md) (11 shared connections)
- [connection disconnection realtime](connection_disconnection_realtime.md) (7 shared connections)
- [mythos mud mapbuilder](mythos_mud_mapbuilder.md) (5 shared connections)
- [main rationale failure()](main_rationale_failure%28%29.md) (2 shared connections)
- [error monitoring scripts](error_monitoring_scripts.md) (1 shared connections)
- [command inventory factories](command_inventory_factories.md) (1 shared connections)
- [combat monitoring service](combat_monitoring_service.md) (1 shared connections)
- [coordinate services generator](coordinate_services_generator.md) (1 shared connections)
- [command combat models](command_combat_models.md) (1 shared connections)
- [nats services service](nats_services_service.md) (1 shared connections)
- [subject validation services](subject_validation_services.md) (1 shared connections)

## Source Files

- `server/monitoring/memory_leak_metrics.py`
- `server/realtime/message_queue.py`
- `server/services/nats_metrics.py`
- `server/services/nats_subject_manager/metrics.py`
- `server/tests/unit/realtime/test_message_queue.py`

## Audit Trail

- EXTRACTED: 43 (58%)
- INFERRED: 31 (42%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*