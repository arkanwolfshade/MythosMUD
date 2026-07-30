# test database

> 2 nodes

## Key Concepts

- **.broadcast_global_event()** (4 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Broadcast a global event to all connected players.** (1 connections) — `server/realtime/messaging/message_broadcaster.py`

## Relationships

- [Any](Any.md) (1 shared connections)
- [Remove sensitive data from log](Remove_sensitive_data_from_log.md) (1 shared connections)
- [canonical room id impl()](canonical_room_id_impl%28%29.md) (1 shared connections)

## Source Files

- `server/realtime/messaging/message_broadcaster.py`

## Audit Trail

- EXTRACTED: 5 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*