# init

> 59 nodes

## Key Concepts

- **system_monitoring.py** (23 connections) — `server/api/system_monitoring.py`
- **get_monitoring_dashboard()** (20 connections) — `server/monitoring/monitoring_dashboard.py`
- **get_cache_manager()** (16 connections) — `server/caching/lru_cache.py`
- **TestMonitoringEndpoints** (16 connections) — `server/tests/unit/test_main.py`
- **test_main.py** (13 connections) — `server/tests/unit/test_main.py`
- **get_system_metrics()** (11 connections) — `server/api/system_monitoring.py`
- **__init__.py** (10 connections) — `server/api/__init__.py`
- **get_system_monitoring_summary()** (10 connections) — `server/api/system_monitoring.py`
- **resolve_system_alert()** (10 connections) — `server/api/system_monitoring.py`
- **get_system_health()** (9 connections) — `server/api/system_monitoring.py`
- **get_system_monitoring_alerts()** (9 connections) — `server/api/system_monitoring.py`
- **SystemHealthResponse** (5 connections) — `server/api/monitoring_models.py`
- **SystemMetricsResponse** (5 connections) — `server/api/monitoring_models.py`
- **SystemMonitoringSummaryResponse** (5 connections) — `server/api/monitoring_models.py`
- **SystemAlertsResponse** (5 connections) — `server/api/monitoring_models.py`
- **AlertResolveResponse** (5 connections) — `server/api/monitoring_models.py`
- **Request** (5 connections)
- **.test_health_check_failure()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_get_metrics_failure()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_get_monitoring_summary_failure()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_get_alerts_failure()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_resolve_alert_not_found()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_resolve_alert_failure()** (4 connections) — `server/tests/unit/test_main.py`
- **.test_health_check_success()** (3 connections) — `server/tests/unit/test_main.py`
- **.test_get_metrics_success()** (3 connections) — `server/tests/unit/test_main.py`
- *... and 34 more nodes in this community*

## Relationships

- [fetch container items()](fetch_container_items%28%29.md) (16 shared connections)
- [AbstractContextManager](AbstractContextManager.md) (14 shared connections)
- [world](world.md) (8 shared connections)
- [PerformanceStats](PerformanceStats.md) (5 shared connections)
- [.shutdown()](shutdown%28%29.md) (5 shared connections)
- [Any](Any.md) (4 shared connections)
- [. init ()](_init_%28%29.md) (3 shared connections)
- [Lock](Lock.md) (3 shared connections)
- [real time](real_time.md) (2 shared connections)
- [DropResolved](DropResolved.md) (2 shared connections)
- [test clear corrupted cache entry](test_clear_corrupted_cache_entry.md) (1 shared connections)
- [APIRouter](APIRouter.md) (1 shared connections)

## Source Files

- `server/api/__init__.py`
- `server/api/monitoring_models.py`
- `server/api/system_monitoring.py`
- `server/caching/lru_cache.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/tests/unit/test_main.py`

## Audit Trail

- EXTRACTED: 241 (97%)
- INFERRED: 8 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*