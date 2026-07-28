# Runbooks Item System

> 9 nodes · cohesion 0.22

## Key Concepts

- **Any** (5 connections)
- **_coerce_row_stats()** (4 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **_defaulted_numerics()** (4 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **_defaulted_strings()** (4 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **_parse_equipped_safely()** (4 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **Extract and coerce stats from row. Returns empty dict if not a dict.** (1 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **Parse equipped_json to dict. Returns empty dict on parse error or invalid type.** (1 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **Extract string fields with defaults: inventory_json, equipped_json, current_room** (1 connections) — `server/persistence/repositories/player_repository_mappers.py`
- **Extract numeric/bool fields with defaults: experience_points, level, is_admin, p** (1 connections) — `server/persistence/repositories/player_repository_mappers.py`

## Relationships

- [Realtime Connection Impl](Realtime_Connection_Impl.md) (5 shared connections)
- [Event Bus Serialization](Event_Bus_Serialization.md) (4 shared connections)

## Source Files

- `server/persistence/repositories/player_repository_mappers.py`

## Audit Trail

- EXTRACTED: 25 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*