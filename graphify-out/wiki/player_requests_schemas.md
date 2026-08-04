# player requests schemas

> 513 nodes

## Key Concepts

- **User** (325 connections) — `server/models/user.py`
- **user.py** (63 connections) — `server/models/user.py`
- **endpoints.py** (61 connections) — `server/auth/endpoints.py`
- **Result** (54 connections) — `scripts/run_test_ci.py`
- **test_users.py** (53 connections) — `server/tests/unit/auth/test_users.py`
- **users.py** (49 connections) — `server/auth/users.py`
- **Invite** (48 connections) — `server/models/invite.py`
- **UserManager** (46 connections) — `server/auth/users.py`
- **InviteManager** (38 connections) — `server/auth/invites.py`
- **login_user()** (33 connections) — `server/auth/endpoints.py`
- **register_user()** (31 connections) — `server/auth/endpoints.py`
- **UserCreate** (27 connections) — `server/auth/endpoints.py`
- **test_auth_dependencies.py** (24 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **LoginRequest** (23 connections) — `server/auth/endpoints.py`
- **test_endpoints_register.py** (22 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_invite_manager.py** (21 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **test_endpoints_login.py** (19 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **dependencies.py** (18 connections) — `server/auth/dependencies.py`
- **invites.py** (17 connections) — `server/auth/invites.py`
- **test_invite.py** (17 connections) — `server/tests/unit/models/test_invite.py`
- **RestartInvalidatingJWTStrategy** (15 connections) — `server/auth/jwt_strategy.py`
- **InviteRead** (15 connections) — `server/schemas/auth/invite.py`
- **test_endpoints_invites.py** (14 connections) — `server/tests/unit/auth/test_endpoints_invites.py`
- **list_invites()** (13 connections) — `server/auth/endpoints.py`
- **get_user_manager()** (13 connections) — `server/auth/users.py`
- *... and 488 more nodes in this community*

## Relationships

- [Exception Containers](Exception_Containers.md) (81 shared connections)
- [commands follow rationale](commands_follow_rationale.md) (36 shared connections)
- [profession game service](profession_game_service.md) (28 shared connections)
- [player preferences service](player_preferences_service.md) (26 shared connections)
- [Player Stats](Player_Stats.md) (25 shared connections)
- [maps handle ascii](maps_handle_ascii.md) (25 shared connections)
- [player preferences services](player_preferences_services.md) (20 shared connections)
- [NPC Combat](NPC_Combat.md) (19 shared connections)
- [metrics schemas rationale](metrics_schemas_rationale.md) (17 shared connections)
- [auth users rationale](auth_users_rationale.md) (13 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (12 shared connections)
- [npc lifecycle combat](npc_lifecycle_combat.md) (10 shared connections)

## Source Files

- `scripts/run_test_ci.py`
- `server/auth/__init__.py`
- `server/auth/dependencies.py`
- `server/auth/email_utils.py`
- `server/auth/endpoints.py`
- `server/auth/invites.py`
- `server/auth/jwt_strategy.py`
- `server/auth/users.py`
- `server/models/invite.py`
- `server/models/user.py`
- `server/schemas/auth/invite.py`
- `server/tests/integration/test_db_connectivity.py`
- `server/tests/unit/api/test_container_exception_handlers.py`
- `server/tests/unit/api/test_container_helpers_loot.py`
- `server/tests/unit/api/test_containers.py`
- `server/tests/unit/auth/test_auth_dependencies.py`
- `server/tests/unit/auth/test_endpoints_invites.py`
- `server/tests/unit/auth/test_endpoints_login.py`
- `server/tests/unit/auth/test_endpoints_login_profession.py`
- `server/tests/unit/auth/test_endpoints_register.py`

## Audit Trail

- EXTRACTED: 2076 (88%)
- INFERRED: 284 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*