# Combat Command Handler

> 237 nodes

## Key Concepts

- **test_users.py** (60 connections) — `server/tests/unit/auth/test_users.py`
- **user.py** (56 connections) — `server/models/user.py`
- **UserManager** (47 connections) — `server/auth/users.py`
- **users.py** (46 connections) — `server/auth/users.py`
- **factory.py** (37 connections) — `server/app/factory.py`
- **game.py** (25 connections) — `server/api/game.py`
- **test_auth_dependencies.py** (24 connections) — `server/tests/unit/auth/test_auth_dependencies.py`
- **professions.py** (19 connections) — `server/api/professions.py`
- **skills.py** (18 connections) — `server/api/skills.py`
- **dependencies.py** (18 connections) — `server/auth/dependencies.py`
- **test_professions_endpoints.py** (13 connections) — `server/tests/unit/api/test_professions_endpoints.py`
- **get_auth_backend()** (12 connections) — `server/auth/users.py`
- **require_invite_code()** (11 connections) — `server/auth/dependencies.py`
- **UsernameAuthenticationBackend** (11 connections) — `server/auth/users.py`
- **get_current_user_with_logging()** (11 connections) — `server/auth/users.py`
- **__init__.py** (10 connections) — `server/api/__init__.py`
- **get_all_professions()** (10 connections) — `server/api/professions.py`
- **get_profession_by_id()** (10 connections) — `server/api/professions.py`
- **get_current_superuser()** (10 connections) — `server/auth/dependencies.py`
- **email_utils.py** (9 connections) — `server/auth/email_utils.py`
- **get_username_auth_backend()** (9 connections) — `server/auth/users.py`
- **get_current_verified_user()** (8 connections) — `server/auth/dependencies.py`
- **get_user_manager()** (8 connections) — `server/auth/users.py`
- **__init__.py** (7 connections) — `server/auth/__init__.py`
- **get_user_db()** (7 connections) — `server/auth/users.py`
- *... and 212 more nodes in this community*

## Relationships

- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (72 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (23 shared connections)
- [Client Event Store](Client_Event_Store.md) (20 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (15 shared connections)
- [Chat Panel Filtering](Chat_Panel_Filtering.md) (9 shared connections)
- [Dead Code Cleanup Plan](Dead_Code_Cleanup_Plan.md) (8 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (7 shared connections)
- [test_parse_exits_json_other_type](test_parse_exits_json_other_type.md) (7 shared connections)
- [Game Mechanics Service](Game_Mechanics_Service.md) (6 shared connections)
- [Disconnect Grace Period](Disconnect_Grace_Period.md) (6 shared connections)
- [Cursor Skills Frontend](Cursor_Skills_Frontend.md) (5 shared connections)
- [Realtime Conftest Mocks](Realtime_Conftest_Mocks.md) (5 shared connections)

## Source Files

- `server/api/__init__.py`
- `server/api/admin/__init__.py`
- `server/api/containers.py`
- `server/api/game.py`
- `server/api/professions.py`
- `server/api/skills.py`
- `server/app/factory.py`
- `server/auth/__init__.py`
- `server/auth/dependencies.py`
- `server/auth/email_utils.py`
- `server/auth/users.py`
- `server/models/user.py`
- `server/tests/unit/api/test_professions_endpoints.py`
- `server/tests/unit/auth/test_auth_dependencies.py`
- `server/tests/unit/auth/test_users.py`

## Audit Trail

- EXTRACTED: 931 (97%)
- INFERRED: 26 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*