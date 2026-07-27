# Persistence Repositories Skill

> 10 nodes · cohesion 0.27

## Key Concepts

- **_row_to_skill()** (8 connections) — `server/persistence/repositories/skill_repository.py`
- **.get_all_skills()** (6 connections) — `server/persistence/repositories/skill_repository.py`
- **.get_skill_by_id()** (6 connections) — `server/persistence/repositories/skill_repository.py`
- **.get_skill_by_key()** (6 connections) — `server/persistence/repositories/skill_repository.py`
- **Skill** (6 connections) — `server/persistence/repositories/skill_repository.py`
- **Any** (3 connections) — `server/persistence/repositories/skill_repository.py`
- **Get a skill by key (e.g. accounting, cthulhu_mythos).          Args:** (1 connections) — `server/persistence/repositories/skill_repository.py`
- **Map procedure result row to Skill model.** (1 connections) — `server/persistence/repositories/skill_repository.py`
- **Get all skills in the catalog.          Returns:             list[Skill]: All sk** (1 connections) — `server/persistence/repositories/skill_repository.py`
- **Get a skill by ID.          Args:             skill_id: Skill primary key.** (1 connections) — `server/persistence/repositories/skill_repository.py`

## Relationships

- [[NPC Admin API]] (9 shared connections)
- [[Game Service Bundle]] (6 shared connections)

## Source Files

- `server/persistence/repositories/skill_repository.py`

## Audit Trail

- EXTRACTED: 35 (90%)
- INFERRED: 4 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
