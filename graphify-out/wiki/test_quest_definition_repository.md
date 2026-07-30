# test quest definition repository

> 46 nodes

## Key Concepts

- **Skill** (27 connections) — `server/models/skill.py`
- **Any** (10 connections)
- **.set_player_skills()** (9 connections) — `server/game/skill_service.py`
- **UUID** (8 connections)
- **_row_to_skill()** (7 connections) — `server/persistence/repositories/skill_repository.py`
- **.get_all_skills()** (7 connections) — `server/persistence/repositories/skill_repository.py`
- **.get_skill_by_id()** (7 connections) — `server/persistence/repositories/skill_repository.py`
- **.get_skill_by_key()** (7 connections) — `server/persistence/repositories/skill_repository.py`
- **._validate_occupation_slots()** (6 connections) — `server/game/skill_service.py`
- **._validate_personal_interest()** (6 connections) — `server/game/skill_service.py`
- **.validate_skills_payload()** (6 connections) — `server/game/skill_service.py`
- **._validate_no_overlap()** (5 connections) — `server/game/skill_service.py`
- **._build_profession_mod_by_key()** (5 connections) — `server/game/skill_service.py`
- **._compute_final_skill_values()** (5 connections) — `server/game/skill_service.py`
- **.get_player_skills()** (4 connections) — `server/game/skill_service.py`
- **.record_successful_skill_use()** (4 connections) — `server/game/skill_service.py`
- **.get_skills_used_this_level()** (4 connections) — `server/game/skill_service.py`
- **.run_improvement_rolls()** (4 connections) — `server/game/skill_service.py`
- **.roll_skill_check()** (4 connections) — `server/game/skill_service.py`
- **.get_skills_catalog()** (3 connections) — `server/game/skill_service.py`
- **sample_skills()** (3 connections) — `server/tests/unit/api/test_skills.py`
- **catalog_with_own_language_and_mythos()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **.__repr__()** (2 connections) — `server/models/skill.py`
- **Any** (2 connections)
- **Return list of skill dicts (id, key, name, base_value, allow_at_creation, catego** (1 connections) — `server/game/skill_service.py`
- *... and 21 more nodes in this community*

## Relationships

- [emit close container event()](emit_close_container_event%28%29.md) (21 shared connections)
- [real time](real_time.md) (14 shared connections)
- [main()](main%28%29.md) (5 shared connections)
- [chat nats publisher](chat_nats_publisher.md) (2 shared connections)
- [test quest instance repository](test_quest_instance_repository.md) (2 shared connections)
- [test player service](test_player_service.md) (2 shared connections)

## Source Files

- `server/game/skill_service.py`
- `server/models/skill.py`
- `server/persistence/repositories/skill_repository.py`
- `server/tests/unit/api/test_skills.py`
- `server/tests/unit/game/test_skill_service.py`

## Audit Trail

- EXTRACTED: 159 (94%)
- INFERRED: 11 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*