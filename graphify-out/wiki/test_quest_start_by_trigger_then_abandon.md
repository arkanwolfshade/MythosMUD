# test_quest_start_by_trigger_then_abandon

> 35 nodes · cohesion 0.06

## Key Concepts

- **Player** (19 connections)
- **.apply_corruption()** (3 connections) — `server/async_persistence.py`
- **.apply_fear()** (3 connections) — `server/async_persistence.py`
- **.apply_lucidity_loss()** (3 connections) — `server/async_persistence.py`
- **.async_damage_player()** (3 connections) — `server/async_persistence.py`
- **.async_heal_player()** (3 connections) — `server/async_persistence.py`
- **.damage_player()** (3 connections) — `server/async_persistence.py`
- **.gain_occult_knowledge()** (3 connections) — `server/async_persistence.py`
- **.get_active_players_by_user_id()** (3 connections) — `server/async_persistence.py`
- **.get_player_by_name()** (3 connections) — `server/async_persistence.py`
- **.get_player_by_user_id()** (3 connections) — `server/async_persistence.py`
- **.get_players_by_user_id()** (3 connections) — `server/async_persistence.py`
- **.get_players_in_room()** (3 connections) — `server/async_persistence.py`
- **.heal_player()** (3 connections) — `server/async_persistence.py`
- **.list_players()** (3 connections) — `server/async_persistence.py`
- **.save_player()** (3 connections) — `server/async_persistence.py`
- **.save_players()** (3 connections) — `server/async_persistence.py`
- **.validate_and_fix_player_room()** (3 connections) — `server/async_persistence.py`
- **Get a player by name. Delegates to PlayerRepository.** (1 connections) — `server/async_persistence.py`
- **Get all players (including deleted) for a user ID. Delegates to…** (1 connections) — `server/async_persistence.py`
- **Get active (non-deleted) players for a user ID. Delegates to PlayerRepository.** (1 connections) — `server/async_persistence.py`
- **Get the first active player by user ID (backward compatibility). Delegates to…** (1 connections) — `server/async_persistence.py`
- **Save a player. Delegates to PlayerRepository.** (1 connections) — `server/async_persistence.py`
- **List all players. Delegates to PlayerRepository.** (1 connections) — `server/async_persistence.py`
- **Get all players in a specific room. Delegates to PlayerRepository.** (1 connections) — `server/async_persistence.py`
- *... and 10 more nodes in this community*

## Relationships

- [test_party_service.py](test_party_service.py.md) (17 shared connections)
- [whisper-movement.spec.ts](whisper-movement.spec.ts.md) (2 shared connections)

## Source Files

- `server/async_persistence.py`

## Audit Trail

- EXTRACTED: 53 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*