# test_party_service.py

> 53 nodes

## Key Concepts

- **test_party_service.py** (39 connections) — `server/tests/unit/game/test_party_service.py`
- **party_service()** (4 connections) — `server/tests/unit/game/test_party_service.py`
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
- **test_is_leader_false_when_not_in_party()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_kick_member_leader_success()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_kick_member_non_leader_rejected()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_kick_self_rejected()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_on_player_disconnect_leader_disbands_party()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_on_player_disconnect_member_removed()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_on_player_disconnect_not_in_party_no_op()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_remove_member_leader_leaves_disbands()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- *... and 28 more nodes in this community*

## Relationships

- [asyncio](asyncio.md) (5 shared connections)
- [PartyService](PartyService.md) (3 shared connections)
- [Party](Party.md) (3 shared connections)
- [test_follow_service.py](test_follow_service.py.md) (2 shared connections)
- [pytest.md](pytest.md.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/test_party_service.py`

## Audit Trail

- EXTRACTED: 65 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*