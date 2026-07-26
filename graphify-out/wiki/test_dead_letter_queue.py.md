# test_dead_letter_queue.py

> 16 nodes · cohesion 0.12

## Key Concepts

- **test_dead_letter_queue.py** (28 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_dequeue_removes_file()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_enqueue_creates_file()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_list_messages_handles_read_error()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_dead_letter_message_to_dict_no_headers()** (3 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_dead_letter_queue_init_with_storage_dir()** (3 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_dequeue_returns_none_when_empty()** (3 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_get_statistics_empty()** (3 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Unit tests for dead letter queue.  Tests the DeadLetterQueue class and DeadLette** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test enqueue() creates DLQ file.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test dequeue() returns None when queue is empty.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test dequeue() removes file after reading.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test get_statistics() returns stats for empty queue.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test list_messages() handles file read errors.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test DeadLetterMessage.to_dict() handles None headers.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test DeadLetterQueue initialization with storage directory.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`

## Relationships

- [DeadLetterMessage](DeadLetterMessage.md) (12 shared connections)
- [DeadLetterQueue](DeadLetterQueue.md) (12 shared connections)
- [.from_dict](from_dict.md) (3 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [Community 1327](Community_1327.md) (1 shared connections)
- [Community 1326](Community_1326.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_dead_letter_queue.py`

## Audit Trail

- EXTRACTED: 60 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*