# Validate Calendar

> 19 nodes

## Key Concepts

- **PerformanceTracker** (17 connections) — `server/realtime/monitoring/performance_tracker.py`
- **._trim_samples()** (7 connections) — `server/realtime/monitoring/performance_tracker.py`
- **.record_connection_establishment()** (3 connections) — `server/realtime/monitoring/performance_tracker.py`
- **.record_message_delivery()** (3 connections) — `server/realtime/monitoring/performance_tracker.py`
- **.record_disconnection()** (3 connections) — `server/realtime/monitoring/performance_tracker.py`
- **.record_session_switch()** (3 connections) — `server/realtime/monitoring/performance_tracker.py`
- **.record_health_check()** (3 connections) — `server/realtime/monitoring/performance_tracker.py`
- **.get_stats()** (3 connections) — `server/realtime/monitoring/performance_tracker.py`
- **.__init__()** (2 connections) — `server/realtime/monitoring/performance_tracker.py`
- **Any** (1 connections)
- **Tracks performance metrics for connection management operations.      This class** (1 connections) — `server/realtime/monitoring/performance_tracker.py`
- **Initialize the performance tracker.          Args:             max_samples: Maxi** (1 connections) — `server/realtime/monitoring/performance_tracker.py`
- **Record a connection establishment event.          Args:             connection_t** (1 connections) — `server/realtime/monitoring/performance_tracker.py`
- **Record a message delivery event.          Args:             message_type: Type o** (1 connections) — `server/realtime/monitoring/performance_tracker.py`
- **Record a disconnection event.          Args:             connection_type: Type o** (1 connections) — `server/realtime/monitoring/performance_tracker.py`
- **Record a session switch event.          Args:             duration_ms: Duration** (1 connections) — `server/realtime/monitoring/performance_tracker.py`
- **Record a health check event.          Args:             duration_ms: Duration in** (1 connections) — `server/realtime/monitoring/performance_tracker.py`
- **Trim samples to prevent unbounded memory growth.          Args:             metr** (1 connections) — `server/realtime/monitoring/performance_tracker.py`
- **Get comprehensive performance statistics with calculated averages.          Retu** (1 connections) — `server/realtime/monitoring/performance_tracker.py`

## Relationships

- [Client Event Store](Client_Event_Store.md) (4 shared connections)
- [Game State Provider Tests](Game_State_Provider_Tests.md) (2 shared connections)
- [Typography Layout Spec](Typography_Layout_Spec.md) (1 shared connections)
- [Connection Statistics Aggregator](Connection_Statistics_Aggregator.md) (1 shared connections)

## Source Files

- `server/realtime/monitoring/performance_tracker.py`

## Audit Trail

- EXTRACTED: 52 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*