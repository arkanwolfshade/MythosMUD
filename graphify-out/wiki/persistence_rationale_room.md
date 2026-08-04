# persistence rationale room

> 102 nodes

## Key Concepts

- **test_connection_disconnection.py** (37 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **connection_disconnection.py** (31 connections) — `server/realtime/connection_disconnection.py`
- **ConnectionMetadata** (21 connections) — `server/realtime/connection_models.py`
- **_DisconnectConnectionManager** (19 connections) — `server/realtime/connection_disconnection.py`
- **_track_disconnect_if_needed()** (15 connections) — `server/realtime/connection_disconnection.py`
- **_cleanup_room_subscriptions()** (15 connections) — `server/realtime/connection_disconnection.py`
- **cleanup_websocket_disconnect()** (15 connections) — `server/realtime/connection_disconnection.py`
- **disconnect_all_websockets_impl()** (13 connections) — `server/realtime/connection_disconnection.py`
- **disconnect_connection_by_id_impl()** (13 connections) — `server/realtime/connection_disconnection.py`
- **_cleanup_player_data()** (12 connections) — `server/realtime/connection_disconnection.py`
- **force_disconnect_player_impl()** (12 connections) — `server/realtime/connection_manager_methods.py`
- **UUID** (11 connections)
- **safe_close_websocket_impl()** (10 connections) — `server/realtime/connection_manager_methods.py`
- **test_connection_models.py** (9 connections) — `server/tests/unit/realtime/test_connection_models.py`
- **_cleanup_fully_disconnected_player()** (8 connections) — `server/realtime/connection_disconnection.py`
- **.has_websocket_connection()** (7 connections) — `server/realtime/connection_disconnection.py`
- **_disconnect_single_websocket()** (7 connections) — `server/realtime/connection_disconnection.py`
- **_is_non_intentional_force_disconnect()** (6 connections) — `server/realtime/connection_disconnection.py`
- **_disconnect_websocket_by_connection_id()** (6 connections) — `server/realtime/connection_disconnection.py`
- **_cleanup_connection_tracking()** (4 connections) — `server/realtime/connection_disconnection.py`
- **test_cleanup_player_data_has_connection()** (4 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **.disconnect_connection_by_id()** (3 connections) — `server/realtime/connection_manager.py`
- **test_track_disconnect_if_needed_new()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_track_disconnect_if_needed_already_processed()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- **test_track_disconnect_if_needed_force_disconnect()** (3 connections) — `server/tests/unit/realtime/test_connection_disconnection.py`
- *... and 77 more nodes in this community*

## Relationships

- [taunt combat commands](taunt_combat_commands.md) (27 shared connections)
- [Room Broadcast](Room_Broadcast.md) (24 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (4 shared connections)
- [connection disconnection realtime](connection_disconnection_realtime.md) (4 shared connections)
- [connection realtime delegates](connection_realtime_delegates.md) (3 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [connection establishment realtime](connection_establishment_realtime.md) (2 shared connections)
- [Loot Generation](Loot_Generation.md) (1 shared connections)

## Source Files

- `server/realtime/connection_disconnection.py`
- `server/realtime/connection_manager.py`
- `server/realtime/connection_manager_methods.py`
- `server/realtime/connection_models.py`
- `server/tests/unit/realtime/test_connection_disconnection.py`
- `server/tests/unit/realtime/test_connection_disconnection_websockets.py`
- `server/tests/unit/realtime/test_connection_models.py`

## Audit Trail

- EXTRACTED: 399 (97%)
- INFERRED: 14 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*