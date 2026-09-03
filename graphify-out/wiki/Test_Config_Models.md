# Test Config Models

> 71 nodes

## Key Concepts

- **test_config_models.py** (25 connections) — `server/tests/unit/config/test_config_models.py`
- **GameConfig** (21 connections) — `server/config/models/game.py`
- **field_validator** (9 connections)
- **_make_game_config()** (6 connections) — `server/tests/unit/config/test_config_models.py`
- **test_game_config_grace_period_accepts_override()** (4 connections) — `server/tests/unit/config/test_config_models.py`
- **test_game_config_grace_period_rejects_over_max()** (4 connections) — `server/tests/unit/config/test_config_models.py`
- **test_game_config_grace_period_rejects_zero()** (4 connections) — `server/tests/unit/config/test_config_models.py`
- **.validate_aliases_dir()** (3 connections) — `server/config/models/game.py`
- **.validate_combat_alert_threshold()** (3 connections) — `server/config/models/game.py`
- **.validate_combat_error_threshold()** (3 connections) — `server/config/models/game.py`
- **.validate_combat_performance_threshold()** (3 connections) — `server/config/models/game.py`
- **.validate_combat_tick_interval()** (3 connections) — `server/config/models/game.py`
- **.validate_combat_timeout()** (3 connections) — `server/config/models/game.py`
- **.validate_combat_xp_multiplier()** (3 connections) — `server/config/models/game.py`
- **.validate_grace_period_seconds()** (3 connections) — `server/config/models/game.py`
- **.validate_max_connections()** (3 connections) — `server/config/models/game.py`
- **test_game_config_default_tick_rate()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_game_config_grace_period_defaults()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_game_config_tick_rate_accepts_positive_override()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_game_config_tick_rate_rejects_negative()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_game_config_tick_rate_rejects_zero()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **parametrize** (3 connections)
- **test_database_config_validate_pool_config_invalid()** (2 connections) — `server/tests/unit/config/test_config_models.py`
- **test_database_config_validate_pool_config_positive()** (2 connections) — `server/tests/unit/config/test_config_models.py`
- **test_database_config_validate_url_empty()** (2 connections) — `server/tests/unit/config/test_config_models.py`
- *... and 46 more nodes in this community*

## Relationships

- [Cors](Cors.md) (4 shared connections)
- [Container Exception Handling](Container_Exception_Handling.md) (1 shared connections)

## Source Files

- `server/config/models/game.py`
- `server/tests/unit/config/test_config_models.py`

## Audit Trail

- EXTRACTED: 92 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*