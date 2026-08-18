# .broadcast_to_room

> 6 nodes

## Key Concepts

- **.broadcast_to_room()** (6 connections) — `server/realtime/messaging/message_broadcaster.py`
- **.broadcast_room_event()** (4 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._prepare_room_targets()** (3 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Dedupe subscribers and count exclusions.** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Broadcast a message to all players in a room. Args: room_id: The room's ID…** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Broadcast a room-specific event.** (1 connections) — `server/realtime/messaging/message_broadcaster.py`

## Relationships

- [MessageBroadcaster](MessageBroadcaster.md) (5 shared connections)
- [build_event](build_event.md) (1 shared connections)

## Source Files

- `server/realtime/messaging/message_broadcaster.py`

## Audit Trail

- EXTRACTED: 11 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*