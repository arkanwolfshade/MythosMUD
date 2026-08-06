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

- [invite models rationale](invite_models_rationale.md) (18 shared connections)
- [combat helpers commands](combat_helpers_commands.md) (6 shared connections)
- [tools generate invite](tools_generate_invite.md) (6 shared connections)
- [channel broadcasting realtime](channel_broadcasting_realtime.md) (4 shared connections)
- [npc aggressive mob](npc_aggressive_mob.md) (2 shared connections)
- [schemas intersection schema](schemas_intersection_schema.md) (2 shared connections)
- [schemas unified room](schemas_unified_room.md) (2 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (1 shared connections)
- [persistence heal player()](persistence_heal_player%28%29.md) (1 shared connections)
- [models invite rationale](models_invite_rationale.md) (1 shared connections)
- [schemas calendar schedule](schemas_calendar_schedule.md) (1 shared connections)
- [schemas room schema](schemas_room_schema.md) (1 shared connections)

## Source Files

- `server/tests/unit/realtime/test_connection_establishment.py`

## Audit Trail

- EXTRACTED: 88 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*