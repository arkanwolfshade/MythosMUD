# FeatureFlagService

> 91 nodes

## Key Concepts

- **FeatureFlagService** (35 connections) — `server/services/feature_flag_service.py`
- **TestFeatureFlagService** (23 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **feature_flag_service.py** (13 connections) — `server/services/feature_flag_service.py`
- **test_feature_flag_service.py** (10 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **get_feature_flags()** (9 connections) — `server/services/feature_flag_service.py`
- **TestGlobalFunctions** (8 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.get_combat_configuration()** (8 connections) — `server/services/feature_flag_service.py`
- **is_combat_enabled()** (8 connections) — `server/services/feature_flag_service.py`
- **.get_feature_status()** (7 connections) — `server/services/feature_flag_service.py`
- **is_combat_logging_enabled()** (6 connections) — `server/services/feature_flag_service.py`
- **is_combat_monitoring_enabled()** (6 connections) — `server/services/feature_flag_service.py`
- **.validate_combat_requirements()** (5 connections) — `server/services/feature_flag_service.py`
- **.__init__()** (4 connections) — `server/services/combat_configuration_service.py`
- **.check_combat_availability()** (4 connections) — `server/services/feature_flag_service.py`
- **refresh_feature_flags()** (4 connections) — `server/services/feature_flag_service.py`
- **.__init__()** (3 connections) — `server/services/feature_flag_service.py`
- **.test_check_combat_availability_disabled()** (3 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.test_check_combat_availability_enabled()** (3 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.test_check_combat_availability_invalid_requirements()** (3 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.test_check_combat_availability_with_player_id()** (3 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.test_clear_cache()** (3 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.test_get_combat_configuration()** (3 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.test_get_feature_status()** (3 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.test_init()** (3 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.test_is_combat_enabled_caching()** (3 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- *... and 66 more nodes in this community*

## Relationships

- [get_config](get_config.md) (3 shared connections)
- [CombatConfiguration](CombatConfiguration.md) (3 shared connections)
- [test_combat_monitoring_service.py](test_combat_monitoring_service.py.md) (2 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [CombatMonitoringService](CombatMonitoringService.md) (1 shared connections)

## Source Files

- `server/services/combat_configuration_service.py`
- `server/services/feature_flag_service.py`
- `server/tests/unit/services/test_feature_flag_service.py`

## Audit Trail

- EXTRACTED: 145 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*