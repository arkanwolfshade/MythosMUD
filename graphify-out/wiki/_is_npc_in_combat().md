# . is npc in combat()

> 29 nodes

## Key Concepts

- **PerformanceMonitor** (24 connections) — `server/monitoring/performance_monitor.py`
- **PerformanceMetric** (9 connections) — `server/monitoring/performance_monitor.py`
- **.record_metric()** (8 connections) — `server/monitoring/performance_monitor.py`
- **get_performance_stats()** (7 connections) — `server/monitoring/performance_monitor.py`
- **Any** (6 connections)
- **.get_operation_stats()** (6 connections) — `server/monitoring/performance_monitor.py`
- **.get_all_stats()** (5 connections) — `server/monitoring/performance_monitor.py`
- **._trigger_alert()** (5 connections) — `server/monitoring/performance_monitor.py`
- **.export_metrics()** (5 connections) — `server/monitoring/performance_monitor.py`
- **.__init__()** (4 connections) — `server/monitoring/performance_monitor.py`
- **.get_recent_metrics()** (4 connections) — `server/monitoring/performance_monitor.py`
- **.add_alert_callback()** (4 connections) — `server/monitoring/performance_monitor.py`
- **.get_slow_operations()** (3 connections) — `server/monitoring/performance_monitor.py`
- **.get_failed_operations()** (3 connections) — `server/monitoring/performance_monitor.py`
- **.reset_metrics()** (3 connections) — `server/monitoring/performance_monitor.py`
- **Represents a single performance metric.** (1 connections) — `server/monitoring/performance_monitor.py`
- **Performance monitoring and metrics collection system.      This class provides c** (1 connections) — `server/monitoring/performance_monitor.py`
- **Initialize the performance monitor.          Args:             max_metrics: Maxi** (1 connections) — `server/monitoring/performance_monitor.py`
- **Record a performance metric.          Args:             operation: Name of the o** (1 connections) — `server/monitoring/performance_monitor.py`
- **Get performance statistics for a specific operation.          Args:** (1 connections) — `server/monitoring/performance_monitor.py`
- **Get performance statistics for all operations.          Returns:             Dic** (1 connections) — `server/monitoring/performance_monitor.py`
- **Get the most recent performance metrics.          Args:             count: Numbe** (1 connections) — `server/monitoring/performance_monitor.py`
- **Get operations that exceeded the performance threshold.          Args:** (1 connections) — `server/monitoring/performance_monitor.py`
- **Get operations that failed.          Returns:             List of failed operati** (1 connections) — `server/monitoring/performance_monitor.py`
- **Add an alert callback function.          Args:             callback: Function to** (1 connections) — `server/monitoring/performance_monitor.py`
- *... and 4 more nodes in this community*

## Relationships

- [.shutdown()](shutdown%28%29.md) (12 shared connections)
- [test command parser](test_command_parser.md) (3 shared connections)
- [websocket integration](websocket_integration.md) (3 shared connections)
- [config](config.md) (3 shared connections)
- [fastapi integration](fastapi_integration.md) (2 shared connections)
- [Coord](Coord.md) (1 shared connections)

## Source Files

- `server/monitoring/performance_monitor.py`

## Audit Trail

- EXTRACTED: 103 (94%)
- INFERRED: 7 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*