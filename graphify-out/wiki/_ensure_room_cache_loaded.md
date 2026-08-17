# ._ensure_room_cache_loaded

> 22 nodes

## Key Concepts

- **._ensure_room_cache_loaded()** (12 connections) — `server/async_persistence.py`
- **.get_player_by_id()** (5 connections) — `server/async_persistence.py`
- **.get_players_batch()** (5 connections) — `server/async_persistence.py`
- **.get_active_players_by_user_id()** (4 connections) — `server/async_persistence.py`
- **.get_player_by_name()** (4 connections) — `server/async_persistence.py`
- **.get_player_by_user_id()** (4 connections) — `server/async_persistence.py`
- **.get_players_by_user_id()** (4 connections) — `server/async_persistence.py`
- **.get_players_in_room()** (4 connections) — `server/async_persistence.py`
- **.list_players()** (4 connections) — `server/async_persistence.py`
- **._load_room_cache_async()** (3 connections) — `server/async_persistence.py`
- **.warmup_room_cache()** (3 connections) — `server/async_persistence.py`
- **Ensure room cache is loaded (lazy loading with lock). This method uses a lock…** (1 connections) — `server/async_persistence.py`
- **Load rooms from PostgreSQL via RoomCacheLoader.** (1 connections) — `server/async_persistence.py`
- **Get a player by name. Delegates to PlayerRepository.** (1 connections) — `server/async_persistence.py`
- **Get a player by ID. Delegates to PlayerRepository.** (1 connections) — `server/async_persistence.py`
- **Get all players (including deleted) for a user ID. Delegates to…** (1 connections) — `server/async_persistence.py`
- **Get active (non-deleted) players for a user ID. Delegates to PlayerRepository.** (1 connections) — `server/async_persistence.py`
- **Get the first active player by user ID (backward compatibility). Delegates to…** (1 connections) — `server/async_persistence.py`
- **List all players. Delegates to PlayerRepository.** (1 connections) — `server/async_persistence.py`
- **Warm up the room cache during application startup. This method should be called…** (1 connections) — `server/async_persistence.py`
- **Get all players in a specific room. Delegates to PlayerRepository.** (1 connections) — `server/async_persistence.py`
- **Get multiple players by IDs in a single batch query. This method uses a single…** (1 connections) — `server/async_persistence.py`

## Relationships

- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (11 shared connections)
- [Player](Player.md) (8 shared connections)
- [UUID](UUID.md) (2 shared connections)

## Source Files

- `server/async_persistence.py`

## Audit Trail

- EXTRACTED: 42 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*