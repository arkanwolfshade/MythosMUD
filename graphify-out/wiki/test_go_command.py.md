# test_go_command.py

> 74 nodes

## Key Concepts

- **test_connection_establishment.py** (59 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **connection_establishment.py** (42 connections) — `server/realtime/connection_establishment.py`
- **_EstablishmentConnectionManager** (25 connections) — `server/realtime/connection_establishment.py`
- **establish_websocket_connection()** (23 connections) — `server/realtime/connection_establishment.py`
- **UUID** (16 connections)
- **_track_player_presence()** (13 connections) — `server/realtime/connection_establishment.py`
- **_find_dead_connections()** (11 connections) — `server/realtime/connection_establishment.py`
- **_setup_player_and_room()** (11 connections) — `server/realtime/connection_establishment.py`
- **asyncio** (11 connections)
- **_cleanup_dead_connections()** (10 connections) — `server/realtime/connection_establishment.py`
- **_bind_accepted_websocket()** (9 connections) — `server/realtime/connection_establishment.py`
- **_cleanup_failed_connection()** (9 connections) — `server/realtime/connection_establishment.py`
- **_register_new_connection()** (9 connections) — `server/realtime/connection_establishment.py`
- **_setup_connection_metadata()** (9 connections) — `server/realtime/connection_establishment.py`
- **_setup_session_tracking()** (9 connections) — `server/realtime/connection_establishment.py`
- **_update_player_connection_list()** (9 connections) — `server/realtime/connection_establishment.py`
- **_remove_dead_connection()** (7 connections) — `server/realtime/connection_establishment.py`
- **_reconcile_prior_session()** (6 connections) — `server/realtime/connection_establishment.py`
- **test_cleanup_dead_connections_empty_list()** (6 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_player_and_room_no_persistence()** (6 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_player_and_room_no_player()** (6 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_player_and_room_no_room_id()** (6 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_player_and_room_success()** (6 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_track_player_presence_cancels_leftover_rest()** (6 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_track_player_presence_existing_player()** (6 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- *... and 49 more nodes in this community*

## Relationships

- [websocket_handler_commands.py](websocket_handler_commands.py.md) (81 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (16 shared connections)
- [P3 · realtime-connection + events-nats](P3_·_realtime-connection_+_events-nats.md) (4 shared connections)
- [ContainerComponent](ContainerComponent.md) (4 shared connections)
- [population_control.py](population_control.py.md) (3 shared connections)
- [PrototypeRegistry](PrototypeRegistry.md) (3 shared connections)
- [NATSRetryHandler](NATSRetryHandler.md) (2 shared connections)
- [chat_service.py](chat_service.py.md) (2 shared connections)
- [test_connection_helpers_impl.py](test_connection_helpers_impl.py.md) (2 shared connections)
- [e2e_reset_players.py](e2e_reset_players.py.md) (2 shared connections)
- [Missing Hourly Clock Chimes](Missing_Hourly_Clock_Chimes.md) (1 shared connections)

## Source Files

- `server/realtime/connection_establishment.py`
- `server/tests/unit/realtime/test_connection_establishment.py`

## Audit Trail

- EXTRACTED: 270 (99%)
- INFERRED: 4 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*