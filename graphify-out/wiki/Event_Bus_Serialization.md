# Event Bus Serialization

> 9 nodes · cohesion 0.01

## Key Concepts

- **UUID** (17 connections) — `server/services/player_respawn_service.py`
- **UUID** (9 connections) — `server/services/player_death_service.py`
- **Player** (9 connections) — `server/services/player_respawn_service.py`
- **AsyncSession** (8 connections) — `server/services/player_respawn_service.py`
- **AsyncSession** (7 connections) — `server/services/player_death_service.py`
- **Any** (6 connections) — `server/services/player_death_service.py`
- **Player** (6 connections) — `server/services/player_death_service.py`
- **datetime** (3 connections) — `server/services/player_respawn_service.py`
- **Exception** (1 connections) — `server/structured_logging/enhanced_logging_config.py`

## Relationships

- No strong cross-community connections detected

## Source Files

- `server/services/player_death_service.py`
- `server/services/player_respawn_service.py`
- `server/structured_logging/enhanced_logging_config.py`

## Audit Trail

- EXTRACTED: 50 (76%)
- INFERRED: 16 (24%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*