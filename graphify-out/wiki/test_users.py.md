# test_users.py

> 288 nodes

## Key Concepts

- **test_users.py** (60 connections) — `server/tests/unit/auth/test_users.py`
- **endpoints.py** (52 connections) — `server/auth/endpoints.py`
- **test_endpoints.py** (51 connections) — `server/tests/unit/auth/test_endpoints.py`
- **UserManager** (46 connections) — `server/auth/users.py`
- **asyncio** (36 connections)
- **login_user()** (29 connections) — `server/auth/endpoints.py`
- **register_user()** (29 connections) — `server/auth/endpoints.py`
- **UserCreate** (26 connections) — `server/auth/endpoints.py`
- **InviteManager** (24 connections) — `server/auth/invites.py`
- **LoginRequest** (22 connections) — `server/auth/endpoints.py`
- **asyncio** (20 connections)
- **invites.py** (16 connections) — `server/auth/invites.py`
- **is_shutdown_pending()** (14 connections) — `server/commands/admin_shutdown_command.py`
- **get_shutdown_blocking_message()** (13 connections) — `server/commands/admin_shutdown_command.py`
- **list_invites()** (11 connections) — `server/auth/endpoints.py`
- **get_current_user_with_logging()** (11 connections) — `server/auth/users.py`
- **UsernameAuthenticationBackend** (10 connections) — `server/auth/users.py`
- **create_invite()** (9 connections) — `server/auth/endpoints.py`
- **get_username_auth_backend()** (9 connections) — `server/auth/users.py`
- **_check_shutdown_status()** (8 connections) — `server/api/character_creation.py`
- **_check_shutdown_status()** (8 connections) — `server/auth/endpoints.py`
- **get_user_manager()** (8 connections) — `server/auth/users.py`
- **Request** (8 connections)
- **LoginResponse** (7 connections) — `server/auth/endpoints.py`
- **_authenticate_user_credentials()** (7 connections) — `server/auth/endpoints.py`
- *... and 263 more nodes in this community*

## Relationships

- [User](User.md) (78 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (11 shared connections)
- [Invite](Invite.md) (8 shared connections)
- [test_admin_shutdown_command.py](test_admin_shutdown_command.py.md) (8 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (7 shared connections)
- [lifespan.py](lifespan.py.md) (6 shared connections)
- [get_logger](get_logger.md) (6 shared connections)
- [factory.py](factory.py.md) (4 shared connections)
- [test_argon2_utils.py](test_argon2_utils.py.md) (4 shared connections)
- [AttributeError](AttributeError.md) (4 shared connections)
- [admin_shutdown_command.py](admin_shutdown_command.py.md) (3 shared connections)
- [server/exceptions.py](server-exceptions.py.md) (3 shared connections)

## Source Files

- `server/api/character_creation.py`
- `server/auth/__init__.py`
- `server/auth/endpoints.py`
- `server/auth/invites.py`
- `server/auth/users.py`
- `server/commands/admin_shutdown_command.py`
- `server/tests/unit/auth/test_endpoints.py`
- `server/tests/unit/auth/test_users.py`

## Audit Trail

- EXTRACTED: 672 (97%)
- INFERRED: 19 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*