# _helpers.py

> 26 nodes

## Key Concepts

- **_helpers.py** (12 connections) — `server/config/models/_helpers.py`
- **test_config_model_helpers.py** (12 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **server_db.py** (10 connections) — `server/config/models/server_db.py`
- **_apply_url_fallback()** (8 connections) — `server/config/models/_helpers.py`
- **_validate_tls_files_and_maybe_update_url()** (7 connections) — `server/config/models/_helpers.py`
- **_parse_list_from_string()** (4 connections) — `server/config/models/_helpers.py`
- **.validate_tls_config()** (4 connections) — `server/config/models/nats.py`
- **test_apply_url_fallback_from_database_env()** (3 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **test_default_cors_origins_from_env()** (3 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **test_validate_tls_files_missing_cert_raises()** (3 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **test_validate_tls_updates_url_scheme()** (3 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **Any** (3 connections)
- **test_apply_url_fallback_from_npc_url()** (2 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **test_apply_url_fallback_keeps_existing_url()** (2 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **test_parse_env_list_empty_and_none()** (2 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **test_parse_list_from_string_json_and_csv()** (2 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **MonkeyPatch** (2 connections)
- **Path** (2 connections)
- **model_validator** (1 connections)
- **Shared helpers for config model parsing and validation. Used by server_db,…** (1 connections) — `server/config/models/_helpers.py`
- **Parse non-empty string as JSON list or CSV. Used by _parse_env_list.** (1 connections) — `server/config/models/_helpers.py`
- **If url is missing, set it from npc_url in data or from DATABASE_* env vars.…** (1 connections) — `server/config/models/_helpers.py`
- **When TLS is enabled, validate cert/key (and optional CA) exist and update url…** (1 connections) — `server/config/models/_helpers.py`
- **Validate TLS configuration is complete when enabled.** (1 connections) — `server/config/models/nats.py`
- **Server and database configuration models.** (1 connections) — `server/config/models/server_db.py`
- *... and 1 more nodes in this community*

## Relationships

- [test_config_models.py](test_config_models.py.md) (8 shared connections)
- [config/models/__init__.py](config-models-__init__.py.md) (5 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [DatabaseConfig](DatabaseConfig.md) (2 shared connections)
- [NATSService](NATSService.md) (1 shared connections)
- [BaseCommand](BaseCommand.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/config/models/_helpers.py`
- `server/config/models/nats.py`
- `server/config/models/server_db.py`
- `server/tests/unit/config/test_config_model_helpers.py`

## Audit Trail

- EXTRACTED: 57 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*