# Monitoring Bundle Services

> 51 nodes · cohesion 0.06

## Key Concepts

- **LogAggregator** (24 connections) — `server/structured_logging/log_aggregator.py`
- **MonitoringBundle** (13 connections) — `server/container/bundles/monitoring.py`
- **LogEntry** (12 connections) — `server/structured_logging/log_aggregator.py`
- **log_aggregator.py** (11 connections) — `server/structured_logging/log_aggregator.py`
- **monitoring.py** (9 connections) — `server/container/bundles/monitoring.py`
- **.get_logs()** (9 connections) — `server/structured_logging/log_aggregator.py`
- **.initialize()** (7 connections) — `server/container/bundles/monitoring.py`
- **ApplicationContainer** (7 connections) — `server/container/bundles/monitoring.py`
- **.export_logs()** (7 connections) — `server/structured_logging/log_aggregator.py`
- **aggregate_log_entry()** (6 connections) — `server/structured_logging/log_aggregator.py`
- **.add_log_entry()** (6 connections) — `server/structured_logging/log_aggregator.py`
- **._export_csv()** (5 connections) — `server/structured_logging/log_aggregator.py`
- **._export_json()** (5 connections) — `server/structured_logging/log_aggregator.py`
- **.__init__()** (5 connections) — `server/structured_logging/log_aggregator.py`
- **Path** (4 connections) — `server/structured_logging/log_aggregator.py`
- **.get_correlation_logs()** (4 connections) — `server/structured_logging/log_aggregator.py`
- **.get_error_logs()** (4 connections) — `server/structured_logging/log_aggregator.py`
- **.get_user_logs()** (4 connections) — `server/structured_logging/log_aggregator.py`
- **.get_warning_logs()** (4 connections) — `server/structured_logging/log_aggregator.py`
- **._update_stats()** (4 connections) — `server/structured_logging/log_aggregator.py`
- **.shutdown()** (3 connections) — `server/container/bundles/monitoring.py`
- **Any** (3 connections) — `server/structured_logging/log_aggregator.py`
- **.add_aggregation_callback()** (3 connections) — `server/structured_logging/log_aggregator.py`
- **.get_stats()** (3 connections) — `server/structured_logging/log_aggregator.py`
- **._start_processing_thread()** (3 connections) — `server/structured_logging/log_aggregator.py`
- *... and 26 more nodes in this community*

## Relationships

- [[App Lifespan Management]] (8 shared connections)
- [[Application DI Bundles]] (7 shared connections)
- [[Memory Leak Metrics]] (7 shared connections)
- [[Performance Monitor Metrics]] (4 shared connections)
- [[NPC Admin API]] (3 shared connections)
- [[Game Service Bundle]] (1 shared connections)
- [[Logging File Setup]] (1 shared connections)

## Source Files

- `server/container/bundles/monitoring.py`
- `server/structured_logging/log_aggregator.py`

## Audit Trail

- EXTRACTED: 183 (94%)
- INFERRED: 12 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
