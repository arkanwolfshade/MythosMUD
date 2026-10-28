# whisper-movement.spec.ts

> 34 nodes · cohesion 0.06

## Key Concepts

- **UUID** (18 connections)
- **.get_active_player_effects()** (4 connections) — `server/async_persistence.py`
- **.get_player_by_id()** (4 connections) — `server/async_persistence.py`
- **.get_players_batch()** (4 connections) — `server/async_persistence.py`
- **.update_player_last_active()** (4 connections) — `server/async_persistence.py`
- **.award_player_xp()** (3 connections) — `server/async_persistence.py`
- **.clear_player_inventory()** (3 connections) — `server/async_persistence.py`
- **.delete_player()** (3 connections) — `server/async_persistence.py`
- **.get_bank_container()** (3 connections) — `server/async_persistence.py`
- **.get_container()** (3 connections) — `server/async_persistence.py`
- **.get_containers_by_entity_id()** (3 connections) — `server/async_persistence.py`
- **.get_decayed_containers()** (3 connections) — `server/async_persistence.py`
- **.get_player_effect_remaining_ticks()** (3 connections) — `server/async_persistence.py`
- **.has_player_effect()** (3 connections) — `server/async_persistence.py`
- **.remove_player_effect_by_id()** (3 connections) — `server/async_persistence.py`
- **.soft_delete_player()** (3 connections) — `server/async_persistence.py`
- **datetime** (3 connections)
- **.delete_container()** (2 connections) — `server/async_persistence.py`
- **.update_container()** (2 connections) — `server/async_persistence.py`
- **Get a player by ID. Delegates to PlayerRepository.** (1 connections) — `server/async_persistence.py`
- **Soft delete a player (sets is_deleted=True). Delegates to PlayerRepository.** (1 connections) — `server/async_persistence.py`
- **Empty a player's carried and equipped items only. Delegates to PlayerRepository.** (1 connections) — `server/async_persistence.py`
- **Get multiple players by IDs in a single batch query. This method uses a single…** (1 connections) — `server/async_persistence.py`
- **Delete a player. Delegates to PlayerRepository.** (1 connections) — `server/async_persistence.py`
- **Update the last_active timestamp for a player. Delegates to PlayerRepository.** (1 connections) — `server/async_persistence.py`
- *... and 9 more nodes in this community*

## Relationships

- [test_party_service.py](test_party_service.py.md) (17 shared connections)
- [test_quest_start_by_trigger_then_abandon](test_quest_start_by_trigger_then_abandon.md) (2 shared connections)
- [Room](Room.md) (2 shared connections)
- [command_guards.py](command_guards.py.md) (1 shared connections)
- [test_channel_broadcasting_strategies.py](test_channel_broadcasting_strategies.py.md) (1 shared connections)

## Source Files

- `server/async_persistence.py`

## Audit Trail

- EXTRACTED: 56 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*