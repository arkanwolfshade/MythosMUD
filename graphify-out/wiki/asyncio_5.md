# asyncio

> 9 nodes

## Key Concepts

- **asyncio** (4 connections)
- **test_accept_party_invite_success()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **test_decline_party_invite_success()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **test_request_party_invite_creates_pending()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **test_request_party_invite_target_already_in_party_rejected()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **Accepting a party invite adds the player to the party.** (1 connections) — `server/tests/unit/game/test_party_service.py`
- **Declining removes pending invite and does not add to party.** (1 connections) — `server/tests/unit/game/test_party_service.py`
- **Request fails if target is already in a party.** (1 connections) — `server/tests/unit/game/test_party_service.py`
- **Requesting a party invite creates a pending invite (target must accept).** (1 connections) — `server/tests/unit/game/test_party_service.py`

## Relationships

- [test_party_service.py](test_party_service.py.md) (4 shared connections)

## Source Files

- `server/tests/unit/game/test_party_service.py`

## Audit Trail

- EXTRACTED: 20 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*