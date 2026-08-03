# connection establishment realtime

> 22 nodes

## Key Concepts

- **test_connection_establishment.py** (47 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_register_new_connection()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_connection_metadata()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_session_tracking_no_session_id()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_player_and_room_success()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_player_and_room_no_room_id()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_track_player_presence_existing_player()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_cleanup_failed_connection_none()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_cleanup_failed_connection_success()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_establish_websocket_connection_success()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_establish_websocket_connection_cleans_dead_connections()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Unit tests for connection establishment.  Tests the connection_establishment mod** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _register_new_connection() registers new connection.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _setup_connection_metadata() creates metadata.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _setup_session_tracking() handles None session_id.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _setup_player_and_room() successfully sets up player and room.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _setup_player_and_room() handles player with no room_id.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _track_player_presence() broadcasts for existing player.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _cleanup_failed_connection() handles None connection_id.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _cleanup_failed_connection() cleans up connection.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test establish_websocket_connection() successfully establishes connection.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test establish_websocket_connection() cleans up dead connections.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`

## Relationships

- [player event state](player_event_state.md) (18 shared connections)
- [useDraggablePanelInteractions draggableP](useDraggablePanelInteractions_draggableP.md) (6 shared connections)
- [cleanup combat handler](cleanup_combat_handler.md) (6 shared connections)
- [persistence rationale room](persistence_rationale_room.md) (4 shared connections)
- [event bus events](event_bus_events.md) (4 shared connections)
- [room game service](room_game_service.md) (3 shared connections)
- [chat game service](chat_game_service.md) (2 shared connections)
- [npc populate databases](npc_populate_databases.md) (1 shared connections)
- [game room service](game_room_service.md) (1 shared connections)
- [events event bus](events_event_bus.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_connection_establishment.py`

## Audit Trail

- EXTRACTED: 88 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*