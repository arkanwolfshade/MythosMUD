# SpellCostsService

> 39 nodes

## Key Concepts

- **SpellCostsService** (19 connections) — `server/game/magic/spell_costs.py`
- **SpellMaterialsService** (16 connections) — `server/game/magic/spell_materials.py`
- **CorruptionPersistenceProtocol** (16 connections) — `server/services/corruption_service.py`
- **spell_costs.py** (16 connections) — `server/game/magic/spell_costs.py`
- **.__init__()** (11 connections) — `server/game/magic/magic_service.py`
- **spell_materials.py** (11 connections) — `server/game/magic/spell_materials.py`
- **MagicServiceOptionalDeps** (10 connections) — `server/game/magic/magic_service.py`
- **.consume_materials()** (8 connections) — `server/game/magic/spell_materials.py`
- **.apply_costs()** (7 connections) — `server/game/magic/spell_costs.py`
- **._notify_mp_update()** (7 connections) — `server/game/magic/spell_costs.py`
- **._apply_corruption_if_mythos()** (6 connections) — `server/game/magic/spell_costs.py`
- **._spend_lucidity_if_required()** (6 connections) — `server/game/magic/spell_costs.py`
- **UUID** (6 connections)
- **.restore_mp()** (4 connections) — `server/game/magic/spell_costs.py`
- **._build_final_inventory()** (4 connections) — `server/game/magic/spell_materials.py`
- **.check_materials()** (4 connections) — `server/game/magic/spell_materials.py`
- **._consume_material_item()** (4 connections) — `server/game/magic/spell_materials.py`
- **._process_material_requirement()** (4 connections) — `server/game/magic/spell_materials.py`
- **Any** (4 connections)
- **Any** (3 connections)
- **UUID** (3 connections)
- **TypedDict** (1 connections)
- **Initialize the magic service. Args: spell_registry: Registry for spell lookups…** (1 connections) — `server/game/magic/magic_service.py`
- **Optional dependencies for MagicService. All keys optional; defaults applied in…** (1 connections) — `server/game/magic/magic_service.py`
- **Spell cost application service. This module handles applying spell costs (MP,…** (1 connections) — `server/game/magic/spell_costs.py`
- *... and 14 more nodes in this community*

## Relationships

- [TargetMatch](TargetMatch.md) (12 shared connections)
- [SpellEffectType](SpellEffectType.md) (8 shared connections)
- [magic_service.py](magic_service.py.md) (7 shared connections)
- [PlayerService](PlayerService.md) (7 shared connections)
- [get_logger](get_logger.md) (7 shared connections)
- [CorruptionTier](CorruptionTier.md) (6 shared connections)
- [SpellLearningService](SpellLearningService.md) (3 shared connections)
- [_MagicServiceCore](_MagicServiceCore.md) (3 shared connections)
- [cleanse_command.py](cleanse_command.py.md) (3 shared connections)
- [DatabaseError](DatabaseError.md) (2 shared connections)
- [TargetType](TargetType.md) (2 shared connections)
- [send_game_event](send_game_event.md) (2 shared connections)

## Source Files

- `server/game/magic/magic_service.py`
- `server/game/magic/spell_costs.py`
- `server/game/magic/spell_materials.py`
- `server/services/corruption_service.py`

## Audit Trail

- EXTRACTED: 110 (86%)
- INFERRED: 18 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*