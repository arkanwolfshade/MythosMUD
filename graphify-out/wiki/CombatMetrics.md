# CombatMetrics

> 14 nodes

## Key Concepts

- **CombatMetrics** (11 connections) — `server/services/combat_monitoring_service.py`
- **get_combat_metrics()** (6 connections) — `server/services/combat_monitoring_service.py`
- **.get_current_metrics()** (4 connections) — `server/services/combat_monitoring_service.py`
- **test_get_combat_metrics()** (4 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **._save_metrics_snapshot()** (3 connections) — `server/services/combat_monitoring_service.py`
- **test_combat_monitoring_service_init()** (3 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_get_current_metrics()** (3 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **Combat system metrics.** (1 connections) — `server/services/combat_monitoring_service.py`
- **Get current combat metrics.          Returns:             CombatMetrics: Current** (1 connections) — `server/services/combat_monitoring_service.py`
- **Save current metrics as a snapshot.** (1 connections) — `server/services/combat_monitoring_service.py`
- **Convenience function to get current combat metrics.      Returns:         Combat** (1 connections) — `server/services/combat_monitoring_service.py`
- **Test CombatMonitoringService initialization.** (1 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **Test get_current_metrics returns metrics.** (1 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **Test get_combat_metrics returns metrics.** (1 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`

## Relationships

- [.to dict()](to_dict%28%29.md) (5 shared connections)
- [test combat monitoring service](test_combat_monitoring_service.md) (5 shared connections)
- [. init ()](_init_%28%29.md) (1 shared connections)

## Source Files

- `server/services/combat_monitoring_service.py`
- `server/tests/unit/services/test_combat_monitoring_service.py`

## Audit Trail

- EXTRACTED: 35 (85%)
- INFERRED: 6 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*