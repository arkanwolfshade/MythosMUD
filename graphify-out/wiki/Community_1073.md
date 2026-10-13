# Community 1073

> 13 nodes

## Key Concepts

- **DeadLetterQueue** (35 connections) — `server/realtime/dead_letter_queue.py`
- **test_list_messages_handles_read_error()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_dead_letter_queue_init_with_storage_dir()** (3 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_dead_letter_queue_init_without_storage_dir()** (3 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_dead_letter_queue_init_without_storage_dir_uses_dlq_subdirectory()** (3 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_dequeue_returns_none_when_empty()** (3 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **.cleanup_old_messages()** (2 connections) — `server/realtime/dead_letter_queue.py`
- **Test DeadLetterQueue initialization with storage directory.** (2 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Clean up old DLQ messages. Args: max_age_days: Maximum age of messages to keep…** (1 connections) — `server/realtime/dead_letter_queue.py`
- **Store messages that fail after all retries. Implements file-based storage for…** (1 connections) — `server/realtime/dead_letter_queue.py`
- **Default (no explicit storage_dir) path must land in a dlq/ subdirectory (#619).** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test dequeue() returns None when queue is empty.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test list_messages() handles file read errors.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`

## Relationships

- [Community 945](Community_945.md) (12 shared connections)
- [Community 941](Community_941.md) (7 shared connections)
- [Community 1167](Community_1167.md) (5 shared connections)
- [Community 1166](Community_1166.md) (4 shared connections)
- [Community 1884](Community_1884.md) (1 shared connections)
- [Community 1883](Community_1883.md) (1 shared connections)
- [Community 1882](Community_1882.md) (1 shared connections)
- [Community 47](Community_47.md) (1 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (1 shared connections)
- [Community 1169](Community_1169.md) (1 shared connections)

## Source Files

- `server/realtime/dead_letter_queue.py`
- `server/tests/unit/realtime/test_dead_letter_queue.py`

## Audit Trail

- EXTRACTED: 46 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*