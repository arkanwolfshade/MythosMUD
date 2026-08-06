# coercion int inventory

> 15 nodes

## Key Concepts

- **.to_dict()** (8 connections) — `server/models/room.py`
- **.__init__()** (5 connections) — `server/models/room.py`
- **.get_containers()** (5 connections) — `server/models/room.py`
- **.get_npcs()** (4 connections) — `server/models/room.py`
- **.get_occupant_count()** (4 connections) — `server/models/room.py`
- **Any** (3 connections)
- **.get_objects()** (3 connections) — `server/models/room.py`
- **.is_empty()** (3 connections) — `server/models/room.py`
- **Initialize a Room from JSON data.          Args:             room_data: Dictiona** (1 connections) — `server/models/room.py`
- **Get list of object IDs currently in the room.          Returns:             List** (1 connections) — `server/models/room.py`
- **Get list of NPC IDs currently in the room.          Returns:             List of** (1 connections) — `server/models/room.py`
- **Get the total number of occupants in the room.          Returns:             Tot** (1 connections) — `server/models/room.py`
- **Check if the room has no occupants.          Returns:             True if the ro** (1 connections) — `server/models/room.py`
- **Get list of containers in this room.          Returns:             List of conta** (1 connections) — `server/models/room.py`
- **Convert the room to a dictionary representation.          Returns:             D** (1 connections) — `server/models/room.py`

## Relationships

- [room models instance](room_models_instance.md) (7 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (1 shared connections)
- [NPC Services Bootstrap](NPC_Services_Bootstrap.md) (1 shared connections)
- [game rationale schemas](game_rationale_schemas.md) (1 shared connections)
- [game magic regeneration](game_magic_regeneration.md) (1 shared connections)

## Source Files

- `server/models/room.py`

## Audit Trail

- EXTRACTED: 40 (95%)
- INFERRED: 2 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*