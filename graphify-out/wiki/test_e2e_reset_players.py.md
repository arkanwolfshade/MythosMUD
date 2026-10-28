# test_e2e_reset_players.py

> 45 nodes · cohesion 0.08

## Key Concepts

- **SpellMaterial** (25 connections) — `server/models/spell.py`
- **test_spell_materials.py** (22 connections) — `server/tests/unit/game/magic/test_spell_materials.py`
- **SpellMaterialsService** (16 connections) — `server/game/magic/spell_materials.py`
- **_spell()** (15 connections) — `server/tests/unit/game/magic/test_spell_materials.py`
- **.consume_materials()** (8 connections) — `server/game/magic/spell_materials.py`
- **asyncio** (8 connections)
- **Any** (4 connections)
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
- **UUID** (3 connections)
- **.__init__()** (3 connections) — `server/game/magic/spell_materials.py`
- **.load_spells()** (3 connections) — `server/game/magic/spell_registry.py`
- **materials_service()** (3 connections) — `server/tests/unit/game/magic/test_spell_materials.py`
- **test_check_materials_empty_spell()** (3 connections) — `server/tests/unit/game/magic/test_spell_materials.py`
- **test_consume_materials_no_materials()** (3 connections) — `server/tests/unit/game/magic/test_spell_materials.py`
- **test_spell_material_consumed_default()** (3 connections) — `server/tests/unit/models/test_spell.py`
- **test_spell_material_consumed_false()** (3 connections) — `server/tests/unit/models/test_spell.py`
- *... and 20 more nodes in this community*

## Relationships

- [test_nats_message_handler.py](test_nats_message_handler.py.md) (26 shared connections)
- [test_item.py](test_item.py.md) (4 shared connections)
- [GameClientV2ContainerView.tsx](GameClientV2ContainerView.tsx.md) (2 shared connections)
- [test_security_validator.py](test_security_validator.py.md) (2 shared connections)
- [test_event_bus_lifecycle.py](test_event_bus_lifecycle.py.md) (2 shared connections)
- [handle_whisper_command](handle_whisper_command.md) (1 shared connections)
- [test_active_lucidity_service.py](test_active_lucidity_service.py.md) (1 shared connections)

## Source Files

- `server/game/magic/spell_materials.py`
- `server/game/magic/spell_registry.py`
- `server/models/spell.py`
- `server/tests/unit/game/magic/test_spell_materials.py`
- `server/tests/unit/models/test_spell.py`

## Audit Trail

- EXTRACTED: 101 (89%)
- INFERRED: 13 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*