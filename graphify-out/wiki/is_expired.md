# .is_expired

> 4 nodes

## Key Concepts

- **.is_expired()** (3 connections) — `server/models/invite.py`
- **.is_valid()** (3 connections) — `server/models/invite.py`
- **Check if the invite has expired. Handles naive timestamps as UTC.** (1 connections) — `server/models/invite.py`
- **Check if the invite is valid (active and not expired).** (1 connections) — `server/models/invite.py`

## Relationships

- [Invite](Invite.md) (2 shared connections)

## Source Files

- `server/models/invite.py`

## Audit Trail

- EXTRACTED: 5 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*