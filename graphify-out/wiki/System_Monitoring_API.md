# System Monitoring API

> 59 nodes · cohesion 0.07

## Key Concepts

- **system_monitoring.py** (23 connections) — `server/api/system_monitoring.py`
- **get_monitoring_dashboard()** (19 connections) — `server/monitoring/monitoring_dashboard.py`
- **TestMonitoringEndpoints** (16 connections) — `server/tests/unit/test_main.py`
- **test_main.py** (12 connections) — `server/tests/unit/test_main.py`
- **get_system_metrics()** (11 connections) — `server/api/system_monitoring.py`
- **AlertResolveResponse** (10 connections) — `server/api/monitoring_models.py`
- **SystemAlertsResponse** (10 connections) — `server/api/monitoring_models.py`
- **SystemHealthResponse** (10 connections) — `server/api/monitoring_models.py`
- **SystemMetricsResponse** (10 connections) — `server/api/monitoring_models.py`
- **SystemMonitoringSummaryResponse** (10 connections) — `server/api/monitoring_models.py`
- **get_system_monitoring_summary()** (10 connections) — `server/api/system_monitoring.py`
- **resolve_system_alert()** (10 connections) — `server/api/system_monitoring.py`
- **Request** (10 connections) — `server/api/system_monitoring.py`
- **get_system_health()** (9 connections) — `server/api/system_monitoring.py`
- **get_system_monitoring_alerts()** (9 connections) — `server/api/system_monitoring.py`
- **AlertResolveResponse** (6 connections) — `server/api/system_monitoring.py`
- **SystemAlertsResponse** (6 connections) — `server/api/system_monitoring.py`
- **SystemHealthResponse** (6 connections) — `server/api/system_monitoring.py`
- **SystemMetricsResponse** (6 connections) — `server/api/system_monitoring.py`
- **SystemMonitoringSummaryResponse** (6 connections) — `server/api/system_monitoring.py`
- **.test_get_alerts_failure()** (3 connections) — `server/tests/unit/test_main.py`
- **.test_get_alerts_success()** (3 connections) — `server/tests/unit/test_main.py`
- **.test_get_metrics_failure()** (3 connections) — `server/tests/unit/test_main.py`
- **.test_get_metrics_success()** (3 connections) — `server/tests/unit/test_main.py`
- **.test_get_monitoring_summary_failure()** (3 connections) — `server/tests/unit/test_main.py`
- *... and 34 more nodes in this community*

## Relationships

- [[Container Exception Handlers]] (8 shared connections)
- [[Monitoring Response Models]] (7 shared connections)
- [[App Lifespan Management]] (7 shared connections)
- [[Admin NPC Schemas]] (5 shared connections)
- [[NPC Admin API]] (5 shared connections)
- [[Memory Leak Metrics]] (3 shared connections)
- [[Inventory Service Helpers]] (3 shared connections)
- [[Monitoring API Endpoints]] (2 shared connections)
- [[Cache and NPC Cache]] (2 shared connections)
- [[Admin Summon Command]] (2 shared connections)
- [[Weapon Resolution Helpers]] (2 shared connections)
- [[FastAPI App Factory]] (1 shared connections)

## Source Files

- `server/api/monitoring_models.py`
- `server/api/system_monitoring.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/tests/unit/test_main.py`

## Audit Trail

- EXTRACTED: 213 (78%)
- INFERRED: 61 (22%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
