# commands inventory helpers

> 82 nodes

## Key Concepts

- **test_party_service.py** (38 connections) — `server/tests/unit/game/test_party_service.py`
- **party_service.py** (16 connections) — `server/game/party_service.py`
- **PartyUpdated** (12 connections) — `server/events/event_types.py`
- **Party** (12 connections) — `server/game/party_service.py`
- **test_party_flow.py** (12 connections) — `server/tests/integration/test_party_flow.py`
- **party_events()** (4 connections) — `server/tests/integration/test_party_flow.py`
- **party_service()** (4 connections) — `server/tests/integration/test_party_flow.py`
- **test_party_invite_join_leave_disband_state_and_events()** (4 connections) — `server/tests/integration/test_party_flow.py`
- **test_party_leader_leaves_disbands()** (4 connections) — `server/tests/integration/test_party_flow.py`
- **event_bus()** (3 connections) — `server/tests/integration/test_party_flow.py`
- **test_party_post_init_includes_leader_in_members()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **test_party_post_init_preserves_other_members()** (3 connections) — `server/tests/unit/game/test_party_service.py`
- **.__post_init__()** (2 connections) — `server/game/party_service.py`
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
- *... and 57 more nodes in this community*

## Relationships

- [party game service](party_game_service.md) (14 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (8 shared connections)
- [item models rationale](item_models_rationale.md) (3 shared connections)
- [Room Broadcast](Room_Broadcast.md) (3 shared connections)
- [combat messaging services](combat_messaging_services.md) (3 shared connections)
- [command inventory factories](command_inventory_factories.md) (2 shared connections)
- [command service commands](command_service_commands.md) (1 shared connections)
- [connection manager realtime](connection_manager_realtime.md) (1 shared connections)
- [combat services messaging](combat_services_messaging.md) (1 shared connections)

## Source Files

- `server/events/event_types.py`
- `server/game/party_service.py`
- `server/tests/integration/test_party_flow.py`
- `server/tests/unit/game/test_party_service.py`

## Audit Trail

- EXTRACTED: 209 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*