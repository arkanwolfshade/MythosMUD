# Connection Manager

> 234 nodes

## Key Concepts

- **User** (306 connections) — `server/models/user.py`
- **Result** (52 connections) — `scripts/run_test_ci.py`
- **endpoints.py** (52 connections) — `server/auth/endpoints.py`
- **test_endpoints.py** (51 connections) — `server/tests/unit/auth/test_endpoints.py`
- **register_user()** (28 connections) — `server/auth/endpoints.py`
- **login_user()** (28 connections) — `server/auth/endpoints.py`
- **UserCreate** (27 connections) — `server/auth/endpoints.py`
- **InviteManager** (24 connections) — `server/auth/invites.py`
- **LoginRequest** (22 connections) — `server/auth/endpoints.py`
- **RestartInvalidatingJWTStrategy** (12 connections) — `server/auth/jwt_strategy.py`
- **test_user.py** (11 connections) — `server/tests/unit/models/test_user.py`
- **get_current_superuser()** (10 connections) — `server/auth/dependencies.py`
- **list_invites()** (10 connections) — `server/auth/endpoints.py`
- **set_auth_epoch()** (10 connections) — `server/auth/token_epoch.py`
- **InviteRead** (10 connections) — `server/schemas/auth/invite.py`
- **CharacterInfo** (10 connections) — `server/schemas/players/player.py`
- **create_invite()** (9 connections) — `server/auth/endpoints.py`
- **test_jwt_strategy.py** (9 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **get_current_verified_user()** (8 connections) — `server/auth/dependencies.py`
- **_check_shutdown_status()** (8 connections) — `server/auth/endpoints.py`
- **Request** (8 connections)
- **token_epoch.py** (8 connections) — `server/auth/token_epoch.py`
- **get_auth_epoch()** (8 connections) — `server/auth/token_epoch.py`
- **LoginResponse** (7 connections) — `server/auth/endpoints.py`
- **_validate_invite_code()** (7 connections) — `server/auth/endpoints.py`
- *... and 209 more nodes in this community*

## Relationships

- [close db()](close_db%28%29.md) (63 shared connections)
- [AbstractContextManager](AbstractContextManager.md) (61 shared connections)
- [. init ()](_init_%28%29.md) (34 shared connections)
- [equipment helpers](equipment_helpers.md) (25 shared connections)
- [append unique valid occupant()](append_unique_valid_occupant%28%29.md) (22 shared connections)
- [ExitStack](ExitStack.md) (20 shared connections)
- [admin shutdown command](admin_shutdown_command.md) (17 shared connections)
- [APIRouter](APIRouter.md) (17 shared connections)
- [metrics](metrics.md) (14 shared connections)
- [BaseCommand](BaseCommand.md) (12 shared connections)
- [AsyncSessionFactory](AsyncSessionFactory.md) (11 shared connections)
- [init](init.md) (11 shared connections)

## Source Files

- `scripts/run_test_ci.py`
- `server/api/character_creation.py`
- `server/async_persistence.py`
- `server/auth/dependencies.py`
- `server/auth/email_utils.py`
- `server/auth/endpoints.py`
- `server/auth/invites.py`
- `server/auth/jwt_strategy.py`
- `server/auth/token_epoch.py`
- `server/models/user.py`
- `server/schemas/auth/invite.py`
- `server/schemas/players/player.py`
- `server/tests/integration/test_db_connectivity.py`
- `server/tests/unit/api/test_character_creation.py`
- `server/tests/unit/api/test_container_exception_handlers.py`
- `server/tests/unit/api/test_container_helpers_loot.py`
- `server/tests/unit/api/test_containers.py`
- `server/tests/unit/auth/conftest.py`
- `server/tests/unit/auth/test_auth_dependencies.py`
- `server/tests/unit/auth/test_endpoints.py`

## Audit Trail

- EXTRACTED: 1089 (85%)
- INFERRED: 192 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*