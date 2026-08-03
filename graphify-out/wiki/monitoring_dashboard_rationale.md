# monitoring dashboard rationale

> 18 nodes

## Key Concepts

- **sanitize_sensitive_data()** (14 connections) — `server/structured_logging/logging_processors.py`
- **test_sanitize_sensitive_data_password()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_sanitize_sensitive_data_token()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_sanitize_sensitive_data_api_key()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_sanitize_sensitive_data_safe_fields()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_sanitize_sensitive_data_nested_dict()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_sanitize_sensitive_data_multiple_sensitive_fields()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_sanitize_sensitive_data_no_sensitive_fields()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_sanitize_sensitive_data_case_insensitive()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Remove sensitive data from log entries.      This processor automatically redact** (1 connections) — `server/structured_logging/logging_processors.py`
- **Test sanitize_sensitive_data() redacts password fields.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test sanitize_sensitive_data() redacts token fields.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test sanitize_sensitive_data() redacts fields ending with _key.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test sanitize_sensitive_data() preserves safe fields.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test sanitize_sensitive_data() sanitizes nested dictionaries.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test sanitize_sensitive_data() redacts multiple sensitive fields.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test sanitize_sensitive_data() leaves non-sensitive fields unchanged.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test sanitize_sensitive_data() is case insensitive.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`

## Relationships

- [lucidity npc combat](lucidity_npc_combat.md) (9 shared connections)
- [NATS Messaging](NATS_Messaging.md) (2 shared connections)
- [npc populate databases](npc_populate_databases.md) (1 shared connections)
- [services ascii map](services_ascii_map.md) (1 shared connections)

## Source Files

- `server/structured_logging/logging_processors.py`
- `server/tests/unit/structured_logging/test_logging_processors.py`

## Audit Trail

- EXTRACTED: 46 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*