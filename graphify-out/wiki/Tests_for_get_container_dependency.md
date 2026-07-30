# Tests for get container dependency

> 12 nodes

## Key Concepts

- **main.py** (15 connections) — `server/main.py`
- **main()** (4 connections) — `server/main.py`
- **_create_get_app()** (4 connections) — `server/main.py`
- **FastAPI** (3 connections)
- **test_auth()** (3 connections) — `server/main.py`
- **read_root()** (2 connections) — `server/main.py`
- **Any** (1 connections)
- **MythosMUD Server - Main Application Entry Point  This module serves as the prima** (1 connections) — `server/main.py`
- **Main entry point for the MythosMUD server.** (1 connections) — `server/main.py`
- **Factory function that creates the get_app function with encapsulated cache.** (1 connections) — `server/main.py`
- **Root endpoint providing basic server information.** (1 connections) — `server/main.py`
- **Test endpoint to verify JWT authentication is working.** (1 connections) — `server/main.py`

## Relationships

- [init](init.md) (4 shared connections)
- [world](world.md) (4 shared connections)
- [close db()](close_db%28%29.md) (1 shared connections)
- [process dead players()](process_dead_players%28%29.md) (1 shared connections)
- [fastapi integration](fastapi_integration.md) (1 shared connections)

## Source Files

- `server/main.py`

## Audit Trail

- EXTRACTED: 37 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*