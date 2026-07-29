# . init ()

> 69 nodes

## Key Concepts

- **MessageQueue** (45 connections) — `server/realtime/message_queue.py`
- **test_message_queue.py** (32 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **deque** (22 connections)
- **test_message_queue_get_messages_error()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_has_messages_empty_list()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_old_messages()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_old_messages_removes_empty()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_old_messages_string_timestamp()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_old_messages_invalid_timestamp()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_large_structures()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **.cleanup_large_structures()** (3 connections) — `server/realtime/message_queue.py`
- **.__init__()** (3 connections) — `server/services/nats_subject_manager/metrics.py`
- **test_message_queue_init_defaults()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_init_custom()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_add_message()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_add_message_with_timestamp()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_add_message_multiple()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_add_message_limit_reached()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_add_message_error()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_get_messages()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_get_messages_empty()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_has_messages_true()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_has_messages_false()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_get_message_count()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_get_message_count_zero()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- *... and 44 more nodes in this community*

## Relationships

- [.add message()](add_message%28%29.md) (7 shared connections)
- [Coord](Coord.md) (5 shared connections)
- [main()](main%28%29.md) (5 shared connections)
- [connection disconnection](connection_disconnection.md) (2 shared connections)
- [error monitoring](error_monitoring.md) (1 shared connections)
- [.initialize()](initialize%28%29.md) (1 shared connections)
- [PersonalMessageSender](PersonalMessageSender.md) (1 shared connections)
- [. init ()](_init_%28%29.md) (1 shared connections)
- [CoordinateGenerator](CoordinateGenerator.md) (1 shared connections)
- [NATSMetrics](NATSMetrics.md) (1 shared connections)
- [Any](Any.md) (1 shared connections)

## Source Files

- `server/realtime/message_queue.py`
- `server/services/nats_metrics.py`
- `server/services/nats_subject_manager/metrics.py`
- `server/tests/unit/realtime/test_message_queue.py`

## Audit Trail

- EXTRACTED: 214 (88%)
- INFERRED: 28 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*