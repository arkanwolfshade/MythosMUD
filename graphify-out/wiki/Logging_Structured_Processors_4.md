# Logging Structured Processors

> 7 nodes · cohesion 0.29

## Key Concepts

- **add_correlation_id()** (7 connections) — `server/structured_logging/logging_processors.py`
- **EventDict** (5 connections) — `server/structured_logging/logging_processors.py`
- **test_add_correlation_id_existing()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_add_correlation_id_missing()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Add correlation ID to log entries if not already present.      This processor en** (1 connections) — `server/structured_logging/logging_processors.py`
- **Test add_correlation_id() adds correlation_id when missing.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test add_correlation_id() preserves existing correlation_id.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`

## Relationships

- [[Logging Structured Processors]] (7 shared connections)
- [[NPC Admin API]] (2 shared connections)

## Source Files

- `server/structured_logging/logging_processors.py`
- `server/tests/unit/structured_logging/test_logging_processors.py`

## Audit Trail

- EXTRACTED: 20 (95%)
- INFERRED: 1 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
