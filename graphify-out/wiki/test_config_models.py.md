# test_config_models.py

> 102 nodes

## Key Concepts

- **test_config_models.py** (29 connections) — `server/tests/unit/config/test_config_models.py`
- **GameConfig** (22 connections) — `server/config/models/game.py`
- **_parse_env_list()** (12 connections) — `server/config/models/_helpers.py`
- **test_config_model_helpers.py** (11 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **_default_cors_origins()** (9 connections) — `server/config/models/_helpers.py`
- **field_validator** (9 connections)
- **_apply_url_fallback()** (8 connections) — `server/config/models/_helpers.py`
- **_validate_tls_files_and_maybe_update_url()** (7 connections) — `server/config/models/_helpers.py`
- **_make_game_config()** (6 connections) — `server/tests/unit/config/test_config_models.py`
- **.ensure_url_set()** (5 connections) — `server/config/models/server_db.py`
- **_parse_list_from_string()** (4 connections) — `server/config/models/_helpers.py`
- **.validate_tls_config()** (4 connections) — `server/config/models/nats.py`
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
- **test_apply_url_fallback_from_database_env()** (3 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- *... and 77 more nodes in this community*

## Relationships

- [NATSService](NATSService.md) (26 shared connections)

## Source Files

- `server/config/models/_helpers.py`
- `server/config/models/game.py`
- `server/config/models/nats.py`
- `server/config/models/server_db.py`
- `server/tests/unit/config/test_config_model_helpers.py`
- `server/tests/unit/config/test_config_models.py`

## Audit Trail

- EXTRACTED: 162 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*