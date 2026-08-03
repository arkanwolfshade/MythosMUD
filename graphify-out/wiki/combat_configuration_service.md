# combat configuration service

> 29 nodes

## Key Concepts

- **CombatConfiguration** (31 connections) — `server/services/combat_configuration_service.py`
- **CombatConfigurationService** (19 connections) — `server/services/combat_configuration_service.py`
- **.update_combat_configuration()** (10 connections) — `server/services/combat_configuration_service.py`
- **.to_dict()** (7 connections) — `server/services/combat_configuration_service.py`
- **.get_combat_configuration_for_scope()** (7 connections) — `server/services/combat_configuration_service.py`
- **.validate_configuration()** (7 connections) — `server/services/combat_configuration_service.py`
- **.get_combat_settings_summary()** (7 connections) — `server/services/combat_configuration_service.py`
- **get_combat_configuration()** (7 connections) — `server/services/combat_configuration_service.py`
- **Any** (5 connections)
- **.from_dict()** (5 connections) — `server/services/combat_configuration_service.py`
- **.get_active_overrides()** (5 connections) — `server/services/combat_configuration_service.py`
- **.is_combat_available()** (5 connections) — `server/services/combat_configuration_service.py`
- **.validate()** (4 connections) — `server/services/combat_configuration_service.py`
- **.get_combat_configuration()** (4 connections) — `server/services/combat_configuration_service.py`
- **.clear_all_overrides()** (2 connections) — `server/services/combat_configuration_service.py`
- **Combat configuration data class.** (1 connections) — `server/services/combat_configuration_service.py`
- **Convert to dictionary.** (1 connections) — `server/services/combat_configuration_service.py`
- **Create from dictionary.** (1 connections) — `server/services/combat_configuration_service.py`
- **Validate configuration and return list of errors.** (1 connections) — `server/services/combat_configuration_service.py`
- **Centralized combat configuration management service.      Provides type-safe acc** (1 connections) — `server/services/combat_configuration_service.py`
- **Get current combat configuration.          Returns:             CombatConfigurat** (1 connections) — `server/services/combat_configuration_service.py`
- **Get combat configuration for a specific scope.          Args:             scope:** (1 connections) — `server/services/combat_configuration_service.py`
- **Update combat configuration.          Args:             updates: Dictionary of c** (1 connections) — `server/services/combat_configuration_service.py`
- **Clear all configuration overrides.** (1 connections) — `server/services/combat_configuration_service.py`
- **Get all active configuration overrides.          Returns:             Dict[str,** (1 connections) — `server/services/combat_configuration_service.py`
- *... and 4 more nodes in this community*

## Relationships

- [persistence container extended](persistence_container_extended.md) (15 shared connections)
- [npc combat service](npc_combat_service.md) (9 shared connections)
- [combat configuration service](combat_configuration_service.md) (9 shared connections)
- [connection helpers realtime](connection_helpers_realtime.md) (2 shared connections)
- [Item Instances](Item_Instances.md) (1 shared connections)
- [event bus events](event_bus_events.md) (1 shared connections)

## Source Files

- `server/services/combat_configuration_service.py`

## Audit Trail

- EXTRACTED: 130 (94%)
- INFERRED: 9 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*