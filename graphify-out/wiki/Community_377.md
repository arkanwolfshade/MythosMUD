# Community 377

> 46 nodes

## Key Concepts

- **test_auth_rate_limit.py** (25 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **auth_rate_limit.py** (19 connections) — `server/middleware/auth_rate_limit.py`
- **RateLimiter** (12 connections) — `server/utils/rate_limiter.py`
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
- **_HasPrefix** (2 connections) — `server/middleware/auth_rate_limit.py`
- **_HasRoutes** (2 connections) — `server/middleware/auth_rate_limit.py`
- **_IncludedRouterLike** (2 connections) — `server/middleware/auth_rate_limit.py`
- **_auth_bucket()** (2 connections) — `server/middleware/auth_rate_limit.py`
- *... and 21 more nodes in this community*

## Relationships

- [Community 364](Community_364.md) (6 shared connections)
- [Character Creation & Auth Dependencies](Character_Creation_&_Auth_Dependencies.md) (6 shared connections)
- [Community 246](Community_246.md) (2 shared connections)
- [Community 1295](Community_1295.md) (2 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (2 shared connections)
- [Community 640](Community_640.md) (2 shared connections)
- [Community 31](Community_31.md) (1 shared connections)
- [Community 147](Community_147.md) (1 shared connections)
- [Community 188](Community_188.md) (1 shared connections)

## Source Files

- `server/middleware/auth_rate_limit.py`
- `server/tests/unit/middleware/test_auth_rate_limit.py`
- `server/utils/rate_limiter.py`

## Audit Trail

- EXTRACTED: 101 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*