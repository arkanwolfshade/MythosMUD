# security headers middleware

> 8 nodes

## Key Concepts

- **needs_rehash()** (7 connections) — `server/auth/argon2_utils.py`
- **test_needs_rehash_valid_hash()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_needs_rehash_error_handling()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_needs_rehash_invalid_hash()** (3 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **Check if a hash needs to be rehashed due to parameter changes.** (1 connections) — `server/auth/argon2_utils.py`
- **Test needs_rehash with valid hash that doesn't need rehashing.** (1 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **Test needs_rehash with invalid hash returns True.** (1 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **Test needs_rehash handles errors and returns True.** (1 connections) — `server/tests/unit/auth/test_argon2_utils.py`

## Relationships

- [respawn player handlers](respawn_player_handlers.md) (4 shared connections)
- [auth users rationale](auth_users_rationale.md) (2 shared connections)
- [models npc rationale](models_npc_rationale.md) (1 shared connections)
- [persistence constants rationale](persistence_constants_rationale.md) (1 shared connections)

## Source Files

- `server/auth/argon2_utils.py`
- `server/tests/unit/auth/test_argon2_utils.py`

## Audit Trail

- EXTRACTED: 22 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*