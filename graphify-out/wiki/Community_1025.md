# Community 1025

> 14 nodes

## Key Concepts

- **ProfessionRepository** (11 connections) — `server/persistence/repositories/profession_repository.py`
- **_row_to_profession()** (11 connections) — `server/persistence/repositories/profession_repository.py`
- **.get_all_professions()** (6 connections) — `server/persistence/repositories/profession_repository.py`
- **.get_profession_by_id()** (6 connections) — `server/persistence/repositories/profession_repository.py`
- **.__init__()** (3 connections) — `server/persistence/repositories/profession_repository.py`
- **repo()** (3 connections) — `server/tests/unit/persistence/repositories/test_profession_repository.py`
- **Profession** (3 connections)
- **test_row_to_profession()** (2 connections) — `server/tests/unit/persistence/repositories/test_profession_repository.py`
- **fixture** (1 connections)
- **Get a profession by ID. Args: profession_id: Profession ID Returns: Profession…** (1 connections) — `server/persistence/repositories/profession_repository.py`
- **Map procedure result row to Profession model.** (1 connections) — `server/persistence/repositories/profession_repository.py`
- **Repository for profession persistence operations. Handles profession queries…** (1 connections) — `server/persistence/repositories/profession_repository.py`
- **Initialize the profession repository.** (1 connections) — `server/persistence/repositories/profession_repository.py`
- **Get all available professions. Returns: list[Profession]: List of all…** (1 connections) — `server/persistence/repositories/profession_repository.py`

## Relationships

- [Invite & NPC DB Scripts](Invite_&_NPC_DB_Scripts.md) (8 shared connections)
- [Community 900](Community_900.md) (7 shared connections)
- [Community 327](Community_327.md) (2 shared connections)
- [Community 51](Community_51.md) (1 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (1 shared connections)

## Source Files

- `server/persistence/repositories/profession_repository.py`
- `server/tests/unit/persistence/repositories/test_profession_repository.py`

## Audit Trail

- EXTRACTED: 32 (91%)
- INFERRED: 3 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*