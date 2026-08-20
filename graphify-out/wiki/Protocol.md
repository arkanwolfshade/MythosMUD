# Protocol

> 9 nodes

## Key Concepts

- **Protocol** (4 connections)
- **_HasId** (3 connections) — `server/services/admin_auth_service.py`
- **_HasIsAdmin** (3 connections) — `server/services/admin_auth_service.py`
- **_HasIsSuperuser** (3 connections) — `server/services/admin_auth_service.py`
- **_HasUsername** (3 connections) — `server/services/admin_auth_service.py`
- **Narrowing for user shapes that expose is_superuser.** (1 connections) — `server/services/admin_auth_service.py`
- **Narrowing for user shapes that expose is_admin.** (1 connections) — `server/services/admin_auth_service.py`
- **Narrowing for user shapes that expose username.** (1 connections) — `server/services/admin_auth_service.py`
- **Narrowing for user shapes that expose id.** (1 connections) — `server/services/admin_auth_service.py`

## Relationships

- [get_logger](get_logger.md) (4 shared connections)

## Source Files

- `server/services/admin_auth_service.py`

## Audit Trail

- EXTRACTED: 12 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*