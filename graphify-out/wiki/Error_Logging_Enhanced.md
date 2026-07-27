# Error Logging Enhanced

> 12 nodes · cohesion 0.18

## Key Concepts

- **create_enhanced_error_context()** (12 connections) — `server/utils/enhanced_error_logging.py`
- **create_context_from_request()** (7 connections) — `server/utils/error_logging.py`
- **create_context_from_websocket()** (5 connections) — `server/utils/error_logging.py`
- **ErrorContext** (2 connections) — `server/utils/error_logging.py`
- **ErrorContext** (1 connections) — `server/utils/enhanced_error_logging.py`
- **Request** (1 connections) — `server/utils/enhanced_error_logging.py`
- **WebSocket** (1 connections) — `server/utils/enhanced_error_logging.py`
- **Request** (1 connections) — `server/utils/error_logging.py`
- **WebSocket** (1 connections) — `server/utils/error_logging.py`
- **Create enhanced error context with structured information.      This function cr** (1 connections) — `server/utils/enhanced_error_logging.py`
- **Create error context from a FastAPI request. Delegates to create_enhanced_error_** (1 connections) — `server/utils/error_logging.py`
- **Create error context from a WebSocket. Delegates to create_enhanced_error_contex** (1 connections) — `server/utils/error_logging.py`

## Relationships

- [[NPC Admin API]] (6 shared connections)
- [[App Lifespan Management]] (2 shared connections)
- [[Standardized Error Responses]] (1 shared connections)
- [[Api Player]] (1 shared connections)

## Source Files

- `server/utils/enhanced_error_logging.py`
- `server/utils/error_logging.py`

## Audit Trail

- EXTRACTED: 34 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
