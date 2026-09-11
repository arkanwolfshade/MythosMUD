# InstanceRoomLookup

> 7 nodes

## Key Concepts

- **InstanceRoomLookup** (7 connections) — `server/async_persistence_types.py`
- **.set_instance_manager()** (3 connections) — `server/async_persistence.py`
- **.get_room_by_id()** (2 connections) — `server/async_persistence_types.py`
- **Protocol** (1 connections)
- **Room** (1 connections)
- **Set the instance manager for instanced room lookup (instance-first).** (1 connections) — `server/async_persistence.py`
- **Minimal instance-manager surface used for instanced room lookup.** (1 connections) — `server/async_persistence_types.py`

## Relationships

- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (2 shared connections)
- [RoomService](RoomService.md) (1 shared connections)
- [Room](Room.md) (1 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/async_persistence_types.py`

## Audit Trail

- EXTRACTED: 9 (90%)
- INFERRED: 1 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*