# Endpoints

> 5 nodes

## Key Concepts

- **.validate_invite_code()** (3 connections) — `server/auth/endpoints.py`
- **.validate_password()** (3 connections) — `server/auth/endpoints.py`
- **field_validator** (2 connections)
- **Validate password length and content.** (1 connections) — `server/auth/endpoints.py`
- **Validate invite code is present and non-blank.** (1 connections) — `server/auth/endpoints.py`

## Relationships

- [Test Endpoints Register](Test_Endpoints_Register.md) (2 shared connections)

## Source Files

- `server/auth/endpoints.py`

## Audit Trail

- EXTRACTED: 6 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*