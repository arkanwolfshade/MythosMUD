# Test Openapi Tags

> 13 nodes

## Key Concepts

- **create_app()** (14 connections) — `server/app/factory.py`
- **test_openapi_tags.py** (6 connections) — `server/tests/unit/app/test_openapi_tags.py`
- **_register_v1_routers()** (4 connections) — `server/app/factory.py`
- **_openapi_spec()** (4 connections) — `server/tests/unit/app/test_openapi_tags.py`
- **_route_declared_tags()** (4 connections) — `server/tests/unit/app/test_openapi_tags.py`
- **FastAPI** (3 connections)
- **test_openapi_tags_matches_route_declared_tags()** (2 connections) — `server/tests/unit/app/test_openapi_tags.py`
- **test_create_app_auth_rate_limit_paths_match()** (2 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **Mount all versioned API routers under /v1.** (1 connections) — `server/app/factory.py`
- **Create and configure the FastAPI application. This function sets up the FastAPI…** (1 connections) — `server/app/factory.py`
- **Unit tests guarding OPENAPI_TAGS against drift from route-declared tags. route-…** (1 connections) — `server/tests/unit/app/test_openapi_tags.py`
- **FastAPI's .openapi() is typed dict[str, Any]; erase that at the boundary.** (1 connections) — `server/tests/unit/app/test_openapi_tags.py`
- **Every tag any mounted route actually declares.** (1 connections) — `server/tests/unit/app/test_openapi_tags.py`

## Relationships

- [Character Creation API](Character_Creation_API.md) (5 shared connections)
- [Generate Openapi Spec](Generate_Openapi_Spec.md) (2 shared connections)
- [Test Auth Rate Limit](Test_Auth_Rate_Limit.md) (2 shared connections)
- [Error Handling Middleware](Error_Handling_Middleware.md) (1 shared connections)
- [Auth Rate Limit](Auth_Rate_Limit.md) (1 shared connections)
- [Test Lifespan Startup](Test_Lifespan_Startup.md) (1 shared connections)

## Source Files

- `server/app/factory.py`
- `server/tests/unit/app/test_openapi_tags.py`
- `server/tests/unit/middleware/test_auth_rate_limit.py`

## Audit Trail

- EXTRACTED: 27 (96%)
- INFERRED: 1 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*