# FastAPI Best Practices

> 11 nodes

## Key Concepts

- **PlayerStatsConfig** (7 connections) — `server/config/models/player_stats.py`
- **.to_dict()** (3 connections) — `server/config/models/player_stats.py`
- **.validate_derived_stats()** (3 connections) — `server/config/models/player_stats.py`
- **.validate_stat_range()** (3 connections) — `server/config/models/player_stats.py`
- **field_validator** (2 connections)
- **Any** (1 connections)
- **BaseSettings** (1 connections)
- **Default player statistics configuration.** (1 connections) — `server/config/models/player_stats.py`
- **Validate stats are in valid range.** (1 connections) — `server/config/models/player_stats.py`
- **Validate derived stats values.** (1 connections) — `server/config/models/player_stats.py`
- **Convert to dictionary format expected by game code.** (1 connections) — `server/config/models/player_stats.py`

## Relationships

- [generate_invites_db.py](generate_invites_db.py.md) (2 shared connections)

## Source Files

- `server/config/models/player_stats.py`

## Audit Trail

- EXTRACTED: 13 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*