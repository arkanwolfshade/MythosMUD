# Player Respawn Events

> 36 nodes · cohesion 0.09

## Key Concepts

- **RespawnPlayerEventPayload** (13 connections) — `server/realtime/player_event_handlers_respawn.py`
- **UUID** (13 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._fetch_delirium_respawn_player_snapshot()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.get_player_data_for_respawn()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.handle_player_respawned()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._resolve_player_data_for_respawn_event()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._build_respawn_player_payload()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._fetch_fallback_player_data_for_respawn()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.handle_player_delirium_respawned()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.send_respawn_event_with_retry()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **PlayerRespawnedEvent** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._build_fallback_respawn_player_payload()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._build_player_respawned_event()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._send_room_occupants_after_respawn()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.get_current_lucidity()** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.get_player_data_for_delirium_respawn()** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.update_connection_manager_position()** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._position_from_stats()** (4 connections) — `server/realtime/player_event_handlers_respawn.py`
- **Player** (3 connections) — `server/realtime/player_event_handlers_respawn.py`
- **PlayerDeliriumRespawnedEvent** (3 connections) — `server/realtime/player_event_handlers_respawn.py`
- **Update connection manager's in-memory position state.          As documented in** (1 connections) — `server/realtime/player_event_handlers_respawn.py`
- **Resolve posture string from player stats JSON.** (1 connections) — `server/realtime/player_event_handlers_respawn.py`
- **Build client-expected player payload for respawn events.** (1 connections) — `server/realtime/player_event_handlers_respawn.py`
- **Get updated player data for respawn event.          As documented in "Resurrecti** (1 connections) — `server/realtime/player_event_handlers_respawn.py`
- **Send respawn event with retry logic to handle temporary connection unavailabilit** (1 connections) — `server/realtime/player_event_handlers_respawn.py`
- *... and 11 more nodes in this community*

## Relationships

- [[Player Respawn Events]] (22 shared connections)
- [[Room Occupant Events]] (5 shared connections)
- [[Integer Coercion Utils]] (4 shared connections)
- [[Combat Player Broadcasts]] (3 shared connections)
- [[NPC Admin API]] (1 shared connections)
- [[Respawn Occupant Enrichment]] (1 shared connections)
- [[Dependency Risk Analyzer]] (1 shared connections)

## Source Files

- `server/realtime/player_event_handlers_respawn.py`

## Audit Trail

- EXTRACTED: 145 (94%)
- INFERRED: 10 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
