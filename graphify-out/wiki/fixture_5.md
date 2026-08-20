# fixture

> 11 nodes

## Key Concepts

- **fixture** (6 connections)
- **catalog_with_own_language_and_mythos()** (4 connections) — `server/tests/unit/game/test_skill_service.py`
- **mock_persistence()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **mock_player_skill_repo()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **mock_skill_repo()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **mock_skill_use_log_repo()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **Mock PlayerSkillRepository.** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **Mock AsyncPersistenceLayer (get_profession_by_id, get_player_by_id).** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **Mock SkillUseLogRepository for use logging and improvement (plan 10.4).** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **Minimal catalog: accounting, library_use, own_language, cthulhu_mythos (for…** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **Mock SkillRepository returning catalog.** (1 connections) — `server/tests/unit/game/test_skill_service.py`

## Relationships

- [test_skill_service.py](test_skill_service.py.md) (5 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [SkillService](SkillService.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/test_skill_service.py`

## Audit Trail

- EXTRACTED: 16 (94%)
- INFERRED: 1 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*