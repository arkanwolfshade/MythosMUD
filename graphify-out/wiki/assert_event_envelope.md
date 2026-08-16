# assert_event_envelope

> 18 nodes

## Key Concepts

- **assert_event_envelope()** (11 connections) — `server/tests/unit/realtime/envelope_assertions.py`
- **envelope_assertions.py** (6 connections) — `server/tests/unit/realtime/envelope_assertions.py`
- **test_party_invite_event_envelope_shape()** (5 connections) — `server/tests/unit/game/test_party_service.py`
- **asyncio** (5 connections)
- **test_broadcast_combat_start()** (4 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`
- **test_accept_party_invite_success()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **test_decline_party_invite_success()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **test_request_party_invite_creates_pending()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **test_request_party_invite_target_already_in_party_rejected()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **Any** (1 connections)
- **Accepting a party invite adds the player to the party.** (1 connections) — `server/tests/unit/game/test_party_service.py`
- **Declining removes pending invite and does not add to party.** (1 connections) — `server/tests/unit/game/test_party_service.py`
- **Request fails if target is already in a party.** (1 connections) — `server/tests/unit/game/test_party_service.py`
- **party_invite producer emits a build_event-shaped envelope.** (1 connections) — `server/tests/unit/game/test_party_service.py`
- **Requesting a party invite creates a pending invite (target must accept).** (1 connections) — `server/tests/unit/game/test_party_service.py`
- **Shared contract assertions for realtime event envelopes produced via…** (1 connections) — `server/tests/unit/realtime/envelope_assertions.py`
- **Assert a fan-out producer event matches the build_event envelope shape.** (1 connections) — `server/tests/unit/realtime/envelope_assertions.py`
- **Test broadcast_combat_start broadcasts combat start event.** (1 connections) — `server/tests/unit/services/test_combat_messaging_integration.py`

## Relationships

- [test_party_service.py](test_party_service.py.md) (7 shared connections)
- [test_combat_messaging_integration.py](test_combat_messaging_integration.py.md) (4 shared connections)
- [.__post_init__](__post_init__.md) (3 shared connections)
- [test_follow_service.py](test_follow_service.py.md) (3 shared connections)
- [PartyService](PartyService.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/test_party_service.py`
- `server/tests/unit/realtime/envelope_assertions.py`
- `server/tests/unit/services/test_combat_messaging_integration.py`

## Audit Trail

- EXTRACTED: 34 (97%)
- INFERRED: 1 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*