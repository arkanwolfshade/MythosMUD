# ._get_room_uuid_by_stable_id

> 17 nodes

## Key Concepts

- **._get_room_uuid_by_stable_id()** (7 connections) — `server/services/exploration_service.py`
- **.mark_room_as_explored()** (7 connections) — `server/services/exploration_service.py`
- **UUID** (7 connections)
- **.is_room_explored()** (6 connections) — `server/services/exploration_service.py`
- **.get_explored_rooms()** (5 connections) — `server/services/exploration_service.py`
- **._mark_explored_in_session()** (5 connections) — `server/services/exploration_service.py`
- **AsyncSession** (5 connections)
- **.__init__()** (4 connections) — `server/services/exploration_service.py`
- **.mark_room_as_explored_sync()** (4 connections) — `server/services/exploration_service.py`
- **Any** (2 connections)
- **Get room UUID by stable_id (hierarchical room ID). Args: stable_id:…** (1 connections) — `server/services/exploration_service.py`
- **Mark room as explored using the provided session. Args: session: Database…** (1 connections) — `server/services/exploration_service.py`
- **Get list of room IDs that a player has explored. Args: player_id: UUID of the…** (1 connections) — `server/services/exploration_service.py`
- **Check if a player has explored a specific room. Args: player_id: UUID of the…** (1 connections) — `server/services/exploration_service.py`
- **Synchronous wrapper for mark_room_as_explored. This method is designed to be…** (1 connections) — `server/services/exploration_service.py`
- **Initialize the exploration service. Args: database_manager: Database manager…** (1 connections) — `server/services/exploration_service.py`
- **Mark a room as explored by a player. This method inserts a record into the…** (1 connections) — `server/services/exploration_service.py`

## Relationships

- [ExplorationService](ExplorationService.md) (7 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [.get_instance](get_instance.md) (1 shared connections)

## Source Files

- `server/services/exploration_service.py`

## Audit Trail

- EXTRACTED: 36 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*