# TestMonitoringEndpoints

> 38 nodes

## Key Concepts

- **TestMonitoringEndpoints** (16 connections) — `server/tests/unit/test_main.py`
- **asyncio** (14 connections)
- **TestLifespan** (6 connections) — `server/tests/unit/test_main.py`
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
- **.test_resolve_alert_not_found()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_resolve_alert_success()** (4 connections) — `server/tests/unit/test_main.py`
- **.mock_app()** (3 connections) — `server/tests/unit/test_main.py`
- **.mock_dashboard()** (3 connections) — `server/tests/unit/test_main.py`
- **fixture** (2 connections)
- **Test health check endpoint returns system health.** (1 connections) — `server/tests/unit/test_main.py`
- **Test health check endpoint handles errors.** (1 connections) — `server/tests/unit/test_main.py`
- **Test metrics endpoint returns monitoring data.** (1 connections) — `server/tests/unit/test_main.py`
- **Test metrics endpoint handles errors.** (1 connections) — `server/tests/unit/test_main.py`
- **Test monitoring summary endpoint returns summary data.** (1 connections) — `server/tests/unit/test_main.py`
- *... and 13 more nodes in this community*

## Relationships

- [MonitoringDashboard](MonitoringDashboard.md) (13 shared connections)
- [lifespan.py](lifespan.py.md) (3 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (2 shared connections)

## Source Files

- `server/tests/unit/test_main.py`

## Audit Trail

- EXTRACTED: 66 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*