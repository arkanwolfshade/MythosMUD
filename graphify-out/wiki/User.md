# User

> 341 nodes

## Key Concepts

- **User** (310 connections) — `server/models/user.py`
- **endpoints.py** (66 connections) — `server/auth/endpoints.py`
- **test_users.py** (53 connections) — `server/tests/unit/auth/test_users.py`
- **users.py** (48 connections) — `server/auth/users.py`
- **UserManager** (41 connections) — `server/auth/users.py`
- **login_user()** (35 connections) — `server/auth/endpoints.py`
- **test_auth_dependencies.py** (24 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **LoginRequest** (22 connections) — `server/auth/endpoints.py`
- **test_endpoints_login.py** (20 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **auth/dependencies.py** (18 connections) — `server/auth/dependencies.py`
- **list_invites()** (14 connections) — `server/auth/endpoints.py`
- **asyncio** (14 connections)
- **test_endpoints_invites.py** (14 connections) — `server/tests/unit/auth/test_endpoints_invites.py`
- **RestartInvalidatingJWTStrategy** (13 connections) — `server/auth/jwt_strategy.py`
- **get_user_manager()** (13 connections) — `server/auth/users.py`
- **InviteRead** (12 connections) — `server/schemas/auth/invite.py`
- **get_current_superuser()** (12 connections) — `server/auth/dependencies.py`
- **create_invite()** (12 connections) — `server/auth/endpoints.py`
- **get_auth_backend()** (12 connections) — `server/auth/users.py`
- **test_users_current_user_logging.py** (12 connections) — `server/tests/unit/auth/test_users_current_user_logging.py`
- **require_invite_code()** (11 connections) — `server/auth/dependencies.py`
- **get_current_user_with_logging()** (11 connections) — `server/auth/users.py`
- **get_user_db()** (11 connections) — `server/auth/users.py`
- **asyncio** (11 connections)
- **asyncio** (11 connections)
- *... and 316 more nodes in this community*

## Relationships

- [LoggedHTTPException](LoggedHTTPException.md) (50 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (29 shared connections)
- [register_user](register_user.md) (28 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (27 shared connections)
- [ExplorationService](ExplorationService.md) (25 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (19 shared connections)
- [Player](Player.md) (19 shared connections)
- [SecureBaseModel](SecureBaseModel.md) (18 shared connections)
- [Invite](Invite.md) (18 shared connections)
- [test_metrics_endpoints.py](test_metrics_endpoints.py.md) (15 shared connections)
- [RoomService](RoomService.md) (11 shared connections)
- [handle_transfer_items_exceptions](handle_transfer_items_exceptions.md) (8 shared connections)

## Source Files

- `server/auth/__init__.py`
- `server/auth/dependencies.py`
- `server/auth/endpoints.py`
- `server/auth/invites.py`
- `server/auth/jwt_strategy.py`
- `server/auth/token_epoch.py`
- `server/auth/users.py`
- `server/models/user.py`
- `server/schemas/auth/invite.py`
- `server/tests/unit/auth/conftest.py`
- `server/tests/unit/auth/test_auth_dependencies.py`
- `server/tests/unit/auth/test_endpoints_invites.py`
- `server/tests/unit/auth/test_endpoints_login.py`
- `server/tests/unit/auth/test_endpoints_login_profession.py`
- `server/tests/unit/auth/test_jwt_strategy.py`
- `server/tests/unit/auth/test_users.py`
- `server/tests/unit/auth/test_users_current_user_logging.py`
- `server/tests/unit/models/test_user.py`

## Audit Trail

- EXTRACTED: 897 (87%)
- INFERRED: 137 (13%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*