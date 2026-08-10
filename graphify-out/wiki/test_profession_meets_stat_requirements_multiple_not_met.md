# test_profession_meets_stat_requirements_multiple_not_met

> 149 nodes

## Key Concepts

- **game.py** (32 connections) — `server/models/game.py`
- **StatusEffect** (32 connections) — `server/models/game.py`
- **Player** (26 connections) — `server/models/game.py`
- **spell_effects_status.py** (24 connections) — `server/game/magic/spell_effects_status.py`
- **test_game_player.py** (23 connections) — `server/tests/unit/models/test_game_player.py`
- **InventoryItem** (19 connections) — `server/models/game.py`
- **test_player_schema_converter_weapon.py** (19 connections) — `server/tests/unit/game/test_player_schema_converter_weapon.py`
- **StatusEffectType** (18 connections) — `server/models/game.py`
- **test_game_status_effect.py** (13 connections) — `server/tests/unit/models/test_game_status_effect.py`
- **benchmark_model_memory_usage()** (13 connections) — `server/utils/memory_profiler.py`
- **_weapon_from_prototype_registry()** (12 connections) — `server/game/player_schema_converter.py`
- **.create_player_read_from_object()** (12 connections) — `server/game/player_schema_converter.py`
- **Any** (11 connections)
- **_inventory_item_with_weapon()** (11 connections) — `server/game/player_schema_converter.py`
- **_apply_player_status_with_grace_check()** (10 connections) — `server/game/magic/spell_effects_status.py`
- **_handle_player_status_effect()** (10 connections) — `server/game/magic/spell_effects_status.py`
- **run_status_effect()** (10 connections) — `server/game/magic/spell_effects_status.py`
- **.create_player_read_from_dict()** (10 connections) — `server/game/player_schema_converter.py`
- **memory_profiler.py** (10 connections) — `server/utils/memory_profiler.py`
- **_apply_status_effect_to_player()** (9 connections) — `server/game/magic/spell_effects_status.py`
- **Any** (8 connections)
- **_grace_period_blocks_negative_status_effect()** (7 connections) — `server/game/magic/spell_effects_status.py`
- **_maybe_run_force_flee_effect()** (7 connections) — `server/game/magic/spell_effects_status.py`
- **_remove_player_status_effect()** (7 connections) — `server/game/magic/spell_effects_status.py`
- **WeaponStats** (7 connections) — `server/models/game.py`
- *... and 124 more nodes in this community*

## Relationships

- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (26 shared connections)
- [Combat Attack Service](Combat_Attack_Service.md) (15 shared connections)
- [Game Mechanics Service](Game_Mechanics_Service.md) (11 shared connections)
- [NPC Service Tests](NPC_Service_Tests.md) (10 shared connections)
- [Memory Profiler Tools](Memory_Profiler_Tools.md) (7 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (6 shared connections)
- [Player Creation Service](Player_Creation_Service.md) (5 shared connections)
- [Quest Instance Repository](Quest_Instance_Repository.md) (4 shared connections)
- [Magic Lifespan Initialization](Magic_Lifespan_Initialization.md) (4 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (4 shared connections)
- [Investigations Sessions Session](Investigations_Sessions_Session.md) (3 shared connections)
- [Player Respawn Events](Player_Respawn_Events.md) (3 shared connections)

## Source Files

- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_effects_status.py`
- `server/game/player_schema_converter.py`
- `server/models/game.py`
- `server/tests/unit/game/test_player_schema_converter_weapon.py`
- `server/tests/unit/models/test_game_inventory_item.py`
- `server/tests/unit/models/test_game_player.py`
- `server/tests/unit/models/test_game_status_effect.py`
- `server/utils/memory_profiler.py`

## Audit Trail

- EXTRACTED: 597 (96%)
- INFERRED: 26 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*