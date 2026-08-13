# _row_to_profession

> 14 nodes

## Key Concepts

- **_row_to_profession()** (9 connections) — `server/persistence/repositories/profession_repository.py`
- **.get_all_professions()** (6 connections) — `server/persistence/repositories/profession_repository.py`
- **.get_profession_by_id()** (6 connections) — `server/persistence/repositories/profession_repository.py`
- **_bool_or_default()** (4 connections) — `server/persistence/repositories/profession_repository.py`
- **_text_or_default()** (4 connections) — `server/persistence/repositories/profession_repository.py`
- **Any** (4 connections)
- **_str_or_default()** (3 connections) — `server/persistence/repositories/profession_repository.py`
- **Profession** (3 connections)
- **Get a profession by ID. Args: profession_id: Profession ID Returns: Profession…** (1 connections) — `server/persistence/repositories/profession_repository.py`
- **Return value as str or a default if falsy.** (1 connections) — `server/persistence/repositories/profession_repository.py`
- **Return text value or default if falsy.** (1 connections) — `server/persistence/repositories/profession_repository.py`
- **Return bool(value) when not None, otherwise default.** (1 connections) — `server/persistence/repositories/profession_repository.py`
- **Map procedure result row to Profession model.** (1 connections) — `server/persistence/repositories/profession_repository.py`
- **Get all available professions. Returns: list[Profession]: List of all…** (1 connections) — `server/persistence/repositories/profession_repository.py`

## Relationships

- [DatabaseError](DatabaseError.md) (6 shared connections)
- [log_and_raise](log_and_raise.md) (2 shared connections)
- [get_session_maker](get_session_maker.md) (2 shared connections)
- [Profession](Profession.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/profession_repository.py`

## Audit Trail

- EXTRACTED: 28 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*