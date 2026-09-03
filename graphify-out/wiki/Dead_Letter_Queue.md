# Dead Letter Queue

> 18 nodes

## Key Concepts

- **Any** (7 connections)
- **Path** (5 connections)
- **.__init__()** (4 connections) — `server/realtime/dead_letter_queue.py`
- **.replay_message()** (4 connections) — `server/realtime/dead_letter_queue.py`
- **.to_dict()** (3 connections) — `server/realtime/dead_letter_queue.py`
- **.delete_message()** (3 connections) — `server/realtime/dead_letter_queue.py`
- **.dequeue()** (3 connections) — `server/realtime/dead_letter_queue.py`
- **.dequeue_async()** (3 connections) — `server/realtime/dead_letter_queue.py`
- **.get_statistics()** (3 connections) — `server/realtime/dead_letter_queue.py`
- **.list_messages()** (3 connections) — `server/realtime/dead_letter_queue.py`
- **Retrieve and remove oldest message from DLQ (async version). Returns: Message…** (1 connections) — `server/realtime/dead_letter_queue.py`
- **Retrieve and remove oldest message from DLQ (sync version). Returns: Message…** (1 connections) — `server/realtime/dead_letter_queue.py`
- **Get DLQ statistics. Returns: Dictionary with DLQ metrics AI: For monitoring…** (1 connections) — `server/realtime/dead_letter_queue.py`
- **List messages in DLQ without removing them. Args: limit: Maximum number of…** (1 connections) — `server/realtime/dead_letter_queue.py`
- **Retrieve message for replay and remove from DLQ. Args: filepath: Path to DLQ…** (1 connections) — `server/realtime/dead_letter_queue.py`
- **Delete a message from DLQ without processing. Args: filepath: Path to DLQ file…** (1 connections) — `server/realtime/dead_letter_queue.py`
- **Convert message to dictionary for JSON serialization.** (1 connections) — `server/realtime/dead_letter_queue.py`
- **Initialize dead letter queue. Args: storage_dir: Optional directory to store…** (1 connections) — `server/realtime/dead_letter_queue.py`

## Relationships

- [Test Dead Letter Queue](Test_Dead_Letter_Queue.md) (11 shared connections)
- [Test Config Init](Test_Config_Init.md) (1 shared connections)

## Source Files

- `server/realtime/dead_letter_queue.py`

## Audit Trail

- EXTRACTED: 29 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*