# realtime dead letter

> 9 nodes

## Key Concepts

- **Any** (7 connections)
- **.dequeue_async()** (3 connections) — `server/realtime/dead_letter_queue.py`
- **.dequeue()** (3 connections) — `server/realtime/dead_letter_queue.py`
- **.get_statistics()** (3 connections) — `server/realtime/dead_letter_queue.py`
- **.list_messages()** (3 connections) — `server/realtime/dead_letter_queue.py`
- **Retrieve and remove oldest message from DLQ (async version).          Returns:** (1 connections) — `server/realtime/dead_letter_queue.py`
- **Retrieve and remove oldest message from DLQ (sync version).          Returns:** (1 connections) — `server/realtime/dead_letter_queue.py`
- **Get DLQ statistics.          Returns:             Dictionary with DLQ metrics** (1 connections) — `server/realtime/dead_letter_queue.py`
- **List messages in DLQ without removing them.          Args:             limit: Ma** (1 connections) — `server/realtime/dead_letter_queue.py`

## Relationships

- [realtime dead letter](realtime_dead_letter.md) (4 shared connections)
- [dead letter realtime](dead_letter_realtime.md) (3 shared connections)

## Source Files

- `server/realtime/dead_letter_queue.py`

## Audit Trail

- EXTRACTED: 23 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*