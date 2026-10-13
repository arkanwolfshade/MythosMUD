# Community 941

> 16 nodes

## Key Concepts

- **DeadLetterMessage** (24 connections) — `server/realtime/dead_letter_queue.py`
- **test_cleanup_old_messages()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_enqueue_creates_file()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_enqueue_writes_correct_data()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_get_statistics_with_messages()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_list_messages_respects_limit()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_replay_message()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_dead_letter_message_to_dict_no_headers()** (3 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Message stored in dead letter queue. Contains message data and failure context…** (1 connections) — `server/realtime/dead_letter_queue.py`
- **Test enqueue() creates DLQ file.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test enqueue() writes correct message data.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test get_statistics() returns stats with messages.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test list_messages() respects limit parameter.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test replay_message() retrieves and removes message.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test DeadLetterMessage.to_dict() handles None headers.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test cleanup_old_messages() removes old messages.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`

## Relationships

- [Community 945](Community_945.md) (11 shared connections)
- [Community 1073](Community_1073.md) (7 shared connections)
- [Community 1327](Community_1327.md) (4 shared connections)
- [Community 1167](Community_1167.md) (2 shared connections)
- [Community 1884](Community_1884.md) (1 shared connections)
- [Community 1883](Community_1883.md) (1 shared connections)
- [Community 1882](Community_1882.md) (1 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (1 shared connections)
- [Community 1166](Community_1166.md) (1 shared connections)

## Source Files

- `server/realtime/dead_letter_queue.py`
- `server/tests/unit/realtime/test_dead_letter_queue.py`

## Audit Trail

- EXTRACTED: 41 (93%)
- INFERRED: 3 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*