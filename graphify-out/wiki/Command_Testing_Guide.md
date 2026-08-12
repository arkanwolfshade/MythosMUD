# Command Testing Guide

> 32 nodes

## Key Concepts

- **hash_password()** (28 connections) — `server/auth/argon2_utils.py`
- **argon2_utils.py** (19 connections) — `server/auth/argon2_utils.py`
- **auth_utils.py** (16 connections) — `server/auth_utils.py`
- **seed_e2e_users.py** (9 connections) — `scripts/seed_e2e_users.py`
- **_ensure_player_for_user()** (5 connections) — `scripts/seed_e2e_users.py`
- **_seed_e2e_users()** (4 connections) — `scripts/seed_e2e_users.py`
- **_validate_password_for_hashing()** (4 connections) — `server/auth/argon2_utils.py`
- **test_hash_password_empty_string()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_verify_password_empty_string()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_hash_password_invalid_type()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_hash_password_non_string_type()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_hash_password_hashing_error()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_hash_password_type_error()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **main()** (3 connections) — `scripts/seed_e2e_users.py`
- **._hash_password()** (3 connections) — `server/auth/users.py`
- **E2eUserSpec** (2 connections) — `scripts/seed_e2e_users.py`
- **UUID** (2 connections)
- **datetime** (2 connections)
- **Connection** (1 connections)
- **One row in users plus optional default character for login E2E.** (1 connections) — `scripts/seed_e2e_users.py`
- **Entry point: run E2E user seed via anyio.** (1 connections) — `scripts/seed_e2e_users.py`
- **Argon2 password hashing utilities for MythosMUD.  This module implements the gol** (1 connections) — `server/auth/argon2_utils.py`
- **Validate password input before Argon2 hashing.** (1 connections) — `server/auth/argon2_utils.py`
- **Hash a plaintext password using Argon2id.      This function provides superior s** (1 connections) — `server/auth/argon2_utils.py`
- **Hash password using Argon2 instead of bcrypt.** (1 connections) — `server/auth/users.py`
- *... and 7 more nodes in this community*

## Relationships

- [Combat Command Models](Combat_Command_Models.md) (22 shared connections)
- [Standardized Error Responses](Standardized_Error_Responses.md) (12 shared connections)
- [Client Event Store](Client_Event_Store.md) (4 shared connections)
- [Optimization Archive Modernization](Optimization_Archive_Modernization.md) (3 shared connections)
- [Integer Coercion Utils](Integer_Coercion_Utils.md) (3 shared connections)
- [Auth Token Utilities](Auth_Token_Utilities.md) (3 shared connections)
- [Realtime Conftest Mocks](Realtime_Conftest_Mocks.md) (2 shared connections)
- [Room Occupancy Class](Room_Occupancy_Class.md) (2 shared connections)
- [NPC Combat Lifecycle](NPC_Combat_Lifecycle.md) (2 shared connections)
- [Enhanced Logging Exceptions](Enhanced_Logging_Exceptions.md) (1 shared connections)
- [Package Engines Node](Package_Engines_Node.md) (1 shared connections)
- [Combat Command Handler](Combat_Command_Handler.md) (1 shared connections)

## Source Files

- `scripts/seed_e2e_users.py`
- `server/auth/argon2_utils.py`
- `server/auth/users.py`
- `server/auth_utils.py`
- `server/tests/unit/auth/test_argon2_utils.py`

## Audit Trail

- EXTRACTED: 126 (93%)
- INFERRED: 9 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*