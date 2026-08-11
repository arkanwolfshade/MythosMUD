# Dead Letter Queue

> 80 nodes

## Key Concepts

- **DeadLetterQueue** (35 connections) — `server/realtime/dead_letter_queue.py`
- **test_dead_letter_queue.py** (28 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **DeadLetterMessage** (25 connections) — `server/realtime/dead_letter_queue.py`
- **Any** (7 connections)
- **.from_dict()** (6 connections) — `server/realtime/dead_letter_queue.py`
- **.to_dict()** (5 connections) — `server/realtime/dead_letter_queue.py`
- **.enqueue_async()** (5 connections) — `server/realtime/dead_letter_queue.py`
- **Path** (5 connections)
- **.enqueue()** (5 connections) — `server/realtime/dead_letter_queue.py`
- **.__init__()** (4 connections) — `server/realtime/dead_letter_queue.py`
- **.replay_message()** (4 connections) — `server/realtime/dead_letter_queue.py`
- **test_enqueue_creates_file()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_enqueue_writes_correct_data()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_dequeue_returns_oldest_message()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_dequeue_removes_file()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_get_statistics_with_messages()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_list_messages_returns_all()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_list_messages_respects_limit()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_list_messages_handles_read_error()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_replay_message()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_delete_message()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_cleanup_old_messages()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_cleanup_old_messages_no_old_messages()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **.dequeue_async()** (3 connections) — `server/realtime/dead_letter_queue.py`
- **.dequeue()** (3 connections) — `server/realtime/dead_letter_queue.py`
- *... and 55 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (5 shared connections)
- [NATS Chat Broadcasting](NATS_Chat_Broadcasting.md) (4 shared connections)
- [Test Optimization Insights](Test_Optimization_Insights.md) (1 shared connections)
- [Combat Domain Events](Combat_Domain_Events.md) (1 shared connections)

## Source Files

- `server/realtime/dead_letter_queue.py`
- `server/tests/unit/realtime/test_dead_letter_queue.py`

## Audit Trail

- EXTRACTED: 267 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*