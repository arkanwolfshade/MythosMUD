# nats config()

> 83 nodes

## Key Concepts

- **MessageQueue** (54 connections) — `server/realtime/message_queue.py`
- **test_message_queue.py** (32 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **mock_manager()** (5 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **.add_message()** (4 connections) — `server/realtime/message_queue.py`
- **Any** (4 connections)
- **.cleanup_old_messages()** (4 connections) — `server/realtime/message_queue.py`
- **._is_message_recent()** (4 connections) — `server/realtime/message_queue.py`
- **test_message_queue_get_messages_error()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_has_messages_empty_list()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_old_messages()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_old_messages_removes_empty()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_old_messages_string_timestamp()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_old_messages_invalid_timestamp()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_cleanup_large_structures()** (4 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **.get_messages()** (3 connections) — `server/realtime/message_queue.py`
- **.cleanup_large_structures()** (3 connections) — `server/realtime/message_queue.py`
- **.get_stats()** (3 connections) — `server/realtime/message_queue.py`
- **test_message_queue_init_defaults()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_init_custom()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_add_message()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_add_message_with_timestamp()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_add_message_multiple()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_add_message_limit_reached()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_add_message_error()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- **test_message_queue_get_messages()** (3 connections) — `server/tests/unit/realtime/test_message_queue.py`
- *... and 58 more nodes in this community*

## Relationships

- [Coord](Coord.md) (10 shared connections)
- [connection disconnection](connection_disconnection.md) (8 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (4 shared connections)
- [test statistics aggregator](test_statistics_aggregator.md) (2 shared connections)
- [Player](Player.md) (2 shared connections)
- [Custom user manager for MythosMUD.](Custom_user_manager_for_MythosMUD.md) (1 shared connections)
- [Any](Any.md) (1 shared connections)

## Source Files

- `server/realtime/message_queue.py`
- `server/tests/unit/realtime/test_connection_disconnection.py`
- `server/tests/unit/realtime/test_message_queue.py`

## Audit Trail

- EXTRACTED: 239 (93%)
- INFERRED: 17 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*