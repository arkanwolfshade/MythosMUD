# Auth Rate Limit

> 12 nodes

## Key Concepts

- **auth_rate_limit.py** (19 connections) — `server/middleware/auth_rate_limit.py`
- **assert_auth_rate_limit_paths_registered()** (9 connections) — `server/middleware/auth_rate_limit.py`
- **_collect_post_paths()** (3 connections) — `server/middleware/auth_rate_limit.py`
- **Protocol** (3 connections)
- **_HasPrefix** (2 connections) — `server/middleware/auth_rate_limit.py`
- **_HasRoutes** (2 connections) — `server/middleware/auth_rate_limit.py`
- **_IncludedRouterLike** (2 connections) — `server/middleware/auth_rate_limit.py`
- **_join_route_path()** (2 connections) — `server/middleware/auth_rate_limit.py`
- **test_assert_auth_rate_limit_paths_registered_missing()** (2 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **FastAPI** (2 connections)
- **IP-based rate limiting for unauthenticated auth HTTP endpoints.** (1 connections) — `server/middleware/auth_rate_limit.py`
- **Fail startup if AUTH_RATE_LIMITED_PATHS do not match mounted POST routes.** (1 connections) — `server/middleware/auth_rate_limit.py`

## Relationships

- [Test Auth Rate Limit](Test_Auth_Rate_Limit.md) (8 shared connections)
- [Character Creation API](Character_Creation_API.md) (2 shared connections)
- [Test Openapi Tags](Test_Openapi_Tags.md) (1 shared connections)
- [Container/Inventory Helpers](Container-Inventory_Helpers.md) (1 shared connections)
- [Error Handling & Exceptions](Error_Handling_&_Exceptions.md) (1 shared connections)
- [Test Rate Limiter Utils](Test_Rate_Limiter_Utils.md) (1 shared connections)
- [Auth Rate Limit](Auth_Rate_Limit.md) (1 shared connections)
- [Player Guid Formatter](Player_Guid_Formatter.md) (1 shared connections)

## Source Files

- `server/middleware/auth_rate_limit.py`
- `server/tests/unit/middleware/test_auth_rate_limit.py`

## Audit Trail

- EXTRACTED: 32 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*