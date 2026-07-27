# DeadLetterQueue

> 14 nodes · cohesion 0.14

## Key Concepts

- **DeadLetterQueue** (35 connections) — `server/realtime/dead_letter_queue.py`
- **test_get_statistics_with_messages()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_cleanup_old_messages_handles_errors()** (3 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_dead_letter_queue_init_without_storage_dir()** (3 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_dequeue_handles_read_error()** (3 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_list_messages_empty()** (3 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **.cleanup_old_messages()** (2 connections) — `server/realtime/dead_letter_queue.py`
- **Clean up old DLQ messages.          Args:             max_age_days: Maximum age** (1 connections) — `server/realtime/dead_letter_queue.py`
- **Store messages that fail after all retries.      Implements file-based storage f** (1 connections) — `server/realtime/dead_letter_queue.py`
- **Test DeadLetterQueue initialization without storage directory.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test dequeue() handles file read errors.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test get_statistics() returns stats with messages.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test list_messages() returns empty list when queue is empty.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test cleanup_old_messages() handles file errors.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`

## Relationships

- [test_dead_letter_queue.py](test_dead_letter_queue.py.md) (12 shared connections)
- [DeadLetterMessage](DeadLetterMessage.md) (7 shared connections)
- [.to_dict](to_dict.md) (5 shared connections)
- [Any](Any.md) (4 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)
- [NATSMessageHandler](NATSMessageHandler.md) (1 shared connections)
- [EventHandler](EventHandler.md) (1 shared connections)
- [test_process_dict_occupant_with_npc_name](test_process_dict_occupant_with_npc_name.md) (1 shared connections)
- [test_process_dict_occupant_with_player_name](test_process_dict_occupant_with_player_name.md) (1 shared connections)

## Source Files

- `server/realtime/dead_letter_queue.py`
- `server/tests/unit/realtime/test_dead_letter_queue.py`

## Audit Trail

- EXTRACTED: 59 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*