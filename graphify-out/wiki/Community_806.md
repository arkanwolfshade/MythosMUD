# Community 806

> 20 nodes

## Key Concepts

- **hash_password()** (25 connections) — `server/auth/argon2_utils.py`
- **seed_e2e_users.py** (9 connections) — `scripts/seed_e2e_users.py`
- **_ensure_player_for_user()** (5 connections) — `scripts/seed_e2e_users.py`
- **_seed_e2e_users()** (4 connections) — `scripts/seed_e2e_users.py`
- **_validate_password_for_hashing()** (4 connections) — `server/auth/argon2_utils.py`
- **test_verify_password_failure()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_verify_password_non_string_password()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **test_verify_password_success()** (4 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **main()** (3 connections) — `scripts/seed_e2e_users.py`
- **E2eUserSpec** (2 connections) — `scripts/seed_e2e_users.py`
- **datetime** (2 connections)
- **UUID** (2 connections)
- **Connection** (1 connections)
- **Entry point: run E2E user seed via anyio.** (1 connections) — `scripts/seed_e2e_users.py`
- **One row in users plus optional default character for login E2E.** (1 connections) — `scripts/seed_e2e_users.py`
- **Validate password input before Argon2 hashing.** (1 connections) — `server/auth/argon2_utils.py`
- **Hash a plaintext password using Argon2id. This function provides superior…** (1 connections) — `server/auth/argon2_utils.py`
- **Test verifying password with non-string password returns False.** (1 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **Test successful password verification.** (1 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **Test password verification with wrong password.** (1 connections) — `server/tests/unit/auth/test_argon2_utils.py`

## Relationships

- [Community 212](Community_212.md) (15 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (9 shared connections)
- [User Manager & Character Info](User_Manager_&_Character_Info.md) (2 shared connections)
- [Community 94](Community_94.md) (2 shared connections)

## Source Files

- `scripts/seed_e2e_users.py`
- `server/auth/argon2_utils.py`
- `server/tests/unit/auth/test_argon2_utils.py`

## Audit Trail

- EXTRACTED: 51 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*