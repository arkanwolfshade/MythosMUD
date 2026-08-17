# SpellTargetingService

> 37 nodes

## Key Concepts

- **SpellTargetingService** (27 connections) — `server/game/magic/spell_targeting.py`
- **SpellMaterialsService** (16 connections) — `server/game/magic/spell_materials.py`
- **.__init__()** (11 connections) — `server/game/magic/magic_service.py`
- **MagicServiceOptionalDeps** (10 connections) — `server/game/magic/magic_service.py`
- **.resolve_spell_target()** (9 connections) — `server/game/magic/spell_targeting.py`
- **.consume_materials()** (8 connections) — `server/game/magic/spell_materials.py`
- **UUID** (8 connections)
- **._get_player()** (7 connections) — `server/game/magic/spell_targeting.py`
- **._match_combat_opponent()** (7 connections) — `server/game/magic/spell_targeting.py`
- **._get_combat_target()** (6 connections) — `server/game/magic/spell_targeting.py`
- **._resolve_area_target()** (6 connections) — `server/game/magic/spell_targeting.py`
- **._resolve_entity_target()** (6 connections) — `server/game/magic/spell_targeting.py`
- **._resolve_self_target()** (6 connections) — `server/game/magic/spell_targeting.py`
- **._build_final_inventory()** (4 connections) — `server/game/magic/spell_materials.py`
- **.check_materials()** (4 connections) — `server/game/magic/spell_materials.py`
- **._consume_material_item()** (4 connections) — `server/game/magic/spell_materials.py`
- **._process_material_requirement()** (4 connections) — `server/game/magic/spell_materials.py`
- **Any** (4 connections)
- **UUID** (3 connections)
- **TypedDict** (1 connections)
- **Player** (1 connections)
- **Initialize the magic service. Args: spell_registry: Registry for spell lookups…** (1 connections) — `server/game/magic/magic_service.py`
- **Optional dependencies for MagicService. All keys optional; defaults applied in…** (1 connections) — `server/game/magic/magic_service.py`
- **Build final inventory with consumed materials removed. Args: inventory:…** (1 connections) — `server/game/magic/spell_materials.py`
- **Consume spell materials from player inventory. Args: player_id: Player ID…** (1 connections) — `server/game/magic/spell_materials.py`
- *... and 12 more nodes in this community*

## Relationships

- [AliasStorage](AliasStorage.md) (8 shared connections)
- [TargetMatch](TargetMatch.md) (7 shared connections)
- [Spell](Spell.md) (6 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (4 shared connections)
- [PlayerService](PlayerService.md) (3 shared connections)
- [_MagicServiceCore](_MagicServiceCore.md) (3 shared connections)
- [SpellRegistry](SpellRegistry.md) (3 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (3 shared connections)
- [test_magic_service.py](test_magic_service.py.md) (2 shared connections)
- [SpellMaterial](SpellMaterial.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [magic.py](magic.py.md) (2 shared connections)

## Source Files

- `server/game/magic/magic_service.py`
- `server/game/magic/spell_materials.py`
- `server/game/magic/spell_targeting.py`

## Audit Trail

- EXTRACTED: 90 (82%)
- INFERRED: 20 (18%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*