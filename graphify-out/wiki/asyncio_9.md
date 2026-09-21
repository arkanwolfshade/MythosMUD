# asyncio

> 15 nodes

## Key Concepts

- **asyncio** (7 connections)
- **test_party_invite_event_envelope_shape()** (5 connections) — `server/tests/unit/game/test_party_service.py`
- **test_on_player_disconnect_cancels_pending_invite_as_inviter()** (4 connections) — `server/tests/unit/game/test_party_service.py`
- **test_on_player_disconnect_cancels_pending_invite_as_target()** (4 connections) — `server/tests/unit/game/test_party_service.py`
- **test_accept_party_invite_success()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **test_decline_party_invite_success()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **test_request_party_invite_creates_pending()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **test_request_party_invite_target_already_in_party_rejected()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **Accepting a party invite adds the player to the party.** (1 connections) — `server/tests/unit/game/test_party_service.py`
- **Declining removes pending invite and does not add to party.** (1 connections) — `server/tests/unit/game/test_party_service.py`
- **Request fails if target is already in a party.** (1 connections) — `server/tests/unit/game/test_party_service.py`
- **party_invite producer emits a build_event-shaped envelope.** (1 connections) — `server/tests/unit/game/test_party_service.py`
- **Disconnect of the inviter cancels their pending invite to the target.** (1 connections) — `server/tests/unit/game/test_party_service.py`
- **Disconnect of the invite target cancels the pending invite.** (1 connections) — `server/tests/unit/game/test_party_service.py`
- **Requesting a party invite creates a pending invite (target must accept).** (1 connections) — `server/tests/unit/game/test_party_service.py`

## Relationships

- [test_party_service.py](test_party_service.py.md) (7 shared connections)
- [PartyService](PartyService.md) (3 shared connections)
- [._bind_event_type](_bind_event_type.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/test_party_service.py`

## Audit Trail

- EXTRACTED: 23 (92%)
- INFERRED: 2 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*