# effect player repository

> 58 nodes

## Key Concepts

- **player_effect_repository.py** (21 connections) — `server/persistence/repositories/player_effect_repository.py`
- **PlayerEffectRepository** (18 connections) — `server/persistence/repositories/player_effect_repository.py`
- **test_player_effect_repository.py** (17 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **.get_active_effects_for_player()** (10 connections) — `server/persistence/repositories/player_effect_repository.py`
- **_row_to_player_effect()** (8 connections) — `server/persistence/repositories/player_effect_repository.py`
- **UUID** (8 connections)
- **.add_effect()** (8 connections) — `server/persistence/repositories/player_effect_repository.py`
- **Any** (7 connections)
- **AddEffectInput** (7 connections) — `server/persistence/repositories/player_effect_repository.py`
- **_add_effect_params()** (6 connections) — `server/persistence/repositories/player_effect_repository.py`
- **.delete_effect()** (6 connections) — `server/persistence/repositories/player_effect_repository.py`
- **_make_effect()** (6 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **._execute_add_effect()** (5 connections) — `server/persistence/repositories/player_effect_repository.py`
- **.get_effect_remaining_ticks()** (5 connections) — `server/persistence/repositories/player_effect_repository.py`
- **_row_from_effect()** (5 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **_str_opt()** (4 connections) — `server/persistence/repositories/player_effect_repository.py`
- **_int_opt()** (4 connections) — `server/persistence/repositories/player_effect_repository.py`
- **_opt_str()** (4 connections) — `server/persistence/repositories/player_effect_repository.py`
- **.has_effect()** (4 connections) — `server/persistence/repositories/player_effect_repository.py`
- **test_get_active_effects_for_player_filters_by_remaining()** (4 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **test_has_effect_true()** (4 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **test_get_effect_remaining_ticks()** (4 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **._remaining_ticks()** (3 connections) — `server/persistence/repositories/player_effect_repository.py`
- **repo()** (3 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- **test_add_effect_returns_id()** (2 connections) — `server/tests/unit/persistence/test_player_effect_repository.py`
- *... and 33 more nodes in this community*

## Relationships

- [Database Config](Database_Config.md) (20 shared connections)
- [world models rationale](world_models_rationale.md) (9 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [models npc rationale](models_npc_rationale.md) (2 shared connections)
- [combat npc services](combat_npc_services.md) (1 shared connections)
- [NPC Combat](NPC_Combat.md) (1 shared connections)
- [command admin setlucidity](command_admin_setlucidity.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/player_effect_repository.py`
- `server/tests/unit/persistence/test_player_effect_repository.py`

## Audit Trail

- EXTRACTED: 200 (95%)
- INFERRED: 10 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*