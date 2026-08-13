# CombatConfigurationService

> 33 nodes

## Key Concepts

- **CombatConfigurationService** (19 connections) — `server/services/combat_configuration_service.py`
- **.update_combat_configuration()** (8 connections) — `server/services/combat_configuration_service.py`
- **.get_combat_configuration_for_scope()** (7 connections) — `server/services/combat_configuration_service.py`
- **get_combat_configuration()** (7 connections) — `server/services/combat_configuration_service.py`
- **.get_combat_settings_summary()** (6 connections) — `server/services/combat_configuration_service.py`
- **.validate_configuration()** (6 connections) — `server/services/combat_configuration_service.py`
- **.from_dict()** (5 connections) — `server/services/combat_configuration_service.py`
- **.is_combat_available()** (5 connections) — `server/services/combat_configuration_service.py`
- **Any** (5 connections)
- **.get_active_overrides()** (4 connections) — `server/services/combat_configuration_service.py`
- **.__init__()** (4 connections) — `server/services/combat_configuration_service.py`
- **.to_dict()** (3 connections) — `server/services/combat_configuration_service.py`
- **.get_combat_configuration()** (3 connections) — `server/services/combat_configuration_service.py`
- **.refresh_configuration()** (3 connections) — `server/services/combat_configuration_service.py`
- **.test_from_dict()** (3 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **.clear_all_overrides()** (2 connections) — `server/services/combat_configuration_service.py`
- **.clear_cache()** (2 connections) — `server/services/combat_configuration_service.py`
- **Initialize the combat configuration service.** (1 connections) — `server/services/combat_configuration_service.py`
- **Get current combat configuration. Returns: CombatConfiguration: Current combat…** (1 connections) — `server/services/combat_configuration_service.py`
- **Get combat configuration for a specific scope. Args: scope: Configuration scope…** (1 connections) — `server/services/combat_configuration_service.py`
- **Update combat configuration. Args: updates: Dictionary of configuration updates…** (1 connections) — `server/services/combat_configuration_service.py`
- **Clear all configuration overrides.** (1 connections) — `server/services/combat_configuration_service.py`
- **Get all active configuration overrides. Returns: Dict[str, Dict[str, Any]]:…** (1 connections) — `server/services/combat_configuration_service.py`
- **Validate combat configuration. Args: config: Optional configuration to validate…** (1 connections) — `server/services/combat_configuration_service.py`
- **Check if combat is available for a specific player/room. Args: player_id:…** (1 connections) — `server/services/combat_configuration_service.py`
- *... and 8 more nodes in this community*

## Relationships

- [CombatConfiguration](CombatConfiguration.md) (9 shared connections)
- [CombatConfigurationScope](CombatConfigurationScope.md) (5 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [TestCombatConfigurationService](TestCombatConfigurationService.md) (2 shared connections)
- [FeatureFlagService](FeatureFlagService.md) (1 shared connections)

## Source Files

- `server/services/combat_configuration_service.py`
- `server/tests/unit/services/test_combat_configuration_service.py`

## Audit Trail

- EXTRACTED: 63 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*