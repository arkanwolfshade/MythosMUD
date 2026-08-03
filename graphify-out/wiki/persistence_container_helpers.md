# persistence container helpers

> 8 nodes

## Key Concepts

- **._build_connection_stats()** (10 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **.get_connection_stats()** (4 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._session_connection_distribution()** (3 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **._connection_age_extrema()** (3 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Count how many sessions have each connection-count size.** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Return (avg, max, min) connection ages; zeros when the list is empty.** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Compose connection statistics payload (extracted to keep get_connection_stats CC** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`
- **Get comprehensive connection statistics.          Args:             player_webso** (1 connections) — `server/realtime/monitoring/statistics_aggregator.py`

## Relationships

- [target services resolution](target_services_resolution.md) (6 shared connections)
- [player game schema](player_game_schema.md) (3 shared connections)
- [game magic regeneration](game_magic_regeneration.md) (1 shared connections)

## Source Files

- `server/realtime/monitoring/statistics_aggregator.py`

## Audit Trail

- EXTRACTED: 24 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*