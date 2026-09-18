# Community 671

> 25 nodes

## Key Concepts

- **Invite** (47 connections) — `server/models/invite.py`
- **test_invite.py** (17 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_is_expired_with_aware_datetime()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_is_expired_with_future_expiry()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_is_expired_with_past_expiry()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_is_valid_with_active_and_not_expired()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_is_valid_with_expired()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_is_valid_with_inactive()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_is_valid_with_inactive_and_expired()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_repr()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_use_invite()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **.use_invite()** (2 connections) — `server/models/invite.py`
- **Test is_valid returns False for expired invite.** (2 connections) — `server/tests/unit/models/test_invite.py`
- **.__repr__()** (1 connections) — `server/models/invite.py`
- **Base** (1 connections)
- **Model for user registration invites.** (1 connections) — `server/models/invite.py`
- **Mark this invite as used by a specific user.** (1 connections) — `server/models/invite.py`
- **Unit tests for the Invite model. Tests the Invite model methods including…** (1 connections) — `server/tests/unit/models/test_invite.py`
- **Test is_expired returns False for future expiry date.** (1 connections) — `server/tests/unit/models/test_invite.py`
- **Test __repr__ returns expected string format.** (1 connections) — `server/tests/unit/models/test_invite.py`
- **Test is_expired returns True for past expiry date.** (1 connections) — `server/tests/unit/models/test_invite.py`
- **Test is_expired handles timezone-aware datetime.** (1 connections) — `server/tests/unit/models/test_invite.py`
- **Test is_valid returns True for active, non-expired invite.** (1 connections) — `server/tests/unit/models/test_invite.py`
- **Test is_valid returns False for inactive invite.** (1 connections) — `server/tests/unit/models/test_invite.py`
- **Test use_invite marks invite as used and sets user_id.** (1 connections) — `server/tests/unit/models/test_invite.py`

## Relationships

- [Community 692](Community_692.md) (11 shared connections)
- [Community 1296](Community_1296.md) (7 shared connections)
- [Community 1293](Community_1293.md) (6 shared connections)
- [Character Creation & Auth Dependencies](Character_Creation_&_Auth_Dependencies.md) (5 shared connections)
- [Invite Codes & Session Maker (E2E)](Invite_Codes_&_Session_Maker_E2E.md) (2 shared connections)
- [Community 1466](Community_1466.md) (2 shared connections)
- [Community 1467](Community_1467.md) (2 shared connections)
- [Community 1557](Community_1557.md) (2 shared connections)
- [Community 1188](Community_1188.md) (1 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (1 shared connections)

## Source Files

- `server/models/invite.py`
- `server/tests/unit/models/test_invite.py`

## Audit Trail

- EXTRACTED: 57 (78%)
- INFERRED: 16 (22%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*