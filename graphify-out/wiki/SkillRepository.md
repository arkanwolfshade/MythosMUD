# SkillRepository

> 20 nodes

## Key Concepts

- **SkillRepository** (29 connections) — `server/persistence/repositories/skill_repository.py`
- **test_skill_repository.py** (16 connections) — `server/tests/unit/persistence/repositories/test_skill_repository.py`
- **asyncio** (8 connections)
- **get_skill_repository()** (3 connections) — `server/dependencies.py`
- **.__init__()** (3 connections) — `server/persistence/repositories/skill_repository.py`
- **repo()** (3 connections) — `server/tests/unit/persistence/repositories/test_skill_repository.py`
- **test_get_all_skills_db_error()** (3 connections) — `server/tests/unit/persistence/repositories/test_skill_repository.py`
- **test_get_all_skills_success()** (3 connections) — `server/tests/unit/persistence/repositories/test_skill_repository.py`
- **test_get_skill_by_id_db_error()** (3 connections) — `server/tests/unit/persistence/repositories/test_skill_repository.py`
- **test_get_skill_by_id_found()** (3 connections) — `server/tests/unit/persistence/repositories/test_skill_repository.py`
- **test_get_skill_by_id_not_found()** (3 connections) — `server/tests/unit/persistence/repositories/test_skill_repository.py`
- **test_get_skill_by_key_db_error()** (3 connections) — `server/tests/unit/persistence/repositories/test_skill_repository.py`
- **test_get_skill_by_key_found()** (3 connections) — `server/tests/unit/persistence/repositories/test_skill_repository.py`
- **test_get_skill_by_key_not_found()** (3 connections) — `server/tests/unit/persistence/repositories/test_skill_repository.py`
- **test_row_to_skill_defaults()** (2 connections) — `server/tests/unit/persistence/repositories/test_skill_repository.py`
- **fixture** (1 connections)
- **Get a SkillRepository instance for skills catalog queries. Used by GET…** (1 connections) — `server/dependencies.py`
- **Repository for skills catalog persistence. Handles skill queries for character…** (1 connections) — `server/persistence/repositories/skill_repository.py`
- **Initialize the skill repository.** (1 connections) — `server/persistence/repositories/skill_repository.py`
- **Unit tests for SkillRepository.** (1 connections) — `server/tests/unit/persistence/repositories/test_skill_repository.py`

## Relationships

- [get_logger](get_logger.md) (16 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (3 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (2 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (1 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (1 shared connections)

## Source Files

- `server/dependencies.py`
- `server/persistence/repositories/skill_repository.py`
- `server/tests/unit/persistence/repositories/test_skill_repository.py`

## Audit Trail

- EXTRACTED: 54 (93%)
- INFERRED: 4 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*