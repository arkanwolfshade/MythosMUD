# models lucidity rationale

> 83 nodes

## Key Concepts

- **PerformanceMonitor** (32 connections) — `server/monitoring/performance_monitor.py`
- **measure_performance()** (22 connections) — `server/monitoring/performance_monitor.py`
- **performance_monitor.py** (21 connections) — `server/monitoring/performance_monitor.py`
- **correct_patterns.py** (20 connections) — `docs/examples/logging/correct_patterns.py`
- **test_performance_monitor.py** (18 connections) — `server/tests/unit/monitoring/test_performance_monitor.py`
- **get_performance_monitor()** (15 connections) — `server/monitoring/performance_monitor.py`
- **PerformanceMetric** (9 connections) — `server/monitoring/performance_monitor.py`
- **get_performance_stats()** (9 connections) — `server/monitoring/performance_monitor.py`
- **.record_metric()** (8 connections) — `server/monitoring/performance_monitor.py`
- **record_performance_metric()** (8 connections) — `server/monitoring/performance_monitor.py`
- **reset_performance_metrics()** (7 connections) — `server/monitoring/performance_monitor.py`
- **Any** (6 connections)
- **.get_operation_stats()** (6 connections) — `server/monitoring/performance_monitor.py`
- **correct_performance_logging()** (5 connections) — `docs/examples/logging/correct_patterns.py`
- **correct_async_logging()** (5 connections) — `docs/examples/logging/correct_patterns.py`
- **.get_all_stats()** (5 connections) — `server/monitoring/performance_monitor.py`
- **._trigger_alert()** (5 connections) — `server/monitoring/performance_monitor.py`
- **.export_metrics()** (5 connections) — `server/monitoring/performance_monitor.py`
- **correct_exception_tracking()** (4 connections) — `docs/examples/logging/correct_patterns.py`
- **risky_operation()** (4 connections) — `docs/examples/logging/correct_patterns.py`
- **database** (4 connections) — `docs/examples/logging/correct_patterns.py`
- **.execute()** (4 connections) — `docs/examples/logging/correct_patterns.py`
- **.__init__()** (4 connections) — `server/monitoring/performance_monitor.py`
- **.get_recent_metrics()** (4 connections) — `server/monitoring/performance_monitor.py`
- **.add_alert_callback()** (4 connections) — `server/monitoring/performance_monitor.py`
- *... and 58 more nodes in this community*

## Relationships

- [room cache services](room_cache_services.md) (8 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (7 shared connections)
- [middleware correlation rationale](middleware_correlation_rationale.md) (6 shared connections)
- [app factory rationale](app_factory_rationale.md) (5 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (4 shared connections)
- [examples logging testing](examples_logging_testing.md) (4 shared connections)
- [aggro threat services](aggro_threat_services.md) (3 shared connections)
- [nats services service](nats_services_service.md) (3 shared connections)
- [player room realtime](player_room_realtime.md) (2 shared connections)
- [lucidity flux passive](lucidity_flux_passive.md) (2 shared connections)
- [player requests schemas](player_requests_schemas.md) (1 shared connections)
- [mythos mud mapbuilder](mythos_mud_mapbuilder.md) (1 shared connections)

## Source Files

- `docs/examples/logging/correct_patterns.py`
- `server/monitoring/performance_monitor.py`
- `server/tests/unit/monitoring/test_performance_monitor.py`

## Audit Trail

- EXTRACTED: 312 (96%)
- INFERRED: 12 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*