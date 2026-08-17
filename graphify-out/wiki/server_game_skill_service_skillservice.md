# server game skill service skillservice

> 36 nodes

## Key Concepts

- **SkillRepository** (29 connections) — `server/persistence/repositories/skill_repository.py`
- **test_skill_repository.py** (17 connections) — `server/tests/unit/persistence/repositories/test_skill_repository.py`
- **SkillUseLogRepository** (15 connections) — `server/persistence/repositories/skill_use_log_repository.py`
- **_row_to_skill()** (9 connections) — `server/persistence/repositories/skill_repository.py`
- **asyncio** (8 connections)
- **.get_all_skills()** (6 connections) — `server/persistence/repositories/skill_repository.py`
- **.get_skill_by_id()** (6 connections) — `server/persistence/repositories/skill_repository.py`
- **.get_skill_by_key()** (6 connections) — `server/persistence/repositories/skill_repository.py`
- **.__init__()** (5 connections) — `server/game/skill_service.py`
- **.get_skill_ids_used_at_level()** (5 connections) — `server/persistence/repositories/skill_use_log_repository.py`
- **.record_use()** (5 connections) — `server/persistence/repositories/skill_use_log_repository.py`
- **test_get_all_skills_db_error()** (4 connections) — `server/tests/unit/persistence/repositories/test_skill_repository.py`
- **test_get_skill_by_id_db_error()** (4 connections) — `server/tests/unit/persistence/repositories/test_skill_repository.py`
- **test_get_skill_by_key_db_error()** (4 connections) — `server/tests/unit/persistence/repositories/test_skill_repository.py`
- **.__init__()** (3 connections) — `server/persistence/repositories/skill_repository.py`
- **repo()** (3 connections) — `server/tests/unit/persistence/repositories/test_skill_repository.py`
- **test_get_all_skills_success()** (3 connections) — `server/tests/unit/persistence/repositories/test_skill_repository.py`
- **test_get_skill_by_id_found()** (3 connections) — `server/tests/unit/persistence/repositories/test_skill_repository.py`
- **test_get_skill_by_id_not_found()** (3 connections) — `server/tests/unit/persistence/repositories/test_skill_repository.py`
- **test_get_skill_by_key_found()** (3 connections) — `server/tests/unit/persistence/repositories/test_skill_repository.py`
- **test_get_skill_by_key_not_found()** (3 connections) — `server/tests/unit/persistence/repositories/test_skill_repository.py`
- **UUID** (3 connections)
- **.__init__()** (2 connections) — `server/persistence/repositories/skill_use_log_repository.py`
- **test_row_to_skill_defaults()** (2 connections) — `server/tests/unit/persistence/repositories/test_skill_repository.py`
- **Any** (1 connections)
- *... and 11 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (16 shared connections)
- [server game skill service](server_game_skill_service.md) (8 shared connections)
- [scripts populate test npc databases](scripts_populate_test_npc_databases.md) (8 shared connections)
- [server container bundles game gamebundle](server_container_bundles_game_gamebundle.md) (5 shared connections)
- [e2e tests load tests get](e2e_tests_load_tests_get.md) (5 shared connections)
- [scripts validate calendar](scripts_validate_calendar.md) (2 shared connections)
- [leveluphook](leveluphook.md) (2 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (2 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (1 shared connections)
- [server api skills get skills](server_api_skills_get_skills.md) (1 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/game/skill_service.py`
- `server/persistence/repositories/skill_repository.py`
- `server/persistence/repositories/skill_use_log_repository.py`
- `server/tests/unit/persistence/repositories/test_skill_repository.py`

## Audit Trail

- EXTRACTED: 86 (80%)
- INFERRED: 21 (20%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*