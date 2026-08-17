# Player

> 23 nodes

## Key Concepts

- **Player** (19 connections)
- **.apply_corruption()** (3 connections) — `server/async_persistence.py`
- **.apply_fear()** (3 connections) — `server/async_persistence.py`
- **.apply_lucidity_loss()** (3 connections) — `server/async_persistence.py`
- **.async_damage_player()** (3 connections) — `server/async_persistence.py`
- **.async_heal_player()** (3 connections) — `server/async_persistence.py`
- **.damage_player()** (3 connections) — `server/async_persistence.py`
- **.gain_experience()** (3 connections) — `server/async_persistence.py`
- **.heal_player()** (3 connections) — `server/async_persistence.py`
- **.save_player()** (3 connections) — `server/async_persistence.py`
- **.save_players()** (3 connections) — `server/async_persistence.py`
- **.validate_and_fix_player_room()** (3 connections) — `server/async_persistence.py`
- **Save a player. Delegates to PlayerRepository.** (1 connections) — `server/async_persistence.py`
- **Save multiple players in a single transaction. Delegates to PlayerRepository.** (1 connections) — `server/async_persistence.py`
- **Validate and fix player room if needed. Delegates to PlayerRepository.** (1 connections) — `server/async_persistence.py`
- **Apply lucidity loss to a player. Delegates to ExperienceRepository.** (1 connections) — `server/async_persistence.py`
- **Apply fear to a player. Delegates to ExperienceRepository.** (1 connections) — `server/async_persistence.py`
- **Apply corruption to a player. Delegates to ExperienceRepository.** (1 connections) — `server/async_persistence.py`
- **Award experience to a player atomically. Delegates to ExperienceRepository.** (1 connections) — `server/async_persistence.py`
- **Heal a player. Delegates to HealthRepository.** (1 connections) — `server/async_persistence.py`
- **Async alias for heal_player. Delegates to HealthRepository.** (1 connections) — `server/async_persistence.py`
- **Damage a player. Delegates to HealthRepository.** (1 connections) — `server/async_persistence.py`
- **Async alias for damage_player. Delegates to HealthRepository.** (1 connections) — `server/async_persistence.py`

## Relationships

- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (11 shared connections)
- [._ensure_room_cache_loaded](_ensure_room_cache_loaded.md) (8 shared connections)

## Source Files

- `server/async_persistence.py`

## Audit Trail

- EXTRACTED: 41 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*