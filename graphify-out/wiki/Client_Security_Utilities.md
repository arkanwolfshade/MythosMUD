# Client Security Utilities

> 33 nodes · cohesion 0.10

## Key Concepts

- **player_effect_repository.py** (21 connections) — `server/persistence/repositories/player_effect_repository.py`
- **PlayerEffectRepository** (18 connections) — `server/persistence/repositories/player_effect_repository.py`
- **.get_active_effects_for_player()** (10 connections) — `server/persistence/repositories/player_effect_repository.py`
- **.add_effect()** (8 connections) — `server/persistence/repositories/player_effect_repository.py`
- **UUID** (8 connections)
- **_row_to_player_effect()** (8 connections) — `server/persistence/repositories/player_effect_repository.py`
- **AddEffectInput** (7 connections) — `server/persistence/repositories/player_effect_repository.py`
- **Any** (7 connections)
- **_add_effect_params()** (6 connections) — `server/persistence/repositories/player_effect_repository.py`
- **.delete_effect()** (6 connections) — `server/persistence/repositories/player_effect_repository.py`
- **._execute_add_effect()** (5 connections) — `server/persistence/repositories/player_effect_repository.py`
- **.get_effect_remaining_ticks()** (5 connections) — `server/persistence/repositories/player_effect_repository.py`
- **_int_opt()** (4 connections) — `server/persistence/repositories/player_effect_repository.py`
- **_opt_str()** (4 connections) — `server/persistence/repositories/player_effect_repository.py`
- **.has_effect()** (4 connections) — `server/persistence/repositories/player_effect_repository.py`
- **_str_opt()** (4 connections) — `server/persistence/repositories/player_effect_repository.py`
- **._remaining_ticks()** (3 connections) — `server/persistence/repositories/player_effect_repository.py`
- **TypedDict** (1 connections)
- **Player effect repository for the effects system (ADR-009).  Async persistence fo** (1 connections) — `server/persistence/repositories/player_effect_repository.py`
- **Add a player effect. Returns the effect id (UUID string).          Args:** (1 connections) — `server/persistence/repositories/player_effect_repository.py`
- **Delete an effect by id. No-op if not found.** (1 connections) — `server/persistence/repositories/player_effect_repository.py`
- **Compute remaining ticks. Effect is active when result > 0.** (1 connections) — `server/persistence/repositories/player_effect_repository.py`
- **Return effects where remaining_ticks > 0. Order by applied_at_tick.** (1 connections) — `server/persistence/repositories/player_effect_repository.py`
- **Return str(val) or empty string if val is None.** (1 connections) — `server/persistence/repositories/player_effect_repository.py`
- **Return True if player has an active effect of the given type.** (1 connections) — `server/persistence/repositories/player_effect_repository.py`
- *... and 8 more nodes in this community*

## Relationships

- [Realtime Connection Impl](Realtime_Connection_Impl.md) (21 shared connections)
- [Combat Attack Flow](Combat_Attack_Flow.md) (9 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (4 shared connections)
- [NPC Admin API](NPC_Admin_API.md) (1 shared connections)
- [Players API Endpoints](Players_API_Endpoints.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/player_effect_repository.py`

## Audit Trail

- EXTRACTED: 135 (94%)
- INFERRED: 9 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*