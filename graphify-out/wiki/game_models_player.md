# game models player

> 64 nodes

## Key Concepts

- **test_spell.py** (30 connections) — `server/tests/unit/models/test_spell.py`
- **SpellMaterial** (25 connections) — `server/models/spell.py`
- **test_spell_materials.py** (22 connections) — `server/tests/unit/game/magic/test_spell_materials.py`
- **_spell()** (11 connections) — `server/tests/unit/game/magic/test_spell_materials.py`
- **.load_spells()** (4 connections) — `server/game/magic/spell_registry.py`
- **test_spell_mp_cost_validation_negative()** (4 connections) — `server/tests/unit/models/test_spell.py`
- **test_spell_lucidity_cost_validation_negative()** (4 connections) — `server/tests/unit/models/test_spell.py`
- **test_spell_with_materials()** (4 connections) — `server/tests/unit/models/test_spell.py`
- **test_check_materials_missing_player()** (3 connections) — `server/tests/unit/game/magic/test_spell_materials.py`
- **test_check_materials_all_present()** (3 connections) — `server/tests/unit/game/magic/test_spell_materials.py`
- **test_check_materials_reports_missing()** (3 connections) — `server/tests/unit/game/magic/test_spell_materials.py`
- **test_consume_materials_player_not_found()** (3 connections) — `server/tests/unit/game/magic/test_spell_materials.py`
- **test_consume_materials_decrements_quantity()** (3 connections) — `server/tests/unit/game/magic/test_spell_materials.py`
- **test_consume_materials_non_consumed_keeps_item()** (3 connections) — `server/tests/unit/game/magic/test_spell_materials.py`
- **test_spell_material_creation()** (3 connections) — `server/tests/unit/models/test_spell.py`
- **test_spell_material_consumed_default()** (3 connections) — `server/tests/unit/models/test_spell.py`
- **test_spell_material_consumed_false()** (3 connections) — `server/tests/unit/models/test_spell.py`
- **test_spell_material_consumed_true()** (3 connections) — `server/tests/unit/models/test_spell.py`
- **test_spell_is_mythos_true()** (3 connections) — `server/tests/unit/models/test_spell.py`
- **test_spell_is_mythos_false()** (3 connections) — `server/tests/unit/models/test_spell.py`
- **test_spell_requires_lucidity_true()** (3 connections) — `server/tests/unit/models/test_spell.py`
- **test_spell_requires_lucidity_false_zero()** (3 connections) — `server/tests/unit/models/test_spell.py`
- **test_spell_requires_lucidity_false_default()** (3 connections) — `server/tests/unit/models/test_spell.py`
- **test_spell_default_values()** (3 connections) — `server/tests/unit/models/test_spell.py`
- **test_spell_with_effect_data()** (3 connections) — `server/tests/unit/models/test_spell.py`
- *... and 39 more nodes in this community*

## Relationships

- [spell game magic](spell_game_magic.md) (15 shared connections)
- [coercion int inventory](coercion_int_inventory.md) (13 shared connections)
- [player respawn event](player_respawn_event.md) (3 shared connections)
- [manager room npcs](manager_room_npcs.md) (2 shared connections)
- [room realtime rationale](room_realtime_rationale.md) (2 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (2 shared connections)
- [task registry app](task_registry_app.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_registry.py`
- `server/models/spell.py`
- `server/tests/unit/game/magic/test_spell_materials.py`
- `server/tests/unit/models/test_spell.py`

## Audit Trail

- EXTRACTED: 203 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*