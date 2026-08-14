# FeatureFlagService

> 20 nodes

## Key Concepts

- **FeatureFlagService** (35 connections) — `server/services/feature_flag_service.py`
- **.__init__()** (3 connections) — `server/services/feature_flag_service.py`
- **.test_check_combat_availability_invalid_requirements()** (3 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.test_init()** (3 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.test_is_combat_monitoring_enabled_false()** (3 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.test_validate_combat_requirements_invalid_xp_multiplier()** (3 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.clear_cache()** (2 connections) — `server/services/feature_flag_service.py`
- **.is_combat_enabled()** (2 connections) — `server/services/feature_flag_service.py`
- **.is_combat_logging_enabled()** (2 connections) — `server/services/feature_flag_service.py`
- **.is_combat_monitoring_enabled()** (2 connections) — `server/services/feature_flag_service.py`
- **Clear the feature flag cache. This should be called when configuration changes…** (1 connections) — `server/services/feature_flag_service.py`
- **Centralized feature flag service for MythosMUD. Provides type-safe access to…** (1 connections) — `server/services/feature_flag_service.py`
- **Initialize the feature flag service.** (1 connections) — `server/services/feature_flag_service.py`
- **Check if combat system is enabled. Returns: bool: True if combat is enabled,…** (1 connections) — `server/services/feature_flag_service.py`
- **Check if combat logging is enabled. Returns: bool: True if combat logging is…** (1 connections) — `server/services/feature_flag_service.py`
- **Check if combat monitoring is enabled. Returns: bool: True if combat monitoring…** (1 connections) — `server/services/feature_flag_service.py`
- **Test is_combat_monitoring_enabled returns False when disabled.** (1 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **Test FeatureFlagService initialization.** (1 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **Test validate_combat_requirements returns False with invalid XP multiplier.** (1 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **Test check_combat_availability returns False when requirements are invalid.** (1 connections) — `server/tests/unit/services/test_feature_flag_service.py`

## Relationships

- [TestFeatureFlagService](TestFeatureFlagService.md) (16 shared connections)
- [test_feature_flag_service.py](test_feature_flag_service.py.md) (5 shared connections)
- [combat_monitoring_service.py](combat_monitoring_service.py.md) (2 shared connections)
- [.test_check_combat_availability_with_player_id](test_check_combat_availability_with_player_id.md) (1 shared connections)
- [.test_get_feature_status](test_get_feature_status.md) (1 shared connections)
- [.test_is_combat_enabled_true](test_is_combat_enabled_true.md) (1 shared connections)
- [.test_is_combat_logging_enabled_false](test_is_combat_logging_enabled_false.md) (1 shared connections)
- [.test_is_combat_monitoring_enabled_true](test_is_combat_monitoring_enabled_true.md) (1 shared connections)
- [TestGlobalFunctions](TestGlobalFunctions.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)

## Source Files

- `server/services/feature_flag_service.py`
- `server/tests/unit/services/test_feature_flag_service.py`

## Audit Trail

- EXTRACTED: 47 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*