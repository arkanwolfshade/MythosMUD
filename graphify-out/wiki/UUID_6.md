# UUID

> 21 nodes

## Key Concepts

- **UUID** (15 connections)
- **.add_player_effect()** (4 connections) — `server/async_persistence.py`
- **.get_active_player_effects()** (4 connections) — `server/async_persistence.py`
- **.get_container()** (4 connections) — `server/async_persistence.py`
- **.get_containers_by_entity_id()** (4 connections) — `server/async_persistence.py`
- **.delete_player()** (3 connections) — `server/async_persistence.py`
- **.get_player_effect_remaining_ticks()** (3 connections) — `server/async_persistence.py`
- **.has_player_effect()** (3 connections) — `server/async_persistence.py`
- **.remove_player_effect_by_id()** (3 connections) — `server/async_persistence.py`
- **.soft_delete_player()** (3 connections) — `server/async_persistence.py`
- **.update_container()** (3 connections) — `server/async_persistence.py`
- **.delete_container()** (2 connections) — `server/async_persistence.py`
- **Soft delete a player (sets is_deleted=True). Delegates to PlayerRepository.** (1 connections) — `server/async_persistence.py`
- **Delete a player. Delegates to PlayerRepository.** (1 connections) — `server/async_persistence.py`
- **Add a player effect. Returns effect id.** (1 connections) — `server/async_persistence.py`
- **Remove a player effect by id.** (1 connections) — `server/async_persistence.py`
- **Get active effects for a player (remaining_ticks > 0). Returns list of…** (1 connections) — `server/async_persistence.py`
- **Return True if player has an active effect of the given type.** (1 connections) — `server/async_persistence.py`
- **Return remaining ticks for the effect, or None.** (1 connections) — `server/async_persistence.py`
- **Get a container by ID.** (1 connections) — `server/async_persistence.py`
- **Get all containers owned by an entity.** (1 connections) — `server/async_persistence.py`

## Relationships

- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (12 shared connections)
- [Any](Any.md) (5 shared connections)
- [._ensure_room_cache_loaded](_ensure_room_cache_loaded.md) (2 shared connections)
- [.get_decayed_containers](get_decayed_containers.md) (1 shared connections)

## Source Files

- `server/async_persistence.py`

## Audit Trail

- EXTRACTED: 40 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*