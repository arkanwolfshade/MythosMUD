# ascii map renderer

> 115 nodes

## Key Concepts

- **User** (319 connections) — `server/models/user.py`
- **LoginRequest** (23 connections) — `server/auth/endpoints.py`
- **test_game.py** (20 connections) — `server/tests/unit/api/test_game.py`
- **test_endpoints_login.py** (19 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **test_user.py** (11 connections) — `server/tests/unit/models/test_user.py`
- **test_endpoints_login_profession.py** (10 connections) — `server/tests/unit/auth/test_endpoints_login_profession.py`
- **email_utils.py** (9 connections) — `server/auth/email_utils.py`
- **_get_user_characters()** (7 connections) — `server/auth/endpoints.py`
- **test_login_user_invalid_credentials()** (7 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **test_login_user_no_email()** (7 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **test_login_user_id_mismatch()** (7 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **test_login_user_generic_exception()** (7 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **test_login_user_authenticate_returns_none()** (7 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **test_login_user_authenticate_raises_exception()** (7 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **.login()** (6 connections) — `server/auth/users.py`
- **test_login_user_success()** (6 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **test_login_user_not_found()** (6 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **test_login_user_with_characters()** (6 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **test_login_user_http_exception_re_raised()** (6 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **test_login_user_profession_lookup_success()** (6 connections) — `server/tests/unit/auth/test_endpoints_login_profession.py`
- **test_login_user_profession_lookup_error()** (6 connections) — `server/tests/unit/auth/test_endpoints_login_profession.py`
- **test_login_user_profession_lookup_none()** (6 connections) — `server/tests/unit/auth/test_endpoints_login_profession.py`
- **test_login_user_player_no_profession_id()** (6 connections) — `server/tests/unit/auth/test_endpoints_login_profession.py`
- **is_bogus_email()** (5 connections) — `server/auth/email_utils.py`
- **.on_after_register()** (5 connections) — `server/auth/users.py`
- *... and 90 more nodes in this community*

## Relationships

- [auth users rationale](auth_users_rationale.md) (62 shared connections)
- [Exception Containers](Exception_Containers.md) (37 shared connections)
- [admin auth service](admin_auth_service.md) (27 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (25 shared connections)
- [game rationale schemas](game_rationale_schemas.md) (19 shared connections)
- [logging file setup](logging_file_setup.md) (18 shared connections)
- [maps handle ascii](maps_handle_ascii.md) (16 shared connections)
- [metrics schemas rationale](metrics_schemas_rationale.md) (14 shared connections)
- [player preferences service](player_preferences_service.md) (14 shared connections)
- [Player Stats](Player_Stats.md) (13 shared connections)
- [Loot Generation](Loot_Generation.md) (12 shared connections)
- [command inventory factories](command_inventory_factories.md) (10 shared connections)

## Source Files

- `server/async_persistence.py`
- `server/auth/email_utils.py`
- `server/auth/endpoints.py`
- `server/auth/users.py`
- `server/models/user.py`
- `server/tests/integration/test_db_connectivity.py`
- `server/tests/unit/api/conftest.py`
- `server/tests/unit/api/test_container_exception_handlers.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_container_helpers_loot.py`
- `server/tests/unit/api/test_containers.py`
- `server/tests/unit/api/test_game.py`
- `server/tests/unit/auth/test_endpoints_login.py`
- `server/tests/unit/auth/test_endpoints_login_profession.py`
- `server/tests/unit/infrastructure/test_async_persistence_core.py`
- `server/tests/unit/models/test_user.py`
- `server/tests/unit/services/test_admin_auth_service.py`

## Audit Trail

- EXTRACTED: 579 (85%)
- INFERRED: 100 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*