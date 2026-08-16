# system_monitoring.py

> 59 nodes

## Key Concepts

- **system_monitoring.py** (24 connections) — `server/api/system_monitoring.py`
- **TestMonitoringEndpoints** (16 connections) — `server/tests/unit/test_main.py`
- **asyncio** (14 connections)
- **get_system_monitoring_summary()** (11 connections) — `server/api/system_monitoring.py`
- **resolve_system_alert()** (11 connections) — `server/api/system_monitoring.py`
- **get_system_health()** (10 connections) — `server/api/system_monitoring.py`
- **get_system_monitoring_alerts()** (10 connections) — `server/api/system_monitoring.py`
- **AlertResolveResponse** (5 connections) — `server/api/monitoring_models.py`
- **SystemAlertsResponse** (5 connections) — `server/api/monitoring_models.py`
- **SystemHealthResponse** (5 connections) — `server/api/monitoring_models.py`
- **SystemMonitoringSummaryResponse** (5 connections) — `server/api/monitoring_models.py`
- **TestLifespan** (5 connections) — `server/tests/unit/test_main.py`
- **Request** (5 connections)
- **.test_lifespan_initialization_failure()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_lifespan_shutdown()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_lifespan_success()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_get_alerts_failure()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_get_alerts_success()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_get_metrics_failure()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_get_metrics_success()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_get_monitoring_summary_failure()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_get_monitoring_summary_success()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_health_check_failure()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_health_check_success()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_resolve_alert_failure()** (4 connections) — `server/tests/unit/test_main.py`
- *... and 34 more nodes in this community*

## Relationships

- [lifespan.py](lifespan.py.md) (15 shared connections)
- [api/monitoring.py](api-monitoring.py.md) (12 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (9 shared connections)
- [MonitoringDashboard](MonitoringDashboard.md) (6 shared connections)
- [get_logger](get_logger.md) (2 shared connections)
- [test_cache_service.py](test_cache_service.py.md) (1 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (1 shared connections)

## Source Files

- `server/api/monitoring_models.py`
- `server/api/system_monitoring.py`
- `server/tests/unit/test_main.py`

## Audit Trail

- EXTRACTED: 129 (96%)
- INFERRED: 5 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*