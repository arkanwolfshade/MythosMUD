# append unique valid occupant()

> 13 nodes

## Key Concepts

- **._extract_occupant_names()** (9 connections) — `server/realtime/player_event_handlers_respawn.py`
- **._room_data_from_persistence_room()** (5 connections) — `server/realtime/player_event_handlers_respawn.py`
- **_occupant_str_field()** (3 connections) — `server/realtime/player_event_handlers_respawn.py`
- **_is_npc_occupant_row()** (3 connections) — `server/realtime/player_event_handlers_respawn.py`
- **_append_unique_valid_occupant()** (3 connections) — `server/realtime/player_event_handlers_respawn.py`
- **_ensure_respawned_player_in_lists()** (3 connections) — `server/realtime/player_event_handlers_respawn.py`
- **Room** (1 connections)
- **Return the first string value found for any of the given occupant dict keys.** (1 connections) — `server/realtime/player_event_handlers_respawn.py`
- **True when the occupant row should be classified as an NPC.** (1 connections) — `server/realtime/player_event_handlers_respawn.py`
- **Append a validated name to primary and occupant lists when not already present.** (1 connections) — `server/realtime/player_event_handlers_respawn.py`
- **Ensure the respawned player appears in player and occupant name lists.** (1 connections) — `server/realtime/player_event_handlers_respawn.py`
- **Build room payload from persistence when no live connection manager is available** (1 connections) — `server/realtime/player_event_handlers_respawn.py`
- **Extract NPC and player names from room occupants.          Args:             roo** (1 connections) — `server/realtime/player_event_handlers_respawn.py`

## Relationships

- [. init ()](_init_%28%29.md) (4 shared connections)
- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (4 shared connections)
- [.model dump()](model_dump%28%29.md) (1 shared connections)

## Source Files

- `server/realtime/player_event_handlers_respawn.py`

## Audit Trail

- EXTRACTED: 32 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*