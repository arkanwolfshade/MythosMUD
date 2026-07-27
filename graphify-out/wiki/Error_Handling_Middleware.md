# Error Handling Middleware

> 10 nodes · cohesion 0.06

## Key Concepts

- **FastAPI** (4 connections) — `server/middleware/error_handling_middleware.py`
- **Scope** (3 connections) — `server/middleware/error_handling_middleware.py`
- **Exception** (2 connections) — `server/middleware/error_handling_middleware.py`
- **Receive** (2 connections) — `server/middleware/error_handling_middleware.py`
- **Request** (2 connections) — `server/middleware/error_handling_middleware.py`
- **Send** (2 connections) — `server/middleware/error_handling_middleware.py`
- **BaseException** (2 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **Scope** (2 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **Response** (1 connections) — `server/middleware/error_handling_middleware.py`
- **ASGIApp** (1 connections) — `server/middleware/error_handling_middleware.py`

## Relationships

- No strong cross-community connections detected

## Source Files

- `server/middleware/error_handling_middleware.py`
- `server/tests/unit/middleware/test_error_handling_middleware.py`

## Audit Trail

- EXTRACTED: 19 (90%)
- INFERRED: 2 (10%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*