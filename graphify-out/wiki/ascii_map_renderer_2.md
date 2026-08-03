# ascii map renderer

> 67 nodes

## Key Concepts

- **login_user()** (33 connections) — `server/auth/endpoints.py`
- **register_user()** (31 connections) — `server/auth/endpoints.py`
- **LoginRequest** (23 connections) — `server/auth/endpoints.py`
- **test_endpoints_login.py** (19 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **test_endpoints_login_profession.py** (10 connections) — `server/tests/unit/auth/test_endpoints_login_profession.py`
- **_check_shutdown_status()** (8 connections) — `server/auth/endpoints.py`
- **Request** (8 connections)
- **_generate_jwt_token()** (8 connections) — `server/auth/endpoints.py`
- **_authenticate_user_credentials()** (8 connections) — `server/auth/endpoints.py`
- **LoginResponse** (7 connections) — `server/auth/endpoints.py`
- **_check_username_exists()** (7 connections) — `server/auth/endpoints.py`
- **_handle_integrity_error()** (7 connections) — `server/auth/endpoints.py`
- **_find_user_by_username()** (7 connections) — `server/auth/endpoints.py`
- **_get_user_characters()** (7 connections) — `server/auth/endpoints.py`
- **test_login_user_invalid_credentials()** (7 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **test_login_user_no_email()** (7 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **test_login_user_id_mismatch()** (7 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **test_login_user_generic_exception()** (7 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **test_login_user_authenticate_returns_none()** (7 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **test_login_user_authenticate_raises_exception()** (7 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **test_login_user_success()** (6 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **test_login_user_not_found()** (6 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **test_login_user_with_characters()** (6 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **test_login_user_http_exception_re_raised()** (6 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **test_login_user_profession_lookup_success()** (6 connections) — `server/tests/unit/auth/test_endpoints_login_profession.py`
- *... and 42 more nodes in this community*

## Relationships

- [Exception Containers](Exception_Containers.md) (35 shared connections)
- [player requests schemas](player_requests_schemas.md) (25 shared connections)
- [player service game](player_service_game.md) (18 shared connections)
- [npc combat service](npc_combat_service.md) (14 shared connections)
- [auth users rationale](auth_users_rationale.md) (4 shared connections)
- [admin auth service](admin_auth_service.md) (2 shared connections)
- [models profession rationale](models_profession_rationale.md) (1 shared connections)
- [shutdown admin command](shutdown_admin_command.md) (1 shared connections)
- [Magic Spell Service](Magic_Spell_Service.md) (1 shared connections)
- [auth rationale access](auth_rationale_access.md) (1 shared connections)
- [NPC Combat](NPC_Combat.md) (1 shared connections)
- [profession game service](profession_game_service.md) (1 shared connections)

## Source Files

- `server/auth/endpoints.py`
- `server/tests/unit/auth/test_endpoints_login.py`
- `server/tests/unit/auth/test_endpoints_login_profession.py`

## Audit Trail

- EXTRACTED: 303 (92%)
- INFERRED: 28 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*