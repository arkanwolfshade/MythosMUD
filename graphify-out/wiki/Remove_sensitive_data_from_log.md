# Remove sensitive data from log

> 22 nodes

## Key Concepts

- **test_logging_processors.py** (36 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **sanitize_sensitive_data()** (14 connections) — `server/structured_logging/logging_processors.py`
- **test_sanitize_sensitive_data_password()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_sanitize_sensitive_data_token()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_sanitize_sensitive_data_api_key()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_sanitize_sensitive_data_safe_fields()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_sanitize_sensitive_data_nested_dict()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_sanitize_sensitive_data_multiple_sensitive_fields()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_sanitize_sensitive_data_no_sensitive_fields()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_sanitize_sensitive_data_case_insensitive()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **sample_event_dict()** (2 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Remove sensitive data from log entries.      This processor automatically redact** (1 connections) — `server/structured_logging/logging_processors.py`
- **Unit tests for logging processors.  Tests the logging processors for sanitizing** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Create a sample event dictionary.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test sanitize_sensitive_data() redacts password fields.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test sanitize_sensitive_data() redacts token fields.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test sanitize_sensitive_data() redacts fields ending with _key.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test sanitize_sensitive_data() preserves safe fields.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test sanitize_sensitive_data() sanitizes nested dictionaries.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test sanitize_sensitive_data() redacts multiple sensitive fields.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test sanitize_sensitive_data() leaves non-sensitive fields unchanged.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test sanitize_sensitive_data() is case insensitive.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`

## Relationships

- [enhance player ids()](enhance_player_ids%28%29.md) (14 shared connections)
- [add request context()](add_request_context%28%29.md) (6 shared connections)
- [EventDict](EventDict.md) (4 shared connections)
- [main()](main%28%29.md) (2 shared connections)
- [logging processors](logging_processors.md) (2 shared connections)
- [mock player service()](mock_player_service%28%29.md) (1 shared connections)

## Source Files

- `server/structured_logging/logging_processors.py`
- `server/tests/unit/structured_logging/test_logging_processors.py`

## Audit Trail

- EXTRACTED: 86 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*