# Argon2 Password Hashing

> 223 nodes · cohesion 0.02

## Key Concepts

- **endpoints.py** (49 connections) — `server/auth/endpoints.py`
- **test_endpoints.py** (49 connections) — `server/tests/unit/auth/test_endpoints.py`
- **test_argon2_utils.py** (41 connections) — `server/tests/unit/auth/test_argon2_utils.py`
- **login_user()** (29 connections) — `server/auth/endpoints.py`
- **register_user()** (28 connections) — `server/auth/endpoints.py`
- **InviteManager** (28 connections) — `server/auth/invites.py`
- **hash_password()** (27 connections) — `server/auth/argon2_utils.py`
- **UserCreate** (26 connections) — `server/auth/endpoints.py`
- **LoginRequest** (22 connections) — `server/auth/endpoints.py`
- **verify_password()** (16 connections) — `server/auth/argon2_utils.py`
- **create_hasher_with_params()** (11 connections) — `server/auth/argon2_utils.py`
- **User** (11 connections) — `server/auth/endpoints.py`
- **list_invites()** (10 connections) — `server/auth/endpoints.py`
- **Request** (10 connections) — `server/auth/endpoints.py`
- **is_argon2_hash()** (9 connections) — `server/auth/argon2_utils.py`
- **_check_shutdown_status()** (8 connections) — `server/auth/endpoints.py`
- **create_invite()** (8 connections) — `server/auth/endpoints.py`
- **IntegrityError** (8 connections) — `server/auth/endpoints.py`
- **Any** (8 connections) — `server/auth/endpoints.py`
- **needs_rehash()** (7 connections) — `server/auth/argon2_utils.py`
- **_authenticate_user_credentials()** (7 connections) — `server/auth/endpoints.py`
- **_create_user_object()** (7 connections) — `server/auth/endpoints.py`
- **_find_user_by_username()** (7 connections) — `server/auth/endpoints.py`
- **LoginResponse** (7 connections) — `server/auth/endpoints.py`
- **_validate_invite_code()** (7 connections) — `server/auth/endpoints.py`
- *... and 198 more nodes in this community*

## Relationships

- [[NPC Admin API]] (31 shared connections)
- [[API Test Fixtures]] (28 shared connections)
- [[Restart Invalidating JWT]] (16 shared connections)
- [[Container Exception Handlers]] (9 shared connections)
- [[Auth Token Utilities]] (6 shared connections)
- [[Admin NPC Schemas]] (5 shared connections)
- [[FastAPI App Factory]] (4 shared connections)
- [[Database Manager Tests]] (3 shared connections)
- [[Seed E 2 E Users]] (2 shared connections)
- [[Standardized Error Responses]] (2 shared connections)
- [[Character Creation API]] (2 shared connections)
- [[Admin Shutdown Command]] (2 shared connections)

## Source Files

- `server/auth/argon2_utils.py`
- `server/auth/endpoints.py`
- `server/auth/invites.py`
- `server/auth/users.py`
- `server/tests/unit/auth/test_argon2_utils.py`
- `server/tests/unit/auth/test_endpoints.py`

## Audit Trail

- EXTRACTED: 884 (95%)
- INFERRED: 50 (5%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
