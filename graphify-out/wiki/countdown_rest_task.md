# countdown rest task

> 17 nodes

## Key Concepts

- **create_hasher_with_params()** (11 connections) — `server/auth/argon2_utils.py`
- **test_create_hasher_with_params_valid()** (3 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_create_hasher_with_params_invalid_time_cost()** (3 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_create_hasher_with_params_invalid_memory_cost()** (3 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_create_hasher_with_params_invalid_parallelism()** (3 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_create_hasher_with_params_invalid_hash_len()** (3 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_create_hasher_with_params_low_time_cost_warning()** (3 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_create_hasher_with_params_low_memory_cost_warning()** (3 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **PasswordHasher** (1 connections)
- **Create a PasswordHasher with custom parameters.** (1 connections) — `server/auth/argon2_utils.py`
- **Test creating hasher with valid parameters.** (1 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **Test creating hasher with invalid time_cost.** (1 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **Test creating hasher with invalid memory_cost.** (1 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **Test creating hasher with invalid parallelism.** (1 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **Test creating hasher with invalid hash_len.** (1 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **Test that create_hasher_with_params logs warning for low time_cost.** (1 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **Test that create_hasher_with_params logs warning for low memory_cost.** (1 connections) — `server/tests/unit/auth/test_argon2_utils.py`

## Relationships

- [respawn player handlers](respawn_player_handlers.md) (8 shared connections)
- [models npc rationale](models_npc_rationale.md) (1 shared connections)

## Source Files

- `server/auth/argon2_utils.py`
- `server/tests/unit/auth/test_argon2_utils.py`

## Audit Trail

- EXTRACTED: 41 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*