# test quest instance repository

> 19 nodes

## Key Concepts

- **test_skills.py** (14 connections) — `server/tests/unit/api/test_skills.py`
- **get_skills_catalog()** (11 connections) — `server/api/skills.py`
- **SkillListResponse** (7 connections) — `server/schemas/players/skill.py`
- **SkillData** (5 connections) — `server/schemas/players/skill.py`
- **test_get_skills_catalog_returns_list()** (4 connections) — `server/tests/unit/api/test_skills.py`
- **test_get_skills_catalog_unauthorized()** (4 connections) — `server/tests/unit/api/test_skills.py`
- **mock_user()** (3 connections) — `server/tests/unit/api/test_skills.py`
- **mock_request()** (2 connections) — `server/tests/unit/api/test_skills.py`
- **mock_skill_repository()** (2 connections) — `server/tests/unit/api/test_skills.py`
- **Request** (1 connections)
- **Return the  skills catalog (base values, allow_at_creation).      Cthulhu Mythos** (1 connections) — `server/api/skills.py`
- **Single skill catalog entry.** (1 connections) — `server/schemas/players/skill.py`
- **Response model for skills catalog list.** (1 connections) — `server/schemas/players/skill.py`
- **Unit tests for skills catalog API (GET /v1/skills).  Character creation revamp 4** (1 connections) — `server/tests/unit/api/test_skills.py`
- **Create a mock request object.** (1 connections) — `server/tests/unit/api/test_skills.py`
- **Create a mock user for auth.** (1 connections) — `server/tests/unit/api/test_skills.py`
- **Mock SkillRepository that returns sample skills.** (1 connections) — `server/tests/unit/api/test_skills.py`
- **GET /v1/skills returns SkillListResponse with skills list.** (1 connections) — `server/tests/unit/api/test_skills.py`
- **GET /v1/skills without authenticated user returns 401.** (1 connections) — `server/tests/unit/api/test_skills.py`

## Relationships

- [metrics](metrics.md) (6 shared connections)
- [append unique valid occupant()](append_unique_valid_occupant%28%29.md) (5 shared connections)
- [AbstractContextManager](AbstractContextManager.md) (3 shared connections)
- [test quest definition repository](test_quest_definition_repository.md) (2 shared connections)
- [emit close container event()](emit_close_container_event%28%29.md) (1 shared connections)
- [main()](main%28%29.md) (1 shared connections)

## Source Files

- `server/api/skills.py`
- `server/schemas/players/skill.py`
- `server/tests/unit/api/test_skills.py`

## Audit Trail

- EXTRACTED: 59 (95%)
- INFERRED: 3 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*