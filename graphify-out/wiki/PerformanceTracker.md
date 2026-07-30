# PerformanceTracker

> 21 nodes

## Key Concepts

- **connection_establishment.py** (24 connections) — `server/realtime/connection_establishment.py`
- **establish_websocket_connection()** (23 connections) — `server/realtime/connection_establishment.py`
- **UUID** (12 connections)
- **Any** (12 connections)
- **_setup_player_and_room()** (10 connections) — `server/realtime/connection_establishment.py`
- **_cleanup_failed_connection()** (10 connections) — `server/realtime/connection_establishment.py`
- **_register_new_connection()** (9 connections) — `server/realtime/connection_establishment.py`
- **_setup_connection_metadata()** (9 connections) — `server/realtime/connection_establishment.py`
- **_setup_session_tracking()** (9 connections) — `server/realtime/connection_establishment.py`
- **_track_player_presence()** (8 connections) — `server/realtime/connection_establishment.py`
- **_cancel_rest_countdown_if_active()** (6 connections) — `server/realtime/connection_establishment.py`
- **WebSocket** (2 connections)
- **Connection establishment management for connection manager.  This module handles** (1 connections) — `server/realtime/connection_establishment.py`
- **Register a new WebSocket connection.      Args:         websocket: The WebSocket** (1 connections) — `server/realtime/connection_establishment.py`
- **Create and store connection metadata.      Args:         connection_id: The conn** (1 connections) — `server/realtime/connection_establishment.py`
- **Track connection in session.      Args:         connection_id: The connection ID** (1 connections) — `server/realtime/connection_establishment.py`
- **Get player and setup room subscription.      Args:         player_id: The player** (1 connections) — `server/realtime/connection_establishment.py`
- **Track player presence and broadcast connection message.      Args:         playe** (1 connections) — `server/realtime/connection_establishment.py`
- **Cleanup connection on failure.      Args:         connection_id: The connection** (1 connections) — `server/realtime/connection_establishment.py`
- **Cancel leftover /rest countdown from a prior session (crashed client / mid-rest** (1 connections) — `server/realtime/connection_establishment.py`
- **Establish a new WebSocket connection.      Args:         websocket: The WebSocke** (1 connections) — `server/realtime/connection_establishment.py`

## Relationships

- [test connection establishment](test_connection_establishment.md) (18 shared connections)
- [middleware()](middleware%28%29.md) (6 shared connections)
- [Player](Player.md) (6 shared connections)
- [real time](real_time.md) (4 shared connections)
- [Test get spawn rules() successfully](Test_get_spawn_rules%28%29_successfully.md) (4 shared connections)
- [Test subscribe to subject returns](Test_subscribe_to_subject_returns.md) (3 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (2 shared connections)
- [world](world.md) (2 shared connections)
- [get current tick()](get_current_tick%28%29.md) (1 shared connections)
- [test_register_new_connection_existing_player](test_register_new_connection_existing_player.md) (1 shared connections)
- [test_setup_connection_metadata_no_session_token](test_setup_connection_metadata_no_session_token.md) (1 shared connections)
- [test_setup_session_tracking_existing_session](test_setup_session_tracking_existing_session.md) (1 shared connections)

## Source Files

- `server/realtime/connection_establishment.py`

## Audit Trail

- EXTRACTED: 141 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*