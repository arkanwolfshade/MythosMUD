# Cursor Skills Critique

> 7 nodes

## Key Concepts

- **get_skills_catalog()** (11 connections) — `server/api/skills.py`
- **test_get_skills_catalog_returns_list()** (4 connections) — `server/tests/unit/api/test_skills.py`
- **test_get_skills_catalog_unauthorized()** (4 connections) — `server/tests/unit/api/test_skills.py`
- **Request** (1 connections)
- **Return the  skills catalog (base values, allow_at_creation).      Cthulhu Mythos** (1 connections) — `server/api/skills.py`
- **GET /v1/skills returns SkillListResponse with skills list.** (1 connections) — `server/tests/unit/api/test_skills.py`
- **GET /v1/skills without authenticated user returns 401.** (1 connections) — `server/tests/unit/api/test_skills.py`

## Relationships

- [Chat Channel Logger](Chat_Channel_Logger.md) (4 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (3 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (2 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (2 shared connections)

## Source Files

- `server/api/skills.py`
- `server/tests/unit/api/test_skills.py`

## Audit Trail

- EXTRACTED: 21 (91%)
- INFERRED: 2 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*