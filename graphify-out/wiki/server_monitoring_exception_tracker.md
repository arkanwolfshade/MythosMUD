# server monitoring exception tracker

> 76 nodes

## Key Concepts

- **ExceptionTracker** (30 connections) — `server/monitoring/exception_tracker.py`
- **monitoring_dashboard.py** (26 connections) — `server/monitoring/monitoring_dashboard.py`
- **exception_tracker.py** (21 connections) — `server/monitoring/exception_tracker.py`
- **get_monitoring_dashboard()** (19 connections) — `server/monitoring/monitoring_dashboard.py`
- **track_exception()** (15 connections) — `server/monitoring/exception_tracker.py`
- **test_exception_tracker.py** (13 connections) — `server/tests/unit/monitoring/test_exception_tracker.py`
- **ExceptionRecord** (12 connections) — `server/monitoring/exception_tracker.py`
- **get_exception_tracker()** (12 connections) — `server/monitoring/exception_tracker.py`
- **server/monitoring/__init__.py** (11 connections) — `server/monitoring/__init__.py`
- **ExceptionStats** (10 connections) — `server/monitoring/exception_tracker.py`
- **PerformanceStats** (10 connections) — `server/monitoring/performance_monitor.py`
- **.track_exception()** (8 connections) — `server/monitoring/exception_tracker.py`
- **__getattr__()** (8 connections) — `server/monitoring/__init__.py`
- **Exception** (7 connections)
- **ExceptionTrackInput** (6 connections) — `server/monitoring/exception_tracker.py`
- **MonitoringSummary** (6 connections) — `server/monitoring/monitoring_dashboard.py`
- **._create_and_store_record()** (6 connections) — `server/monitoring/exception_tracker.py`
- **track_exception_with_context()** (6 connections) — `server/monitoring/exception_tracker.py`
- **._call_handlers()** (5 connections) — `server/monitoring/exception_tracker.py`
- **._log_tracked_exception()** (5 connections) — `server/monitoring/exception_tracker.py`
- **Any** (5 connections)
- **ExceptionContextTrackInput** (4 connections) — `server/monitoring/exception_tracker.py`
- **.add_exception_handler()** (4 connections) — `server/monitoring/exception_tracker.py`
- **._parse_track_options()** (4 connections) — `server/monitoring/exception_tracker.py`
- **._update_stats()** (4 connections) — `server/monitoring/exception_tracker.py`
- *... and 51 more nodes in this community*

## Relationships

- [performancestats](performancestats.md) (13 shared connections)
- [server monitoring monitoring dashboard monitoringdashboard](server_monitoring_monitoring_dashboard_monitoringdashboard.md) (10 shared connections)
- [server app lifespan](server_app_lifespan.md) (6 shared connections)
- [server api monitoring models](server_api_monitoring_models.md) (6 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (5 shared connections)
- [docs examples logging correct patterns](docs_examples_logging_correct_patterns.md) (3 shared connections)
- [docs examples logging testing examples](docs_examples_logging_testing_examples.md) (3 shared connections)
- [docs examples logging websocket integration](docs_examples_logging_websocket_integration.md) (3 shared connections)
- [server monitoring exception metrics](server_monitoring_exception_metrics.md) (3 shared connections)
- [server commands admin summon command](server_commands_admin_summon_command.md) (3 shared connections)
- [server services inventory mutation guard](server_services_inventory_mutation_guard.md) (3 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (2 shared connections)

## Source Files

- `server/monitoring/__init__.py`
- `server/monitoring/exception_tracker.py`
- `server/monitoring/monitoring_dashboard.py`
- `server/monitoring/performance_monitor.py`
- `server/tests/unit/monitoring/test_exception_tracker.py`

## Audit Trail

- EXTRACTED: 195 (94%)
- INFERRED: 12 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*