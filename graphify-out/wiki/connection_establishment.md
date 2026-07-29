# connection establishment

> 18 nodes

## Key Concepts

- **establish_websocket_connection()** (22 connections) — `server/realtime/connection_establishment.py`
- **connection_establishment.py** (17 connections) — `server/realtime/connection_establishment.py`
- **UUID** (12 connections)
- **Any** (12 connections)
- **_setup_player_and_room()** (10 connections) — `server/realtime/connection_establishment.py`
- **_setup_session_tracking()** (9 connections) — `server/realtime/connection_establishment.py`
- **_cleanup_failed_connection()** (9 connections) — `server/realtime/connection_establishment.py`
- **_setup_connection_metadata()** (8 connections) — `server/realtime/connection_establishment.py`
- **_track_player_presence()** (8 connections) — `server/realtime/connection_establishment.py`
- **_cancel_rest_countdown_if_active()** (5 connections) — `server/realtime/connection_establishment.py`
- **Connection establishment management for connection manager.  This module handles** (1 connections) — `server/realtime/connection_establishment.py`
- **Create and store connection metadata.      Args:         connection_id: The conn** (1 connections) — `server/realtime/connection_establishment.py`
- **Track connection in session.      Args:         connection_id: The connection ID** (1 connections) — `server/realtime/connection_establishment.py`
- **Get player and setup room subscription.      Args:         player_id: The player** (1 connections) — `server/realtime/connection_establishment.py`
- **Track player presence and broadcast connection message.      Args:         playe** (1 connections) — `server/realtime/connection_establishment.py`
- **Cleanup connection on failure.      Args:         connection_id: The connection** (1 connections) — `server/realtime/connection_establishment.py`
- **Cancel leftover /rest countdown from a prior session (crashed client / mid-rest** (1 connections) — `server/realtime/connection_establishment.py`
- **Establish a new WebSocket connection.      Args:         websocket: The WebSocke** (1 connections) — `server/realtime/connection_establishment.py`

## Relationships

- [test connection establishment](test_connection_establishment.md) (19 shared connections)
- [cleanup dead connections()](cleanup_dead_connections%28%29_2.md) (6 shared connections)
- [WebSocket](WebSocket.md) (5 shared connections)
- [find dead connections()](find_dead_connections%28%29.md) (4 shared connections)
- [Update player's connection list to](Update_player%27s_connection_list_to.md) (3 shared connections)
- [Any](Any.md) (2 shared connections)
- [Test setup player and room()](Test_setup_player_and_room%28%29.md) (2 shared connections)
- [main()](main%28%29.md) (1 shared connections)
- [Test setup connection metadata() creates](Test_setup_connection_metadata%28%29_creates.md) (1 shared connections)
- [Test setup session tracking() adds](Test_setup_session_tracking%28%29_adds.md) (1 shared connections)
- [.connect websocket()](connect_websocket%28%29.md) (1 shared connections)
- [Reconnect cancels an in progress](Reconnect_cancels_an_in_progress.md) (1 shared connections)

## Source Files

- `server/realtime/connection_establishment.py`

## Audit Trail

- EXTRACTED: 120 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*