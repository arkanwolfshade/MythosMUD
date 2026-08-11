# Map Editing Hooks

> 29 nodes

## Key Concepts

- **GameConfig** (15 connections) — `server/config/models/game.py`
- **PlayerStatsConfig** (9 connections) — `server/config/models/player_stats.py`
- **.to_dict()** (3 connections) — `server/config/models/player_stats.py`
- **.validate_max_connections()** (2 connections) — `server/config/models/game.py`
- **.validate_aliases_dir()** (2 connections) — `server/config/models/game.py`
- **.validate_combat_tick_interval()** (2 connections) — `server/config/models/game.py`
- **.validate_combat_timeout()** (2 connections) — `server/config/models/game.py`
- **.validate_combat_xp_multiplier()** (2 connections) — `server/config/models/game.py`
- **.validate_combat_alert_threshold()** (2 connections) — `server/config/models/game.py`
- **.validate_combat_performance_threshold()** (2 connections) — `server/config/models/game.py`
- **.validate_combat_error_threshold()** (2 connections) — `server/config/models/game.py`
- **.validate_stat_range()** (2 connections) — `server/config/models/player_stats.py`
- **.validate_derived_stats()** (2 connections) — `server/config/models/player_stats.py`
- **BaseSettings** (1 connections)
- **Game-specific configuration.** (1 connections) — `server/config/models/game.py`
- **Validate max connections is reasonable.** (1 connections) — `server/config/models/game.py`
- **Validate aliases directory path.** (1 connections) — `server/config/models/game.py`
- **Validate combat tick interval.** (1 connections) — `server/config/models/game.py`
- **Validate combat timeout.** (1 connections) — `server/config/models/game.py`
- **Validate combat XP multiplier.** (1 connections) — `server/config/models/game.py`
- **Validate combat alert threshold.** (1 connections) — `server/config/models/game.py`
- **Validate combat performance threshold.** (1 connections) — `server/config/models/game.py`
- **Validate combat error threshold.** (1 connections) — `server/config/models/game.py`
- **BaseSettings** (1 connections)
- **Any** (1 connections)
- *... and 4 more nodes in this community*

## Relationships

- [Pydantic Error Handlers](Pydantic_Error_Handlers.md) (6 shared connections)
- [Command Parser](Command_Parser.md) (3 shared connections)

## Source Files

- `server/config/models/game.py`
- `server/config/models/player_stats.py`

## Audit Trail

- EXTRACTED: 61 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*