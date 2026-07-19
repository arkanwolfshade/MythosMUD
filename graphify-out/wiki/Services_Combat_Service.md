# Services Combat Service

> 24 nodes · cohesion 0.09

## Key Concepts

- **combat_monitoring_service.py** (16 connections) — `server/services/combat_monitoring_service.py`
- **CombatMetrics** (8 connections) — `server/services/combat_monitoring_service.py`
- **.__init__()** (7 connections) — `server/services/combat_monitoring_service.py`
- **get_combat_metrics()** (6 connections) — `server/services/combat_monitoring_service.py`
- **AlertSeverity** (5 connections) — `server/services/combat_monitoring_service.py`
- **AlertType** (5 connections) — `server/services/combat_monitoring_service.py`
- **.get_current_metrics()** (4 connections) — `server/services/combat_monitoring_service.py`
- **._save_metrics_snapshot()** (3 connections) — `server/services/combat_monitoring_service.py`
- **record_combat_error()** (3 connections) — `server/services/combat_monitoring_service.py`
- **test_get_combat_metrics()** (3 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **end_combat_monitoring()** (2 connections) — `server/services/combat_monitoring_service.py`
- **start_combat_monitoring()** (2 connections) — `server/services/combat_monitoring_service.py`
- **Combat monitoring and alerting service for MythosMUD.  This service provides com** (1 connections) — `server/services/combat_monitoring_service.py`
- **Initialize the combat monitoring service.** (1 connections) — `server/services/combat_monitoring_service.py`
- **Get current combat metrics.          Returns:             CombatMetrics: Current** (1 connections) — `server/services/combat_monitoring_service.py`
- **Alert severity levels.** (1 connections) — `server/services/combat_monitoring_service.py`
- **Alert types for combat monitoring.** (1 connections) — `server/services/combat_monitoring_service.py`
- **Combat system metrics.** (1 connections) — `server/services/combat_monitoring_service.py`
- **Save current metrics as a snapshot.** (1 connections) — `server/services/combat_monitoring_service.py`
- **Convenience function to start combat monitoring.      Args:         combat_id: U** (1 connections) — `server/services/combat_monitoring_service.py`
- **Convenience function to end combat monitoring.      Args:         combat_id: Uni** (1 connections) — `server/services/combat_monitoring_service.py`
- **Convenience function to record combat error.      Args:         error_type: Type** (1 connections) — `server/services/combat_monitoring_service.py`
- **Convenience function to get current combat metrics.      Returns:         Combat** (1 connections) — `server/services/combat_monitoring_service.py`
- **Test get_combat_metrics returns metrics.** (1 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`

## Relationships

- [[Combat Monitoring Service]] (15 shared connections)
- [[NPC Admin API]] (6 shared connections)
- [[Combat Configuration Service]] (2 shared connections)
- [[Combat Feature Flags]] (2 shared connections)
- [[Message Queue Cleanup]] (1 shared connections)

## Source Files

- `server/services/combat_monitoring_service.py`
- `server/tests/unit/services/test_combat_monitoring_service.py`

## Audit Trail

- EXTRACTED: 75 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
