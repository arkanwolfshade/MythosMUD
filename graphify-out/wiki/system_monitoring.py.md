# system_monitoring.py

> 61 nodes

## Key Concepts

- **system_monitoring.py** (23 connections) — `server/api/system_monitoring.py`
- **TestMonitoringEndpoints** (16 connections) — `server/tests/unit/test_main.py`
- **asyncio** (14 connections)
- **test_main.py** (13 connections) — `server/tests/unit/test_main.py`
- **get_system_monitoring_summary()** (11 connections) — `server/api/system_monitoring.py`
- **resolve_system_alert()** (11 connections) — `server/api/system_monitoring.py`
- **get_system_health()** (10 connections) — `server/api/system_monitoring.py`
- **get_system_monitoring_alerts()** (10 connections) — `server/api/system_monitoring.py`
- **TestLifespan** (6 connections) — `server/tests/unit/test_main.py`
- **AlertResolveResponse** (5 connections) — `server/api/monitoring_models.py`
- **SystemAlertsResponse** (5 connections) — `server/api/monitoring_models.py`
- **SystemHealthResponse** (5 connections) — `server/api/monitoring_models.py`
- **SystemMonitoringSummaryResponse** (5 connections) — `server/api/monitoring_models.py`
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
- *... and 36 more nodes in this community*

## Relationships

- [lifespan.py](lifespan.py.md) (12 shared connections)
- [monitoring_models.py](monitoring_models.py.md) (10 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (8 shared connections)
- [MonitoringDashboard](MonitoringDashboard.md) (6 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [api/monitoring.py](api-monitoring.py.md) (2 shared connections)
- [get_config](get_config.md) (1 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (1 shared connections)

## Source Files

- `server/api/monitoring_models.py`
- `server/api/system_monitoring.py`
- `server/tests/unit/test_main.py`

## Audit Trail

- EXTRACTED: 139 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*