# Magic Lifespan Initialization

> 17 nodes

## Key Concepts

- **.mark_room_as_explored()** (7 connections) — `server/services/exploration_service.py`
- **UUID** (7 connections)
- **._get_room_uuid_by_stable_id()** (7 connections) — `server/services/exploration_service.py`
- **.is_room_explored()** (6 connections) — `server/services/exploration_service.py`
- **AsyncSession** (5 connections)
- **._mark_explored_in_session()** (5 connections) — `server/services/exploration_service.py`
- **.get_explored_rooms()** (5 connections) — `server/services/exploration_service.py`
- **.__init__()** (4 connections) — `server/services/exploration_service.py`
- **.mark_room_as_explored_sync()** (4 connections) — `server/services/exploration_service.py`
- **Any** (2 connections)
- **Initialize the exploration service.          Args:             database_manager:** (1 connections) — `server/services/exploration_service.py`
- **Mark a room as explored by a player.          This method inserts a record into** (1 connections) — `server/services/exploration_service.py`
- **Get room UUID by stable_id (hierarchical room ID).          Args:             st** (1 connections) — `server/services/exploration_service.py`
- **Mark room as explored using the provided session.          Args:             ses** (1 connections) — `server/services/exploration_service.py`
- **Get list of room IDs that a player has explored.          Args:             play** (1 connections) — `server/services/exploration_service.py`
- **Check if a player has explored a specific room.          Args:             playe** (1 connections) — `server/services/exploration_service.py`
- **Synchronous wrapper for mark_room_as_explored.          This method is designed** (1 connections) — `server/services/exploration_service.py`

## Relationships

- [Container Persistence Ops](Container_Persistence_Ops.md) (8 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (4 shared connections)
- [Spell Registry Costs](Spell_Registry_Costs.md) (1 shared connections)

## Source Files

- `server/services/exploration_service.py`

## Audit Trail

- EXTRACTED: 59 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*