# spell models rationale

> 136 nodes

## Key Concepts

- **Spell** (84 connections) — `server/models/spell.py`
- **spell_effects.py** (47 connections) — `server/game/magic/spell_effects.py`
- **player_service.py** (45 connections) — `server/game/player_service.py`
- **test_spell.py** (30 connections) — `server/tests/unit/models/test_spell.py`
- **spell_targeting.py** (25 connections) — `server/game/magic/spell_targeting.py`
- **spell.py** (22 connections) — `server/models/spell.py`
- **spell_effects_support.py** (19 connections) — `server/game/magic/spell_effects_support.py`
- **SpellMaterialsService** (15 connections) — `server/game/magic/spell_materials.py`
- **test_spell_targeting.py** (15 connections) — `server/tests/unit/game/magic/test_spell_targeting.py`
- **SpellMaterial** (13 connections) — `server/models/spell.py`
- **spell_costs.py** (12 connections) — `server/game/magic/spell_costs.py`
- **spell_materials.py** (10 connections) — `server/game/magic/spell_materials.py`
- **process_stat_modify_effect()** (9 connections) — `server/game/magic/spell_effects_support.py`
- **process_create_object_effect()** (9 connections) — `server/game/magic/spell_effects_support.py`
- **SpellEffectType** (9 connections) — `server/models/spell.py`
- **_apply_stat_modify_to_player()** (8 connections) — `server/game/magic/spell_effects_support.py`
- **.consume_materials()** (8 connections) — `server/game/magic/spell_materials.py`
- **SpellSchool** (8 connections) — `server/models/spell.py`
- **SpellTargetType** (8 connections) — `server/models/spell.py`
- **Any** (6 connections)
- **_create_object_for_room()** (6 connections) — `server/game/magic/spell_effects_support.py`
- **SpellRangeType** (6 connections) — `server/models/spell.py`
- **.apply_costs()** (5 connections) — `server/game/magic/spell_costs.py`
- **_build_stat_modifications()** (5 connections) — `server/game/magic/spell_effects_support.py`
- **_create_object_for_player()** (5 connections) — `server/game/magic/spell_effects_support.py`
- *... and 111 more nodes in this community*

## Relationships

- [spell game magic](spell_game_magic.md) (49 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (44 shared connections)
- [Item Instances](Item_Instances.md) (21 shared connections)
- [NATS Messaging](NATS_Messaging.md) (19 shared connections)
- [game models player](game_models_player.md) (14 shared connections)
- [magic healing game](magic_healing_game.md) (13 shared connections)
- [command inventory factories](command_inventory_factories.md) (11 shared connections)
- [aggro threat services](aggro_threat_services.md) (8 shared connections)
- [world models rationale](world_models_rationale.md) (8 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (4 shared connections)
- [Async Query Helpers](Async_Query_Helpers.md) (4 shared connections)
- [magic completion game](magic_completion_game.md) (3 shared connections)

## Source Files

- `server/game/magic/spell_costs.py`
- `server/game/magic/spell_effects.py`
- `server/game/magic/spell_effects_internal.py`
- `server/game/magic/spell_effects_stats.py`
- `server/game/magic/spell_effects_support.py`
- `server/game/magic/spell_materials.py`
- `server/game/magic/spell_registry.py`
- `server/game/magic/spell_targeting.py`
- `server/game/player_service.py`
- `server/models/spell.py`
- `server/tests/unit/game/magic/test_spell_targeting.py`
- `server/tests/unit/models/test_spell.py`

## Audit Trail

- EXTRACTED: 611 (97%)
- INFERRED: 21 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*