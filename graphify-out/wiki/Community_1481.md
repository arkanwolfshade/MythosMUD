# Community 1481

> 5 nodes

## Key Concepts

- **.get_profession_by_id()** (3 connections) — `server/async_persistence.py`
- **.get_professions()** (3 connections) — `server/async_persistence.py`
- **Profession** (2 connections)
- **Get all available professions using SQLAlchemy ORM.** (1 connections) — `server/async_persistence.py`
- **Get a profession by ID. Delegates to ProfessionRepository.** (1 connections) — `server/async_persistence.py`

## Relationships

- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (2 shared connections)

## Source Files

- `server/async_persistence.py`

## Audit Trail

- EXTRACTED: 6 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*