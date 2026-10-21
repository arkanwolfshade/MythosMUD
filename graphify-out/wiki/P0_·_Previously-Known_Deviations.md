# P0 · Previously-Known Deviations

> 5 nodes · cohesion 0.40

## Key Concepts

- **.get_professions()** (4 connections) — `server/async_persistence.py`
- **.get_profession_by_id()** (3 connections) — `server/async_persistence.py`
- **Profession** (2 connections)
- **Get all available professions using SQLAlchemy ORM.** (1 connections) — `server/async_persistence.py`
- **Get a profession by ID. Delegates to ProfessionRepository.** (1 connections) — `server/async_persistence.py`

## Relationships

- [test_party_service.py](test_party_service.py.md) (2 shared connections)
- [LoggingPatternLinter](LoggingPatternLinter.md) (1 shared connections)

## Source Files

- `server/async_persistence.py`

## Audit Trail

- EXTRACTED: 7 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*