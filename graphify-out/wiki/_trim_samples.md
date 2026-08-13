# ._trim_samples

> 12 nodes

## Key Concepts

- **._trim_samples()** (7 connections) — `server/realtime/monitoring/performance_tracker.py`
- **.record_connection_establishment()** (3 connections) — `server/realtime/monitoring/performance_tracker.py`
- **.record_disconnection()** (3 connections) — `server/realtime/monitoring/performance_tracker.py`
- **.record_health_check()** (3 connections) — `server/realtime/monitoring/performance_tracker.py`
- **.record_message_delivery()** (3 connections) — `server/realtime/monitoring/performance_tracker.py`
- **.record_session_switch()** (3 connections) — `server/realtime/monitoring/performance_tracker.py`
- **Record a session switch event. Args: duration_ms: Duration in milliseconds** (1 connections) — `server/realtime/monitoring/performance_tracker.py`
- **Record a health check event. Args: duration_ms: Duration in milliseconds** (1 connections) — `server/realtime/monitoring/performance_tracker.py`
- **Trim samples to prevent unbounded memory growth. Args: metric_key: Key in…** (1 connections) — `server/realtime/monitoring/performance_tracker.py`
- **Record a connection establishment event. Args: connection_type: Type of…** (1 connections) — `server/realtime/monitoring/performance_tracker.py`
- **Record a message delivery event. Args: message_type: Type of message…** (1 connections) — `server/realtime/monitoring/performance_tracker.py`
- **Record a disconnection event. Args: connection_type: Type of connection…** (1 connections) — `server/realtime/monitoring/performance_tracker.py`

## Relationships

- [get_logger](get_logger.md) (6 shared connections)

## Source Files

- `server/realtime/monitoring/performance_tracker.py`

## Audit Trail

- EXTRACTED: 17 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*