# Logging Structured Processors

> 18 nodes · cohesion 0.11

## Key Concepts

- **sanitize_sensitive_data()** (13 connections) — `server/structured_logging/logging_processors.py`
- **test_sanitize_sensitive_data_api_key()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_sanitize_sensitive_data_case_insensitive()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_sanitize_sensitive_data_multiple_sensitive_fields()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_sanitize_sensitive_data_nested_dict()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_sanitize_sensitive_data_no_sensitive_fields()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_sanitize_sensitive_data_password()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_sanitize_sensitive_data_safe_fields()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_sanitize_sensitive_data_token()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Remove sensitive data from log entries.      This processor automatically redact** (1 connections) — `server/structured_logging/logging_processors.py`
- **Test sanitize_sensitive_data() is case insensitive.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test sanitize_sensitive_data() redacts password fields.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test sanitize_sensitive_data() redacts token fields.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test sanitize_sensitive_data() redacts fields ending with _key.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test sanitize_sensitive_data() preserves safe fields.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test sanitize_sensitive_data() sanitizes nested dictionaries.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test sanitize_sensitive_data() redacts multiple sensitive fields.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test sanitize_sensitive_data() leaves non-sensitive fields unchanged.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`

## Relationships

- [[Logging Structured Processors]] (11 shared connections)
- [[NPC Admin API]] (1 shared connections)

## Source Files

- `server/structured_logging/logging_processors.py`
- `server/tests/unit/structured_logging/test_logging_processors.py`

## Audit Trail

- EXTRACTED: 46 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
