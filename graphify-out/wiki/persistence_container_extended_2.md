# persistence container extended

> 28 nodes

## Key Concepts

- **TestCombatConfiguration** (19 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **.test_init_defaults()** (3 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **.test_init_custom_values()** (3 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **.test_to_dict()** (3 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **.test_from_dict()** (3 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **.test_validate_valid()** (3 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **.test_validate_invalid_tick_interval_too_low()** (3 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **.test_validate_invalid_tick_interval_too_high()** (3 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **.test_validate_invalid_timeout_too_low()** (3 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **.test_validate_invalid_timeout_too_high()** (3 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **.test_validate_invalid_xp_multiplier_too_low()** (3 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **.test_validate_invalid_xp_multiplier_too_high()** (3 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **.test_validate_invalid_alert_threshold()** (3 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **.test_validate_invalid_max_participants()** (3 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **Test suite for CombatConfiguration dataclass.** (1 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **Test CombatConfiguration initialization with defaults.** (1 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **Test CombatConfiguration initialization with custom values.** (1 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **Test to_dict converts configuration to dictionary.** (1 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **Test from_dict creates configuration from dictionary.** (1 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **Test validate returns empty list for valid configuration.** (1 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **Test validate catches tick interval too low.** (1 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **Test validate catches tick interval too high.** (1 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **Test validate catches timeout too low.** (1 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **Test validate catches timeout too high.** (1 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **Test validate catches XP multiplier too low.** (1 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- *... and 3 more nodes in this community*

## Relationships

- [combat configuration service](combat_configuration_service.md) (15 shared connections)
- [npc combat service](npc_combat_service.md) (3 shared connections)

## Source Files

- `server/tests/unit/services/test_combat_configuration_service.py`

## Audit Trail

- EXTRACTED: 68 (94%)
- INFERRED: 4 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*