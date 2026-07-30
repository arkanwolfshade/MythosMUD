# Remove sensitive data from log

> 14 nodes

## Key Concepts

- **MessageBroadcaster** (19 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._deliver_room_broadcast()** (6 connections) — `server/realtime/messaging/message_broadcaster.py`
- **.broadcast_to_room()** (6 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._build_target_mapping()** (5 connections) — `server/realtime/messaging/message_broadcaster.py`
- **.broadcast_room_event()** (4 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._prepare_room_targets()** (3 connections) — `server/realtime/messaging/message_broadcaster.py`
- **message_broadcaster()** (3 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **Broadcasts messages to rooms and globally.      This class provides:     - Room-** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Convert string player IDs to UUIDs for message sending.          Args:** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Dedupe subscribers and count exclusions.** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Run batch gather (or fallback) for a room broadcast.** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Broadcast a message to all players in a room.          Args:             room_id** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Broadcast a room-specific event.** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Create a MessageBroadcaster instance.** (1 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`

## Relationships

- [canonical room id impl()](canonical_room_id_impl%28%29.md) (10 shared connections)
- [TerminalButtonProps](TerminalButtonProps.md) (3 shared connections)
- [SendPersonalMessage](SendPersonalMessage.md) (2 shared connections)
- [test connection cleaner](test_connection_cleaner.md) (1 shared connections)
- [test database](test_database.md) (1 shared connections)
- [game](game.md) (1 shared connections)
- [Any](Any.md) (1 shared connections)

## Source Files

- `server/realtime/messaging/message_broadcaster.py`
- `server/tests/unit/realtime/messaging/test_message_broadcaster.py`

## Audit Trail

- EXTRACTED: 53 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*