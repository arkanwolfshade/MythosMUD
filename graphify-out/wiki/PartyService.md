# PartyService

> 53 nodes

## Key Concepts

- **PartyService** (36 connections) — `server/game/party_service.py`
- **_str_id()** (16 connections) — `server/game/party_service.py`
- **UUID** (15 connections)
- **Any** (10 connections)
- **Party** (9 connections) — `server/game/party_service.py`
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
- **.__init__()** (6 connections) — `server/game/party_service.py`
- **._notify_player_removed_from_party()** (6 connections) — `server/game/party_service.py`
- **.on_player_disconnect()** (6 connections) — `server/game/party_service.py`
- **._schedule_notification()** (6 connections) — `server/game/party_service.py`
- **.is_in_same_party()** (5 connections) — `server/game/party_service.py`
- **.is_leader()** (5 connections) — `server/game/party_service.py`
- **.get_party_members()** (4 connections) — `server/game/party_service.py`
- **._send_party_invite_to_target()** (4 connections) — `server/game/party_service.py`
- *... and 28 more nodes in this community*

## Relationships

- [test_party_service.py](test_party_service.py.md) (6 shared connections)
- [ConnectionManager](ConnectionManager.md) (6 shared connections)
- [test_party_flow.py](test_party_flow.py.md) (6 shared connections)
- [ApplicationContainer](ApplicationContainer.md) (2 shared connections)
- [EventBus](EventBus.md) (2 shared connections)
- [test_container_bundles.py](test_container_bundles.py.md) (1 shared connections)
- [get_logger](get_logger.md) (1 shared connections)
- [build_event](build_event.md) (1 shared connections)

## Source Files

- `server/game/party_service.py`

## Audit Trail

- EXTRACTED: 127 (92%)
- INFERRED: 11 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*