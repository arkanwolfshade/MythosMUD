# FeatureFlagService

> 51 nodes

## Key Concepts

- **FeatureFlagService** (36 connections) — `server/services/feature_flag_service.py`
- **TestFeatureFlagService** (23 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.__init__()** (3 connections) — `server/services/feature_flag_service.py`
- **.test_init()** (3 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.test_is_combat_enabled_true()** (3 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.test_is_combat_enabled_false()** (3 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.test_is_combat_enabled_caching()** (3 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.test_is_combat_logging_enabled_true()** (3 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.test_is_combat_logging_enabled_false()** (3 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.test_is_combat_monitoring_enabled_true()** (3 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.test_is_combat_monitoring_enabled_false()** (3 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.test_get_combat_configuration()** (3 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.test_clear_cache()** (3 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.test_validate_combat_requirements_disabled()** (3 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.test_validate_combat_requirements_valid()** (3 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.test_validate_combat_requirements_invalid_tick_interval()** (3 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.test_validate_combat_requirements_invalid_timeout()** (3 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.test_validate_combat_requirements_invalid_xp_multiplier()** (3 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.test_get_feature_status()** (3 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.test_check_combat_availability_enabled()** (3 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.test_check_combat_availability_disabled()** (3 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.test_check_combat_availability_invalid_requirements()** (3 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.test_check_combat_availability_with_player_id()** (3 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.is_combat_enabled()** (2 connections) — `server/services/feature_flag_service.py`
- **.is_combat_logging_enabled()** (2 connections) — `server/services/feature_flag_service.py`
- *... and 26 more nodes in this community*

## Relationships

- [. init ()](_init_%28%29.md) (11 shared connections)
- [initialize nats and combat services()](initialize_nats_and_combat_services%28%29.md) (1 shared connections)

## Source Files

- `server/services/feature_flag_service.py`
- `server/tests/unit/services/test_feature_flag_service.py`

## Audit Trail

- EXTRACTED: 150 (97%)
- INFERRED: 4 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*