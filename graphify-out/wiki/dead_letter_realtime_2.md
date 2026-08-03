# dead letter realtime

> 8 nodes

## Key Concepts

- **.from_dict()** (6 connections) — `server/realtime/dead_letter_queue.py`
- **test_dead_letter_message_from_dict()** (3 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_dead_letter_message_from_dict_string_timestamp()** (3 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_dead_letter_message_from_dict_datetime_timestamp()** (3 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Reconstruct message from dictionary.** (1 connections) — `server/realtime/dead_letter_queue.py`
- **Test DeadLetterMessage.from_dict() reconstructs message.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test DeadLetterMessage.from_dict() handles string timestamp.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test DeadLetterMessage.from_dict() handles datetime timestamp.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`

## Relationships

- [dead letter queue](dead_letter_queue.md) (3 shared connections)
- [message nats handler](message_nats_handler.md) (1 shared connections)
- [realtime dead letter](realtime_dead_letter.md) (1 shared connections)

## Source Files

- `server/realtime/dead_letter_queue.py`
- `server/tests/unit/realtime/test_dead_letter_queue.py`

## Audit Trail

- EXTRACTED: 19 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*