# player service game

> 90 nodes

## Key Concepts

- **factory.py** (45 connections) — `server/app/factory.py`
- **UserCreate** (27 connections) — `server/auth/endpoints.py`
- **test_endpoints_register.py** (22 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **main.py** (15 connections) — `server/main.py`
- **create_app()** (14 connections) — `server/app/factory.py`
- **CORSConfigDict** (7 connections) — `server/app/factory.py`
- **_register_v1_routers()** (7 connections) — `server/app/factory.py`
- **test_register_user_duplicate_username()** (7 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_register_user_integrity_error()** (7 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_register_user_email_constraint_violation()** (7 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_register_user_username_constraint_violation()** (7 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_register_user_generic_constraint_violation()** (7 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **_get_cors_config_from_app_config()** (6 connections) — `server/app/factory.py`
- **_parse_cors_env_vars()** (6 connections) — `server/app/factory.py`
- **_configure_cors()** (6 connections) — `server/app/factory.py`
- **UserRead** (6 connections) — `server/auth/endpoints.py`
- **UserUpdate** (6 connections) — `server/auth/endpoints.py`
- **_create_user_object()** (6 connections) — `server/auth/endpoints.py`
- **IntegrityError** (6 connections)
- **test_register_user_success()** (6 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **_apply_cors_env_overrides()** (5 connections) — `server/app/factory.py`
- **test_register_user_shutdown_pending()** (5 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_register_user_no_email()** (5 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_register_user_invite_validation_failure()** (5 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_register_user_invite_marking_success()** (5 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- *... and 65 more nodes in this community*

## Relationships

- [ascii map renderer](ascii_map_renderer.md) (18 shared connections)
- [Exception Containers](Exception_Containers.md) (12 shared connections)
- [models npc rationale](models_npc_rationale.md) (11 shared connections)
- [player requests schemas](player_requests_schemas.md) (11 shared connections)
- [npc combat service](npc_combat_service.md) (11 shared connections)
- [auth users rationale](auth_users_rationale.md) (4 shared connections)
- [admin auth service](admin_auth_service.md) (3 shared connections)
- [middleware comprehensive logging](middleware_comprehensive_logging.md) (3 shared connections)
- [middleware error handling](middleware_error_handling.md) (3 shared connections)
- [Player Stats](Player_Stats.md) (2 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [message broadcaster realtime](message_broadcaster_realtime.md) (2 shared connections)

## Source Files

- `scripts/generate_openapi_spec.py`
- `server/app/factory.py`
- `server/auth/endpoints.py`
- `server/main.py`
- `server/tests/unit/auth/test_endpoints_register.py`
- `server/tests/unit/services/test_player_preferences_service.py`

## Audit Trail

- EXTRACTED: 320 (88%)
- INFERRED: 45 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*