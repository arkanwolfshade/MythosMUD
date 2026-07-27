# Combat Monitoring Service

> 55 nodes · cohesion 0.05

## Key Concepts

- **CombatMonitoringService** (31 connections) — `server/services/combat_monitoring_service.py`
- **Any** (9 connections) — `server/services/combat_monitoring_service.py`
- **._generate_alert()** (9 connections) — `server/services/combat_monitoring_service.py`
- **.to_dict()** (7 connections) — `server/services/combat_monitoring_service.py`
- **Alert** (5 connections) — `server/services/combat_monitoring_service.py`
- **._check_error_threshold()** (4 connections) — `server/services/combat_monitoring_service.py`
- **._check_resource_thresholds()** (4 connections) — `server/services/combat_monitoring_service.py`
- **.get_active_alerts()** (4 connections) — `server/services/combat_monitoring_service.py`
- **.get_all_alerts()** (4 connections) — `server/services/combat_monitoring_service.py`
- **.get_metrics_history()** (4 connections) — `server/services/combat_monitoring_service.py`
- **.get_monitoring_summary()** (4 connections) — `server/services/combat_monitoring_service.py`
- **.record_combat_error()** (4 connections) — `server/services/combat_monitoring_service.py`
- **.to_dict()** (3 connections) — `server/services/combat_monitoring_service.py`
- **.add_alert_callback()** (3 connections) — `server/services/combat_monitoring_service.py`
- **._check_performance_threshold()** (3 connections) — `server/services/combat_monitoring_service.py`
- **.end_combat_monitoring()** (3 connections) — `server/services/combat_monitoring_service.py`
- **.end_turn_monitoring()** (3 connections) — `server/services/combat_monitoring_service.py`
- **.refresh_configuration()** (3 connections) — `server/services/combat_monitoring_service.py`
- **.remove_alert_callback()** (3 connections) — `server/services/combat_monitoring_service.py`
- **.update_resource_metrics()** (3 connections) — `server/services/combat_monitoring_service.py`
- **._update_timing_metrics()** (3 connections) — `server/services/combat_monitoring_service.py`
- **._update_turn_timing_metrics()** (3 connections) — `server/services/combat_monitoring_service.py`
- **monitoring_service()** (3 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_record_combat_error_disabled()** (3 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- **test_start_combat_monitoring_disabled()** (3 connections) — `server/tests/unit/services/test_combat_monitoring_service.py`
- *... and 30 more nodes in this community*

## Relationships

- [[Services Combat Service]] (9 shared connections)
- [[Combat Monitoring Service]] (5 shared connections)
- [[NPC Admin API]] (1 shared connections)

## Source Files

- `server/services/combat_monitoring_service.py`
- `server/tests/unit/services/test_combat_monitoring_service.py`

## Audit Trail

- EXTRACTED: 163 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
