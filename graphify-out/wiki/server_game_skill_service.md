# server game skill service

> 112 nodes

## Key Concepts

- **SkillService** (38 connections) — `server/game/skill_service.py`
- **test_skill_service.py** (37 connections) — `server/tests/unit/game/test_skill_service.py`
- **Skill** (26 connections) — `server/models/skill.py`
- **asyncio** (23 connections)
- **skill_service.py** (21 connections) — `server/game/skill_service.py`
- **PlayerSkill** (14 connections) — `server/models/player_skill.py`
- **models/skill.py** (13 connections) — `server/models/skill.py`
- **_occupation_slots_9()** (11 connections) — `server/tests/unit/game/test_skill_service.py`
- **.set_player_skills()** (9 connections) — `server/game/skill_service.py`
- **Any** (9 connections)
- **_personal_interest_4()** (8 connections) — `server/tests/unit/game/test_skill_service.py`
- **UUID** (7 connections)
- **._validate_occupation_slots()** (6 connections) — `server/game/skill_service.py`
- **._validate_personal_interest()** (6 connections) — `server/game/skill_service.py`
- **.validate_skills_payload()** (6 connections) — `server/game/skill_service.py`
- **_row_to_player_skill_with_skill()** (6 connections) — `server/persistence/repositories/player_skill_repository.py`
- **fixture** (6 connections)
- **._build_profession_mod_by_key()** (5 connections) — `server/game/skill_service.py`
- **._compute_final_skill_values()** (5 connections) — `server/game/skill_service.py`
- **._validate_no_overlap()** (5 connections) — `server/game/skill_service.py`
- **skill_service()** (5 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_set_player_skills_cthulhu_mythos_in_occupation_rejected()** (5 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_set_player_skills_duplicate_occupation_skill_ids_raises()** (5 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_set_player_skills_own_language_not_allocated_equals_edu()** (5 connections) — `server/tests/unit/game/test_skill_service.py`
- **test_set_player_skills_valid_creates_rows()** (5 connections) — `server/tests/unit/game/test_skill_service.py`
- *... and 87 more nodes in this community*

## Relationships

- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (26 shared connections)
- [fixturerequest](fixturerequest.md) (10 shared connections)
- [server commands skills commands](server_commands_skills_commands.md) (7 shared connections)
- [server api character creation](server_api_character_creation.md) (6 shared connections)
- [server api players](server_api_players.md) (6 shared connections)
- [server dependencies](server_dependencies.md) (3 shared connections)
- [server async persistence](server_async_persistence.md) (3 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (2 shared connections)
- [scripts validate calendar](scripts_validate_calendar.md) (1 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (1 shared connections)
- [server async persistence asyncpersistencelayer](server_async_persistence_asyncpersistencelayer.md) (1 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (1 shared connections)

## Source Files

- `server/game/skill_service.py`
- `server/models/player_skill.py`
- `server/models/skill.py`
- `server/persistence/repositories/player_skill_repository.py`
- `server/tests/unit/game/test_skill_service.py`

## Audit Trail

- EXTRACTED: 241 (94%)
- INFERRED: 16 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*