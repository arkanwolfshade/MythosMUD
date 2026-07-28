# Server Services (85)

> 15 nodes

## Key Concepts

- **test_feature_flag_service.py** (10 connections) — `server/tests/unit/services/test_feature_flag_service.py`
- **.get_combat_configuration()** (8 connections) — `server/services/feature_flag_service.py`
- **is_combat_enabled()** (8 connections) — `server/services/feature_flag_service.py`
- **.get_feature_status()** (7 connections) — `server/services/feature_flag_service.py`
- **is_combat_logging_enabled()** (6 connections) — `server/services/feature_flag_service.py`
- **is_combat_monitoring_enabled()** (6 connections) — `server/services/feature_flag_service.py`
- **.validate_combat_requirements()** (5 connections) — `server/services/feature_flag_service.py`
- **.check_combat_availability()** (4 connections) — `server/services/feature_flag_service.py`
- **Convenience function to check if combat is enabled.      Returns:         bool:** (3 connections) — `server/services/feature_flag_service.py`
- **Any** (2 connections)
- **Get all combat-related configuration settings.          Returns:             Dic** (1 connections) — `server/services/feature_flag_service.py`
- **Validate that all combat requirements are met.          Returns:             boo** (1 connections) — `server/services/feature_flag_service.py`
- **Get status of all feature flags.          Returns:             Dict[str, Dict[st** (1 connections) — `server/services/feature_flag_service.py`
- **Check if combat is available for a specific player or globally.          Args:** (1 connections) — `server/services/feature_flag_service.py`
- **Unit tests for feature flag service.  Tests the FeatureFlagService class and glo** (1 connections) — `server/tests/unit/services/test_feature_flag_service.py`

## Relationships

- [Server Services (79)](Server_Services_%2879%29.md) (5 shared connections)
- [Server Commands](Server_Commands.md) (4 shared connections)
- [Server Services (106)](Server_Services_%28106%29.md) (4 shared connections)
- [Server Config (2)](Server_Config_%282%29.md) (1 shared connections)
- [Server Services (113)](Server_Services_%28113%29.md) (1 shared connections)
- [Server Services (71)](Server_Services_%2871%29.md) (1 shared connections)

## Source Files

- `server/services/feature_flag_service.py`
- `server/tests/unit/services/test_feature_flag_service.py`

## Audit Trail

- EXTRACTED: 64 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*