# statusParser.ts

> 14 nodes · cohesion 0.24

## Key Concepts

- **test_spell_repository.py** (14 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`
- **_row_to_spell_dict()** (7 connections) — `server/persistence/repositories/spell_repository.py`
- **_mock_session()** (4 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`
- **asyncio** (4 connections)
- **test_get_all_spells()** (4 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`
- **test_get_spell_by_id_found()** (4 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`
- **repo()** (3 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`
- **_spell_row()** (3 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`
- **test_get_all_spells_db_error()** (3 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`
- **test_get_spell_by_id_not_found()** (3 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`
- **test_row_to_spell_dict_maps_fields()** (2 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`
- **Map procedure result row to spell dict.** (1 connections) — `server/persistence/repositories/spell_repository.py`
- **fixture** (1 connections)
- **Unit tests for SpellRepository.** (1 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`

## Relationships

- [endpoints.py](endpoints.py.md) (3 shared connections)
- [AttributeError](AttributeError.md) (3 shared connections)
- [LoggingPatternLinter](LoggingPatternLinter.md) (2 shared connections)
- [test_event_bus_lifecycle.py](test_event_bus_lifecycle.py.md) (2 shared connections)

## Source Files

- `server/persistence/repositories/spell_repository.py`
- `server/tests/unit/persistence/repositories/test_spell_repository.py`

## Audit Trail

- EXTRACTED: 30 (94%)
- INFERRED: 2 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*