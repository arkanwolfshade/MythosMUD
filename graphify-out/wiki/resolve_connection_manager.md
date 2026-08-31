# resolve_connection_manager

> 4 nodes

## Key Concepts

- **resolve_connection_manager()** (5 connections) — `server/api/real_time.py`
- **test_resolve_connection_manager_delegates_when_none()** (2 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **test_resolve_connection_manager_returns_candidate()** (2 connections) — `server/tests/unit/api/test_real_time_helpers.py`
- **Prefer the supplied manager; otherwise the container singleton. Static import…** (1 connections) — `server/api/real_time.py`

## Relationships

- [real_time.py](real_time.py.md) (2 shared connections)
- [test_real_time_helpers.py](test_real_time_helpers.py.md) (2 shared connections)

## Source Files

- `server/api/real_time.py`
- `server/tests/unit/api/test_real_time_helpers.py`

## Audit Trail

- EXTRACTED: 7 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*