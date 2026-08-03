# player requests schemas

> 126 nodes

## Key Concepts

- **endpoints.py** (61 connections) — `server/auth/endpoints.py`
- **Invite** (48 connections) — `server/models/invite.py`
- **InviteManager** (38 connections) — `server/auth/invites.py`
- **test_invite_manager.py** (21 connections) — `server/tests/unit/auth/test_invite_manager.py`
- **dependencies.py** (18 connections) — `server/auth/dependencies.py`
- **invites.py** (17 connections) — `server/auth/invites.py`
- **test_invite.py** (17 connections) — `server/tests/unit/models/test_invite.py`
- **InviteRead** (15 connections) — `server/schemas/auth/invite.py`
- **test_endpoints_invites.py** (14 connections) — `server/tests/unit/auth/test_endpoints_invites.py`
- **list_invites()** (13 connections) — `server/auth/endpoints.py`
- **get_current_superuser()** (12 connections) — `server/auth/dependencies.py`
- **invite.py** (12 connections) — `server/models/invite.py`
- **require_invite_code()** (11 connections) — `server/auth/dependencies.py`
- **create_invite()** (11 connections) — `server/auth/endpoints.py`
- **get_invite_manager()** (11 connections) — `server/auth/invites.py`
- **get_current_user_info()** (8 connections) — `server/auth/endpoints.py`
- **__init__.py** (7 connections) — `server/auth/__init__.py`
- **_validate_invite_code()** (7 connections) — `server/auth/endpoints.py`
- **CurrentUserInfo** (6 connections) — `server/auth/endpoints.py`
- **_mark_invite_as_used()** (6 connections) — `server/auth/endpoints.py`
- **.validate_invite()** (6 connections) — `server/auth/invites.py`
- **.create_invite()** (6 connections) — `server/models/invite.py`
- **._generate_invite_code()** (6 connections) — `server/models/invite.py`
- **.use_invite()** (5 connections) — `server/auth/invites.py`
- **test_list_invites()** (5 connections) — `server/tests/unit/auth/test_endpoints_invites.py`
- *... and 101 more nodes in this community*

## Relationships

- [Exception Containers](Exception_Containers.md) (27 shared connections)
- [ascii map renderer](ascii_map_renderer.md) (25 shared connections)
- [useWebSocketConnectionTestFixtures useWe](useWebSocketConnectionTestFixtures_useWe.md) (14 shared connections)
- [player service game](player_service_game.md) (11 shared connections)
- [admin auth service](admin_auth_service.md) (8 shared connections)
- [auth users rationale](auth_users_rationale.md) (7 shared connections)
- [models npc rationale](models_npc_rationale.md) (7 shared connections)
- [command factories moderation](command_factories_moderation.md) (6 shared connections)
- [world models rationale](world_models_rationale.md) (5 shared connections)
- [command inventory factories](command_inventory_factories.md) (4 shared connections)
- [combat npc services](combat_npc_services.md) (4 shared connections)
- [game models enums](game_models_enums.md) (3 shared connections)

## Source Files

- `server/auth/__init__.py`
- `server/auth/dependencies.py`
- `server/auth/endpoints.py`
- `server/auth/invites.py`
- `server/models/invite.py`
- `server/schemas/auth/invite.py`
- `server/tests/unit/auth/test_endpoints_invites.py`
- `server/tests/unit/auth/test_invite_manager.py`
- `server/tests/unit/models/test_invite.py`

## Audit Trail

- EXTRACTED: 535 (93%)
- INFERRED: 41 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*