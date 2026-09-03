# Container Exception Handling

> 401 nodes

## Key Concepts

- **pytest.md** (543 connections) — `.claude/rules/pytest.md`
- **User** (217 connections) — `server/models/user.py`
- **fastapi.md** (91 connections) — `.claude/rules/fastapi.md`
- **models/user.py** (67 connections) — `server/models/user.py`
- **login_user()** (35 connections) — `server/auth/endpoints.py`
- **api/game.py** (29 connections) — `server/api/game.py`
- **handle_transfer_items_exceptions()** (28 connections) — `server/api/container_exception_handlers.py`
- **test_container_exception_handlers.py** (28 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- **test_command_factories_player_state.py** (28 connections) — `server/tests/unit/utils/test_command_factories_player_state.py`
- **handle_open_container_exceptions()** (23 connections) — `server/api/container_exception_handlers.py`
- **LoginRequest** (22 connections) — `server/auth/endpoints.py`
- **container_exception_handlers.py** (22 connections) — `server/api/container_exception_handlers.py`
- **handle_close_container_exceptions()** (21 connections) — `server/api/container_exception_handlers.py`
- **test_game.py** (21 connections) — `server/tests/unit/api/test_game.py`
- **handle_loot_all_exceptions()** (20 connections) — `server/api/container_exception_handlers.py`
- **test_endpoints_login.py** (20 connections) — `server/tests/unit/auth/test_endpoints_login.py`
- **skills.py** (19 connections) — `server/api/skills.py`
- **create_error_context()** (17 connections) — `server/api/container_helpers.py`
- **api/conftest.py** (16 connections) — `server/tests/unit/api/conftest.py`
- **test_skills.py** (16 connections) — `server/tests/unit/api/test_skills.py`
- **get_mythos_time()** (15 connections) — `server/api/game.py`
- **test_main.py** (15 connections) — `server/tests/unit/test_main.py`
- **broadcast_message()** (14 connections) — `server/api/game.py`
- **test_users_current_user_logging.py** (13 connections) — `server/tests/unit/auth/test_users_current_user_logging.py`
- **TestHandleTransferItemsExceptions** (12 connections) — `server/tests/unit/api/test_container_exception_handlers.py`
- *... and 376 more nodes in this community*

## Relationships

- [Container/Inventory Helpers](Container-Inventory_Helpers.md) (62 shared connections)
- [Test Auth Dependencies](Test_Auth_Dependencies.md) (51 shared connections)
- [Character Creation API](Character_Creation_API.md) (43 shared connections)
- [Npc Admin](Npc_Admin.md) (41 shared connections)
- [Container Service Helpers](Container_Service_Helpers.md) (39 shared connections)
- [Error Handling & Exceptions](Error_Handling_&_Exceptions.md) (27 shared connections)
- [Test Command Factories Player State](Test_Command_Factories_Player_State.md) (23 shared connections)
- [Test Users](Test_Users.md) (22 shared connections)
- [Player Model & Migrations](Player_Model_&_Migrations.md) (21 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (21 shared connections)
- [Metrics](Metrics.md) (19 shared connections)
- [NPC Definitions API](NPC_Definitions_API.md) (18 shared connections)

## Source Files

- `.claude/rules/fastapi.md`
- `.claude/rules/pytest.md`
- `server/api/container_exception_handlers.py`
- `server/api/container_helpers.py`
- `server/api/game.py`
- `server/api/player_helpers.py`
- `server/api/skills.py`
- `server/auth/endpoints.py`
- `server/auth/users.py`
- `server/models/user.py`
- `server/schemas/game/__init__.py`
- `server/schemas/game/game.py`
- `server/schemas/players/skill.py`
- `server/tests/integration/test_db_connectivity.py`
- `server/tests/integration/test_quest_flow.py`
- `server/tests/unit/api/conftest.py`
- `server/tests/unit/api/test_container_endpoints_loot_register.py`
- `server/tests/unit/api/test_container_exception_handlers.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_containers.py`

## Audit Trail

- EXTRACTED: 1587 (92%)
- INFERRED: 141 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*