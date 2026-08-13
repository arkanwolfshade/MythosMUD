# PersonalMessageSender

> 16 nodes

## Key Concepts

- **PersonalMessageSender** (11 connections) — `server/realtime/messaging/personal_message_sender.py`
- **.send_message()** (7 connections) — `server/realtime/messaging/personal_message_sender.py`
- **UUID** (7 connections)
- **._prepare_payload()** (6 connections) — `server/realtime/messaging/personal_message_sender.py`
- **._queue_message_if_needed()** (6 connections) — `server/realtime/messaging/personal_message_sender.py`
- **Any** (6 connections)
- **._send_to_websocket()** (5 connections) — `server/realtime/messaging/personal_message_sender.py`
- **.get_delivery_stats()** (4 connections) — `server/realtime/messaging/personal_message_sender.py`
- **.__init__()** (4 connections) — `server/realtime/messaging/personal_message_sender.py`
- **Send message to a single WebSocket connection. Returns True if successful.** (1 connections) — `server/realtime/messaging/personal_message_sender.py`
- **Queue message if no active connections.** (1 connections) — `server/realtime/messaging/personal_message_sender.py`
- **Send a personal message to a player via WebSocket. Args: player_id: The…** (1 connections) — `server/realtime/messaging/personal_message_sender.py`
- **Get message delivery statistics for a player.** (1 connections) — `server/realtime/messaging/personal_message_sender.py`
- **Sends personal messages to individual players. This class provides: - Personal…** (1 connections) — `server/realtime/messaging/personal_message_sender.py`
- **Initialize the personal message sender. Args: message_queue: MessageQueue…** (1 connections) — `server/realtime/messaging/personal_message_sender.py`
- **Prepare and optimize the payload for sending.** (1 connections) — `server/realtime/messaging/personal_message_sender.py`

## Relationships

- [get_logger](get_logger.md) (4 shared connections)
- [test_connection_initialization.py](test_connection_initialization.py.md) (1 shared connections)
- [MessageBroadcaster](MessageBroadcaster.md) (1 shared connections)
- [deque](deque.md) (1 shared connections)

## Source Files

- `server/realtime/messaging/personal_message_sender.py`

## Audit Trail

- EXTRACTED: 34 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*