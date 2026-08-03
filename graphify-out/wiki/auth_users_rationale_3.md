# auth users rationale

> 122 nodes

## Key Concepts

- **test_users.py** (53 connections) — `server/tests/unit/auth/test_users.py`
- **UserManager** (46 connections) — `server/auth/users.py`
- **get_user_manager()** (13 connections) — `server/auth/users.py`
- **get_auth_backend()** (12 connections) — `server/auth/users.py`
- **get_user_db()** (11 connections) — `server/auth/users.py`
- **UsernameAuthenticationBackend** (9 connections) — `server/auth/users.py`
- **get_username_auth_backend()** (9 connections) — `server/auth/users.py`
- **UUID** (7 connections)
- **validate_jwt_secret()** (6 connections) — `server/auth/users.py`
- **.login()** (6 connections) — `server/auth/users.py`
- **.__init__()** (5 connections) — `server/auth/users.py`
- **.on_after_register()** (5 connections) — `server/auth/users.py`
- **.on_after_forgot_password()** (4 connections) — `server/auth/users.py`
- **.on_after_request_verify()** (4 connections) — `server/auth/users.py`
- **test_user_manager_on_after_register_bogus_email()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_register_non_bogus_email()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_register_no_email()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_register_with_request()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_forgot_password()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_request_verify()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_get_user_manager()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_username_authentication_backend_login()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_forgot_password_with_request()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_request_verify_with_request()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_get_username_auth_backend_returns_username_authentication_backend()** (4 connections) — `server/tests/unit/auth/test_users.py`
- *... and 97 more nodes in this community*

## Relationships

- [Exception Containers](Exception_Containers.md) (17 shared connections)
- [admin auth service](admin_auth_service.md) (10 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (7 shared connections)
- [player requests schemas](player_requests_schemas.md) (6 shared connections)
- [ascii map renderer](ascii_map_renderer.md) (4 shared connections)
- [player service game](player_service_game.md) (3 shared connections)
- [channel broadcasting strategies](channel_broadcasting_strategies.md) (2 shared connections)
- [auth users rationale](auth_users_rationale.md) (1 shared connections)
- [models npc rationale](models_npc_rationale.md) (1 shared connections)
- [skill service game](skill_service_game.md) (1 shared connections)

## Source Files

- `server/auth/users.py`
- `server/tests/unit/auth/test_users.py`

## Audit Trail

- EXTRACTED: 384 (96%)
- INFERRED: 16 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*