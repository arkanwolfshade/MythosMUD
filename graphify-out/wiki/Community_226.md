# Community 226

> 65 nodes

## Key Concepts

- **PlayerEffectRepository** (18 connections) — `server/persistence/repositories/player_effect_repository.py`
- **test_player_effect_repository.py** (17 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **PlayerEffect** (12 connections) — `server/models/player_effect.py`
- **.get_active_effects_for_player()** (9 connections) — `server/persistence/repositories/player_effect_repository.py`
- **_row_to_player_effect()** (8 connections) — `server/persistence/repositories/player_effect_repository.py`
- **asyncio** (8 connections)
- **.add_effect()** (7 connections) — `server/persistence/repositories/player_effect_repository.py`
- **UUID** (7 connections)
- **AddEffectInput** (6 connections) — `server/persistence/repositories/player_effect_repository.py`
- **_add_effect_params()** (6 connections) — `server/persistence/repositories/player_effect_repository.py`
- **_make_effect()** (6 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **Any** (6 connections)
- **.delete_effect()** (5 connections) — `server/persistence/repositories/player_effect_repository.py`
- **._execute_add_effect()** (5 connections) — `server/persistence/repositories/player_effect_repository.py`
- **.expire_effects_for_tick()** (5 connections) — `server/persistence/repositories/player_effect_repository.py`
- **.get_effect_remaining_ticks()** (5 connections) — `server/persistence/repositories/player_effect_repository.py`
- **.get_effects_expiring_this_tick()** (5 connections) — `server/persistence/repositories/player_effect_repository.py`
- **_row_from_effect()** (5 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **test_get_active_effects_for_player_filters_by_remaining()** (5 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **test_get_effect_remaining_ticks()** (5 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **test_has_effect_true()** (5 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **_int_opt()** (4 connections) — `server/persistence/repositories/player_effect_repository.py`
- **_opt_str()** (4 connections) — `server/persistence/repositories/player_effect_repository.py`
- **.has_effect()** (4 connections) — `server/persistence/repositories/player_effect_repository.py`
- **_str_opt()** (4 connections) — `server/persistence/repositories/player_effect_repository.py`
- *... and 40 more nodes in this community*

## Relationships

- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (23 shared connections)
- [Invite Codes & Session Maker (E2E)](Invite_Codes_&_Session_Maker_E2E.md) (5 shared connections)
- [Async Persistence Layer](Async_Persistence_Layer.md) (1 shared connections)
- [Community 543](Community_543.md) (1 shared connections)

## Source Files

- `server/models/player_effect.py`
- `server/persistence/repositories/player_effect_repository.py`
- `server/tests/unit/persistence/test_player_effect_repository.py`

## Audit Trail

- EXTRACTED: 124 (96%)
- INFERRED: 5 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*