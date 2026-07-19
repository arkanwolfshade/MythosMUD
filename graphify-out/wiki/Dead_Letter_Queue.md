# Dead Letter Queue

> 75 nodes · cohesion 0.05

## Key Concepts

- **DeadLetterQueue** (37 connections) — `server/realtime/dead_letter_queue.py`
- **DeadLetterMessage** (27 connections) — `server/realtime/dead_letter_queue.py`
- **test_dead_letter_queue.py** (27 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Any** (7 connections) — `server/realtime/dead_letter_queue.py`
- **.to_dict()** (5 connections) — `server/realtime/dead_letter_queue.py`
- **.enqueue()** (5 connections) — `server/realtime/dead_letter_queue.py`
- **.enqueue_async()** (5 connections) — `server/realtime/dead_letter_queue.py`
- **Path** (5 connections) — `server/realtime/dead_letter_queue.py`
- **.__init__()** (4 connections) — `server/realtime/dead_letter_queue.py`
- **.replay_message()** (4 connections) — `server/realtime/dead_letter_queue.py`
- **test_cleanup_old_messages()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_cleanup_old_messages_no_old_messages()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_delete_message()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_dequeue_removes_file()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_dequeue_returns_oldest_message()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_enqueue_creates_file()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_enqueue_writes_correct_data()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_get_statistics_with_messages()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_list_messages_handles_read_error()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_list_messages_respects_limit()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_list_messages_returns_all()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_replay_message()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **.from_dict()** (3 connections) — `server/realtime/dead_letter_queue.py`
- **.delete_message()** (3 connections) — `server/realtime/dead_letter_queue.py`
- **.dequeue()** (3 connections) — `server/realtime/dead_letter_queue.py`
- *... and 50 more nodes in this community*

## Relationships

- [[NATS Chat Broadcasting]] (8 shared connections)
- [[NPC Admin API]] (5 shared connections)
- [[Alias Game Chat]] (1 shared connections)
- [[Circuit Breaker Core]] (1 shared connections)

## Source Files

- `server/realtime/dead_letter_queue.py`
- `server/tests/unit/realtime/test_dead_letter_queue.py`

## Audit Trail

- EXTRACTED: 259 (98%)
- INFERRED: 6 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
