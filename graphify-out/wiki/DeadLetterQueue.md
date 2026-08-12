# DeadLetterQueue

> 14 nodes

## Key Concepts

- **DeadLetterQueue** (35 connections) — `server/realtime/dead_letter_queue.py`
- **test_get_statistics_with_messages()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_cleanup_old_messages_handles_errors()** (3 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_dead_letter_queue_init_without_storage_dir()** (3 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_dequeue_handles_read_error()** (3 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_list_messages_empty()** (3 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **.cleanup_old_messages()** (2 connections) — `server/realtime/dead_letter_queue.py`
- **Clean up old DLQ messages. Args: max_age_days: Maximum age of messages to keep…** (1 connections) — `server/realtime/dead_letter_queue.py`
- **Store messages that fail after all retries. Implements file-based storage for…** (1 connections) — `server/realtime/dead_letter_queue.py`
- **Test DeadLetterQueue initialization without storage directory.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test dequeue() handles file read errors.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test get_statistics() returns stats with messages.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test list_messages() returns empty list when queue is empty.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test cleanup_old_messages() handles file errors.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`

## Relationships

- [test_dead_letter_queue.py](test_dead_letter_queue.py.md) (12 shared connections)
- [DeadLetterMessage](DeadLetterMessage.md) (7 shared connections)
- [Path](Path.md) (5 shared connections)
- [Any](Any.md) (4 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [EventHandler](EventHandler.md) (1 shared connections)
- [test_dequeue_returns_oldest_message](test_dequeue_returns_oldest_message.md) (1 shared connections)
- [test_enqueue_writes_correct_data](test_enqueue_writes_correct_data.md) (1 shared connections)
- [NATSMessageHandler](NATSMessageHandler.md) (1 shared connections)

## Source Files

- `server/realtime/dead_letter_queue.py`
- `server/tests/unit/realtime/test_dead_letter_queue.py`

## Audit Trail

- EXTRACTED: 59 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*