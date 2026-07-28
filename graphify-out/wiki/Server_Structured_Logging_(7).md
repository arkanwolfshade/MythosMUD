# Server Structured Logging (7)

> 45 nodes

## Key Concepts

- **LogAggregator** (23 connections) — `server/structured_logging/log_aggregator.py`
- **log_aggregator.py** (13 connections) — `server/structured_logging/log_aggregator.py`
- **LogEntry** (13 connections) — `server/structured_logging/log_aggregator.py`
- **.get_logs()** (9 connections) — `server/structured_logging/log_aggregator.py`
- **get_log_aggregator()** (8 connections) — `server/structured_logging/log_aggregator.py`
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
- **Log aggregation and centralized collection system for MythosMUD server.  This mo** (1 connections) — `server/structured_logging/log_aggregator.py`
- *... and 20 more nodes in this community*

## Relationships

- [Server Monitoring](Server_Monitoring.md) (8 shared connections)
- [Server Commands](Server_Commands.md) (3 shared connections)
- [Server Npc (6)](Server_Npc_%286%29.md) (1 shared connections)
- [Server Structured Logging (5)](Server_Structured_Logging_%285%29.md) (1 shared connections)
- [Server App (2)](Server_App_%282%29.md) (1 shared connections)
- [Docs Examples](Docs_Examples.md) (1 shared connections)
- [Server Monitoring (2)](Server_Monitoring_%282%29.md) (1 shared connections)

## Source Files

- `server/structured_logging/log_aggregator.py`

## Audit Trail

- EXTRACTED: 161 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*