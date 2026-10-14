# test_config_models.py

> 80 nodes

## Key Concepts

- **test_config_models.py** (32 connections) — `server/tests/unit/config/test_config_models.py`
- **_parse_env_list()** (12 connections) — `server/config/models/_helpers.py`
- **test_config_model_helpers.py** (11 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **_default_cors_origins()** (9 connections) — `server/config/models/_helpers.py`
- **_apply_url_fallback()** (8 connections) — `server/config/models/_helpers.py`
- **_validate_tls_files_and_maybe_update_url()** (8 connections) — `server/config/models/_helpers.py`
- **_make_game_config()** (7 connections) — `server/tests/unit/config/test_config_models.py`
- **.ensure_url_set()** (5 connections) — `server/config/models/server_db.py`
- **_parse_list_from_string()** (4 connections) — `server/config/models/_helpers.py`
- **.validate_tls_config()** (4 connections) — `server/config/models/nats.py`
- **test_game_config_grace_period_accepts_override()** (4 connections) — `server/tests/unit/config/test_config_models.py`
- **test_game_config_grace_period_rejects_over_max()** (4 connections) — `server/tests/unit/config/test_config_models.py`
- **test_game_config_grace_period_rejects_zero()** (4 connections) — `server/tests/unit/config/test_config_models.py`
- **test_apply_url_fallback_from_database_env()** (3 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **test_default_cors_origins_from_env()** (3 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **test_validate_tls_files_missing_cert_raises()** (3 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **test_validate_tls_updates_url_scheme()** (3 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **test_database_config_validate_pool_config_invalid()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_database_config_validate_pool_config_positive()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_database_config_validate_url_empty()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_database_config_validate_url_postgresql()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_default_cors_origins_no_env()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_default_cors_origins_with_env()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_game_config_default_tick_rate()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_game_config_grace_period_defaults()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- *... and 55 more nodes in this community*

## Relationships

- [NATSService](NATSService.md) (29 shared connections)
- [LoggingConfig](LoggingConfig.md) (3 shared connections)
- [ValueError](ValueError.md) (2 shared connections)

## Source Files

- `server/config/models/_helpers.py`
- `server/config/models/nats.py`
- `server/config/models/server_db.py`
- `server/tests/unit/config/test_config_model_helpers.py`
- `server/tests/unit/config/test_config_models.py`

## Audit Trail

- EXTRACTED: 133 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*