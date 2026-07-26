# Player

> 35 nodes · cohesion 0.07

## Key Concepts

- **Player** (22 connections)
- **._ensure_room_cache_loaded()** (13 connections) — `server/async_persistence.py`
- **.get_player_by_id()** (6 connections) — `server/async_persistence.py`
- **.get_players_batch()** (5 connections) — `server/async_persistence.py`
- **.async_damage_player()** (4 connections) — `server/async_persistence.py`
- **.damage_player()** (4 connections) — `server/async_persistence.py`
- **.get_active_players_by_user_id()** (4 connections) — `server/async_persistence.py`
- **.get_player_by_name()** (4 connections) — `server/async_persistence.py`
- **.get_player_by_user_id()** (4 connections) — `server/async_persistence.py`
- **.get_players_by_user_id()** (4 connections) — `server/async_persistence.py`
- **.get_players_in_room()** (4 connections) — `server/async_persistence.py`
- **.list_players()** (4 connections) — `server/async_persistence.py`
- **.gain_experience()** (3 connections) — `server/async_persistence.py`
- **._load_room_cache_async()** (3 connections) — `server/async_persistence.py`
- **.save_player()** (3 connections) — `server/async_persistence.py`
- **.save_players()** (3 connections) — `server/async_persistence.py`
- **.validate_and_fix_player_room()** (3 connections) — `server/async_persistence.py`
- **.warmup_room_cache()** (3 connections) — `server/async_persistence.py`
- **Get a player by name. Delegates to PlayerRepository.** (2 connections) — `server/async_persistence.py`
- **Ensure room cache is loaded (lazy loading with lock).          This method uses** (1 connections) — `server/async_persistence.py`
- **Load rooms from PostgreSQL via RoomCacheLoader.** (1 connections) — `server/async_persistence.py`
- **Get a player by ID. Delegates to PlayerRepository.** (1 connections) — `server/async_persistence.py`
- **Get all players (including deleted) for a user ID. Delegates to PlayerRepository** (1 connections) — `server/async_persistence.py`
- **Get active (non-deleted) players for a user ID. Delegates to PlayerRepository.** (1 connections) — `server/async_persistence.py`
- **Get the first active player by user ID (backward compatibility). Delegates to Pl** (1 connections) — `server/async_persistence.py`
- *... and 10 more nodes in this community*

## Relationships

- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (17 shared connections)
- [UUID](UUID.md) (5 shared connections)
- [DatabaseError](DatabaseError.md) (2 shared connections)
- [.async_heal_player](async_heal_player.md) (2 shared connections)
- [CreateItemInstanceInput](CreateItemInstanceInput.md) (1 shared connections)
- [RoomCacheLoader](RoomCacheLoader.md) (1 shared connections)

## Source Files

- `server/async_persistence.py`

## Audit Trail

- EXTRACTED: 110 (96%)
- INFERRED: 4 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*