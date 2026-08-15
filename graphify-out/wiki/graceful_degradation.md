# graceful_degradation

> 8 nodes

## Key Concepts

- **graceful_degradation()** (5 connections) — `server/legacy_error_handlers.py`
- **TestGracefulDegradation** (4 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_graceful_degradation_failure()** (3 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **.test_graceful_degradation_success()** (3 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **Context manager for graceful degradation. Provides fallback behavior when…** (1 connections) — `server/legacy_error_handlers.py`
- **Test graceful_degradation context manager.** (1 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **Test graceful_degradation with successful operation.** (1 connections) — `server/tests/unit/test_legacy_error_handlers.py`
- **Test graceful_degradation catches exceptions.** (1 connections) — `server/tests/unit/test_legacy_error_handlers.py`

## Relationships

- [MythosMUDError](MythosMUDError.md) (3 shared connections)

## Source Files

- `server/legacy_error_handlers.py`
- `server/tests/unit/test_legacy_error_handlers.py`

## Audit Trail

- EXTRACTED: 11 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*