# Server Persistence (8)

> 37 nodes

## Key Concepts

- **player_effect_repository.py** (21 connections) — `server/persistence/repositories/player_effect_repository.py`
- **PlayerEffectRepository** (18 connections) — `server/persistence/repositories/player_effect_repository.py`
- **.get_active_effects_for_player()** (10 connections) — `server/persistence/repositories/player_effect_repository.py`
- **_row_to_player_effect()** (8 connections) — `server/persistence/repositories/player_effect_repository.py`
- **UUID** (8 connections)
- **.add_effect()** (8 connections) — `server/persistence/repositories/player_effect_repository.py`
- **Any** (7 connections)
- **AddEffectInput** (7 connections) — `server/persistence/repositories/player_effect_repository.py`
- **_add_effect_params()** (6 connections) — `server/persistence/repositories/player_effect_repository.py`
- **.delete_effect()** (6 connections) — `server/persistence/repositories/player_effect_repository.py`
- **.get_effects_expiring_this_tick()** (6 connections) — `server/persistence/repositories/player_effect_repository.py`
- **.expire_effects_for_tick()** (6 connections) — `server/persistence/repositories/player_effect_repository.py`
- **._execute_add_effect()** (5 connections) — `server/persistence/repositories/player_effect_repository.py`
- **.get_effect_remaining_ticks()** (5 connections) — `server/persistence/repositories/player_effect_repository.py`
- **_str_opt()** (4 connections) — `server/persistence/repositories/player_effect_repository.py`
- **_int_opt()** (4 connections) — `server/persistence/repositories/player_effect_repository.py`
- **_opt_str()** (4 connections) — `server/persistence/repositories/player_effect_repository.py`
- **.has_effect()** (4 connections) — `server/persistence/repositories/player_effect_repository.py`
- **._remaining_ticks()** (3 connections) — `server/persistence/repositories/player_effect_repository.py`
- **TypedDict** (1 connections)
- **Player effect repository for the effects system (ADR-009).  Async persistence fo** (1 connections) — `server/persistence/repositories/player_effect_repository.py`
- **Return str(val) or empty string if val is None.** (1 connections) — `server/persistence/repositories/player_effect_repository.py`
- **Return int value or default if val is None.** (1 connections) — `server/persistence/repositories/player_effect_repository.py`
- **Return str value or default if val is None.** (1 connections) — `server/persistence/repositories/player_effect_repository.py`
- **Map procedure result row to PlayerEffect model.** (1 connections) — `server/persistence/repositories/player_effect_repository.py`
- *... and 12 more nodes in this community*

## Relationships

- [Server Persistence](Server_Persistence.md) (10 shared connections)
- [Server Persistence (11)](Server_Persistence_%2811%29.md) (9 shared connections)
- [Server Admin](Server_Admin.md) (7 shared connections)
- [Server Persistence (3)](Server_Persistence_%283%29.md) (6 shared connections)
- [Server Api](Server_Api.md) (6 shared connections)
- [Server Commands](Server_Commands.md) (2 shared connections)

## Source Files

- `server/persistence/repositories/player_effect_repository.py`

## Audit Trail

- EXTRACTED: 147 (93%)
- INFERRED: 11 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*