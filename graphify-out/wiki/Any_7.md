# Any

> 9 nodes · cohesion 0.22

## Key Concepts

- **Any** (7 connections)
- **.dequeue()** (3 connections) — `server/realtime/dead_letter_queue.py`
- **.dequeue_async()** (3 connections) — `server/realtime/dead_letter_queue.py`
- **.get_statistics()** (3 connections) — `server/realtime/dead_letter_queue.py`
- **.list_messages()** (3 connections) — `server/realtime/dead_letter_queue.py`
- **Retrieve and remove oldest message from DLQ (async version).          Returns:** (1 connections) — `server/realtime/dead_letter_queue.py`
- **Retrieve and remove oldest message from DLQ (sync version).          Returns:** (1 connections) — `server/realtime/dead_letter_queue.py`
- **Get DLQ statistics.          Returns:             Dictionary with DLQ metrics** (1 connections) — `server/realtime/dead_letter_queue.py`
- **List messages in DLQ without removing them.          Args:             limit: Ma** (1 connections) — `server/realtime/dead_letter_queue.py`

## Relationships

- [DeadLetterQueue](DeadLetterQueue.md) (4 shared connections)
- [.to_dict](to_dict.md) (2 shared connections)
- [.from_dict](from_dict.md) (1 shared connections)

## Source Files

- `server/realtime/dead_letter_queue.py`

## Audit Trail

- EXTRACTED: 23 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*