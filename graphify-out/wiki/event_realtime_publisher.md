# event realtime publisher

> 48 nodes

## Key Concepts

- **StatisticsAggregator** (29 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._build_connection_stats()** (10 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **.get_connection_health_stats()** (8 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._compose_memory_stats()** (7 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **MemoryStatsSnapshot** (6 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **UUID** (6 connections)
- **._memory_connections_section()** (6 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._memory_sessions_section()** (5 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._safe_ratio()** (5 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **.get_memory_stats()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._count_orphaned_connections()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **.get_connection_stats()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._analyze_connection_health()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._analyze_connection_ages()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._build_health_trends()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._build_health_stats_response()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._memory_monitor_config_section()** (3 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._session_connection_distribution()** (3 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._connection_age_extrema()** (3 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._analyze_connection_types()** (3 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._analyze_session_health()** (3 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._calculate_session_health_percentages()** (3 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **.__init__()** (2 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **.get_memory_alerts()** (2 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **TypedDict** (1 connections)
- *... and 23 more nodes in this community*

## Relationships

- [services chat logger](services_chat_logger.md) (3 shared connections)
- [connection disconnection realtime](connection_disconnection_realtime.md) (3 shared connections)
- [services npc startup](services_npc_startup.md) (2 shared connections)
- [cleanup combat handler](cleanup_combat_handler.md) (2 shared connections)

## Source Files

- `server/realtime/monitoring/statistics_aggregator.py`

## Audit Trail

- EXTRACTED: 154 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*