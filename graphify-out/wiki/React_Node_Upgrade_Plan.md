# React Node Upgrade Plan

> 3 nodes

## Key Concepts

- **.set_legacy_environment_variables()** (3 connections) — `server/config/models/app.py`
- **model_validator** (1 connections)
- **Set environment variables for legacy code that reads them directly.** (1 connections) — `server/config/models/app.py`

## Relationships

- [generate_invites_db.py](generate_invites_db.py.md) (1 shared connections)

## Source Files

- `server/config/models/app.py`

## Audit Trail

- EXTRACTED: 3 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*