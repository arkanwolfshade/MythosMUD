# character creation service

> 28 nodes

## Key Concepts

- **test_skills.py** (14 connections) — `server/tests/unit/api/test_skills.py`
- **get_skills_catalog()** (11 connections) — `server/api/skills.py`
- **skill.py** (8 connections) — `server/schemas/players/skill.py`
- **SkillListResponse** (7 connections) — `server/schemas/players/skill.py`
- **SkillData** (5 connections) — `server/schemas/players/skill.py`
- **PlayerSkillEntry** (5 connections) — `server/schemas/players/skill.py`
- **PlayerSkillsResponse** (5 connections) — `server/schemas/players/skill.py`
- **BaseModel** (4 connections)
- **test_get_skills_catalog_returns_list()** (4 connections) — `server/tests/unit/api/test_skills.py`
- **test_get_skills_catalog_unauthorized()** (4 connections) — `server/tests/unit/api/test_skills.py`
- **mock_user()** (3 connections) — `server/tests/unit/api/test_skills.py`
- **sample_skills()** (3 connections) — `server/tests/unit/api/test_skills.py`
- **mock_request()** (2 connections) — `server/tests/unit/api/test_skills.py`
- **mock_skill_repository()** (2 connections) — `server/tests/unit/api/test_skills.py`
- **Request** (1 connections)
- **Return the  skills catalog (base values, allow_at_creation).      Cthulhu Mythos** (1 connections) — `server/api/skills.py`
- **Skill catalog API response schemas.  Used by GET /v1/skills (or equivalent) for** (1 connections) — `server/schemas/players/skill.py`
- **Single skill catalog entry.** (1 connections) — `server/schemas/players/skill.py`
- **Response model for skills catalog list.** (1 connections) — `server/schemas/players/skill.py`
- **Single player skill (character creation revamp 4.3).** (1 connections) — `server/schemas/players/skill.py`
- **Response for GET /v1/api/players/{player_id}/skills.** (1 connections) — `server/schemas/players/skill.py`
- **Unit tests for skills catalog API (GET /v1/skills).  Character creation revamp 4** (1 connections) — `server/tests/unit/api/test_skills.py`
- **Create a mock request object.** (1 connections) — `server/tests/unit/api/test_skills.py`
- **Create a mock user for auth.** (1 connections) — `server/tests/unit/api/test_skills.py`
- **Sample skills for catalog response.** (1 connections) — `server/tests/unit/api/test_skills.py`
- *... and 3 more nodes in this community*

## Relationships

- [command inventory factories](command_inventory_factories.md) (7 shared connections)
- [Exception Containers](Exception_Containers.md) (3 shared connections)
- [ascii map renderer](ascii_map_renderer.md) (3 shared connections)
- [Database Config](Database_Config.md) (3 shared connections)
- [Player Stats](Player_Stats.md) (2 shared connections)
- [world models rationale](world_models_rationale.md) (1 shared connections)

## Source Files

- `server/api/skills.py`
- `server/schemas/players/skill.py`
- `server/tests/unit/api/test_skills.py`

## Audit Trail

- EXTRACTED: 88 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*