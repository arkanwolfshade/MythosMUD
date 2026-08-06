# websocket handler realtime

> 147 nodes

## Key Concepts

- **test_users.py** (53 connections) — `server/tests/unit/auth/test_users.py`
- **users.py** (49 connections) — `server/auth/users.py`
- **UserManager** (46 connections) — `server/auth/users.py`
- **RestartInvalidatingJWTStrategy** (15 connections) — `server/auth/jwt_strategy.py`
- **get_user_manager()** (13 connections) — `server/auth/users.py`
- **get_auth_backend()** (12 connections) — `server/auth/users.py`
- **test_email_utils.py** (12 connections) — `server/tests/unit/auth/test_email_utils.py`
- **get_user_db()** (11 connections) — `server/auth/users.py`
- **email_utils.py** (10 connections) — `server/auth/email_utils.py`
- **UsernameAuthenticationBackend** (9 connections) — `server/auth/users.py`
- **get_username_auth_backend()** (9 connections) — `server/auth/users.py`
- **generate_unique_bogus_email()** (8 connections) — `server/auth/email_utils.py`
- **__init__.py** (7 connections) — `server/auth/__init__.py`
- **is_bogus_email()** (7 connections) — `server/auth/email_utils.py`
- **validate_bogus_email_format()** (7 connections) — `server/auth/email_utils.py`
- **.read_token()** (7 connections) — `server/auth/jwt_strategy.py`
- **UUID** (7 connections)
- **.login()** (6 connections) — `server/auth/users.py`
- **.__init__()** (5 connections) — `server/auth/users.py`
- **.on_after_register()** (5 connections) — `server/auth/users.py`
- **.on_after_forgot_password()** (4 connections) — `server/auth/users.py`
- **.on_after_request_verify()** (4 connections) — `server/auth/users.py`
- **test_user_manager_on_after_register_bogus_email()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_register_non_bogus_email()** (4 connections) — `server/tests/unit/auth/test_users.py`
- **test_user_manager_on_after_register_no_email()** (4 connections) — `server/tests/unit/auth/test_users.py`
- *... and 122 more nodes in this community*

## Relationships

- [player requests schemas](player_requests_schemas.md) (43 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (9 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (6 shared connections)
- [package argon2 engines](package_argon2_engines.md) (5 shared connections)
- [NPC Combat](NPC_Combat.md) (2 shared connections)
- [Exception Containers](Exception_Containers.md) (2 shared connections)
- [maps handle ascii](maps_handle_ascii.md) (2 shared connections)
- [command handler processing](command_handler_processing.md) (2 shared connections)
- [useWebSocketConnectionTestFixtures useWe](useWebSocketConnectionTestFixtures_useWe.md) (2 shared connections)
- [channel broadcasting strategies](channel_broadcasting_strategies.md) (2 shared connections)
- [combat npc service](combat_npc_service.md) (1 shared connections)
- [metrics schemas rationale](metrics_schemas_rationale.md) (1 shared connections)

## Source Files

- `server/auth/__init__.py`
- `server/auth/email_utils.py`
- `server/auth/jwt_strategy.py`
- `server/auth/users.py`
- `server/tests/unit/auth/test_email_utils.py`
- `server/tests/unit/auth/test_users.py`

## Audit Trail

- EXTRACTED: 517 (96%)
- INFERRED: 21 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*