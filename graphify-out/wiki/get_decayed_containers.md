# .get_decayed_containers

> 5 nodes

## Key Concepts

- **.get_decayed_containers()** (4 connections) — `server/async_persistence.py`
- **.update_player_last_active()** (4 connections) — `server/async_persistence.py`
- **datetime** (3 connections)
- **Update the last_active timestamp for a player. Delegates to PlayerRepository.** (1 connections) — `server/async_persistence.py`
- **Get decayed containers.** (1 connections) — `server/async_persistence.py`

## Relationships

- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (3 shared connections)
- [Any](Any.md) (1 shared connections)
- [UUID](UUID.md) (1 shared connections)

## Source Files

- `server/async_persistence.py`

## Audit Trail

- EXTRACTED: 9 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*