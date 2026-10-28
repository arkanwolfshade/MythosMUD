# test_wearable_container_service.py

> 52 nodes · cohesion 0.09

## Key Concepts

- **PartyService** (47 connections) — `server/game/party_service.py`
- **_str_id()** (16 connections) — `server/game/party_service.py`
- **UUID** (15 connections)
- **Any** (11 connections)
- **._emit_party_updated()** (9 connections) — `server/game/party_service.py`
- **.accept_party_invite()** (8 connections) — `server/game/party_service.py`
- **.disband_party()** (8 connections) — `server/game/party_service.py`
- **.get_party_for_player()** (8 connections) — `server/game/party_service.py`
- **.kick_member()** (8 connections) — `server/game/party_service.py`
- **.remove_member()** (8 connections) — `server/game/party_service.py`
- **._send_result_to_player()** (8 connections) — `server/game/party_service.py`
- **.add_member()** (7 connections) — `server/game/party_service.py`
- **.create_party()** (7 connections) — `server/game/party_service.py`
- **.decline_party_invite()** (7 connections) — `server/game/party_service.py`
- **._expire_pending_invites()** (7 connections) — `server/game/party_service.py`
- **.request_party_invite()** (7 connections) — `server/game/party_service.py`
- **._notify_player_removed_from_party()** (6 connections) — `server/game/party_service.py`
- **.on_player_disconnect()** (6 connections) — `server/game/party_service.py`
- **._schedule_notification()** (6 connections) — `server/game/party_service.py`
- **.is_in_same_party()** (5 connections) — `server/game/party_service.py`
- **.is_leader()** (5 connections) — `server/game/party_service.py`
- **._notify_party_disbanded()** (5 connections) — `server/game/party_service.py`
- **._cancel_pending_invites_for()** (4 connections) — `server/game/party_service.py`
- **.get_party_members()** (4 connections) — `server/game/party_service.py`
- **._leave_party_on_disconnect()** (4 connections) — `server/game/party_service.py`
- *... and 27 more nodes in this community*

## Relationships

- [test_experience_procedures.py](test_experience_procedures.py.md) (12 shared connections)
- [LogAggregator](LogAggregator.md) (5 shared connections)
- [test_message_handlers.py](test_message_handlers.py.md) (3 shared connections)
- [TestNPCCombatLifecycle](TestNPCCombatLifecycle.md) (3 shared connections)
- [PlayerPositionService](PlayerPositionService.md) (2 shared connections)
- [item_catalog.sql](item_catalog.sql.md) (2 shared connections)
- [get_username_from_user](get_username_from_user.md) (1 shared connections)
- [ChatService](ChatService.md) (1 shared connections)
- [.publish_with_pool](publish_with_pool.md) (1 shared connections)
- [test_database_extended.py](test_database_extended.py.md) (1 shared connections)

## Source Files

- `server/game/party_service.py`

## Audit Trail

- EXTRACTED: 134 (92%)
- INFERRED: 11 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*