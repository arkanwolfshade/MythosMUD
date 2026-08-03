# auth users rationale

> 583 nodes

## Key Concepts

- **User** (315 connections) — `server/models/user.py`
- **test_users.py** (60 connections) — `server/tests/unit/auth/test_users.py`
- **endpoints.py** (59 connections) — `server/auth/endpoints.py`
- **user.py** (58 connections) — `server/models/user.py`
- **Result** (52 connections) — `scripts/run_test_ci.py`
- **test_endpoints.py** (51 connections) — `server/tests/unit/auth/test_endpoints.py`
- **users.py** (48 connections) — `server/auth/users.py`
- **UserManager** (48 connections) — `server/auth/users.py`
- **test_argon2_utils.py** (42 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **Invite** (38 connections) — `server/models/invite.py`
- **login_user()** (32 connections) — `server/auth/endpoints.py`
- **register_user()** (31 connections) — `server/auth/endpoints.py`
- **hash_password()** (27 connections) — `server/auth/argon2_utils.py`
- **UserCreate** (27 connections) — `server/auth/endpoints.py`
- **subject_controller.py** (26 connections) — `server/api/admin/subject_controller.py`
- **InviteManager** (25 connections) — `server/auth/invites.py`
- **test_auth_dependencies.py** (24 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **LoginRequest** (22 connections) — `server/auth/endpoints.py`
- **create_character_with_stats()** (18 connections) — `server/api/character_creation.py`
- **argon2_utils.py** (18 connections) — `server/auth/argon2_utils.py`
- **dependencies.py** (18 connections) — `server/auth/dependencies.py`
- **test_invite.py** (17 connections) — `server/tests/unit/models/test_invite.py`
- **verify_password()** (16 connections) — `server/auth/argon2_utils.py`
- **invites.py** (16 connections) — `server/auth/invites.py`
- **list_invites()** (13 connections) — `server/auth/endpoints.py`
- *... and 558 more nodes in this community*

## Relationships

- [Exception Containers](Exception_Containers.md) (114 shared connections)
- [admin auth service](admin_auth_service.md) (44 shared connections)
- [Player Stats](Player_Stats.md) (38 shared connections)
- [player preferences service](player_preferences_service.md) (25 shared connections)
- [NATS Messaging](NATS_Messaging.md) (22 shared connections)
- [maps handle ascii](maps_handle_ascii.md) (22 shared connections)
- [character creation validate](character_creation_validate.md) (17 shared connections)
- [metrics schemas rationale](metrics_schemas_rationale.md) (17 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (16 shared connections)
- [world models rationale](world_models_rationale.md) (15 shared connections)
- [command inventory factories](command_inventory_factories.md) (13 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (12 shared connections)

## Source Files

- `scripts/run_test_ci.py`
- `server/api/admin/subject_controller.py`
- `server/api/character_creation.py`
- `server/api/player_helpers.py`
- `server/auth/__init__.py`
- `server/auth/argon2_utils.py`
- `server/auth/dependencies.py`
- `server/auth/email_utils.py`
- `server/auth/endpoints.py`
- `server/auth/invites.py`
- `server/auth/jwt_strategy.py`
- `server/auth/token_epoch.py`
- `server/auth/users.py`
- `server/commands/admin_shutdown_command.py`
- `server/models/invite.py`
- `server/models/user.py`
- `server/schemas/auth/invite.py`
- `server/tests/integration/test_db_connectivity.py`
- `server/tests/unit/auth/conftest.py`
- `server/tests/unit/auth/test_argon2_utils.py`

## Audit Trail

- EXTRACTED: 2418 (92%)
- INFERRED: 220 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*