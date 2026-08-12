# fetch_professions

> 8 nodes

## Key Concepts

- **fetch_professions()** (7 connections) — `server/async_persistence_direct_queries.py`
- **.get_professions()** (4 connections) — `server/async_persistence.py`
- **.get_profession_by_id()** (3 connections) — `server/async_persistence.py`
- **Profession** (2 connections)
- **Profession** (1 connections)
- **Get all available professions using SQLAlchemy ORM.** (1 connections) — `server/async_persistence_direct_queries.py`
- **Get all available professions using SQLAlchemy ORM.** (1 connections) — `server/async_persistence.py`
- **Get a profession by ID. Delegates to ProfessionRepository.** (1 connections) — `server/async_persistence.py`

## Relationships

- [get_logger](get_logger.md) (3 shared connections)
- [database.py](database.py.md) (2 shared connections)
- [log_and_raise](log_and_raise.md) (1 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/async_persistence_direct_queries.py`

## Audit Trail

- EXTRACTED: 20 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*