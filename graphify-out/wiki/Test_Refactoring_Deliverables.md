# Test Refactoring Deliverables

> 25 nodes

## Key Concepts

- **test_professions_endpoints.py** (13 connections) — `server/tests/unit/api/test_professions_endpoints.py`
- **get_all_professions()** (10 connections) — `server/api/professions.py`
- **get_profession_by_id()** (10 connections) — `server/api/professions.py`
- **profession.py** (7 connections) — `server/schemas/players/profession.py`
- **ProfessionListResponse** (7 connections) — `server/schemas/players/profession.py`
- **ProfessionResponse** (7 connections) — `server/schemas/players/profession.py`
- **BaseModel** (5 connections)
- **StatRequirement** (4 connections) — `server/schemas/players/profession.py`
- **MechanicalEffect** (4 connections) — `server/schemas/players/profession.py`
- **ProfessionData** (4 connections) — `server/schemas/players/profession.py`
- **_user()** (4 connections) — `server/tests/unit/api/test_professions_endpoints.py`
- **test_get_all_professions_requires_auth()** (4 connections) — `server/tests/unit/api/test_professions_endpoints.py`
- **test_get_profession_by_id_not_found()** (4 connections) — `server/tests/unit/api/test_professions_endpoints.py`
- **test_get_all_professions_success()** (3 connections) — `server/tests/unit/api/test_professions_endpoints.py`
- **test_get_profession_by_id_success()** (3 connections) — `server/tests/unit/api/test_professions_endpoints.py`
- **Request** (2 connections)
- **Retrieve all available professions for character creation with caching.      :pa** (1 connections) — `server/api/professions.py`
- **Retrieve specific profession details by ID with caching.      :param profession_** (1 connections) — `server/api/professions.py`
- **Profession API response schemas for MythosMUD server.  This module provides Pyda** (1 connections) — `server/schemas/players/profession.py`
- **Stat requirement for a profession.** (1 connections) — `server/schemas/players/profession.py`
- **Mechanical effect of a profession.** (1 connections) — `server/schemas/players/profession.py`
- **Profession data model.** (1 connections) — `server/schemas/players/profession.py`
- **Response model for listing all professions.** (1 connections) — `server/schemas/players/profession.py`
- **Response model for a single profession.** (1 connections) — `server/schemas/players/profession.py`
- **Unit tests for server.api.professions.** (1 connections) — `server/tests/unit/api/test_professions_endpoints.py`

## Relationships

- [Room Occupancy Class](Room_Occupancy_Class.md) (10 shared connections)
- [Disconnect Grace Period](Disconnect_Grace_Period.md) (6 shared connections)
- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (5 shared connections)
- [Game Mechanics Service](Game_Mechanics_Service.md) (2 shared connections)
- [Game Terminal Panels](Game_Terminal_Panels.md) (2 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (1 shared connections)

## Source Files

- `server/api/professions.py`
- `server/schemas/players/profession.py`
- `server/tests/unit/api/test_professions_endpoints.py`

## Audit Trail

- EXTRACTED: 97 (97%)
- INFERRED: 3 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*