# register_error_handlers

> 10 nodes

## Key Concepts

- **register_error_handlers()** (10 connections) — `server/middleware/error_handling_middleware.py`
- **setup_error_handling()** (10 connections) — `server/middleware/error_handling_middleware.py`
- **add_error_handling_middleware()** (7 connections) — `server/middleware/error_handling_middleware.py`
- **server/middleware/__init__.py** (6 connections) — `server/middleware/__init__.py`
- **test_add_register_setup_error_handling()** (4 connections) — `server/tests/unit/middleware/test_error_handling_middleware.py`
- **FastAPI** (4 connections)
- **Add error handling middleware to FastAPI application. Args: app: FastAPI…** (1 connections) — `server/middleware/error_handling_middleware.py`
- **Register error handlers for FastAPI application. This function registers…** (1 connections) — `server/middleware/error_handling_middleware.py`
- **Setup complete error handling for FastAPI application. This function sets up…** (1 connections) — `server/middleware/error_handling_middleware.py`
- **Middleware package for MythosMUD server. This package contains middleware…** (1 connections) — `server/middleware/__init__.py`

## Relationships

- [test_error_handling_middleware.py](test_error_handling_middleware.py.md) (6 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [ErrorType](ErrorType.md) (1 shared connections)
- [ExceptionTracker](ExceptionTracker.md) (1 shared connections)
- [create_app](create_app.md) (1 shared connections)

## Source Files

- `server/middleware/__init__.py`
- `server/middleware/error_handling_middleware.py`
- `server/tests/unit/middleware/test_error_handling_middleware.py`

## Audit Trail

- EXTRACTED: 29 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*