# . init ()

> 38 nodes

## Key Concepts

- **feature_flag_service.py** (13 connections) — `server/services/feature_flag_service.py`
- **test_feature_flag_service.py** (10 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **get_feature_flags()** (9 connections) — `server/services/feature_flag_service.py`
- **.__init__()** (8 connections) — `server/services/combat_monitoring_service.py`
- **.get_combat_configuration()** (8 connections) — `server/services/feature_flag_service.py`
- **is_combat_enabled()** (8 connections) — `server/services/feature_flag_service.py`
- **TestGlobalFunctions** (8 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.get_feature_status()** (7 connections) — `server/services/feature_flag_service.py`
- **is_combat_logging_enabled()** (6 connections) — `server/services/feature_flag_service.py`
- **is_combat_monitoring_enabled()** (6 connections) — `server/services/feature_flag_service.py`
- **.validate_combat_requirements()** (5 connections) — `server/services/feature_flag_service.py`
- **refresh_feature_flags()** (5 connections) — `server/services/feature_flag_service.py`
- **.__init__()** (4 connections) — `server/services/combat_configuration_service.py`
- **.check_combat_availability()** (4 connections) — `server/services/feature_flag_service.py`
- **.test_get_feature_flags()** (4 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.clear_cache()** (3 connections) — `server/services/feature_flag_service.py`
- **Convenience function to check if combat is enabled.      Returns:         bool:** (3 connections) — `server/services/feature_flag_service.py`
- **.test_is_combat_enabled_global()** (3 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.test_is_combat_logging_enabled_global()** (3 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.test_is_combat_monitoring_enabled_global()** (3 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.test_refresh_feature_flags()** (3 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **Any** (2 connections)
- **Test global is_combat_enabled function.** (2 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **Initialize the combat configuration service.** (1 connections) — `server/services/combat_configuration_service.py`
- **Initialize the combat monitoring service.** (1 connections) — `server/services/combat_monitoring_service.py`
- *... and 13 more nodes in this community*

## Relationships

- [FeatureFlagService](FeatureFlagService.md) (11 shared connections)
- [combat configuration service](combat_configuration_service.md) (4 shared connections)
- [.to dict()](to_dict%28%29.md) (4 shared connections)
- [initialize nats and combat services()](initialize_nats_and_combat_services%28%29.md) (3 shared connections)
- [main()](main%28%29.md) (2 shared connections)
- [. init ()](_init_%28%29.md) (1 shared connections)
- [CombatMetrics](CombatMetrics.md) (1 shared connections)

## Source Files

- `server/services/combat_configuration_service.py`
- `server/services/combat_monitoring_service.py`
- `server/services/feature_flag_service.py`
- `server/tests/unit/services/test_feature_flag_service.py`

## Audit Trail

- EXTRACTED: 138 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*