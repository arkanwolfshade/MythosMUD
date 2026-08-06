# player requests schemas

> 308 nodes

## Key Concepts

- **User** (325 connections) — `server/models/user.py`
- **endpoints.py** (61 connections) — `server/auth/endpoints.py`
- **Result** (54 connections) — `scripts/run_test_ci.py`
- **Invite** (48 connections) — `server/models/invite.py`
- **factory.py** (45 connections) — `server/app/factory.py`
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
- **invite.py** (12 connections) — `server/models/invite.py`
- **create_invite()** (11 connections) — `server/auth/endpoints.py`
- **get_invite_manager()** (11 connections) — `server/auth/invites.py`
- **test_procedures_return_shape.py** (11 connections) — `server/tests/integration/test_procedures_return_shape.py`
- **test_user.py** (11 connections) — `server/tests/unit/models/test_user.py`
- **set_auth_epoch()** (10 connections) — `server/auth/token_epoch.py`
- **test_endpoints_login_profession.py** (10 connections) — `server/tests/unit/auth/test_endpoints_login_profession.py`
- *... and 283 more nodes in this community*

## Relationships

- [services inventory mutation](services_inventory_mutation.md) (54 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (45 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (43 shared connections)
- [Exception Containers](Exception_Containers.md) (37 shared connections)
- [NPC Combat](NPC_Combat.md) (32 shared connections)
- [maps handle ascii](maps_handle_ascii.md) (28 shared connections)
- [Player Stats](Player_Stats.md) (22 shared connections)
- [player preferences service](player_preferences_service.md) (17 shared connections)
- [metrics schemas rationale](metrics_schemas_rationale.md) (15 shared connections)
- [feature services flag](feature_services_flag.md) (14 shared connections)
- [player room realtime](player_room_realtime.md) (13 shared connections)
- [combat npc service](combat_npc_service.md) (10 shared connections)

## Source Files

- `scripts/run_test_ci.py`
- `server/app/factory.py`
- `server/auth/endpoints.py`
- `server/auth/invites.py`
- `server/auth/jwt_strategy.py`
- `server/auth/token_epoch.py`
- `server/auth/users.py`
- `server/models/invite.py`
- `server/models/user.py`
- `server/schemas/auth/invite.py`
- `server/tests/integration/test_db_connectivity.py`
- `server/tests/integration/test_procedures_return_shape.py`
- `server/tests/unit/api/test_character_creation.py`
- `server/tests/unit/auth/conftest.py`
- `server/tests/unit/auth/test_endpoints_invites.py`
- `server/tests/unit/auth/test_endpoints_login.py`
- `server/tests/unit/auth/test_endpoints_login_profession.py`
- `server/tests/unit/auth/test_endpoints_register.py`
- `server/tests/unit/auth/test_invite_manager.py`
- `server/tests/unit/auth/test_jwt_strategy.py`

## Audit Trail

- EXTRACTED: 1430 (86%)
- INFERRED: 236 (14%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*