# server models room py any

> 15 nodes

## Key Concepts

- **.to_dict()** (8 connections) — `server/models/room.py`
- **.get_containers()** (4 connections) — `server/models/room.py`
- **.get_npcs()** (4 connections) — `server/models/room.py`
- **.get_occupant_count()** (4 connections) — `server/models/room.py`
- **.get_players()** (4 connections) — `server/models/room.py`
- **.get_objects()** (3 connections) — `server/models/room.py`
- **.is_empty()** (3 connections) — `server/models/room.py`
- **Any** (3 connections)
- **Get list of player IDs currently in the room. Returns: List of player IDs in…** (1 connections) — `server/models/room.py`
- **Get list of object IDs currently in the room. Returns: List of object IDs in…** (1 connections) — `server/models/room.py`
- **Get list of NPC IDs currently in the room. Returns: List of NPC IDs in the room** (1 connections) — `server/models/room.py`
- **Get the total number of occupants in the room. Returns: Total count of players,…** (1 connections) — `server/models/room.py`
- **Check if the room has no occupants. Returns: True if the room is empty, False…** (1 connections) — `server/models/room.py`
- **Get list of containers in this room. Returns: List of container data…** (1 connections) — `server/models/room.py`
- **Convert the room to a dictionary representation. Returns: Dictionary containing…** (1 connections) — `server/models/room.py`

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (8 shared connections)
- [server schemas shared target metadata](server_schemas_shared_target_metadata.md) (1 shared connections)
- [server npc aggressive mob npc](server_npc_aggressive_mob_npc.md) (1 shared connections)

## Source Files

- `server/models/room.py`

## Audit Trail

- EXTRACTED: 23 (92%)
- INFERRED: 2 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*