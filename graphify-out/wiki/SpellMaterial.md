# SpellMaterial

> 43 nodes

## Key Concepts

- **SpellMaterial** (25 connections) — `server/models/spell.py`
- **test_spell_materials.py** (23 connections) — `server/tests/unit/game/magic/test_spell_materials.py`
- **SpellMaterialsService** (16 connections) — `server/game/magic/spell_materials.py`
- **_spell()** (15 connections) — `server/tests/unit/game/magic/test_spell_materials.py`
- **.consume_materials()** (8 connections) — `server/game/magic/spell_materials.py`
- **asyncio** (8 connections)
- **._build_final_inventory()** (4 connections) — `server/game/magic/spell_materials.py`
- **.check_materials()** (4 connections) — `server/game/magic/spell_materials.py`
- **._consume_material_item()** (4 connections) — `server/game/magic/spell_materials.py`
- **._process_material_requirement()** (4 connections) — `server/game/magic/spell_materials.py`
- **test_check_materials_all_present()** (4 connections) — `server/tests/unit/game/magic/test_spell_materials.py`
- **test_check_materials_missing_player()** (4 connections) — `server/tests/unit/game/magic/test_spell_materials.py`
- **test_check_materials_reports_missing()** (4 connections) — `server/tests/unit/game/magic/test_spell_materials.py`
- **test_consume_materials_decrements_quantity()** (4 connections) — `server/tests/unit/game/magic/test_spell_materials.py`
- **test_consume_materials_non_consumed_keeps_item()** (4 connections) — `server/tests/unit/game/magic/test_spell_materials.py`
- **test_consume_materials_player_not_found()** (4 connections) — `server/tests/unit/game/magic/test_spell_materials.py`
- **Any** (4 connections)
- **.load_spells()** (3 connections) — `server/game/magic/spell_registry.py`
- **materials_service()** (3 connections) — `server/tests/unit/game/magic/test_spell_materials.py`
- **test_check_materials_empty_spell()** (3 connections) — `server/tests/unit/game/magic/test_spell_materials.py`
- **test_consume_materials_no_materials()** (3 connections) — `server/tests/unit/game/magic/test_spell_materials.py`
- **test_spell_material_consumed_default()** (3 connections) — `server/tests/unit/models/test_spell.py`
- **test_spell_material_consumed_false()** (3 connections) — `server/tests/unit/models/test_spell.py`
- **test_spell_material_consumed_true()** (3 connections) — `server/tests/unit/models/test_spell.py`
- **test_spell_material_creation()** (3 connections) — `server/tests/unit/models/test_spell.py`
- *... and 18 more nodes in this community*

## Relationships

- [TargetMatch](TargetMatch.md) (31 shared connections)
- [test_magic_service.py](test_magic_service.py.md) (3 shared connections)
- [PlayerService](PlayerService.md) (2 shared connections)
- [_MagicServiceCore](_MagicServiceCore.md) (1 shared connections)
- [Player](Player.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_materials.py`
- `server/game/magic/spell_registry.py`
- `server/models/spell.py`
- `server/tests/unit/game/magic/test_spell_materials.py`
- `server/tests/unit/models/test_spell.py`

## Audit Trail

- EXTRACTED: 87 (77%)
- INFERRED: 26 (23%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*