# test_performance_tracker.py

> 14 nodes

## Key Concepts

- **test_performance_tracker.py** (9 connections) — `server/tests/unit/realtime/monitoring/test_performance_tracker.py`
- **test_get_stats_calculates_averages()** (3 connections) — `server/tests/unit/realtime/monitoring/test_performance_tracker.py`
- **test_get_stats_empty_returns_zeros()** (3 connections) — `server/tests/unit/realtime/monitoring/test_performance_tracker.py`
- **test_get_stats_error_path_returns_error_dict()** (3 connections) — `server/tests/unit/realtime/monitoring/test_performance_tracker.py`
- **test_get_stats_non_websocket_connections_excluded_from_websocket_stats()** (3 connections) — `server/tests/unit/realtime/monitoring/test_performance_tracker.py`
- **test_record_events_increase_counters()** (3 connections) — `server/tests/unit/realtime/monitoring/test_performance_tracker.py`
- **test_trim_samples_keeps_max_samples()** (3 connections) — `server/tests/unit/realtime/monitoring/test_performance_tracker.py`
- **Unit tests for PerformanceTracker.** (1 connections) — `server/tests/unit/realtime/monitoring/test_performance_tracker.py`
- **Samples beyond max_samples are trimmed from the front.** (1 connections) — `server/tests/unit/realtime/monitoring/test_performance_tracker.py`
- **Empty tracker returns zero averages.** (1 connections) — `server/tests/unit/realtime/monitoring/test_performance_tracker.py`
- **get_stats computes min/max/avg for recorded metrics.** (1 connections) — `server/tests/unit/realtime/monitoring/test_performance_tracker.py`
- **Only websocket connection types count toward websocket stats.** (1 connections) — `server/tests/unit/realtime/monitoring/test_performance_tracker.py`
- **Exception during stats calculation returns error payload.** (1 connections) — `server/tests/unit/realtime/monitoring/test_performance_tracker.py`
- **Recording events updates totals and sample lists.** (1 connections) — `server/tests/unit/realtime/monitoring/test_performance_tracker.py`

## Relationships

- [get_logger](get_logger.md) (8 shared connections)

## Source Files

- `server/tests/unit/realtime/monitoring/test_performance_tracker.py`

## Audit Trail

- EXTRACTED: 15 (71%)
- INFERRED: 6 (29%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*