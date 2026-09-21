# test_party_service.py

> 72 nodes

## Key Concepts

- **test_party_service.py** (40 connections) — `server/tests/unit/game/test_party_service.py`
- **asyncio** (7 connections)
- **test_party_invite_event_envelope_shape()** (5 connections) — `server/tests/unit/game/test_party_service.py`
- **party_service()** (4 connections) — `server/tests/unit/game/test_party_service.py`
- **test_on_player_disconnect_cancels_pending_invite_as_inviter()** (4 connections) — `server/tests/unit/game/test_party_service.py`
- **test_on_player_disconnect_cancels_pending_invite_as_target()** (4 connections) — `server/tests/unit/game/test_party_service.py`
- **test_accept_party_invite_success()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **test_decline_party_invite_success()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **test_party_post_init_includes_leader_in_members()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **test_party_post_init_preserves_other_members()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **test_request_party_invite_creates_pending()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **test_request_party_invite_target_already_in_party_rejected()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **test_add_member_already_in_party_rejected()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_add_member_no_such_party()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_add_member_success()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_create_party_already_in_party_rejected()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_create_party_success()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_disband_party_by_id_without_caller()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_disband_party_by_leader_success()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_disband_party_by_non_leader_rejected()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_get_party_for_player_not_in_party()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_get_party_members_empty_when_not_in_party()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_get_party_members_includes_self()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_is_in_same_party_false_when_different_parties()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_is_in_same_party_false_when_one_not_in_party()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- *... and 47 more nodes in this community*

## Relationships

- [PartyService](PartyService.md) (9 shared connections)
- [test_lifespan_event_subscriptions.py](test_lifespan_event_subscriptions.py.md) (3 shared connections)

## Source Files

- `server/tests/unit/game/test_party_service.py`

## Audit Trail

- EXTRACTED: 87 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*