# Server Realtime (90)

> 14 nodes

## Key Concepts

- **.send_message()** (8 connections) — `server/realtime/messaging/personal_message_sender.py`
- **UUID** (7 connections)
- **._prepare_payload()** (7 connections) — `server/realtime/messaging/personal_message_sender.py`
- **Any** (6 connections)
- **._queue_message_if_needed()** (6 connections) — `server/realtime/messaging/personal_message_sender.py`
- **._send_to_websocket()** (5 connections) — `server/realtime/messaging/personal_message_sender.py`
- **.__init__()** (4 connections) — `server/realtime/messaging/personal_message_sender.py`
- **.get_delivery_stats()** (4 connections) — `server/realtime/messaging/personal_message_sender.py`
- **Initialize the personal message sender.          Args:             message_queue** (1 connections) — `server/realtime/messaging/personal_message_sender.py`
- **Prepare and optimize the payload for sending.** (1 connections) — `server/realtime/messaging/personal_message_sender.py`
- **Send message to a single WebSocket connection. Returns True if successful.** (1 connections) — `server/realtime/messaging/personal_message_sender.py`
- **Queue message if no active connections.** (1 connections) — `server/realtime/messaging/personal_message_sender.py`
- **Send a personal message to a player via WebSocket.          Args:             pl** (1 connections) — `server/realtime/messaging/personal_message_sender.py`
- **Get message delivery statistics for a player.** (1 connections) — `server/realtime/messaging/personal_message_sender.py`

## Relationships

- [Server Realtime (43)](Server_Realtime_%2843%29.md) (7 shared connections)
- [Server Persistence](Server_Persistence.md) (2 shared connections)
- [Server Realtime (98)](Server_Realtime_%2898%29.md) (1 shared connections)
- [Server Realtime (15)](Server_Realtime_%2815%29.md) (1 shared connections)

## Source Files

- `server/realtime/messaging/personal_message_sender.py`

## Audit Trail

- EXTRACTED: 50 (94%)
- INFERRED: 3 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*