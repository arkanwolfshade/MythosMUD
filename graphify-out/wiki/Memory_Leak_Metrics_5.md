# Memory Leak Metrics

> 106 nodes

## Key Concepts

- **MonitoringDashboard** (33 connections) — `server/monitoring/monitoring_dashboard.py`
- **monitoring_dashboard.py** (25 connections) — `server/monitoring/monitoring_dashboard.py`
- **PerformanceMonitor** (25 connections) — `server/monitoring/performance_monitor.py`
- **performance_monitor.py** (20 connections) — `server/monitoring/performance_monitor.py`
- **get_monitoring_dashboard()** (19 connections) — `server/monitoring/monitoring_dashboard.py`
- **Alert** (14 connections) — `server/monitoring/monitoring_dashboard.py`
- **get_performance_monitor()** (13 connections) — `server/monitoring/performance_monitor.py`
- **ExceptionStats** (12 connections) — `server/monitoring/exception_tracker.py`
- **__init__.py** (11 connections) — `server/monitoring/__init__.py`
- **.get_system_health()** (11 connections) — `server/monitoring/monitoring_dashboard.py`
- **PerformanceStats** (11 connections) — `server/monitoring/performance_monitor.py`
- **LogAggregationStats** (10 connections) — `server/structured_logging/log_aggregator.py`
- **.record_custom_alert()** (9 connections) — `server/monitoring/monitoring_dashboard.py`
- **PerformanceMetric** (9 connections) — `server/monitoring/performance_monitor.py`
- **_initialize_enhanced_systems()** (8 connections) — `server/app/lifespan.py`
- **__getattr__()** (8 connections) — `server/monitoring/__init__.py`
- **SystemHealth** (8 connections) — `server/monitoring/monitoring_dashboard.py`
- **.check_alerts()** (8 connections) — `server/monitoring/monitoring_dashboard.py`
- **.record_metric()** (8 connections) — `server/monitoring/performance_monitor.py`
- **.initialize()** (7 connections) — `server/container/bundles/monitoring.py`
- **MonitoringSummary** (7 connections) — `server/monitoring/monitoring_dashboard.py`
- **._generate_recommendations()** (7 connections) — `server/monitoring/monitoring_dashboard.py`
- **get_performance_stats()** (7 connections) — `server/monitoring/performance_monitor.py`
- **.__init__()** (6 connections) — `server/monitoring/monitoring_dashboard.py`
- **.get_monitoring_summary()** (6 connections) — `server/monitoring/monitoring_dashboard.py`
- *... and 81 more nodes in this community*

## Relationships

- [Game Service Bundle](Game_Service_Bundle.md) (14 shared connections)
- [Merge Refactoring Summary](Merge_Refactoring_Summary.md) (11 shared connections)
- [Monitoring Bundle Services](Monitoring_Bundle_Services.md) (8 shared connections)
- [Monitoring Response Models](Monitoring_Response_Models.md) (8 shared connections)
- [Test Optimization Insights](Test_Optimization_Insights.md) (7 shared connections)
- [Party Service Management](Party_Service_Management.md) (6 shared connections)
- [Mythos Time HUD](Mythos_Time_HUD.md) (6 shared connections)
- [Performance Monitor Metrics](Performance_Monitor_Metrics.md) (5 shared connections)
- [Magic Command Handlers](Magic_Command_Handlers.md) (4 shared connections)
- [NPC Database Sessions](NPC_Database_Sessions.md) (3 shared connections)
- [Quest Instance Repository](Quest_Instance_Repository.md) (2 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (1 shared connections)

## Source Files

- `server/app/lifespan.py`
- `server/container/bundles/monitoring.py`
- `server/monitoring/__init__.py`
- `server/monitoring/exception_tracker.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/monitoring/performance_monitor.py`
- `server/structured_logging/log_aggregator.py`

## Audit Trail

- EXTRACTED: 426 (89%)
- INFERRED: 50 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*