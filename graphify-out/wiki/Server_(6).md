# Server (6)

> 27 nodes

## Key Concepts

- **TestMonitoringEndpoints** (16 connections) — `server/tests/unit/test_main.py`
- **.test_health_check_failure()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_get_metrics_failure()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_get_monitoring_summary_failure()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_get_alerts_failure()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_resolve_alert_not_found()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_resolve_alert_failure()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_health_check_success()** (3 connections) — `server/tests/unit/test_main.py`
- **.test_get_metrics_success()** (3 connections) — `server/tests/unit/test_main.py`
- **.test_get_monitoring_summary_success()** (3 connections) — `server/tests/unit/test_main.py`
- **.test_get_alerts_success()** (3 connections) — `server/tests/unit/test_main.py`
- **.test_resolve_alert_success()** (3 connections) — `server/tests/unit/test_main.py`
- **.mock_app()** (2 connections) — `server/tests/unit/test_main.py`
- **.mock_dashboard()** (2 connections) — `server/tests/unit/test_main.py`
- **Test metrics endpoint handles errors.** (2 connections) — `server/tests/unit/test_main.py`
- **Test monitoring endpoint functions.** (1 connections) — `server/tests/unit/test_main.py`
- **Create a mock FastAPI app.** (1 connections) — `server/tests/unit/test_main.py`
- **Create a mock monitoring dashboard.** (1 connections) — `server/tests/unit/test_main.py`
- **Test health check endpoint returns system health.** (1 connections) — `server/tests/unit/test_main.py`
- **Test health check endpoint handles errors.** (1 connections) — `server/tests/unit/test_main.py`
- **Test metrics endpoint returns monitoring data.** (1 connections) — `server/tests/unit/test_main.py`
- **Test monitoring summary endpoint returns summary data.** (1 connections) — `server/tests/unit/test_main.py`
- **Test monitoring summary endpoint handles errors.** (1 connections) — `server/tests/unit/test_main.py`
- **Test alerts endpoint returns alert data.** (1 connections) — `server/tests/unit/test_main.py`
- **Test resolve alert endpoint succeeds.** (1 connections) — `server/tests/unit/test_main.py`
- *... and 2 more nodes in this community*

## Relationships

- [Server Monitoring](Server_Monitoring.md) (10 shared connections)
- [Server Api](Server_Api.md) (7 shared connections)
- [Server Api (5)](Server_Api_%285%29.md) (2 shared connections)

## Source Files

- `server/tests/unit/test_main.py`

## Audit Trail

- EXTRACTED: 66 (90%)
- INFERRED: 7 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*