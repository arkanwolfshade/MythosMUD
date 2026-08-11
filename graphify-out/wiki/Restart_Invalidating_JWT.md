# Restart Invalidating JWT

> 44 nodes

## Key Concepts

- **PlayerRespawnEventHandler** (33 connections) — `server/realtime/player_event_handlers_respawn.py`
- **RespawnPlayerEventPayload** (13 connections) — `server/realtime/player_event_handlers_respawn.py`
- **UUID** (11 connections)
- **.get_player_data_for_respawn()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.handle_player_respawned()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._fetch_delirium_respawn_player_snapshot()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._resolve_player_data_for_respawn_event()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._build_respawn_player_payload()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.send_respawn_event_with_retry()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._fetch_fallback_player_data_for_respawn()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.handle_player_delirium_respawned()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._build_fallback_respawn_player_payload()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._build_player_respawned_event()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._send_room_occupants_after_respawn()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._enrich_room_data_with_occupant_names()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.get_current_lucidity()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.update_connection_manager_position()** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
- **.get_player_data_for_delirium_respawn()** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._position_from_stats()** (4 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._convert_npc_ids_to_names()** (4 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._get_npc_name_from_lifecycle_manager()** (4 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._merge_player_lists()** (3 connections) — `server/realtime/player_event_handlers_respawn.py`
- **Player** (1 connections)
- **Client-facing player snapshot sent in respawn WebSocket events.** (1 connections) — `server/realtime/player_event_handlers_respawn.py`
- **Handles player respawn events (respawn, delirium respawn).** (1 connections) — `server/realtime/player_event_handlers_respawn.py`
- *... and 19 more nodes in this community*

## Relationships

- [Combat Domain Events](Combat_Domain_Events.md) (10 shared connections)
- [Application Config Settings](Application_Config_Settings.md) (6 shared connections)
- [Investigations Sessions Xx](Investigations_Sessions_Xx.md) (4 shared connections)
- [Archive Bug Fix](Archive_Bug_Fix.md) (3 shared connections)
- [Services Combat Initialization](Services_Combat_Initialization.md) (3 shared connections)
- [Character Creation E2E](Character_Creation_E2E.md) (3 shared connections)
- [NPC Utility Functions](NPC_Utility_Functions.md) (3 shared connections)
- [Pylint Unique Findings](Pylint_Unique_Findings.md) (3 shared connections)
- [Spell Registry Costs](Spell_Registry_Costs.md) (1 shared connections)
- [Enhanced Logging Exceptions](Enhanced_Logging_Exceptions.md) (1 shared connections)

## Source Files

- `server/realtime/player_event_handlers_respawn.py`

## Audit Trail

- EXTRACTED: 191 (97%)
- INFERRED: 6 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*