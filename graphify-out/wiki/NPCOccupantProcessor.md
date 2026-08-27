# NPCOccupantProcessor

> 73 nodes

## Key Concepts

- **MonitoringDashboard** (34 connections) — `server/monitoring/monitoring_dashboard.py`
- **monitoring_dashboard.py** (24 connections) — `server/monitoring/monitoring_dashboard.py`
- **get_monitoring_dashboard()** (19 connections) — `server/monitoring/monitoring_dashboard.py`
- **test_monitoring_dashboard.py** (17 connections) — `server/tests/unit/monitoring/test_monitoring_dashboard.py`
- **Alert** (12 connections) — `server/monitoring/monitoring_dashboard.py`
- **PerformanceStats** (12 connections) — `server/monitoring/performance_monitor.py`
- **.get_system_health()** (11 connections) — `server/monitoring/monitoring_dashboard.py`
- **_dashboard()** (11 connections) — `server/tests/unit/monitoring/test_monitoring_dashboard.py`
- **server/monitoring/__init__.py** (11 connections) — `server/monitoring/__init__.py`
- **LogAggregationStats** (10 connections) — `server/structured_logging/log_aggregator.py`
- **__getattr__()** (8 connections) — `server/monitoring/__init__.py`
- **.record_custom_alert()** (8 connections) — `server/monitoring/monitoring_dashboard.py`
- **._generate_recommendations()** (7 connections) — `server/monitoring/monitoring_dashboard.py`
- **SystemHealth** (6 connections) — `server/monitoring/monitoring_dashboard.py`
- **.check_alerts()** (6 connections) — `server/monitoring/monitoring_dashboard.py`
- **.get_monitoring_summary()** (6 connections) — `server/monitoring/monitoring_dashboard.py`
- **Any** (6 connections)
- **MonitoringSummary** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **.export_monitoring_data()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **.record_durability_anomaly()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **.record_registry_failure()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **.record_summon_quantity_spike()** (5 connections) — `server/monitoring/monitoring_dashboard.py`
- **._calculate_performance_score()** (4 connections) — `server/monitoring/monitoring_dashboard.py`
- **.get_alert_history()** (4 connections) — `server/monitoring/monitoring_dashboard.py`
- **._get_memory_leak_metrics()** (4 connections) — `server/monitoring/monitoring_dashboard.py`
- *... and 48 more nodes in this community*

## Relationships

- [TestMonitoringEndpoints](TestMonitoringEndpoints.md) (9 shared connections)
- [combat_taunt.py](combat_taunt.py.md) (6 shared connections)
- [debrief_command.py](debrief_command.py.md) (5 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (5 shared connections)
- [ContainerComponent](ContainerComponent.md) (4 shared connections)
- [Profession](Profession.md) (4 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (3 shared connections)
- [verify_enhanced_logging_compliance.py](verify_enhanced_logging_compliance.py.md) (3 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)
- [pytest.md](pytest.md.md) (2 shared connections)
- [authenticated.ts](authenticated.ts.md) (2 shared connections)
- [Coverage Improvement Summary - Plan 2 Execution](Coverage_Improvement_Summary_-_Plan_2_Execution.md) (1 shared connections)

## Source Files

- `server/monitoring/__init__.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/monitoring/performance_monitor.py`
- `server/structured_logging/log_aggregator.py`
- `server/tests/unit/monitoring/test_monitoring_dashboard.py`

## Audit Trail

- EXTRACTED: 171 (92%)
- INFERRED: 14 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*