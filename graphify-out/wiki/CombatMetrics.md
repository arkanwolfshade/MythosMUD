# CombatMetrics

> 14 nodes

## Key Concepts

- **CombatMetrics** (11 connections) — `server/services/combat_monitoring_service.py`
- **get_combat_metrics()** (5 connections) — `server/services/combat_monitoring_service.py`
- **test_get_combat_metrics()** (4 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **.get_current_metrics()** (3 connections) — `server/services/combat_monitoring_service.py`
- **._save_metrics_snapshot()** (3 connections) — `server/services/combat_monitoring_service.py`
- **test_combat_monitoring_service_init()** (3 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_get_current_metrics()** (3 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **Get current combat metrics. Returns: CombatMetrics: Current metrics** (1 connections) — `server/services/combat_monitoring_service.py`
- **Combat system metrics.** (1 connections) — `server/services/combat_monitoring_service.py`
- **Save current metrics as a snapshot.** (1 connections) — `server/services/combat_monitoring_service.py`
- **Convenience function to get current combat metrics. Returns: CombatMetrics:…** (1 connections) — `server/services/combat_monitoring_service.py`
- **Test get_current_metrics returns metrics.** (1 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **Test get_combat_metrics returns metrics.** (1 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **Test CombatMonitoringService initialization.** (1 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`

## Relationships

- [test_combat_monitoring_service.py](test_combat_monitoring_service.py.md) (5 shared connections)
- [FeatureFlagService](FeatureFlagService.md) (3 shared connections)
- [CombatMonitoringService](CombatMonitoringService.md) (2 shared connections)
- [Any](Any.md) (1 shared connections)

## Source Files

- `server/services/combat_monitoring_service.py`
- `server/tests/unit/services/test_combat_monitoring_service.py`

## Audit Trail

- EXTRACTED: 22 (88%)
- INFERRED: 3 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*