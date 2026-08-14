# TestGlobalFunctions

> 14 nodes

## Key Concepts

- **TestGlobalFunctions** (8 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **refresh_feature_flags()** (4 connections) — `server/services/feature_flag_service.py`
- **.test_get_feature_flags()** (3 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.test_is_combat_enabled_global()** (3 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.test_is_combat_logging_enabled_global()** (3 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.test_is_combat_monitoring_enabled_global()** (3 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.test_refresh_feature_flags()** (3 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **Refresh feature flags by clearing cache and reloading configuration. This…** (1 connections) — `server/services/feature_flag_service.py`
- **Test suite for global convenience functions.** (1 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **Test get_feature_flags returns the global service instance.** (1 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **Test global is_combat_enabled function.** (1 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **Test global is_combat_logging_enabled function.** (1 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **Test global is_combat_monitoring_enabled function.** (1 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **Test refresh_feature_flags clears cache.** (1 connections) — `server/tests/unit/services/test_feature_flag_service.py`

## Relationships

- [test_feature_flag_service.py](test_feature_flag_service.py.md) (5 shared connections)
- [combat_monitoring_service.py](combat_monitoring_service.py.md) (2 shared connections)
- [FeatureFlagService](FeatureFlagService.md) (1 shared connections)

## Source Files

- `server/services/feature_flag_service.py`
- `server/tests/unit/services/test_feature_flag_service.py`

## Audit Trail

- EXTRACTED: 20 (95%)
- INFERRED: 1 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*