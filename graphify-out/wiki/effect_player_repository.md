# effect player repository

> 61 nodes

## Key Concepts

- **player_effect_repository.py** (21 connections) — `server/persistence/repositories/player_effect_repository.py`
- **PlayerEffectRepository** (18 connections) — `server/persistence/repositories/player_effect_repository.py`
- **PlayerEffect** (17 connections) — `server/models/player_effect.py`
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
- *... and 36 more nodes in this community*

## Relationships

- [commands shutdown process](commands_shutdown_process.md) (15 shared connections)
- [world models rationale](world_models_rationale.md) (5 shared connections)
- [Database Config](Database_Config.md) (4 shared connections)
- [argon2 auth rationale](argon2_auth_rationale.md) (3 shared connections)
- [combat models rationale](combat_models_rationale.md) (2 shared connections)
- [npc population stats](npc_population_stats.md) (2 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [player preferences service](player_preferences_service.md) (1 shared connections)
- [game models enums](game_models_enums.md) (1 shared connections)
- [Loot Generation](Loot_Generation.md) (1 shared connections)
- [persistence rationale players](persistence_rationale_players.md) (1 shared connections)

## Source Files

- `server/models/player_effect.py`
- `server/persistence/repositories/player_effect_repository.py`
- `server/tests/unit/persistence/test_player_effect_repository.py`

## Audit Trail

- EXTRACTED: 211 (92%)
- INFERRED: 18 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*