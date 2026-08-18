# .from_dict

> 8 nodes

## Key Concepts

- **.from_dict()** (6 connections) — `server/realtime/dead_letter_queue.py`
- **test_dead_letter_message_from_dict()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_dead_letter_message_from_dict_datetime_timestamp()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_dead_letter_message_from_dict_string_timestamp()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Reconstruct message from dictionary.** (1 connections) — `server/realtime/dead_letter_queue.py`
- **Test DeadLetterMessage.from_dict() reconstructs message.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test DeadLetterMessage.from_dict() handles string timestamp.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test DeadLetterMessage.from_dict() handles datetime timestamp.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`

## Relationships

- [DeadLetterMessage](DeadLetterMessage.md) (4 shared connections)
- [DeadLetterQueue](DeadLetterQueue.md) (3 shared connections)
- [Any](Any.md) (1 shared connections)

## Source Files

- `server/realtime/dead_letter_queue.py`
- `server/tests/unit/realtime/test_dead_letter_queue.py`

## Audit Trail

- EXTRACTED: 12 (80%)
- INFERRED: 3 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*