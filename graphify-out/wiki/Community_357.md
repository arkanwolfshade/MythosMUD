# Community 357

> 48 nodes

## Key Concepts

- **test_rate_limiter_utils.py** (30 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **utils/rate_limiter.py** (14 connections) — `server/utils/rate_limiter.py`
- **auth_login_rate_limit_settings()** (7 connections) — `server/utils/rate_limiter.py`
- **character_creation_rate_limit_settings()** (7 connections) — `server/utils/rate_limiter.py`
- **_positive_int_env()** (4 connections) — `server/utils/rate_limiter.py`
- **test_character_creation_rate_limit_settings_defaults()** (3 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_character_creation_rate_limit_settings_from_env()** (3 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_enforce_rate_limit_includes_retry_after()** (3 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_enforce_rate_limit_raises_when_exceeded()** (3 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_auth_login_limiter_matches_settings()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_auth_login_rate_limit_settings_defaults()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_auth_login_rate_limit_settings_from_env()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_character_creation_limiter_initialized()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_character_creation_limiter_matches_settings()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_check_rate_limit_different_users()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_check_rate_limit_exceeds_limit()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_check_rate_limit_first_request()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_check_rate_limit_multiple_requests()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_check_rate_limit_removes_old_requests()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_enforce_rate_limit_allows_request()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_get_rate_limit_info_calculates_reset_time()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_get_rate_limit_info_calculates_retry_after()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_get_rate_limit_info_filters_old_requests()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_get_rate_limit_info_no_requests()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- **test_get_rate_limit_info_with_requests()** (2 connections) — `server/tests/unit/utils/test_rate_limiter_utils.py`
- *... and 23 more nodes in this community*

## Relationships

- [Container API Models](Container_API_Models.md) (5 shared connections)
- [Community 351](Community_351.md) (5 shared connections)
- [Invite & NPC DB Scripts](Invite_&_NPC_DB_Scripts.md) (2 shared connections)
- [Community 1495](Community_1495.md) (1 shared connections)
- [Event Bus & Persistence Core](Event_Bus_&_Persistence_Core.md) (1 shared connections)
- [Character Creation & Professions](Character_Creation_&_Professions.md) (1 shared connections)

## Source Files

- `server/tests/unit/utils/test_rate_limiter_utils.py`
- `server/utils/rate_limiter.py`

## Audit Trail

- EXTRACTED: 72 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*