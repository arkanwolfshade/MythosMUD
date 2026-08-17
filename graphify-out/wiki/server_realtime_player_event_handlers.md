# server realtime player event handlers

> 62 nodes

## Key Concepts

- **PlayerRespawnEventHandler** (30 connections) — `server/realtime/player_event_handlers_respawn.py`
- **RespawnPlayerEventPayload** (11 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._extract_occupant_names()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._fetch_delirium_respawn_player_snapshot()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.get_player_data_for_respawn()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.handle_player_respawned()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._resolve_player_data_for_respawn_event()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._build_respawn_player_payload()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._fetch_fallback_player_data_for_respawn()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._prepare_room_data_for_respawn()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.send_respawn_event_with_retry()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._build_fallback_respawn_player_payload()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._build_player_respawned_event()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._enrich_room_data_with_occupant_names()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.handle_player_delirium_respawned()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._send_room_occupants_after_respawn()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **UUID** (6 connections)
- **.get_current_lucidity()** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.get_player_data_for_delirium_respawn()** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._room_data_from_persistence_room()** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._convert_npc_ids_to_names()** (4 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._get_npc_name_from_lifecycle_manager()** (4 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._position_from_stats()** (4 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.update_connection_manager_position()** (4 connections) — `server/realtime/player_event_handlers_respawn.py`
- **RespawnPlayerStatsPayload** (3 connections) — `server/realtime/player_event_handlers_respawn.py`
- *... and 37 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (9 shared connections)
- [baseevent](baseevent.md) (6 shared connections)
- [server commands inventory command coercion](server_commands_inventory_command_coercion.md) (4 shared connections)
- [server tests unit realtime test](server_tests_unit_realtime_test.md) (3 shared connections)
- [server realtime envelope build event](server_realtime_envelope_build_event.md) (3 shared connections)
- [server realtime player event handlers](server_realtime_player_event_handlers.md) (2 shared connections)
- [room](room.md) (2 shared connections)
- [playercombatservice](playercombatservice.md) (1 shared connections)
- [server realtime websocket handler](server_realtime_websocket_handler.md) (1 shared connections)
- [scripts add flavor text column](scripts_add_flavor_text_column.md) (1 shared connections)

## Source Files

- `server/realtime/player_event_handlers_respawn.py`

## Audit Trail

- EXTRACTED: 125 (96%)
- INFERRED: 5 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*