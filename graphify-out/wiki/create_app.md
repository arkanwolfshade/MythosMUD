# create_app

> 18 nodes

## Key Concepts

- **create_app()** (17 connections) — `server/app/factory.py`
- **test_openapi_tags.py** (6 connections) — `server/tests/unit/app/test_openapi_tags.py`
- **_register_v1_routers()** (4 connections) — `server/app/factory.py`
- **_create_get_app()** (4 connections) — `server/main.py`
- **main()** (4 connections) — `server/main.py`
- **_openapi_spec()** (4 connections) — `server/tests/unit/app/test_openapi_tags.py`
- **_route_declared_tags()** (4 connections) — `server/tests/unit/app/test_openapi_tags.py`
- **FastAPI** (3 connections)
- **FastAPI** (3 connections)
- **test_openapi_tags_matches_route_declared_tags()** (2 connections) — `server/tests/unit/app/test_openapi_tags.py`
- **test_create_app_auth_rate_limit_paths_match()** (2 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **Mount all versioned API routers under /v1.** (1 connections) — `server/app/factory.py`
- **Create and configure the FastAPI application. This function sets up the FastAPI…** (1 connections) — `server/app/factory.py`
- **Main entry point for the MythosMUD server.** (1 connections) — `server/main.py`
- **Factory function that creates the get_app function with encapsulated cache.…** (1 connections) — `server/main.py`
- **Unit tests guarding OPENAPI_TAGS against drift from route-declared tags. route-…** (1 connections) — `server/tests/unit/app/test_openapi_tags.py`
- **FastAPI's .openapi() is typed dict[str, Any]; erase that at the boundary.** (1 connections) — `server/tests/unit/app/test_openapi_tags.py`
- **Every tag any mounted route actually declares.** (1 connections) — `server/tests/unit/app/test_openapi_tags.py`

## Relationships

- [get_logger](get_logger.md) (9 shared connections)
- [test_auth_rate_limit.py](test_auth_rate_limit.py.md) (3 shared connections)
- [generate_openapi_spec.py](generate_openapi_spec.py.md) (2 shared connections)
- [register_error_handlers](register_error_handlers.md) (1 shared connections)
- [lifespan.py](lifespan.py.md) (1 shared connections)

## Source Files

- `server/app/factory.py`
- `server/main.py`
- `server/tests/unit/app/test_openapi_tags.py`
- `server/tests/unit/middleware/test_auth_rate_limit.py`

## Audit Trail

- EXTRACTED: 37 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*