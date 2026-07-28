# Server Realtime (89)

> 14 nodes

## Key Concepts

- **DeadLetterQueue** (35 connections) — `server/realtime/dead_letter_queue.py`
- **Any** (7 connections)
- **.replay_message()** (4 connections) — `server/realtime/dead_letter_queue.py`
- **.dequeue_async()** (3 connections) — `server/realtime/dead_letter_queue.py`
- **.dequeue()** (3 connections) — `server/realtime/dead_letter_queue.py`
- **.get_statistics()** (3 connections) — `server/realtime/dead_letter_queue.py`
- **.list_messages()** (3 connections) — `server/realtime/dead_letter_queue.py`
- **.cleanup_old_messages()** (2 connections) — `server/realtime/dead_letter_queue.py`
- **Retrieve and remove oldest message from DLQ (async version).          Returns:** (2 connections) — `server/realtime/dead_letter_queue.py`
- **Store messages that fail after all retries.      Implements file-based storage f** (1 connections) — `server/realtime/dead_letter_queue.py`
- **Get DLQ statistics.          Returns:             Dictionary with DLQ metrics** (1 connections) — `server/realtime/dead_letter_queue.py`
- **List messages in DLQ without removing them.          Args:             limit: Ma** (1 connections) — `server/realtime/dead_letter_queue.py`
- **Retrieve message for replay and remove from DLQ.          Args:             file** (1 connections) — `server/realtime/dead_letter_queue.py`
- **Clean up old DLQ messages.          Args:             max_age_days: Maximum age** (1 connections) — `server/realtime/dead_letter_queue.py`

## Relationships

- [Server Realtime (79)](Server_Realtime_%2879%29.md) (10 shared connections)
- [Server Realtime (80)](Server_Realtime_%2880%29.md) (7 shared connections)
- [Server Realtime](Server_Realtime.md) (3 shared connections)
- [Server Realtime (114)](Server_Realtime_%28114%29.md) (1 shared connections)
- [Server Commands](Server_Commands.md) (1 shared connections)
- [Server Realtime (162)](Server_Realtime_%28162%29.md) (1 shared connections)
- [Server Realtime (157)](Server_Realtime_%28157%29.md) (1 shared connections)
- [Server Realtime (156)](Server_Realtime_%28156%29.md) (1 shared connections)
- [Server Realtime (154)](Server_Realtime_%28154%29.md) (1 shared connections)
- [Server Realtime (155)](Server_Realtime_%28155%29.md) (1 shared connections)
- [Server Realtime (158)](Server_Realtime_%28158%29.md) (1 shared connections)
- [Server Realtime (160)](Server_Realtime_%28160%29.md) (1 shared connections)

## Source Files

- `server/realtime/dead_letter_queue.py`

## Audit Trail

- EXTRACTED: 66 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*