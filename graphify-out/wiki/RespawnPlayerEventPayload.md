# RespawnPlayerEventPayload

> 34 nodes

## Key Concepts

- **RespawnPlayerEventPayload** (13 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._fetch_delirium_respawn_player_snapshot()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.get_player_data_for_respawn()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.handle_player_respawned()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._resolve_player_data_for_respawn_event()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._build_respawn_player_payload()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._fetch_fallback_player_data_for_respawn()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.send_respawn_event_with_retry()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._build_fallback_respawn_player_payload()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._build_player_respawned_event()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.handle_player_delirium_respawned()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._send_room_occupants_after_respawn()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **UUID** (6 connections)
- **.get_current_lucidity()** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.get_player_data_for_delirium_respawn()** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._position_from_stats()** (4 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.update_connection_manager_position()** (4 connections) — `server/realtime/player_event_handlers_respawn.py`
- **Player** (1 connections)
- **Update connection manager's in-memory position state. As documented in…** (1 connections) — `server/realtime/player_event_handlers_respawn.py`
- **Resolve posture string from player stats JSON.** (1 connections) — `server/realtime/player_event_handlers_respawn.py`
- **Build client-expected player payload for respawn events.** (1 connections) — `server/realtime/player_event_handlers_respawn.py`
- **Get updated player data for respawn event. As documented in "Resurrection and…** (1 connections) — `server/realtime/player_event_handlers_respawn.py`
- **Send respawn event with retry logic to handle temporary connection…** (1 connections) — `server/realtime/player_event_handlers_respawn.py`
- **Build respawn player payload from connection-manager player when persistence…** (1 connections) — `server/realtime/player_event_handlers_respawn.py`
- **Try connection-manager player lookup when persistence-based respawn data is…** (1 connections) — `server/realtime/player_event_handlers_respawn.py`
- *... and 9 more nodes in this community*

## Relationships

- [RealTimeEventHandler](RealTimeEventHandler.md) (20 shared connections)
- [event_types.py](event_types.py.md) (6 shared connections)
- [Player](Player.md) (4 shared connections)
- [build_event](build_event.md) (3 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [get_async_session](get_async_session.md) (1 shared connections)

## Source Files

- `server/realtime/player_event_handlers_respawn.py`

## Audit Trail

- EXTRACTED: 81 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*