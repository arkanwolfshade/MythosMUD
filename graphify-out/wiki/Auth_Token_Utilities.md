# Auth Token Utilities

> 107 nodes

## Key Concepts

- **AuthenticationError** (64 connections) — `server/exceptions.py`
- **test_auth_utils.py** (52 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **AttributeError** (38 connections)
- **create_access_token()** (30 connections) — `server/auth_utils.py`
- **decode_access_token()** (25 connections) — `server/auth_utils.py`
- **hash_password()** (18 connections) — `server/auth_utils.py`
- **auth_utils.py** (16 connections) — `server/auth_utils.py`
- **verify_password()** (9 connections) — `server/auth_utils.py`
- **test_create_access_token_attribute_error()** (5 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_attribute_error()** (5 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_verify_password_success()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_verify_password_failure()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_hash_password_raises_on_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_success()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_expired()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_with_custom_secret()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_with_none_secret()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_none_secret()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_wrong_secret()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_jwt_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_value_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_value_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_type_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_runtime_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_hash_password_authentication_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- *... and 82 more nodes in this community*

## Relationships

- [Standardized Error Responses](Standardized_Error_Responses.md) (27 shared connections)
- [Realtime Conftest Mocks](Realtime_Conftest_Mocks.md) (15 shared connections)
- [Schemas Maps Map](Schemas_Maps_Map.md) (7 shared connections)
- [Client Memory Leak Detector](Client_Memory_Leak_Detector.md) (4 shared connections)
- [Container Data Models](Container_Data_Models.md) (3 shared connections)
- [Holiday Persistence Models](Holiday_Persistence_Models.md) (3 shared connections)
- [Client Event Store](Client_Event_Store.md) (2 shared connections)
- [Room Occupant Events](Room_Occupant_Events.md) (2 shared connections)
- [Mythos Time HUD](Mythos_Time_HUD.md) (2 shared connections)
- [Combat Turn Processor](Combat_Turn_Processor.md) (2 shared connections)
- [Status Command Handlers](Status_Command_Handlers.md) (2 shared connections)
- [Distributed Event Bus](Distributed_Event_Bus.md) (2 shared connections)

## Source Files

- `server/auth_utils.py`
- `server/exceptions.py`
- `server/tests/unit/auth/test_auth_utils.py`
- `server/tests/unit/services/test_npc_instance_service.py`

## Audit Trail

- EXTRACTED: 376 (79%)
- INFERRED: 99 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*