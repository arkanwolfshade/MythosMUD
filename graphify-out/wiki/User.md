# User

> 395 nodes · cohesion 0.01

## Key Concepts

- **User** (306 connections) — `server/models/user.py`
- **test_users.py** (60 connections) — `server/tests/unit/auth/test_users.py`
- **user.py** (57 connections) — `server/models/user.py`
- **Result** (52 connections) — `scripts/run_test_ci.py`
- **endpoints.py** (52 connections) — `server/auth/endpoints.py`
- **test_endpoints.py** (51 connections) — `server/tests/unit/auth/test_endpoints.py`
- **users.py** (47 connections) — `server/auth/users.py`
- **UserManager** (47 connections) — `server/auth/users.py`
- **login_user()** (28 connections) — `server/auth/endpoints.py`
- **register_user()** (28 connections) — `server/auth/endpoints.py`
- **UserCreate** (27 connections) — `server/auth/endpoints.py`
- **InviteManager** (24 connections) — `server/auth/invites.py`
- **test_auth_dependencies.py** (24 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **LoginRequest** (22 connections) — `server/auth/endpoints.py`
- **professions.py** (19 connections) — `server/api/professions.py`
- **dependencies.py** (18 connections) — `server/auth/dependencies.py`
- **invites.py** (16 connections) — `server/auth/invites.py`
- **test_professions_endpoints.py** (13 connections) — `server/tests/unit/api/test_professions_endpoints.py`
- **get_auth_backend()** (12 connections) — `server/auth/users.py`
- **require_invite_code()** (11 connections) — `server/auth/dependencies.py`
- **get_current_user_with_logging()** (11 connections) — `server/auth/users.py`
- **UsernameAuthenticationBackend** (11 connections) — `server/auth/users.py`
- **test_user.py** (11 connections) — `server/tests/unit/models/test_user.py`
- **get_all_professions()** (10 connections) — `server/api/professions.py`
- **get_profession_by_id()** (10 connections) — `server/api/professions.py`
- *... and 370 more nodes in this community*

## Relationships

- [LoggedHTTPException](LoggedHTTPException.md) (82 shared connections)
- [exceptions.py](exceptions.py.md) (35 shared connections)
- [test_player_preferences_service.py](test_player_preferences_service.py.md) (25 shared connections)
- [ContainerService](ContainerService.md) (25 shared connections)
- [ExplorationService](ExplorationService.md) (23 shared connections)
- [get_logger](get_logger.md) (19 shared connections)
- [__init__.py](__init__.py.md) (16 shared connections)
- [get_admin_auth_service](get_admin_auth_service.md) (16 shared connections)
- [character_creation.py](character_creation.py.md) (15 shared connections)
- [lifespan.py](lifespan.py.md) (11 shared connections)
- [factory.py](factory.py.md) (11 shared connections)
- [Invite](Invite.md) (11 shared connections)

## Source Files

- `scripts/run_test_ci.py`
- `server/api/player_helpers.py`
- `server/api/professions.py`
- `server/auth/__init__.py`
- `server/auth/dependencies.py`
- `server/auth/email_utils.py`
- `server/auth/endpoints.py`
- `server/auth/invites.py`
- `server/auth/users.py`
- `server/models/user.py`
- `server/schemas/auth/invite.py`
- `server/tests/integration/test_db_connectivity.py`
- `server/tests/unit/api/test_professions_endpoints.py`
- `server/tests/unit/auth/test_auth_dependencies.py`
- `server/tests/unit/auth/test_endpoints.py`
- `server/tests/unit/auth/test_users.py`
- `server/tests/unit/infrastructure/test_async_persistence_core.py`
- `server/tests/unit/models/test_user.py`
- `server/tests/unit/services/test_player_preferences_service.py`

## Audit Trail

- EXTRACTED: 1746 (89%)
- INFERRED: 208 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*