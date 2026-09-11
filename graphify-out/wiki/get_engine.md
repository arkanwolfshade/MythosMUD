# .get_engine

> 7 nodes

## Key Concepts

- **.get_engine()** (4 connections) — `server/database.py`
- **_dispose_engine_safely()** (4 connections) — `server/database.py`
- **AsyncEngine** (4 connections)
- **.close()** (3 connections) — `server/database.py`
- **Dispose database engine with Windows/asyncpg-safe cleanup.** (1 connections) — `server/database.py`
- **Get the database engine, initializing if necessary. Returns: AsyncEngine: The…** (1 connections) — `server/database.py`
- **Close database connections.** (1 connections) — `server/database.py`

## Relationships

- [get_logger](get_logger.md) (3 shared connections)
- [DatabaseManager](DatabaseManager.md) (2 shared connections)
- [MemoryMonitor](MemoryMonitor.md) (1 shared connections)

## Source Files

- `server/database.py`

## Audit Trail

- EXTRACTED: 12 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*