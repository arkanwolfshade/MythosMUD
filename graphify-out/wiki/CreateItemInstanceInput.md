# CreateItemInstanceInput

> 15 nodes · cohesion 0.13

## Key Concepts

- **CreateItemInstanceInput** (11 connections) — `server/async_persistence_constants.py`
- **datetime** (6 connections)
- **Profession** (5 connections)
- **.get_decayed_containers()** (4 connections) — `server/async_persistence.py`
- **.update_player_last_active()** (4 connections) — `server/async_persistence.py`
- **.create_item_instance()** (3 connections) — `server/async_persistence.py`
- **.get_profession_by_id()** (3 connections) — `server/async_persistence.py`
- **async_persistence_constants.py** (3 connections) — `server/async_persistence_constants.py`
- **TypedDict** (1 connections)
- **Constants and shared types for async persistence layer.  Extracted to keep async** (1 connections) — `server/async_persistence_constants.py`
- **Optional fields for create_item_instance. owner_type, owner_id, etc. with defaul** (1 connections) — `server/async_persistence_constants.py`
- **Update the last_active timestamp for a player. Delegates to PlayerRepository.** (1 connections) — `server/async_persistence.py`
- **Get a profession by ID. Delegates to ProfessionRepository.** (1 connections) — `server/async_persistence.py`
- **Get decayed containers.** (1 connections) — `server/async_persistence.py`
- **Create a new item instance. Delegates to ItemRepository.** (1 connections) — `server/async_persistence.py`

## Relationships

- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (5 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [Any](Any.md) (2 shared connections)
- [UUID](UUID.md) (2 shared connections)
- [RoomCacheLoader](RoomCacheLoader.md) (2 shared connections)
- [DatabaseError](DatabaseError.md) (2 shared connections)
- [Player](Player.md) (1 shared connections)
- [get_async_session](get_async_session.md) (1 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/async_persistence_constants.py`

## Audit Trail

- EXTRACTED: 34 (74%)
- INFERRED: 12 (26%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*