# Help and WebSocket Core

> 82 nodes

## Key Concepts

- **MonitoringDashboard** (33 connections) — `server/monitoring/monitoring_dashboard.py`
- **monitoring_dashboard.py** (25 connections) — `server/monitoring/monitoring_dashboard.py`
- **exception_tracker.py** (20 connections) — `server/monitoring/exception_tracker.py`
- **performance_monitor.py** (20 connections) — `server/monitoring/performance_monitor.py`
- **get_monitoring_dashboard()** (19 connections) — `server/monitoring/monitoring_dashboard.py`
- **track_exception()** (14 connections) — `server/monitoring/exception_tracker.py`
- **Alert** (14 connections) — `server/monitoring/monitoring_dashboard.py`
- **get_performance_monitor()** (13 connections) — `server/monitoring/performance_monitor.py`
- **ExceptionStats** (12 connections) — `server/monitoring/exception_tracker.py`
- **__init__.py** (11 connections) — `server/monitoring/__init__.py`
- **.get_system_health()** (11 connections) — `server/monitoring/monitoring_dashboard.py`
- **PerformanceStats** (11 connections) — `server/monitoring/performance_monitor.py`
- **get_exception_tracker()** (10 connections) — `server/monitoring/exception_tracker.py`
- **LogAggregationStats** (10 connections) — `server/structured_logging/log_aggregator.py`
- **.record_custom_alert()** (9 connections) — `server/monitoring/monitoring_dashboard.py`
- **_initialize_enhanced_systems()** (8 connections) — `server/app/lifespan.py`
- **__getattr__()** (8 connections) — `server/monitoring/__init__.py`
- **SystemHealth** (8 connections) — `server/monitoring/monitoring_dashboard.py`
- **.check_alerts()** (8 connections) — `server/monitoring/monitoring_dashboard.py`
- **track_exception_with_context()** (7 connections) — `server/monitoring/exception_tracker.py`
- **MonitoringSummary** (7 connections) — `server/monitoring/monitoring_dashboard.py`
- **._generate_recommendations()** (7 connections) — `server/monitoring/monitoring_dashboard.py`
- **.__init__()** (6 connections) — `server/monitoring/monitoring_dashboard.py`
- **.get_monitoring_summary()** (6 connections) — `server/monitoring/monitoring_dashboard.py`
- **Any** (6 connections)
- *... and 57 more nodes in this community*

## Relationships

- [Merge Refactoring Summary](Merge_Refactoring_Summary.md) (11 shared connections)
- [Flee Command Tests](Flee_Command_Tests.md) (11 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (9 shared connections)
- [Client Event Store](Client_Event_Store.md) (8 shared connections)
- [Monitoring Bundle Services](Monitoring_Bundle_Services.md) (7 shared connections)
- [Room Occupant Manager Tests](Room_Occupant_Manager_Tests.md) (7 shared connections)
- [Memory Leak Metrics](Memory_Leak_Metrics.md) (6 shared connections)
- [NATS Subject Metrics](NATS_Subject_Metrics.md) (6 shared connections)
- [Player Movement Service](Player_Movement_Service.md) (4 shared connections)
- [Character Info Panel Fix](Character_Info_Panel_Fix.md) (4 shared connections)
- [Test Migration Mapping](Test_Migration_Mapping.md) (4 shared connections)
- [Client Lifecycle Metrics](Client_Lifecycle_Metrics.md) (4 shared connections)

## Source Files

- `server/app/lifespan.py`
- `server/monitoring/__init__.py`
- `server/monitoring/exception_tracker.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/monitoring/performance_monitor.py`
- `server/structured_logging/log_aggregator.py`

## Audit Trail

- EXTRACTED: 367 (90%)
- INFERRED: 41 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*