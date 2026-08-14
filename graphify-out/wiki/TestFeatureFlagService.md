# TestFeatureFlagService

> 24 nodes

## Key Concepts

- **TestFeatureFlagService** (23 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.test_check_combat_availability_disabled()** (3 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.test_check_combat_availability_enabled()** (3 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.test_clear_cache()** (3 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.test_get_combat_configuration()** (3 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.test_is_combat_enabled_caching()** (3 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.test_is_combat_enabled_false()** (3 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.test_is_combat_logging_enabled_true()** (3 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.test_validate_combat_requirements_disabled()** (3 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.test_validate_combat_requirements_invalid_tick_interval()** (3 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.test_validate_combat_requirements_invalid_timeout()** (3 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.test_validate_combat_requirements_valid()** (3 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **Test get_combat_configuration returns all combat settings.** (1 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **Test clear_cache resets all cached values.** (1 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **Test validate_combat_requirements returns True when combat is disabled.** (1 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **Test validate_combat_requirements returns True with valid configuration.** (1 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **Test suite for FeatureFlagService class.** (1 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **Test validate_combat_requirements returns False with invalid tick interval.** (1 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **Test validate_combat_requirements returns False with invalid timeout.** (1 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **Test check_combat_availability returns True when combat is enabled and valid.** (1 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **Test check_combat_availability returns False when combat is disabled.** (1 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **Test is_combat_enabled returns False when disabled.** (1 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **Test is_combat_enabled caches the result.** (1 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **Test is_combat_logging_enabled returns True when enabled.** (1 connections) — `server/tests/unit/services/test_feature_flag_service.py`

## Relationships

- [FeatureFlagService](FeatureFlagService.md) (16 shared connections)
- [test_feature_flag_service.py](test_feature_flag_service.py.md) (1 shared connections)
- [.test_is_combat_monitoring_enabled_true](test_is_combat_monitoring_enabled_true.md) (1 shared connections)
- [.test_get_feature_status](test_get_feature_status.md) (1 shared connections)
- [.test_check_combat_availability_with_player_id](test_check_combat_availability_with_player_id.md) (1 shared connections)
- [.test_is_combat_enabled_true](test_is_combat_enabled_true.md) (1 shared connections)
- [.test_is_combat_logging_enabled_false](test_is_combat_logging_enabled_false.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_feature_flag_service.py`

## Audit Trail

- EXTRACTED: 44 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*