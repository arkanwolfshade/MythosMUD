# test_config_models.py

> 30 nodes

## Key Concepts

- **test_config_models.py** (25 connections) — `server/tests/unit/config/test_config_models.py`
- **ServerConfig** (12 connections) — `server/config/models/server_db.py`
- **_parse_env_list()** (12 connections) — `server/config/models/_helpers.py`
- **_default_cors_origins()** (9 connections) — `server/config/models/_helpers.py`
- **test_default_cors_origins_no_env()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_default_cors_origins_with_env()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_parse_env_list_csv()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_parse_env_list_empty_string()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_parse_env_list_json()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_parse_env_list_none()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_server_config_default_host()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_server_config_validate_port_invalid_high()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_server_config_validate_port_invalid_low()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_server_config_validate_port_valid()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_default_cors_origins_fallback()** (2 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **BaseSettings** (2 connections)
- **Parse a string from the environment as JSON list or CSV.** (1 connections) — `server/config/models/_helpers.py`
- **Derive default CORS origins with environment taking precedence.** (1 connections) — `server/config/models/_helpers.py`
- **Server network configuration.** (1 connections) — `server/config/models/server_db.py`
- **Unit tests for configuration models.** (1 connections) — `server/tests/unit/config/test_config_models.py`
- **Test parsing None as env list.** (1 connections) — `server/tests/unit/config/test_config_models.py`
- **Test parsing empty string as env list.** (1 connections) — `server/tests/unit/config/test_config_models.py`
- **Test parsing JSON list.** (1 connections) — `server/tests/unit/config/test_config_models.py`
- **Test parsing CSV list.** (1 connections) — `server/tests/unit/config/test_config_models.py`
- **Test default CORS origins when no env vars set.** (1 connections) — `server/tests/unit/config/test_config_models.py`
- *... and 5 more nodes in this community*

## Relationships

- [_helpers.py](_helpers.py.md) (8 shared connections)
- [DatabaseConfig](DatabaseConfig.md) (7 shared connections)
- [GameConfig](GameConfig.md) (5 shared connections)
- [config/models/__init__.py](config-models-__init__.py.md) (4 shared connections)
- [AppConfig](AppConfig.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/config/models/_helpers.py`
- `server/config/models/server_db.py`
- `server/tests/unit/config/test_config_model_helpers.py`
- `server/tests/unit/config/test_config_models.py`

## Audit Trail

- EXTRACTED: 65 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*