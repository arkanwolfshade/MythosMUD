# required

> 16 nodes

## Key Concepts

- **logging_processors.py** (14 connections) — `server/structured_logging/logging_processors.py`
- **add_correlation_id()** (6 connections) — `server/structured_logging/logging_processors.py`
- **EventDict** (5 connections)
- **_database_error_type()** (4 connections) — `server/structured_logging/logging_processors.py`
- **_enhance_one_player_id()** (4 connections) — `server/structured_logging/logging_processors.py`
- **_EnhancePlayerIdsTls** (3 connections) — `server/structured_logging/logging_processors.py`
- **test_add_correlation_id_existing()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **test_add_correlation_id_missing()** (3 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **_PlayerServiceHolder** (1 connections) — `server/structured_logging/logging_processors.py`
- **.__init__()** (1 connections) — `server/structured_logging/logging_processors.py`
- **BaseException** (1 connections)
- **Logging processors for structlog event processing. This module provides…** (1 connections) — `server/structured_logging/logging_processors.py`
- **Add correlation ID to log entries if not already present. This processor…** (1 connections) — `server/structured_logging/logging_processors.py`
- **Thread-local recursion guard for enhance_player_ids (typed .active for static…** (1 connections) — `server/structured_logging/logging_processors.py`
- **Test add_correlation_id() adds correlation_id when missing.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`
- **Test add_correlation_id() preserves existing correlation_id.** (1 connections) — `server/tests/unit/structured_logging/test_logging_processors.py`

## Relationships

- [zone](zone.md) (6 shared connections)
- [run_quality_fragmentation_guard.py](run_quality_fragmentation_guard.py.md) (4 shared connections)
- [ContainerComponent](ContainerComponent.md) (2 shared connections)
- [🔴 Anti-Patterns Check (Critical)](🔴_Anti-Patterns_Check_Critical.md) (2 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (2 shared connections)

## Source Files

- `server/structured_logging/logging_processors.py`
- `server/tests/unit/structured_logging/test_logging_processors.py`

## Audit Trail

- EXTRACTED: 32 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*