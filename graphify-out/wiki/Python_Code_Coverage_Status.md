# Python Code Coverage Status

> 11 nodes

## Key Concepts

- **test_party_invite_event_envelope_shape()** (5 connections) — `server/tests/unit/game/test_party_service.py`
- **asyncio** (5 connections)
- **test_accept_party_invite_success()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **test_decline_party_invite_success()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **test_request_party_invite_creates_pending()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **test_request_party_invite_target_already_in_party_rejected()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **Accepting a party invite adds the player to the party.** (1 connections) — `server/tests/unit/game/test_party_service.py`
- **Declining removes pending invite and does not add to party.** (1 connections) — `server/tests/unit/game/test_party_service.py`
- **Request fails if target is already in a party.** (1 connections) — `server/tests/unit/game/test_party_service.py`
- **party_invite producer emits a build_event-shaped envelope.** (1 connections) — `server/tests/unit/game/test_party_service.py`
- **Requesting a party invite creates a pending invite (target must accept).** (1 connections) — `server/tests/unit/game/test_party_service.py`

## Relationships

- [SafeHtml.tsx](SafeHtml.tsx.md) (5 shared connections)
- [NPCMovementIntegration](NPCMovementIntegration.md) (1 shared connections)
- [WebSocket Best Practices](WebSocket_Best_Practices.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/test_party_service.py`

## Audit Trail

- EXTRACTED: 16 (94%)
- INFERRED: 1 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*