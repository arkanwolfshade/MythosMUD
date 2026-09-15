# LoggedHTTPException

> 215 nodes

## Key Concepts

- **LoggedHTTPException** (374 connections) — `server/exceptions.py`
- **endpoints.py** (66 connections) — `server/auth/endpoints.py`
- **login_user()** (35 connections) — `server/auth/endpoints.py`
- **UserCreate** (31 connections) — `server/auth/endpoints.py`
- **register_user()** (31 connections) — `server/auth/endpoints.py`
- **test_endpoints_register.py** (30 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **LoginRequest** (22 connections) — `server/auth/endpoints.py`
- **test_endpoints_login.py** (20 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **asyncio** (18 connections)
- **list_invites()** (14 connections) — `server/auth/endpoints.py`
- **test_endpoints_invites.py** (14 connections) — `server/tests/unit/auth/test_endpoints_invites.py`
- **RestartInvalidatingJWTStrategy** (13 connections) — `server/auth/jwt_strategy.py`
- **get_current_superuser()** (12 connections) — `server/auth/dependencies.py`
- **create_invite()** (12 connections) — `server/auth/endpoints.py`
- **_persist_new_user()** (12 connections) — `server/auth/endpoints.py`
- **asyncio** (11 connections)
- **set_auth_epoch()** (10 connections) — `server/auth/token_epoch.py`
- **_mock_invite_manager()** (10 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_endpoints_login_profession.py** (10 connections) — `server/tests/unit/auth/test_endpoints_login_profession.py`
- **get_current_user_info()** (9 connections) — `server/auth/endpoints.py`
- **test_jwt_strategy.py** (9 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **_authenticate_user_credentials()** (8 connections) — `server/auth/endpoints.py`
- **_check_shutdown_status()** (8 connections) — `server/auth/endpoints.py`
- **_generate_jwt_token()** (8 connections) — `server/auth/endpoints.py`
- **get_auth_epoch()** (8 connections) — `server/auth/token_epoch.py`
- *... and 190 more nodes in this community*

## Relationships

- [User](User.md) (90 shared connections)
- [Invite](Invite.md) (40 shared connections)
- [players.py](players.py.md) (39 shared connections)
- [get_logger](get_logger.md) (29 shared connections)
- [api/character_creation.py](api-character_creation.py.md) (27 shared connections)
- [api/monitoring.py](api-monitoring.py.md) (19 shared connections)
- [test_player_respawn_api.py](test_player_respawn_api.py.md) (18 shared connections)
- [test_admin_auth_service.py](test_admin_auth_service.py.md) (17 shared connections)
- [maps.py](maps.py.md) (16 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (15 shared connections)
- [test_metrics_endpoints.py](test_metrics_endpoints.py.md) (15 shared connections)
- [rooms.py](rooms.py.md) (15 shared connections)

## Source Files

- `server/auth/dependencies.py`
- `server/auth/endpoints.py`
- `server/auth/invites.py`
- `server/auth/jwt_strategy.py`
- `server/auth/token_epoch.py`
- `server/auth/users.py`
- `server/exceptions.py`
- `server/tests/unit/auth/conftest.py`
- `server/tests/unit/auth/test_auth_dependencies.py`
- `server/tests/unit/auth/test_endpoints_invites.py`
- `server/tests/unit/auth/test_endpoints_login.py`
- `server/tests/unit/auth/test_endpoints_login_profession.py`
- `server/tests/unit/auth/test_endpoints_register.py`
- `server/tests/unit/auth/test_jwt_strategy.py`
- `server/tests/unit/test_exceptions.py`
- `server/tests/unit/test_exceptions_comprehensive.py`

## Audit Trail

- EXTRACTED: 694 (76%)
- INFERRED: 220 (24%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*