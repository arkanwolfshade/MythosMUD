# Tests for get spell targeting

> 9 nodes

## Key Concepts

- **TestGetSpellTargetingService** (5 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **TestGetSpellLearningService** (5 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_spell_targeting_service_success()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_spell_targeting_service_none_raises_runtime_error()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_spell_learning_service_success()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **.test_get_spell_learning_service_none_raises_runtime_error()** (3 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Tests for get_spell_targeting_service dependency function.** (2 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_spell_targeting_service returns service when present.** (2 connections) — `server/tests/unit/infrastructure/test_dependencies.py`
- **Test get_spell_targeting_service raises RuntimeError when service is None.** (2 connections) — `server/tests/unit/infrastructure/test_dependencies.py`

## Relationships

- [. init ()](_init_%28%29.md) (6 shared connections)
- [Connection Manager](Connection_Manager.md) (2 shared connections)

## Source Files

- `server/tests/unit/infrastructure/test_dependencies.py`

## Audit Trail

- EXTRACTED: 26 (93%)
- INFERRED: 2 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*