# Community 1493

> 5 nodes

## Key Concepts

- **.use_invite()** (5 connections) — `server/auth/invites.py`
- **.get_user_invites()** (4 connections) — `server/auth/invites.py`
- **UUID** (3 connections)
- **Mark an invite as used by a specific user (atomic auth-and-capture). Uses the…** (1 connections) — `server/auth/invites.py`
- **Get all invites used by a user.** (1 connections) — `server/auth/invites.py`

## Relationships

- [Community 510](Community_510.md) (2 shared connections)
- [Community 610](Community_610.md) (2 shared connections)
- [Container API Models](Container_API_Models.md) (1 shared connections)
- [Auth Dependencies & Users](Auth_Dependencies_&_Users.md) (1 shared connections)

## Source Files

- `server/auth/invites.py`

## Audit Trail

- EXTRACTED: 10 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*