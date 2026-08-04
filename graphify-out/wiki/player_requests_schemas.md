# player requests schemas

> 311 nodes

## Key Concepts

- **User** (325 connections) — `server/models/user.py`
- **user.py** (63 connections) — `server/models/user.py`
- **endpoints.py** (61 connections) — `server/auth/endpoints.py`
- **Result** (54 connections) — `scripts/run_test_ci.py`
- **Invite** (48 connections) — `server/models/invite.py`
- **InviteManager** (38 connections) — `server/auth/invites.py`
- **login_user()** (33 connections) — `server/auth/endpoints.py`
- **register_user()** (31 connections) — `server/auth/endpoints.py`
- **UserCreate** (27 connections) — `server/auth/endpoints.py`
- **game.py** (25 connections) — `server/api/game.py`
- **test_auth_dependencies.py** (24 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **LoginRequest** (23 connections) — `server/auth/endpoints.py`
- **test_endpoints_register.py** (22 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_invite_manager.py** (21 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **test_game.py** (20 connections) — `server/tests/unit/api/test_game.py`
- **test_endpoints_login.py** (19 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **dependencies.py** (18 connections) — `server/auth/dependencies.py`
- **invites.py** (17 connections) — `server/auth/invites.py`
- **test_invite.py** (17 connections) — `server/tests/unit/models/test_invite.py`
- **InviteRead** (15 connections) — `server/schemas/auth/invite.py`
- **test_endpoints_invites.py** (14 connections) — `server/tests/unit/auth/test_endpoints_invites.py`
- **list_invites()** (13 connections) — `server/auth/endpoints.py`
- **get_current_superuser()** (12 connections) — `server/auth/dependencies.py`
- **invite.py** (12 connections) — `server/models/invite.py`
- **require_invite_code()** (11 connections) — `server/auth/dependencies.py`
- *... and 286 more nodes in this community*

## Relationships

- [Exception Containers](Exception_Containers.md) (110 shared connections)
- [auth users rationale](auth_users_rationale.md) (39 shared connections)
- [metrics schemas rationale](metrics_schemas_rationale.md) (35 shared connections)
- [inventory schemas schema](inventory_schemas_schema.md) (34 shared connections)
- [maps handle ascii](maps_handle_ascii.md) (26 shared connections)
- [Player Stats](Player_Stats.md) (25 shared connections)
- [game rationale schemas](game_rationale_schemas.md) (24 shared connections)
- [Loot Generation](Loot_Generation.md) (23 shared connections)
- [profession game service](profession_game_service.md) (18 shared connections)
- [player preferences service](player_preferences_service.md) (17 shared connections)
- [Database Access Layer](Database_Access_Layer.md) (12 shared connections)
- [task registry app](task_registry_app.md) (9 shared connections)

## Source Files

- `scripts/run_test_ci.py`
- `server/api/game.py`
- `server/async_persistence.py`
- `server/auth/__init__.py`
- `server/auth/dependencies.py`
- `server/auth/endpoints.py`
- `server/auth/invites.py`
- `server/auth/users.py`
- `server/models/invite.py`
- `server/models/user.py`
- `server/schemas/auth/invite.py`
- `server/tests/unit/api/test_container_exception_handlers.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_container_helpers_loot.py`
- `server/tests/unit/api/test_containers.py`
- `server/tests/unit/api/test_game.py`
- `server/tests/unit/auth/test_auth_dependencies.py`
- `server/tests/unit/auth/test_endpoints_invites.py`
- `server/tests/unit/auth/test_endpoints_login.py`
- `server/tests/unit/auth/test_endpoints_login_profession.py`

## Audit Trail

- EXTRACTED: 1507 (86%)
- INFERRED: 241 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*