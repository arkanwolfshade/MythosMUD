# test_npc_event_handlers.py

> 112 nodes · cohesion 0.03

## Key Concepts

- **test_player_disconnect_handlers.py** (48 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **player_disconnect_handlers.py** (35 connections) — `server/realtime/player_disconnect_handlers.py`
- **extract_player_name()** (22 connections) — `server/realtime/player_presence_utils.py`
- **_collect_disconnect_keys()** (19 connections) — `server/realtime/player_disconnect_handlers.py`
- **player_presence_utils.py** (18 connections) — `server/realtime/player_presence_utils.py`
- **test_player_presence_utils.py** (18 connections) — `server/tests/unit/realtime/test_player_presence_utils.py`
- **handle_player_disconnect_broadcast()** (17 connections) — `server/realtime/player_disconnect_handlers.py`
- **age_off_disconnected_sessions()** (11 connections) — `server/realtime/player_disconnect_handlers.py`
- **flush_departing_tutorial_instance()** (11 connections) — `server/realtime/player_disconnect_handlers.py`
- **get_player_position()** (10 connections) — `server/realtime/player_presence_utils.py`
- **asyncio** (10 connections)
- **UUID** (8 connections)
- **test_flush_departing_tutorial_instance_flushes_the_players_instance()** (7 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **_is_valid_name()** (6 connections) — `server/realtime/player_presence_utils.py`
- **_FlushOwner** (6 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_flush_departing_tutorial_instance_skips_non_tutorial_players()** (6 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **_release_container_sessions()** (5 connections) — `server/realtime/player_disconnect_handlers.py`
- **_is_uuid_string()** (5 connections) — `server/realtime/player_presence_utils.py`
- **test_cleanup_player_references_releases_open_container_sessions()** (5 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **_get_session_maps_for_age_off()** (4 connections) — `server/realtime/player_disconnect_handlers.py`
- **_purge_expired_sessions_from_maps()** (4 connections) — `server/realtime/player_disconnect_handlers.py`
- **_get_name_from_user()** (4 connections) — `server/realtime/player_presence_utils.py`
- **test_handle_player_disconnect_broadcast_empty_player_name()** (4 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_handle_player_disconnect_broadcast_no_persistence()** (4 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- **test_handle_player_disconnect_broadcast_no_player_name()** (4 connections) — `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- *... and 87 more nodes in this community*

## Relationships

- [player_connection_setup.py](player_connection_setup.py.md) (21 shared connections)
- [setup_jwt_secret](setup_jwt_secret.md) (18 shared connections)
- [test_look_player.py](test_look_player.py.md) (7 shared connections)
- [container_helpers_inventory_ops.py](container_helpers_inventory_ops.py.md) (6 shared connections)
- [Room](Room.md) (5 shared connections)
- [connection_initialization.py](connection_initialization.py.md) (4 shared connections)
- [test_websocket_helpers.py](test_websocket_helpers.py.md) (3 shared connections)
- [LoggingPatternLinter](LoggingPatternLinter.md) (3 shared connections)
- [test_disconnect_catchup.py](test_disconnect_catchup.py.md) (3 shared connections)
- [fixtures/auth.ts](fixtures-auth.ts.md) (3 shared connections)
- [.publish_with_pool](publish_with_pool.md) (2 shared connections)
- [test_active_lucidity_service.py](test_active_lucidity_service.py.md) (2 shared connections)

## Source Files

- `server/realtime/player_disconnect_handlers.py`
- `server/realtime/player_presence_utils.py`
- `server/tests/unit/realtime/test_player_disconnect_handlers.py`
- `server/tests/unit/realtime/test_player_presence_utils.py`

## Audit Trail

- EXTRACTED: 263 (97%)
- INFERRED: 9 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*