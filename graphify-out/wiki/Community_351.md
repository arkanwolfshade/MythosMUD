# Community 351

> 48 nodes

## Key Concepts

- **test_auth_rate_limit.py** (25 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **auth_rate_limit.py** (19 connections) — `server/middleware/auth_rate_limit.py`
- **RateLimiter** (13 connections) — `server/utils/rate_limiter.py`
- **auth_client_key()** (11 connections) — `server/middleware/auth_rate_limit.py`
- **auth_rate_limit_response()** (11 connections) — `server/middleware/auth_rate_limit.py`
- **_post_request()** (9 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **assert_auth_rate_limit_paths_registered()** (7 connections) — `server/middleware/auth_rate_limit.py`
- **is_auth_rate_limited_path()** (5 connections) — `server/middleware/auth_rate_limit.py`
- **test_auth_rate_limit_response_returns_429_when_exceeded()** (5 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **.enforce_rate_limit()** (5 connections) — `server/utils/rate_limiter.py`
- **test_auth_client_key_rejects_non_ip_xff()** (4 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **test_auth_client_key_uses_xff_when_trusted()** (4 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **test_auth_rate_limit_response_maps_rate_limit_error()** (4 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **.get_rate_limit_info()** (4 connections) — `server/utils/rate_limiter.py`
- **_collect_post_paths()** (3 connections) — `server/middleware/auth_rate_limit.py`
- **test_assert_auth_rate_limit_paths_registered_ok()** (3 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **test_auth_client_key_ignores_xff_by_default()** (3 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **test_auth_client_key_uses_ip()** (3 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **test_auth_rate_limit_response_skips_other_paths()** (3 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **.check_rate_limit()** (3 connections) — `server/utils/rate_limiter.py`
- **Protocol** (3 connections)
- **server/utils/__init__.py** (3 connections) — `server/utils/__init__.py`
- **_HasPrefix** (2 connections) — `server/middleware/auth_rate_limit.py`
- **_HasRoutes** (2 connections) — `server/middleware/auth_rate_limit.py`
- **_IncludedRouterLike** (2 connections) — `server/middleware/auth_rate_limit.py`
- *... and 23 more nodes in this community*

## Relationships

- [Container API Models](Container_API_Models.md) (5 shared connections)
- [Community 357](Community_357.md) (5 shared connections)
- [Community 1441](Community_1441.md) (2 shared connections)
- [Community 1325](Community_1325.md) (2 shared connections)
- [Auth Dependencies & Users](Auth_Dependencies_&_Users.md) (2 shared connections)
- [Invite & NPC DB Scripts](Invite_&_NPC_DB_Scripts.md) (2 shared connections)
- [Community 608](Community_608.md) (2 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (1 shared connections)
- [Community 1495](Community_1495.md) (1 shared connections)
- [Community 307](Community_307.md) (1 shared connections)
- [Community 169](Community_169.md) (1 shared connections)

## Source Files

- `server/middleware/auth_rate_limit.py`
- `server/tests/unit/middleware/test_auth_rate_limit.py`
- `server/utils/__init__.py`
- `server/utils/rate_limiter.py`

## Audit Trail

- EXTRACTED: 102 (96%)
- INFERRED: 4 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*