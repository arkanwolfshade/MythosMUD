# server tests unit game test

> 50 nodes

## Key Concepts

- **test_party_service.py** (39 connections) — `server/tests/unit/game/test_party_service.py`
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
- **test_remove_member_leave_success()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- *... and 25 more nodes in this community*

## Relationships

- [server tests unit game test](server_tests_unit_game_test.md) (6 shared connections)
- [server game party service party](server_game_party_service_party.md) (3 shared connections)
- [server app lifespan event subscriptions](server_app_lifespan_event_subscriptions.md) (2 shared connections)
- [claude rules pytest](claude_rules_pytest.md) (1 shared connections)
- [server game party service partyservice](server_game_party_service_partyservice.md) (1 shared connections)
- [claude rules asyncio](claude_rules_asyncio.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/test_party_service.py`

## Audit Trail

- EXTRACTED: 63 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*