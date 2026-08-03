# persistence constants rationale

> 10 nodes

## Key Concepts

- **is_argon2_hash()** (9 connections) — `server/auth/argon2_utils.py`
- **test_is_argon2_hash_valid()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_is_argon2_hash_invalid()** (3 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_is_argon2_hash_none()** (3 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_is_argon2_hash_non_string()** (3 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **Check if a given string is an Argon2 hash.** (1 connections) — `server/auth/argon2_utils.py`
- **Test is_argon2_hash with valid Argon2 hash.** (1 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **Test is_argon2_hash with invalid hash.** (1 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **Test is_argon2_hash with None.** (1 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **Test is_argon2_hash with non-string type.** (1 connections) — `server/tests/unit/auth/test_argon2_utils.py`

## Relationships

- [respawn player handlers](respawn_player_handlers.md) (5 shared connections)
- [models npc rationale](models_npc_rationale.md) (1 shared connections)
- [archive QUALITY AUDIT](archive_QUALITY_AUDIT.md) (1 shared connections)
- [security headers middleware](security_headers_middleware.md) (1 shared connections)
- [auth users rationale](auth_users_rationale.md) (1 shared connections)

## Source Files

- `server/auth/argon2_utils.py`
- `server/tests/unit/auth/test_argon2_utils.py`

## Audit Trail

- EXTRACTED: 27 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*