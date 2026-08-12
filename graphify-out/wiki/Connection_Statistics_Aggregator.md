# Connection Statistics Aggregator

> 28 nodes

## Key Concepts

- **StatisticsAggregator** (20 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **.get_connection_health_stats()** (9 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Any** (8 connections)
- **._build_health_stats_response()** (5 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **.get_memory_stats()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **.get_connection_stats()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._analyze_connection_health()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._analyze_connection_types()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._analyze_connection_ages()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._analyze_session_health()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **UUID** (3 connections)
- **._calculate_session_health_percentages()** (3 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._build_health_trends()** (3 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **.__init__()** (2 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **.get_memory_alerts()** (2 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Aggregates statistics from connection management components.      This class pro** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Initialize the statistics aggregator.          Args:             memory_monitor:** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Get comprehensive memory and connection statistics.          Args:             a** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Get comprehensive connection statistics.          Args:             player_webso** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Analyze connection health distribution.          Args:             connection_me** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Analyze connection types.          Args:             connection_metadata: Connec** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Analyze connection ages.          Args:             connection_metadata: Connect** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Analyze session health.          Args:             connection_metadata: Connecti** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Calculate session health percentages.          Args:             session_health:** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Build health trends statistics.          Args:             connection_ages: List** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- *... and 3 more nodes in this community*

## Relationships

- [Client Event Store](Client_Event_Store.md) (3 shared connections)
- [Game State Provider Tests](Game_State_Provider_Tests.md) (2 shared connections)
- [Test Refactoring Status](Test_Refactoring_Status.md) (2 shared connections)
- [Validate Calendar](Validate_Calendar.md) (1 shared connections)

## Source Files

- `server/realtime/monitoring/statistics_aggregator.py`

## Audit Trail

- EXTRACTED: 91 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*