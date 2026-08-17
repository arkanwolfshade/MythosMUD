# User

> 190 nodes

## Key Concepts

- **User** (293 connections) — `server/models/user.py`
- **endpoints.py** (66 connections) — `server/auth/endpoints.py`
- **login_user()** (35 connections) — `server/auth/endpoints.py`
- **register_user()** (32 connections) — `server/auth/endpoints.py`
- **UserCreate** (24 connections) — `server/auth/endpoints.py`
- **test_endpoints_register.py** (23 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **LoginRequest** (21 connections) — `server/auth/endpoints.py`
- **test_endpoints_login.py** (20 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **test_endpoints_invites.py** (15 connections) — `server/tests/unit/auth/test_endpoints_invites.py`
- **list_invites()** (14 connections) — `server/auth/endpoints.py`
- **is_shutdown_pending()** (14 connections) — `server/commands/admin_shutdown_command.py`
- **asyncio** (14 connections)
- **get_shutdown_blocking_message()** (13 connections) — `server/commands/admin_shutdown_command.py`
- **InviteRead** (12 connections) — `server/schemas/auth/invite.py`
- **create_invite()** (12 connections) — `server/auth/endpoints.py`
- **test_endpoints_login_profession.py** (11 connections) — `server/tests/unit/auth/test_endpoints_login_profession.py`
- **asyncio** (11 connections)
- **test_user.py** (11 connections) — `server/tests/unit/models/test_user.py`
- **get_current_user_info()** (9 connections) — `server/auth/endpoints.py`
- **_check_shutdown_status()** (8 connections) — `server/api/character_creation.py`
- **_prepare_create_character_request()** (8 connections) — `server/api/character_creation.py`
- **_authenticate_user_credentials()** (8 connections) — `server/auth/endpoints.py`
- **_check_shutdown_status()** (8 connections) — `server/auth/endpoints.py`
- **_generate_jwt_token()** (8 connections) — `server/auth/endpoints.py`
- **Request** (8 connections)
- *... and 165 more nodes in this community*

## Relationships

- [LoggedHTTPException](LoggedHTTPException.md) (45 shared connections)
- [Invite](Invite.md) (32 shared connections)
- [models/user.py](models-user.py.md) (26 shared connections)
- [get_logger](get_logger.md) (25 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (24 shared connections)
- [test_users.py](test_users.py.md) (24 shared connections)
- [maps.py](maps.py.md) (24 shared connections)
- [PlayerService](PlayerService.md) (22 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (18 shared connections)
- [DatabaseError](DatabaseError.md) (12 shared connections)
- [pytest.md](pytest.md.md) (11 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (11 shared connections)

## Source Files

- `server/api/character_creation.py`
- `server/auth/endpoints.py`
- `server/commands/admin_shutdown_command.py`
- `server/models/user.py`
- `server/schemas/auth/invite.py`
- `server/tests/integration/test_db_connectivity.py`
- `server/tests/unit/auth/test_endpoints_invites.py`
- `server/tests/unit/auth/test_endpoints_login.py`
- `server/tests/unit/auth/test_endpoints_login_profession.py`
- `server/tests/unit/auth/test_endpoints_register.py`
- `server/tests/unit/models/test_user.py`

## Audit Trail

- EXTRACTED: 615 (81%)
- INFERRED: 146 (19%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*