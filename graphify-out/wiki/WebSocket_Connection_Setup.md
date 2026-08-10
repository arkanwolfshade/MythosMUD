# WebSocket Connection Setup

> 22 nodes

## Key Concepts

- **test_connection_establishment.py** (46 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_establish_websocket_connection_error()** (4 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_remove_dead_connection()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_remove_dead_connection_not_present()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_update_player_connection_list_no_active()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_cleanup_dead_connections_empty_list()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_cleanup_dead_connections_with_dead()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_register_new_connection()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_setup_connection_metadata_no_session_token()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_establish_websocket_connection_success()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **test_establish_websocket_connection_cleans_dead_connections()** (3 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Unit tests for connection establishment.  Tests the connection_establishment mod** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _remove_dead_connection() removes connection from tracking.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _remove_dead_connection() handles connection not present.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _update_player_connection_list() removes player when no active connections.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _cleanup_dead_connections() handles empty list.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _cleanup_dead_connections() cleans up dead connections.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _register_new_connection() registers new connection.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test _setup_connection_metadata() handles None session and token.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test establish_websocket_connection() successfully establishes connection.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test establish_websocket_connection() handles errors.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`
- **Test establish_websocket_connection() cleans up dead connections.** (1 connections) — `server/tests/unit/realtime/test_connection_establishment.py`

## Relationships

- [Logging Structured Setup](Logging_Structured_Setup.md) (18 shared connections)
- [App Game Tick](App_Game_Tick.md) (6 shared connections)
- [Components Ui Designtokens](Components_Ui_Designtokens.md) (5 shared connections)
- [Realtime Connection Impl](Realtime_Connection_Impl.md) (4 shared connections)
- [Services Npc Startup](Services_Npc_Startup.md) (4 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (2 shared connections)
- [test_get_combat_victory_message](test_get_combat_victory_message.md) (1 shared connections)
- [test_is_valid_target_name_valid](test_is_valid_target_name_valid.md) (1 shared connections)
- [test_setup_connection_metadata](test_setup_connection_metadata.md) (1 shared connections)
- [test_track_player_presence_existing_player](test_track_player_presence_existing_player.md) (1 shared connections)
- [test_track_player_presence_new_player](test_track_player_presence_new_player.md) (1 shared connections)
- [test_validate_combat_state_in_combat_required](test_validate_combat_state_in_combat_required.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_connection_establishment.py`

## Audit Trail

- EXTRACTED: 88 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*