# admin command setstat

> 45 nodes

## Key Concepts

- **_helpers.py** (12 connections) — `server/config/models/_helpers.py`
- **_parse_env_list()** (12 connections) — `server/config/models/_helpers.py`
- **test_config_model_helpers.py** (11 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **_default_cors_origins()** (9 connections) — `server/config/models/_helpers.py`
- **_apply_url_fallback()** (8 connections) — `server/config/models/_helpers.py`
- **nats.py** (8 connections) — `server/config/models/nats.py`
- **_validate_tls_files_and_maybe_update_url()** (7 connections) — `server/config/models/_helpers.py`
- **_parse_list_from_string()** (4 connections) — `server/config/models/_helpers.py`
- **.ensure_url_set()** (4 connections) — `server/config/models/server_db.py`
- **Any** (3 connections)
- **.validate_tls_config()** (3 connections) — `server/config/models/nats.py`
- **test_default_cors_origins_from_env()** (3 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **test_apply_url_fallback_from_database_env()** (3 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **test_validate_tls_files_missing_cert_raises()** (3 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **test_validate_tls_updates_url_scheme()** (3 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **test_parse_env_list_none()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_parse_env_list_empty_string()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_parse_env_list_json()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_parse_env_list_csv()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_default_cors_origins_no_env()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_default_cors_origins_with_env()** (3 connections) — `server/tests/unit/config/test_config_models.py`
- **test_parse_list_from_string_json_and_csv()** (2 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **test_parse_env_list_empty_and_none()** (2 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **MonkeyPatch** (2 connections)
- **test_default_cors_origins_fallback()** (2 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- *... and 20 more nodes in this community*

## Relationships

- [config models rationale](config_models_rationale.md) (9 shared connections)
- [lucidity npc combat](lucidity_npc_combat.md) (7 shared connections)
- [models npc rationale](models_npc_rationale.md) (4 shared connections)
- [combat validator validators](combat_validator_validators.md) (2 shared connections)

## Source Files

- `server/config/models/_helpers.py`
- `server/config/models/nats.py`
- `server/config/models/server_db.py`
- `server/tests/unit/config/test_config_model_helpers.py`
- `server/tests/unit/config/test_config_models.py`

## Audit Trail

- EXTRACTED: 142 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*