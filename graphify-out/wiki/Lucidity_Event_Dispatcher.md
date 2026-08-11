# Lucidity Event Dispatcher

> 33 nodes

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
- **Input for add_effect. effect_type, category, duration, applied_at_tick required;** (1 connections) — `server/persistence/repositories/player_effect_repository.py`
- **Build params dict for add_player_effect procedure.** (1 connections) — `server/persistence/repositories/player_effect_repository.py`
- *... and 8 more nodes in this community*

## Relationships

- [Schemas Maps Map](Schemas_Maps_Map.md) (23 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (6 shared connections)
- [Client Event Store](Client_Event_Store.md) (3 shared connections)
- [Command Request App State](Command_Request_App_State.md) (3 shared connections)
- [NATS Subject Manager](NATS_Subject_Manager.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/player_effect_repository.py`

## Audit Trail

- EXTRACTED: 135 (94%)
- INFERRED: 9 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*