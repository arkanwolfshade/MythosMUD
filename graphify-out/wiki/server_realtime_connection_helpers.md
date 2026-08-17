# server realtime connection helpers

> 19 nodes

## Key Concepts

- **connection_helpers.py** (22 connections) — `server/realtime/connection_helpers.py`
- **send_personal_message_old_impl()** (10 connections) — `server/realtime/connection_helpers.py`
- **Any** (10 connections)
- **broadcast_global_event_impl()** (6 connections) — `server/realtime/connection_helpers.py`
- **broadcast_room_event_impl()** (6 connections) — `server/realtime/connection_helpers.py`
- **_queue_message_if_needed()** (6 connections) — `server/realtime/connection_helpers.py`
- **mark_player_seen_impl()** (5 connections) — `server/realtime/connection_helpers.py`
- **test_broadcast_global_event_impl()** (4 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_mark_player_seen_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_queue_message_if_needed()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Helper utilities for connection manager. This module provides utility functions…** (1 connections) — `server/realtime/connection_helpers.py`
- **Queue message for later delivery if no active connections. Args: player_id: The…** (1 connections) — `server/realtime/connection_helpers.py`
- **Send a personal message to a player via WebSocket (deprecated implementation).…** (1 connections) — `server/realtime/connection_helpers.py`
- **Broadcast a room-specific event to all players in the room.** (1 connections) — `server/realtime/connection_helpers.py`
- **Broadcast a global event to all connected players.** (1 connections) — `server/realtime/connection_helpers.py`
- **Update last-seen timestamp for a player and all their connections.** (1 connections) — `server/realtime/connection_helpers.py`
- **Test broadcast_global_event_impl() broadcasts global event.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Test mark_player_seen_impl() marks player as seen.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Test _queue_message_if_needed() queues message.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`

## Relationships

- [server realtime connection helpers convert](server_realtime_connection_helpers_convert.md) (12 shared connections)
- [server realtime connection helpers rationale](server_realtime_connection_helpers_rationale.md) (10 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (4 shared connections)
- [server realtime envelope build event](server_realtime_envelope_build_event.md) (3 shared connections)
- [server realtime connection helpers optimize](server_realtime_connection_helpers_optimize.md) (3 shared connections)
- [server realtime connection helpers handle](server_realtime_connection_helpers_handle.md) (2 shared connections)
- [scripts populate test npc databases](scripts_populate_test_npc_databases.md) (1 shared connections)
- [server commands rest command](server_commands_rest_command.md) (1 shared connections)
- [server app game tick counter](server_app_game_tick_counter.md) (1 shared connections)
- [server realtime payload optimizer](server_realtime_payload_optimizer.md) (1 shared connections)

## Source Files

- `server/realtime/connection_helpers.py`
- `server/tests/unit/realtime/test_connection_helpers_impl.py`

## Audit Trail

- EXTRACTED: 61 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*