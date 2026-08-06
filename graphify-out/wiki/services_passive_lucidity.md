# services passive lucidity

> 10 nodes

## Key Concepts

- **PlayerStatsConfig** (9 connections) — `server/config/models/player_stats.py`
- **.to_dict()** (3 connections) — `server/config/models/player_stats.py`
- **.validate_stat_range()** (2 connections) — `server/config/models/player_stats.py`
- **.validate_derived_stats()** (2 connections) — `server/config/models/player_stats.py`
- **BaseSettings** (1 connections)
- **Any** (1 connections)
- **Default player statistics configuration.** (1 connections) — `server/config/models/player_stats.py`
- **Validate stats are in valid range.** (1 connections) — `server/config/models/player_stats.py`
- **Validate derived stats values.** (1 connections) — `server/config/models/player_stats.py`
- **Convert to dictionary format expected by game code.** (1 connections) — `server/config/models/player_stats.py`

## Relationships

- [websocket validation realtime](websocket_validation_realtime.md) (3 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (1 shared connections)

## Source Files

- `server/config/models/player_stats.py`

## Audit Trail

- EXTRACTED: 21 (95%)
- INFERRED: 1 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*