# dead letter queue

> 18 nodes

## Key Concepts

- **test_dead_letter_queue.py** (28 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_enqueue_creates_file()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_delete_message()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_cleanup_old_messages()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_dead_letter_message_to_dict()** (3 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_dead_letter_message_to_dict_no_headers()** (3 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_dead_letter_queue_init_without_storage_dir()** (3 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_get_statistics_empty()** (3 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_cleanup_old_messages_handles_errors()** (3 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Unit tests for dead letter queue.  Tests the DeadLetterQueue class and DeadLette** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test DeadLetterMessage.to_dict() converts to dictionary.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test DeadLetterMessage.to_dict() handles None headers.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test DeadLetterQueue initialization without storage directory.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test enqueue() creates DLQ file.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test get_statistics() returns stats for empty queue.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test delete_message() removes message file.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test cleanup_old_messages() removes old messages.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test cleanup_old_messages() handles file errors.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`

## Relationships

- [realtime dead letter](realtime_dead_letter.md) (17 shared connections)
- [message nats handler](message_nats_handler.md) (6 shared connections)
- [dead letter realtime](dead_letter_realtime.md) (3 shared connections)
- [game room service](game_room_service.md) (3 shared connections)
- [NATS Messaging](NATS_Messaging.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_dead_letter_queue.py`

## Audit Trail

- EXTRACTED: 64 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*