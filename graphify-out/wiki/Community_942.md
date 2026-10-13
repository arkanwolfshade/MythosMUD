# Community 942

> 16 nodes

## Key Concepts

- **.send_message()** (8 connections) — `server/realtime/messaging/personal_message_sender.py`
- **UUID** (8 connections)
- **._prepare_payload()** (6 connections) — `server/realtime/messaging/personal_message_sender.py`
- **._send_to_websocket()** (6 connections) — `server/realtime/messaging/personal_message_sender.py`
- **Any** (6 connections)
- **_coerce_player_uuid()** (5 connections) — `server/realtime/messaging/personal_message_sender.py`
- **._queue_message_if_needed()** (5 connections) — `server/realtime/messaging/personal_message_sender.py`
- **.get_delivery_stats()** (4 connections) — `server/realtime/messaging/personal_message_sender.py`
- **.__init__()** (4 connections) — `server/realtime/messaging/personal_message_sender.py`
- **Send message to a single WebSocket connection. Returns True if successful.** (1 connections) — `server/realtime/messaging/personal_message_sender.py`
- **Queue message if no active connections.** (1 connections) — `server/realtime/messaging/personal_message_sender.py`
- **Send a personal message to a player via WebSocket. ``player_websockets`` is…** (1 connections) — `server/realtime/messaging/personal_message_sender.py`
- **Get message delivery statistics for a player.** (1 connections) — `server/realtime/messaging/personal_message_sender.py`
- **Normalise a player id to UUID so connection lookups keyed by UUID cannot…** (1 connections) — `server/realtime/messaging/personal_message_sender.py`
- **Initialize the personal message sender. Args: message_queue: MessageQueue…** (1 connections) — `server/realtime/messaging/personal_message_sender.py`
- **Prepare and optimize the payload for sending.** (1 connections) — `server/realtime/messaging/personal_message_sender.py`

## Relationships

- [Community 731](Community_731.md) (6 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (2 shared connections)
- [Community 226](Community_226.md) (1 shared connections)
- [Community 473](Community_473.md) (1 shared connections)
- [Community 164](Community_164.md) (1 shared connections)

## Source Files

- `server/realtime/messaging/personal_message_sender.py`

## Audit Trail

- EXTRACTED: 34 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*