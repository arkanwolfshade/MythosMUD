# PersonalMessageSender

> 16 nodes · cohesion 0.23

## Key Concepts

- **PersonalMessageSender** (12 connections) — `server/realtime/messaging/personal_message_sender.py`
- **.send_message()** (8 connections) — `server/realtime/messaging/personal_message_sender.py`
- **._prepare_payload()** (7 connections) — `server/realtime/messaging/personal_message_sender.py`
- **UUID** (7 connections)
- **._queue_message_if_needed()** (6 connections) — `server/realtime/messaging/personal_message_sender.py`
- **Any** (6 connections)
- **._send_to_websocket()** (5 connections) — `server/realtime/messaging/personal_message_sender.py`
- **.get_delivery_stats()** (4 connections) — `server/realtime/messaging/personal_message_sender.py`
- **.__init__()** (4 connections) — `server/realtime/messaging/personal_message_sender.py`
- **Send message to a single WebSocket connection. Returns True if successful.** (1 connections) — `server/realtime/messaging/personal_message_sender.py`
- **Queue message if no active connections.** (1 connections) — `server/realtime/messaging/personal_message_sender.py`
- **Send a personal message to a player via WebSocket.          Args:             pl** (1 connections) — `server/realtime/messaging/personal_message_sender.py`
- **Get message delivery statistics for a player.** (1 connections) — `server/realtime/messaging/personal_message_sender.py`
- **Sends personal messages to individual players.      This class provides:     - P** (1 connections) — `server/realtime/messaging/personal_message_sender.py`
- **Initialize the personal message sender.          Args:             message_queue** (1 connections) — `server/realtime/messaging/personal_message_sender.py`
- **Prepare and optimize the payload for sending.** (1 connections) — `server/realtime/messaging/personal_message_sender.py`

## Relationships

- [get_logger](get_logger.md) (3 shared connections)
- [DatabaseError](DatabaseError.md) (2 shared connections)
- [.__init__](__init__.md) (1 shared connections)
- [connection_manager.py](connection_manager.py.md) (1 shared connections)
- [MessageBroadcaster](MessageBroadcaster.md) (1 shared connections)
- [test_connection_helpers_impl.py](test_connection_helpers_impl.py.md) (1 shared connections)
- [deque](deque.md) (1 shared connections)

## Source Files

- `server/realtime/messaging/personal_message_sender.py`

## Audit Trail

- EXTRACTED: 63 (95%)
- INFERRED: 3 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*