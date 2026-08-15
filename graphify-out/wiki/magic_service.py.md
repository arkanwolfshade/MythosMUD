# magic_service.py

> 63 nodes

## Key Concepts

- **magic_service.py** (41 connections) — `server/game/magic/magic_service.py`
- **spell.py** (28 connections) — `server/models/spell.py`
- **SpellTargetingService** (27 connections) — `server/game/magic/spell_targeting.py`
- **spell_targeting.py** (25 connections) — `server/game/magic/spell_targeting.py`
- **SpellMaterialsService** (16 connections) — `server/game/magic/spell_materials.py`
- **magic_healing_events.py** (15 connections) — `server/game/magic/magic_healing_events.py`
- **SpellCostsService** (14 connections) — `server/game/magic/spell_costs.py`
- **spell_costs.py** (13 connections) — `server/game/magic/spell_costs.py`
- **.__init__()** (11 connections) — `server/game/magic/magic_service.py`
- **spell_materials.py** (11 connections) — `server/game/magic/spell_materials.py`
- **.resolve_spell_target()** (9 connections) — `server/game/magic/spell_targeting.py`
- **MagicServiceOptionalDeps** (8 connections) — `server/game/magic/magic_service.py`
- **.consume_materials()** (8 connections) — `server/game/magic/spell_materials.py`
- **UUID** (8 connections)
- **._get_player()** (7 connections) — `server/game/magic/spell_targeting.py`
- **._match_combat_opponent()** (7 connections) — `server/game/magic/spell_targeting.py`
- **._get_combat_target()** (6 connections) — `server/game/magic/spell_targeting.py`
- **._resolve_area_target()** (6 connections) — `server/game/magic/spell_targeting.py`
- **._resolve_entity_target()** (6 connections) — `server/game/magic/spell_targeting.py`
- **._resolve_self_target()** (6 connections) — `server/game/magic/spell_targeting.py`
- **.apply_costs()** (5 connections) — `server/game/magic/spell_costs.py`
- **.__init__()** (5 connections) — `server/game/magic/spell_targeting.py`
- **.restore_mp()** (4 connections) — `server/game/magic/spell_costs.py`
- **._build_final_inventory()** (4 connections) — `server/game/magic/spell_materials.py`
- **.check_materials()** (4 connections) — `server/game/magic/spell_materials.py`
- *... and 38 more nodes in this community*

## Relationships

- [SpellEffectType](SpellEffectType.md) (21 shared connections)
- [Spell](Spell.md) (15 shared connections)
- [lifespan_magic.py](lifespan_magic.py.md) (14 shared connections)
- [TargetMatch](TargetMatch.md) (13 shared connections)
- [get_logger](get_logger.md) (13 shared connections)
- [PlayerService](PlayerService.md) (10 shared connections)
- [test_magic_service.py](test_magic_service.py.md) (8 shared connections)
- [_MagicServiceCore](_MagicServiceCore.md) (6 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (6 shared connections)
- [CombatService](CombatService.md) (6 shared connections)
- [test_magic_healing_events.py](test_magic_healing_events.py.md) (5 shared connections)
- [magic_service_completion.py](magic_service_completion.py.md) (4 shared connections)

## Source Files

- `server/game/magic/magic_healing_events.py`
- `server/game/magic/magic_service.py`
- `server/game/magic/spell_costs.py`
- `server/game/magic/spell_materials.py`
- `server/game/magic/spell_targeting.py`
- `server/models/spell.py`

## Audit Trail

- EXTRACTED: 228 (91%)
- INFERRED: 22 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*