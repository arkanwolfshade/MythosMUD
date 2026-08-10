# Argon2 Password Hashing

> 83 nodes

## Key Concepts

- **TransferContainerRequest** (57 connections) — `server/api/container_models.py`
- **test_container_helpers.py** (43 connections) — `server/tests/unit/api/test_container_helpers.py`
- **TestHandleContainerServiceError** (13 connections) — `server/tests/unit/api/test_container_helpers.py`
- **execute_transfer()** (12 connections) — `server/api/container_helpers.py`
- **TestCreateErrorContext** (12 connections) — `server/tests/unit/api/test_container_helpers.py`
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
- **TestGetContainerService** (10 connections) — `server/tests/unit/api/test_container_helpers.py`
- **.test_handle_container_service_error_with_request_data()** (6 connections) — `server/tests/unit/api/test_container_helpers.py`
- **.test_apply_rate_limiting_for_open_container_exceeded()** (5 connections) — `server/tests/unit/api/test_container_helpers.py`
- **.test_apply_rate_limiting_for_transfer_exceeded()** (5 connections) — `server/tests/unit/api/test_container_helpers.py`
- **.test_execute_transfer_to_container()** (5 connections) — `server/tests/unit/api/test_container_helpers.py`
- **.test_execute_transfer_to_player()** (5 connections) — `server/tests/unit/api/test_container_helpers.py`
- **.test_handle_container_service_error_stale_token()** (5 connections) — `server/tests/unit/api/test_container_helpers.py`
- **.test_handle_container_service_error_invalid_stack()** (5 connections) — `server/tests/unit/api/test_container_helpers.py`
- **.test_handle_container_service_error_generic()** (5 connections) — `server/tests/unit/api/test_container_helpers.py`
- **.test_apply_rate_limiting_for_close_container_exceeded()** (5 connections) — `server/tests/unit/api/test_container_helpers.py`
- *... and 58 more nodes in this community*

## Relationships

- [Aggressive Mob NPC](Aggressive_Mob_NPC.md) (129 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (32 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (15 shared connections)
- [Product Requirements Document](Product_Requirements_Document.md) (9 shared connections)
- [Game Service Bundle](Game_Service_Bundle.md) (2 shared connections)
- [Chat Service Whispers](Chat_Service_Whispers.md) (1 shared connections)
- [Room Service Tests](Room_Service_Tests.md) (1 shared connections)

## Source Files

- `server/api/container_helpers.py`
- `server/api/container_models.py`
- `server/tests/unit/api/test_container_helpers.py`
- `server/tests/unit/api/test_containers.py`

## Audit Trail

- EXTRACTED: 267 (68%)
- INFERRED: 124 (32%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*