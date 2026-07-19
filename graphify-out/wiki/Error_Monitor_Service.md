# Error Monitor Service

> 28 nodes · cohesion 0.14

## Key Concepts

- **ErrorMonitor** (13 connections) — `scripts/error_monitoring.py`
- **.calculate_error_rate()** (10 connections) — `scripts/error_monitoring.py`
- **main()** (8 connections) — `scripts/error_monitoring.py`
- **.check_alerts()** (7 connections) — `scripts/error_monitoring.py`
- **._parse_recent_errors()** (7 connections) — `scripts/error_monitoring.py`
- **Any** (7 connections) — `scripts/error_monitoring.py`
- **.detect_error_trends()** (6 connections) — `scripts/error_monitoring.py`
- **.monitor_continuously()** (6 connections) — `scripts/error_monitoring.py`
- **._find_recent_error_logs()** (5 connections) — `scripts/error_monitoring.py`
- **._categorize_error()** (4 connections) — `scripts/error_monitoring.py`
- **._determine_severity()** (4 connections) — `scripts/error_monitoring.py`
- **.__init__()** (4 connections) — `scripts/error_monitoring.py`
- **._parse_log_line()** (4 connections) — `scripts/error_monitoring.py`
- **Path** (4 connections) — `scripts/error_monitoring.py`
- **error_monitoring.py** (3 connections) — `scripts/error_monitoring.py`
- **datetime** (3 connections) — `scripts/error_monitoring.py`
- **Detect error trends over time.          Returns trend analysis results.** (1 connections) — `scripts/error_monitoring.py`
- **Check for alert conditions.          Returns list of active alerts.** (1 connections) — `scripts/error_monitoring.py`
- **Monitor errors continuously for a specified duration.          Args:** (1 connections) — `scripts/error_monitoring.py`
- **Real-time error monitoring system for MythosMUD.      This monitor can track err** (1 connections) — `scripts/error_monitoring.py`
- **Find error log files that have been modified since the given time.** (1 connections) — `scripts/error_monitoring.py`
- **Parse recent errors from a log file.** (1 connections) — `scripts/error_monitoring.py`
- **Parse a single log line and extract error information.** (1 connections) — `scripts/error_monitoring.py`
- **Categorize an error based on its content.** (1 connections) — `scripts/error_monitoring.py`
- **Initialize the error monitor.          Args:             log_dir: Directory cont** (1 connections) — `scripts/error_monitoring.py`
- *... and 3 more nodes in this community*

## Relationships

- [[Message Queue Cleanup]] (1 shared connections)

## Source Files

- `scripts/error_monitoring.py`

## Audit Trail

- EXTRACTED: 106 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
