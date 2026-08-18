# DeadLetterQueue

> 34 nodes

## Key Concepts

- **DeadLetterQueue** (37 connections) — `server/realtime/dead_letter_queue.py`
- **test_dead_letter_queue.py** (28 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_cleanup_old_messages()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_dequeue_returns_oldest_message()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_enqueue_creates_file()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_list_messages_handles_read_error()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_list_messages_returns_all()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_replay_message()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_cleanup_old_messages_handles_errors()** (3 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_dead_letter_message_to_dict_no_headers()** (3 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_dead_letter_queue_init_with_storage_dir()** (3 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_dead_letter_queue_init_without_storage_dir()** (3 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_dequeue_handles_read_error()** (3 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_dequeue_returns_none_when_empty()** (3 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_get_statistics_empty()** (3 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_list_messages_empty()** (3 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **.cleanup_old_messages()** (2 connections) — `server/realtime/dead_letter_queue.py`
- **Clean up old DLQ messages. Args: max_age_days: Maximum age of messages to keep…** (1 connections) — `server/realtime/dead_letter_queue.py`
- **Store messages that fail after all retries. Implements file-based storage for…** (1 connections) — `server/realtime/dead_letter_queue.py`
- **Unit tests for dead letter queue. Tests the DeadLetterQueue class and…** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test DeadLetterQueue initialization without storage directory.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test enqueue() creates DLQ file.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test dequeue() returns None when queue is empty.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test dequeue() returns oldest message.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test dequeue() handles file read errors.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- *... and 9 more nodes in this community*

## Relationships

- [DeadLetterMessage](DeadLetterMessage.md) (21 shared connections)
- [Path](Path.md) (5 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [Any](Any.md) (4 shared connections)
- [.from_dict](from_dict.md) (3 shared connections)
- [MessageFilteringHelper](MessageFilteringHelper.md) (1 shared connections)
- [NATSMessageHandlerMixinBase](NATSMessageHandlerMixinBase.md) (1 shared connections)
- [lifespan_protocols.py](lifespan_protocols.py.md) (1 shared connections)

## Source Files

- `server/realtime/dead_letter_queue.py`
- `server/tests/unit/realtime/test_dead_letter_queue.py`

## Audit Trail

- EXTRACTED: 84 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*