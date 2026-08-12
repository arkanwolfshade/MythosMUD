# MessageBroadcaster

> 15 nodes

## Key Concepts

- **MessageBroadcaster** (19 connections) — `server/realtime/messaging/message_broadcaster.py`
- **.broadcast_to_room()** (6 connections) — `server/realtime/messaging/message_broadcaster.py`
- **server/realtime/messaging/__init__.py** (5 connections) — `server/realtime/messaging/__init__.py`
- **.broadcast_global_event()** (4 connections) — `server/realtime/messaging/message_broadcaster.py`
- **.broadcast_room_event()** (4 connections) — `server/realtime/messaging/message_broadcaster.py`
- **.__init__()** (4 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._prepare_room_targets()** (3 connections) — `server/realtime/messaging/message_broadcaster.py`
- **SendPersonalMessage** (1 connections)
- **Messaging components for connection management. This package provides modular…** (1 connections) — `server/realtime/messaging/__init__.py`
- **Dedupe subscribers and count exclusions.** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Broadcast a message to all players in a room. Args: room_id: The room's ID…** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Broadcast a room-specific event.** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Broadcast a global event to all connected players.** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Broadcasts messages to rooms and globally. This class provides: - Room-scoped…** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Initialize the message broadcaster. Args: room_manager: RoomSubscriptionManager…** (1 connections) — `server/realtime/messaging/message_broadcaster.py`

## Relationships

- [message_broadcaster.py](message_broadcaster.py.md) (8 shared connections)
- [RateLimiter](RateLimiter.md) (5 shared connections)
- [._deliver_room_broadcast](_deliver_room_broadcast.md) (4 shared connections)
- [build_event](build_event.md) (2 shared connections)
- [message_broadcaster](message_broadcaster.md) (1 shared connections)
- [test_message_broadcaster.py](test_message_broadcaster.py.md) (1 shared connections)

## Source Files

- `server/realtime/messaging/__init__.py`
- `server/realtime/messaging/message_broadcaster.py`

## Audit Trail

- EXTRACTED: 53 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*