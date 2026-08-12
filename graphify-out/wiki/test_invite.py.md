# test_invite.py

> 16 nodes

## Key Concepts

- **test_invite.py** (17 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_is_expired_with_aware_datetime()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_is_expired_with_future_expiry()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_is_expired_with_past_expiry()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_is_valid_with_active_and_not_expired()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_is_valid_with_expired()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_is_valid_with_inactive_and_expired()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **test_invite_use_invite()** (3 connections) — `server/tests/unit/models/test_invite.py`
- **Unit tests for the Invite model. Tests the Invite model methods including…** (1 connections) — `server/tests/unit/models/test_invite.py`
- **Test is_expired returns False for future expiry date.** (1 connections) — `server/tests/unit/models/test_invite.py`
- **Test is_expired returns True for past expiry date.** (1 connections) — `server/tests/unit/models/test_invite.py`
- **Test is_expired handles timezone-aware datetime.** (1 connections) — `server/tests/unit/models/test_invite.py`
- **Test is_valid returns True for active, non-expired invite.** (1 connections) — `server/tests/unit/models/test_invite.py`
- **Test is_valid returns False for expired invite.** (1 connections) — `server/tests/unit/models/test_invite.py`
- **Test is_valid returns False for inactive and expired invite.** (1 connections) — `server/tests/unit/models/test_invite.py`
- **Test use_invite marks invite as used and sets user_id.** (1 connections) — `server/tests/unit/models/test_invite.py`

## Relationships

- [Invite](Invite.md) (11 shared connections)
- [.create_invite](create_invite.md) (3 shared connections)
- [._generate_invite_code](_generate_invite_code.md) (2 shared connections)

## Source Files

- `server/tests/unit/models/test_invite.py`

## Audit Trail

- EXTRACTED: 46 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*