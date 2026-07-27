# Respawn Occupant Enrichment

> 27 nodes · cohesion 0.08

## Key Concepts

- **._extract_occupant_names()** (8 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._prepare_room_data_for_respawn()** (7 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._enrich_room_data_with_occupant_names()** (6 connections) — `server/realtime/player_event_handlers_respawn.py`
- **get_npc_lifecycle_manager_from_connection_manager()** (6 connections) — `server/realtime/websocket_initial_state.py`
- **_NpcLifecycleManagerForOccupants** (6 connections) — `server/realtime/websocket_initial_state.py`
- **._room_data_from_persistence_room()** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._convert_npc_ids_to_names()** (4 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._get_npc_name_from_lifecycle_manager()** (4 connections) — `server/realtime/player_event_handlers_respawn.py`
- **_append_unique_valid_occupant()** (3 connections) — `server/realtime/player_event_handlers_respawn.py`
- **_ensure_respawned_player_in_lists()** (3 connections) — `server/realtime/player_event_handlers_respawn.py`
- **_is_npc_occupant_row()** (3 connections) — `server/realtime/player_event_handlers_respawn.py`
- **_occupant_str_field()** (3 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._merge_player_lists()** (3 connections) — `server/realtime/player_event_handlers_respawn.py`
- **Room** (3 connections) — `server/realtime/player_event_handlers_respawn.py`
- **Prepare room data with NPC and player names for a respawn event.** (1 connections) — `server/realtime/player_event_handlers_respawn.py`
- **Build room payload from persistence when no live connection manager is available** (1 connections) — `server/realtime/player_event_handlers_respawn.py`
- **Merge live occupants into room_data and return name lists for the respawn payloa** (1 connections) — `server/realtime/player_event_handlers_respawn.py`
- **Extract NPC and player names from room occupants.          Args:             roo** (1 connections) — `server/realtime/player_event_handlers_respawn.py`
- **Convert NPC IDs to names if they're still UUIDs.          Args:             exis** (1 connections) — `server/realtime/player_event_handlers_respawn.py`
- **Return the first string value found for any of the given occupant dict keys.** (1 connections) — `server/realtime/player_event_handlers_respawn.py`
- **Get NPC name from lifecycle manager.          Args:             npc_id: NPC ID t** (1 connections) — `server/realtime/player_event_handlers_respawn.py`
- **Merge existing player list with extracted player names.          Args:** (1 connections) — `server/realtime/player_event_handlers_respawn.py`
- **True when the occupant row should be classified as an NPC.** (1 connections) — `server/realtime/player_event_handlers_respawn.py`
- **Append a validated name to primary and occupant lists when not already present.** (1 connections) — `server/realtime/player_event_handlers_respawn.py`
- **Ensure the respawned player appears in player and occupant name lists.** (1 connections) — `server/realtime/player_event_handlers_respawn.py`
- *... and 2 more nodes in this community*

## Relationships

- [[Player Respawn Events]] (14 shared connections)
- [[WebSocket Initial State]] (4 shared connections)
- [[Room Occupant Events]] (2 shared connections)
- [[Realtime WebSocket Auth]] (1 shared connections)
- [[Player Combat XP]] (1 shared connections)
- [[Realtime Event Delegation]] (1 shared connections)

## Source Files

- `server/realtime/player_event_handlers_respawn.py`
- `server/realtime/websocket_initial_state.py`

## Audit Trail

- EXTRACTED: 73 (95%)
- INFERRED: 4 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
