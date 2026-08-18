# logentry

> 69 nodes

## Key Concepts

- **LogAggregator** (37 connections) — `server/structured_logging/log_aggregator.py`
- **log_aggregator.py** (21 connections) — `server/structured_logging/log_aggregator.py`
- **test_log_aggregator.py** (18 connections) — `server/tests/unit/structured_logging/test_log_aggregator.py`
- **LogEntry** (17 connections) — `server/structured_logging/log_aggregator.py`
- **LogQueryFilter** (11 connections) — `server/structured_logging/log_aggregator.py`
- **.get_logs()** (10 connections) — `server/structured_logging/log_aggregator.py`
- **_entry()** (10 connections) — `server/tests/unit/structured_logging/test_log_aggregator.py`
- **get_log_aggregator()** (8 connections) — `server/structured_logging/log_aggregator.py`
- **aggregate_log_entry()** (7 connections) — `server/structured_logging/log_aggregator.py`
- **.export_logs()** (7 connections) — `server/structured_logging/log_aggregator.py`
- **_query_filter_from_mapping()** (6 connections) — `server/structured_logging/log_aggregator.py`
- **_flush_queue()** (6 connections) — `server/tests/unit/structured_logging/test_log_aggregator.py`
- **._export_csv()** (5 connections) — `server/structured_logging/log_aggregator.py`
- **._export_json()** (5 connections) — `server/structured_logging/log_aggregator.py`
- **.get_correlation_logs()** (5 connections) — `server/structured_logging/log_aggregator.py`
- **.get_error_logs()** (5 connections) — `server/structured_logging/log_aggregator.py`
- **.get_user_logs()** (5 connections) — `server/structured_logging/log_aggregator.py`
- **.get_warning_logs()** (5 connections) — `server/structured_logging/log_aggregator.py`
- **.__init__()** (5 connections) — `server/structured_logging/log_aggregator.py`
- **._log_matches_filter()** (5 connections) — `server/structured_logging/log_aggregator.py`
- **peek_log_aggregator()** (5 connections) — `server/structured_logging/log_aggregator.py`
- **test_export_logs_json()** (5 connections) — `server/tests/unit/structured_logging/test_log_aggregator.py`
- **test_get_logs_after_flush()** (5 connections) — `server/tests/unit/structured_logging/test_log_aggregator.py`
- **.add_log_entry()** (4 connections) — `server/structured_logging/log_aggregator.py`
- **._update_stats()** (4 connections) — `server/structured_logging/log_aggregator.py`
- *... and 44 more nodes in this community*

## Relationships

- [claude rules asyncio](claude_rules_asyncio.md) (5 shared connections)
- [performancestats](performancestats.md) (4 shared connections)
- [server app lifespan](server_app_lifespan.md) (3 shared connections)
- [server container bundles chat](server_container_bundles_chat.md) (2 shared connections)
- [server monitoring exception tracker](server_monitoring_exception_tracker.md) (2 shared connections)
- [server app lifespan startup legacy](server_app_lifespan_startup_legacy.md) (1 shared connections)
- [server monitoring monitoring dashboard monitoringdashboard](server_monitoring_monitoring_dashboard_monitoringdashboard.md) (1 shared connections)
- [server realtime memory monitor collect](server_realtime_memory_monitor_collect.md) (1 shared connections)
- [logger](logger.md) (1 shared connections)

## Source Files

- `server/structured_logging/log_aggregator.py`
- `server/tests/unit/structured_logging/test_log_aggregator.py`

## Audit Trail

- EXTRACTED: 158 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*