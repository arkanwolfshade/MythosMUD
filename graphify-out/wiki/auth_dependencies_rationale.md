# auth dependencies rationale

> 23 nodes

## Key Concepts

- **skills.py** (18 connections) — `server/api/skills.py`
- **test_skills.py** (14 connections) — `server/tests/unit/api/test_skills.py`
- **get_skills_catalog()** (11 connections) — `server/api/skills.py`
- **skill.py** (8 connections) — `server/schemas/players/skill.py`
- **SkillListResponse** (7 connections) — `server/schemas/players/skill.py`
- **SkillData** (5 connections) — `server/schemas/players/skill.py`
- **test_get_skills_catalog_returns_list()** (4 connections) — `server/tests/unit/api/test_skills.py`
- **test_get_skills_catalog_unauthorized()** (4 connections) — `server/tests/unit/api/test_skills.py`
- **mock_user()** (3 connections) — `server/tests/unit/api/test_skills.py`
- **mock_request()** (2 connections) — `server/tests/unit/api/test_skills.py`
- **mock_skill_repository()** (2 connections) — `server/tests/unit/api/test_skills.py`
- **Request** (1 connections)
- **Skills catalog API endpoints.  GET /v1/skills returns the skills catalog for cha** (1 connections) — `server/api/skills.py`
- **Return the  skills catalog (base values, allow_at_creation).      Cthulhu Mythos** (1 connections) — `server/api/skills.py`
- **Skill catalog API response schemas.  Used by GET /v1/skills (or equivalent) for** (1 connections) — `server/schemas/players/skill.py`
- **Single skill catalog entry.** (1 connections) — `server/schemas/players/skill.py`
- **Response model for skills catalog list.** (1 connections) — `server/schemas/players/skill.py`
- **Unit tests for skills catalog API (GET /v1/skills).  Character creation revamp 4** (1 connections) — `server/tests/unit/api/test_skills.py`
- **Create a mock request object.** (1 connections) — `server/tests/unit/api/test_skills.py`
- **Create a mock user for auth.** (1 connections) — `server/tests/unit/api/test_skills.py`
- **Mock SkillRepository that returns sample skills.** (1 connections) — `server/tests/unit/api/test_skills.py`
- **GET /v1/skills returns SkillListResponse with skills list.** (1 connections) — `server/tests/unit/api/test_skills.py`
- **GET /v1/skills without authenticated user returns 401.** (1 connections) — `server/tests/unit/api/test_skills.py`

## Relationships

- [endpoints auth rationale](endpoints_auth_rationale.md) (6 shared connections)
- [player requests schemas](player_requests_schemas.md) (5 shared connections)
- [Player Stats](Player_Stats.md) (5 shared connections)
- [services inventory mutation](services_inventory_mutation.md) (4 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (2 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (2 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (1 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (1 shared connections)
- [handler realtime nats](handler_realtime_nats.md) (1 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (1 shared connections)

## Source Files

- `server/api/skills.py`
- `server/schemas/players/skill.py`
- `server/tests/unit/api/test_skills.py`

## Audit Trail

- EXTRACTED: 87 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*