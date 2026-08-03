# combat npc services

> 10 nodes

## Key Concepts

- **test_spell_repository.py** (14 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`
- **_mock_session()** (4 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`
- **_spell_row()** (3 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`
- **test_get_all_spells()** (3 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`
- **test_get_spell_by_id_found()** (3 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`
- **test_row_to_spell_dict_maps_fields()** (2 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`
- **repo()** (2 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`
- **test_get_spell_by_id_not_found()** (2 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`
- **test_get_all_spells_db_error()** (2 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`
- **Unit tests for SpellRepository.** (1 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`

## Relationships

- [Database Config](Database_Config.md) (5 shared connections)
- [coercion int inventory](coercion_int_inventory.md) (2 shared connections)
- [command inventory factories](command_inventory_factories.md) (1 shared connections)

## Source Files

- `server/tests/unit/persistence/repositories/test_spell_repository.py`

## Audit Trail

- EXTRACTED: 35 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*