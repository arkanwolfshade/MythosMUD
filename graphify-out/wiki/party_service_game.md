# party service game

> 58 nodes

## Key Concepts

- **test_party_service.py** (38 connections) — `server/tests/unit/game/test_party_service.py`
- **test_party_post_init_includes_leader_in_members()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **test_party_post_init_preserves_other_members()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **test_create_party_success()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_create_party_already_in_party_rejected()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_add_member_success()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_add_member_already_in_party_rejected()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_add_member_no_such_party()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_request_party_invite_creates_pending()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_accept_party_invite_success()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_decline_party_invite_success()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_request_party_invite_target_already_in_party_rejected()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_remove_member_leave_success()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_remove_member_leader_leaves_disbands()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_kick_member_leader_success()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_kick_member_non_leader_rejected()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_kick_self_rejected()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_disband_party_by_leader_success()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_disband_party_by_non_leader_rejected()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_disband_party_by_id_without_caller()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_get_party_for_player_not_in_party()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_get_party_members_empty_when_not_in_party()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_get_party_members_includes_self()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_is_leader_false_when_not_in_party()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_on_player_disconnect_member_removed()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- *... and 33 more nodes in this community*

## Relationships

- [NATS Messaging](NATS_Messaging.md) (6 shared connections)
- [envelope event game](envelope_event_game.md) (3 shared connections)
- [models invite rationale](models_invite_rationale.md) (1 shared connections)
- [persistence heal player()](persistence_heal_player%28%29.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/test_party_service.py`

## Audit Trail

- EXTRACTED: 125 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*