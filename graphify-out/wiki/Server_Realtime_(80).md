# Server Realtime (80)

> 18 nodes

## Key Concepts

- **DeadLetterMessage** (25 connections) — `server/realtime/dead_letter_queue.py`
- **.to_dict()** (5 connections) — `server/realtime/dead_letter_queue.py`
- **.enqueue_async()** (5 connections) — `server/realtime/dead_letter_queue.py`
- **Path** (5 connections)
- **.enqueue()** (5 connections) — `server/realtime/dead_letter_queue.py`
- **.__init__()** (4 connections) — `server/realtime/dead_letter_queue.py`
- **test_list_messages_returns_all()** (4 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **.delete_message()** (3 connections) — `server/realtime/dead_letter_queue.py`
- **test_dead_letter_message_to_dict()** (3 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **test_dead_letter_message_to_dict_no_headers()** (3 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Add failed message to dead letter queue (async version).          Args:** (2 connections) — `server/realtime/dead_letter_queue.py`
- **Message stored in dead letter queue.      Contains message data and failure cont** (1 connections) — `server/realtime/dead_letter_queue.py`
- **Convert message to dictionary for JSON serialization.** (1 connections) — `server/realtime/dead_letter_queue.py`
- **Initialize dead letter queue.          Args:             storage_dir: Optional d** (1 connections) — `server/realtime/dead_letter_queue.py`
- **Delete a message from DLQ without processing.          Args:             filepat** (1 connections) — `server/realtime/dead_letter_queue.py`
- **Test DeadLetterMessage.to_dict() converts to dictionary.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test DeadLetterMessage.to_dict() handles None headers.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`
- **Test list_messages() returns all messages.** (1 connections) — `server/tests/unit/realtime/test_dead_letter_queue.py`

## Relationships

- [Server Realtime (89)](Server_Realtime_%2889%29.md) (7 shared connections)
- [Server Realtime (79)](Server_Realtime_%2879%29.md) (6 shared connections)
- [Server Realtime](Server_Realtime.md) (4 shared connections)
- [Server Commands](Server_Commands.md) (1 shared connections)
- [Server Realtime (114)](Server_Realtime_%28114%29.md) (1 shared connections)
- [Server Realtime (162)](Server_Realtime_%28162%29.md) (1 shared connections)
- [Server Realtime (157)](Server_Realtime_%28157%29.md) (1 shared connections)
- [Server Realtime (156)](Server_Realtime_%28156%29.md) (1 shared connections)
- [Server Realtime (154)](Server_Realtime_%28154%29.md) (1 shared connections)
- [Server Realtime (155)](Server_Realtime_%28155%29.md) (1 shared connections)
- [Server Realtime (158)](Server_Realtime_%28158%29.md) (1 shared connections)
- [Server Realtime (160)](Server_Realtime_%28160%29.md) (1 shared connections)

## Source Files

- `server/realtime/dead_letter_queue.py`
- `server/tests/unit/realtime/test_dead_letter_queue.py`

## Audit Trail

- EXTRACTED: 70 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*