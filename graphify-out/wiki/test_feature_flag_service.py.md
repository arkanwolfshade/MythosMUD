# test_feature_flag_service.py

> 17 nodes

## Key Concepts

- **test_feature_flag_service.py** (10 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.get_combat_configuration()** (8 connections) — `server/services/feature_flag_service.py`
- **is_combat_enabled()** (8 connections) — `server/services/feature_flag_service.py`
- **.get_feature_status()** (7 connections) — `server/services/feature_flag_service.py`
- **is_combat_logging_enabled()** (6 connections) — `server/services/feature_flag_service.py`
- **is_combat_monitoring_enabled()** (6 connections) — `server/services/feature_flag_service.py`
- **.validate_combat_requirements()** (5 connections) — `server/services/feature_flag_service.py`
- **.check_combat_availability()** (4 connections) — `server/services/feature_flag_service.py`
- **Any** (2 connections)
- **Validate that all combat requirements are met. Returns: bool: True if combat…** (1 connections) — `server/services/feature_flag_service.py`
- **Get status of all feature flags. Returns: Dict[str, Dict[str, Any]]: Status of…** (1 connections) — `server/services/feature_flag_service.py`
- **Check if combat is available for a specific player or globally. Args:…** (1 connections) — `server/services/feature_flag_service.py`
- **Convenience function to check if combat is enabled. Returns: bool: True if…** (1 connections) — `server/services/feature_flag_service.py`
- **Convenience function to check if combat logging is enabled. Returns: bool: True…** (1 connections) — `server/services/feature_flag_service.py`
- **Convenience function to check if combat monitoring is enabled. Returns: bool:…** (1 connections) — `server/services/feature_flag_service.py`
- **Get all combat-related configuration settings. Returns: Dict[str, Any]:…** (1 connections) — `server/services/feature_flag_service.py`
- **Unit tests for feature flag service. Tests the FeatureFlagService class and…** (1 connections) — `server/tests/unit/services/test_feature_flag_service.py`

## Relationships

- [FeatureFlagService](FeatureFlagService.md) (5 shared connections)
- [TestGlobalFunctions](TestGlobalFunctions.md) (5 shared connections)
- [combat_monitoring_service.py](combat_monitoring_service.py.md) (5 shared connections)
- [TestFeatureFlagService](TestFeatureFlagService.md) (1 shared connections)

## Source Files

- `server/services/feature_flag_service.py`
- `server/tests/unit/services/test_feature_flag_service.py`

## Audit Trail

- EXTRACTED: 40 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*