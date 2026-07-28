# Server Realtime (93)

> 13 nodes

## Key Concepts

- **Any** (10 connections)
- **mark_player_seen_impl()** (8 connections) — `server/realtime/connection_helpers.py`
- **broadcast_room_event_impl()** (6 connections) — `server/realtime/connection_helpers.py`
- **broadcast_global_event_impl()** (6 connections) — `server/realtime/connection_helpers.py`
- **test_broadcast_room_event_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_broadcast_global_event_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **test_mark_player_seen_impl()** (3 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Broadcast a room-specific event to all players in the room.** (1 connections) — `server/realtime/connection_helpers.py`
- **Broadcast a global event to all connected players.** (1 connections) — `server/realtime/connection_helpers.py`
- **Update last-seen timestamp for a player and all their connections.** (1 connections) — `server/realtime/connection_helpers.py`
- **Test broadcast_room_event_impl() broadcasts room event.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Test broadcast_global_event_impl() broadcasts global event.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`
- **Test mark_player_seen_impl() marks player as seen.** (1 connections) — `server/tests/unit/realtime/test_connection_helpers_impl.py`

## Relationships

- [Server Realtime (77)](Server_Realtime_%2877%29.md) (7 shared connections)
- [Server Realtime (98)](Server_Realtime_%2898%29.md) (4 shared connections)
- [Server Realtime (104)](Server_Realtime_%28104%29.md) (2 shared connections)
- [Server Realtime (2)](Server_Realtime_%282%29.md) (2 shared connections)
- [Server Realtime (84)](Server_Realtime_%2884%29.md) (1 shared connections)
- [Server Realtime (118)](Server_Realtime_%28118%29.md) (1 shared connections)
- [Server Realtime (112)](Server_Realtime_%28112%29.md) (1 shared connections)
- [Server Persistence](Server_Persistence.md) (1 shared connections)
- [Server Realtime (7)](Server_Realtime_%287%29.md) (1 shared connections)
- [Server Realtime (4)](Server_Realtime_%284%29.md) (1 shared connections)

## Source Files

- `server/realtime/connection_helpers.py`
- `server/tests/unit/realtime/test_connection_helpers_impl.py`

## Audit Trail

- EXTRACTED: 44 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*