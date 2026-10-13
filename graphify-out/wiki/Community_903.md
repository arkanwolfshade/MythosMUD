# Community 903

> 17 nodes

## Key Concepts

- **extract_occupant_names()** (10 connections) — `server/realtime/player_event_handlers_respawn_room.py`
- **player_event_handlers_respawn_types.py** (9 connections) — `server/realtime/player_event_handlers_respawn_types.py`
- **append_unique_valid_occupant()** (4 connections) — `server/realtime/player_event_handlers_respawn_types.py`
- **ensure_respawned_player_in_lists()** (4 connections) — `server/realtime/player_event_handlers_respawn_types.py`
- **is_npc_occupant_row()** (4 connections) — `server/realtime/player_event_handlers_respawn_types.py`
- **occupant_str_field()** (4 connections) — `server/realtime/player_event_handlers_respawn_types.py`
- **RespawnPlayerEventPayload** (3 connections) — `server/realtime/player_event_handlers_respawn_types.py`
- **RespawnPlayerStatsPayload** (3 connections) — `server/realtime/player_event_handlers_respawn_types.py`
- **TypedDict** (2 connections)
- **Extract NPC and player names from room occupants.** (1 connections) — `server/realtime/player_event_handlers_respawn_room.py`
- **Shared TypedDicts and occupant helpers for respawn event handlers.** (1 connections) — `server/realtime/player_event_handlers_respawn_types.py`
- **Nested stats object in WebSocket respawn player payloads.** (1 connections) — `server/realtime/player_event_handlers_respawn_types.py`
- **Client-facing player snapshot sent in respawn WebSocket events.** (1 connections) — `server/realtime/player_event_handlers_respawn_types.py`
- **Return the first string value found for any of the given occupant dict keys.** (1 connections) — `server/realtime/player_event_handlers_respawn_types.py`
- **True when the occupant row should be classified as an NPC.** (1 connections) — `server/realtime/player_event_handlers_respawn_types.py`
- **Append a validated name to primary and occupant lists when not already present.** (1 connections) — `server/realtime/player_event_handlers_respawn_types.py`
- **Ensure the respawned player appears in player and occupant name lists.** (1 connections) — `server/realtime/player_event_handlers_respawn_types.py`

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (7 shared connections)
- [Community 553](Community_553.md) (3 shared connections)
- [Community 164](Community_164.md) (1 shared connections)

## Source Files

- `server/realtime/player_event_handlers_respawn_room.py`
- `server/realtime/player_event_handlers_respawn_types.py`

## Audit Trail

- EXTRACTED: 30 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*