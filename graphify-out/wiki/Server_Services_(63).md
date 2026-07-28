# Server Services (63)

> 25 nodes

## Key Concepts

- **CombatConfiguration** (31 connections) — `server/services/combat_configuration_service.py`
- **TestCombatConfiguration** (19 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **.test_init_defaults()** (3 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **.test_init_custom_values()** (3 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **.test_to_dict()** (3 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **.test_validate_valid()** (3 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **.test_validate_invalid_tick_interval_too_low()** (3 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **.test_validate_invalid_tick_interval_too_high()** (3 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **.test_validate_invalid_timeout_too_low()** (3 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **.test_validate_invalid_timeout_too_high()** (3 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **.test_validate_invalid_xp_multiplier_too_low()** (3 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **.test_validate_invalid_xp_multiplier_too_high()** (3 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **.test_validate_invalid_alert_threshold()** (3 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **.test_validate_invalid_max_participants()** (3 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **Test validate catches tick interval too low.** (2 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **Test validate catches timeout too low.** (2 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **Test validate catches XP multiplier too low.** (2 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **Combat configuration data class.** (1 connections) — `server/services/combat_configuration_service.py`
- **Test suite for CombatConfiguration dataclass.** (1 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **Test CombatConfiguration initialization with defaults.** (1 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **Test CombatConfiguration initialization with custom values.** (1 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **Test to_dict converts configuration to dictionary.** (1 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **Test validate returns empty list for valid configuration.** (1 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **Test validate catches alert threshold out of range.** (1 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **Test validate catches max participants out of range.** (1 connections) — `server/tests/unit/services/test_combat_configuration_service.py`

## Relationships

- [Server Services (54)](Server_Services_%2854%29.md) (7 shared connections)
- [Server Services (75)](Server_Services_%2875%29.md) (6 shared connections)
- [Server Services (104)](Server_Services_%28104%29.md) (4 shared connections)
- [Server Services (84)](Server_Services_%2884%29.md) (4 shared connections)
- [Server Commands](Server_Commands.md) (1 shared connections)

## Source Files

- `server/services/combat_configuration_service.py`
- `server/tests/unit/services/test_combat_configuration_service.py`

## Audit Trail

- EXTRACTED: 89 (89%)
- INFERRED: 11 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*