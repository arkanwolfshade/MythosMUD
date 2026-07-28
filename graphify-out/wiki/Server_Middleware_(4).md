# Server Middleware (4)

> 35 nodes

## Key Concepts

- **main.py** (15 connections) — `server/main.py`
- **correlation_middleware.py** (9 connections) — `server/middleware/correlation_middleware.py`
- **.__call__()** (8 connections) — `server/middleware/correlation_middleware.py`
- **CorrelationMiddleware** (6 connections) — `server/middleware/correlation_middleware.py`
- **WebSocketCorrelationMiddleware** (5 connections) — `server/middleware/correlation_middleware.py`
- **main()** (4 connections) — `server/main.py`
- **_create_get_app()** (4 connections) — `server/main.py`
- **_get_header()** (4 connections) — `server/middleware/correlation_middleware.py`
- **create_correlation_middleware()** (4 connections) — `server/middleware/correlation_middleware.py`
- **FastAPI** (3 connections)
- **test_auth()** (3 connections) — `server/main.py`
- **.__init__()** (3 connections) — `server/middleware/correlation_middleware.py`
- **create_websocket_correlation_middleware()** (3 connections) — `server/middleware/correlation_middleware.py`
- **read_root()** (2 connections) — `server/main.py`
- **Scope** (2 connections)
- **.__init__()** (2 connections) — `server/middleware/correlation_middleware.py`
- **Any** (2 connections)
- **Any** (1 connections)
- **MythosMUD Server - Main Application Entry Point  This module serves as the prima** (1 connections) — `server/main.py`
- **Main entry point for the MythosMUD server.** (1 connections) — `server/main.py`
- **Factory function that creates the get_app function with encapsulated cache.** (1 connections) — `server/main.py`
- **Root endpoint providing basic server information.** (1 connections) — `server/main.py`
- **Test endpoint to verify JWT authentication is working.** (1 connections) — `server/main.py`
- **ASGIApp** (1 connections)
- **Receive** (1 connections)
- *... and 10 more nodes in this community*

## Relationships

- [Server Commands](Server_Commands.md) (5 shared connections)
- [Server Middleware](Server_Middleware.md) (4 shared connections)
- [Docs Examples](Docs_Examples.md) (4 shared connections)
- [Server Admin](Server_Admin.md) (1 shared connections)
- [Server Config (2)](Server_Config_%282%29.md) (1 shared connections)

## Source Files

- `server/main.py`
- `server/middleware/correlation_middleware.py`

## Audit Trail

- EXTRACTED: 95 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*