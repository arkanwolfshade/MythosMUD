# SkillService

> 26 nodes

## Key Concepts

- **SkillService** (38 connections) — `server/game/skill_service.py`
- **.set_player_skills()** (9 connections) — `server/game/skill_service.py`
- **Any** (9 connections)
- **_get_container_services()** (8 connections) — `server/commands/skills_commands.py`
- **._validate_occupation_slots()** (6 connections) — `server/game/skill_service.py`
- **._validate_personal_interest()** (6 connections) — `server/game/skill_service.py`
- **.validate_skills_payload()** (6 connections) — `server/game/skill_service.py`
- **._build_profession_mod_by_key()** (5 connections) — `server/game/skill_service.py`
- **._compute_final_skill_values()** (5 connections) — `server/game/skill_service.py`
- **._validate_no_overlap()** (5 connections) — `server/game/skill_service.py`
- **skill_service()** (5 connections) — `server/tests/unit/game/test_skill_service.py`
- **.get_player_skills()** (4 connections) — `server/game/skill_service.py`
- **.get_skills_catalog()** (3 connections) — `server/game/skill_service.py`
- **test_get_container_services_ok()** (3 connections) — `server/tests/unit/commands/test_skills_commands.py`
- **Get container, persistence, and skill_service from request, or None if…** (1 connections) — `server/commands/skills_commands.py`
- **Raise ValueError if any skill_id appears in both occupation and personal…** (1 connections) — `server/game/skill_service.py`
- **Build skill_key -> total modifier from profession skill_modifiers (supports…** (1 connections) — `server/game/skill_service.py`
- **Compute final skill_id -> value: base + profession mod, then occupation…** (1 connections) — `server/game/skill_service.py`
- **Validate skills allocation without persisting. Raises ValueError if invalid.…** (1 connections) — `server/game/skill_service.py`
- **Set all skills for a character at creation. Validates occupation_slots (9…** (1 connections) — `server/game/skill_service.py`
- **Return list of {skill_id, skill_key, skill_name, value} for the player. If the…** (1 connections) — `server/game/skill_service.py`
- **Service for skills catalog, per-character skills, use logging, and improvement…** (1 connections) — `server/game/skill_service.py`
- **Return list of skill dicts (id, key, name, base_value, allow_at_creation,…** (1 connections) — `server/game/skill_service.py`
- **Raise ValueError if occupation_slots are not exactly one 70, two 60, three 50,…** (1 connections) — `server/game/skill_service.py`
- **Require exactly 4 skill_ids; Cthulhu Mythos not allowed; all skill_ids unique.** (1 connections) — `server/game/skill_service.py`
- *... and 1 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (12 shared connections)
- [UUID](UUID.md) (6 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (5 shared connections)
- [handle_skills_command](handle_skills_command.md) (5 shared connections)
- [bundles/game.py](bundles-game.py.md) (2 shared connections)
- [User](User.md) (2 shared connections)
- [server/dependencies.py](server-dependencies.py.md) (2 shared connections)
- [test_skill_service.py](test_skill_service.py.md) (2 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)
- [fixture](fixture.md) (1 shared connections)

## Source Files

- `server/commands/skills_commands.py`
- `server/game/skill_service.py`
- `server/tests/unit/commands/test_skills_commands.py`
- `server/tests/unit/game/test_skill_service.py`

## Audit Trail

- EXTRACTED: 73 (90%)
- INFERRED: 8 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*