# realtime dead letter

> 2 nodes

## Key Concepts

- **test_replay_message()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test replay_message() retrieves and removes message.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`

## Relationships

- [message nats handler](message_nats_handler.md) (1 shared connections)
- [realtime dead letter](realtime_dead_letter.md) (1 shared connections)
- [dead letter queue](dead_letter_queue.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_dead_letter_queue.py`

## Audit Trail

- EXTRACTED: 5 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*