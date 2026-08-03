# game models player

> 123 nodes

## Key Concepts

- **game.py** (32 connections) — `server/models/game.py`
- **StatusEffect** (32 connections) — `server/models/game.py`
- **Player** (26 connections) — `server/models/game.py`
- **spell_effects_status.py** (24 connections) — `server/game/magic/spell_effects_status.py`
- **test_game_player.py** (23 connections) — `server/tests/unit/models/test_game_player.py`
- **InventoryItem** (19 connections) — `server/models/game.py`
- **StatusEffectType** (18 connections) — `server/models/game.py`
- **test_game_status_effect.py** (13 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **test_game_enums.py** (11 connections) — `server/tests/unit/models/test_game_enums.py`
- **_apply_player_status_with_grace_check()** (10 connections) — `server/game/magic/spell_effects_status.py`
- **_handle_player_status_effect()** (10 connections) — `server/game/magic/spell_effects_status.py`
- **run_status_effect()** (10 connections) — `server/game/magic/spell_effects_status.py`
- **memory_profiler.py** (10 connections) — `server/utils/memory_profiler.py`
- **_apply_status_effect_to_player()** (9 connections) — `server/game/magic/spell_effects_status.py`
- **Any** (8 connections)
- **_grace_period_blocks_negative_status_effect()** (7 connections) — `server/game/magic/spell_effects_status.py`
- **_maybe_run_force_flee_effect()** (7 connections) — `server/game/magic/spell_effects_status.py`
- **_remove_player_status_effect()** (7 connections) — `server/game/magic/spell_effects_status.py`
- **UUID** (6 connections)
- **_parse_status_effect_metadata()** (6 connections) — `server/game/magic/spell_effects_status.py`
- **test_game_inventory_item.py** (6 connections) — `server/tests/unit/models/test_game_inventory_item.py`
- **BaseModel** (5 connections)
- **.is_active()** (5 connections) — `server/models/game.py`
- **.get_active_status_effects()** (4 connections) — `server/models/game.py`
- **test_inventory_item_quantity_validation_min()** (4 connections) — `server/tests/unit/models/test_game_inventory_item.py`
- *... and 98 more nodes in this community*

## Relationships

- [spell models rationale](spell_models_rationale.md) (14 shared connections)
- [game weapon player](game_weapon_player.md) (13 shared connections)
- [spell game magic](spell_game_magic.md) (11 shared connections)
- [game models stats](game_models_stats.md) (11 shared connections)
- [world models rationale](world_models_rationale.md) (6 shared connections)
- [command inventory factories](command_inventory_factories.md) (5 shared connections)
- [NATS Messaging](NATS_Messaging.md) (4 shared connections)
- [Player Stats](Player_Stats.md) (4 shared connections)
- [memory profiler rationale](memory_profiler_rationale.md) (4 shared connections)
- [grace period login](grace_period_login.md) (3 shared connections)
- [Item Instances](Item_Instances.md) (3 shared connections)
- [Async Query Helpers](Async_Query_Helpers.md) (3 shared connections)

## Source Files

- `server/game/magic/spell_effects_status.py`
- `server/models/game.py`
- `server/tests/unit/models/test_game_enums.py`
- `server/tests/unit/models/test_game_inventory_item.py`
- `server/tests/unit/models/test_game_player.py`
- `server/tests/unit/models/test_game_status_effect.py`
- `server/utils/memory_profiler.py`

## Audit Trail

- EXTRACTED: 481 (98%)
- INFERRED: 10 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*