# baseusermanager

> 186 nodes

## Key Concepts

- **endpoints.py** (66 connections) — `server/auth/endpoints.py`
- **login_user()** (35 connections) — `server/auth/endpoints.py`
- **register_user()** (32 connections) — `server/auth/endpoints.py`
- **UserCreate** (24 connections) — `server/auth/endpoints.py`
- **test_endpoints_register.py** (23 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **LoginRequest** (21 connections) — `server/auth/endpoints.py`
- **test_endpoints_login.py** (20 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **test_endpoints_invites.py** (15 connections) — `server/tests/unit/auth/test_endpoints_invites.py`
- **list_invites()** (14 connections) — `server/auth/endpoints.py`
- **asyncio** (14 connections)
- **RestartInvalidatingJWTStrategy** (13 connections) — `server/auth/jwt_strategy.py`
- **get_shutdown_blocking_message()** (13 connections) — `server/commands/admin_shutdown_command.py`
- **create_invite()** (12 connections) — `server/auth/endpoints.py`
- **test_endpoints_login_profession.py** (11 connections) — `server/tests/unit/auth/test_endpoints_login_profession.py`
- **asyncio** (11 connections)
- **set_auth_epoch()** (10 connections) — `server/auth/token_epoch.py`
- **test_jwt_strategy.py** (10 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **get_current_user_info()** (9 connections) — `server/auth/endpoints.py`
- **_authenticate_user_credentials()** (8 connections) — `server/auth/endpoints.py`
- **_check_shutdown_status()** (8 connections) — `server/auth/endpoints.py`
- **_generate_jwt_token()** (8 connections) — `server/auth/endpoints.py`
- **get_auth_epoch()** (8 connections) — `server/auth/token_epoch.py`
- **Request** (8 connections)
- **token_epoch.py** (8 connections) — `server/auth/token_epoch.py`
- **auth/conftest.py** (8 connections) — `server/tests/unit/auth/conftest.py`
- *... and 161 more nodes in this community*

## Relationships

- [dependsparam](dependsparam.md) (36 shared connections)
- [server api players](server_api_players.md) (23 shared connections)
- [claude rules fastapi](claude_rules_fastapi.md) (16 shared connections)
- [server auth invites](server_auth_invites.md) (14 shared connections)
- [authenticationbackend](authenticationbackend.md) (12 shared connections)
- [asyncio mark](asyncio_mark.md) (7 shared connections)
- [server api character creation](server_api_character_creation.md) (6 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (6 shared connections)
- [server schemas auth init](server_schemas_auth_init.md) (5 shared connections)
- [claude rules sqlalchemy](claude_rules_sqlalchemy.md) (5 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (4 shared connections)
- [server auth dependencies get current](server_auth_dependencies_get_current.md) (3 shared connections)

## Source Files

- `server/auth/endpoints.py`
- `server/auth/jwt_strategy.py`
- `server/auth/token_epoch.py`
- `server/auth/users.py`
- `server/commands/admin_shutdown_command.py`
- `server/tests/unit/auth/conftest.py`
- `server/tests/unit/auth/test_endpoints_invites.py`
- `server/tests/unit/auth/test_endpoints_login.py`
- `server/tests/unit/auth/test_endpoints_login_profession.py`
- `server/tests/unit/auth/test_endpoints_register.py`
- `server/tests/unit/auth/test_jwt_strategy.py`

## Audit Trail

- EXTRACTED: 433 (84%)
- INFERRED: 82 (16%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*