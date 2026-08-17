# performancestats

> 62 nodes

## Key Concepts

- **MonitoringDashboard** (35 connections) — `server/monitoring/monitoring_dashboard.py`
- **test_monitoring_dashboard.py** (17 connections) — `server/tests/unit/monitoring/test_monitoring_dashboard.py`
- **Alert** (12 connections) — `server/monitoring/monitoring_dashboard.py`
- **.get_system_health()** (11 connections) — `server/monitoring/monitoring_dashboard.py`
- **_dashboard()** (11 connections) — `server/tests/unit/monitoring/test_monitoring_dashboard.py`
- **LogAggregationStats** (10 connections) — `server/structured_logging/log_aggregator.py`
- **.record_custom_alert()** (9 connections) — `server/monitoring/monitoring_dashboard.py`
- **.check_alerts()** (7 connections) — `server/monitoring/monitoring_dashboard.py`
- **._generate_recommendations()** (7 connections) — `server/monitoring/monitoring_dashboard.py`
- **MonitoringSummary** (6 connections) — `server/monitoring/monitoring_dashboard.py`
- **SystemHealth** (6 connections) — `server/monitoring/monitoring_dashboard.py`
- **.get_monitoring_summary()** (6 connections) — `server/monitoring/monitoring_dashboard.py`
- **Any** (6 connections)
- **.export_monitoring_data()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **.record_durability_anomaly()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **.record_registry_failure()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **.record_summon_quantity_spike()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **._calculate_performance_score()** (4 connections) — `server/monitoring/monitoring_dashboard.py`
- **._get_memory_leak_metrics()** (4 connections) — `server/monitoring/monitoring_dashboard.py`
- **._determine_health_status()** (3 connections) — `server/monitoring/monitoring_dashboard.py`
- **._get_active_users()** (3 connections) — `server/monitoring/monitoring_dashboard.py`
- **.get_alert_history()** (3 connections) — `server/monitoring/monitoring_dashboard.py`
- **._get_disk_usage()** (3 connections) — `server/monitoring/monitoring_dashboard.py`
- **._get_memory_usage()** (3 connections) — `server/monitoring/monitoring_dashboard.py`
- **._get_system_load()** (3 connections) — `server/monitoring/monitoring_dashboard.py`
- *... and 37 more nodes in this community*

## Relationships

- [server api monitoring models](server_api_monitoring_models.md) (7 shared connections)
- [docs examples logging websocket integration](docs_examples_logging_websocket_integration.md) (4 shared connections)
- [server monitoring init getattr](server_monitoring_init_getattr.md) (4 shared connections)
- [logentry](logentry.md) (4 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (3 shared connections)
- [docs examples logging correct patterns](docs_examples_logging_correct_patterns.md) (3 shared connections)
- [server monitoring memory leak metrics](server_monitoring_memory_leak_metrics.md) (1 shared connections)
- [abstractcontextmanager](abstractcontextmanager.md) (1 shared connections)

## Source Files

- `server/monitoring/monitoring_dashboard.py`
- `server/structured_logging/log_aggregator.py`
- `server/tests/unit/monitoring/test_monitoring_dashboard.py`

## Audit Trail

- EXTRACTED: 120 (88%)
- INFERRED: 16 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*