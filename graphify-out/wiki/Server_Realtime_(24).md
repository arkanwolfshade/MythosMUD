# Server Realtime (24)

> 66 nodes

## Key Concepts

- **player_event_handlers_respawn.py** (33 connections) — `server/realtime/player_event_handlers_respawn.py`
- **PlayerRespawnEventHandler** (33 connections) — `server/realtime/player_event_handlers_respawn.py`
- **PlayerRespawnedEvent** (19 connections) — `server/events/event_types.py`
- **RespawnPlayerEventPayload** (13 connections) — `server/realtime/player_event_handlers_respawn.py`
- **UUID** (11 connections)
- **.get_player_data_for_respawn()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.handle_player_respawned()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._extract_occupant_names()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._fetch_delirium_respawn_player_snapshot()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._resolve_player_data_for_respawn_event()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._build_respawn_player_payload()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.send_respawn_event_with_retry()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._fetch_fallback_player_data_for_respawn()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._prepare_room_data_for_respawn()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.handle_player_delirium_respawned()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._build_fallback_respawn_player_payload()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._build_player_respawned_event()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._send_room_occupants_after_respawn()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._enrich_room_data_with_occupant_names()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.get_current_lucidity()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **RespawnPlayerStatsPayload** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.update_connection_manager_position()** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._room_data_from_persistence_room()** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.get_player_data_for_delirium_respawn()** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._position_from_stats()** (4 connections) — `server/realtime/player_event_handlers_respawn.py`
- *... and 41 more nodes in this community*

## Relationships

- [Server Services](Server_Services.md) (14 shared connections)
- [Server Events](Server_Events.md) (13 shared connections)
- [Server Realtime (6)](Server_Realtime_%286%29.md) (7 shared connections)
- [Server Realtime (35)](Server_Realtime_%2835%29.md) (7 shared connections)
- [Server Realtime (4)](Server_Realtime_%284%29.md) (4 shared connections)
- [Server Realtime (2)](Server_Realtime_%282%29.md) (4 shared connections)
- [Server Realtime (32)](Server_Realtime_%2832%29.md) (4 shared connections)
- [Server Admin](Server_Admin.md) (3 shared connections)
- [Server Realtime (9)](Server_Realtime_%289%29.md) (2 shared connections)
- [Server Infrastructure (4)](Server_Infrastructure_%284%29.md) (1 shared connections)
- [Server Models (23)](Server_Models_%2823%29.md) (1 shared connections)
- [Server Realtime (7)](Server_Realtime_%287%29.md) (1 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/realtime/player_event_handlers_respawn.py`

## Audit Trail

- EXTRACTED: 288 (96%)
- INFERRED: 12 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*