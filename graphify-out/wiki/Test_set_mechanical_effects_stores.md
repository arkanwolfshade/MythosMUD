# Test set mechanical effects stores

> 5 nodes

## Key Concepts

- **AdminSession** (6 connections) — `server/services/admin_auth_service.py`
- **test_admin_session_init()** (3 connections) — `server/tests/unit/services/test_admin_auth_service.py`
- **.__init__()** (2 connections) — `server/services/admin_auth_service.py`
- **Represents an admin session.** (1 connections) — `server/services/admin_auth_service.py`
- **Test AdminSession initialization.** (1 connections) — `server/tests/unit/services/test_admin_auth_service.py`

## Relationships

- [init](init.md) (2 shared connections)
- [Request](Request.md) (2 shared connections)
- [close db()](close_db%28%29.md) (1 shared connections)

## Source Files

- `server/services/admin_auth_service.py`
- `server/tests/unit/services/test_admin_auth_service.py`

## Audit Trail

- EXTRACTED: 13 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*