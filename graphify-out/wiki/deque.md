# deque

> 83 nodes

## Key Concepts

- **MessageQueue** (48 connections) — `server/realtime/message_queue.py`
- **test_message_queue.py** (32 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **deque** (25 connections)
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
- **.__init__()** (3 connections) — `server/services/nats_subject_manager/metrics.py`
- **test_message_queue_add_message()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_add_message_error()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_add_message_limit_reached()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_add_message_multiple()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_add_message_with_timestamp()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_large_structures_error()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- *... and 58 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (6 shared connections)
- [coord](coord.md) (5 shared connections)
- [server realtime messaging personal message](server_realtime_messaging_personal_message.md) (3 shared connections)
- [server realtime connection session management](server_realtime_connection_session_management.md) (2 shared connections)
- [server realtime connection initialization initialize](server_realtime_connection_initialization_initialize.md) (2 shared connections)
- [server monitoring memory leak metrics](server_monitoring_memory_leak_metrics.md) (1 shared connections)
- [server services nats subject manager](server_services_nats_subject_manager.md) (1 shared connections)
- [scripts error monitoring](scripts_error_monitoring.md) (1 shared connections)
- [server monitoring init getattr](server_monitoring_init_getattr.md) (1 shared connections)
- [server services combat monitoring service](server_services_combat_monitoring_service.md) (1 shared connections)
- [server services coordinate generator coordinategenerator](server_services_coordinate_generator_coordinategenerator.md) (1 shared connections)
- [server services nats metrics natsmetrics](server_services_nats_metrics_natsmetrics.md) (1 shared connections)

## Source Files

- `server/monitoring/memory_leak_metrics.py`
- `server/realtime/message_queue.py`
- `server/services/nats_subject_manager/metrics.py`
- `server/tests/unit/realtime/test_message_queue.py`

## Audit Trail

- EXTRACTED: 101 (67%)
- INFERRED: 50 (33%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*