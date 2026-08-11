# WebSocket Connection Setup

> 30 nodes

## Key Concepts

- **test_connection_establishment.py** (46 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_establish_websocket_connection_error()** (4 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_find_dead_connections_all_active()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_find_dead_connections_not_in_active()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_find_dead_connections_not_connected()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_connection_metadata()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_session_tracking_new_session()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_player_and_room_success()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_player_and_room_no_room_id()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_track_player_presence_new_player()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_track_player_presence_existing_player()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_cleanup_failed_connection_none()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_cleanup_failed_connection_error()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_establish_websocket_connection_success()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_establish_websocket_connection_cleans_dead_connections()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Unit tests for connection establishment.  Tests the connection_establishment mod** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _find_dead_connections() returns empty list when all connections are active** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _find_dead_connections() skips connections not in active_websockets.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _find_dead_connections() finds dead connections.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _setup_connection_metadata() creates metadata.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _setup_session_tracking() creates new session entry.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _setup_player_and_room() successfully sets up player and room.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _setup_player_and_room() handles player with no room_id.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _track_player_presence() tracks new player.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _track_player_presence() broadcasts for existing player.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- *... and 5 more nodes in this community*

## Relationships

- [Architecture Review Plan](Architecture_Review_Plan.md) (22 shared connections)
- [Archive Npc Population](Archive_Npc_Population.md) (6 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (4 shared connections)
- [Archive Optimization Summary](Archive_Optimization_Summary.md) (3 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (2 shared connections)
- [Cursor Plans First](Cursor_Plans_First.md) (1 shared connections)
- [Cursor Plans Generate](Cursor_Plans_Generate.md) (1 shared connections)
- [Persistence Item Repositories](Persistence_Item_Repositories.md) (1 shared connections)
- [Realtime Payload Optimizer](Realtime_Payload_Optimizer.md) (1 shared connections)
- [Components Map Roommapeditor](Components_Map_Roommapeditor.md) (1 shared connections)
- [Cursor Plans Eliminate](Cursor_Plans_Eliminate.md) (1 shared connections)
- [Cursor Plans Disconnect](Cursor_Plans_Disconnect.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_connection_establishment.py`

## Audit Trail

- EXTRACTED: 104 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*