# _PlayerCombatClearing

> 20 nodes · cohesion 0.20

## Key Concepts

- **test_auth_rate_limit.py** (25 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **auth_client_key()** (11 connections) — `server/middleware/auth_rate_limit.py`
- **auth_rate_limit_response()** (11 connections) — `server/middleware/auth_rate_limit.py`
- **_post_request()** (9 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **is_auth_rate_limited_path()** (5 connections) — `server/middleware/auth_rate_limit.py`
- **test_auth_rate_limit_response_returns_429_when_exceeded()** (5 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **test_auth_client_key_rejects_non_ip_xff()** (4 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **test_auth_client_key_uses_xff_when_trusted()** (4 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **test_auth_rate_limit_response_maps_rate_limit_error()** (4 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **test_assert_auth_rate_limit_paths_registered_ok()** (3 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **test_auth_client_key_ignores_xff_by_default()** (3 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **test_auth_client_key_uses_ip()** (3 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **test_auth_rate_limit_response_skips_other_paths()** (3 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **_ok_post()** (2 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **MonkeyPatch** (2 connections)
- **test_is_auth_rate_limited_path()** (2 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **Return 429 when an auth POST exceeds the limiter; otherwise None.** (1 connections) — `server/middleware/auth_rate_limit.py`
- **Return True if path is an unauthenticated auth POST covered by the limiter.** (1 connections) — `server/middleware/auth_rate_limit.py`
- **Key the limiter by client IP. Default uses the TCP peer (request.client.host).…** (1 connections) — `server/middleware/auth_rate_limit.py`
- **Unit tests for auth HTTP rate limiting.** (1 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`

## Relationships

- [Optimize Skill](Optimize_Skill.md) (8 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (3 shared connections)
- [AttributeError](AttributeError.md) (3 shared connections)
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (3 shared connections)
- [process_room_files](process_room_files.md) (2 shared connections)
- [Dead Light and Other Dark Turns (source summary)](Dead_Light_and_Other_Dark_Turns_source_summary.md) (1 shared connections)
- [EventBus](EventBus.md) (1 shared connections)
- [test_calendar_procedures.py](test_calendar_procedures.py.md) (1 shared connections)
- [Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\character_sheets  (2026-08-12)](Graph_Report_-_C-_Users_arkan_Proton_Drive_arkanwolfshade_My_files_Chaosium_character_sheets__2026-08-12.md) (1 shared connections)
- [test_container_persistence_async_helpers.py](test_container_persistence_async_helpers.py.md) (1 shared connections)

## Source Files

- `server/middleware/auth_rate_limit.py`
- `server/tests/unit/middleware/test_auth_rate_limit.py`

## Audit Trail

- EXTRACTED: 60 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*