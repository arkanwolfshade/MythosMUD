# NATS Messaging

> 65 nodes

## Key Concepts

- **PlayerRespawnEventHandler** (33 connections) — `server/realtime/player_event_handlers_respawn.py`
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
- **.__init__()** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.update_connection_manager_position()** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._room_data_from_persistence_room()** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.get_player_data_for_delirium_respawn()** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._position_from_stats()** (4 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._convert_npc_ids_to_names()** (4 connections) — `server/realtime/player_event_handlers_respawn.py`
- *... and 40 more nodes in this community*

## Relationships

- [player room realtime](player_room_realtime.md) (13 shared connections)
- [profession models rationale](profession_models_rationale.md) (13 shared connections)
- [Room Broadcast](Room_Broadcast.md) (4 shared connections)
- [useWebSocketConnectionTestFixtures useWe](useWebSocketConnectionTestFixtures_useWe.md) (3 shared connections)
- [combat services messaging](combat_services_messaging.md) (3 shared connections)
- [realtime websocket initial](realtime_websocket_initial.md) (3 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (1 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (1 shared connections)

## Source Files

- `server/realtime/player_event_handlers_respawn.py`

## Audit Trail

- EXTRACTED: 244 (96%)
- INFERRED: 9 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*