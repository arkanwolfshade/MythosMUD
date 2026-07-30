# PerformanceStats

> 71 nodes

## Key Concepts

- **MonitoringDashboard** (31 connections) — `server/monitoring/monitoring_dashboard.py`
- **monitoring_dashboard.py** (25 connections) — `server/monitoring/monitoring_dashboard.py`
- **performance_monitor.py** (20 connections) — `server/monitoring/performance_monitor.py`
- **exception_tracker.py** (18 connections) — `server/monitoring/exception_tracker.py`
- **get_performance_monitor()** (13 connections) — `server/monitoring/performance_monitor.py`
- **ExceptionStats** (12 connections) — `server/monitoring/exception_tracker.py`
- **Alert** (12 connections) — `server/monitoring/monitoring_dashboard.py`
- **__init__.py** (11 connections) — `server/monitoring/__init__.py`
- **.get_system_health()** (11 connections) — `server/monitoring/monitoring_dashboard.py`
- **PerformanceStats** (11 connections) — `server/monitoring/performance_monitor.py`
- **get_exception_tracker()** (10 connections) — `server/monitoring/exception_tracker.py`
- **.record_custom_alert()** (10 connections) — `server/monitoring/monitoring_dashboard.py`
- **LogAggregationStats** (10 connections) — `server/structured_logging/log_aggregator.py`
- **__getattr__()** (8 connections) — `server/monitoring/__init__.py`
- **SystemHealth** (8 connections) — `server/monitoring/monitoring_dashboard.py`
- **MonitoringSummary** (7 connections) — `server/monitoring/monitoring_dashboard.py`
- **._generate_recommendations()** (7 connections) — `server/monitoring/monitoring_dashboard.py`
- **.__init__()** (6 connections) — `server/monitoring/monitoring_dashboard.py`
- **.get_monitoring_summary()** (6 connections) — `server/monitoring/monitoring_dashboard.py`
- **.check_alerts()** (6 connections) — `server/monitoring/monitoring_dashboard.py`
- **Any** (6 connections)
- **.record_registry_failure()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **.record_summon_quantity_spike()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **.record_durability_anomaly()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **.export_monitoring_data()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- *... and 46 more nodes in this community*

## Relationships

- [nats retry handler](nats_retry_handler.md) (11 shared connections)
- [. is npc in combat()](_is_npc_in_combat%28%29.md) (11 shared connections)
- [world](world.md) (10 shared connections)
- [.shutdown()](shutdown%28%29.md) (7 shared connections)
- [Any](Any.md) (7 shared connections)
- [aggregate log entry()](aggregate_log_entry%28%29.md) (6 shared connections)
- [init](init.md) (5 shared connections)
- [Send a system message to](Send_a_system_message_to.md) (4 shared connections)
- [Lock](Lock.md) (3 shared connections)
- [item](item.md) (2 shared connections)
- [testing examples](testing_examples.md) (2 shared connections)
- [websocket integration](websocket_integration.md) (2 shared connections)

## Source Files

- `server/monitoring/__init__.py`
- `server/monitoring/exception_tracker.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/monitoring/performance_monitor.py`
- `server/structured_logging/log_aggregator.py`

## Audit Trail

- EXTRACTED: 298 (88%)
- INFERRED: 42 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*