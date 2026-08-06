# calendar models rationale

> 20 nodes

## Key Concepts

- **test_config_model_helpers.py** (11 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **_apply_url_fallback()** (8 connections) — `server/config/models/_helpers.py`
- **_validate_tls_files_and_maybe_update_url()** (7 connections) — `server/config/models/_helpers.py`
- **_parse_list_from_string()** (4 connections) — `server/config/models/_helpers.py`
- **Any** (3 connections)
- **.validate_tls_config()** (3 connections) — `server/config/models/nats.py`
- **test_default_cors_origins_from_env()** (3 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **test_apply_url_fallback_from_database_env()** (3 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **test_validate_tls_files_missing_cert_raises()** (3 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **test_validate_tls_updates_url_scheme()** (3 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **test_parse_list_from_string_json_and_csv()** (2 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **MonkeyPatch** (2 connections)
- **test_apply_url_fallback_from_npc_url()** (2 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **test_apply_url_fallback_keeps_existing_url()** (2 connections) — `server/tests/unit/config/test_config_model_helpers.py`
- **Path** (2 connections)
- **Parse non-empty string as JSON list or CSV. Used by _parse_env_list.** (1 connections) — `server/config/models/_helpers.py`
- **If url is missing, set it from npc_url in data or from DATABASE_* env vars.** (1 connections) — `server/config/models/_helpers.py`
- **When TLS is enabled, validate cert/key (and optional CA) exist and update url to** (1 connections) — `server/config/models/_helpers.py`
- **Validate TLS configuration is complete when enabled.** (1 connections) — `server/config/models/nats.py`
- **Unit tests for server.config.models._helpers.** (1 connections) — `server/tests/unit/config/test_config_model_helpers.py`

## Relationships

- [Error Conversion](Error_Conversion.md) (5 shared connections)
- [config models rationale](config_models_rationale.md) (5 shared connections)
- [websocket validation realtime](websocket_validation_realtime.md) (1 shared connections)
- [room validator path](room_validator_path.md) (1 shared connections)
- [occupants npc commands](occupants_npc_commands.md) (1 shared connections)

## Source Files

- `server/config/models/_helpers.py`
- `server/config/models/nats.py`
- `server/tests/unit/config/test_config_model_helpers.py`

## Audit Trail

- EXTRACTED: 63 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*