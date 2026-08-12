# get_skills_catalog

> 9 nodes

## Key Concepts

- **get_skills_catalog()** (12 connections) — `server/api/skills.py`
- **test_get_skills_catalog_returns_list()** (4 connections) — `server/tests/unit/api/test_skills.py`
- **test_get_skills_catalog_unauthorized()** (4 connections) — `server/tests/unit/api/test_skills.py`
- **asyncio** (2 connections)
- **get** (1 connections)
- **Request** (1 connections)
- **Return the skills catalog (base values, allow_at_creation). Cthulhu Mythos is…** (1 connections) — `server/api/skills.py`
- **GET /v1/skills without authenticated user returns 401.** (1 connections) — `server/tests/unit/api/test_skills.py`
- **GET /v1/skills returns SkillListResponse with skills list.** (1 connections) — `server/tests/unit/api/test_skills.py`

## Relationships

- [PlayerService](PlayerService.md) (3 shared connections)
- [test_skills.py](test_skills.py.md) (3 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (1 shared connections)
- [User](User.md) (1 shared connections)
- [DatabaseError](DatabaseError.md) (1 shared connections)

## Source Files

- `server/api/skills.py`
- `server/tests/unit/api/test_skills.py`

## Audit Trail

- EXTRACTED: 27 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*