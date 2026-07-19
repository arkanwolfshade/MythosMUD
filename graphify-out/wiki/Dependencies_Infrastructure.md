# Dependencies Infrastructure

> 12 nodes · cohesion 0.24

## Key Concepts

- **get_spell_learning_service()** (8 connections) — `server/dependencies.py`
- **get_spell_targeting_service()** (8 connections) — `server/dependencies.py`
- **TestGetSpellLearningService** (5 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **TestGetSpellTargetingService** (5 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_spell_learning_service_none_raises_runtime_error()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_spell_learning_service_success()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_spell_targeting_service_none_raises_runtime_error()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_spell_targeting_service_success()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Tests for get_spell_targeting_service dependency function.** (2 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_spell_targeting_service returns service when present.** (2 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_spell_targeting_service raises RuntimeError when service is None.** (2 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Get a SpellTargetingService instance with dependency injection.      Args:** (2 connections) — `server/dependencies.py`

## Relationships

- [[Dependency Injection Tests]] (8 shared connections)
- [[Combat Command Handler]] (2 shared connections)
- [[NPC Admin API]] (2 shared connections)
- [[Database Manager Tests]] (2 shared connections)

## Source Files

- `server/dependencies.py`
- `server/tests/unit/infrastructure/test_dependencies.py`

## Audit Trail

- EXTRACTED: 42 (91%)
- INFERRED: 4 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
