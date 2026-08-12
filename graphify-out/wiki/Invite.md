# Invite

> 19 nodes

## Key Concepts

- **Invite** (34 connections) — `server/models/invite.py`
- **models/invite.py** (10 connections) — `server/models/invite.py`
- **.get_unused_invites()** (3 connections) — `server/auth/invites.py`
- **.is_expired()** (3 connections) — `server/models/invite.py`
- **.is_valid()** (3 connections) — `server/models/invite.py`
- **test_invite_is_valid_with_inactive()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_repr()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **.list_invites()** (2 connections) — `server/auth/invites.py`
- **.use_invite()** (2 connections) — `server/models/invite.py`
- **.__repr__()** (1 connections) — `server/models/invite.py`
- **Base** (1 connections)
- **Get all unused invites.** (1 connections) — `server/auth/invites.py`
- **Invite model for MythosMUD. This module defines the Invite model for managing…** (1 connections) — `server/models/invite.py`
- **Model for user registration invites.** (1 connections) — `server/models/invite.py`
- **Check if the invite has expired. Handles naive timestamps as UTC.** (1 connections) — `server/models/invite.py`
- **Check if the invite is valid (active and not expired).** (1 connections) — `server/models/invite.py`
- **Mark this invite as used by a specific user.** (1 connections) — `server/models/invite.py`
- **Test __repr__ returns expected string format.** (1 connections) — `server/tests/unit/models/test_invite.py`
- **Test is_valid returns False for inactive invite.** (1 connections) — `server/tests/unit/models/test_invite.py`

## Relationships

- [test_invite.py](test_invite.py.md) (11 shared connections)
- [User](User.md) (9 shared connections)
- [Player](Player.md) (5 shared connections)
- [generate_invites_db.py](generate_invites_db.py.md) (3 shared connections)
- [server/schemas/__init__.py](server-schemas-__init__.py.md) (2 shared connections)
- [._generate_invite_code](_generate_invite_code.md) (2 shared connections)
- [.get_instance](get_instance.md) (1 shared connections)
- [.is_active](is_active.md) (1 shared connections)
- [.create_invite](create_invite.md) (1 shared connections)

## Source Files

- `server/auth/invites.py`
- `server/models/invite.py`
- `server/tests/unit/models/test_invite.py`

## Audit Trail

- EXTRACTED: 52 (96%)
- INFERRED: 2 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*