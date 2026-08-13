# test_party_service.py

> 67 nodes

## Key Concepts

- **test_party_service.py** (35 connections) — `server/tests/unit/game/test_party_service.py`
- **Party** (12 connections) — `server/game/party_service.py`
- **asyncio** (4 connections)
- **test_accept_party_invite_success()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **test_decline_party_invite_success()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **test_party_post_init_includes_leader_in_members()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **test_party_post_init_preserves_other_members()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **test_request_party_invite_creates_pending()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **test_request_party_invite_target_already_in_party_rejected()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **.__post_init__()** (2 connections) — `server/game/party_service.py`
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
- **test_is_in_same_party_true_when_both_in_party()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_is_leader_false_when_member()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- *... and 42 more nodes in this community*

## Relationships

- [PartyService](PartyService.md) (6 shared connections)
- [EventBus](EventBus.md) (3 shared connections)
- [ConnectionManager](ConnectionManager.md) (1 shared connections)

## Source Files

- `server/game/party_service.py`
- `server/tests/unit/game/test_party_service.py`

## Audit Trail

- EXTRACTED: 78 (96%)
- INFERRED: 3 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*