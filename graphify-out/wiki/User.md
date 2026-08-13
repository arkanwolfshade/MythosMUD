# User

> 267 nodes

## Key Concepts

- **User** (297 connections) — `server/models/user.py`
- **endpoints.py** (52 connections) — `server/auth/endpoints.py`
- **test_endpoints.py** (51 connections) — `server/tests/unit/auth/test_endpoints.py`
- **asyncio** (36 connections)
- **login_user()** (29 connections) — `server/auth/endpoints.py`
- **register_user()** (29 connections) — `server/auth/endpoints.py`
- **UserCreate** (26 connections) — `server/auth/endpoints.py`
- **InviteManager** (24 connections) — `server/auth/invites.py`
- **test_auth_dependencies.py** (24 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **LoginRequest** (22 connections) — `server/auth/endpoints.py`
- **auth/dependencies.py** (18 connections) — `server/auth/dependencies.py`
- **invites.py** (16 connections) — `server/auth/invites.py`
- **asyncio** (14 connections)
- **RestartInvalidatingJWTStrategy** (12 connections) — `server/auth/jwt_strategy.py`
- **get_auth_backend()** (12 connections) — `server/auth/users.py`
- **require_invite_code()** (11 connections) — `server/auth/dependencies.py`
- **list_invites()** (11 connections) — `server/auth/endpoints.py`
- **test_user.py** (11 connections) — `server/tests/unit/models/test_user.py`
- **get_current_superuser()** (10 connections) — `server/auth/dependencies.py`
- **set_auth_epoch()** (10 connections) — `server/auth/token_epoch.py`
- **create_invite()** (9 connections) — `server/auth/endpoints.py`
- **test_jwt_strategy.py** (9 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **get_current_verified_user()** (8 connections) — `server/auth/dependencies.py`
- **_check_shutdown_status()** (8 connections) — `server/auth/endpoints.py`
- **get_auth_epoch()** (8 connections) — `server/auth/token_epoch.py`
- *... and 242 more nodes in this community*

## Relationships

- [ContainerServiceError](ContainerServiceError.md) (54 shared connections)
- [get_logger](get_logger.md) (44 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (39 shared connections)
- [test_users.py](test_users.py.md) (36 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (19 shared connections)
- [get_admin_auth_service](get_admin_auth_service.md) (17 shared connections)
- [maps.py](maps.py.md) (13 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (12 shared connections)
- [log_and_raise](log_and_raise.md) (10 shared connections)
- [Invite](Invite.md) (9 shared connections)
- [players/__init__.py](players-__init__.py.md) (7 shared connections)
- [ContainerComponent](ContainerComponent.md) (5 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/auth/__init__.py`
- `server/auth/dependencies.py`
- `server/auth/endpoints.py`
- `server/auth/invites.py`
- `server/auth/jwt_strategy.py`
- `server/auth/token_epoch.py`
- `server/auth/users.py`
- `server/models/user.py`
- `server/tests/integration/test_db_connectivity.py`
- `server/tests/unit/auth/conftest.py`
- `server/tests/unit/auth/test_auth_dependencies.py`
- `server/tests/unit/auth/test_endpoints.py`
- `server/tests/unit/auth/test_jwt_strategy.py`
- `server/tests/unit/models/test_user.py`

## Audit Trail

- EXTRACTED: 814 (92%)
- INFERRED: 68 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*