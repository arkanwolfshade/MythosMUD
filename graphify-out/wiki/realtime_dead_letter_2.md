# realtime dead letter

> 14 nodes

## Key Concepts

- **DeadLetterQueue** (37 connections) — `server/realtime/dead_letter_queue.py`
- **test_dequeue_removes_file()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_list_messages_respects_limit()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_list_messages_handles_read_error()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_dequeue_returns_none_when_empty()** (3 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_list_messages_empty()** (3 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **.cleanup_old_messages()** (2 connections) — `server/realtime/dead_letter_queue.py`
- **Store messages that fail after all retries.      Implements file-based storage f** (1 connections) — `server/realtime/dead_letter_queue.py`
- **Clean up old DLQ messages.          Args:             max_age_days: Maximum age** (1 connections) — `server/realtime/dead_letter_queue.py`
- **Test dequeue() returns None when queue is empty.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test dequeue() removes file after reading.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test list_messages() returns empty list when queue is empty.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test list_messages() respects limit parameter.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test list_messages() handles file read errors.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`

## Relationships

- [dead letter queue](dead_letter_queue.md) (12 shared connections)
- [realtime dead letter](realtime_dead_letter.md) (9 shared connections)
- [dead letter realtime](dead_letter_realtime.md) (5 shared connections)
- [message nats handler](message_nats_handler.md) (4 shared connections)
- [NATS Messaging](NATS_Messaging.md) (3 shared connections)
- [game room service](game_room_service.md) (3 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (1 shared connections)
- [realtime message filtering](realtime_message_filtering.md) (1 shared connections)

## Source Files

- `server/realtime/dead_letter_queue.py`
- `server/tests/unit/realtime/test_dead_letter_queue.py`

## Audit Trail

- EXTRACTED: 62 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*