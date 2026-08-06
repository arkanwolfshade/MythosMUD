# container persistence rationale

> 77 nodes

## Key Concepts

- **test_logging_processors.py** (36 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **set_global_player_service()** (17 connections) — `server/structured_logging/logging_processors.py`
- **enhance_player_ids()** (17 connections) — `server/structured_logging/logging_processors.py`
- **sanitize_sensitive_data()** (14 connections) — `server/structured_logging/logging_processors.py`
- **logging_processors.py** (12 connections) — `server/structured_logging/logging_processors.py`
- **add_request_context()** (11 connections) — `server/structured_logging/logging_processors.py`
- **add_correlation_id()** (8 connections) — `server/structured_logging/logging_processors.py`
- **EventDict** (5 connections)
- **test_enhance_player_ids_persistence_error()** (5 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **_EnhancePlayerIdsTls** (4 connections) — `server/structured_logging/logging_processors.py`
- **test_enhance_player_ids_no_player_service()** (4 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_enhance_player_ids_player_found()** (4 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_enhance_player_ids_player_not_found()** (4 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_enhance_player_ids_invalid_uuid_format()** (4 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_enhance_player_ids_short_string()** (4 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_enhance_player_ids_non_string_value()** (4 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_enhance_player_ids_no_player_id_field()** (4 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_enhance_player_ids_player_no_name_attribute()** (4 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_enhance_player_ids_prevents_recursion()** (4 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_enhance_player_ids_no_persistence_attribute()** (4 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_set_global_player_service()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_sanitize_sensitive_data_password()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_sanitize_sensitive_data_token()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_sanitize_sensitive_data_api_key()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_sanitize_sensitive_data_safe_fields()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- *... and 52 more nodes in this community*

## Relationships

- [Error Conversion](Error_Conversion.md) (11 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (4 shared connections)
- [aggro threat services](aggro_threat_services.md) (1 shared connections)
- [room sync service](room_sync_service.md) (1 shared connections)

## Source Files

- `server/structured_logging/logging_processors.py`
- `server/tests/unit/structured_logging/test_logging_processors.py`

## Audit Trail

- EXTRACTED: 253 (97%)
- INFERRED: 8 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*