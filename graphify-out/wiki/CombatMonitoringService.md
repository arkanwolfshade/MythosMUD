# CombatMonitoringService

> 62 nodes

## Key Concepts

- **CombatMonitoringService** (32 connections) — `server/services/combat_monitoring_service.py`
- **._generate_alert()** (9 connections) — `server/services/combat_monitoring_service.py`
- **Any** (9 connections)
- **.__init__()** (7 connections) — `server/services/combat_monitoring_service.py`
- **Alert** (5 connections) — `server/services/combat_monitoring_service.py`
- **._check_error_threshold()** (4 connections) — `server/services/combat_monitoring_service.py`
- **._check_resource_thresholds()** (4 connections) — `server/services/combat_monitoring_service.py`
- **.record_combat_error()** (4 connections) — `server/services/combat_monitoring_service.py`
- **.to_dict()** (3 connections) — `server/services/combat_monitoring_service.py`
- **.to_dict()** (3 connections) — `server/services/combat_monitoring_service.py`
- **.add_alert_callback()** (3 connections) — `server/services/combat_monitoring_service.py`
- **._check_performance_threshold()** (3 connections) — `server/services/combat_monitoring_service.py`
- **.end_combat_monitoring()** (3 connections) — `server/services/combat_monitoring_service.py`
- **.end_turn_monitoring()** (3 connections) — `server/services/combat_monitoring_service.py`
- **.get_active_alerts()** (3 connections) — `server/services/combat_monitoring_service.py`
- **.get_all_alerts()** (3 connections) — `server/services/combat_monitoring_service.py`
- **.get_current_metrics()** (3 connections) — `server/services/combat_monitoring_service.py`
- **.get_metrics_history()** (3 connections) — `server/services/combat_monitoring_service.py`
- **.get_monitoring_summary()** (3 connections) — `server/services/combat_monitoring_service.py`
- **.refresh_configuration()** (3 connections) — `server/services/combat_monitoring_service.py`
- **.remove_alert_callback()** (3 connections) — `server/services/combat_monitoring_service.py`
- **._save_metrics_snapshot()** (3 connections) — `server/services/combat_monitoring_service.py`
- **.update_resource_metrics()** (3 connections) — `server/services/combat_monitoring_service.py`
- **._update_timing_metrics()** (3 connections) — `server/services/combat_monitoring_service.py`
- **._update_turn_timing_metrics()** (3 connections) — `server/services/combat_monitoring_service.py`
- *... and 37 more nodes in this community*

## Relationships

- [test_combat_monitoring_service.py](test_combat_monitoring_service.py.md) (14 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [monitoring_service](monitoring_service.md) (1 shared connections)
- [FeatureFlagService](FeatureFlagService.md) (1 shared connections)
- [CombatConfiguration](CombatConfiguration.md) (1 shared connections)
- [build_event](build_event.md) (1 shared connections)

## Source Files

- `server/services/combat_monitoring_service.py`
- `server/tests/unit/services/test_combat_monitoring_service.py`

## Audit Trail

- EXTRACTED: 93 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*