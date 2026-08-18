# DeadLetterMessage

> 16 nodes

## Key Concepts

- **DeadLetterMessage** (28 connections) — `server/realtime/dead_letter_queue.py`
- **test_cleanup_old_messages_no_old_messages()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_delete_message()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_dequeue_removes_file()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_enqueue_writes_correct_data()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_get_statistics_with_messages()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_list_messages_respects_limit()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_dead_letter_message_to_dict()** (3 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Message stored in dead letter queue. Contains message data and failure context…** (1 connections) — `server/realtime/dead_letter_queue.py`
- **Test enqueue() writes correct message data.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test DeadLetterMessage.to_dict() converts to dictionary.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test dequeue() removes file after reading.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test get_statistics() returns stats with messages.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test list_messages() respects limit parameter.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test delete_message() removes message file.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test cleanup_old_messages() returns 0 when no old messages.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`

## Relationships

- [DeadLetterQueue](DeadLetterQueue.md) (21 shared connections)
- [.from_dict](from_dict.md) (4 shared connections)
- [._handle_nats_message](_handle_nats_message.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [Path](Path.md) (2 shared connections)
- [Any](Any.md) (1 shared connections)
- [NATSMessageProcessingMixin](NATSMessageProcessingMixin.md) (1 shared connections)

## Source Files

- `server/realtime/dead_letter_queue.py`
- `server/tests/unit/realtime/test_dead_letter_queue.py`

## Audit Trail

- EXTRACTED: 44 (92%)
- INFERRED: 4 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*