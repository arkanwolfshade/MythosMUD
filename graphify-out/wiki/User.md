# User

> 231 nodes

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
- **require_invite_code()** (11 connections) — `server/auth/dependencies.py`
- **list_invites()** (11 connections) — `server/auth/endpoints.py`
- **test_user.py** (11 connections) — `server/tests/unit/models/test_user.py`
- **get_current_superuser()** (10 connections) — `server/auth/dependencies.py`
- **create_invite()** (9 connections) — `server/auth/endpoints.py`
- **get_current_verified_user()** (8 connections) — `server/auth/dependencies.py`
- **_check_shutdown_status()** (8 connections) — `server/auth/endpoints.py`
- **Request** (8 connections)
- **LoginResponse** (7 connections) — `server/auth/endpoints.py`
- **_authenticate_user_credentials()** (7 connections) — `server/auth/endpoints.py`
- **_find_user_by_username()** (7 connections) — `server/auth/endpoints.py`
- **get_current_user_info()** (7 connections) — `server/auth/endpoints.py`
- *... and 206 more nodes in this community*

## Relationships

- [LoggedHTTPException](LoggedHTTPException.md) (49 shared connections)
- [database.py](database.py.md) (41 shared connections)
- [test_users.py](test_users.py.md) (26 shared connections)
- [ContainerServiceError](ContainerServiceError.md) (24 shared connections)
- [PlayerService](PlayerService.md) (24 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (19 shared connections)
- [test_metrics_endpoints.py](test_metrics_endpoints.py.md) (12 shared connections)
- [Invite](Invite.md) (11 shared connections)
- [api/game.py](api-game.py.md) (11 shared connections)
- [Player](Player.md) (9 shared connections)
- [maps.py](maps.py.md) (8 shared connections)
- [lifespan.py](lifespan.py.md) (7 shared connections)

## Source Files

- `docs/examples/logging/fastapi_integration.py`
- `docs/examples/logging/websocket_integration.py`
- `server/auth/__init__.py`
- `server/auth/dependencies.py`
- `server/auth/endpoints.py`
- `server/auth/invites.py`
- `server/models/user.py`
- `server/tests/unit/auth/test_auth_dependencies.py`
- `server/tests/unit/auth/test_endpoints.py`
- `server/tests/unit/models/test_user.py`

## Audit Trail

- EXTRACTED: 1219 (94%)
- INFERRED: 76 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*