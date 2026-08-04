# logging examples fastapi

> 22 nodes

## Key Concepts

- **.create_instance()** (7 connections) — `server/game/instance_manager.py`
- **._build_instance_rooms()** (6 connections) — `server/game/instance_manager.py`
- **.__init__()** (5 connections) — `server/game/instance_manager.py`
- **Room** (5 connections)
- **._stable_id_from_room()** (5 connections) — `server/game/instance_manager.py`
- **Instance** (4 connections) — `server/game/instance_manager.py`
- **._get_template_rooms()** (4 connections) — `server/game/instance_manager.py`
- **._remap_exits()** (4 connections) — `server/game/instance_manager.py`
- **._stable_id_from_target()** (3 connections) — `server/game/instance_manager.py`
- **.get_instance()** (3 connections) — `server/game/instance_manager.py`
- **.get_room_by_id()** (3 connections) — `server/game/instance_manager.py`
- **UUID** (2 connections)
- **An instanced set of rooms, unique per player or group.** (1 connections) — `server/game/instance_manager.py`
- **Initialize the instance manager.          Args:             room_cache: Shared r** (1 connections) — `server/game/instance_manager.py`
- **Create an instance from room templates with the given template_id.          Args** (1 connections) — `server/game/instance_manager.py`
- **Return template rooms matching instance_template_id.** (1 connections) — `server/game/instance_manager.py`
- **Clone template rooms into instance-scoped rooms with remapped exits.** (1 connections) — `server/game/instance_manager.py`
- **Extract stable_id from room - use room.id if it looks like a full path.** (1 connections) — `server/game/instance_manager.py`
- **Remap exit targets: same-instance rooms use instance IDs, outside exits use fixe** (1 connections) — `server/game/instance_manager.py`
- **Extract stable_id from a room ID (may be full path or short form).** (1 connections) — `server/game/instance_manager.py`
- **Return the instance if it exists.** (1 connections) — `server/game/instance_manager.py`
- **Look up a room by ID, checking instances first.          Used by persistence lay** (1 connections) — `server/game/instance_manager.py`

## Relationships

- [websocket realtime handler](websocket_realtime_handler.md) (9 shared connections)
- [room models instance](room_models_instance.md) (2 shared connections)
- [Error Conversion](Error_Conversion.md) (1 shared connections)
- [NPC Combat](NPC_Combat.md) (1 shared connections)

## Source Files

- `server/game/instance_manager.py`

## Audit Trail

- EXTRACTED: 61 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*