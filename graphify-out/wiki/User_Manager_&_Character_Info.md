# User Manager & Character Info

> 246 nodes

## Key Concepts

- **LoggedHTTPException** (355 connections) — `server/exceptions.py`
- **endpoints.py** (66 connections) — `server/auth/endpoints.py`
- **login_user()** (35 connections) — `server/auth/endpoints.py`
- **register_user()** (31 connections) — `server/auth/endpoints.py`
- **UserCreate** (30 connections) — `server/auth/endpoints.py`
- **test_endpoints_register.py** (30 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_auth_dependencies.py** (24 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **LoginRequest** (22 connections) — `server/auth/endpoints.py`
- **test_endpoints_login.py** (20 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **asyncio** (18 connections)
- **TestLootAllItems** (16 connections) — `server/tests/unit/api/test_container_endpoints_loot.py`
- **asyncio** (14 connections)
- **get_current_superuser()** (12 connections) — `server/auth/dependencies.py`
- **_persist_new_user()** (12 connections) — `server/auth/endpoints.py`
- **require_invite_code()** (11 connections) — `server/auth/dependencies.py`
- **asyncio** (11 connections)
- **RestartInvalidatingJWTStrategy** (10 connections) — `server/auth/jwt_strategy.py`
- **set_auth_epoch()** (10 connections) — `server/auth/token_epoch.py`
- **_mock_invite_manager()** (10 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_endpoints_login_profession.py** (10 connections) — `server/tests/unit/auth/test_endpoints_login_profession.py`
- **asyncio** (9 connections)
- **test_jwt_strategy.py** (9 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **get_current_verified_user()** (8 connections) — `server/auth/dependencies.py`
- **_authenticate_user_credentials()** (8 connections) — `server/auth/endpoints.py`
- **_check_shutdown_status()** (8 connections) — `server/auth/endpoints.py`
- *... and 221 more nodes in this community*

## Relationships

- [Character Creation & Auth Dependencies](Character_Creation_&_Auth_Dependencies.md) (113 shared connections)
- [Admin NPC Management API](Admin_NPC_Management_API.md) (41 shared connections)
- [Community 144](Community_144.md) (28 shared connections)
- [DI Containers & API Bootstrap](DI_Containers_&_API_Bootstrap.md) (27 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (22 shared connections)
- [Community 479](Community_479.md) (18 shared connections)
- [Community 178](Community_178.md) (17 shared connections)
- [Community 79](Community_79.md) (16 shared connections)
- [Player Effects (Corruption/Fear/Lucidity)](Player_Effects_Corruption-Fear-Lucidity.md) (15 shared connections)
- [Community 140](Community_140.md) (15 shared connections)
- [Community 71](Community_71.md) (15 shared connections)
- [Community 43](Community_43.md) (14 shared connections)

## Source Files

- `server/auth/dependencies.py`
- `server/auth/endpoints.py`
- `server/auth/invites.py`
- `server/auth/jwt_strategy.py`
- `server/auth/token_epoch.py`
- `server/auth/users.py`
- `server/exceptions.py`
- `server/tests/unit/api/test_container_endpoints_loot.py`
- `server/tests/unit/auth/conftest.py`
- `server/tests/unit/auth/test_auth_dependencies.py`
- `server/tests/unit/auth/test_endpoints_login.py`
- `server/tests/unit/auth/test_endpoints_login_profession.py`
- `server/tests/unit/auth/test_endpoints_register.py`
- `server/tests/unit/auth/test_jwt_strategy.py`
- `server/tests/unit/test_exceptions.py`
- `server/tests/unit/test_exceptions_comprehensive.py`

## Audit Trail

- EXTRACTED: 754 (78%)
- INFERRED: 208 (22%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*