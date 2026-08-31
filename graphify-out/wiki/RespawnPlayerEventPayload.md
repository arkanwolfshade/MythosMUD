# RespawnPlayerEventPayload

> 39 nodes

## Key Concepts

- **RespawnPlayerEventPayload** (11 connections) — `server/realtime/player_event_handlers_respawn.py`
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
- **._position_from_stats()** (4 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.update_connection_manager_position()** (4 connections) — `server/realtime/player_event_handlers_respawn.py`
- **RespawnPlayerStatsPayload** (3 connections) — `server/realtime/player_event_handlers_respawn.py`
- **TypedDict** (2 connections)
- **Player** (1 connections)
- **Update connection manager's in-memory position state. As documented in…** (1 connections) — `server/realtime/player_event_handlers_respawn.py`
- **Resolve posture string from player stats JSON.** (1 connections) — `server/realtime/player_event_handlers_respawn.py`
- **Build client-expected player payload for respawn events.** (1 connections) — `server/realtime/player_event_handlers_respawn.py`
- **Get updated player data for respawn event. As documented in "Resurrection and…** (1 connections) — `server/realtime/player_event_handlers_respawn.py`
- *... and 14 more nodes in this community*

## Relationships

- [player_event_handlers.py](player_event_handlers.py.md) (17 shared connections)
- [coerce_int](coerce_int.md) (7 shared connections)
- [test_player_respawn_service.py](test_player_respawn_service.py.md) (6 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [emit_posture_change](emit_posture_change.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/realtime/player_event_handlers_respawn.py`

## Audit Trail

- EXTRACTED: 90 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*