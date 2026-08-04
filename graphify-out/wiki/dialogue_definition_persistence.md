# dialogue definition persistence

> 20 nodes

## Key Concepts

- **test_profession_repository.py** (18 connections) — `server/tests/unit/persistence/repositories/test_profession_repository.py`
- **_row_to_profession()** (11 connections) — `server/persistence/repositories/profession_repository.py`
- **_text_or_default()** (6 connections) — `server/persistence/repositories/profession_repository.py`
- **_bool_or_default()** (6 connections) — `server/persistence/repositories/profession_repository.py`
- **_str_or_default()** (5 connections) — `server/persistence/repositories/profession_repository.py`
- **Any** (5 connections)
- **test_helpers_defaults()** (4 connections) — `server/tests/unit/persistence/repositories/test_profession_repository.py`
- **_mock_session()** (4 connections) — `server/tests/unit/persistence/repositories/test_profession_repository.py`
- **_profession_row()** (3 connections) — `server/tests/unit/persistence/repositories/test_profession_repository.py`
- **test_get_all_professions()** (3 connections) — `server/tests/unit/persistence/repositories/test_profession_repository.py`
- **test_get_profession_by_id()** (3 connections) — `server/tests/unit/persistence/repositories/test_profession_repository.py`
- **test_row_to_profession()** (2 connections) — `server/tests/unit/persistence/repositories/test_profession_repository.py`
- **repo()** (2 connections) — `server/tests/unit/persistence/repositories/test_profession_repository.py`
- **test_get_profession_by_id_not_found()** (2 connections) — `server/tests/unit/persistence/repositories/test_profession_repository.py`
- **test_get_all_professions_db_error()** (2 connections) — `server/tests/unit/persistence/repositories/test_profession_repository.py`
- **Return value as str or a default if falsy.** (1 connections) — `server/persistence/repositories/profession_repository.py`
- **Return text value or default if falsy.** (1 connections) — `server/persistence/repositories/profession_repository.py`
- **Return bool(value) when not None, otherwise default.** (1 connections) — `server/persistence/repositories/profession_repository.py`
- **Map procedure result row to Profession model.** (1 connections) — `server/persistence/repositories/profession_repository.py`
- **Unit tests for ProfessionRepository.** (1 connections) — `server/tests/unit/persistence/repositories/test_profession_repository.py`

## Relationships

- [Database Config](Database_Config.md) (8 shared connections)
- [Loot Generation](Loot_Generation.md) (6 shared connections)
- [profession models rationale](profession_models_rationale.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/profession_repository.py`
- `server/tests/unit/persistence/repositories/test_profession_repository.py`

## Audit Trail

- EXTRACTED: 79 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*