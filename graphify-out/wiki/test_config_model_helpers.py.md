# test_config_model_helpers.py

> 15 nodes

## Key Concepts

- **test_config_model_helpers.py** (12 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **_apply_url_fallback()** (8 connections) — `server/config/models/_helpers.py`
- **_validate_tls_files_and_maybe_update_url()** (7 connections) — `server/config/models/_helpers.py`
- **test_apply_url_fallback_from_database_env()** (3 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **test_default_cors_origins_from_env()** (3 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **test_validate_tls_files_missing_cert_raises()** (3 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **test_validate_tls_updates_url_scheme()** (3 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **Any** (3 connections)
- **test_apply_url_fallback_from_npc_url()** (2 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **test_apply_url_fallback_keeps_existing_url()** (2 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **MonkeyPatch** (2 connections)
- **Path** (2 connections)
- **If url is missing, set it from npc_url in data or from DATABASE_* env vars.…** (1 connections) — `server/config/models/_helpers.py`
- **When TLS is enabled, validate cert/key (and optional CA) exist and update url…** (1 connections) — `server/config/models/_helpers.py`
- **Unit tests for server.config.models._helpers.** (1 connections) — `server/tests/unit/config/test_config_model_helpers.py`

## Relationships

- [get_logger](get_logger.md) (5 shared connections)
- [_parse_env_list](_parse_env_list.md) (3 shared connections)
- [_default_cors_origins](_default_cors_origins.md) (2 shared connections)
- [.ensure_url_set](ensure_url_set.md) (1 shared connections)
- [.validate_tls_config](validate_tls_config.md) (1 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/config/models/_helpers.py`
- `server/tests/unit/config/test_config_model_helpers.py`

## Audit Trail

- EXTRACTED: 33 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*