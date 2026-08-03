# dead letter realtime

> 13 nodes

## Key Concepts

- **.to_dict()** (5 connections) — `server/realtime/dead_letter_queue.py`
- **.enqueue_async()** (5 connections) — `server/realtime/dead_letter_queue.py`
- **Path** (5 connections)
- **.enqueue()** (5 connections) — `server/realtime/dead_letter_queue.py`
- **.__init__()** (4 connections) — `server/realtime/dead_letter_queue.py`
- **.replay_message()** (4 connections) — `server/realtime/dead_letter_queue.py`
- **.delete_message()** (3 connections) — `server/realtime/dead_letter_queue.py`
- **Convert message to dictionary for JSON serialization.** (1 connections) — `server/realtime/dead_letter_queue.py`
- **Initialize dead letter queue.          Args:             storage_dir: Optional d** (1 connections) — `server/realtime/dead_letter_queue.py`
- **Add failed message to dead letter queue (async version).          Args:** (1 connections) — `server/realtime/dead_letter_queue.py`
- **Add failed message to dead letter queue (sync version).          Args:** (1 connections) — `server/realtime/dead_letter_queue.py`
- **Retrieve message for replay and remove from DLQ.          Args:             file** (1 connections) — `server/realtime/dead_letter_queue.py`
- **Delete a message from DLQ without processing.          Args:             filepat** (1 connections) — `server/realtime/dead_letter_queue.py`

## Relationships

- [realtime dead letter](realtime_dead_letter.md) (7 shared connections)
- [message nats handler](message_nats_handler.md) (3 shared connections)
- [Item Instances](Item_Instances.md) (1 shared connections)

## Source Files

- `server/realtime/dead_letter_queue.py`

## Audit Trail

- EXTRACTED: 37 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*