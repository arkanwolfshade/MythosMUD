# .to dict()

> 66 nodes

## Key Concepts

- **CombatMonitoringService** (32 connections) — `server/services/combat_monitoring_service.py`
- **combat_monitoring_service.py** (21 connections) — `server/services/combat_monitoring_service.py`
- **Any** (9 connections)
- **._generate_alert()** (9 connections) — `server/services/combat_monitoring_service.py`
- **.to_dict()** (7 connections) — `server/services/combat_monitoring_service.py`
- **Alert** (6 connections) — `server/services/combat_monitoring_service.py`
- **AlertSeverity** (5 connections) — `server/services/combat_monitoring_service.py`
- **AlertType** (5 connections) — `server/services/combat_monitoring_service.py`
- **get_combat_monitoring()** (5 connections) — `server/services/combat_monitoring_service.py`
- **.record_combat_error()** (4 connections) — `server/services/combat_monitoring_service.py`
- **.get_metrics_history()** (4 connections) — `server/services/combat_monitoring_service.py`
- **.get_active_alerts()** (4 connections) — `server/services/combat_monitoring_service.py`
- **.get_all_alerts()** (4 connections) — `server/services/combat_monitoring_service.py`
- **.get_monitoring_summary()** (4 connections) — `server/services/combat_monitoring_service.py`
- **._check_error_threshold()** (4 connections) — `server/services/combat_monitoring_service.py`
- **._check_resource_thresholds()** (4 connections) — `server/services/combat_monitoring_service.py`
- **test_get_combat_monitoring()** (4 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **Enum** (3 connections)
- **.to_dict()** (3 connections) — `server/services/combat_monitoring_service.py`
- **.end_combat_monitoring()** (3 connections) — `server/services/combat_monitoring_service.py`
- **.end_turn_monitoring()** (3 connections) — `server/services/combat_monitoring_service.py`
- **.update_resource_metrics()** (3 connections) — `server/services/combat_monitoring_service.py`
- **.add_alert_callback()** (3 connections) — `server/services/combat_monitoring_service.py`
- **.remove_alert_callback()** (3 connections) — `server/services/combat_monitoring_service.py`
- **._update_timing_metrics()** (3 connections) — `server/services/combat_monitoring_service.py`
- *... and 41 more nodes in this community*

## Relationships

- [test combat monitoring service](test_combat_monitoring_service.md) (9 shared connections)
- [CombatMetrics](CombatMetrics.md) (5 shared connections)
- [. init ()](_init_%28%29.md) (4 shared connections)
- [main()](main%28%29.md) (3 shared connections)
- [initialize nats and combat services()](initialize_nats_and_combat_services%28%29.md) (2 shared connections)
- [combat configuration service](combat_configuration_service.md) (2 shared connections)

## Source Files

- `server/services/combat_monitoring_service.py`
- `server/tests/unit/services/test_combat_monitoring_service.py`

## Audit Trail

- EXTRACTED: 208 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*