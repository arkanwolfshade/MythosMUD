# test_combat_flee_helpers.py

> 66 nodes

## Key Concepts

- **PlayerRespawnEventHandler** (32 connections) — `server/realtime/player_event_handlers_respawn.py`
- **RespawnPlayerEventPayload** (11 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._extract_occupant_names()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._fetch_delirium_respawn_player_snapshot()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.handle_player_respawned()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._resolve_player_data_for_respawn_event()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._fetch_fallback_player_data_for_respawn()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.get_player_data_for_respawn()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._prepare_room_data_for_respawn()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._build_respawn_player_payload()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._enrich_room_data_with_occupant_names()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.send_respawn_event_with_retry()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.validate_name()** (6 connections) — `server/schemas/players/player_requests.py`
- **UUID** (6 connections)
- **._build_fallback_respawn_player_payload()** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._build_player_respawned_event()** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.get_current_lucidity()** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.get_player_data_for_delirium_respawn()** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.handle_player_delirium_respawned()** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._send_room_occupants_after_respawn()** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
- **PlayerRespawnedEvent** (5 connections)
- **_append_unique_valid_occupant()** (4 connections) — `server/realtime/player_event_handlers_respawn.py`
- **_ensure_respawned_player_in_lists()** (4 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._convert_npc_ids_to_names()** (4 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._get_npc_name_from_lifecycle_manager()** (4 connections) — `server/realtime/player_event_handlers_respawn.py`
- *... and 41 more nodes in this community*

## Relationships

- [NPCDefinition](NPCDefinition.md) (9 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (4 shared connections)
- [field_validator](field_validator.md) (3 shared connections)
- [InventoryCommandFactory](InventoryCommandFactory.md) (2 shared connections)
- [PopulationStats](PopulationStats.md) (1 shared connections)
- [CombatAuditLogger](CombatAuditLogger.md) (1 shared connections)
- [CombatEventHandler](CombatEventHandler.md) (1 shared connections)
- [ChatChannelLoggerMixin](ChatChannelLoggerMixin.md) (1 shared connections)
- [dialogue_definitions_api.py](dialogue_definitions_api.py.md) (1 shared connections)

## Source Files

- `server/realtime/player_event_handlers_respawn.py`
- `server/schemas/players/player_requests.py`

## Audit Trail

- EXTRACTED: 122 (94%)
- INFERRED: 8 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*