# Config Player Stats

> 4 nodes · cohesion 0.33

## Key Concepts

- **nats_config()** (3 connections) — `server/tests/unit/services/test_nats_service.py`
- **.validate_stat_range()** (2 connections) — `server/config/models/player_stats.py`
- **Validate stats are in valid range.** (1 connections) — `server/config/models/player_stats.py`
- **Create a NATSConfig instance.** (1 connections) — `server/tests/unit/services/test_nats_service.py`

## Relationships

- [[Application Config Settings]] (2 shared connections)
- [[Combat Domain Events]] (1 shared connections)

## Source Files

- `server/config/models/player_stats.py`
- `server/tests/unit/services/test_nats_service.py`

## Audit Trail

- EXTRACTED: 7 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
