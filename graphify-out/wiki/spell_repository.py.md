# spell_repository.py

> 21 nodes

## Key Concepts

- **spell_repository.py** (15 connections) — `server/persistence/repositories/spell_repository.py`
- **test_spell_repository.py** (15 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`
- **_row_to_spell_dict()** (7 connections) — `server/persistence/repositories/spell_repository.py`
- **.get_all_spells()** (6 connections) — `server/persistence/repositories/spell_repository.py`
- **.get_spell_by_id()** (6 connections) — `server/persistence/repositories/spell_repository.py`
- **_mock_session()** (4 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`
- **test_get_all_spells()** (4 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`
- **test_get_spell_by_id_found()** (4 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`
- **asyncio** (4 connections)
- **repo()** (3 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`
- **_spell_row()** (3 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`
- **test_get_all_spells_db_error()** (3 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`
- **test_get_spell_by_id_not_found()** (3 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`
- **Any** (3 connections)
- **test_row_to_spell_dict_maps_fields()** (2 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`
- **fixture** (1 connections)
- **Spell repository for async persistence operations. This module provides async…** (1 connections) — `server/persistence/repositories/spell_repository.py`
- **Get a spell by ID. Args: spell_id: Spell ID Returns: dict | None: Spell…** (1 connections) — `server/persistence/repositories/spell_repository.py`
- **Map procedure result row to spell dict.** (1 connections) — `server/persistence/repositories/spell_repository.py`
- **Get all spells from the database. Returns: list[dict]: List of all spell…** (1 connections) — `server/persistence/repositories/spell_repository.py`
- **Unit tests for SpellRepository.** (1 connections) — `server/tests/unit/persistence/repositories/test_spell_repository.py`

## Relationships

- [SpellEffects](SpellEffects.md) (6 shared connections)
- [get_session_maker](get_session_maker.md) (3 shared connections)
- [log_and_raise](log_and_raise.md) (3 shared connections)
- [DatabaseError](DatabaseError.md) (3 shared connections)
- [get_logger](get_logger.md) (3 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (2 shared connections)
- [sqlalchemy.md](sqlalchemy.md.md) (1 shared connections)
- [ValidationError](ValidationError.md) (1 shared connections)
- [error_logging.py](error_logging.py.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/spell_repository.py`
- `server/tests/unit/persistence/repositories/test_spell_repository.py`

## Audit Trail

- EXTRACTED: 54 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*