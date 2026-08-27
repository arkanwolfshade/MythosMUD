# zone

> 20 nodes

## Key Concepts

- **test_logging_processors.py** (37 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **sanitize_sensitive_data()** (12 connections) — `server/structured_logging/logging_processors.py`
- **test_sanitize_sensitive_data_api_key()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_sanitize_sensitive_data_case_insensitive()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_sanitize_sensitive_data_multiple_sensitive_fields()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_sanitize_sensitive_data_nested_dict()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_sanitize_sensitive_data_no_sensitive_fields()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_sanitize_sensitive_data_password()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_sanitize_sensitive_data_safe_fields()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_sanitize_sensitive_data_token()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **sanitize_sensitive_data.** (1 connections) — `server/structured_logging/logging_processors.py`
- **Unit tests for logging processors. Tests the logging processors for sanitizing…** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test sanitize_sensitive_data() is case insensitive.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test sanitize_sensitive_data() redacts password fields.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test sanitize_sensitive_data() redacts token fields.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test sanitize_sensitive_data() redacts fields ending with _key.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test sanitize_sensitive_data() preserves safe fields.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test sanitize_sensitive_data() sanitizes nested dictionaries.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test sanitize_sensitive_data() redacts multiple sensitive fields.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test sanitize_sensitive_data() leaves non-sensitive fields unchanged.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`

## Relationships

- [run_quality_fragmentation_guard.py](run_quality_fragmentation_guard.py.md) (14 shared connections)
- [required](required.md) (6 shared connections)
- [🔴 Anti-Patterns Check (Critical)](🔴_Anti-Patterns_Check_Critical.md) (6 shared connections)
- [name](name.md) (2 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)

## Source Files

- `server/structured_logging/logging_processors.py`
- `server/tests/unit/structured_logging/test_logging_processors.py`

## Audit Trail

- EXTRACTED: 56 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*