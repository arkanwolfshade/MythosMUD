# main

> 13 nodes

## Key Concepts

- **fixture** (6 connections)
- **skill_service()** (5 connections) — `server/tests/unit/game/test_skill_service.py`
- **catalog_with_own_language_and_mythos()** (4 connections) — `server/tests/unit/game/test_skill_service.py`
- **mock_persistence()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **mock_player_skill_repo()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **mock_skill_repo()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **mock_skill_use_log_repo()** (3 connections) — `server/tests/unit/game/test_skill_service.py`
- **Mock PlayerSkillRepository.** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **Mock AsyncPersistenceLayer (get_profession_by_id, get_player_by_id).** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **Mock SkillUseLogRepository for use logging and improvement (plan 10.4).** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **SkillService with mocks.** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **Minimal catalog: accounting, library_use, own_language, cthulhu_mythos (for…** (1 connections) — `server/tests/unit/game/test_skill_service.py`
- **Mock SkillRepository returning catalog.** (1 connections) — `server/tests/unit/game/test_skill_service.py`

## Relationships

- [MessageFilteringHelper](MessageFilteringHelper.md) (6 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)
- [TargetResolutionService](TargetResolutionService.md) (1 shared connections)
- [CacheManager](CacheManager.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/test_skill_service.py`

## Audit Trail

- EXTRACTED: 18 (86%)
- INFERRED: 3 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*