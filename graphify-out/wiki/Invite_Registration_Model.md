# Invite Registration Model

> 48 nodes · cohesion 0.05

## Key Concepts

- **Invite** (34 connections) — `server/models/invite.py`
- **test_invite.py** (16 connections) — `server/tests/unit/models/test_invite.py`
- **set_display_name_default()** (4 connections) — `server/models/user.py`
- **Any** (4 connections) — `server/models/user.py`
- **.create_invite()** (3 connections) — `server/models/invite.py`
- **._generate_invite_code()** (3 connections) — `server/models/invite.py`
- **.__init__()** (3 connections) — `server/models/invite.py`
- **.is_expired()** (3 connections) — `server/models/invite.py`
- **.is_valid()** (3 connections) — `server/models/invite.py`
- **test_invite_is_expired_with_aware_datetime()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_is_expired_with_future_expiry()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_is_expired_with_past_expiry()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_is_valid_with_active_and_not_expired()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_is_valid_with_expired()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_is_valid_with_inactive()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_is_valid_with_inactive_and_expired()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_repr()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_use_invite()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **Any** (3 connections) — `server/models/invite.py`
- **.use_invite()** (2 connections) — `server/models/invite.py`
- **Test is_valid returns False for expired invite.** (2 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_create_invite_defaults()** (2 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_create_invite_with_creator()** (2 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_create_invite_with_custom_expiry()** (2 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_generate_invite_code_format()** (2 connections) — `server/tests/unit/models/test_invite.py`
- *... and 23 more nodes in this community*

## Relationships

- [[SQLAlchemy Model Base]] (6 shared connections)
- [[NPC Admin API]] (4 shared connections)
- [[Lucidity Database Models]] (4 shared connections)
- [[Invite Generate Invites]] (3 shared connections)
- [[API Test Fixtures]] (3 shared connections)
- [[Player Domain Model]] (1 shared connections)

## Source Files

- `server/models/invite.py`
- `server/models/user.py`
- `server/tests/unit/models/test_invite.py`

## Audit Trail

- EXTRACTED: 126 (91%)
- INFERRED: 13 (9%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
