# Playwright MCP Scenarios

> 7 nodes

## Key Concepts

- **exception_metrics.py** (4 connections) — `server/monitoring/exception_metrics.py`
- **get_summary()** (3 connections) — `server/monitoring/exception_metrics.py`
- **increment_exception()** (2 connections) — `server/monitoring/exception_metrics.py`
- **Any** (1 connections)
- **Exception metrics tracking for monitoring. This module provides thread-safe…** (1 connections) — `server/monitoring/exception_metrics.py`
- **Increment the count for a specific exception type. Args: exc_type: The…** (1 connections) — `server/monitoring/exception_metrics.py`
- **Get a summary of exception counts. Returns: dict[str, Any]: Dictionary…** (1 connections) — `server/monitoring/exception_metrics.py`

## Relationships

- [generate_invites_db.py](generate_invites_db.py.md) (1 shared connections)

## Source Files

- `server/monitoring/exception_metrics.py`

## Audit Trail

- EXTRACTED: 7 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*