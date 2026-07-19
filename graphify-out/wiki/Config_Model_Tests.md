# Config Model Tests

> 53 nodes · cohesion 0.05

## Key Concepts

- **test_config_models.py** (19 connections) — `server/tests/unit/config/test_config_models.py`
- **ServerConfig** (17 connections) — `server/config/models/server_db.py`
- **_helpers.py** (11 connections) — `server/config/models/_helpers.py`
- **_parse_env_list()** (11 connections) — `server/config/models/_helpers.py`
- **server_db.py** (9 connections) — `server/config/models/server_db.py`
- **_default_cors_origins()** (7 connections) — `server/config/models/_helpers.py`
- **_apply_url_fallback()** (5 connections) — `server/config/models/_helpers.py`
- **_validate_tls_files_and_maybe_update_url()** (5 connections) — `server/config/models/_helpers.py`
- **.ensure_url_set()** (4 connections) — `server/config/models/server_db.py`
- **test_database_config_validate_pool_config_invalid()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_database_config_validate_pool_config_positive()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_database_config_validate_url_empty()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_database_config_validate_url_postgresql()** (3 connections) — `server/tests/unit/config/test_config_models.py`
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
- **_parse_list_from_string()** (3 connections) — `server/config/models/_helpers.py`
- **.validate_tls_config()** (3 connections) — `server/config/models/nats.py`
- *... and 28 more nodes in this community*

## Relationships

- [[Application Config Settings]] (24 shared connections)
- [[NPC Admin API]] (4 shared connections)

## Source Files

- `server/config/models/_helpers.py`
- `server/config/models/nats.py`
- `server/config/models/server_db.py`
- `server/tests/unit/config/test_config_models.py`

## Audit Trail

- EXTRACTED: 162 (96%)
- INFERRED: 6 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
