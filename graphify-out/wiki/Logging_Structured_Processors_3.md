# Logging Structured Processors

> 11 nodes · cohesion 0.20

## Key Concepts

- **add_request_context()** (10 connections) — `server/structured_logging/logging_processors.py`
- **test_add_request_context_adds_logger_name()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_add_request_context_adds_request_id()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_add_request_context_adds_timestamp()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_add_request_context_preserves_request_id()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_add_request_context_preserves_timestamp()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test add_request_context() preserves existing timestamp.** (2 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Add request context information to log entries.      This processor adds context** (1 connections) — `server/structured_logging/logging_processors.py`
- **Test add_request_context() adds timestamp when missing.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test add_request_context() adds logger_name.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test add_request_context() adds request_id when missing.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`

## Relationships

- [[Logging Structured Processors]] (8 shared connections)
- [[NPC Admin API]] (1 shared connections)

## Source Files

- `server/structured_logging/logging_processors.py`
- `server/tests/unit/structured_logging/test_logging_processors.py`

## Audit Trail

- EXTRACTED: 31 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
