# target services resolution

> 18 nodes

## Key Concepts

- **StatisticsAggregator** (29 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **.get_connection_health_stats()** (8 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._analyze_connection_health()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._analyze_connection_ages()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._analyze_connection_types()** (3 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._analyze_session_health()** (3 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._calculate_session_health_percentages()** (3 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **.__init__()** (2 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **.get_memory_alerts()** (2 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Aggregates statistics from connection management components.      This class pro** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Initialize the statistics aggregator.          Args:             memory_monitor:** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Analyze connection health distribution.          Args:             connection_me** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Analyze connection types.          Args:             connection_metadata: Connec** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Analyze connection ages.          Args:             connection_metadata: Connect** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Analyze session health.          Args:             connection_metadata: Connecti** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Calculate session health percentages.          Args:             session_health:** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Get comprehensive connection health statistics.          Args:             conne** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Get memory-related alerts.          Args:             connection_timestamps: Con** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`

## Relationships

- [persistence container helpers](persistence_container_helpers.md) (6 shared connections)
- [Room Broadcast](Room_Broadcast.md) (5 shared connections)
- [player game schema](player_game_schema.md) (4 shared connections)
- [game magic regeneration](game_magic_regeneration.md) (3 shared connections)
- [subject admin controller](subject_admin_controller.md) (3 shared connections)
- [services nats service](services_nats_service.md) (2 shared connections)

## Source Files

- `server/realtime/monitoring/statistics_aggregator.py`

## Audit Trail

- EXTRACTED: 66 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*