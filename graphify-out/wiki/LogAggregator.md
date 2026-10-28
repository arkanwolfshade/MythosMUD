# LogAggregator

> 73 nodes · cohesion 0.03

## Key Concepts

- **test_party_service.py** (40 connections) — `server/tests/unit/game/test_party_service.py`
- **assert_event_envelope()** (9 connections) — `server/tests/unit/realtime/envelope_assertions.py`
- **asyncio** (7 connections)
- **test_party_invite_event_envelope_shape()** (5 connections) — `server/tests/unit/game/test_party_service.py`
- **envelope_assertions.py** (5 connections) — `server/tests/unit/realtime/envelope_assertions.py`
- **party_service()** (4 connections) — `server/tests/unit/game/test_party_service.py`
- **test_on_player_disconnect_cancels_pending_invite_as_inviter()** (4 connections) — `server/tests/unit/game/test_party_service.py`
- **test_on_player_disconnect_cancels_pending_invite_as_target()** (4 connections) — `server/tests/unit/game/test_party_service.py`
- **test_accept_party_invite_success()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **test_decline_party_invite_success()** (3 connections) — `server/tests/unit/game/test_party_service.py`
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
- *... and 48 more nodes in this community*

## Relationships

- [test_wearable_container_service.py](test_wearable_container_service.py.md) (5 shared connections)
- [test_experience_procedures.py](test_experience_procedures.py.md) (4 shared connections)
- [SpellLearningService](SpellLearningService.md) (3 shared connections)
- [SchemaValidator](SchemaValidator.md) (3 shared connections)

## Source Files

- `server/tests/unit/game/test_party_service.py`
- `server/tests/unit/realtime/envelope_assertions.py`

## Audit Trail

- EXTRACTED: 93 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*