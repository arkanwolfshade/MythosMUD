# .add_message

> 11 nodes

## Key Concepts

- **.add_message()** (4 connections) — `server/realtime/message_queue.py`
- **.cleanup_old_messages()** (4 connections) — `server/realtime/message_queue.py`
- **._is_message_recent()** (4 connections) — `server/realtime/message_queue.py`
- **Any** (4 connections)
- **.get_messages()** (3 connections) — `server/realtime/message_queue.py`
- **.get_stats()** (3 connections) — `server/realtime/message_queue.py`
- **Clean up old messages to prevent memory bloat. Args: max_age_seconds: Maximum…** (1 connections) — `server/realtime/message_queue.py`
- **Check if a message is recent (within the specified age limit). Args: msg:…** (1 connections) — `server/realtime/message_queue.py`
- **Get message queue statistics. Returns: Dict[str, Any]: Statistics about the…** (1 connections) — `server/realtime/message_queue.py`
- **Add a message to a player's pending message queue. Args: player_id: The…** (1 connections) — `server/realtime/message_queue.py`
- **Get all pending messages for a player and clear the queue. Args: player_id: The…** (1 connections) — `server/realtime/message_queue.py`

## Relationships

- [time.py](time.py.md) (5 shared connections)
- [deque](deque.md) (2 shared connections)

## Source Files

- `server/realtime/message_queue.py`

## Audit Trail

- EXTRACTED: 25 (93%)
- INFERRED: 2 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*