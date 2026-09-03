# Connection Establishment

> 28 nodes

## Key Concepts

- **_EstablishmentConnectionManager** (25 connections) — `server/realtime/connection_establishment.py`
- **UUID** (16 connections)
- **_track_player_presence()** (13 connections) — `server/realtime/connection_establishment.py`
- **_setup_player_and_room()** (11 connections) — `server/realtime/connection_establishment.py`
- **_bind_accepted_websocket()** (9 connections) — `server/realtime/connection_establishment.py`
- **_register_new_connection()** (9 connections) — `server/realtime/connection_establishment.py`
- **_setup_connection_metadata()** (9 connections) — `server/realtime/connection_establishment.py`
- **_setup_session_tracking()** (9 connections) — `server/realtime/connection_establishment.py`
- **_update_player_connection_list()** (9 connections) — `server/realtime/connection_establishment.py`
- **_reconcile_prior_session()** (6 connections) — `server/realtime/connection_establishment.py`
- **Player** (5 connections)
- **.broadcast_connection_message()** (4 connections) — `server/realtime/connection_establishment.py`
- **.get_player()** (4 connections) — `server/realtime/connection_establishment.py`
- **.track_player_connected()** (4 connections) — `server/realtime/connection_establishment.py`
- **WebSocket** (3 connections)
- **Protocol** (1 connections)
- **Update player's connection list to only include active connections. Args:…** (1 connections) — `server/realtime/connection_establishment.py`
- **Register a new WebSocket connection. Args: websocket: The WebSocket connection…** (1 connections) — `server/realtime/connection_establishment.py`
- **Create and store connection metadata. Args: connection_id: The connection ID…** (1 connections) — `server/realtime/connection_establishment.py`
- **Track connection in session. Args: connection_id: The connection ID player_id:…** (1 connections) — `server/realtime/connection_establishment.py`
- **Register an accepted socket and attach session metadata.** (1 connections) — `server/realtime/connection_establishment.py`
- **Get player and setup room subscription. Args: player_id: The player's ID…** (1 connections) — `server/realtime/connection_establishment.py`
- **Track player presence and broadcast connection message. Args: player_id: The…** (1 connections) — `server/realtime/connection_establishment.py`
- **Connection manager surface used by establishment helpers.** (1 connections) — `server/realtime/connection_establishment.py`
- **Settle a differing prior session before a new socket is registered. ADR-018…** (1 connections) — `server/realtime/connection_establishment.py`
- *... and 3 more nodes in this community*

## Relationships

- [Test Connection Establishment](Test_Connection_Establishment.md) (34 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (13 shared connections)
- [Test Connection Establishment Ws](Test_Connection_Establishment_Ws.md) (7 shared connections)
- [Test Connection Rate Limiter](Test_Connection_Rate_Limiter.md) (1 shared connections)
- [Test Message Queue](Test_Message_Queue.md) (1 shared connections)
- [Connection Session Management](Connection_Session_Management.md) (1 shared connections)
- [Test Rest Command](Test_Rest_Command.md) (1 shared connections)
- [Test Rest And Grace Period](Test_Rest_And_Grace_Period.md) (1 shared connections)

## Source Files

- `server/realtime/connection_establishment.py`

## Audit Trail

- EXTRACTED: 100 (96%)
- INFERRED: 4 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*