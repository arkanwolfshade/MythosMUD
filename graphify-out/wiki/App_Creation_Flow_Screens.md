# App Creation Flow Screens

> 18 nodes · cohesion 0.12

## Key Concepts

- **CombatMetrics** (11 connections) — `server/services/combat_monitoring_service.py`
- **.__init__()** (8 connections) — `server/services/combat_monitoring_service.py`
- **get_combat_metrics()** (6 connections) — `server/services/combat_monitoring_service.py`
- **get_combat_config()** (5 connections) — `server/services/combat_configuration_service.py`
- **.get_current_metrics()** (4 connections) — `server/services/combat_monitoring_service.py`
- **test_get_combat_metrics()** (4 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **._save_metrics_snapshot()** (3 connections) — `server/services/combat_monitoring_service.py`
- **test_combat_monitoring_service_init()** (3 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_get_current_metrics()** (3 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **Get the global combat configuration service instance.      Returns:         Comb** (1 connections) — `server/services/combat_configuration_service.py`
- **Initialize the combat monitoring service.** (1 connections) — `server/services/combat_monitoring_service.py`
- **Get current combat metrics.          Returns:             CombatMetrics: Current** (1 connections) — `server/services/combat_monitoring_service.py`
- **Combat system metrics.** (1 connections) — `server/services/combat_monitoring_service.py`
- **Save current metrics as a snapshot.** (1 connections) — `server/services/combat_monitoring_service.py`
- **Convenience function to get current combat metrics.      Returns:         Combat** (1 connections) — `server/services/combat_monitoring_service.py`
- **Test get_current_metrics returns metrics.** (1 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **Test get_combat_metrics returns metrics.** (1 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **Test CombatMonitoringService initialization.** (1 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`

## Relationships

- [Combat Monitoring Service](Combat_Monitoring_Service.md) (8 shared connections)
- [Circuit Breaker Core](Circuit_Breaker_Core.md) (5 shared connections)
- [Combat Configuration Service](Combat_Configuration_Service.md) (2 shared connections)
- [Mythos Map Builder](Mythos_Map_Builder.md) (1 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (1 shared connections)
- [Combat Feature Flags](Combat_Feature_Flags.md) (1 shared connections)

## Source Files

- `server/services/combat_configuration_service.py`
- `server/services/combat_monitoring_service.py`
- `server/tests/unit/services/test_combat_monitoring_service.py`

## Audit Trail

- EXTRACTED: 48 (86%)
- INFERRED: 8 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*