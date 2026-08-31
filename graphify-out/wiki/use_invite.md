# .use_invite

> 5 nodes

## Key Concepts

- **.use_invite()** (5 connections) — `server/auth/invites.py`
- **.get_user_invites()** (4 connections) — `server/auth/invites.py`
- **UUID** (3 connections)
- **Mark an invite as used by a specific user (atomic auth-and-capture). Uses the…** (1 connections) — `server/auth/invites.py`
- **Get all invites used by a user.** (1 connections) — `server/auth/invites.py`

## Relationships

- [Invite](Invite.md) (2 shared connections)
- [InviteManager](InviteManager.md) (2 shared connections)
- [LoggedHTTPException](LoggedHTTPException.md) (2 shared connections)

## Source Files

- `server/auth/invites.py`

## Audit Trail

- EXTRACTED: 10 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*