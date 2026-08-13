# CombatMonitoringService

> 28 nodes

## Key Concepts

- **CombatMonitoringService** (31 connections) — `server/services/combat_monitoring_service.py`
- **.end_combat_monitoring()** (3 connections) — `server/services/combat_monitoring_service.py`
- **.end_turn_monitoring()** (3 connections) — `server/services/combat_monitoring_service.py`
- **.get_current_metrics()** (3 connections) — `server/services/combat_monitoring_service.py`
- **.refresh_configuration()** (3 connections) — `server/services/combat_monitoring_service.py`
- **._save_metrics_snapshot()** (3 connections) — `server/services/combat_monitoring_service.py`
- **._update_timing_metrics()** (3 connections) — `server/services/combat_monitoring_service.py`
- **._update_turn_timing_metrics()** (3 connections) — `server/services/combat_monitoring_service.py`
- **test_record_combat_error_disabled()** (3 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_start_combat_monitoring_disabled()** (3 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **.clear_resolved_alerts()** (2 connections) — `server/services/combat_monitoring_service.py`
- **.resolve_alert()** (2 connections) — `server/services/combat_monitoring_service.py`
- **.start_combat_monitoring()** (2 connections) — `server/services/combat_monitoring_service.py`
- **.start_turn_monitoring()** (2 connections) — `server/services/combat_monitoring_service.py`
- **Comprehensive combat monitoring and alerting service. Tracks combat system…** (1 connections) — `server/services/combat_monitoring_service.py`
- **Start monitoring a combat instance. Args: combat_id: Unique combat identifier** (1 connections) — `server/services/combat_monitoring_service.py`
- **End monitoring a combat instance. Args: combat_id: Unique combat identifier…** (1 connections) — `server/services/combat_monitoring_service.py`
- **Start monitoring a combat turn. Args: combat_id: Unique combat identifier** (1 connections) — `server/services/combat_monitoring_service.py`
- **End monitoring a combat turn. Args: combat_id: Unique combat identifier** (1 connections) — `server/services/combat_monitoring_service.py`
- **Get current combat metrics. Returns: CombatMetrics: Current metrics** (1 connections) — `server/services/combat_monitoring_service.py`
- **Resolve an alert. Args: alert_id: Alert identifier Returns: bool: True if alert…** (1 connections) — `server/services/combat_monitoring_service.py`
- **Clear resolved alerts. Returns: int: Number of alerts cleared** (1 connections) — `server/services/combat_monitoring_service.py`
- **Update timing metrics with new combat duration.** (1 connections) — `server/services/combat_monitoring_service.py`
- **Update turn timing metrics.** (1 connections) — `server/services/combat_monitoring_service.py`
- **Save current metrics as a snapshot.** (1 connections) — `server/services/combat_monitoring_service.py`
- *... and 3 more nodes in this community*

## Relationships

- [Any](Any.md) (6 shared connections)
- [get_logger](get_logger.md) (5 shared connections)
- [._generate_alert](_generate_alert.md) (4 shared connections)
- [test_combat_monitoring_service.py](test_combat_monitoring_service.py.md) (3 shared connections)
- [Alert](Alert.md) (2 shared connections)
- [monitoring_service](monitoring_service.md) (1 shared connections)
- [get_combat_monitoring](get_combat_monitoring.md) (1 shared connections)

## Source Files

- `server/services/combat_monitoring_service.py`
- `server/tests/unit/services/test_combat_monitoring_service.py`

## Audit Trail

- EXTRACTED: 51 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*