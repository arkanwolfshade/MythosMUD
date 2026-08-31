# GameConfig

> 24 nodes

## Key Concepts

- **GameConfig** (19 connections) — `server/config/models/game.py`
- **field_validator** (8 connections)
- **.validate_aliases_dir()** (3 connections) — `server/config/models/game.py`
- **.validate_combat_alert_threshold()** (3 connections) — `server/config/models/game.py`
- **.validate_combat_error_threshold()** (3 connections) — `server/config/models/game.py`
- **.validate_combat_performance_threshold()** (3 connections) — `server/config/models/game.py`
- **.validate_combat_tick_interval()** (3 connections) — `server/config/models/game.py`
- **.validate_combat_timeout()** (3 connections) — `server/config/models/game.py`
- **.validate_combat_xp_multiplier()** (3 connections) — `server/config/models/game.py`
- **.validate_max_connections()** (3 connections) — `server/config/models/game.py`
- **test_game_config_tick_rate_accepts_positive_override()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_game_config_tick_rate_rejects_zero()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **BaseSettings** (1 connections)
- **Game-specific configuration.** (1 connections) — `server/config/models/game.py`
- **Validate combat alert threshold.** (1 connections) — `server/config/models/game.py`
- **Validate combat performance threshold.** (1 connections) — `server/config/models/game.py`
- **Validate combat error threshold.** (1 connections) — `server/config/models/game.py`
- **Validate max connections is reasonable.** (1 connections) — `server/config/models/game.py`
- **Validate aliases directory path.** (1 connections) — `server/config/models/game.py`
- **Validate combat tick interval.** (1 connections) — `server/config/models/game.py`
- **Validate combat timeout.** (1 connections) — `server/config/models/game.py`
- **Validate combat XP multiplier.** (1 connections) — `server/config/models/game.py`
- **Test GameConfig server_tick_rate accepts a valid positive override.** (1 connections) — `server/tests/unit/config/test_config_models.py`
- **Test GameConfig server_tick_rate rejects zero (#622: busy-spins the tick loop…** (1 connections) — `server/tests/unit/config/test_config_models.py`

## Relationships

- [test_config_models.py](test_config_models.py.md) (5 shared connections)
- [AppConfig](AppConfig.md) (4 shared connections)

## Source Files

- `server/config/models/game.py`
- `server/tests/unit/config/test_config_models.py`

## Audit Trail

- EXTRACTED: 38 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*