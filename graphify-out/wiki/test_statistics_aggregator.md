# test statistics aggregator

> 103 nodes

## Key Concepts

- **connection_initialization.py** (38 connections) — `server/realtime/connection_initialization.py`
- **StatisticsAggregator** (29 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **connection_cleaner.py** (22 connections) — `server/realtime/maintenance/connection_cleaner.py`
- **statistics_aggregator.py** (22 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **room_subscription_manager.py** (18 connections) — `server/realtime/room_subscription_manager.py`
- **rate_limiter.py** (14 connections) — `server/realtime/rate_limiter.py`
- **test_statistics_aggregator.py** (14 connections) — `server/tests/unit/realtime/monitoring/test_statistics_aggregator.py`
- **MemoryMonitor** (13 connections) — `server/realtime/memory_monitor.py`
- **._build_connection_stats()** (10 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **memory_monitor.py** (9 connections) — `server/realtime/memory_monitor.py`
- **.get_connection_health_stats()** (8 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._compose_memory_stats()** (7 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **MemoryStatsSnapshot** (6 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **UUID** (6 connections)
- **._memory_connections_section()** (6 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._memory_sessions_section()** (5 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._safe_ratio()** (5 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **.get_memory_usage()** (4 connections) — `server/realtime/memory_monitor.py`
- **.get_memory_alerts()** (4 connections) — `server/realtime/memory_monitor.py`
- **.get_memory_stats()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._count_orphaned_connections()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **.get_connection_stats()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._analyze_connection_health()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._analyze_connection_ages()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._build_health_trends()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- *... and 78 more nodes in this community*

## Relationships

- [world](world.md) (25 shared connections)
- [test connection cleaner](test_connection_cleaner.md) (11 shared connections)
- [connection disconnection](connection_disconnection.md) (8 shared connections)
- [Player](Player.md) (8 shared connections)
- [get current tick()](get_current_tick%28%29.md) (6 shared connections)
- [NPCDefinitionCRUDMixin](NPCDefinitionCRUDMixin.md) (5 shared connections)
- [Custom user manager for MythosMUD.](Custom_user_manager_for_MythosMUD.md) (5 shared connections)
- [Any](Any.md) (4 shared connections)
- [nats config()](nats_config%28%29.md) (3 shared connections)
- [SendPersonalMessage](SendPersonalMessage.md) (3 shared connections)
- [UUID](UUID.md) (2 shared connections)
- [real time](real_time.md) (2 shared connections)

## Source Files

- `server/realtime/connection_initialization.py`
- `server/realtime/maintenance/connection_cleaner.py`
- `server/realtime/memory_monitor.py`
- `server/realtime/monitoring/statistics_aggregator.py`
- `server/realtime/rate_limiter.py`
- `server/realtime/room_subscription_manager.py`
- `server/tests/unit/realtime/monitoring/test_statistics_aggregator.py`

## Audit Trail

- EXTRACTED: 380 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*