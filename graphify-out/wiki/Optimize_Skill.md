# Optimize Skill

> 13 nodes · cohesion 0.22

## Key Concepts

- **auth_rate_limit.py** (19 connections) — `server/middleware/auth_rate_limit.py`
- **assert_auth_rate_limit_paths_registered()** (9 connections) — `server/middleware/auth_rate_limit.py`
- **_collect_post_paths()** (3 connections) — `server/middleware/auth_rate_limit.py`
- **Protocol** (3 connections)
- **_auth_bucket()** (2 connections) — `server/middleware/auth_rate_limit.py`
- **_HasPrefix** (2 connections) — `server/middleware/auth_rate_limit.py`
- **_HasRoutes** (2 connections) — `server/middleware/auth_rate_limit.py`
- **_IncludedRouterLike** (2 connections) — `server/middleware/auth_rate_limit.py`
- **_join_route_path()** (2 connections) — `server/middleware/auth_rate_limit.py`
- **FastAPI** (2 connections)
- **test_assert_auth_rate_limit_paths_registered_missing()** (2 connections) — `server/tests/unit/middleware/test_auth_rate_limit.py`
- **IP-based rate limiting for unauthenticated auth HTTP endpoints.** (1 connections) — `server/middleware/auth_rate_limit.py`
- **Fail startup if AUTH_RATE_LIMITED_PATHS do not match mounted POST routes.** (1 connections) — `server/middleware/auth_rate_limit.py`

## Relationships

- [_PlayerCombatClearing](_PlayerCombatClearing.md) (8 shared connections)
- [test_combat_flee_helpers.py](test_combat_flee_helpers.py.md) (3 shared connections)
- [AttributeError](AttributeError.md) (2 shared connections)
- [Graph Report - C:\Users\arkan\Proton Drive\arkanwolfshade\My files\Chaosium\character_sheets  (2026-08-12)](Graph_Report_-_C-_Users_arkan_Proton_Drive_arkanwolfshade_My_files_Chaosium_character_sheets__2026-08-12.md) (1 shared connections)
- [test_calendar_procedures.py](test_calendar_procedures.py.md) (1 shared connections)
- [Dead Light and Other Dark Turns (source summary)](Dead_Light_and_Other_Dark_Turns_source_summary.md) (1 shared connections)

## Source Files

- `server/middleware/auth_rate_limit.py`
- `server/tests/unit/middleware/test_auth_rate_limit.py`

## Audit Trail

- EXTRACTED: 33 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*