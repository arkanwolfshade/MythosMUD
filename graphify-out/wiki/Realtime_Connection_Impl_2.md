# Realtime Connection Impl

> 21 nodes · cohesion 0.12

## Key Concepts

- **connection_helpers.py** (19 connections) — `server/realtime/connection_helpers.py`
- **send_personal_message_old_impl()** (12 connections) — `server/realtime/connection_helpers.py`
- **Any** (10 connections) — `server/realtime/connection_helpers.py`
- **mark_player_seen_impl()** (7 connections) — `server/realtime/connection_helpers.py`
- **broadcast_global_event_impl()** (6 connections) — `server/realtime/connection_helpers.py`
- **broadcast_room_event_impl()** (6 connections) — `server/realtime/connection_helpers.py`
- **_queue_message_if_needed()** (6 connections) — `server/realtime/connection_helpers.py`
- **test_mark_player_seen_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_queue_message_if_needed()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_send_personal_message_old_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_send_personal_message_old_impl_no_connections()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Helper utilities for connection manager.  This module provides utility functions** (1 connections) — `server/realtime/connection_helpers.py`
- **Queue message for later delivery if no active connections.      Args:         pl** (1 connections) — `server/realtime/connection_helpers.py`
- **Send a personal message to a player via WebSocket (deprecated implementation).** (1 connections) — `server/realtime/connection_helpers.py`
- **Broadcast a room-specific event to all players in the room.** (1 connections) — `server/realtime/connection_helpers.py`
- **Broadcast a global event to all connected players.** (1 connections) — `server/realtime/connection_helpers.py`
- **Update last-seen timestamp for a player and all their connections.** (1 connections) — `server/realtime/connection_helpers.py`
- **Test send_personal_message_old_impl() sends message.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Test mark_player_seen_impl() marks player as seen.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Test send_personal_message_old_impl() when no connections.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Test _queue_message_if_needed() queues message.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`

## Relationships

- [[Realtime Connection Impl]] (22 shared connections)
- [[NPC Admin API]] (6 shared connections)
- [[Room Occupant Events]] (5 shared connections)
- [[Combat Player Broadcasts]] (3 shared connections)
- [[Message Broadcaster Tests]] (2 shared connections)

## Source Files

- `server/realtime/connection_helpers.py`
- `server/tests/unit/realtime/test_connection_helpers_impl.py`

## Audit Trail

- EXTRACTED: 88 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
