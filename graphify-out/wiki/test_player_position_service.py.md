# test_player_position_service.py

> 38 nodes

## Key Concepts

- **test_auth_dependencies.py** (26 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **auth/dependencies.py** (19 connections) — `server/auth/dependencies.py`
- **asyncio** (14 connections)
- **require_invite_code()** (11 connections) — `server/auth/dependencies.py`
- **get_current_superuser()** (9 connections) — `server/auth/dependencies.py`
- **get_current_verified_user()** (8 connections) — `server/auth/dependencies.py`
- **get_optional_current_user()** (6 connections) — `server/auth/dependencies.py`
- **test_get_current_superuser_failure()** (6 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_get_current_superuser_with_none_user()** (6 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_get_current_verified_user_failure()** (6 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_get_current_verified_user_with_none_user()** (6 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_get_current_superuser_success()** (5 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_get_current_verified_user_success()** (5 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_get_optional_current_user_with_user()** (5 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_require_invite_code_generic_exception()** (5 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_require_invite_code_invalid()** (5 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_require_invite_code_logged_http_exception()** (5 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_require_invite_code_none()** (5 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_get_optional_current_user_none()** (4 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_require_invite_code_success()** (4 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **test_require_invite_code_with_request()** (4 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **Test requiring invite code when validate_invite raises LoggedHTTPException.** (2 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **Test getting current superuser when user is superuser.** (2 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **Test getting current verified user when user is verified.** (2 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **Authentication dependencies for MythosMUD. This module provides dependency…** (1 connections) — `server/auth/dependencies.py`
- *... and 13 more nodes in this community*

## Relationships

- [NPCSpawningService](NPCSpawningService.md) (13 shared connections)
- [NATSServicePoolMixin](NATSServicePoolMixin.md) (12 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (5 shared connections)
- [enum](enum.md) (3 shared connections)
- [AliasStorage](AliasStorage.md) (2 shared connections)
- [models/container.py](models-container.py.md) (2 shared connections)
- [maps.py](maps.py.md) (2 shared connections)
- [test_message_broadcaster.py](test_message_broadcaster.py.md) (1 shared connections)
- [test_combat_service_modules.py](test_combat_service_modules.py.md) (1 shared connections)
- [ContainerComponent](ContainerComponent.md) (1 shared connections)

## Source Files

- `server/auth/dependencies.py`
- `server/tests/unit/auth/test_auth_dependencies.py`

## Audit Trail

- EXTRACTED: 97 (86%)
- INFERRED: 16 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*