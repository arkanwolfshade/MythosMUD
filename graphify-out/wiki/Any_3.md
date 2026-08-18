# Any

> 11 nodes

## Key Concepts

- **Any** (7 connections)
- **.to_dict()** (3 connections) — `server/realtime/dead_letter_queue.py`
- **.dequeue()** (3 connections) — `server/realtime/dead_letter_queue.py`
- **.dequeue_async()** (3 connections) — `server/realtime/dead_letter_queue.py`
- **.get_statistics()** (3 connections) — `server/realtime/dead_letter_queue.py`
- **.list_messages()** (3 connections) — `server/realtime/dead_letter_queue.py`
- **Retrieve and remove oldest message from DLQ (async version). Returns: Message…** (1 connections) — `server/realtime/dead_letter_queue.py`
- **Retrieve and remove oldest message from DLQ (sync version). Returns: Message…** (1 connections) — `server/realtime/dead_letter_queue.py`
- **Get DLQ statistics. Returns: Dictionary with DLQ metrics AI: For monitoring…** (1 connections) — `server/realtime/dead_letter_queue.py`
- **List messages in DLQ without removing them. Args: limit: Maximum number of…** (1 connections) — `server/realtime/dead_letter_queue.py`
- **Convert message to dictionary for JSON serialization.** (1 connections) — `server/realtime/dead_letter_queue.py`

## Relationships

- [DeadLetterQueue](DeadLetterQueue.md) (4 shared connections)
- [DeadLetterMessage](DeadLetterMessage.md) (1 shared connections)
- [.from_dict](from_dict.md) (1 shared connections)
- [Path](Path.md) (1 shared connections)

## Source Files

- `server/realtime/dead_letter_queue.py`

## Audit Trail

- EXTRACTED: 17 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*