# connection_helpers.py

> 23 nodes

## Key Concepts

- **connection_helpers.py** (22 connections) — `server/realtime/connection_helpers.py`
- **send_personal_message_old_impl()** (12 connections) — `server/realtime/connection_helpers.py`
- **Any** (10 connections)
- **mark_player_seen_impl()** (7 connections) — `server/realtime/connection_helpers.py`
- **broadcast_global_event_impl()** (6 connections) — `server/realtime/connection_helpers.py`
- **broadcast_room_event_impl()** (6 connections) — `server/realtime/connection_helpers.py`
- **_queue_message_if_needed()** (6 connections) — `server/realtime/connection_helpers.py`
- **.mark_player_seen()** (4 connections) — `server/realtime/connection_manager.py`
- **.send_personal_message_old()** (4 connections) — `server/realtime/connection_manager.py`
- **test_send_personal_message_old_impl()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_mark_player_seen_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_queue_message_if_needed()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Helper utilities for connection manager. This module provides utility functions…** (1 connections) — `server/realtime/connection_helpers.py`
- **Queue message for later delivery if no active connections. Args: player_id: The…** (1 connections) — `server/realtime/connection_helpers.py`
- **Send a personal message to a player via WebSocket (deprecated implementation).…** (1 connections) — `server/realtime/connection_helpers.py`
- **Broadcast a room-specific event to all players in the room.** (1 connections) — `server/realtime/connection_helpers.py`
- **Broadcast a global event to all connected players.** (1 connections) — `server/realtime/connection_helpers.py`
- **Update last-seen timestamp for a player and all their connections.** (1 connections) — `server/realtime/connection_helpers.py`
- **Update last-seen timestamp for a player and all their connections.** (1 connections) — `server/realtime/connection_manager.py`
- **Send a personal message to a player via WebSocket (deprecated).** (1 connections) — `server/realtime/connection_manager.py`
- **Test send_personal_message_old_impl() sends message.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Test mark_player_seen_impl() marks player as seen.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Test _queue_message_if_needed() queues message.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`

## Relationships

- [test_connection_helpers_impl.py](test_connection_helpers_impl.py.md) (16 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [connection_manager.py](connection_manager.py.md) (3 shared connections)
- [_optimize_payload](_optimize_payload.md) (3 shared connections)
- [_update_delivery_status](_update_delivery_status.md) (3 shared connections)
- [convert_uuids_to_strings](convert_uuids_to_strings.md) (3 shared connections)
- [UUID](UUID.md) (2 shared connections)
- [ConnectionManager](ConnectionManager.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [handle_new_login_impl](handle_new_login_impl.md) (2 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)
- [test_rest_command.py](test_rest_command.py.md) (1 shared connections)

## Source Files

- `server/realtime/connection_helpers.py`
- `server/realtime/connection_manager.py`
- `server/tests/unit/realtime/test_connection_helpers_impl.py`

## Audit Trail

- EXTRACTED: 71 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*