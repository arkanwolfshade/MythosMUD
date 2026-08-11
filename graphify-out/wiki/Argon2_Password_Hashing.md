# Argon2 Password Hashing

> 131 nodes

## Key Concepts

- **RateLimitError** (76 connections) — `server/exceptions.py`
- **TransferContainerRequest** (57 connections) — `server/api/container_models.py`
- **container_helpers.py** (44 connections) — `server/api/container_helpers.py`
- **test_container_helpers.py** (43 connections) — `server/tests/unit/api/test_container_helpers.py`
- **get_player_id_from_user()** (19 connections) — `server/api/container_helpers.py`
- **handle_container_service_error()** (19 connections) — `server/api/container_helpers.py`
- **create_error_context()** (17 connections) — `server/api/container_helpers.py`
- **TestHandleContainerServiceError** (13 connections) — `server/tests/unit/api/test_container_helpers.py`
- **execute_transfer()** (12 connections) — `server/api/container_helpers.py`
- **container_models.py** (12 connections) — `server/api/container_models.py`
- **TestCreateErrorContext** (12 connections) — `server/tests/unit/api/test_container_helpers.py`
- **Request** (11 connections)
- **TestGetPlayerIdFromUser** (11 connections) — `server/tests/unit/api/test_container_helpers.py`
- **TestValidateUserForOpenContainer** (11 connections) — `server/tests/unit/api/test_container_helpers.py`
- **TestApplyRateLimitingForOpenContainer** (11 connections) — `server/tests/unit/api/test_container_helpers.py`
- **TestValidateUserForTransfer** (11 connections) — `server/tests/unit/api/test_container_helpers.py`
- **TestApplyRateLimitingForTransfer** (11 connections) — `server/tests/unit/api/test_container_helpers.py`
- **TestExecuteTransfer** (11 connections) — `server/tests/unit/api/test_container_helpers.py`
- **TestValidateUserForCloseContainer** (11 connections) — `server/tests/unit/api/test_container_helpers.py`
- **TestApplyRateLimitingForCloseContainer** (11 connections) — `server/tests/unit/api/test_container_helpers.py`
- **TestValidateUserForLootAll** (11 connections) — `server/tests/unit/api/test_container_helpers.py`
- **TestApplyRateLimitingForLootAll** (11 connections) — `server/tests/unit/api/test_container_helpers.py`
- **validate_user_for_open_container()** (10 connections) — `server/api/container_helpers.py`
- **apply_rate_limiting_for_open_container()** (10 connections) — `server/api/container_helpers.py`
- **validate_user_for_transfer()** (10 connections) — `server/api/container_helpers.py`
- *... and 106 more nodes in this community*

## Relationships

- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (99 shared connections)
- [Combat Player Broadcasts](Combat_Player_Broadcasts.md) (33 shared connections)
- [Realtime Service Bundle](Realtime_Service_Bundle.md) (29 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (27 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (26 shared connections)
- [Container API Endpoints](Container_API_Endpoints.md) (18 shared connections)
- [Player Effects API](Player_Effects_API.md) (18 shared connections)
- [Database Manager Tests](Database_Manager_Tests.md) (11 shared connections)
- [Container Exception Handlers](Container_Exception_Handlers.md) (8 shared connections)
- [Game Mechanics Service](Game_Mechanics_Service.md) (7 shared connections)
- [Container Component Capacity](Container_Component_Capacity.md) (5 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (4 shared connections)

## Source Files

- `server/api/container_helpers.py`
- `server/api/container_models.py`
- `server/exceptions.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_containers.py`
- `server/utils/rate_limiter.py`

## Audit Trail

- EXTRACTED: 569 (77%)
- INFERRED: 173 (23%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*