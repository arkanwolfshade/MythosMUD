# Community 185

> 73 nodes

## Key Concepts

- **MessageQueue** (52 connections) — `server/realtime/message_queue.py`
- **test_message_queue.py** (32 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **deque** (24 connections)
- **test_message_queue_cleanup_large_structures()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_old_messages()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_old_messages_invalid_timestamp()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_old_messages_removes_empty()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_old_messages_string_timestamp()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_get_messages_error()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_has_messages_empty_list()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **.__init__()** (3 connections) — `server/monitoring/performance_monitor.py`
- **.cleanup_large_structures()** (3 connections) — `server/realtime/message_queue.py`
- **.__init__()** (3 connections) — `server/services/nats_subject_manager/metrics.py`
- **test_message_queue_add_message()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_add_message_error()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_add_message_limit_reached()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_add_message_multiple()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_add_message_with_timestamp()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_large_structures_error()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_old_messages_error()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_get_message_count()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_get_message_count_zero()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_get_messages()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_get_messages_empty()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_get_stats()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- *... and 48 more nodes in this community*

## Relationships

- [Community 42](Community_42.md) (7 shared connections)
- [Community 1139](Community_1139.md) (7 shared connections)
- [Community 354](Community_354.md) (5 shared connections)
- [Community 78](Community_78.md) (2 shared connections)
- [Community 118](Community_118.md) (2 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (2 shared connections)
- [Community 586](Community_586.md) (2 shared connections)
- [Community 518](Community_518.md) (2 shared connections)
- [Community 239](Community_239.md) (1 shared connections)
- [Realtime Message Filtering & Formatting](Realtime_Message_Filtering_&_Formatting.md) (1 shared connections)
- [Community 28](Community_28.md) (1 shared connections)
- [Community 601](Community_601.md) (1 shared connections)

## Source Files

- `server/monitoring/performance_monitor.py`
- `server/realtime/message_queue.py`
- `server/services/nats_metrics.py`
- `server/services/nats_subject_manager/metrics.py`
- `server/tests/unit/realtime/test_message_queue.py`

## Audit Trail

- EXTRACTED: 123 (85%)
- INFERRED: 22 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*