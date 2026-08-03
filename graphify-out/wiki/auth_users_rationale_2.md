# auth users rationale

> 22 nodes

## Key Concepts

- **hash_password()** (27 connections) — `server/auth/argon2_utils.py`
- **test_verify_password_success()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_verify_password_failure()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_hash_password_empty_string()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_verify_password_empty_string()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_hash_password_invalid_type()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_hash_password_non_string_type()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_verify_password_non_string_password()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_hash_password_type_error()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **._hash_password()** (3 connections) — `server/auth/users.py`
- **test_hash_password_success()** (3 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **Hash a plaintext password using Argon2id.      This function provides superior s** (1 connections) — `server/auth/argon2_utils.py`
- **Hash password using Argon2 instead of bcrypt.** (1 connections) — `server/auth/users.py`
- **Test successful password hashing.** (1 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **Test successful password verification.** (1 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **Test password verification with wrong password.** (1 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **Test hashing empty password raises AuthenticationError.** (1 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **Test verifying empty password - cannot hash empty password.** (1 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **Test hashing password with invalid type.** (1 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **Test hashing password with non-string type raises AuthenticationError.** (1 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **Test verifying password with non-string password returns False.** (1 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **Test hash_password handles TypeError.** (1 connections) — `server/tests/unit/auth/test_argon2_utils.py`

## Relationships

- [respawn player handlers](respawn_player_handlers.md) (11 shared connections)
- [Error Handling Core](Error_Handling_Core.md) (6 shared connections)
- [models npc rationale](models_npc_rationale.md) (5 shared connections)
- [argon2 auth rationale](argon2_auth_rationale.md) (2 shared connections)
- [security headers middleware](security_headers_middleware.md) (2 shared connections)
- [Database Config](Database_Config.md) (1 shared connections)
- [player requests schemas](player_requests_schemas.md) (1 shared connections)
- [player service game](player_service_game.md) (1 shared connections)
- [admin auth service](admin_auth_service.md) (1 shared connections)
- [npc lifecycle combat](npc_lifecycle_combat.md) (1 shared connections)
- [archive QUALITY AUDIT](archive_QUALITY_AUDIT.md) (1 shared connections)
- [persistence constants rationale](persistence_constants_rationale.md) (1 shared connections)

## Source Files

- `server/auth/argon2_utils.py`
- `server/auth/users.py`
- `server/tests/unit/auth/test_argon2_utils.py`

## Audit Trail

- EXTRACTED: 71 (93%)
- INFERRED: 5 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*