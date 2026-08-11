# Test Refactoring Deliverables

> 24 nodes

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
- **test_add_correlation_id_missing()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **mock_player_service()** (2 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **sanitize_sensitive_data.** (1 connections) — `server/structured_logging/logging_processors.py`
- **Unit tests for logging processors.  Tests the logging processors for sanitizing** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Create a mock player service.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test sanitize_sensitive_data() redacts password fields.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test sanitize_sensitive_data() redacts token fields.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test sanitize_sensitive_data() redacts fields ending with _key.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test sanitize_sensitive_data() preserves safe fields.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test sanitize_sensitive_data() sanitizes nested dictionaries.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test sanitize_sensitive_data() redacts multiple sensitive fields.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test sanitize_sensitive_data() leaves non-sensitive fields unchanged.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test sanitize_sensitive_data() is case insensitive.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test add_correlation_id() adds correlation_id when missing.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`

## Relationships

- [Logging Structured Processors](Logging_Structured_Processors.md) (15 shared connections)
- [Archive Planning Aliases](Archive_Planning_Aliases.md) (6 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (4 shared connections)
- [Archive Bug Prevention](Archive_Bug_Prevention.md) (2 shared connections)
- [E 2 E Scenarios Scenario](E_2_E_Scenarios_Scenario.md) (2 shared connections)

## Source Files

- `server/structured_logging/logging_processors.py`
- `server/tests/unit/structured_logging/test_logging_processors.py`

## Audit Trail

- EXTRACTED: 90 (99%)
- INFERRED: 1 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*