# DeadLetterMessage

> 16 nodes · cohesion 0.12

## Key Concepts

- **DeadLetterMessage** (25 connections) — `server/realtime/dead_letter_queue.py`
- **test_cleanup_old_messages()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_cleanup_old_messages_no_old_messages()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_delete_message()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_list_messages_respects_limit()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_list_messages_returns_all()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_replay_message()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_dead_letter_message_to_dict()** (3 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Message stored in dead letter queue.      Contains message data and failure cont** (1 connections) — `server/realtime/dead_letter_queue.py`
- **Test DeadLetterMessage.to_dict() converts to dictionary.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test list_messages() returns all messages.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test list_messages() respects limit parameter.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test replay_message() retrieves and removes message.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test delete_message() removes message file.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test cleanup_old_messages() removes old messages.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test cleanup_old_messages() returns 0 when no old messages.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`

## Relationships

- [test_dead_letter_queue.py](test_dead_letter_queue.py.md) (12 shared connections)
- [DeadLetterQueue](DeadLetterQueue.md) (7 shared connections)
- [.to_dict](to_dict.md) (3 shared connections)
- [NATSMessageHandler](NATSMessageHandler.md) (3 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [.from_dict](from_dict.md) (1 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)
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