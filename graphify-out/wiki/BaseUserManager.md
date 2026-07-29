# BaseUserManager

> 235 nodes

## Key Concepts

- **Result** (52 connections) — `scripts/run_test_ci.py`
- **endpoints.py** (52 connections) — `server/auth/endpoints.py`
- **test_endpoints.py** (51 connections) — `server/tests/unit/auth/test_endpoints.py`
- **users.py** (47 connections) — `server/auth/users.py`
- **factory.py** (37 connections) — `server/app/factory.py`
- **register_user()** (28 connections) — `server/auth/endpoints.py`
- **login_user()** (28 connections) — `server/auth/endpoints.py`
- **UserCreate** (27 connections) — `server/auth/endpoints.py`
- **game.py** (25 connections) — `server/api/game.py`
- **InviteManager** (24 connections) — `server/auth/invites.py`
- **LoginRequest** (22 connections) — `server/auth/endpoints.py`
- **dependencies.py** (18 connections) — `server/auth/dependencies.py`
- **create_app()** (16 connections) — `server/app/factory.py`
- **invites.py** (16 connections) — `server/auth/invites.py`
- **main.py** (15 connections) — `server/main.py`
- **RestartInvalidatingJWTStrategy** (12 connections) — `server/auth/jwt_strategy.py`
- **get_auth_backend()** (12 connections) — `server/auth/users.py`
- **list_invites()** (10 connections) — `server/auth/endpoints.py`
- **set_auth_epoch()** (10 connections) — `server/auth/token_epoch.py`
- **InviteRead** (10 connections) — `server/schemas/auth/invite.py`
- **email_utils.py** (9 connections) — `server/auth/email_utils.py`
- **create_invite()** (9 connections) — `server/auth/endpoints.py`
- **get_username_auth_backend()** (9 connections) — `server/auth/users.py`
- **test_jwt_strategy.py** (9 connections) — `server/tests/unit/auth/test_jwt_strategy.py`
- **_check_shutdown_status()** (8 connections) — `server/auth/endpoints.py`
- *... and 210 more nodes in this community*

## Relationships

- [APIRouter](APIRouter.md) (82 shared connections)
- [main()](main%28%29.md) (35 shared connections)
- [Custom user manager for MythosMUD.](Custom_user_manager_for_MythosMUD.md) (20 shared connections)
- [test player preferences service](test_player_preferences_service.md) (13 shared connections)
- [.use invite()](use_invite%28%29.md) (10 shared connections)
- [character creation](character_creation.md) (8 shared connections)
- [Request](Request.md) (7 shared connections)
- [. init ()](_init_%28%29.md) (6 shared connections)
- [Connection Manager](Connection_Manager.md) (6 shared connections)
- [lifespan](lifespan.md) (6 shared connections)
- [AuthenticationBackend](AuthenticationBackend.md) (6 shared connections)
- [PasswordHasher](PasswordHasher.md) (5 shared connections)

## Source Files

- `scripts/generate_openapi_spec.py`
- `scripts/run_test_ci.py`
- `server/api/game.py`
- `server/app/factory.py`
- `server/auth/__init__.py`
- `server/auth/dependencies.py`
- `server/auth/email_utils.py`
- `server/auth/endpoints.py`
- `server/auth/invites.py`
- `server/auth/jwt_strategy.py`
- `server/auth/token_epoch.py`
- `server/auth/users.py`
- `server/main.py`
- `server/schemas/auth/invite.py`
- `server/tests/unit/auth/conftest.py`
- `server/tests/unit/auth/test_endpoints.py`
- `server/tests/unit/auth/test_jwt_strategy.py`
- `server/tests/unit/services/test_player_preferences_service.py`

## Audit Trail

- EXTRACTED: 1028 (89%)
- INFERRED: 127 (11%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*