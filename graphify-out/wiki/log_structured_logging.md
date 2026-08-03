# log structured logging

> 41 nodes

## Key Concepts

- **LogAggregator** (23 connections) — `server/structured_logging/log_aggregator.py`
- **LogEntry** (13 connections) — `server/structured_logging/log_aggregator.py`
- **.get_logs()** (9 connections) — `server/structured_logging/log_aggregator.py`
- **.export_logs()** (7 connections) — `server/structured_logging/log_aggregator.py`
- **.__init__()** (6 connections) — `server/structured_logging/log_aggregator.py`
- **.add_log_entry()** (6 connections) — `server/structured_logging/log_aggregator.py`
- **aggregate_log_entry()** (6 connections) — `server/structured_logging/log_aggregator.py`
- **._export_json()** (5 connections) — `server/structured_logging/log_aggregator.py`
- **._export_csv()** (5 connections) — `server/structured_logging/log_aggregator.py`
- **.get_error_logs()** (4 connections) — `server/structured_logging/log_aggregator.py`
- **.get_warning_logs()** (4 connections) — `server/structured_logging/log_aggregator.py`
- **.get_user_logs()** (4 connections) — `server/structured_logging/log_aggregator.py`
- **.get_correlation_logs()** (4 connections) — `server/structured_logging/log_aggregator.py`
- **._update_stats()** (4 connections) — `server/structured_logging/log_aggregator.py`
- **Path** (4 connections)
- **Any** (3 connections)
- **.get_stats()** (3 connections) — `server/structured_logging/log_aggregator.py`
- **.add_aggregation_callback()** (3 connections) — `server/structured_logging/log_aggregator.py`
- **._start_processing_thread()** (3 connections) — `server/structured_logging/log_aggregator.py`
- **datetime** (2 connections)
- **.shutdown()** (2 connections) — `server/structured_logging/log_aggregator.py`
- **._process_logs()** (2 connections) — `server/structured_logging/log_aggregator.py`
- **Represents a single log entry.** (1 connections) — `server/structured_logging/log_aggregator.py`
- **Centralized log aggregation and collection system.      This class provides comp** (1 connections) — `server/structured_logging/log_aggregator.py`
- **Initialize the log aggregator.          Args:             max_entries: Maximum n** (1 connections) — `server/structured_logging/log_aggregator.py`
- *... and 16 more nodes in this community*

## Relationships

- [command inventory factories](command_inventory_factories.md) (8 shared connections)
- [Error Conversion](Error_Conversion.md) (3 shared connections)

## Source Files

- `server/structured_logging/log_aggregator.py`

## Audit Trail

- EXTRACTED: 138 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*