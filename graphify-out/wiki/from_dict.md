# .from_dict

> 8 nodes · cohesion 0.25

## Key Concepts

- **.from_dict()** (6 connections) — `server/realtime/dead_letter_queue.py`
- **test_dead_letter_message_from_dict()** (3 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_dead_letter_message_from_dict_datetime_timestamp()** (3 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_dead_letter_message_from_dict_string_timestamp()** (3 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Reconstruct message from dictionary.** (1 connections) — `server/realtime/dead_letter_queue.py`
- **Test DeadLetterMessage.from_dict() reconstructs message.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test DeadLetterMessage.from_dict() handles string timestamp.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test DeadLetterMessage.from_dict() handles datetime timestamp.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`

## Relationships

- [test_dead_letter_queue.py](test_dead_letter_queue.py.md) (3 shared connections)
- [DeadLetterMessage](DeadLetterMessage.md) (1 shared connections)
- [Any](Any.md) (1 shared connections)

## Source Files

- `server/realtime/dead_letter_queue.py`
- `server/tests/unit/realtime/test_dead_letter_queue.py`

## Audit Trail

- EXTRACTED: 19 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*