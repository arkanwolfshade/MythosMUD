# room cache services

> 56 nodes

## Key Concepts

- **MonitoringDashboard** (33 connections) — `server/monitoring/monitoring_dashboard.py`
- **test_monitoring_dashboard.py** (17 connections) — `server/tests/unit/monitoring/test_monitoring_dashboard.py`
- **Alert** (14 connections) — `server/monitoring/monitoring_dashboard.py`
- **LogAggregationStats** (12 connections) — `server/structured_logging/log_aggregator.py`
- **.get_system_health()** (11 connections) — `server/monitoring/monitoring_dashboard.py`
- **_dashboard()** (11 connections) — `server/tests/unit/monitoring/test_monitoring_dashboard.py`
- **SystemHealth** (10 connections) — `server/monitoring/monitoring_dashboard.py`
- **.record_custom_alert()** (10 connections) — `server/monitoring/monitoring_dashboard.py`
- **._generate_recommendations()** (7 connections) — `server/monitoring/monitoring_dashboard.py`
- **.get_monitoring_summary()** (6 connections) — `server/monitoring/monitoring_dashboard.py`
- **.check_alerts()** (6 connections) — `server/monitoring/monitoring_dashboard.py`
- **Any** (6 connections)
- **.record_registry_failure()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **.record_summon_quantity_spike()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **.record_durability_anomaly()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **.export_monitoring_data()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **._get_memory_leak_metrics()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **._calculate_performance_score()** (4 connections) — `server/monitoring/monitoring_dashboard.py`
- **.get_alert_history()** (3 connections) — `server/monitoring/monitoring_dashboard.py`
- **._determine_health_status()** (3 connections) — `server/monitoring/monitoring_dashboard.py`
- **._get_active_users()** (3 connections) — `server/monitoring/monitoring_dashboard.py`
- **._get_system_load()** (3 connections) — `server/monitoring/monitoring_dashboard.py`
- **._get_memory_usage()** (3 connections) — `server/monitoring/monitoring_dashboard.py`
- **._get_disk_usage()** (3 connections) — `server/monitoring/monitoring_dashboard.py`
- **_log_stats()** (3 connections) — `server/tests/unit/monitoring/test_monitoring_dashboard.py`
- *... and 31 more nodes in this community*

## Relationships

- [Magic Spell Service](Magic_Spell_Service.md) (21 shared connections)
- [log structured logging](log_structured_logging.md) (4 shared connections)
- [middleware correlation rationale](middleware_correlation_rationale.md) (3 shared connections)
- [websocket realtime handler](websocket_realtime_handler.md) (2 shared connections)
- [event connection helpers](event_connection_helpers.md) (2 shared connections)
- [nats services service](nats_services_service.md) (1 shared connections)

## Source Files

- `server/monitoring/monitoring_dashboard.py`
- `server/structured_logging/log_aggregator.py`
- `server/tests/unit/monitoring/test_monitoring_dashboard.py`

## Audit Trail

- EXTRACTED: 211 (90%)
- INFERRED: 24 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*