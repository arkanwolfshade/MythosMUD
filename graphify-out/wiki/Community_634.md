# Community 634

> 27 nodes

## Key Concepts

- **connection_helpers.py** (21 connections) — `server/realtime/connection_helpers.py`
- **send_personal_message_old_impl()** (12 connections) — `server/realtime/connection_helpers.py`
- **Any** (10 connections)
- **_update_delivery_status()** (8 connections) — `server/realtime/connection_helpers.py`
- **mark_player_seen_impl()** (7 connections) — `server/realtime/connection_helpers.py`
- **broadcast_global_event_impl()** (6 connections) — `server/realtime/connection_helpers.py`
- **broadcast_room_event_impl()** (6 connections) — `server/realtime/connection_helpers.py`
- **_queue_message_if_needed()** (6 connections) — `server/realtime/connection_helpers.py`
- **test_send_personal_message_old_impl()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_mark_player_seen_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_queue_message_if_needed()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_update_delivery_status_failed()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_update_delivery_status_no_attempts()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_update_delivery_status_success()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Helper utilities for connection manager. This module provides utility functions…** (1 connections) — `server/realtime/connection_helpers.py`
- **Queue message for later delivery if no active connections. Args: player_id: The…** (1 connections) — `server/realtime/connection_helpers.py`
- **Update final delivery status based on connection results. Args:…** (1 connections) — `server/realtime/connection_helpers.py`
- **Send a personal message to a player via WebSocket (deprecated implementation).…** (1 connections) — `server/realtime/connection_helpers.py`
- **Broadcast a room-specific event to all players in the room.** (1 connections) — `server/realtime/connection_helpers.py`
- **Broadcast a global event to all connected players.** (1 connections) — `server/realtime/connection_helpers.py`
- **Update last-seen timestamp for a player and all their connections.** (1 connections) — `server/realtime/connection_helpers.py`
- **Test send_personal_message_old_impl() sends message.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Test mark_player_seen_impl() marks player as seen.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Test _update_delivery_status() when no connection attempts.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Test _queue_message_if_needed() queues message.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- *... and 2 more nodes in this community*

## Relationships

- [Community 472](Community_472.md) (19 shared connections)
- [Community 787](Community_787.md) (7 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (5 shared connections)
- [Community 41](Community_41.md) (3 shared connections)
- [Community 188](Community_188.md) (2 shared connections)
- [Invite & NPC DB Scripts](Invite_&_NPC_DB_Scripts.md) (2 shared connections)
- [Community 1443](Community_1443.md) (2 shared connections)
- [Community 76](Community_76.md) (1 shared connections)
- [Community 473](Community_473.md) (1 shared connections)

## Source Files

- `server/realtime/connection_helpers.py`
- `server/tests/unit/realtime/test_connection_helpers_impl.py`

## Audit Trail

- EXTRACTED: 75 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*