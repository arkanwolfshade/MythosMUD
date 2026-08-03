# logging file setup

> 51 nodes

## Key Concepts

- **user.py** (62 connections) — `server/models/user.py`
- **professions.py** (19 connections) — `server/api/professions.py`
- **test_professions_endpoints.py** (13 connections) — `server/tests/unit/api/test_professions_endpoints.py`
- **test_users_current_user_logging.py** (12 connections) — `server/tests/unit/auth/test_users_current_user_logging.py`
- **get_current_user_with_logging()** (11 connections) — `server/auth/users.py`
- **get_all_professions()** (10 connections) — `server/api/professions.py`
- **get_profession_by_id()** (10 connections) — `server/api/professions.py`
- **profession.py** (7 connections) — `server/schemas/players/profession.py`
- **ProfessionListResponse** (7 connections) — `server/schemas/players/profession.py`
- **ProfessionResponse** (7 connections) — `server/schemas/players/profession.py`
- **BaseModel** (5 connections)
- **set_display_name_default()** (4 connections) — `server/models/user.py`
- **StatRequirement** (4 connections) — `server/schemas/players/profession.py`
- **MechanicalEffect** (4 connections) — `server/schemas/players/profession.py`
- **ProfessionData** (4 connections) — `server/schemas/players/profession.py`
- **_user()** (4 connections) — `server/tests/unit/api/test_professions_endpoints.py`
- **test_get_all_professions_requires_auth()** (4 connections) — `server/tests/unit/api/test_professions_endpoints.py`
- **test_get_profession_by_id_not_found()** (4 connections) — `server/tests/unit/api/test_professions_endpoints.py`
- **test_get_current_user_with_logging_success()** (4 connections) — `server/tests/unit/auth/test_users_current_user_logging.py`
- **test_get_current_user_with_logging_no_request()** (4 connections) — `server/tests/unit/auth/test_users_current_user_logging.py`
- **test_get_current_user_with_logging_long_auth_header()** (4 connections) — `server/tests/unit/auth/test_users_current_user_logging.py`
- **test_get_current_user_with_logging_no_auth_header()** (4 connections) — `server/tests/unit/auth/test_users_current_user_logging.py`
- **test_get_all_professions_success()** (3 connections) — `server/tests/unit/api/test_professions_endpoints.py`
- **test_get_profession_by_id_success()** (3 connections) — `server/tests/unit/api/test_professions_endpoints.py`
- **test_get_current_user_with_logging_no_user()** (3 connections) — `server/tests/unit/auth/test_users_current_user_logging.py`
- *... and 26 more nodes in this community*

## Relationships

- [ascii map renderer](ascii_map_renderer.md) (18 shared connections)
- [auth users rationale](auth_users_rationale.md) (9 shared connections)
- [Exception Containers](Exception_Containers.md) (9 shared connections)
- [Database Config](Database_Config.md) (8 shared connections)
- [admin auth service](admin_auth_service.md) (8 shared connections)
- [game models stats](game_models_stats.md) (7 shared connections)
- [command inventory factories](command_inventory_factories.md) (5 shared connections)
- [profession game service](profession_game_service.md) (4 shared connections)
- [world models rationale](world_models_rationale.md) (4 shared connections)
- [Loot Generation](Loot_Generation.md) (3 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (2 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (2 shared connections)

## Source Files

- `server/api/professions.py`
- `server/auth/users.py`
- `server/models/user.py`
- `server/schemas/players/profession.py`
- `server/tests/unit/api/test_professions_endpoints.py`
- `server/tests/unit/auth/test_users_current_user_logging.py`

## Audit Trail

- EXTRACTED: 244 (99%)
- INFERRED: 3 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*