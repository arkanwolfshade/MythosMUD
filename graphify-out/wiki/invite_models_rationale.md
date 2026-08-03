# invite models rationale

> 19 nodes

## Key Concepts

- **GameConfig** (15 connections) — `server/config/models/game.py`
- **.validate_max_connections()** (2 connections) — `server/config/models/game.py`
- **.validate_aliases_dir()** (2 connections) — `server/config/models/game.py`
- **.validate_combat_tick_interval()** (2 connections) — `server/config/models/game.py`
- **.validate_combat_timeout()** (2 connections) — `server/config/models/game.py`
- **.validate_combat_xp_multiplier()** (2 connections) — `server/config/models/game.py`
- **.validate_combat_alert_threshold()** (2 connections) — `server/config/models/game.py`
- **.validate_combat_performance_threshold()** (2 connections) — `server/config/models/game.py`
- **.validate_combat_error_threshold()** (2 connections) — `server/config/models/game.py`
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

## Relationships

- [command inventory factories](command_inventory_factories.md) (3 shared connections)
- [player event handlers](player_event_handlers.md) (2 shared connections)

## Source Files

- `server/config/models/game.py`

## Audit Trail

- EXTRACTED: 40 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*