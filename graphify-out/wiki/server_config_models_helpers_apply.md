# server config models helpers apply

> 43 nodes

## Key Concepts

- **_parse_env_list()** (12 connections) — `server/config/models/_helpers.py`
- **test_config_model_helpers.py** (12 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **_default_cors_origins()** (9 connections) — `server/config/models/_helpers.py`
- **_apply_url_fallback()** (8 connections) — `server/config/models/_helpers.py`
- **_validate_tls_files_and_maybe_update_url()** (7 connections) — `server/config/models/_helpers.py`
- **.ensure_url_set()** (5 connections) — `server/config/models/server_db.py`
- **_parse_list_from_string()** (4 connections) — `server/config/models/_helpers.py`
- **.validate_tls_config()** (4 connections) — `server/config/models/nats.py`
- **test_apply_url_fallback_from_database_env()** (3 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **test_default_cors_origins_from_env()** (3 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **test_validate_tls_files_missing_cert_raises()** (3 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **test_validate_tls_updates_url_scheme()** (3 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **test_default_cors_origins_no_env()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_default_cors_origins_with_env()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_parse_env_list_csv()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_parse_env_list_empty_string()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_parse_env_list_json()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_parse_env_list_none()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **Any** (3 connections)
- **test_apply_url_fallback_from_npc_url()** (2 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **test_apply_url_fallback_keeps_existing_url()** (2 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **test_default_cors_origins_fallback()** (2 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **test_parse_env_list_empty_and_none()** (2 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **test_parse_list_from_string_json_and_csv()** (2 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **MonkeyPatch** (2 connections)
- *... and 18 more nodes in this community*

## Relationships

- [server config init create config](server_config_init_create_config.md) (13 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (7 shared connections)
- [characterinfo](characterinfo.md) (1 shared connections)

## Source Files

- `server/config/models/_helpers.py`
- `server/config/models/nats.py`
- `server/config/models/server_db.py`
- `server/tests/unit/config/test_config_model_helpers.py`
- `server/tests/unit/config/test_config_models.py`

## Audit Trail

- EXTRACTED: 73 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*