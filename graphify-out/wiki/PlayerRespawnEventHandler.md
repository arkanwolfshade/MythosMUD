# PlayerRespawnEventHandler

> 37 nodes

## Key Concepts

- **Player** (22 connections)
- **._ensure_room_cache_loaded()** (13 connections) — `server/async_persistence.py`
- **.get_player_by_id()** (5 connections) — `server/async_persistence.py`
- **.get_players_batch()** (5 connections) — `server/async_persistence.py`
- **.get_player_by_name()** (4 connections) — `server/async_persistence.py`
- **.get_players_by_user_id()** (4 connections) — `server/async_persistence.py`
- **.get_active_players_by_user_id()** (4 connections) — `server/async_persistence.py`
- **.get_player_by_user_id()** (4 connections) — `server/async_persistence.py`
- **.list_players()** (4 connections) — `server/async_persistence.py`
- **.get_players_in_room()** (4 connections) — `server/async_persistence.py`
- **.apply_lucidity_loss()** (4 connections) — `server/async_persistence.py`
- **.apply_fear()** (4 connections) — `server/async_persistence.py`
- **.apply_corruption()** (4 connections) — `server/async_persistence.py`
- **._load_room_cache_async()** (3 connections) — `server/async_persistence.py`
- **.save_player()** (3 connections) — `server/async_persistence.py`
- **.warmup_room_cache()** (3 connections) — `server/async_persistence.py`
- **.save_players()** (3 connections) — `server/async_persistence.py`
- **.validate_and_fix_player_room()** (3 connections) — `server/async_persistence.py`
- **.gain_experience()** (3 connections) — `server/async_persistence.py`
- **Ensure room cache is loaded (lazy loading with lock).          This method uses** (1 connections) — `server/async_persistence.py`
- **Load rooms from PostgreSQL via RoomCacheLoader.** (1 connections) — `server/async_persistence.py`
- **Get a player by name. Delegates to PlayerRepository.** (1 connections) — `server/async_persistence.py`
- **Get a player by ID. Delegates to PlayerRepository.** (1 connections) — `server/async_persistence.py`
- **Get all players (including deleted) for a user ID. Delegates to PlayerRepository** (1 connections) — `server/async_persistence.py`
- **Get active (non-deleted) players for a user ID. Delegates to PlayerRepository.** (1 connections) — `server/async_persistence.py`
- *... and 12 more nodes in this community*

## Relationships

- [chat nats publisher](chat_nats_publisher.md) (18 shared connections)
- [init](init.md) (5 shared connections)
- [real time](real_time.md) (2 shared connections)
- [get item prototype count()](get_item_prototype_count%28%29.md) (2 shared connections)
- [get app instance()](get_app_instance%28%29.md) (2 shared connections)
- [time commands](time_commands.md) (1 shared connections)
- [Protocol](Protocol.md) (1 shared connections)

## Source Files

- `server/async_persistence.py`

## Audit Trail

- EXTRACTED: 113 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*