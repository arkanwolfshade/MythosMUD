# Argon2 Password Hashing

> 23 nodes · cohesion 0.01

## Key Concepts

- **Request** (10 connections) — `server/auth/endpoints.py`
- **IntegrityError** (8 connections) — `server/auth/endpoints.py`
- **Any** (8 connections) — `server/auth/endpoints.py`
- **AsyncSession** (7 connections) — `server/auth/endpoints.py`
- **Result** (5 connections) — `scripts/run_test_ci.py`
- **Any** (5 connections) — `server/auth/users.py`
- **UserManager** (4 connections) — `server/auth/endpoints.py`
- **Request** (4 connections) — `server/auth/users.py`
- **UUID** (4 connections) — `server/auth/users.py`
- **Any** (4 connections) — `server/models/user.py`
- **SQLAlchemyUserDatabase** (4 connections) — `server/auth/users.py`
- **AuthenticationBackend** (3 connections) — `server/auth/users.py`
- **UUID** (3 connections) — `server/auth/invites.py`
- **Request** (2 connections) — `server/api/professions.py`
- **AsyncSession** (2 connections) — `server/auth/invites.py`
- **datetime** (2 connections) — `server/auth/invites.py`
- **AsyncSession** (2 connections) — `server/auth/users.py`
- **Container for subprocess result data (returncode, stdout, stderr).** (1 connections) — `scripts/run_test_ci.py`
- **.__init__()** (1 connections) — `scripts/run_test_ci.py`
- **AsyncSession** (1 connections) — `server/auth/email_utils.py`
- **Request** (1 connections) — `server/auth/invites.py`
- **SQLAlchemyBaseUserTableUUID** (1 connections)
- **UUIDIDMixin** (1 connections)

## Relationships

- [Distributed Event Bus](Distributed_Event_Bus.md) (1 shared connections)

## Source Files

- `scripts/run_test_ci.py`
- `server/api/professions.py`
- `server/auth/email_utils.py`
- `server/auth/endpoints.py`
- `server/auth/invites.py`
- `server/auth/users.py`
- `server/models/user.py`

## Audit Trail

- EXTRACTED: 57 (69%)
- INFERRED: 26 (31%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*