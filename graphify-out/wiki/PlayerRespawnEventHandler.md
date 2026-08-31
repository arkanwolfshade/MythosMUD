# PlayerRespawnEventHandler

> 103 nodes

## Key Concepts

- **PlayerRespawnEventHandler** (55 connections) — `server/realtime/player_event_handlers_respawn.py`
- **test_player_event_handlers_respawn.py** (36 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **asyncio** (22 connections)
- **.handle_player_respawned()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._fetch_delirium_respawn_player_snapshot()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.get_player_data_for_respawn()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._resolve_player_data_for_respawn_event()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._build_respawn_player_payload()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._fetch_fallback_player_data_for_respawn()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.handle_player_delirium_respawned()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.send_respawn_event_with_retry()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **UUID** (7 connections)
- **._build_fallback_respawn_player_payload()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._build_player_respawned_event()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._emit_respawn_room_posture()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._send_room_occupants_after_respawn()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.get_current_lucidity()** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.get_player_data_for_delirium_respawn()** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
- **player_respawn_event_handler()** (5 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **test_send_respawn_event_with_retry_no_connection_manager()** (5 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **._position_from_stats()** (4 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.update_connection_manager_position()** (4 connections) — `server/realtime/player_event_handlers_respawn.py`
- **mock_utils()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **test_get_current_lucidity_found()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- **test_get_current_lucidity_not_found()** (4 connections) — `server/tests/unit/realtime/test_player_event_handlers_respawn.py`
- *... and 78 more nodes in this community*

## Relationships

- [PlayerEnteredRoom](PlayerEnteredRoom.md) (11 shared connections)
- [test_websocket_initial_state.py](test_websocket_initial_state.py.md) (10 shared connections)
- [PlayerEventHandlerUtils](PlayerEventHandlerUtils.md) (7 shared connections)
- [coerce_int](coerce_int.md) (4 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [realtime/conftest.py](realtime-conftest.py.md) (1 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)
- [player_event_handlers_state.py](player_event_handlers_state.py.md) (1 shared connections)
- [ValidationError](ValidationError.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [disconnect_grace_period.py](disconnect_grace_period.py.md) (1 shared connections)

## Source Files

- `server/realtime/player_event_handlers_respawn.py`
- `server/tests/unit/realtime/test_player_event_handlers_respawn.py`

## Audit Trail

- EXTRACTED: 187 (85%)
- INFERRED: 32 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*