# npc combat service

> 20 nodes

## Key Concepts

- **combat_configuration_service.py** (17 connections) — `server/services/combat_configuration_service.py`
- **CombatConfigurationError** (11 connections) — `server/services/combat_configuration_service.py`
- **CombatConfigurationScope** (9 connections) — `server/services/combat_configuration_service.py`
- **test_combat_configuration_service.py** (8 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **.clear_scope_override()** (4 connections) — `server/services/combat_configuration_service.py`
- **.test_update_combat_configuration_global_raises()** (3 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **.test_update_combat_configuration_invalid_raises()** (3 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **.test_clear_scope_override_global_raises()** (3 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **Enum** (2 connections)
- **is_combat_available()** (2 connections) — `server/services/combat_configuration_service.py`
- **Exception** (1 connections)
- **Combat configuration management service for MythosMUD.  This service provides ce** (1 connections) — `server/services/combat_configuration_service.py`
- **Exception raised for combat configuration errors.** (1 connections) — `server/services/combat_configuration_service.py`
- **Scope for combat configuration changes.** (1 connections) — `server/services/combat_configuration_service.py`
- **Clear configuration override for a specific scope.          Args:             sc** (1 connections) — `server/services/combat_configuration_service.py`
- **Convenience function to check if combat is available.      Args:         player_** (1 connections) — `server/services/combat_configuration_service.py`
- **Unit tests for combat configuration service.  Tests the CombatConfigurationServi** (1 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **Test update_combat_configuration raises error for global scope.** (1 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **Test update_combat_configuration raises error for invalid config.** (1 connections) — `server/tests/unit/services/test_combat_configuration_service.py`
- **Test clear_scope_override raises error for global scope.** (1 connections) — `server/tests/unit/services/test_combat_configuration_service.py`

## Relationships

- [combat configuration service](combat_configuration_service.md) (15 shared connections)
- [NATS Messaging](NATS_Messaging.md) (3 shared connections)
- [persistence container extended](persistence_container_extended.md) (3 shared connections)
- [service feature services](service_feature_services.md) (2 shared connections)
- [Item Instances](Item_Instances.md) (1 shared connections)
- [event bus events](event_bus_events.md) (1 shared connections)
- [connection helpers realtime](connection_helpers_realtime.md) (1 shared connections)

## Source Files

- `server/services/combat_configuration_service.py`
- `server/tests/unit/services/test_combat_configuration_service.py`

## Audit Trail

- EXTRACTED: 62 (86%)
- INFERRED: 10 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*