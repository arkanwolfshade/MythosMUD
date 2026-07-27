# Auth Token Utilities

> 87 nodes · cohesion 0.04

## Key Concepts

- **test_auth_utils.py** (52 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **create_access_token()** (30 connections) — `server/auth_utils.py`
- **decode_access_token()** (25 connections) — `server/auth_utils.py`
- **hash_password()** (17 connections) — `server/auth_utils.py`
- **verify_password()** (9 connections) — `server/auth_utils.py`
- **timedelta** (6 connections) — `server/auth_utils.py`
- **test_decode_access_token_attribute_error()** (5 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_expired()** (5 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_runtime_error()** (5 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_with_expired_token_immediately()** (5 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **Test decode_access_token handles ValueError and returns None.** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **Test hash_password raises AuthenticationError on AuthenticationError from argon2** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_attribute_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_runtime_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_with_audience()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_with_custom_expires_delta_zero()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_with_custom_secret()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_create_access_token_with_expires_delta()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_none_secret()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_success()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_type_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_value_error()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_with_custom_algorithm()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_with_wrong_algorithm()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- **test_decode_access_token_wrong_secret()** (4 connections) — `server/tests/unit/auth/test_auth_utils.py`
- *... and 62 more nodes in this community*

## Relationships

- [[NPC Admin API]] (8 shared connections)
- [[Argon2 Password Hashing]] (6 shared connections)
- [[Standardized Error Responses]] (4 shared connections)
- [[Database Manager Tests]] (4 shared connections)
- [[Services Service Room]] (3 shared connections)
- [[Realtime WebSocket Auth]] (3 shared connections)
- [[Room Occupant Events]] (2 shared connections)
- [[Auth Set Secret]] (1 shared connections)
- [[API Test Fixtures]] (1 shared connections)

## Source Files

- `server/auth_utils.py`
- `server/tests/unit/auth/test_argon2_utils.py`
- `server/tests/unit/auth/test_auth_utils.py`

## Audit Trail

- EXTRACTED: 342 (98%)
- INFERRED: 8 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
