# server realtime connection establishment

> 34 nodes

## Key Concepts

- **connection_establishment.py** (42 connections) — `server/realtime/connection_establishment.py`
- **_EstablishmentConnectionManager** (25 connections) — `server/realtime/connection_establishment.py`
- **establish_websocket_connection()** (25 connections) — `server/realtime/connection_establishment.py`
- **UUID** (16 connections)
- **_track_player_presence()** (13 connections) — `server/realtime/connection_establishment.py`
- **_find_dead_connections()** (11 connections) — `server/realtime/connection_establishment.py`
- **_setup_player_and_room()** (11 connections) — `server/realtime/connection_establishment.py`
- **_bind_accepted_websocket()** (9 connections) — `server/realtime/connection_establishment.py`
- **_cleanup_failed_connection()** (9 connections) — `server/realtime/connection_establishment.py`
- **_register_new_connection()** (9 connections) — `server/realtime/connection_establishment.py`
- **_setup_connection_metadata()** (9 connections) — `server/realtime/connection_establishment.py`
- **_setup_session_tracking()** (9 connections) — `server/realtime/connection_establishment.py`
- **_reconcile_prior_session()** (6 connections) — `server/realtime/connection_establishment.py`
- **Player** (5 connections)
- **.broadcast_connection_message()** (4 connections) — `server/realtime/connection_establishment.py`
- **.get_player()** (4 connections) — `server/realtime/connection_establishment.py`
- **.track_player_connected()** (4 connections) — `server/realtime/connection_establishment.py`
- **WebSocket** (3 connections)
- **Protocol** (1 connections)
- **Connection establishment management for connection manager. This module handles…** (1 connections) — `server/realtime/connection_establishment.py`
- **Register a new WebSocket connection. Args: websocket: The WebSocket connection…** (1 connections) — `server/realtime/connection_establishment.py`
- **Create and store connection metadata. Args: connection_id: The connection ID…** (1 connections) — `server/realtime/connection_establishment.py`
- **Track connection in session. Args: connection_id: The connection ID player_id:…** (1 connections) — `server/realtime/connection_establishment.py`
- **Register an accepted socket and attach session metadata.** (1 connections) — `server/realtime/connection_establishment.py`
- **Get player and setup room subscription. Args: player_id: The player's ID…** (1 connections) — `server/realtime/connection_establishment.py`
- *... and 9 more nodes in this community*

## Relationships

- [server realtime connection establishment cleanup](server_realtime_connection_establishment_cleanup.md) (40 shared connections)
- [server tests unit realtime test](server_tests_unit_realtime_test.md) (14 shared connections)
- [server realtime connection models](server_realtime_connection_models.md) (4 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (4 shared connections)
- [deque](deque.md) (3 shared connections)
- [server realtime connection error methods](server_realtime_connection_error_methods.md) (3 shared connections)
- [server realtime connection session management](server_realtime_connection_session_management.md) (3 shared connections)
- [server realtime disconnect grace period](server_realtime_disconnect_grace_period.md) (3 shared connections)
- [server realtime room subscription manager](server_realtime_room_subscription_manager.md) (2 shared connections)
- [server realtime rate limiter py](server_realtime_rate_limiter_py.md) (2 shared connections)
- [server commands combat handler combatcommandhandler](server_commands_combat_handler_combatcommandhandler.md) (2 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (2 shared connections)

## Source Files

- `server/realtime/connection_establishment.py`

## Audit Trail

- EXTRACTED: 155 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*