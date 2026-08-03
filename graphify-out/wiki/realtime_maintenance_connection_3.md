# realtime maintenance connection

> 17 nodes

## Key Concepts

- **MessageBroadcaster** (19 connections) — `server/realtime/messaging/message_broadcaster.py`
- **.broadcast_to_room()** (6 connections) — `server/realtime/messaging/message_broadcaster.py`
- **__init__.py** (5 connections) — `server/realtime/messaging/__init__.py`
- **.__init__()** (4 connections) — `server/realtime/messaging/message_broadcaster.py`
- **.broadcast_room_event()** (4 connections) — `server/realtime/messaging/message_broadcaster.py`
- **.broadcast_global_event()** (4 connections) — `server/realtime/messaging/message_broadcaster.py`
- **._prepare_room_targets()** (3 connections) — `server/realtime/messaging/message_broadcaster.py`
- **message_broadcaster()** (3 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`
- **Messaging components for connection management.  This package provides modular m** (1 connections) — `server/realtime/messaging/__init__.py`
- **SendPersonalMessage** (1 connections)
- **Broadcasts messages to rooms and globally.      This class provides:     - Room-** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Initialize the message broadcaster.          Args:             room_manager: Roo** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Dedupe subscribers and count exclusions.** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Broadcast a message to all players in a room.          Args:             room_id** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Broadcast a room-specific event.** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Broadcast a global event to all connected players.** (1 connections) — `server/realtime/messaging/message_broadcaster.py`
- **Create a MessageBroadcaster instance.** (1 connections) — `server/tests/unit/realtime/messaging/test_message_broadcaster.py`

## Relationships

- [realtime messaging message](realtime_messaging_message.md) (8 shared connections)
- [Room Broadcast](Room_Broadcast.md) (5 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (4 shared connections)
- [combat configuration service](combat_configuration_service.md) (2 shared connections)
- [combat services messaging](combat_services_messaging.md) (2 shared connections)

## Source Files

- `server/realtime/messaging/__init__.py`
- `server/realtime/messaging/message_broadcaster.py`
- `server/tests/unit/realtime/messaging/test_message_broadcaster.py`

## Audit Trail

- EXTRACTED: 57 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*