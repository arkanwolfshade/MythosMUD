# Monitoring Bundle Services

> 48 nodes

## Key Concepts

- **LogAggregator** (25 connections) — `server/structured_logging/log_aggregator.py`
- **LogEntry** (15 connections) — `server/structured_logging/log_aggregator.py`
- **log_aggregator.py** (14 connections) — `server/structured_logging/log_aggregator.py`
- **.get_logs()** (10 connections) — `server/structured_logging/log_aggregator.py`
- **LogQueryFilter** (9 connections) — `server/structured_logging/log_aggregator.py`
- **.export_logs()** (8 connections) — `server/structured_logging/log_aggregator.py`
- **get_log_aggregator()** (8 connections) — `server/structured_logging/log_aggregator.py`
- **.__init__()** (6 connections) — `server/structured_logging/log_aggregator.py`
- **aggregate_log_entry()** (6 connections) — `server/structured_logging/log_aggregator.py`
- **.add_log_entry()** (5 connections) — `server/structured_logging/log_aggregator.py`
- **._log_matches_filter()** (5 connections) — `server/structured_logging/log_aggregator.py`
- **.get_error_logs()** (5 connections) — `server/structured_logging/log_aggregator.py`
- **.get_warning_logs()** (5 connections) — `server/structured_logging/log_aggregator.py`
- **.get_user_logs()** (5 connections) — `server/structured_logging/log_aggregator.py`
- **.get_correlation_logs()** (5 connections) — `server/structured_logging/log_aggregator.py`
- **._export_json()** (5 connections) — `server/structured_logging/log_aggregator.py`
- **._export_csv()** (5 connections) — `server/structured_logging/log_aggregator.py`
- **._update_stats()** (4 connections) — `server/structured_logging/log_aggregator.py`
- **Path** (4 connections)
- **.get_stats()** (3 connections) — `server/structured_logging/log_aggregator.py`
- **.add_aggregation_callback()** (3 connections) — `server/structured_logging/log_aggregator.py`
- **._start_processing_thread()** (3 connections) — `server/structured_logging/log_aggregator.py`
- **._eq_if_set()** (2 connections) — `server/structured_logging/log_aggregator.py`
- **.shutdown()** (2 connections) — `server/structured_logging/log_aggregator.py`
- **._process_logs()** (2 connections) — `server/structured_logging/log_aggregator.py`
- *... and 23 more nodes in this community*

## Relationships

- [Help and WebSocket Core](Help_and_WebSocket_Core.md) (6 shared connections)
- [Docker PostgreSQL Typo Bug](Docker_PostgreSQL_Typo_Bug.md) (3 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (3 shared connections)
- [WebSocket Code Review](WebSocket_Code_Review.md) (2 shared connections)
- [Realtime Service Bundle](Realtime_Service_Bundle.md) (1 shared connections)
- [Logging File Setup](Logging_File_Setup.md) (1 shared connections)
- [User Manager Mute Tests](User_Manager_Mute_Tests.md) (1 shared connections)

## Source Files

- `server/structured_logging/log_aggregator.py`

## Audit Trail

- EXTRACTED: 184 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*