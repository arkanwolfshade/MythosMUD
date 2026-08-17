# CombatConfiguration

> 30 nodes

## Key Concepts

- **CombatConfiguration** (26 connections) — `server/services/combat_configuration_service.py`
- **TestCombatConfiguration** (16 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
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
- **.validate()** (2 connections) — `server/services/combat_configuration_service.py`
- **Combat configuration data class.** (1 connections) — `server/services/combat_configuration_service.py`
- **Validate configuration and return list of errors.** (1 connections) — `server/services/combat_configuration_service.py`
- **Test validate catches XP multiplier too high.** (1 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **Test validate catches alert threshold out of range.** (1 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **Test validate catches max participants out of range.** (1 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **Test suite for CombatConfiguration dataclass.** (1 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **Test CombatConfiguration initialization with defaults.** (1 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **Test CombatConfiguration initialization with custom values.** (1 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **Test to_dict converts configuration to dictionary.** (1 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **Test validate returns empty list for valid configuration.** (1 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- *... and 5 more nodes in this community*

## Relationships

- [CombatConfigurationService](CombatConfigurationService.md) (4 shared connections)
- [.update_combat_configuration](update_combat_configuration.md) (4 shared connections)
- [TestCombatConfigurationService](TestCombatConfigurationService.md) (2 shared connections)
- [test_combat_configuration_service.py](test_combat_configuration_service.py.md) (2 shared connections)
- [FeatureFlagService](FeatureFlagService.md) (1 shared connections)

## Source Files

- `server/services/combat_configuration_service.py`
- `server/tests/unit/services/test_combat_configuration_service.py`

## Audit Trail

- EXTRACTED: 52 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*