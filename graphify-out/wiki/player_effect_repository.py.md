# player_effect_repository.py

> 37 nodes

## Key Concepts

- **player_effect_repository.py** (22 connections) — `server/persistence/repositories/player_effect_repository.py`
- **PlayerEffectRepository** (18 connections) — `server/persistence/repositories/player_effect_repository.py`
- **.get_active_effects_for_player()** (9 connections) — `server/persistence/repositories/player_effect_repository.py`
- **_row_to_player_effect()** (8 connections) — `server/persistence/repositories/player_effect_repository.py`
- **.add_effect()** (7 connections) — `server/persistence/repositories/player_effect_repository.py`
- **UUID** (7 connections)
- **AddEffectInput** (6 connections) — `server/persistence/repositories/player_effect_repository.py`
- **_add_effect_params()** (6 connections) — `server/persistence/repositories/player_effect_repository.py`
- **Any** (6 connections)
- **.delete_effect()** (5 connections) — `server/persistence/repositories/player_effect_repository.py`
- **._execute_add_effect()** (5 connections) — `server/persistence/repositories/player_effect_repository.py`
- **.expire_effects_for_tick()** (5 connections) — `server/persistence/repositories/player_effect_repository.py`
- **.get_effect_remaining_ticks()** (5 connections) — `server/persistence/repositories/player_effect_repository.py`
- **.get_effects_expiring_this_tick()** (5 connections) — `server/persistence/repositories/player_effect_repository.py`
- **_int_opt()** (4 connections) — `server/persistence/repositories/player_effect_repository.py`
- **_opt_str()** (4 connections) — `server/persistence/repositories/player_effect_repository.py`
- **.has_effect()** (4 connections) — `server/persistence/repositories/player_effect_repository.py`
- **_str_opt()** (4 connections) — `server/persistence/repositories/player_effect_repository.py`
- **._remaining_ticks()** (3 connections) — `server/persistence/repositories/player_effect_repository.py`
- **TypedDict** (1 connections)
- **Player effect repository for the effects system (ADR-019). Async persistence…** (1 connections) — `server/persistence/repositories/player_effect_repository.py`
- **Add a player effect. Returns the effect id (UUID string). Args: player_id:…** (1 connections) — `server/persistence/repositories/player_effect_repository.py`
- **Delete an effect by id. No-op if not found.** (1 connections) — `server/persistence/repositories/player_effect_repository.py`
- **Compute remaining ticks. Effect is active when result > 0.** (1 connections) — `server/persistence/repositories/player_effect_repository.py`
- **Return effects where remaining_ticks > 0. Order by applied_at_tick.** (1 connections) — `server/persistence/repositories/player_effect_repository.py`
- *... and 12 more nodes in this community*

## Relationships

- [Player](Player.md) (8 shared connections)
- [DatabaseError](DatabaseError.md) (8 shared connections)
- [get_session_maker](get_session_maker.md) (6 shared connections)
- [async_persistence.py](async_persistence.py.md) (3 shared connections)
- [repositories/__init__.py](repositories-__init__.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (2 shared connections)
- [ExperienceRepository](ExperienceRepository.md) (1 shared connections)
- [DatabaseManager](DatabaseManager.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/player_effect_repository.py`

## Audit Trail

- EXTRACTED: 89 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*