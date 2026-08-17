# SpellMaterial

> 29 nodes

## Key Concepts

- **SpellMaterial** (25 connections) — `server/models/spell.py`
- **test_spell_materials.py** (23 connections) — `server/tests/unit/game/magic/test_spell_materials.py`
- **_spell()** (15 connections) — `server/tests/unit/game/magic/test_spell_materials.py`
- **asyncio** (8 connections)
- **test_check_materials_all_present()** (4 connections) — `server/tests/unit/game/magic/test_spell_materials.py`
- **test_check_materials_missing_player()** (4 connections) — `server/tests/unit/game/magic/test_spell_materials.py`
- **test_check_materials_reports_missing()** (4 connections) — `server/tests/unit/game/magic/test_spell_materials.py`
- **test_consume_materials_decrements_quantity()** (4 connections) — `server/tests/unit/game/magic/test_spell_materials.py`
- **test_consume_materials_non_consumed_keeps_item()** (4 connections) — `server/tests/unit/game/magic/test_spell_materials.py`
- **test_consume_materials_player_not_found()** (4 connections) — `server/tests/unit/game/magic/test_spell_materials.py`
- **.load_spells()** (3 connections) — `server/game/magic/spell_registry.py`
- **materials_service()** (3 connections) — `server/tests/unit/game/magic/test_spell_materials.py`
- **test_check_materials_empty_spell()** (3 connections) — `server/tests/unit/game/magic/test_spell_materials.py`
- **test_consume_materials_no_materials()** (3 connections) — `server/tests/unit/game/magic/test_spell_materials.py`
- **test_spell_material_consumed_default()** (3 connections) — `server/tests/unit/models/test_spell.py`
- **test_spell_material_consumed_false()** (3 connections) — `server/tests/unit/models/test_spell.py`
- **test_spell_material_consumed_true()** (3 connections) — `server/tests/unit/models/test_spell.py`
- **test_spell_material_creation()** (3 connections) — `server/tests/unit/models/test_spell.py`
- **player_service()** (2 connections) — `server/tests/unit/game/magic/test_spell_materials.py`
- **test_process_material_requirement_skips_processed_index()** (2 connections) — `server/tests/unit/game/magic/test_spell_materials.py`
- **BaseModel** (2 connections)
- **fixture** (2 connections)
- **Load all spells from the database into memory. This should be called during…** (1 connections) — `server/game/magic/spell_registry.py`
- **Material component required for casting a spell.** (1 connections) — `server/models/spell.py`
- **Unit tests for spell material checking and consumption.** (1 connections) — `server/tests/unit/game/magic/test_spell_materials.py`
- *... and 4 more nodes in this community*

## Relationships

- [SpellEffectType](SpellEffectType.md) (16 shared connections)
- [test_magic_service.py](test_magic_service.py.md) (3 shared connections)
- [Spell](Spell.md) (3 shared connections)
- [SpellRegistry](SpellRegistry.md) (2 shared connections)
- [SpellTargetingService](SpellTargetingService.md) (2 shared connections)
- [AliasStorage](AliasStorage.md) (1 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_registry.py`
- `server/models/spell.py`
- `server/tests/unit/game/magic/test_spell_materials.py`
- `server/tests/unit/models/test_spell.py`

## Audit Trail

- EXTRACTED: 60 (73%)
- INFERRED: 22 (27%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*