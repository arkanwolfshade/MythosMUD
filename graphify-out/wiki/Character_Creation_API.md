# Character Creation API

> 191 nodes

## Key Concepts

- **api/character_creation.py** (67 connections) — `server/api/character_creation.py`
- **factory.py** (54 connections) — `server/app/factory.py`
- **users.py** (48 connections) — `server/auth/users.py`
- **players/__init__.py** (48 connections) — `server/schemas/players/__init__.py`
- **roll_character_stats()** (26 connections) — `server/api/character_creation.py`
- **CreateCharacterRequest** (24 connections) — `server/schemas/players/player_requests.py`
- **test_character_creation.py** (24 connections) — `server/tests/unit/api/test_character_creation.py`
- **create_character_with_stats()** (23 connections) — `server/api/character_creation.py`
- **RollStatsRequest** (22 connections) — `server/schemas/players/player_requests.py`
- **ProfessionService** (21 connections) — `server/game/profession_service.py`
- **professions.py** (21 connections) — `server/api/professions.py`
- **validate_character_stats()** (15 connections) — `server/api/character_creation.py`
- **test_professions_endpoints.py** (15 connections) — `server/tests/unit/api/test_professions_endpoints.py`
- **asyncio** (14 connections)
- **_execute_create_character()** (13 connections) — `server/api/character_creation.py`
- **RollStatsResponse** (12 connections) — `server/schemas/players/character_creation.py`
- **TestRollCharacterStats** (12 connections) — `server/tests/unit/api/test_character_creation.py`
- **_roll_stats_with_profession_preview()** (12 connections) — `server/api/character_creation.py`
- **_convert_stat_summary_to_stat_summary_model()** (11 connections) — `server/api/character_creation.py`
- **get_all_professions()** (11 connections) — `server/api/professions.py`
- **get_profession_by_id()** (11 connections) — `server/api/professions.py`
- **server/api/__init__.py** (11 connections) — `server/api/__init__.py`
- **players/character_creation.py** (11 connections) — `server/schemas/players/character_creation.py`
- **_dispatch_roll_stats()** (10 connections) — `server/api/character_creation.py`
- **CreateCharacterResponse** (9 connections) — `server/schemas/players/character_creation.py`
- *... and 166 more nodes in this community*

## Relationships

- [Container Exception Handling](Container_Exception_Handling.md) (43 shared connections)
- [Test Auth Dependencies](Test_Auth_Dependencies.md) (27 shared connections)
- [Dependency Injection (FastAPI)](Dependency_Injection_FastAPI.md) (19 shared connections)
- [Test Player Schemas](Test_Player_Schemas.md) (17 shared connections)
- [Memory Monitor & Health Alerts](Memory_Monitor_&_Health_Alerts.md) (15 shared connections)
- [Npc Admin](Npc_Admin.md) (14 shared connections)
- [NPC Definitions API](NPC_Definitions_API.md) (13 shared connections)
- [Test Player Requests](Test_Player_Requests.md) (12 shared connections)
- [Stats Generator](Stats_Generator.md) (11 shared connections)
- [Test Users](Test_Users.md) (11 shared connections)
- [Container/Inventory Helpers](Container-Inventory_Helpers.md) (10 shared connections)
- [Error Handling & Exceptions](Error_Handling_&_Exceptions.md) (8 shared connections)

## Source Files

- `server/api/__init__.py`
- `server/api/character_creation.py`
- `server/api/containers.py`
- `server/api/player_router.py`
- `server/api/professions.py`
- `server/app/factory.py`
- `server/auth/users.py`
- `server/game/profession_service.py`
- `server/schemas/players/__init__.py`
- `server/schemas/players/character_creation.py`
- `server/schemas/players/player_effects.py`
- `server/schemas/players/player_requests.py`
- `server/schemas/players/profession.py`
- `server/schemas/players/stat_values.py`
- `server/tests/unit/api/test_character_creation.py`
- `server/tests/unit/api/test_professions_endpoints.py`

## Audit Trail

- EXTRACTED: 639 (97%)
- INFERRED: 22 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*