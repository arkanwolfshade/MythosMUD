# Help and WebSocket Core

> 61 nodes

## Key Concepts

- **MonitoringDashboard** (33 connections) — `server/monitoring/monitoring_dashboard.py`
- **monitoring_dashboard.py** (25 connections) — `server/monitoring/monitoring_dashboard.py`
- **Alert** (14 connections) — `server/monitoring/monitoring_dashboard.py`
- **ExceptionStats** (12 connections) — `server/monitoring/exception_tracker.py`
- **__init__.py** (11 connections) — `server/monitoring/__init__.py`
- **.get_system_health()** (11 connections) — `server/monitoring/monitoring_dashboard.py`
- **PerformanceStats** (11 connections) — `server/monitoring/performance_monitor.py`
- **LogAggregationStats** (10 connections) — `server/structured_logging/log_aggregator.py`
- **.record_custom_alert()** (9 connections) — `server/monitoring/monitoring_dashboard.py`
- **__getattr__()** (8 connections) — `server/monitoring/__init__.py`
- **SystemHealth** (8 connections) — `server/monitoring/monitoring_dashboard.py`
- **.check_alerts()** (8 connections) — `server/monitoring/monitoring_dashboard.py`
- **MonitoringSummary** (7 connections) — `server/monitoring/monitoring_dashboard.py`
- **._generate_recommendations()** (7 connections) — `server/monitoring/monitoring_dashboard.py`
- **.get_monitoring_summary()** (6 connections) — `server/monitoring/monitoring_dashboard.py`
- **Any** (6 connections)
- **.record_registry_failure()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **.record_summon_quantity_spike()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **.record_durability_anomaly()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **.export_monitoring_data()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **._get_memory_leak_metrics()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **._calculate_performance_score()** (4 connections) — `server/monitoring/monitoring_dashboard.py`
- **._make_rate_alert()** (3 connections) — `server/monitoring/monitoring_dashboard.py`
- **._make_performance_alert()** (3 connections) — `server/monitoring/monitoring_dashboard.py`
- **.resolve_alert()** (3 connections) — `server/monitoring/monitoring_dashboard.py`
- *... and 36 more nodes in this community*

## Relationships

- [Docker PostgreSQL Typo Bug](Docker_PostgreSQL_Typo_Bug.md) (13 shared connections)
- [Memory Leak Metrics](Memory_Leak_Metrics.md) (8 shared connections)
- [Room Occupant Manager Tests](Room_Occupant_Manager_Tests.md) (5 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (4 shared connections)
- [Monitoring Bundle Services](Monitoring_Bundle_Services.md) (4 shared connections)
- [Merge Refactoring Summary](Merge_Refactoring_Summary.md) (3 shared connections)
- [Client Event Store](Client_Event_Store.md) (3 shared connections)
- [Realtime Errors Error](Realtime_Errors_Error.md) (3 shared connections)
- [Magic Command Handlers](Magic_Command_Handlers.md) (2 shared connections)
- [Auth Token Utilities](Auth_Token_Utilities.md) (1 shared connections)
- [Spell Effect Protocols](Spell_Effect_Protocols.md) (1 shared connections)

## Source Files

- `server/monitoring/__init__.py`
- `server/monitoring/exception_tracker.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/monitoring/performance_monitor.py`
- `server/structured_logging/log_aggregator.py`

## Audit Trail

- EXTRACTED: 233 (85%)
- INFERRED: 40 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*