# Fastapi Code Review

> 7 nodes

## Key Concepts

- **create_enhanced_error_context()** (12 connections) — `server/utils/enhanced_error_logging.py`
- **create_context_from_websocket()** (5 connections) — `server/utils/error_logging.py`
- **Request** (1 connections)
- **WebSocket** (1 connections)
- **Create enhanced error context with structured information.      This function cr** (1 connections) — `server/utils/enhanced_error_logging.py`
- **WebSocket** (1 connections)
- **Create error context from a WebSocket. Delegates to create_enhanced_error_contex** (1 connections) — `server/utils/error_logging.py`

## Relationships

- [Active Lucidity Service](Active_Lucidity_Service.md) (3 shared connections)
- [Docker PostgreSQL Typo Bug](Docker_PostgreSQL_Typo_Bug.md) (2 shared connections)
- [Realtime Errors Error](Realtime_Errors_Error.md) (2 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (2 shared connections)
- [Combat Client Crash Report](Combat_Client_Crash_Report.md) (1 shared connections)

## Source Files

- `server/utils/enhanced_error_logging.py`
- `server/utils/error_logging.py`

## Audit Trail

- EXTRACTED: 22 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*