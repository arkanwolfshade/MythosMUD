# CombatConfigurationService

> 18 nodes

## Key Concepts

- **CombatConfigurationService** (18 connections) — `server/services/combat_configuration_service.py`
- **.get_combat_configuration_for_scope()** (7 connections) — `server/services/combat_configuration_service.py`
- **get_combat_configuration()** (7 connections) — `server/services/combat_configuration_service.py`
- **.validate_configuration()** (6 connections) — `server/services/combat_configuration_service.py`
- **.is_combat_available()** (5 connections) — `server/services/combat_configuration_service.py`
- **.get_combat_configuration()** (3 connections) — `server/services/combat_configuration_service.py`
- **.refresh_configuration()** (3 connections) — `server/services/combat_configuration_service.py`
- **.clear_all_overrides()** (2 connections) — `server/services/combat_configuration_service.py`
- **.clear_cache()** (2 connections) — `server/services/combat_configuration_service.py`
- **Get current combat configuration. Returns: CombatConfiguration: Current combat…** (1 connections) — `server/services/combat_configuration_service.py`
- **Get combat configuration for a specific scope. Args: scope: Configuration scope…** (1 connections) — `server/services/combat_configuration_service.py`
- **Clear all configuration overrides.** (1 connections) — `server/services/combat_configuration_service.py`
- **Validate combat configuration. Args: config: Optional configuration to validate…** (1 connections) — `server/services/combat_configuration_service.py`
- **Check if combat is available for a specific player/room. Args: player_id:…** (1 connections) — `server/services/combat_configuration_service.py`
- **Refresh configuration from source.** (1 connections) — `server/services/combat_configuration_service.py`
- **Clear configuration cache.** (1 connections) — `server/services/combat_configuration_service.py`
- **Convenience function to get current combat configuration. Returns:…** (1 connections) — `server/services/combat_configuration_service.py`
- **Centralized combat configuration management service. Provides type-safe access…** (1 connections) — `server/services/combat_configuration_service.py`

## Relationships

- [.update_combat_configuration](update_combat_configuration.md) (6 shared connections)
- [FeatureFlagService](FeatureFlagService.md) (4 shared connections)
- [CombatConfiguration](CombatConfiguration.md) (4 shared connections)
- [test_combat_configuration_service.py](test_combat_configuration_service.py.md) (3 shared connections)
- [.service](service.md) (1 shared connections)
- [TestCombatConfigurationService](TestCombatConfigurationService.md) (1 shared connections)
- [AsyncPersistenceLayer](AsyncPersistenceLayer.md) (1 shared connections)

## Source Files

- `server/services/combat_configuration_service.py`

## Audit Trail

- EXTRACTED: 40 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*