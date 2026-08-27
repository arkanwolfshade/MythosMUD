# create_app

> 25 nodes

## Key Concepts

- **create_app()** (17 connections) — `server/app/factory.py`
- **server/main.py** (17 connections) — `server/main.py`
- **test_openapi_tags.py** (6 connections) — `server/tests/unit/app/test_openapi_tags.py`
- **_register_v1_routers()** (4 connections) — `server/app/factory.py`
- **_create_get_app()** (4 connections) — `server/main.py`
- **main()** (4 connections) — `server/main.py`
- **test_auth()** (4 connections) — `server/main.py`
- **_openapi_spec()** (4 connections) — `server/tests/unit/app/test_openapi_tags.py`
- **_route_declared_tags()** (4 connections) — `server/tests/unit/app/test_openapi_tags.py`
- **read_root()** (3 connections) — `server/main.py`
- **FastAPI** (3 connections)
- **FastAPI** (3 connections)
- **test_openapi_tags_matches_route_declared_tags()** (2 connections) — `server/tests/unit/app/test_openapi_tags.py`
- **get** (2 connections)
- **Any** (1 connections)
- **Mount all versioned API routers under /v1.** (1 connections) — `server/app/factory.py`
- **Create and configure the FastAPI application. This function sets up the FastAPI…** (1 connections) — `server/app/factory.py`
- **MythosMUD Server - Main Application Entry Point This module serves as the…** (1 connections) — `server/main.py`
- **Root endpoint providing basic server information.** (1 connections) — `server/main.py`
- **Test endpoint to verify JWT authentication is working.** (1 connections) — `server/main.py`
- **Main entry point for the MythosMUD server.** (1 connections) — `server/main.py`
- **Factory function that creates the get_app function with encapsulated cache.…** (1 connections) — `server/main.py`
- **Unit tests guarding OPENAPI_TAGS against drift from route-declared tags. route-…** (1 connections) — `server/tests/unit/app/test_openapi_tags.py`
- **FastAPI's .openapi() is typed dict[str, Any]; erase that at the boundary.** (1 connections) — `server/tests/unit/app/test_openapi_tags.py`
- **Every tag any mounted route actually declares.** (1 connections) — `server/tests/unit/app/test_openapi_tags.py`

## Relationships

- [factory.py](factory.py.md) (6 shared connections)
- [get_logger](get_logger.md) (4 shared connections)
- [generate_openapi_spec.py](generate_openapi_spec.py.md) (2 shared connections)
- [test_auth_rate_limit.py](test_auth_rate_limit.py.md) (2 shared connections)
- [middleware](middleware.md) (2 shared connections)
- [error_handling_middleware.py](error_handling_middleware.py.md) (1 shared connections)
- [auth_rate_limit.py](auth_rate_limit.py.md) (1 shared connections)
- [lifespan_startup.py](lifespan_startup.py.md) (1 shared connections)
- [Uvicorn ASGI Server Best Practices](Uvicorn_ASGI_Server_Best_Practices.md) (1 shared connections)
- [get_config](get_config.md) (1 shared connections)
- [test_users.py](test_users.py.md) (1 shared connections)

## Source Files

- `server/app/factory.py`
- `server/main.py`
- `server/tests/unit/app/test_openapi_tags.py`

## Audit Trail

- EXTRACTED: 54 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*