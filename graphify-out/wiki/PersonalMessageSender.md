# PersonalMessageSender

> 28 nodes

## Key Concepts

- **PersonalMessageSender** (13 connections) — `server/realtime/messaging/personal_message_sender.py`
- **.send_message()** (7 connections) — `server/realtime/messaging/personal_message_sender.py`
- **._send_to_websocket()** (7 connections) — `server/realtime/messaging/personal_message_sender.py`
- **Any** (7 connections)
- **UUID** (7 connections)
- **._prepare_payload()** (6 connections) — `server/realtime/messaging/personal_message_sender.py`
- **._queue_message_if_needed()** (6 connections) — `server/realtime/messaging/personal_message_sender.py`
- **test_personal_message_sender.py** (6 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **.get_delivery_stats()** (4 connections) — `server/realtime/messaging/personal_message_sender.py`
- **.__init__()** (4 connections) — `server/realtime/messaging/personal_message_sender.py`
- **_websocket_is_sendable()** (4 connections) — `server/realtime/messaging/personal_message_sender.py`
- **_make_sender()** (4 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **test_send_to_websocket_accept_first_is_expected_close()** (4 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **test_send_to_websocket_skips_non_connected_client_state()** (4 connections) — `server/tests/unit/realtime/test_personal_message_sender.py`
- **_is_expected_websocket_close()** (3 connections) — `server/realtime/messaging/personal_message_sender.py`
- **asyncio** (2 connections)
- **Send message to a single WebSocket connection. Returns True if successful.** (1 connections) — `server/realtime/messaging/personal_message_sender.py`
- **Queue message if no active connections.** (1 connections) — `server/realtime/messaging/personal_message_sender.py`
- **Send a personal message to a player via WebSocket. Args: player_id: The…** (1 connections) — `server/realtime/messaging/personal_message_sender.py`
- **Get message delivery statistics for a player.** (1 connections) — `server/realtime/messaging/personal_message_sender.py`
- **False when Starlette client/application state cannot accept a send.** (1 connections) — `server/realtime/messaging/personal_message_sender.py`
- **True for send-after-close / accept-first races (log at debug, not warning).** (1 connections) — `server/realtime/messaging/personal_message_sender.py`
- **Sends personal messages to individual players. This class provides: - Personal…** (1 connections) — `server/realtime/messaging/personal_message_sender.py`
- **Initialize the personal message sender. Args: message_queue: MessageQueue…** (1 connections) — `server/realtime/messaging/personal_message_sender.py`
- **Prepare and optimize the payload for sending.** (1 connections) — `server/realtime/messaging/personal_message_sender.py`
- *... and 3 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (6 shared connections)
- [connection_initialization.py](connection_initialization.py.md) (2 shared connections)
- [MessageBroadcaster](MessageBroadcaster.md) (1 shared connections)
- [deque](deque.md) (1 shared connections)

## Source Files

- `server/realtime/messaging/personal_message_sender.py`
- `server/tests/unit/realtime/test_personal_message_sender.py`

## Audit Trail

- EXTRACTED: 54 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*