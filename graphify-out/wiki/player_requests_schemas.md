# player requests schemas

> 288 nodes

## Key Concepts

- **User** (325 connections) — `server/models/user.py`
- **endpoints.py** (61 connections) — `server/auth/endpoints.py`
- **Result** (54 connections) — `scripts/run_test_ci.py`
- **Invite** (48 connections) — `server/models/invite.py`
- **InviteManager** (38 connections) — `server/auth/invites.py`
- **login_user()** (33 connections) — `server/auth/endpoints.py`
- **register_user()** (31 connections) — `server/auth/endpoints.py`
- **UserCreate** (27 connections) — `server/auth/endpoints.py`
- **LoginRequest** (23 connections) — `server/auth/endpoints.py`
- **test_endpoints_register.py** (22 connections) — `server/tests/unit/auth/test_endpoints_register.py`
- **test_invite_manager.py** (21 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **test_endpoints_login.py** (19 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **invites.py** (17 connections) — `server/auth/invites.py`
- **test_invite.py** (17 connections) — `server/tests/unit/models/test_invite.py`
- **InviteRead** (15 connections) — `server/schemas/auth/invite.py`
- **test_endpoints_invites.py** (14 connections) — `server/tests/unit/auth/test_endpoints_invites.py`
- **list_invites()** (13 connections) — `server/auth/endpoints.py`
- **get_current_superuser()** (12 connections) — `server/auth/dependencies.py`
- **invite.py** (12 connections) — `server/models/invite.py`
- **create_invite()** (11 connections) — `server/auth/endpoints.py`
- **get_invite_manager()** (11 connections) — `server/auth/invites.py`
- **test_procedures_return_shape.py** (11 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **test_user.py** (11 connections) — `server/tests/unit/models/test_user.py`
- **test_endpoints_login_profession.py** (10 connections) — `server/tests/unit/auth/test_endpoints_login_profession.py`
- **_check_shutdown_status()** (8 connections) — `server/auth/endpoints.py`
- *... and 263 more nodes in this community*

## Relationships

- [persistence container rationale](persistence_container_rationale.md) (69 shared connections)
- [services inventory mutation](services_inventory_mutation.md) (58 shared connections)
- [Exception Containers](Exception_Containers.md) (45 shared connections)
- [auth users rationale](auth_users_rationale.md) (35 shared connections)
- [player preferences service](player_preferences_service.md) (25 shared connections)
- [commands shutdown process](commands_shutdown_process.md) (23 shared connections)
- [Player Stats](Player_Stats.md) (23 shared connections)
- [commands admin helpers](commands_admin_helpers.md) (21 shared connections)
- [maps handle ascii](maps_handle_ascii.md) (17 shared connections)
- [metrics schemas rationale](metrics_schemas_rationale.md) (14 shared connections)
- [fixtures return shape](fixtures_return_shape.md) (8 shared connections)
- [feature services flag](feature_services_flag.md) (7 shared connections)

## Source Files

- `scripts/run_test_ci.py`
- `server/async_persistence.py`
- `server/auth/dependencies.py`
- `server/auth/endpoints.py`
- `server/auth/invites.py`
- `server/auth/token_epoch.py`
- `server/auth/users.py`
- `server/models/invite.py`
- `server/models/user.py`
- `server/schemas/auth/invite.py`
- `server/tests/integration/test_db_connectivity.py`
- `server/tests/integration/test_procedures_return_shape.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_container_helpers_loot.py`
- `server/tests/unit/api/test_containers.py`
- `server/tests/unit/api/test_game.py`
- `server/tests/unit/auth/test_auth_dependencies.py`
- `server/tests/unit/auth/test_endpoints_invites.py`
- `server/tests/unit/auth/test_endpoints_login.py`
- `server/tests/unit/auth/test_endpoints_login_profession.py`

## Audit Trail

- EXTRACTED: 1329 (85%)
- INFERRED: 232 (15%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*