# CombatConfiguration

> 34 nodes

## Key Concepts

- **CombatConfiguration** (26 connections) — `server/services/combat_configuration_service.py`
- **TestCombatConfiguration** (19 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **.get_combat_configuration()** (3 connections) — `server/services/combat_configuration_service.py`
- **.test_init_custom_values()** (3 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **.test_init_defaults()** (3 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **.test_to_dict()** (3 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **.test_validate_invalid_alert_threshold()** (3 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **.test_validate_invalid_max_participants()** (3 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **.test_validate_invalid_tick_interval_too_high()** (3 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **.test_validate_invalid_tick_interval_too_low()** (3 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **.test_validate_invalid_timeout_too_high()** (3 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **.test_validate_invalid_timeout_too_low()** (3 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **.test_validate_invalid_xp_multiplier_too_high()** (3 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **.test_validate_invalid_xp_multiplier_too_low()** (3 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **.test_validate_valid()** (3 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **.test_validate_configuration_custom()** (3 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **.validate()** (2 connections) — `server/services/combat_configuration_service.py`
- **Get current combat configuration. Returns: CombatConfiguration: Current combat…** (1 connections) — `server/services/combat_configuration_service.py`
- **Combat configuration data class.** (1 connections) — `server/services/combat_configuration_service.py`
- **Validate configuration and return list of errors.** (1 connections) — `server/services/combat_configuration_service.py`
- **Test validate catches XP multiplier too high.** (1 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **Test validate catches alert threshold out of range.** (1 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **Test validate catches max participants out of range.** (1 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **Test suite for CombatConfiguration dataclass.** (1 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **Test CombatConfiguration initialization with defaults.** (1 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- *... and 9 more nodes in this community*

## Relationships

- [combat_monitoring_service.py](combat_monitoring_service.py.md) (7 shared connections)
- [.update_combat_configuration](update_combat_configuration.md) (4 shared connections)
- [.get_combat_configuration_for_scope](get_combat_configuration_for_scope.md) (3 shared connections)
- [TestCombatConfigurationService](TestCombatConfigurationService.md) (2 shared connections)

## Source Files

- `server/services/combat_configuration_service.py`
- `server/tests/unit/services/test_combat_configuration_service.py`

## Audit Trail

- EXTRACTED: 56 (92%)
- INFERRED: 5 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*