# Player

> 47 nodes

## Key Concepts

- **Player** (20 connections)
- **._ensure_room_cache_loaded()** (12 connections) — `server/async_persistence.py`
- **.get_player_by_id()** (5 connections) — `server/async_persistence.py`
- **.get_players_batch()** (5 connections) — `server/async_persistence.py`
- **.get_active_players_by_user_id()** (4 connections) — `server/async_persistence.py`
- **.get_player_by_name()** (4 connections) — `server/async_persistence.py`
- **.get_player_by_user_id()** (4 connections) — `server/async_persistence.py`
- **.get_players_by_user_id()** (4 connections) — `server/async_persistence.py`
- **.get_players_in_room()** (4 connections) — `server/async_persistence.py`
- **.list_players()** (4 connections) — `server/async_persistence.py`
- **.apply_corruption()** (3 connections) — `server/async_persistence.py`
- **.apply_fear()** (3 connections) — `server/async_persistence.py`
- **.apply_lucidity_loss()** (3 connections) — `server/async_persistence.py`
- **.async_damage_player()** (3 connections) — `server/async_persistence.py`
- **.async_heal_player()** (3 connections) — `server/async_persistence.py`
- **.damage_player()** (3 connections) — `server/async_persistence.py`
- **.gain_experience()** (3 connections) — `server/async_persistence.py`
- **.gain_occult_knowledge()** (3 connections) — `server/async_persistence.py`
- **.heal_player()** (3 connections) — `server/async_persistence.py`
- **._load_room_cache_async()** (3 connections) — `server/async_persistence.py`
- **.save_player()** (3 connections) — `server/async_persistence.py`
- **.save_players()** (3 connections) — `server/async_persistence.py`
- **.validate_and_fix_player_room()** (3 connections) — `server/async_persistence.py`
- **.warmup_room_cache()** (3 connections) — `server/async_persistence.py`
- **Ensure room cache is loaded (lazy loading with lock). This method uses a lock…** (1 connections) — `server/async_persistence.py`
- *... and 22 more nodes in this community*

## Relationships

- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (25 shared connections)

## Source Files

- `server/async_persistence.py`

## Audit Trail

- EXTRACTED: 78 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*