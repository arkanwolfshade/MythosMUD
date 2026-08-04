# commands inventory helpers

> 42 nodes

## Key Concepts

- **test_party_service.py** (38 connections) — `server/tests/unit/game/test_party_service.py`
- **test_party_post_init_includes_leader_in_members()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **test_party_post_init_preserves_other_members()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **test_create_party_success()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_add_member_success()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_add_member_already_in_party_rejected()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_request_party_invite_creates_pending()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_accept_party_invite_success()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_decline_party_invite_success()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_request_party_invite_target_already_in_party_rejected()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_remove_member_leave_success()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_kick_member_leader_success()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_kick_self_rejected()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_disband_party_by_leader_success()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_disband_party_by_non_leader_rejected()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_disband_party_by_id_without_caller()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_get_party_for_player_not_in_party()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_get_party_members_empty_when_not_in_party()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_get_party_members_includes_self()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_on_player_disconnect_not_in_party_no_op()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **test_is_in_same_party_false_when_different_parties()** (2 connections) — `server/tests/unit/game/test_party_service.py`
- **Unit tests for PartyService.  Covers: create_party, disband_party, add_member, r** (1 connections) — `server/tests/unit/game/test_party_service.py`
- **Leader can create a new party.** (1 connections) — `server/tests/unit/game/test_party_service.py`
- **Leader can add a member (invite flow simulated).** (1 connections) — `server/tests/unit/game/test_party_service.py`
- **Adding a player who is already in a party fails.** (1 connections) — `server/tests/unit/game/test_party_service.py`
- *... and 17 more nodes in this community*

## Relationships

- [Error Conversion](Error_Conversion.md) (4 shared connections)
- [event bus events](event_bus_events.md) (4 shared connections)
- [skill game service](skill_game_service.md) (3 shared connections)
- [room game service](room_game_service.md) (2 shared connections)
- [chat game service](chat_game_service.md) (2 shared connections)
- [party game service](party_game_service.md) (1 shared connections)
- [room realtime subscription](room_realtime_subscription.md) (1 shared connections)
- [game room service](game_room_service.md) (1 shared connections)
- [events event bus](events_event_bus.md) (1 shared connections)

## Source Files

- `server/tests/unit/game/test_party_service.py`

## Audit Trail

- EXTRACTED: 101 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*