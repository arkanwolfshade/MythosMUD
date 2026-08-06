# invite models rationale

> 27 nodes

## Key Concepts

- **professions.py** (19 connections) — `server/api/professions.py`
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
- **Profession management API endpoints for MythosMUD server.  This module handles a** (1 connections) — `server/api/professions.py`
- **Retrieve all available professions for character creation with caching.      :pa** (1 connections) — `server/api/professions.py`
- **Retrieve specific profession details by ID with caching.      :param profession_** (1 connections) — `server/api/professions.py`
- **Profession API response schemas for MythosMUD server.  This module provides Pyda** (1 connections) — `server/schemas/players/profession.py`
- **Stat requirement for a profession.** (1 connections) — `server/schemas/players/profession.py`
- **Mechanical effect of a profession.** (1 connections) — `server/schemas/players/profession.py`
- **Profession data model.** (1 connections) — `server/schemas/players/profession.py`
- **Response model for listing all professions.** (1 connections) — `server/schemas/players/profession.py`
- *... and 2 more nodes in this community*

## Relationships

- [services inventory mutation](services_inventory_mutation.md) (6 shared connections)
- [player requests schemas](player_requests_schemas.md) (6 shared connections)
- [commands admin helpers](commands_admin_helpers.md) (6 shared connections)
- [persistence container rationale](persistence_container_rationale.md) (4 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (3 shared connections)
- [combat npc service](combat_npc_service.md) (3 shared connections)
- [logging examples fastapi](logging_examples_fastapi.md) (2 shared connections)
- [websocket handler realtime](websocket_handler_realtime.md) (1 shared connections)
- [NPC Definitions Admin](NPC_Definitions_Admin.md) (1 shared connections)
- [handler realtime nats](handler_realtime_nats.md) (1 shared connections)
- [websocket helpers realtime](websocket_helpers_realtime.md) (1 shared connections)

## Source Files

- `server/api/professions.py`
- `server/schemas/players/profession.py`
- `server/tests/unit/api/test_professions_endpoints.py`

## Audit Trail

- EXTRACTED: 117 (98%)
- INFERRED: 3 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*