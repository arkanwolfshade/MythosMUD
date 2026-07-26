# test_party_service.py

> 56 nodes · cohesion 0.04

## Key Concepts

- **test_party_service.py** (35 connections) — `server/tests/unit/game/test_party_service.py`
- **test_party_post_init_includes_leader_in_members()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **test_party_post_init_preserves_other_members()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **test_accept_party_invite_success()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_add_member_already_in_party_rejected()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_add_member_no_such_party()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_add_member_success()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_create_party_already_in_party_rejected()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_create_party_success()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_decline_party_invite_success()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_disband_party_by_id_without_caller()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_disband_party_by_leader_success()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_disband_party_by_non_leader_rejected()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_get_party_members_empty_when_not_in_party()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_get_party_members_includes_self()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_is_in_same_party_false_when_different_parties()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_is_in_same_party_false_when_one_not_in_party()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_is_in_same_party_true_when_both_in_party()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_is_leader_false_when_member()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_is_leader_false_when_not_in_party()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_kick_member_leader_success()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_kick_self_rejected()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_on_player_disconnect_leader_disbands_party()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_on_player_disconnect_not_in_party_no_op()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_remove_member_leader_leaves_disbands()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- *... and 31 more nodes in this community*

## Relationships

- [get_logger](get_logger.md) (4 shared connections)
- [PartyService](PartyService.md) (2 shared connections)
- [test_mute_channel_system_channel](test_mute_channel_system_channel.md) (1 shared connections)
- [test_update_default_channel_not_found](test_update_default_channel_not_found.md) (1 shared connections)
- [test_unmute_channel_success](test_unmute_channel_success.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/test_party_service.py`

## Audit Trail

- EXTRACTED: 119 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*