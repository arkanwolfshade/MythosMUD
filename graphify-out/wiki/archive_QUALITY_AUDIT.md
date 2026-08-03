# archive QUALITY AUDIT

> 6 nodes

## Key Concepts

- **get_hash_info()** (6 connections) — `server/auth/argon2_utils.py`
- **test_get_hash_info_valid()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_get_hash_info_invalid()** (3 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **Extract parameters from an Argon2 hash string.** (1 connections) — `server/auth/argon2_utils.py`
- **Test get_hash_info with valid Argon2 hash.** (1 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **Test get_hash_info with invalid hash returns None.** (1 connections) — `server/tests/unit/auth/test_argon2_utils.py`

## Relationships

- [respawn player handlers](respawn_player_handlers.md) (3 shared connections)
- [models npc rationale](models_npc_rationale.md) (1 shared connections)
- [persistence constants rationale](persistence_constants_rationale.md) (1 shared connections)
- [auth users rationale](auth_users_rationale.md) (1 shared connections)

## Source Files

- `server/auth/argon2_utils.py`
- `server/tests/unit/auth/test_argon2_utils.py`

## Audit Trail

- EXTRACTED: 16 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*