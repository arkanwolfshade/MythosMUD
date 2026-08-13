# MessageQueue

> 68 nodes

## Key Concepts

- **MessageQueue** (50 connections) — `server/realtime/message_queue.py`
- **test_message_queue.py** (32 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_large_structures()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_old_messages()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_old_messages_invalid_timestamp()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_old_messages_removes_empty()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_old_messages_string_timestamp()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_get_messages_error()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_has_messages_empty_list()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
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
- **test_message_queue_get_stats_empty()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_get_stats_error()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_has_messages_false()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_has_messages_true()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- *... and 43 more nodes in this community*

## Relationships

- [deque](deque.md) (13 shared connections)
- [get_logger](get_logger.md) (9 shared connections)
- [test_connection_disconnection.py](test_connection_disconnection.py.md) (3 shared connections)

## Source Files

- `server/realtime/message_queue.py`
- `server/tests/unit/realtime/test_message_queue.py`

## Audit Trail

- EXTRACTED: 112 (93%)
- INFERRED: 8 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*